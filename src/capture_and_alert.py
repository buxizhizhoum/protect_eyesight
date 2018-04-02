#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import cv2

from capture_image import capture_image
from face_recognition import faces_size

xml_path = "/usr/local/lib/python2.7/dist-packages/cv2/data/haarcascade_frontalface_default.xml"
limit = 222


camera = cv2.VideoCapture(0)


while True:
    ret, image = capture_image(camera)
    if ret is True:
        faces_sizes = faces_size(image, xml_path)
        # if there are many faces in image?
        for face_size in faces_sizes:
            print face_size
            width, height = face_size
            if width > limit or height > limit:
                print "you are too close to screen!"
    time.sleep(1)
