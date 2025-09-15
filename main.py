# import random
# import cv2 #OpenCV: xử lý ảnh, video, đọc camera, hiện thị cửa sổ, xử lý ảnh nền
# import cvzone # thư viện hỗ trợ built-in trên openCV
# from cvzone.HandTrackingModule import HandDetector
# import time
#
# #khởi tạo camera
# cap = cv2.VideoCapture(0) #-> mở webcam mặc định là 0
# cap.set(3, 640) #→ đặt chiều rộng frame = 640 px.
# cap.set(4, 480) #→ đặt chiều cao frame = 480 px
#
# detector = HandDetector(maxHands=1) # -> chỉ nhận diện tối đa 1 bàn tay (của người chơi ) & HandDetector là class của cvzone
#
# timer = 0  # biến đếm thời gian cho mỗi lượt chơi
# stateResult = False # = False → đang đếm thời gian; = True → đã có kết quả.
# startGame = False # False → chưa bắt đầu; True → đang chơi.
# scores = [0, 0]  # lưu điểm [AI, Player]
#
# while True:
#     imgBG = cv2.imread("Resources/BG.png") # ảnh nền (layout game)
#     success, img = cap.read() # đọc một frame từ webcam, success = true nếu lấy được ảnh, img= frame gốc từ camera
#
#     #-> cách chia tỷ lệ trên máy
#     imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
#     imgScaled = imgScaled[:, 80:480]
#
#     # Find Hands
#     hands, img = detector.findHands(imgScaled)  # with draw
#
#     if startGame:
#         if stateResult is False:
#             timer = time.time() - initialTime
#             cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
#
#             if timer > 3:
#                 stateResult = True
#                 timer = 0
#                 if hands:
#                     playerMove = None
#                     hand = hands[0]
#                     fingers = detector.fingersUp(hand)
#                     if fingers == [0, 0, 0, 0, 0]:
#                         playerMove = 1
#                     if fingers == [1, 1, 1, 1, 1]:
#                         playerMove = 2
#                     if fingers == [0, 1, 1, 0, 0]:
#                         playerMove = 3
#
#                     randomNumber = random.randint(1, 3)
#                     imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
#                     imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
#
#                     # Player Wins
#                     if (playerMove == 1 and randomNumber == 3) or \
#                             (playerMove == 2 and randomNumber == 1) or \
#                             (playerMove == 3 and randomNumber == 2):
#                         scores[1] += 1
#
#                     # AI Wins
#                     if (playerMove == 3 and randomNumber == 1) or \
#                             (playerMove == 1 and randomNumber == 2) or \
#                             (playerMove == 2 and randomNumber == 3):
#                         scores[0] += 1
#
#     imgBG[234:654, 795:1195] = imgScaled
#
#     if stateResult:
#         imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
#
#     cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
#     cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
#
#     # cv2.imshow("Image", img)
#     cv2.imshow("BG", imgBG)
#     # cv2.imshow("Scaled", imgScaled)
#
#     key = cv2.waitKey(1)
#     if key == ord('s'):
#         startGame = True
#         initialTime = time.time()
#         stateResult = False

# import random
# import cv2 #OpenCV: xử lý ảnh, video, đọc camera, hiện thị cửa sổ, xử lý ảnh nền
# import cvzone # thư viện hỗ trợ built-in trên openCV
# from cvzone.HandTrackingModule import HandDetector
# import time
#
# #khởi tạo camera
# cap = cv2.VideoCapture(0) #-> mở webcam mặc định là 0
# cap.set(3, 640) #→ đặt chiều rộng frame = 640 px.
# cap.set(4, 480) #→ đặt chiều cao frame = 480 px
#
# detector = HandDetector(maxHands=1) # -> chỉ nhận diện tối đa 1 bàn tay (của người chơi ) & HandDetector là class của cvzone
#
# timer = 0
# stateResult = False # = False → đang đếm thời gian; = True → đã có kết quả.
# startGame = False # False → chưa bắt đầu; True → đang chơi.
# scores = [0, 0]  # lưu điểm [AI, Player]
# resultText = ""
# while True:
#     imgBG = cv2.imread("Resources/BG.png") # ảnh nền (layout game)
#     success, img = cap.read() # đọc một frame từ webcam, success = true nếu lấy được ảnh, img= frame gốc từ camera
#
#     #-> cách chia tỷ lệ trên máy
#     imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
#     imgScaled = imgScaled[:, 80:480]
#
#     # Find Hands
#     hands, img = detector.findHands(imgScaled)  # with draw
#
#     if startGame:
#         if stateResult is False:
#             timer = time.time() - initialTime
#             cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
#
#             if timer > 3:
#                 stateResult = True
#                 timer = 0
#
#                 if hands:
#                     playerMove = None
#                     hand = hands[0]
#                     fingers = detector.fingersUp(hand)
#                     if fingers == [0, 0, 0, 0, 0]:
#                         playerMove = 1
#                     if fingers == [1, 1, 1, 1, 1]:
#                         playerMove = 2
#                     if fingers == [0, 1, 1, 0, 0]:
#                         playerMove = 3
#
#                     randomNumber = random.randint(1, 3)
#                     imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
#                     imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
#
#                     # Player Wins
#                     if (playerMove == 1 and randomNumber == 3) or \
#                             (playerMove == 2 and randomNumber == 1) or \
#                             (playerMove == 3 and randomNumber == 2):
#                         scores[1] += 1
#                         resultText = "You win"
#                     # AI Wins
#                     elif (playerMove == 3 and randomNumber == 1) or \
#                             (playerMove == 1 and randomNumber == 2) or \
#                             (playerMove == 2 and randomNumber == 3):
#                         scores[0] += 1
#                         resultText = "AI Wins!"
#                     else:
#
#                         resultText = "Draw"
#                 else:
#                     resultText = "AI Wins!"
#                     scores[0] += 1
#                     randomNumber = random.randint(1, 3)
#                     imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
#                     imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
#
#     imgBG[234:654, 795:1195] = imgScaled
#
#     if stateResult:
#         imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
#     cv2.putText(imgBG, resultText, (550, 435), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
#     cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
#     cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
#
#     # cv2.imshow("Image", img)
#     cv2.imshow("BG", imgBG)
#     # cv2.imshow("Scaled", imgScaled)
#
#     key = cv2.waitKey(1)
#     if key == ord('s'):
#         startGame = True
#         initialTime = time.time()
#         stateResult = False
#         resultText = ""

