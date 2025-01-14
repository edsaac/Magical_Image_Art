import cv2
import numpy as np
from PIL import Image

#########################################################################
# FUNCTIONS FOR APPLYING VARIETY OF EFFECTS


def pop_art(original):

    original = np.array(original)

    # import the image as greyscale
    image = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # set colours (BGR)
    background_colour = [247, 19, 217]
    dots_colour = (13, 10, 52)

    # set the max dots (on the longest side of the image)
    max_dots = 170

    # extract dimensions
    image_height, image_width = image.shape

    # down size to number of dots
    if image_height == max(image_height, image_width):
        downsized_image = cv2.resize(image, (int(image_height*(max_dots/image_width)), max_dots))
    else:
        downsized_image = cv2.resize(image, (max_dots, int(image_height*(max_dots/image_width))))

    # extract dimensions of new image
    downsized_image_height, downsized_image_width = downsized_image.shape

    # final image size
    multiplier = 30

    # set the size of our blank canvas
    blank_img_height = downsized_image_height * multiplier
    blank_img_width = downsized_image_width * multiplier

    # set the padding value so the dots start in frame (rather than being off the edge)
    padding = int(multiplier/2)

    # create canvas containing just the background colour
    blank_img = np.full(((blank_img_height), (blank_img_width), 3), background_colour, dtype=np.uint8)

    # run through each pixel and draw the circle on our blank canvas
    for y in range(0, downsized_image_height):
        for x in range(0, downsized_image_width):
            cv2.circle(blank_img, (((x*multiplier)+padding), ((y*multiplier)+padding)),
                       int((0.6 * multiplier) * ((255-downsized_image[y][x])/255)), dots_colour, -1)

    return blank_img

########################################################################


def cartoon_style(original):
    image_1 = np.array(original)

    # applying effects --> sigma_s : Range between 0 to 200.
    # sigma_r : Range between 0 to 1.
    cartoon_image = cv2.stylization(image_1, sigma_s=150, sigma_r=0.25)
    cartoon_image = Image.fromarray(cartoon_image)
    return cartoon_image

#######################################################################


def waterColor_style(original):
    image_2 = np.array(original)

    # Resize the image
    image_resized = cv2.resize(image_2, None, fx=0.5, fy=0.5)

    # Clearing the impurities
    image_cleared = cv2.medianBlur(image_resized, 3)
    image_cleared = cv2.medianBlur(image_cleared, 3)
    image_cleared = cv2.medianBlur(image_cleared, 3)
    image_cleared = cv2.edgePreservingFilter(image_cleared, sigma_s=6)

    # Bilateral Image filtering
    image_filtered = cv2.bilateralFilter(image_cleared, 3, 10, 5)

    for i in range(2):
        image_filtered = cv2.bilateralFilter(image_filtered, 3, 20, 10)

    for i in range(3):
        image_filtered = cv2.bilateralFilter(image_filtered, 5, 30, 10)

    # Final part -- Sharpening the image
    gaussian_mask = cv2.GaussianBlur(image_filtered, (7, 7), 2)
    image_sharp = cv2.addWeighted(image_filtered, 1.5, gaussian_mask, -0.5, 0)
    image_sharp = cv2.addWeighted(image_sharp, 1.4, gaussian_mask, -0.2, 10)

    #image_sharp = Image.fromarray(image_sharp)
    return image_sharp


def main():
    pass


if __name__ == "__main__":
    main()
