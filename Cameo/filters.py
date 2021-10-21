import cv2
import numpy as np
import utils

def strokeEdges(src, dst, blurKsize = 7, edgeKsize = 5):
    if blurKsize >= 3:
        blurredSrc = cv2.medianBlur(src, blurKsize)
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize = edgeKsize)
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels, dst)

class VConvolutionFilter(object):
    #A filter that applies a convolution to V (or all of BGR)
    def __init__(self, kernel):
        self._kernel = kernel
    def apply(self, src, dst):
        #Apply the filter with a BGR or gray source/ destination
        cv2.filter2D(src, -1, self._kernel, dst)

class SharpenFilter(VConvolutionFilter):
    # A sharpen filter with a 1-pixel radius
    def __init__(self):
        kernel = np.array(
            [[-1, -1, -1],
            [-1, 9, -1],
            [-1, -1, -1]]
        )
        super().__init__(kernel)
class FindEdgesFilter(VConvolutionFilter):
    #An edge finding filter with 1-pixel radius
    def __init__(self):
        kernel = np.array(
            [[-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]]
        )
        super().__init__(kernel)

class BlurFilter(VConvolutionFilter):
    # a blur filter with a 2-pixel radius
    def __init__(self):
        kernel = np.array([
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04],
            [0.04, 0.04, 0.04, 0.04, 0.04]
        ])
        super().__init__(kernel)

class EmbossFilter(VConvolutionFilter):
    #an emboss filter with 1-pixel radius
    def __init__(self):
        kernel = np.array([
            [-2, -1, 0],
            [-1, 1, 1],
            [0, 1, 2]
        ])
        super().__init__(kernel)

