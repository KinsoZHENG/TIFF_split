import os

import natsort as natsort
from libtiff import *

def split_tif(image_name):
    path = "./input/" + image_name  # set the TIF file path
    tif_dir = TIFF.open(path, mode='r')  # Open the TIF file by using TIFF mode 'read'
    tif_set = tif_dir.iter_images()  # Get all tif in TIFs as a list

    for idx, tif in enumerate(tif_set):  # Get each tif from TIFs
        save_path = "./output/" + os.path.splitext(image_name)[0] \
                    + "_{" + str(idx) + "}" + ".tif"  # Set the save_path file_name format
        # file_name Format = TIF_name + _{num} + ".tif"
        img_write = TIFF.open(save_path, 'w')  # Open save file(s)
        img_write.write_image(tif)  # Write in output_ file

    tif_dir.close()


if __name__ == '__main__':
    path = "input"
    tif_list = natsort.natsorted(os.listdir(path))

    for tif in tif_list:
        split_tif(tif)
