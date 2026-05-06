# TODO

## ① 이미지 전처리
- scene과 template을 각각 불러와 그레이스케일로 변환하라
- scene에 가우시안 블러를 적용해 노이즈를 줄여라
- 블러 적용 전·후를 subplot으로 비교 출력하라
- 참고: Day1 Ch01~02 / Day2 Ch04

## ② 템플릿 매칭 수행
- `cv2.matchTemplate()`로 scene에서 template과 가장 유사한 위치를 탐색하라
- `cv2.minMaxLoc()`로 최적 위치(좌표)를 추출하라
- 매칭 유사도(similarity score)를 콘솔에 출력하라
- 참고: Day3 Ch08

## ③ 결과 시각화
- 찾은 위치에 `cv2.rectangle()`로 바운딩 박스를 그려라
- 박스 위에 `cv2.putText()`로 "Found!" 텍스트를 표시하라
- 원본 scene과 결과(박스 표시) 이미지를 subplot으로 나란히 출력하라
- 참고: Day1 Ch01~02 / Day2 Ch03

### 코드 설명

```python
h, w = template.shape
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
```
- `template.shape` → `(높이, 너비)` 반환. 바운딩 박스의 크기를 template 크기로 결정
- `max_loc` → `minMaxLoc()`가 반환한 가장 유사한 위치의 좌상단 좌표 `(x, y)`
- `bottom_right` → 좌상단에 template 너비·높이를 더해 우하단 좌표 계산

```python
scene_result = scene.copy()
cv2.rectangle(scene_result, top_left, bottom_right, 255, 2)
```
- `scene.copy()` → 원본을 보존하기 위해 복사본에 그림
- `cv2.rectangle(이미지, 좌상단, 우하단, 색상, 두께)` → 흰색(255) 2픽셀 두께 사각형

```python
cv2.putText(scene_result, 'Found!', (top_left[0], top_left[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2)
```
- `cv2.putText(이미지, 텍스트, 위치, 폰트, 크기, 색상, 두께)`
- 위치를 `top_left[1] - 10`으로 설정해 박스 바로 위에 텍스트 표시

```python
fig2, axes2 = plt.subplots(1, 2, figsize=(5, 5))
axes2[0].imshow(scene, cmap='gray')     # 왼쪽: 원본
axes2[1].imshow(scene_result, cmap='gray')  # 오른쪽: 바운딩 박스 결과
```
- `plt.subplots(1, 2)` → 1행 2열 subplot 생성
- `figsize=(5, 5)` → 창 크기 가로 5인치, 세로 5인치
- `axis('off')` → 축 눈금 제거

## ④ 이진화로 후처리 시각화
- 매칭 결과 히트맵(`matchTemplate` 반환값)에 임계값을 적용해 이진화하라
- 이진화된 히트맵을 별도 창 또는 subplot으로 출력하라
- 임계값을 바꿔가며 결과 차이를 확인하고 코드에 주석으로 기록하라
- 참고: Day2 Ch07