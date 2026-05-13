# Day 1 셀프 수업 실습가이드

## 학습 목표

- DataFrame, Series, Index를 표 구조 관점에서 읽어볼 수 있어요.
- `loc`, `iloc`, 조건 필터링, `str.contains()`를 섞어서 필요한 행과 열만 골라볼 수 있어요.
- 결측치를 진단하고 `dropna()`, `fillna()` 중 무엇을 써야 할지 판단해볼 수 있어요.
- Telco CSV를 읽은 뒤 `shape`, `columns`, `dtypes`, `info()`로 구조를 빠르게 파악해볼 수 있어요.
- `TotalCharges` 공백 문자열을 수치형으로 바꾸고, `.copy()` 패턴으로 안전하게 파생 열을 만들어볼 수 있어요.

---

## 사용 데이터 안내

- **Tips**: seaborn 내장 데이터셋을 기본으로 사용해요.
- **Telco Churn**: `WA_Fn-UseC_-Telco-Customer-Churn.csv` 또는 비슷한 이름의 CSV를 사용해요.
- **권장 실행 환경**: Windows 11, Python 3.12, pandas 2.2.x, seaborn 0.13.x
- 아래 문제는 현재 작업 폴더 또는 하위 폴더 어딘가에 CSV가 있다고 가정해요.
- Tips는 결측치가 거의 없을 수 있어서, 문제 3에서는 연습용 복사본에 결측을 일부 만들어서 처리해볼게요.

---

## 공통 준비 코드

```python
import pandas as pd
import numpy as np
import seaborn as sns
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


def load_tips():
    try:
        return sns.load_dataset("tips")
    except Exception:
        return load_csv("tips.csv")


def load_telco():
    filenames = [
        "WA_Fn-UseC_-Telco-Customer-Churn.csv",
        "telco_churn.csv",
        "Telco-Customer-Churn.csv",
    ]

    for filename in filenames:
        try:
            return load_csv(filename)
        except FileNotFoundError:
            continue

    raise FileNotFoundError("Telco Churn CSV 파일을 찾지 못했어요.")
```

---

## 문제 1. [쉬움] Tips 데이터에서 DataFrame 구조 파악하기

### 문제 설명

Tips도 결국 하나의 DataFrame이에요.
`shape`, `columns`, `dtypes`, `index`를 직접 확인하면서 표 구조를 읽어볼게요.
필요하면 특정 열 하나를 꺼내 Series인지 같이 확인해봐도 좋아요.

### 빈 코드셀

```python
# TODO: tips 데이터를 불러와요.


# TODO: tips의 shape를 출력해요.


# TODO: tips의 columns를 리스트로 출력해요.


# TODO: tips의 dtypes를 출력해요.


# TODO: tips의 index를 출력해요.


# TODO: tips의 앞 3행을 출력해서 표 구조를 눈으로 확인해요.


# TODO: 선택 사항이에요. tips["total_bill"]을 꺼내서 type()으로 확인해요.
```

### 힌트

- `tips.shape`는 함수가 아니라 속성이에요. 괄호 없이 읽어야 해요.
- `tips.columns.tolist()`로 보면 열 이름을 리스트처럼 읽기 편해져요.
- 열 하나를 꺼낼 때는 `tips["total_bill"]`처럼 쓰고, 이 결과가 Series인지 `type()`으로 확인해 보세요.

### 완료 확인 기준

- `shape`, `columns`, `dtypes`, `index`가 모두 출력되어야 해요.
- `head(3)` 결과에서 행과 열이 함께 보이면 성공이에요.
- 선택 과제까지 했다면 `tips["total_bill"]`이 Series로 보이면 좋아요.

---

## 문제 2. [쉬움] Tips 데이터에서 loc/iloc 선택과 조건 필터링 해보기

### 문제 설명

이번에는 Tips에서 원하는 행과 열을 직접 골라볼게요.
`loc`, `iloc`, 조건 필터링, `str.contains()`, `drop()`, `rename()`까지 한 번에 연결해보면 Day 1 흐름이 잘 정리돼요.

### 빈 코드셀

