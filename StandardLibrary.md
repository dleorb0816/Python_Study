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

다음은 time.starftime을 사용하는 예이다.  

```python
>>> import time
>>> time.strftime('%x', time.localtime(time.time()))
'05/01/01'
>>> time.strftime('%c', time.localtime(time.time()))
'05/01/01 17:22:21'
```

### time.sleep

time.sleep함수는 주로 루프안에서 많이 사용한다. 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.  
다음 예를 보자.  

```python
#sleep1.py
import time
for i in range(10):
    print(i)
    time.sleep(1)
```

위 예는 1초 간격으로 0부터 9까지의 숫자를 출력한다. 위 예에서 볼 수 있듯이 time.sleep 함수의 인수는 실수 형태를 쓸 수 있다.  
즉 1이면 1초, 0.5면 0.5초가 되는 것이다.  

## math.gcd

math.gcd함수를 이용하면 최대공약수(gcd, greatest common divisor)를 쉽게 구할 수 있다.  
> math.gcd함수는 파이썬 3.5버전부터 사용할 수 있다.

어린이 집에서 사탕 60개, 초콜릿 100개, 젤리 80개를 준비했다. 아이들이 서로 싸우지 않도록 똑같이 나누어 봉지에 담는다고 하면  
최대 몇 봉지까지 만들 수 있을까? 단, 사탕, 초콜릿, 젤리는 남기지 않고 모두 담도록 한다.  

이 문제는 60,100,80의 최대공약수를 구하면 바로 해결된다. 즉, 똑같이 나눌 수 있는 봉지 개수가 최대가 되는 수를 구하면 된다.  

```python
>>> import math
>>> math.gcd(60, 100, 80)
20
```
> 파이썬 3.9버전부터는 math.gcd의 인수로 여러개가 가능하지만 3.9 미만 버전에서는 2개까지만 허용된다.

math.gcd()함수로 최대 공약수를 구했더니 20이었다. 따라서 최대 20봉지를 만들 수 있다. 각 봉지에 들어가는 사탕, 초콜릿, 젤리의 개수는 다음과 같이 전체  
개수를 최대공약수 20으로 나누면 구할수 있다.  

```python
>>> 60/20, 100/20, 80/20
(3.0, 5.0, 4.0)
```

따라서 한 봉지당 사탕 3개씩, 초콜릿 5개씩, 젤리 4개씩 담으면 된다.  

## math.lcm  

math.lcm은 최소공배수(lcm, least common multiple)를 구할때 사용하는 함수이다.  
> math.lcm()함수는 3.9버전부터 사용할 수 있다.

어느 버스 정류장에 시내버스는 15분마다 도착하고 마을버스는 25분마다 도착한다고 한다. 오후 1시에 두 버스가 동시에 도착했다고 할 때  
동시에 도착할 다음 시각을 알려면 어떻게 해야할까?

이 문제는 15와 25의 공통 배수중 가장 작은 수, 즉 최소 공배수를 구하면 바로 해결된다.  

```python
>>> import math
>>> math.lcm(15, 25)
75
```

math.lcm() 함수를 사용하여 최소공배수 75를 구했다. 따라서 두 버스가 동시에 도착할 다음 시각은 75분 후인 오후 2시 15분이다.

## random

random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다. random과 randint에 대해 알아보자.  

다음은 0.0에서 1.0사이의 실수 중에서 난수 값을 돌려주는 예를 보여준다.  

```python
>>> import random
>>> random.random()
0.53840103305098674
```

다음 예는 1에서 10사이의 정수 중에서 난수 값을 돌려준다.  

```python
>>> random.randint(1, 10)
6
```
다음 예는 1에서 55사이의 정수중에서 난수 값을 돌려준다.  

```python
>>> random.randint(1, 55)
43
```

random모듈을 사용해서 재미있는 함수를 하나 만들어 보자.  

```python
# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: 
        print(random_pop(data))
```

```
결과값:
2 
3 
1 
5 
4
```

위 random_pop함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 리턴한다. 물론 꺼낸 요소는 pop메서드에 의해 사라진다.  

함수는 random_pop 함수는 random 모듈의 choice함수를 사용하여 다음과 같이 좀 더 직관적으로 만들 수도 있다.  

```python
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number
```

random.choice함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴한다.  

리스트의 항목을 무작위로 섞고 싶을 떄는 random.shuffle 함수를 사용하면 된다.  

```python
>>> import random
>>> data = [1, 2, 3, 4, 5]
>>> random.shuffle(data)
>>> data
[5, 1, 3, 4, 2]
>>>
```

