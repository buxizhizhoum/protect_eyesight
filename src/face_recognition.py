#!/usr/bin/python
# -*- coding: utf-8 -*-


import cv2


def face_recognize(image_path, classifier_path, color=None, width=None):
    """
    recognize faces in a image specified by image_path, return image with all
    faces in rectangles.
    :param image_path:
    :param classifier_path:
    :param color:
    :param width:
    :return:
    """
    # todo: ignore small faces. default classifier
    color = (255, 255, 255) if color is None else color
    width = 3 if width is None else width

    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(classifier_path)
    faces = face_cascade.detectMultiScale(image_gray, 1.03, 5)
    for (x, y, w, h) in faces:
        img_frame = cv2.rectangle(image, (x, y), (x + w, y + h), color, width)
        # roi_gray = image_gray[y:y + h, x: x + w]
        # roi_color = image[y:y + h, x: x + w]
        yield img_frame

    # cv2.imshow("image", img_frame)
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def faces_size(image, classifier_path):
    """
    recognize faces in a figure specified by the image_path.
    :param image: image
    :param classifier_path: path of pre-trained opencv classifier
    :return: generator from which width and height of faces could be extracted.
    """
    # todo: default classifier.
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(classifier_path)
    faces = face_cascade.detectMultiScale(image_gray, 1.03, 5)
    for (x, y, w, h) in faces:
        yield (w, h)


if __name__ == "__main__":
    img_path = "../figures/angelebaby.jpeg"
    # the path of pre-trained classifier should be absolute path.
    xml_path = "/usr/local/lib/python2.7/dist-packages/cv2/data/haarcascade_frontalface_default.xml"

    faces = face_recognize(image_path=img_path, classifier_path=xml_path)
    # for face in faces:
    #     cv2.imshow("image", face)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    img = cv2.imread(img_path)
    faces_size = faces_size(img, xml_path)
    for face_size in faces_size:
        print face_size
