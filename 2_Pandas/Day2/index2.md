# Day 2 셀프 수업 실습가이드

## 학습 목표

- `merge`와 `groupby`를 함께 써서 Titanic 열을 다시 읽어봐요.
- `Age` 결측치, `Sex_enc`, `Deck` 전처리를 직접 해봐요.
- `get_dummies(drop_first=True)`와 `pd.concat(axis=1)` 흐름을 손으로 익혀요.
- Telco 데이터에서 인코딩, `train_test_split(stratify=y)`, 스케일링까지 한 번에 연결해봐요.
- 데이터 누수를 막는 순서를 말로 설명할 수 있게 해요.

## 사용 데이터 안내

| 데이터 | 파일명 |
|--------|--------|
| Titanic | `titanic.csv` |
| Telco Churn | `telco_churn_clean.csv` |

> 권장 실행 환경: Windows 11, Python 3.12, pandas 2.2.x, scikit-learn 1.6~1.7  
> 아래 문제는 현재 작업 폴더 또는 하위 폴더 어딘가에 CSV가 있다고 가정해요.

## 공통 준비 코드

```python
import pandas as pd
from pathlib import Path


def load_csv(filename):
    candidates = [Path(filename), Path.cwd() / filename]
    candidates.extend(Path.cwd().rglob(filename))

    seen = set()
    for path in candidates:
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        if path.exists():
            return pd.read_csv(path)

    raise FileNotFoundError(f"{filename} 파일을 찾지 못했어요.")
```

---

## 문제 1. [쉬움] Titanic 열 두 묶음을 merge해서 다시 보기

### 문제 설명

Titanic에서 `PassengerId`를 key로 써서 가로로 합쳐볼게요.  
기본 정보 표와 요금 표를 따로 만든 뒤 merge하고, 합쳐진 결과에서 `Pclass`별 인원수와 평균 `Fare`를 구해보세요.

### 빈 코드셀

```python
# TODO: Titanic 데이터를 읽어와요.


# TODO: PassengerId, Pclass, Name이 들어 있는 기본 정보 표를 만들어요.


# TODO: PassengerId, Fare, Embarked가 들어 있는 요금 표를 만들어요.


# TODO: PassengerId를 기준으로 inner merge를 해요.


# TODO: 합쳐진 표의 앞 5행을 출력해요.


# TODO: Pclass별 인원수와 평균 Fare를 groupby로 구하고 reset_index()까지 해요.
```

### 힌트

- `pd.merge(left, right, on="PassengerId", how="inner")` 형태를 먼저 떠올려 보세요.
- 집계는 `groupby("Pclass").agg(...)` 패턴을 그대로 쓰면 돼요.
- 마지막 표는 `passenger_count`, `mean_fare` 같은 읽기 쉬운 이름으로 만들어 보세요.

### 완료 확인 기준

- merge된 결과에 `PassengerId`, `Pclass`, `Name`, `Fare`, `Embarked`가 같이 보여야 해요.
- 집계 결과가 Pclass 1, 2, 3 기준 3행으로 나오면 성공이에요.

---

## 문제 2. [쉬움] Titanic Age, Sex, Cabin 전처리하기

### 문제 설명

이제 Day 2의 핵심 전처리를 직접 해볼게요.  
`Age`는 중앙값으로 채우고, `Sex`는 `Sex_enc`로 바꾸고, `Cabin` 첫 글자를 뽑아서 `Deck`을 만들어 보세요.

### 빈 코드셀

```python
# TODO: Titanic 데이터를 읽고 복사본을 만들어요.


# TODO: 처리 전 Age 결측 개수를 출력해요.


# TODO: Age 중앙값을 변수에 저장해요.


# TODO: Age 결측치를 중앙값으로 채워요.


# TODO: Sex를 {"male": 0, "female": 1}로 매핑해서 Sex_enc 열을 만들어요.


# TODO: Cabin 첫 글자를 뽑고, 결측은 "U"로 채워 Deck 열을 만들어요.


# TODO: Age 결측 개수, Sex_enc 결측 개수, Deck value_counts()를 출력해요.
```

### 힌트

- `age_median = df["Age"].median()`처럼 계산과 적용을 나눠 쓰면 덜 헷갈려요.
- `df["Cabin"].str[0].fillna("U")` 패턴을 그대로 써도 돼요.
- `Sex_enc` 분포가 0과 1로만 보이는지도 같이 확인해 보세요.

### 완료 확인 기준

- `Age` 결측 수가 0이어야 해요.
- `Sex_enc`가 숫자형 0/1로 보여야 해요.
- `Deck` 분포에서 `U`가 가장 많이 보이면 정상이에요.

---

## 문제 3. [보통] Titanic Embarked, Deck 원핫 인코딩 후 X 만들기

### 문제 설명

앞 문제에서 만든 Titanic 전처리 결과를 이어서 써볼게요.  
`Embarked` 결측은 `S`로 채우고, `Embarked`와 `Deck`은 `get_dummies(drop_first=True)`로 바꾼 뒤, `pd.concat(axis=1)`으로 붙여 최종 X를 만들어 보세요.

### 빈 코드셀

