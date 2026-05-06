import sys
import os
import numpy as np
import cv2

#1 이미지 불러오기

#1-1 이미지 파일 경로
template_src = os.path.join(os.path.dirname(__file__), 'img', 'template.png')
scene_src = os.path.join(os.path.dirname(__file__), 'img', 'scene.png')

# OpenCV on Windows can fail to read Unicode paths directly; use Python file read + imdecode.
def imread_unicode(path, flags=cv2.IMREAD_GRAYSCALE):
    with open(path, 'rb') as f:
        data = f.read()
    return cv2.imdecode(np.frombuffer(data, dtype=np.uint8), flags)

template = imread_unicode(template_src, cv2.IMREAD_GRAYSCALE)
scene = imread_unicode(scene_src, cv2.IMREAD_GRAYSCALE)

if template is None or scene is None:
    print(f"image load failed: template={template_src} scene={scene_src}")
    print(f"template loaded: {template is not None}, scene loaded: {scene is not None}")
    sys.exit(1)

cv2.imshow('template', template)
cv2.imshow('scene', scene)

cv2.waitKey(0)
cv2.destroyAllWindows()