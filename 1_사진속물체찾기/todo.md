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

## ④ 이진화로 후처리 시각화
- 매칭 결과 히트맵(`matchTemplate` 반환값)에 임계값을 적용해 이진화하라
- 이진화된 히트맵을 별도 창 또는 subplot으로 출력하라
- 임계값을 바꿔가며 결과 차이를 확인하고 코드에 주석으로 기록하라
- 참고: Day2 Ch07