import cv2

movie_file = "movie/test.mp4"

vfile = cv2.VideoCapture(movie_file)

if vfile.isOpened():
    while True:
        vret, img = vfile.read()
        if vret:
            cv2.imshow(movie_file, img)
            cv2.waitKey(25)
        else:
            break
else:
    print("파일을 열수 없습니다.")

vfile.release()
cv2.destroyAllWindows()