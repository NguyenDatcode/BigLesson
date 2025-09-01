import random
import cv2 #OpenCV: xử lý ảnh, video, đọc camera, hiện thị cửa sổ, xử lý ảnh nền
import cvzone # thư viện hỗ trợ built-in trên openCV
from cvzone.HandTrackingModule import HandDetector
import time

#khởi tạo camera
cap = cv2.VideoCapture(0) #-> mở webcam mặc định là 0
cap.set(3, 640) #→ đặt chiều rộng frame = 640 px.
cap.set(4, 480) #→ đặt chiều cao frame = 480 px

detector = HandDetector(maxHands=1) # -> chỉ nhận diện tối đa 1 bàn tay (của người chơi ) & HandDetector là class của cvzone

timer = 0
stateResult = False # = False → đang đếm thời gian; = True → đã có kết quả.
startGame = False # False → chưa bắt đầu; True → đang chơi.
scores = [0, 0]  # lưu điểm [AI, Player]
 
while True:
    imgBG = cv2.imread("Resources/BG.png") # ảnh nền (layout game)
    success, img = cap.read() # đọc một frame từ webcam, success = true nếu lấy được ảnh, img= frame gốc từ camera

    #-> cách chia tỷ lệ trên máy
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Find Hands
    hands, img = detector.findHands(imgScaled)  # with draw

    if startGame:
        if stateResult is False:
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3

                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # Player Wins
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1

                    # AI Wins
                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1

    imgBG[234:654, 795:1195] = imgScaled

    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    # cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    # cv2.imshow("Scaled", imgScaled)

    key = cv2.waitKey(1)
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False