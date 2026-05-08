# `__file__` 변수 동작 정리

---

## 문제 상황

`.py` 파일에서 `os.path.dirname(__file__)`을 사용할 때 **될 때도 있고 안 될 때도 있다.**  
또한 Jupyter Notebook(`.ipynb`)에서는 **항상 오류가 발생한다.**

```python
import os
os.path.dirname(__file__)
# NameError: name '__file__' is not defined
```

---

## 원인

`__file__`은 Python이 **디스크에서 파일을 읽어 실행할 때** 자동으로 설정되는 변수다.  
파일 경로가 존재하지 않는 실행 방식에서는 Python이 경로를 알 수 없으므로 변수 자체를 설정하지 않는다.

### 안 되는 경우

| 실행 방식 | 예시 | 이유 |
|---|---|---|
| 인터랙티브 인터프리터 | `python` 실행 후 입력 | 파일이 아닌 stdin으로 입력받음 |
| `-c` 옵션 | `python -c "print(__file__)"` | 문자열로 실행, 파일 경로 없음 |
| `exec()` / `eval()` | `exec("print(__file__)")` | 문자열을 동적으로 실행 |
| Jupyter Notebook | `.ipynb` 파일 | 셀 단위 실행, 파일 경로 미설정 |

### 되는 경우

| 실행 방식 | 예시 |
|---|---|
| 파일 직접 실행 | `python myscript.py` |
| 모듈 실행 | `python -m mymodule` |
| 모듈 임포트 | `import mymodule` |

---

## 해결 방안

### `.py` 파일에서 안전하게 사용하기

```python
import os

# __file__이 없을 수 있는 환경을 고려한 방어 코드
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()
```

### Jupyter Notebook에서 대체 방법

```python
import os

# 방법 1: 현재 작업 디렉토리 사용 (가장 간단, 보통 노트북 위치와 동일)
BASE_DIR = os.getcwd()

# 방법 2: pathlib 사용
from pathlib import Path
BASE_DIR = Path.cwd()
```

---

## 참고 사항

- `os.path.abspath(__file__)`을 쓰는 이유: `__file__`이 상대경로로 설정되는 경우가 있어서 절대경로로 변환해주는 것이 안전하다.
- Jupyter에서 `os.getcwd()`는 **노트북을 실행한 위치** 기준이므로, 터미널에서 다른 경로로 실행하면 달라질 수 있다.
- `pathlib.Path`는 Python 3.4+ 부터 사용 가능하며, `os.path` 보다 직관적인 경로 조작을 제공한다.
