# Day 3 셀프 수업 실습가이드

## 학습 목표

- `describe()`, `corr()`, `skew()` 결과를 읽고 기초 통계를 다시 설명해봐요.
- `histplot`, `boxplot`을 골라 써서 분포와 이상치를 같이 확인해봐요.
- `train_test_split`, `fit`, `predict`, `accuracy_score` 흐름을 손으로 다시 익혀봐요.
- KNN, Decision Tree, Random Forest 차이를 정확도 비교와 함께 말로 정리해봐요.
- Penguins 전처리부터 SVM 분류까지 한 번에 연결해보면서 Day 3 전체를 복습해봐요.

---

## 사용 데이터 안내

| 데이터 | 불러오는 방법 |
|---|---|
| Palmer Penguins | `seaborn.load_dataset("penguins")` |
| Iris | `sklearn.datasets.load_iris()` |

> 권장 실행 환경: Windows 11, Python 3.12, pandas 2.2.x, scikit-learn 1.6~1.7, seaborn 0.13.x

---

## 공통 준비 코드

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
```

---

## 문제 1. \[쉬움\] Penguins 기초 통계 요약하고 상관계수 해석하기

### 문제 설명

Penguins 데이터에서 수치형 열만 골라 `describe()`와 `corr()` 결과를 확인해봐요.  
그다음 `body_mass_g`와 가장 강한 상관을 보이는 열이 무엇인지 찾아서 한 줄로 해석해보세요.  
마지막으로 수치형 열의 왜도도 같이 확인해서 분포 모양을 비교해보면 좋아요.

### 빈 코드셀

```python
# TODO: Penguins 데이터를 불러오고 복사본을 만들어요.


# TODO: 수치형 열만 선택해요.


# TODO: describe() 결과를 출력해요.


# TODO: corr() 결과를 출력해요.


# TODO: skew() 결과를 출력해요.


# TODO: body_mass_g와 다른 수치형 열의 상관계수를 따로 확인해요.


# TODO: 가장 상관이 큰 열 이름과 해석을 한 줄로 적어요.
```

### 힌트

- `describe()`, `corr()`, `skew()` 순서로 가면 돼요.
- 상관계수 해석은 `body_mass_g` 열을 기준으로 보면 돼요.

---

## 문제 2. \[보통\] Penguins 분포를 histplot과 boxplot으로 시각화하기

### 문제 설명

Penguins에서 `flipper_length_mm` 분포를 `histplot`으로 그리고,  
종별 `body_mass_g` 분포를 `boxplot`으로 비교해봐요.  
그래프 제목과 축 라벨은 한글로 넣고, 한글이 깨지지 않게 폰트 설정도 같이 해보세요.

### 빈 코드셀

```python
# TODO: Penguins 데이터를 불러와요.


# TODO: matplotlib 한글 폰트를 설정해요.


# TODO: figure와 axes를 만들어요.


# TODO: 첫 번째 축에 flipper_length_mm histplot을 그려요.


# TODO: 두 번째 축에 species별 body_mass_g boxplot을 그려요.


# TODO: 각 그래프 제목과 축 라벨을 한글로 설정해요.


# TODO: tight_layout()과 show()를 호출해요.
```

### 힌트

- `plt.rcParams`, `sns.histplot()`, `sns.boxplot()` 정도만 떠올리면 돼요.
- `subplots()`으로 축 두 개를 한 번에 만들 수 있어요.

---

## 문제 3. \[보통\] Iris로 KNN 분류 3줄 패턴 다시 쓰기

### 문제 설명

Iris 데이터를 불러와서 `train_test_split`으로 나누고,  
`KNeighborsClassifier(n_neighbors=5)`로 학습한 뒤 정확도를 확인해봐요.  
Day 3에서 배운 ML 3줄 패턴을 거의 그대로 다시 써보는 문제예요.

### 빈 코드셀

```python
# TODO: load_iris()로 데이터와 타깃을 준비해요.