```python
# TODO: tips 데이터를 다시 불러와요.


# TODO: loc으로 0~4번 행의 total_bill, tip, time 열만 선택해요.


# TODO: iloc으로 앞 5행, 앞 3열을 선택해요.


# TODO: total_bill이 20 이상인 행만 필터링해요.


# TODO: time 열에 "Din"이 들어가는 행만 str.contains()로 필터링해요.


# TODO: smoker가 "Yes"이면서 day가 "Sun"인 행만 필터링해요.


# TODO: 위 결과에서 size 열을 drop()으로 제거해요.


# TODO: total_bill -> total_bill_usd, tip -> tip_usd로 rename() 해요.


# TODO: 최종 결과의 앞 5행을 출력해요.
```

### 힌트

- `loc`는 이름표 기준, `iloc`는 순서 기준이라고 떠올리면 돼요.
- 문자열 포함 여부는 `tips["time"].str.contains("Din", na=False)`처럼 쓸 수 있어요.
- 복합 조건은 `(조건1) & (조건2)`처럼 괄호를 각각 감싸는 습관이 중요해요.

### 완료 확인 기준

- `loc`와 `iloc` 결과가 각각 출력되어야 해요.
- 조건 필터링 결과에서 `smoker == "Yes"`와 `day == "Sun"` 조건이 동시에 만족되어야 해요.
- 최종 결과에 `size` 열이 없어지고, 열 이름이 바뀌어 있으면 성공이에요.

---

## 문제 3. [보통] Tips 데이터 결측치 진단하고 dropna/fillna 처리하기

### 문제 설명

Tips 원본에는 결측치가 거의 없을 수 있어서, 연습용 복사본에 일부 결측을 만들어서 처리해볼게요.
`isnull()`, `dropna()`, `fillna()` 흐름을 손으로 직접 해보는 게 핵심이에요.

### 빈 코드셀

```python
# TODO: tips 데이터를 불러온 뒤 practice_tips라는 복사본을 만들어요.


# TODO: practice_tips의 일부 행에 결측치를 넣어요.
# TODO: 예시로 total_bill 1개, tip 1개, day 1개 정도를 loc으로 비워 보세요.


# TODO: 열별 결측 개수를 isnull().sum()으로 출력해요.


# TODO: 결측치가 있는 행만 따로 확인해요.


# TODO: total_bill 또는 tip이 비어 있는 행은 dropna(subset=...)로 제거해요.


# TODO: day 열 결측치는 fillna()로 "Unknown"으로 채워요.


# TODO: 처리 후 결측 개수를 다시 출력해요.


# TODO: 처리 전 행 수와 처리 후 행 수를 비교해요.
```

### 힌트

- 원본 보호를 위해 `practice_tips = tips.copy()`부터 시작하는 게 좋아요.
- 일부 결측 만들기는 `practice_tips.loc[0, "total_bill"] = np.nan` 같은 방식으로 해보면 돼요.
- 모든 결측을 한 번에 지우기보다, 어떤 열은 지우고 어떤 열은 채우는 식으로 구분해 보는 게 실전 감각에 더 가까워요.

### 완료 확인 기준

- 결측치 넣기 전후가 아니라, 처리 전후 결측 개수 차이가 보여야 해요.
- `total_bill`과 `tip` 결측은 제거되고, `day` 결측은 `"Unknown"`으로 채워져야 해요.
- 최종 결과에서 남은 결측 수를 직접 확인할 수 있으면 성공이에요.

---

## 문제 4. [보통] Telco CSV를 읽고 구조 파악 후 TotalCharges 타입 변환하기

### 문제 설명

이제 Day 1 관통예제였던 Telco 데이터로 넘어가 볼게요.
CSV를 읽고 구조를 파악한 뒤, `TotalCharges` 공백 문자열을 수치형으로 바꾸고 중복 행도 정리해볼게요.

### 빈 코드셀

```python
# TODO: Telco CSV를 불러오고 telco라는 변수에 저장해요.
telo


# TODO: telco의 shape, columns 개수, dtypes 일부를 출력해요.


# TODO: info()를 실행해서 TotalCharges dtype을 확인해요.


# TODO: TotalCharges 열에서 공백 문자열 개수를 세어 봐요.


# TODO: 원본 보호를 위해 telco_clean = telco.copy()를 만들어요.


# TODO: TotalCharges의 공백 문자열을 np.nan으로 바꿔요.


# TODO: TotalCharges를 pd.to_numeric(errors="coerce")로 수치형으로 변환해요.


# TODO: 변환 후 TotalCharges dtype과 결측 개수를 출력해요.


# TODO: 전체 중복 행 수를 확인해요.


# TODO: drop_duplicates()로 중복을 제거한 뒤 행 수 변화를 확인해요.
```

