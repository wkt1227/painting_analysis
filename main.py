import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2hsv
import pathlib


def main():
    img_paths = pathlib.Path('./input').glob('*')

    for path in img_paths:
        rgb_img = io.imread(path)
        hsv_img = rgb2hsv(rgb_img)
        saturations = hsv_img[:, :, 1].flatten()
        values = hsv_img[:, :, 2].flatten()

        fig = plt.figure(figsize=(10, 5), tight_layout=True)
        gs = fig.add_gridspec(2, 3)

        ax1 = fig.add_subplot(gs[:, 0:2])
        plt.imshow(rgb_img)
        ax1.set_xticks([])
        ax1.set_yticks([])

        ax2 = fig.add_subplot(gs[:, 2])
        plt.scatter(saturations, values, s=1, alpha=0.01)
        plt.ylim((0, 1))
        plt.xlim((0, 1))
        plt.ylabel('value')
        plt.xlabel('saturation')
        ax2.set_aspect('equal')
        ax2.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
        ax2.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

        plt.savefig(f'./output/result_{path.name}')


if __name__ == '__main__':
    main()