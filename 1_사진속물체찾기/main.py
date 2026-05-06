import sys
import os
import numpy as np
import cv2

#1 이미지 불러오기

#1-1 이미지 파일 경로
template_src = os.path.join(os.path.dirname(__file__), 'img', 'template.png')
scene_src = os.path.join(os.path.dirname(__file__), 'img', 'scene.png')


# cv2.imshow('template', template)
# cv2.imshow('scene', scene)

cv2.waitKey(0)
cv2.destroyAllWindows()