# sparta-ai6-week10-pyproj
팀 스파르타 개인과제 (2024-05-02 제출)

# 프로젝트 명: 
우리를 위한 중고거래 :: 스파르타 마켓 (DRF)

## 개요:  
- 개별 과제입니다. 💁‍♂️💁‍♀️
- 각 유저는 자신의 물건을 등록 할 수 있습니다.
- 지역별 유저는 고려하지 않습니다. 우리는 모두 스파르타 이웃이니까요.
- 구매하기 기능은 구현하지 않습니다.
- 프로젝트 명은 `spartamarket_DRF` 입니다.
    - 아래의 앱은 필수로 포함하며, 이외에는 자유롭게 구현해 주세요.
        - `accounts` - 계정 관련 기능
        - `products` - 상품 관련 기능

## 기간:

2024년 4월 26일 ~ 2024년 5월 2일 (총 5일)

## 포지션:

- 정해진: Auth, 상품 CRUD, 유저 프로필

## 적용한 기술:

- Python
- Python Django
- Python Django Rest Framework
- DB: SQLite3
- Server: Django

## ERD

![ERD](https://github.com/creative-darkstar/sparta-ai6-week10-pyproj/assets/159861706/42ee2de3-7329-4899-9938-0369a60867a4)

## APIs

- Accounts

| Method                                 | Authorization | endpoint                       | Description                                         |
|----------------------------------------|---------------|--------------------------------|-----------------------------------------------------|
| <span style="color:yellow">POST</span> | `Anonymous`   | `/api/accounts/`               | 회원가입                                                |
| <span style="color:yellow">POST</span> | `User`        | `/api/accounts/login`          | 로그인                                                 |
| <span style="color:yellow">POST</span> | `User`        | `/api/accounts/login/refresh`  | 로그인 갱신. Refresh Token으로 Access, Refresh Token 신규 발급 |
| <span style="color:green">GET</span>   | `User`     | `/api/accounts/<str:username>` | 유저 프로필 조회 (필요한 데이터만)                                |

- Products

| Method                                 | Authorization | endpoint                      | Description                 |
|----------------------------------------|---------------|-------------------------------|-----------------------------|
| <span style="color:green">GET</span>   | `User`      | `/api/products/`              | 상품 목록 조회                    |
| <span style="color:green">GET</span>   | `User`      | `/api/products/<int:productId>`          | 상품 상세 조회                    |
| <span style="color:yellow">POST</span> | `User`         | `/api/products/` | 상품 등록                       |
| <span style="color:skyblue">PUT</span> | `User`      | `/api/products/<int:productId>` | 상품 정보 수정 (로그인 한 유저가 해당 상품을 등록한 유저일 시) |
| <span style="color:red">DELETE</span>  | `User`      | `/api/products/<int:productId>` | 유저 프로필 조회 (로그인 한 유저가 해당 상품을 등록한 유저일 시)                  |

## 설치 필요 패키지
- requirements.txt에 명시
- `pip install -r requirements.txt` 로 설치