# def fit_to_box(img, box_w, box_h, mode="center"):
#     """
#     Scale + crop ảnh từ camera để khớp đúng với khung (box_w x box_h).
#     mode = "center" -> crop giữa
#     mode = "top"    -> ưu tiên giữ phần trên (ví dụ khuôn mặt)
#     """
#     h, w, _ = img.shape
#     scale = max(box_w / w, box_h / h)  # scale sao cho ảnh >= khung
#     new_w, new_h = int(w * scale), int(h * scale)
#     img_resized = cv2.resize(img, (new_w, new_h))
#
#     # Crop
#     if mode == "center":
#         x_start = (new_w - box_w) // 2
#         y_start = (new_h - box_h) // 2
#     elif mode == "top":  # giữ phần trên (đầu, mặt)
#         x_start = (new_w - box_w) // 2
#         y_start = 0
#     else:
#         x_start, y_start = 0, 0
#
#     img_cropped = img_resized[y_start:y_start+box_h, x_start:x_start+box_w]
#     return img_cropped


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
        cap1 = cv2.VideoCapture(0)  # Player 1 (Laptop cam)
        cap2 = cv2.VideoCapture(1)  # Player 2 (Iriun cam)

        imgBG = cv2.imread("Resources/BG2.png")
        imgBG = cv2.resize(imgBG, (941, 531))

        detector1 = HandDetector(maxHands=1)
        detector2 = HandDetector(maxHands=1)

        # Kích thước khung hiển thị
        ph, pw = 314, 297
        pos1 = (61, 172)
        pos2 = (587, 173)

        resultText = ""

        while True:
            success1, frame1 = cap1.read()
            success2, frame2 = cap2.read()

            imgBG_copy = imgBG.copy()

            if not success1 or not success2:
                cv2.putText(imgBG_copy, "Khong the truy cap camera!", (300, 360),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                cv2.imshow("Rock Paper Scissors", imgBG_copy)
                cv2.waitKey(1)
                continue

            # ----------- Dùng ảnh gốc để detect ----------
            hands1, _ = detector1.findHands(frame1, flipType=False)
            hands2, _ = detector2.findHands(frame2, flipType=False)

            # ----------- Sau đó mới resize để ghép BG ----------
            img1_resized = cv2.resize(frame1, (pw, ph))
            img2_resized = cv2.resize(frame2, (pw, ph))

            imgBG_copy[pos1[1]:pos1[1] + ph, pos1[0]:pos1[0] + pw] = img1_resized
            imgBG_copy[pos2[1]:pos2[1] + ph, pos2[0]:pos2[0] + pw] = img2_resized

            player1Move, player2Move = None, None

            if startGame:
                if not stateResult:
                    timer = time.time() - initialTime
                    countdown = 4 - int(timer)  # hiển thị 3 → 2 → 1

                    if 1 <= countdown <= 3:
                        cv2.putText(imgBG_copy, str(countdown), (600, 120),
                                    cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
                    elif countdown <= 0:
                        stateResult = True

                        # Player1
                        if hands1:
                            fingers1 = detector1.fingersUp(hands1[0])
                            if fingers1 == [0, 0, 0, 0, 0]: player1Move = 1
                            if fingers1 == [1, 1, 1, 1, 1]: player1Move = 2
                            if fingers1 == [0, 1, 1, 0, 0]: player1Move = 3

                        # Player2
                        if hands2:
                            fingers2 = detector2.fingersUp(hands2[0])
                            if fingers2 == [0, 0, 0, 0, 0]: player2Move = 1
                            if fingers2 == [1, 1, 1, 1, 1]: player2Move = 2
                            if fingers2 == [0, 1, 1, 0, 0]: player2Move = 3

                        # Overlay hình bàn tay
                        if player1Move:
                            imgHand1 = cv2.imread(f'Resources/{player1Move}.png', cv2.IMREAD_UNCHANGED)
                            imgBG_copy = cvzone.overlayPNG(imgBG_copy, imgHand1, (200, 350))
                        if player2Move:
                            imgHand2 = cv2.imread(f'Resources/{player2Move}.png', cv2.IMREAD_UNCHANGED)
                            imgBG_copy = cvzone.overlayPNG(imgBG_copy, imgHand2, (900, 350))

                        # So sánh kết quả
                        if player1Move and player2Move:
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

            # Hiển thị kết quả và điểm số
            cv2.putText(imgBG_copy, resultText, (500, 150),
                        cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)

            cv2.putText(imgBG_copy, str(scores_multi[0]), (300, 120),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
            cv2.putText(imgBG_copy, str(scores_multi[1]), (1000, 120),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

            cv2.imshow("Rock Paper Scissors", imgBG_copy)

            key = cv2.waitKey(1)
            if key == ord('s'):
                startGame = True
                initialTime = time.time()
                stateResult = False
                resultText = ""
            if key == ord('m'):
                mode = "menu"
                cap1.release()
                cap2.release()
                break
