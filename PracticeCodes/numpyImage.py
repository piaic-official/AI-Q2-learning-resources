import numpy as np
# for image reading
import matplotlib.pylab as plt
#import matplotlib.image

def plti(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')
    #input('press <ENTER> to continue')

def main():
    #%matplotlib pltinline
    im = plt.imread("airplane.png")
    print(type(im))
    plti(im)
    im = im[400:3800,:2000,:]
    plti(im)
    print( im.shape )
    
main()