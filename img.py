import cv2
# cv2.IMREAD_COLOR (기본값)
# cv2.IMREAD_GRAYSCALE
# cv2.IMREAD_UNCHANGED
img = cv2.imread('img/cat1.jpg') # 이미지 읽어오기

#Shape
#이미지의 height, width, channel 정보
print(img.shape)

cv2.imshow('img', img) # img라는 이름의 창을 img를 표시
key = cv2.waitKey(0) # 지정된 시간동안 사용자 키 입력 대기
print(key)

cv2.destroyAllWindows() #모든 창 닫기


