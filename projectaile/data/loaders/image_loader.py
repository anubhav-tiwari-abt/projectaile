from projectaile.data.loader import LOADER

@LOADER
def image_loader(img_path):
    img = cv2.imread(img_path)
    
    if len(img.shape) == 0:
        return f'Image Not Found At Path : {img_path}'
    
    return img