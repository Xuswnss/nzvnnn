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


#----------------------------------------
#2. 템플릿 매칭 수행
# 2-1 cv2.matchTemplate()로 scene에서 template과 가장 유사한 위치를 탐색하라
# cv2.matchTemplate()로 scene에서 template과 가장 유사한 위치를 탐색하라
# • cv2.minMaxLoc()로 최적 위치(좌표)를 추출하라
# • 매칭 유사도(similarity score)를 콘솔에 출력하라
result = cv2.matchTemplate(scene_blur, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(f'매칭 유사도: {max_val:.1f}, 위치: {max_loc}')

#TM_CCOEFF_NORMED 는 정규화된 상관계수 방식으로 값이 1의 가까울 수록 유사핟.
#minMaxLoc() -> 유사도 맥에서 최솟값 최댓값고 그 위치를 반홚나다.

#----------------------------------------
# 3. 결과 시각화
# • 찾은 위치에 cv2.rectangle()로 바운딩 박스를 그려라
# • 박스 위에 cv2.putText()로  "Found!" 텍스트를 표시하라
# • 원본 scene과 결과(박스 표시) 이미지를 subplot으로 나란히 출력하라
h, w = template.shape
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

scene_result = scene.copy()
cv2.rectangle(scene_result, top_left, bottom_right, 255, 2)
cv2.putText(scene_result, 'Found!', (top_left[0], top_left[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2)

fig2, axes2 = plt.subplots(1, 2, figsize=(5, 5))
axes2[0].imshow(scene, cmap='gray')
axes2[0].set_title('원본 scene')
axes2[0].axis('off')

axes2[1].imshow(scene_result, cmap='gray')
axes2[1].set_title('매칭 결과')
axes2[1].axis('off')

plt.tight_layout()
plt.show()

#----------------------------------------
#4. 이진화로 후처리 후 시각화
# • 매칭 결과 히트맵(matchTemplate 반환값)에 임계값을 적용해 이진화하라
# • 이진화된 히트맵을 별도 창 또는 subplot으로 출력하라
# • 임계값을 바꿔가며 결과 차이를 확인하고 코드에 주석으로 기록하라