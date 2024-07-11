import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf

# #####设置参数#######################
widthImg = 640
heightImg = 480
kernal = np.ones((5, 5))
minArea = 150

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    imgDial = cv2.dilate(imgCanny, kernal, iterations=2)        # 膨胀操作
    imgThres = cv2.erode(imgDial, kernal, iterations=1)         # 腐蚀操作
    return imgThres

def getContours(img):
    imgGet = np.array([[], []]) 
    x, y, w, h, xx, yy, ss = 0, 0, 10, 10, 20, 20, 10 #数据初始化
    contours, noUse = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 检索外部轮廓
    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])
    if len(contours) >= 8:
      del contours[3]  
      del contours[2] 
    # 遍历轮廓
    del contours[4]
    for index, count in enumerate(contours):
        area = cv2.contourArea(count)  
        if area > minArea:  #面积大于特定值则识别为数字或者符号
            if index== 3:
                #cv2.drawContours(imgCopy, count, -1, (0, 0, 0), 4)  #轮廓获取可视化在copy上
                peri = cv2.arcLength(count, True)  # 计算周长
                approx = cv2.approxPolyDP(count, 0.02 * peri, True)  
                x, y, w, h = cv2.boundingRect(approx)  

                a = (w+h)//2
                dd = abs((w-h)//2)      # 边框的差值

            # 这里直接取外接矩形的图像试试，就不要return坐标了
                imgGet = imgProcess[y-60:y+h+60, x-20:x+w+20]

                imgGet = cv2.copyMakeBorder(imgGet, 60 + dd, 60 + dd, 10, 10, cv2.BORDER_CONSTANT, value=[0, 0, 0])
                xx = x-10
                yy = y-dd-10
                ss = w+20
                
                # cv2.rectangle(imgCopy, (x-20, y-60), (x+w+20, y+h+60), (0, 255, 0), 2)
                # plt.imshow(cv2.cvtColor(imgCopy, cv2.COLOR_BGR2RGB))
                # plt.show()
                
                print(a+dd, w)

            else:    

              #cv2.drawContours(imgCopy, count, -1, (0, 0, 255), 4)  #轮廓获取可视化在copy上
              peri = cv2.arcLength(count, True)  # 计算周长
              approx = cv2.approxPolyDP(count, 0.02 * peri, True)  
              x, y, w, h = cv2.boundingRect(approx)  

              a = (w+h)//2
              dd = abs((w-h)//2)      # 边框的差值

            # 这里直接取外接矩形的图像试试，就不要return坐标了
              imgGet = imgProcess[y-90:y+h+90, x-20:x+w+20]

                    
              if w <= h:  # 得到一个正方形框，边界往外扩充10像素,黑色边框
                  imgGet = cv2.copyMakeBorder(imgGet, 30, 30, 30 + dd, 30 + dd, cv2.BORDER_CONSTANT,value=[0, 0, 0])
                  xx = x-dd-10
                  yy = y-10
                  ss = h+20
                  
                #   cv2.rectangle(imgCopy, (x-20, y-90), (x+w+20, y+h+90), (0, 255, 0), 2)    # 看看框选的效果，在imgCopy中
                #   plt.imshow(cv2.cvtColor(imgCopy, cv2.COLOR_BGR2RGB))
                #   plt.show()
                  
                  print(a+dd, h)
              else:               # 边界往外扩充10像素值
                  imgGet = cv2.copyMakeBorder(imgGet, 30 + dd, 30 + dd, 30, 30, cv2.BORDER_CONSTANT, value=[0, 0, 0])
                  xx = x-10
                  yy = y-dd-10
                  ss = w+20
                  
                #   cv2.rectangle(imgCopy, (x-20, y-90), (x+w+20, y+h+90), (0, 255, 0), 2)
                #   plt.imshow(cv2.cvtColor(imgCopy, cv2.COLOR_BGR2RGB))
                #   plt.show()
                  
                  print(a+dd, w)

            Temptuple = (imgGet,xx,yy,ss)       # 将图像及其坐标放在一个元组里面，然后再放进一个列表里面就可以访问了
            borderlist.append(Temptuple)

    return borderlist
            

img = cv2.imread("3.png",cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (widthImg, heightImg))
# cv2.imshow('Resized Image', resized_img)
# plt.show()
imgCopy = resized_img.copy()
borderlist = [] #边缘列表
imgProcess = preProcessing(resized_img)
# plt.imshow(cv2.cvtColor(imgProcess, cv2.COLOR_BGR2RGB))
# plt.show()

borderlist = getContours(imgProcess)

# for index, (imgGet, xx, yy, ss) in enumerate(borderlist):
#         # 使用matplotlib显示图像
#         plt.figure(figsize=(10, 10))  # 你可以根据需要调整图像大小
#         plt.imshow(cv2.cvtColor(imgGet, cv2.COLOR_BGR2RGB))
#         plt.title(f'Image {index}')
#         plt.axis('off')  # 关闭坐标轴显示
#         plt.show()

for index, (imgGet, xx, yy, ss) in enumerate(borderlist):
    letter = chr(ord('a') + index)
    filename = f'1{letter}.jpg'
    cv2.imwrite(filename, imgGet)
    
