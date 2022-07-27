from typing import Union
from fastapi import FastAPI # 1. FastAPI 임포트
from pydantic import BaseModel

app = FastAPI() # 2. FastAPI 인스턴스 생성
# app은 다음 `python -m uvicorn main:app --reload`에서 app에 해당한다.


class Item(BaseModel):
  name: str
  prcie: float
  is_offer: Union[bool, None] = None

# 경로(엔드포인트, 라우트) 동작(Operation) 생성
# 여기서 "동작(Operation)"은 HTTP "메소드"중 하나를 나타낸다.
# 자주 사용하는 메서드로 POST(Create), GET(Read), PUT(Update), DELTE(Delete) 가 존재한다.
@app.get('/') # 3. 경로 동작 생성 - 경로: `/`, 동작: `get`
def read_root(): # 4. 경로 동작 함수 정의
  return {'Hello': 'Hello'} # 5. 콘텐츠 반환 - `dict`, `list`, 단일값을 가진 `str`, `int`등을 반환할 수 있다.

# @decoratoer
# @something 문법은 파이썬에서 "데코레이터"라고 부른다.
# "데코레이터"아래 있는 함수는 그걸 이용해 무언가 하는데,
# @app.get('/') 데코레이터는 FastAPI에게 아래 함수가 경로 `/`에 해당하는 `get`동작을 하라고 알려준다.
# 이것이 "경로 동작 데코레이터"이다.

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
  return {"item_price": item.prcie, "item_id": item_id}