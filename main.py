import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np


# Khởi tạo camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

# Detector
detector = HandDetector(maxHands=2)

# Biến trạng thái
mode = "menu"   # menu | single | multi
startGame = False
stateResult = False
timer = 0
scores = [0, 0]         # [AI, Player]
scores_multi = [0, 0]   # [Player1, Player2]
resultText = ""

while True:
    if mode == "menu":
        # Giao diện menu
        imgMenu = cv2.imread("Resources/Menu.png")
        imgMenu = cv2.resize(imgMenu, (1280, 720))

        cv2.imshow("Rock Paper Scissors", imgMenu)

        key = cv2.waitKey(1)
        if key == ord('1'):
            mode = "single"
            scores = [0, 0]
        elif key == ord('2'):
            mode = "multi"
            scores_multi = [0, 0]

    # ------------------- CHẾ ĐỘ SINGLE PLAYER -------------------
    elif mode == "single":
        imgBG = cv2.imread("Resources/BG.png")
        success, img = cap.read()
        if not success:
            continue

        imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
        imgScaled = imgScaled[:, 80:480]

        hands, img = detector.findHands(imgScaled)

        if startGame:
            if not stateResult:
                timer = time.time() - initialTime
                cv2.putText(imgBG, str(int(timer)), (605, 435),
                            cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

                if timer > 3:
                    stateResult = True
                    if hands:
                        playerMove = None
                        fingers = detector.fingersUp(hands[0])
                        if fingers == [0, 0, 0, 0, 0]:
                            playerMove = 1  # Búa
                        if fingers == [1, 1, 1, 1, 1]:
                            playerMove = 2  # Bao
                        if fingers == [0, 1, 1, 0, 0]:
                            playerMove = 3  # Kéo

                        randomNumber = random.randint(1, 3)
                        imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                        if (playerMove == 1 and randomNumber == 3) or \
                           (playerMove == 2 and randomNumber == 1) or \
                           (playerMove == 3 and randomNumber == 2):
                            scores[1] += 1
                            resultText = "You win"
                        elif (playerMove == 3 and randomNumber == 1) or \
                             (playerMove == 1 and randomNumber == 2) or \
                             (playerMove == 2 and randomNumber == 3):
                            scores[0] += 1
                            resultText = "AI Wins!"
                        else:
                            resultText = "Draw"

        imgBG[234:654, 795:1195] = imgScaled
        if stateResult:
            imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

        cv2.putText(imgBG, resultText, (550, 435),
                    cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
        cv2.putText(imgBG, str(scores[0]), (410, 215),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgBG, str(scores[1]), (1112, 215),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

        cv2.imshow("Rock Paper Scissors", imgBG)

        key = cv2.waitKey(1)
        if key == ord('s'):
            startGame = True
            initialTime = time.time()
            stateResult = False
            resultText = ""
        if key == ord('m'):  # quay lại menu
            mode = "menu"

    # ------------------- CHẾ ĐỘ MULTI PLAYER -------------------
    elif mode == "multi":
        # Mở 2 camera 1 lần khi vào chế độ multi
        cap1 = cv2.VideoCapture(0)  # Player 1 (laptop)
        cap2 = cv2.VideoCapture(1)  # Player 2 (Iriun)

        if not cap1.isOpened() or not cap2.isOpened():
            print("Không mở được 2 camera. Quay về menu.")
            # show message on menu image or just go back
            mode = "menu"
            try:
                cap1.release()
            except:
                pass
            try:
                cap2.release()
            except:
                pass
            continue

        # load layout
        imgBG = cv2.imread("Resources/BG2.png")
        imgBG = cv2.resize(imgBG, (941, 531))

        # 2 detector tách biệt (1 cho mỗi cam) để tránh trùng lặp trạng thái
        detector1 = HandDetector(maxHands=1, detectionCon=0.6)
        detector2 = HandDetector(maxHands=1, detectionCon=0.6)

        # vị trí & kích thước khung (theo thông tin bạn đã cung cấp)
        pos1 = (61, 172)  # top-left (x,y) player1
        pos2 = (587, 173)  # top-left (x,y) player2
        pw = 297  # width khung
        ph = 314  # height khung

        # trạng thái local cho chế độ multi
        resultText = ""
        player1Move, player2Move = None, None
        imgHand1, imgHand2 = None, None

        # vòng lặp độc lập cho chế độ multi
        while True:
            success1, frame1 = cap1.read()
            success2, frame2 = cap2.read()

            frame_ok = True
            if not success1 or frame1 is None:
                frame_ok = False
            if not success2 or frame2 is None:
                frame_ok = False

            imgBG_copy = imgBG.copy()

            if not frame_ok:
                cv2.putText(imgBG_copy, "Khong the truy cap camera!", (250, 300),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                cv2.imshow("Rock Paper Scissors", imgBG_copy)
                if cv2.waitKey(1) & 0xFF == ord('m'):
                    # trở về menu
                    mode = "menu"
                    cap1.release()
                    cap2.release()
                    break
                continue


            # Nếu muốn, flip để giống gương (tùy camera): uncomment nếu cần
            # frame1 = cv2.flip(frame1, 1)
            # frame2 = cv2.flip(frame2, 1)

            # --- PHẦN NHẬN DIỆN (an toàn với nhiều phiên bản cvzone) ---
            # Một số phiên bản trả (hands, img) hoặc (img, hands). Xử lý chung:
            def find_hands_safe(det, frm):
                out = det.findHands(frm, draw=False)
                # out có thể là tuple/list (hands, img) hoặc (img, hands) — ta phát hiện kiểu
                if isinstance(out, tuple) or isinstance(out, list):
                    a, b = out
                    if isinstance(a, list):  # a là hands
                        return a, b
                    elif isinstance(b, list):  # b là hands
                        return b, a
                    else:
                        # fallback
                        return a, b
                else:
                    # fallback: không đúng format
                    return [], frm


            hands1, img1_drawn = find_hands_safe(detector1, frame1.copy())
            hands2, img2_drawn = find_hands_safe(detector2, frame2.copy())

            # --- resize thumbnail và dán vào background ---
            try:
                thumb1 = cv2.resize(frame1, (pw, ph))
                thumb2 = cv2.resize(frame2, (pw, ph))
            except:
                thumb1 = np.zeros((ph, pw, 3), dtype=np.uint8)
                thumb2 = np.zeros((ph, pw, 3), dtype=np.uint8)

            imgBG_copy[pos1[1]:pos1[1] + ph, pos1[0]:pos1[0] + pw] = thumb1
            imgBG_copy[pos2[1]:pos2[1] + ph, pos2[0]:pos2[0] + pw] = thumb2


            # --- LOGIC GAME: countdown 3 -> 2 -> 1 ---
            if startGame:
                if not stateResult:
                    timer = time.time() - initialTime
                    countdown = 3 - int(timer)  # 3,2,1, then <=0
                    if countdown > 0:
                        # Hiển thị countdown rõ ràng ở giữa
                        cv2.putText(imgBG_copy, str(countdown), (442, 335),
                                    cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 5)
                    else:
                        # Hết giờ -> xác định cử chỉ
                        stateResult = True

                        # reset trước khi lấy kết quả
                        player1Move, player2Move = None, None

                        # Lấy cử chỉ P1
                        if hands1:
                            try:
                                fingers1 = detector1.fingersUp(hands1[0])
                            except Exception as e:
                                fingers1 = []
                            # kiểm tra các mẫu (chú ý: trả về [1,0,..] hoặc [0,1,..])
                            if fingers1 == [0, 0, 0, 0, 0]:
                                player1Move = 1
                            elif fingers1 == [1, 1, 1, 1, 1]:
                                player1Move = 2
                            elif fingers1 == [0, 1, 1, 0, 0]:
                                player1Move = 3

                        # Lấy cử chỉ P2
                        if hands2:
                            try:
                                fingers2 = detector2.fingersUp(hands2[0])
                            except Exception as e:
                                fingers2 = []
                            if fingers2 == [0, 0, 0, 0, 0]:
                                player2Move = 1
                            elif fingers2 == [1, 1, 1, 1, 1]:
                                player2Move = 2
                            elif fingers2 == [0, 1, 1, 0, 0]:
                                player2Move = 3

                        # # Nếu muốn debug: hiển thị bộ fingers (ngắn)
                        # if hands1 and 'lmList' in hands1[0]:
                        #     txt1 = str(detector1.fingersUp(hands1[0]))
                        #     cv2.putText(imgBG_copy, txt1, (pos1[0], pos1[1] + ph + 20),
                        #                 cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 1)
                        # if hands2 and 'lmList' in hands2[0]:
                        #     txt2 = str(detector2.fingersUp(hands2[0]))
                        #     cv2.putText(imgBG_copy, txt2, (pos2[0], pos2[1] + ph + 20),
                        #                 cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 1)

                        # Overlay hình biểu tượng move lên màn hình BG (ví dụ ở giữa khung)
                        if player1Move is not None:
                            imgHand1 = cv2.imread(f'Resources/{player1Move}.png', cv2.IMREAD_UNCHANGED)
                            # đặt gần giữa bên trái (tinh chỉnh tuỳ bạn)
                            imgBG_copy = cvzone.overlayPNG(imgBG_copy, imgHand1, (pos1[0] + 60, pos1[1] + 200))
                        if player2Move is not None:
                            imgHand2 = cv2.imread(f'Resources/{player2Move}.png', cv2.IMREAD_UNCHANGED)
                            imgBG_copy = cvzone.overlayPNG(imgBG_copy, imgHand2, (pos2[0] + 0, pos2[1] + 200))

                        # So sánh, cập nhật điểm — chỉ khi cả hai có kết quả
                        if player1Move is not None and player2Move is not None:
                            if (player1Move == 1 and player2Move == 3) or \
                                    (player1Move == 2 and player2Move == 1) or \
                                    (player1Move == 3 and player2Move == 2):
                                scores_multi[0] += 1
                                resultText = "Player 1 Wins"
                            elif (player2Move == 1 and player1Move == 3) or \
                                    (player2Move == 2 and player1Move == 1) or \
                                    (player2Move == 3 and player1Move == 2):
                                scores_multi[1] += 1
                                resultText = "Player 2 Wins"
                            else:
                                resultText = "Draw"
                        else:
                            # Nếu 1 trong 2 không detect được cử chỉ:
                            resultText = "No gesture detected for one player"

            # Hiển thị trạng thái & điểm
            # cv2.putText(imgBG_copy, resultText, (400, 150),
            #             cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 0), 3)
            cv2.putText(imgBG_copy, str(scores_multi[0]), (297, 165),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 6)
            cv2.putText(imgBG_copy, str(scores_multi[1]), (823, 165),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 6)

            cv2.imshow("Rock Paper Scissors", imgBG_copy)

            # ---- phím điều khiển ----
            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):
                # bắt đầu 1 ván mới
                startGame = True
                initialTime = time.time()
                stateResult = False
                resultText = ""
                player1Move, player2Move = None, None
            if key == ord('m'):
                # quay lại menu
                mode = "menu"
                cap1.release()
                cap2.release()
                break
