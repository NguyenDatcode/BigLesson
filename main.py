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

import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

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
        imgBG = cv2.imread("Resources/BG2.png")
        success, img = cap.read()
        imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
        imgScaled = imgScaled[:, 80:480]

        hands, img = detector.findHands(imgScaled)

        if startGame:
            if not stateResult:
                timer = time.time() - initialTime
                # Đồng hồ đếm ngược
                cv2.putText(imgBG, str(int(timer)),
                            (int(605 * 0.737), int(435 * 0.737)),  # (445, 320)
                            cv2.FONT_HERSHEY_PLAIN, 6 * 0.737,
                            (255, 0, 255), 4)

                if timer > 3:
                    stateResult = True
                    player1Move, player2Move = None, None
                    if len(hands) == 2:
                        hand1, hand2 = hands[0], hands[1]
                        fingers1 = detector.fingersUp(hand1)
                        fingers2 = detector.fingersUp(hand2)

                        # Player1
                        if fingers1 == [0, 0, 0, 0, 0]: player1Move = 1
                        if fingers1 == [1, 1, 1, 1, 1]: player1Move = 2
                        if fingers1 == [0, 1, 1, 0, 0]: player1Move = 3

                        # Player2
                        if fingers2 == [0, 0, 0, 0, 0]: player2Move = 1
                        if fingers2 == [1, 1, 1, 1, 1]: player2Move = 2
                        if fingers2 == [0, 1, 1, 0, 0]: player2Move = 3

                        # Overlay hình bàn tay Player1 và Player2
                        if player1Move:
                            imgHand1 = cv2.imread(f'Resources/{player1Move}.png', cv2.IMREAD_UNCHANGED)
                            imgBG = cvzone.overlayPNG(imgBG, imgHand1,
                                                      (int(149 * 0.737), int(310 * 0.737)))  # (110, 228)
                        if player2Move:
                            imgHand2 = cv2.imread(f'Resources/{player2Move}.png', cv2.IMREAD_UNCHANGED)
                            imgBG = cvzone.overlayPNG(imgBG, imgHand2,
                                                      (int(795 * 0.737), int(310 * 0.737)))  # (586, 228)

                        # So sánh kết quả
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

        # Gán camera preview vào giữa
        # Gốc cũ: imgBG[234:654, 795:1195] = imgScaled
        y1, y2 = int(234 * 0.737), int(654 * 0.737)  # (172, 482)
        x1, x2 = int(795 * 0.737), int(1195 * 0.737)  # (586, 880)
        imgBG[y1:y2, x1:x2] = cv2.resize(imgScaled, (x2 - x1, y2 - y1))

        # Hiển thị kết quả và điểm số
        cv2.putText(imgBG, resultText,
                    (int(550 * 0.737), int(435 * 0.737)),  # (405, 320)
                    cv2.FONT_HERSHEY_DUPLEX, 2 * 0.737,
                    (0, 255, 255), 3)

        cv2.putText(imgBG, str(scores_multi[0]),
                    (int(410 * 0.737), int(215 * 0.737)),  # (302, 158)
                    cv2.FONT_HERSHEY_PLAIN, 4 * 0.737,
                    (255, 255, 255), 6)

        cv2.putText(imgBG, str(scores_multi[1]),
                    (int(1112 * 0.737), int(215 * 0.737)),  # (820, 158)
                    cv2.FONT_HERSHEY_PLAIN, 4 * 0.737,
                    (255, 255, 255), 6)

        cv2.imshow("Rock Paper Scissors", imgBG)

        key = cv2.waitKey(1)
        if key == ord('s'):
            startGame = True
            initialTime = time.time()
            stateResult = False
            resultText = ""
        if key == ord('m'):
            mode = "menu"

