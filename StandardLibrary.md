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

## time

시간과 관련된 time모듈에는 함수가 굉장히 많다. 그중 가장 유용한 몇가지만 알아보자.  

### time.time

```time.time()```은 UTC를 사용하여 현재 시간을 실수 형태로 리턴하는 함수이다.  
1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.  

```python
>>> import time
>>> time.time()
988458015.73417199
```

### time.localtime

```time.localtime```은 ```time.time()```이 리턴한 실수 값을 사용해서 연도,월,일,시,분,초, ... 의 형태로 바꾸어 주는 함수이다.  

```python
>>> time.localtime(time.time())
time.struct_time(tm_year=2013, tm_mon=5, tm_mday=21, tm_hour=16,
    tm_min=48, tm_sec=42, tm_wday=1, tm_yday=141, tm_isdst=0)
```

### time.asctime

위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수.  

```python
>>> time.asctime(time.localtime(time.time()))
'Sat Apr 28 20:50:20 2001'
```

### time.ctime

```time.asctime(time.localtime(time.time()))```은 ```time.ctime()```을 사용해 간편하게 표시할 수 있다. asctime과 다른접은  ctime은  
항상 현재 시간만을 리턴한다는 점이다.  

```python
>>> time.ctime()
'Sat Apr 28 20:56:31 2001'
```

### time.strftime

```
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
```

strftime함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.  

시간에 관계된 것을 표현하는 포맷 코드  
**포맷코드**|**설명**|**예**|
---|---|---|
%a|요일 줄임말|Mon|
%A|요일|Monday|
%b|달 줄임말|Jan|
%B|달|January|
%c|날짜와 시간을 출력함|06/01/01 17:22:21|
%d|날(day)|[01,31]|
%H|시간(hour)-24시간 출력 형태|[00,23]|
%I|시간(hour)-12시간 출력 형태|[01,12]|
%j|1년 중 누적 날짜|[001, 366]|
%m|달|[01, 12]|
%M|분|[01, 59]|
%p|AM or PM|AM|
%S|초|00,59|
%U|1년중 누적 주-일요일을 시작으로|00,53|
%w|숫자로 된 요일|0(일요일),6|
%W|1년 중 누적 주-월요일을 시작으로|00, 53|
%x|현재 설정된 로케일에 기반한 날짜 출력|06/01/01|
%X|현재 설정된 로케일에 기반한 시간 출력|17:22:21|
%Y|년도 출력|2001|
%Z|시간대 출력|대한민국 표준시|
%%|문자|%|
%y|세기부분을 제외한 년도 출력|01|

