import numpy as np
import cv2 as cv

class Masquecalculator:
    def __init__(self, image_name):
        path = image_name
        self.image = cv.imread(path)
        print(path)

    def get_image(self):
        return self.image

    def set_image(self, image_name):
        path = image_name
        self.image = cv.imread(path)

    def set_image_raw(self, image):
        self.image = image

    @staticmethod
    def min_threshold(): return 90
    @staticmethod
    def max_threshold(): return 255
    @staticmethod
    def space(): return 'HSV'
    @staticmethod
    def nbr_classes(): return 180

    def resize_image(self):
        image = self.image
        dimensions = image.shape
        width = dimensions[0]; height = dimensions[1]
        # extract a window from the image
        window = image[100: int(width * 9 / 100), 100: int(height * 9 /10)]
        image_out = cv.resize(image, (int(width * 50 / 100), int(height * 50 / 100)))
        return image_out

    def change_space_color(self):
        image = self.resize_image()
        image_changed = cv.cvtColor(image, eval("cv.COLOR_BGR2" + Masquecalculator.space()))
        (h, s, v) = cv.split(image_changed)
        v[:] = Masquecalculator.min_threshold()
        image_changed = cv.merge((v, v, s))
        image_changed = cv.cvtColor(image_changed, cv.COLOR_HSV2RGB)
        image_changed = cv.cvtColor(image_changed, cv.COLOR_RGB2GRAY)
        return image_changed

    def fill_hole(self,mask):
        contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        len_contour = len(contours)
        contour_list = []
        for i in range(len_contour):
            black_image = np.zeros_like(mask, np.uint8)  # create a black image
            img_contour = cv.drawContours(black_image, contours, i, (255, 255, 255), -1)
            contour_list.append(img_contour)
        out = sum(contour_list)
        return out

    def mask(self):
        kernel = np.ones((5, 5), np.float32) / 25
        mask = self.change_space_color()
        mask = cv.filter2D(mask, -1, kernel)
        mask = cv.erode(mask, None, iterations = 3)
        mask = cv.dilate(mask, None, iterations = 3)
        _, mask = cv.threshold(mask, self.min_threshold(), self.max_threshold(), cv.THRESH_BINARY)
        mask = self.area_opening(mask)
        mask = self.fill_hole(mask)
        return mask

    def area_opening(self, mask):
        nb_components, output, stats, centroids = cv.connectedComponentsWithStats(mask, connectivity=8)

        sizes = stats[1:, -1]
        nb_components = nb_components - 1

        # minimum size to keep an element
        min_size = np.sum(mask > 0) * 0.5

        # answer image as a np.array
        mask2 = np.zeros((output.shape))

        # for every component in the image, keep it only if it's above min_size
        for i in range(0, nb_components):
            if sizes[i] >= min_size:
                mask2[output == i + 1] = 255

        mask2 = mask2.astype(np.uint8)

        return mask2




