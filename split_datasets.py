from sklearn.model_selection import train_test_split
import os
import shutil


def split_datasets(images_path='hv_dataset/images', labels_path='hv_dataset/labels', output_path='training/data',
                   test_size=0.2):

    if os.path.isdir(output_path):
        os.remove(output_path)

    image_list = os.listdir(images_path)
    image_train, image_valid = train_test_split(image_list, test_size=test_size)
    os.makedirs(output_path)

    train_path = os.path.join(output_path, 'train')
    valid_path = os.path.join(output_path, 'valid')

    os.mkdir(train_path)
    os.mkdir(valid_path)

    # write to train
    train_images = os.path.join(train_path, 'images')
    train_labels = os.path.join(train_path, 'labels')

    os.mkdir(train_images)
    os.mkdir(train_labels)

    valid_images = os.path.join(valid_path, 'images')
    valid_labels = os.path.join(valid_path, 'labels')

    os.mkdir(valid_images)
    os.mkdir(valid_labels)

    copy_images(image_train, images_path, train_images, labels_path, train_labels)
    copy_images(image_valid, images_path, valid_images, labels_path, valid_labels)


def copy_images(image_list: list, img_src: str, img_dest: str, label_src: str, label_dest: str):
    image: str
    for image in image_list:
        src_image_path = os.path.join(img_src, image)
        dest_image_path = os.path.join(img_dest, image)
        shutil.copy(src_image_path, dest_image_path)

        label = image.replace('jpg', 'txt').replace('png', 'txt').replace('jpeg', 'txt')
        src_label_path = os.path.join(label_src, label)
        dest_label_path = os.path.join(label_dest, label)
        shutil.copy(src_label_path, dest_label_path)


if __name__ == '__main__':
    split_datasets(output_path='data/nesto')
