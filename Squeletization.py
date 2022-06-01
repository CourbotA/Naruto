import numpy as np
import cv2 as cv
import math


class Squeletizer:

    def count_by_region(self,skeleton):
        width = math.floor(len(skeleton) * 0.25)
        height = math.floor(len(skeleton[0]) * 0.25)
        size = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(4):
            x = i * width
            for j in range(4):
                y = j * height
                region_frame = skeleton[x:x + width, y:y + height]
                contours = cv.findContours(region_frame.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                size[i * 4 + j] = len(contours[0])
        return size

    def area_opening(self,mask):
        nb_components, output, stats, centroids = cv.connectedComponentsWithStats(mask, connectivity=8)

        sizes = stats[1:, -1]
        nb_components = nb_components - 1

        # minimum size to keep an elemen
        min_size = np.sum(mask > 0) * 0.001;

        # answer image as a np.array
        mask2 = np.zeros((output.shape))

        # for every component in the image, keep it only if it's above min_size
        for i in range(0, nb_components):
            if sizes[i] >= min_size:
                mask2[output == i + 1] = 255

        mask2 = mask2.astype(np.uint8)

        return mask2

    def squel(self,img):

        # Threshold the image
        ret, img = cv.threshold(img, 127, 255, 0)

        # Step 1: Create an empty skeleton
        size = np.size(img)
        skel = np.zeros(img.shape, np.uint8)

        # Get a Cross Shaped Kernel
        element = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))

        # Repeat steps 2-4
        while True:
            # Step 2: Open the image
            open = cv.morphologyEx(img, cv.MORPH_OPEN, element)
            # Step 3: Substract open from the original image
            temp = cv.subtract(img, open)
            # Step 4: Erode the original image and refine the skeleton
            eroded = cv.erode(img, element)
            skel = cv.bitwise_or(skel, temp)
            img = eroded.copy()
            # Step 5: If there are no white pixels left ie.. the image has been completely eroded, quit the loop
            if cv.countNonZero(img) == 0:
                break

        return skel

    def calculate(self, ROI, Mask):
        edges = cv.Canny(ROI, 50, 250);
        kernel = np.ones((5, 5), np.uint8);
        dilated_edges = cv.dilate(edges, kernel, iterations=2);

#        masque = cv.cvtColor(Mask, cv.COLOR_RGB2GRAY)
        Asquel = Mask - dilated_edges

        skeleton = self.squel(Asquel)
        skeleton = self.area_opening(skeleton)
        sizes = self.count_by_region(skeleton)

        return sizes
