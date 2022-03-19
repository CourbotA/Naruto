import numpy as np
import cv2 as cv

class Masque:
    def __init__(self, image_name):
        path = "BDD/" + image_name + ".bmp"
        self.image = cv.imread(path)

    def get_image(self):
        return self.image

    @set
    def set_image(self, image_name):
        path = "BDD/" + image_name + ".bmp"
        self.image = cv.imread(path)

    @staticmethod
    def min_threshold(): return 90
    @staticmethod
    def max_threshold(): return 255
    @staticmethod
    def space(): return 'HSV'
    @staticmethod
    def space(): return 'HSV'
    @staticmethod
    def nbr_classes(): return 180

    @classmethod
    def resize_image(cls, percentage):
        image = cls.get_image()
        dimensions = image.shape
        width = dimensions[0]; height = dimensions[1]
        # extract a window from the image
        window = image[100: int(width * 9 / 100), 100: int(height * 9 /10)]
        image_out = cv.resize(image, (int(width * percentage / 100), int(height * percentage / 100)))
        return image_out

    @classmethod
    def change_space_color(cls):
        image = cls.resize_image()
        image_changed = cv.cvtColor(image, eval("cv.COLOR_BGR2" + Masque.space()))
        (h, s, v) = cv.split(image_changed)
        v[:] = Masque.min_threshold()
        image_changed = cv.merge((v, v, s))
        image_changed = cv.cvtColor(image_changed, cv.COLOR_HSV2RGB)
        image_changed = cv.cvtColor(image_changed, cv.COLOR_RGB2GRAY)
        return image_changed

    @classmethod
    def fill_hole(cls,mask):
        contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        len_contour = len(contours)
        contour_list = []
        for i in range(len_contour):
            black_image = np.zeros_like(mask, np.uint8)  # create a black image
            img_contour = cv.drawContours(black_image, contours, i, (255, 255, 255), -1)
            contour_list.append(img_contour)
        out = sum(contour_list)
        return out

    @classmethod
    def mask(cls):
        kernel = np.ones((5, 5), np.float32) / 25
        mask = Masque.change_space_color()
        mask = cv.filter2D(mask, -1, kernel)
        mask = cv.erode(mask, None, iterations = 3)
        mask = cv.dilate(mask, None, iterations = 3)
        _, mask = cv.threshold(mask, Masque.min_threshold(), Masque.max_threshold(), cv.THRESH_BINARY)
        mask = Masque.fill_hole(mask)
        return mask






