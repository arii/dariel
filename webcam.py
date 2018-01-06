import cv2

def show_webcam():
    cam = cv2.VideoCapture(0)
    i = 0
    while True:
        ret_val, img = cam.read()
        cv2.imshow('my webcam', img)
        cv2.waitKey(1)
        i += 1

        if i%100==0:
            cv2.imwrite("ari%d.png"%i, img)
        if i > 1000:
            break


def main():
    show_webcam()

if __name__ == '__main__':
    main()
