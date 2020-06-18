import os
import sys
import glob


def main(purpose):
    folder = '../../datasets/DIV2K/DIV2K_{}_LR_bicubic/X4'.format(purpose)
    DIV2K(folder)
    print('Finished.')


def DIV2K(path):
    img_path_l = glob.glob(os.path.join(path, '*'))
    for img_path in img_path_l:
        new_path = img_path.replace('x2', '').replace('x3', '').replace('x4', '').replace('x8', '')
        os.rename(img_path, new_path)


if __name__ == "__main__":
    purpose = sys.argv[1]  # train or valid
    main(purpose)
