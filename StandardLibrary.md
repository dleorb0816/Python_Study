# 표준 라이브러리

> - 파이썬 표준 라이브러리는 파이썬을 설치할때 자동으로 컴퓨터에 설치된다.
> - sys, re 모듈은 파이썬의 중요한 표준 라이브러리이다.

## datetime.date

datetime.date는 년,월,일로 **날짜**를 표현할 때 사용하는 함수이다.  

년, 월, 일로 다음과 같이 datetime.date 객체를 만들수 있다.  

```python
>>> import datetime
>>> day1 = datetime.date(2019, 12, 14)
>>> day2 = datetime.date(2021, 6, 5)
```

이처럼 년,월,일을 인수로 하여 2019년 12월 14일에 해당하는 날짜 객체는 day1, 2021년 6월 5일에 해당하는 날짜 객체는 day2로  
생성하였다. 이렇게 날짜 객체를 만들었다면 두 날짜의 차이는 다음과 같이 뺄셈으로 쉽게 구할 수 있다.  

```python
>>> diff = day2 - day1
>>> diff.days
174
```

day2에서 day1을 빼면 diff 객체가 리턴되고 이 객체를 이용하면 두 날짜의 차이를 쉽게 확인할 수 있다.  

요일은 datetime.date객체의 weekday()함수를 사용하면 쉽게 구할 수 있다.  

```python
>>> import datetime
>>> day = datetime.date(2019, 12, 14)
>>> day.weekday()
5
```

0은 월요일을 의미하며 순서대로 1은 화요일, 2는 수요일,..., 6은 일요일이 된다. 이와는 달리 월요일은 1, 화요일은 2, ..., 일요일은 7을  
리턴하려면 다음처름 isoweekday()함수를 사용하면 된다.  

```python
>>> day.isoweekday()
6
```

2019년 12월 14일은 토요일이므로 isoweekday()를 사용하면 토요일을 뜻하는 6이 리턴된다.(weekday를 사용하면 5가 리턴된다.)  

##time

