
# 학교 식단 API 설명

## 파라미터 표
|건물|data|gubun1|gubun2|
|------|---|---|---|
|수덕전|YYYYMMDD|1|1|
|정보공학관|YYYYMMDD|1|2|
|교직원식당|YYYYMMDD|3|Null|
|효민 기숙사|YYYYMMDD|2|Null|


### 수덕전 파라미터

 - data: 날짜(YYYYMMDD)
 - gubun1: 1
 - gubun2: 1

> 예시: https://smart.deu.ac.kr/m/sel_dfood?date=20231020&gubun2=1&gubun1=1

### 정보공학관 파라미터

 - data: 날짜(YYYYMMDD)
 - gubun1: 1
 - gubun2: 2

> 예시: https://smart.deu.ac.kr/m/sel_dfood?date=20231020&gubun2=2&gubun1=1

### 교직원식당 파라미터

 - data: 날짜(YYYYMMDD)
 - gubun1: 3
 - gubun2: Null

> 예시: https://smart.deu.ac.kr/m/sel_dfood?date=20231020&gubun1=3&gubun2=

### 효민 기숙사 파라미터

 - data: 날짜(YYYYMMDD)
 - gubun1: 2
 - gubun2: Null

> 예시: https://smart.deu.ac.kr/m/sel_dfood?date=20231020&gubun1=3&gubun2=

### 행복 기숙사 파라미터

 - locgbn: DE
 - sch_date: 날짜(YYYY-MM-DD)

> 예시: https://dorm.deu.ac.kr/deu/food/getWeeklyMenu.kmc?locgbn=DE&sch_date=2023-10-20