# TODO: train_test_split()으로 훈련용과 테스트용을 나눠요.


# TODO: KNeighborsClassifier(n_neighbors=5) 모델을 만들어요.


# TODO: fit()으로 모델을 학습시켜요.


# TODO: predict()로 예측값을 구해요.


# TODO: accuracy_score()로 정확도를 출력해요.
```

### 힌트

- `load_iris()`, `train_test_split()`, `fit()`, `predict()` 흐름이에요.
- 정확도 계산은 `accuracy_score()` 하나면 충분해요.

---

## 문제 4. \[어려움\] Iris에서 Decision Tree와 Random Forest 정확도 비교하기

### 문제 설명

문제 3에서 만든 같은 `X_train`, `X_test`, `y_train`, `y_test`를 그대로 재사용해요.  
이번에는 Decision Tree와 Random Forest를 각각 학습하고 정확도를 비교해보세요.  
어느 모델이 더 잘 나왔는지 한 줄 의견도 적어보면 좋아요.

### 빈 코드셀

```python
# TODO: Iris 데이터를 다시 불러오고 같은 기준으로 train_test_split()을 해요.


# TODO: DecisionTreeClassifier 모델을 만들어요.


# TODO: RandomForestClassifier 모델을 만들어요.


# TODO: 두 모델을 각각 fit()으로 학습시켜요.


# TODO: 두 모델의 predict() 결과를 구해요.


# TODO: accuracy_score()로 두 정확도를 각각 출력해요.


# TODO: 어느 쪽이 더 높았는지 비교 문장을 적어요.
```

### 힌트

- `DecisionTreeClassifier()`, `RandomForestClassifier()`를 나란히 쓰면 돼요.
- 핵심은 같은 train/test를 재사용해서 공정하게 비교하는 거예요.

---

## 문제 5. \[도전\] Penguins 전처리 후 StandardScaler와 SVC로 species 분류하기

### 문제 설명

Penguins 데이터에서 `species`를 타깃으로 놓고 분류 모델을 만들어봐요.  
결측치는 제거하고, 범주형 입력 열은 인코딩하고, 수치형 열은 `StandardScaler`로 스케일링한 뒤 `SVC`를 적용해보세요.  
전처리 순서를 잘 지키는지가 가장 중요한 문제예요.

### 빈 코드셀

```python
# TODO: Penguins 데이터를 불러와 필요한 열만 선택해요.


# TODO: 결측치가 있는 행을 제거해요.


# TODO: 입력 열과 타깃 열을 분리해요.


# TODO: 범주형 입력 열을 get_dummies()로 인코딩해요.


# TODO: train_test_split()으로 훈련용과 테스트용을 나눠요.


# TODO: 수치형 열 목록을 정하고 StandardScaler를 준비해요.


# TODO: 훈련 데이터 수치형 열에 fit_transform()을 적용해요.


# TODO: 테스트 데이터 수치형 열에 transform()만 적용해요.


# TODO: SVC 모델을 만들고 fit()으로 학습시켜요.


# TODO: predict()와 accuracy_score()로 결과를 확인해요.
```

### 힌트

- `dropna()`, `pd.get_dummies()`, `StandardScaler()`, `SVC()` 순서예요.
- 스케일러는 훈련 데이터에만 `fit`해야 한다는 점을 꼭 기억해요.

---

## 마무리 점검

- [ ] 문제 1에서는 상관계수와 왜도 해석까지 말로 적어봤나요?
- [ ] 문제 2에서는 한글 폰트 설정이 들어갔나요?
- [ ] 문제 3~4에서는 같은 train/test 기준으로 모델을 비교했나요?
- [ ] 문제 5에서는 전처리 순서 때문에 데이터 누수가 생기지 않게 했나요?

---

> **한 줄 복습**  
> 오늘은 통계 요약, 시각화, ML 기본 패턴, 분류 알고리즘 비교를 한 번에 이어 보는 날이에요.
