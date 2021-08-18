from .preprocess import preprocess


@preprocess()
def resize(x, y, w=None, h=None, keep_ar=False, interpolation=cv2.INTER_AREA):