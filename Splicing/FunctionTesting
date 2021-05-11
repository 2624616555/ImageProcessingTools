from splicing import image_coor, cut_image, splicing_image
from skimage import io
from skimage import data

if __name__ == '__main__':
    image = data.astronaut()
    coor = image_coor(image, 20, 20, 50)
    patch_list = cut_image(image, coor)
    new_image = splicing_image(patch_list, coor)
    io.imsave(r'astronaut_splicing.png',new_image)
