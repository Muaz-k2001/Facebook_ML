from PIL import Image
import shutil
import os



def resize_image(final_size, im):
    size = im.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im = im.resize(new_image_size, Image.Resampling.LANCZOS)
    new_im = Image.new('RGB', (final_size, final_size))
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_im



def create_cleaned_images_folder(new_dir):
    try:
        shutil.rmtree(new_dir)
    except:
        pass
    os.mkdir(new_dir)
    print('cleaned images directory created')



if __name__ == '__main__':
    new_dir = 'cleaned_images/'
    path = 'images/'
    dirs = os.listdir(path)
    final_size = 512
    create_cleaned_images_folder(new_dir)
    for n, item in enumerate(dirs[:5], 1):
        im = Image.open('images/' + item)
        new_im = resize_image(final_size, im)
        new_im.save(f'{new_dir}{n}_resized.jpg')

