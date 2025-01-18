import cv2

cam = cv2.VideoCapture(0)

res , img = cam.read()

if res:
    cv2.imshow("PIC",img)

    height, width, channels = img.shape
    num_pixels = height * width
    print(f"Image Dimensions: {width}x{height}")
    print(f"Total number of pixels: {num_pixels}")
    
    cv2.imwrite("PIC_PNG.png",img)
    cv2.imwrite("PIC_JPG.jpg",img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No image detected")

cam.release()