### 힌트

- `info()`는 출력만 하고 값을 반환하지 않으니, 그냥 한 줄로 실행하면 돼요.
- 공백 문자열은 `telco["TotalCharges"].astype(str).str.strip().eq("")` 패턴으로 세어볼 수 있어요.
- 숫자 변환은 `astype(float)`보다 `pd.to_numeric(errors="coerce")`가 더 안전해요.

### 완료 확인 기준

- Telco의 기본 구조 정보가 출력되어야 해요.
- `TotalCharges`가 수치형으로 바뀌고, 변환 후 dtype을 직접 확인할 수 있어야 해요.
- 중복 제거 전후 행 수를 비교해서 변화가 있는지 또는 없는지 설명할 수 있으면 성공이에요.

---

## 문제 5. [도전] Telco에서 .copy() 패턴으로 파생 열 만들고 SettingWithCopyWarning 피하기

### 문제 설명

마지막 문제는 Day 1 핵심인 `.copy()` 패턴을 적용해보는 문제예요.
필터링한 부분집합에 바로 값을 넣지 말고, `.copy()`로 안전한 작업용 DataFrame을 만든 뒤 파생 열을 추가해볼게요.

### 빈 코드셀

```python
# TODO: Telco 데이터를 다시 불러오고 필요한 기본 정제를 먼저 해요.
# TODO: TotalCharges 공백 처리와 수치형 변환까지 끝낸 상태를 만들어요.


# TODO: Contract가 "Month-to-month"인 고객만 골라서 month_df를 만들어요.


# TODO: month_df를 만들 때 .copy()를 붙여서 독립된 DataFrame으로 만들어요.


# TODO: tenure가 0인 경우를 먼저 확인해요.


# TODO: charge_per_month 파생 열을 만들어요.
# TODO: 힌트: TotalCharges를 tenure로 나누되, tenure가 0이면 np.nan으로 처리해 보세요.


# TODO: senior_partner 파생 열을 만들어요.
# TODO: 힌트: SeniorCitizen이 1이고 Partner가 "Yes"인 경우만 True가 되게 해보세요.


# TODO: loc[:, "새열이름"] 패턴으로 열을 넣어 보세요.


# TODO: 필요한 열만 골라 결과를 확인해요.
# TODO: 예시: customerID, Contract, tenure, TotalCharges, charge_per_month, senior_partner


# TODO: 원본 telco에는 새 열이 생기지 않았는지도 확인해요.
```

### 힌트

- `telco[telco["Contract"] == "Month-to-month"]` 다음에 바로 대입하면 경고가 날 수 있어요. `.copy()`를 붙여서 작업용 표를 따로 만드는 습관이 중요해요.
- 새 열 대입은 `month_df.loc[:, "charge_per_month"] = ...`처럼 쓰면 의도가 더 분명해요.
- `senior_partner`는 불리언 열이라서 먼저 조건식을 만들고, 마지막에 결과만 확인해 보면 돼요.

### 완료 확인 기준

- 필터링한 부분집합이 `.copy()`로 만들어져 있어야 해요.
- 파생 열 2개가 정상적으로 추가되어야 해요.
- 원본 `telco`에 새 열이 생기지 않았으면 성공이에요.

---

## 제출 전 체크

- [ ] 모든 설명과 주석을 한국어로 적었는지 확인해요.
- [ ] `load_csv()` 또는 `load_tips()`, `load_telco()`로 데이터 로드가 되는지 확인해요.
- [ ] 각 문제에서 요구한 출력이 실제로 나오는지 확인해요.
- [ ] `loc`와 `iloc`를 구분해서 썼는지 다시 봐요.
- [ ] `dropna()`와 `fillna()`를 왜 다르게 썼는지 스스로 설명해봐요.
- [ ] Telco에서 `TotalCharges`를 수치형으로 바꾸는 이유를 한 줄로 적어봐요.
- [ ] `.copy()` 없이 부분집합에 바로 대입하지 않았는지 확인해요.

---

> **완료 확인 한 줄 요약**: Tips로 pandas 기본 조작을 연습하고, Telco로 구조 파악부터 정제와 안전한 파생 열 생성까지 직접 해보면 Day 1 핵심이 정리돼요.
