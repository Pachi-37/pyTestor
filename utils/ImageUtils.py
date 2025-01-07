import os.path

from PIL import Image


class ImageUtils:
    @staticmethod
    def get_image_size(image_path):
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height

    @staticmethod
    def resize_image(image_path, percentage):
        with Image.open(image_path) as img:
            width, height = ImageUtils.get_image_size(image_path)
            new_width = int(width * percentage / 100)
            new_height = int(height * percentage / 100)
            resized_img = img.resize((new_width, new_height))
            new_image_path = os.path.join(os.path.dirname(image_path), "resize_" + os.path.basename(image_path))
            resized_img.save(new_image_path)
            return new_image_path

    @staticmethod
    def get_image_size_inch(image_path):
        with Image.open(image_path) as img:
            width, height = img.size
            dpi = img.info.get('dpi', (72, 72))  # 获取 DPI，默认为 (72, 72)
            width_inch = width / dpi[0]
            height_inch = height / dpi[1]
            return width_inch, height_inch


if __name__ == '__main__':
    image_path = "../test.jpg"
    print(ImageUtils.get_image_size(image_path))
    resize_img = ImageUtils.resize_image(image_path, 50)
    resize_img.save("../test_50.jpg")
