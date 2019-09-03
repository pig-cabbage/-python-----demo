# import pylab
# import imageio
# # imageio.plugins.ffmpeg.download()
# import skimage
# import numpy as np
#
# filename='04f67d8ec99f456a18c0216304ffe1d2.wmv'
# vid = imageio.get_reader(filename, 'ffmpeg')
# for num,im in enumerate(vid):
# #image的类型是mageio.core.util.Image可用下面这一注释行转换为arrary
#     print(im.mean())
#     image = skimage.img_as_float(im).astype(np.float64)
#     fig = pylab.figure()
#     fig.suptitle('image #{}'.format(num), fontsize=20)
#     pylab.imshow(im)
# pylab.show()
import asynchat

import cv2

video_full_path = "04f67d8ec99f456a18c0216304ffe1d2.wmv"
cap = cv2.VideoCapture(0)
#获取视频每一帧的长和高，用于下面构建视频文件的句柄
print(cap.get(3))
print(cap.get(4))
cap.isOpened()
frame_count = 1
success = True
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 24.0, (640,480),True)
while (success):
    success, frame = cap.read()
    #获取每一帧图片并存储
    # if(success==True):
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow("shiyan", gray)
    #     params = []
    #     params.append(1)
    #     cv2.imwrite("video4" + "_%d.jpg" % frame_count, frame, params)
    #     frame_count=frame_count+1
    #获取每一帧图片，经过处理后存入写出视频文件的句柄
    if success == True:
        # 在这里对每一帧图片进行处理
        # frame = cv2.flip(frame, 0)水平旋转
        # 90度旋转
        # rows, cols = frame.shape[:2]
        # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 270, 1)
        # frame = cv2.warpAffine(frame, M, (cols, rows))
        # out.write(frame)
    else:
        break

cap.release()
out.release()


import asynchat