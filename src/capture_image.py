#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2


def capture_image(camera=None):
    if camera is None:
        camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    return ret, frame
    # cv2.imshow("test", frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    ret, frame = capture_image()