```python
# TODO: Titanic 데이터를 다시 읽고 Age, Sex_enc, Deck 전처리를 먼저 해요.


# TODO: Embarked 결측을 최빈값 "S"로 채워요.


# TODO: Embarked는 categories=["S", "C", "Q"]로 Categorical을 만들어요.


# TODO: Deck은 categories=["U", "C", "E"]로 Categorical을 만들어요.


# TODO: Embarked 더미열과 Deck 더미열을 각각 get_dummies(drop_first=True, dtype=int)로 만들어요.


# TODO: 숫자 기본 열 6개와 더미열을 axis=1로 concat해요.


# TODO: X의 열 목록, shape, 결측 수 합계를 출력해요.
```

### 힌트

- 기본 열은 `["Pclass", "Sex_enc", "Age", "SibSp", "Parch", "Fare"]`를 그대로 써보세요.
- `pd.concat([base_df, embarked_dummies, deck_dummies], axis=1)` 형태예요.
- 기대하는 더미열 이름은 `Emb_C`, `Emb_Q`, `Deck_C`, `Deck_E`예요.

### 완료 확인 기준

- X에 기본 6개 열과 더미 4개 열이 함께 있어야 해요.
- `X.isnull().sum().sum()` 결과가 0이면 성공이에요.
- `pd.concat`에서 행이 아니라 열이 붙었는지 꼭 확인해요.

---

## 문제 4. [보통] Telco 범주형 인코딩하기

### 문제 설명

이번에는 Telco로 넘어가 볼게요.  
먼저 `Contract`와 `InternetService`별 Churn 비율을 보고, 그다음 이진 범주형은 `map()`, 다값 범주형은 `get_dummies()`로 인코딩해 보세요.

### 빈 코드셀

```python
# TODO: Telco 데이터를 읽고 복사본을 만들어요.


# TODO: Contract별 Churn 비율 표를 만들어요.


# TODO: InternetService별 Churn 비율 표를 만들어요.


# TODO: binary_cols 리스트를 만들어요.


# TODO: multi_cols 리스트를 만들어요.


# TODO: binary_map 사전을 만들고, binary_cols를 반복하면서 map()을 적용해요.


# TODO: get_dummies(columns=multi_cols, drop_first=True, dtype=int)로 인코딩해요.


# TODO: 인코딩 후 전체 열 수와 Contract_ 접두사 열 목록을 출력해요.
```

### 힌트

- `binary_cols`에는 `gender`, `Partner`, `Dependents`, `PhoneService`, `PaperlessBilling`, `Churn`이 들어가요.
- `multi_cols`에는 `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaymentMethod`가 들어가요.
- `groupby(...).value_counts(normalize=True).rename("ratio").reset_index()` 패턴을 다시 떠올려 보세요.

### 완료 확인 기준

- `Contract` 비율 표와 `InternetService` 비율 표가 각각 보여야 해요.
- `Contract_One year`, `Contract_Two year` 열이 보이면 성공이에요.
- 왜 `Contract`에 레이블 인코딩보다 원핫 인코딩이 더 안전한지도 한 줄로 적어 보세요.

---

## 문제 5. [도전] Telco를 ML-ready 데이터셋으로 완성하기

### 문제 설명

이제 Day 2를 한 번에 정리해볼게요.  
Telco 데이터를 인코딩한 뒤 y와 X를 나누고, `train_test_split(stratify=y)`를 적용하고, `tenure`, `MonthlyCharges`, `TotalCharges`만 `StandardScaler`로 스케일링해 보세요.

### 빈 코드셀

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# TODO: 문제 4의 인코딩 결과를 다시 만들거나 이어서 사용해요.


# TODO: y = df["Churn"], X = df.drop(columns=["customerID", "Churn"])로 분리해요.


# TODO: train_test_split(test_size=0.2, random_state=42, stratify=y)로 나눠요.


# TODO: X_train, X_test 사본을 만들어요.


# TODO: num_cols = ["tenure", "MonthlyCharges", "TotalCharges"]를 선언해요.


# TODO: StandardScaler를 만들고 X_train에는 fit_transform, X_test에는 transform만 적용해요.


# TODO: X_train shape, X_test shape, 양쪽 결측 수, y_train/y_test 평균을 출력해요.
```

### 힌트

- split을 먼저 하고 스케일링을 나중에 해야 데이터 누수를 막을 수 있어요.
- `X_train.loc[:, num_cols] = ...` 형태로 넣으면 읽기 편해요.
- `y_train.mean()`과 `y_test.mean()`이 비슷하면 `stratify=y`가 잘 들어간 거예요.

### 완료 확인 기준

- `X_train`, `X_test`가 모두 숫자형 중심 표로 준비돼야 해요.
- `X_train`과 `X_test`의 결측 수 합계가 모두 0이어야 해요.
- `y_train.mean()`과 `y_test.mean()`이 둘 다 0.265 근처면 성공이에요.

---

## 제출 전 체크

- [ ] 문제 1: `merge`와 `groupby` 결과를 모두 출력했나요?
- [ ] 문제 2: `Age`, `Sex_enc`, `Deck` 전처리를 끝냈나요?
- [ ] 문제 3: `pd.concat(axis=1)`로 최종 X를 만들었나요?
- [ ] 문제 4: Telco 인코딩 뒤 `Contract_` 더미열을 확인했나요?
- [ ] 문제 5: `stratify=y`와 `fit/transform` 분리를 지켰나요?

## 완료 확인 한 줄 요약

- Titanic은 전처리와 인코딩까지 끝나야 해요.
- Telco는 인코딩과 스케일링까지 끝나야 해요.
- 마지막에는 **"왜 이 순서가 데이터 누수를 막는지"** 를 말로 설명할 수 있으면 진짜 완료예요.