[1,2,3,4,5] 리스트가 shuffle 함수에 의해 섞여서 [5,1,3,4,2]로 변한 것을 확인할 수 있다.  

## itertools.zip_longest

```itertools.zip_longest(*iterables, fillvalue=None)``` 함수는 같은 개수의 자료형을 묶는 파이썬 내장 함수인 zip()과 똑같이 동작 한다.  
하지만, itertools.zip_longest()함수는 전달한 반복 가능 객체(*iterables)의 길이가 다르다면 긴 것을 기준으로 빠진 값은 fillvalue에 설정한  
값으로 채울수 있다.

유치원생 5명에게 간식을 나누어 주고자 다음과 같은 파이썬 코드를 작성했다.  

```python
students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = zip(students, snacks)
print(list(result))
```

그러나 간식 개수가 유치원생보다 적으므로 이 파이썬 코드를 실행하면 다음과 같은 결과가 나온다.  

```python
[('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리')]
```

students와 snack의 개수가 다르므로 더 적은 snacks의 개수만큼만 zip()으로 묶게 된다. 하지만, students가 snacks보다 많더라도  

다음처럼 부족한 snacks는 '새우깡'으로 채워 간식을 나누는 코드는 작성하려면 어떻게 해야 할까?  

```python
[('한민서', '사탕'), ('황지민', '초컬릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]
```

itertools.zip_longest()를 사용하면 개수가 많은 것을 기준으로 묶을 수 있다. 이때 부족한 항목은 None으로 채우는데, 다음처럼  

fillvalue로 값을 지정하면 None대신 다른 값으로 채울 수 있다.  

```python
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))
```

실행 결과는 다음과 같다.  

```python
[('한민서', '사탕'), ('황지민', '초콜릿'), ('이영철', '젤리'), ('이광수', '새우깡'), ('김승민', '새우깡')]
```

## itertools.permutation

itertools.permutations(iterable, r)은 반복 가능 객체(iterable)중에서 r개를 선택한 순열을 이터레이터로 리턴하는 함수이다.  
> 이터레이터란 반복 가능한 객체를 의미한다.

1,2,3숫자가 적힌 3장의 카드에서 두 장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하려면 어떻게 해야 할까?  

[1,2,3] 3장의 카드 중 순서에 상관없이 2장을 뽑는 경우의 수는 모두 3가지이다.(조합).  

- 1,2
- 2,3
- 1,3

하지만, 이 문제는 2자리 숫자이므로 이 3가지에 순서를 더해 다음처럼 6가지가 된다(순열).

- 1,2
- 2,1
- 2,3
- 3,2
- 1,3
- 3,1

이 순열은 itertools.permutations()를 사용하면 간단히 구할 수 있다.  

```python
>>> import itertools
>>> list(itertools.permutations(['1', '2', '3'], 2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
```

따라서 만들 수 있는 2자리 숫자는 다음과 같이 모두 6가지이다.  

```python
>>> for a, b in itertools.permutations(['1', '2', '3'], 2):
...     print(a+b)
...
12
13
21
23
31
32
```

## itertools.combination

itertools.combinations(iterable, r)은 반복 가능 객체(iterable)중에서 r개를 선택한 조합을 이터레이터로 리턴하는 함수이다.  

1~45중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수(조합)를 구하고 그 개수를 출력하려면 어떻게 해야 할까?  

다음과 같이 itertools.combinations()를 사용하면 45개의 숫자중 6개를 선택하는 경우의 수를 구할 수 있다.  

```python
>>> import itertools
>>> it = itertools.combinations(range(1, 46), 6)
```

iterools.combinations(range(1,46), 6)은 1~45의 숫자중에서 6개를 뽑는 경우의 수를 이터레이터로 리턴한다.  

이터레이터 객체를 루프를 이용하여 출력하면 아마 끝도 없이 출력될 것이다. 궁금하다면 직접 실행해 봐도 좋다.  

```python
>>> for num in it:
...     print(num)
...
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 7)
(1, 2, 3, 4, 5, 8)
(1, 2, 3, 4, 5, 9)
(1, 2, 3, 4, 5, 10)
(1, 2, 3, 4, 5, 11)
(1, 2, 3, 4, 5, 12)
(1, 2, 3, 4, 5, 13)
...
```

하지만, 순환하여 출력하지 않고 이터레이터의 개수만 세려면 다음과 같이 하면 된다.

```python
>>> len(list(itertools.combinations(range(1, 46), 6)))
8145060
```

선택할 수 있는 로또 번호의 가짓수는 8,145,060이다.  

