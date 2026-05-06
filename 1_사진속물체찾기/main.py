import sys
import os
import numpy as np
import cv2

#1 이미지 전처리
#----------------------------------------
#1-1 이미지 파일 경로
template_src = os.path.join(os.path.dirname(__file__), 'img', 'template.png')
scene_src = os.path.join(os.path.dirname(__file__), 'img', 'scene.png')

template = cv2.imdecode(np.fromfile(template_src, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
scene = cv2.imdecode(np.fromfile(scene_src, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

if template is None or scene is None :
    print('########## 이미지 없음!!!')
    sys.exit()

# print('########## 이미지 출력')
# cv2.imshow('template', template)
# cv2.imshow('scene', scene)

#----------------------------------------
#1-2 scene(전체사진)에 가우시안 블러를 적용해 노이즈 줄이기
# 커널 크기는 홀수여야한다.
scene_blur = cv2.GaussianBlur(scene,(3,3), 0 )
# print('###########  가우시안 블러 이미지 출력')
# cv2.imshow('scene_blur', scene_blur)

#----------------------------------------
#1-3 가우시안 블러 전후를 subplot으로 비교 출력하기
import matplotlib.pyplot as plt
#cmap == colormap의 약자, 색을 지정하지않으면 matplotlib이 임의의 색을 지정.
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(scene, cmap='gray')
axes[0].set_title('Before')
axes[0].axis('off')

axes[1].imshow(scene_blur, cmap='gray')
axes[1].set_title('After (GaussianBlur)')
axes[1].axis('off')

plt.tight_layout()
plt.show()