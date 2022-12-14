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

## functools.reduce

functools.reduce(function, iterable)은 반복 가능한 객체(iterable)의 요소에 차례대로(왼쪽에서 오른쪽으로) 누적 적용하여  
이 객체를 하나의 값으로 줄이는 함수이다.  

다음은 입력 인수 data의 요소를 모두 더하여 리턴하는 add()함수이다.  

```python
def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1, 2, 3, 4, 5]
result = add(data)
print(result)  # 15 출력
```

functools.reduce()를 사용하여 마찬가지로 동작하는 코드를 작성하려면 어떻게 해야 할까?  
functools.reduce()를 사용한 코드는 다음과 같다.  

```python
import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)  # 15 출력
```

functools.reduce()를 사용하면 reduce()에 선언한 람다 함수를 data요소에 차례대로 누적 적용하여 다음과 같이 계산한다.  

```
((((1+2)+3)+4)+5)
```

따라서 앞서 본 add()함수와 동일한 역할을 하게 된다.  

## operator.itemgetter

operator.itemgetter는 주로 sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 도와주는 모듈이다.  
예를들어 학생의 이름, 나이, 성적 등의 정보를 저장한 다음과 같은 students리스트가 있다고 하자.  

```python
students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]
```

students리스트에는 3개의 튜플이 있으며 각 튜플은 순서대로 이름, 나이, 성적에 해당하는 데이터로 이루어졌다. 이 리스트를 나이순으로 정렬하려면  
어떻게 해야 될까?  
이 문제는 다음처럼 sorted()함수의 key매개변수에 itemgetter()를 적용하면 쉽게 해결할 수 있다.  

```python
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(1))
print(result)
```

이 파일을 실행하여 출력해 보면 다음과 같이 나이 순서대로 정렬한 것을 확인할 수 있다.  

```python
[('sally', 17, 'B'), ('jane', 22, 'A'), ('dave', 32, 'B')]
```

itemgetter(1)은 students의 아이템인 튜플의 두번째 요소를 기준으로 정려하겠다는 의미이다. 만약 itemgetter(2)와 같이 사용한다면  
성적순으로 정렬한다. 이번에는 students의 요소가 다음처럼 딕셔너리일 때를 생각해 보자.  

```python
students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]
```

딕셔너리일 때도 마찬가지로 age를 기준으로 정렬해 보자. 이때도 마찬가지로 itemgetter()를 적용하면 된다. 단 이번에는  
itemgetter("age)처럼 딕셔너리의 키를 사용해야 한다. itemgetter("age")는 딕셔너리의 키인 age를 기준으로 정렬하겠다는 의미이다.  

```python
from operator import itemgetter

students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)
```

출력  결과는 다음과 같이 age순으로 정렬된 것을 확인할 수 있다.  

```python
[{'name': 'sally', 'age': 17, 'grade': 'B'}, {'name': 'jane', 'age': 22, 'grade': 'A'}, {'name': 'dave', 'age': 32, 'grade': 'B'}]
```

## shutil

shutil은 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈이다.  

작업 중인 파일을 자동으로 백업하는 기능을 구현하고자 c:\doit\a.txt 파일을 c:\temp\a.txt.bak이라는 이름으로 복사하는 프로그램을  
만들고자 한다. 어떻게 만들어야 할까? c:\doit 디렉터리에 a.txt 파일을 만드는 중이며 백업용 c:\temp 디렉터리는 이미 만들었다고 가정한다.  

다음은 shutil을 사용한 방법이다.  

```python
import shutil

shutil.copy("c:/doit/a.txt", "c:/temp/a.txt.bak")
```

## glob

가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다.  
이럴때 사용하는 모듈이 바로 glob이다.  

### 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)  

glob 모듈은 디렉터리 안의 파일들을 읽어서 리턴한다. *,?등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.  
다음은 C:/doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일을 모두 찾아서 읽어들이는 예이다.

```python
>>> import glob
>>> glob.glob("c:/doit/mark*")
['c:/doit\\marks1.py', 'c:/doit\\marks2.py', 'c:/doit\\marks3.py']
>>>
```

## pickle

pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다. 다음 예는 pickle 모듈의 dump함수를  
사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법을 보여준다.  

```python
>>> import pickle
>>> f = open("test.txt", 'wb')
>>> data = {1: 'python', 2: 'you need'}
>>> pickle.dump(data, f)
>>> f.close()
```

다음은 pickle.dump로 저장한 파일을 pickle.load를 사용해서 원래 있던 딕셔너리 객체(data)상태 그대로 불러오는 예이다.  

```python
>>> import pickle
>>> f = open("test.txt", 'rb')
>>> data = pickle.load(f)
>>> print(data)
{2:'you need', 1:'python'}
```

위 예에서는 딕셔너리 객체를 사용했지만 어떤 자료형이든 저장하고 불러올수 있다.  

## os

os모듈은 환경 변수나 디렉터리, 파일 등의 os 자원을 제어할 수 있게 해주는 모듈이다.  

### 내 시스템의 환경 변수 값을 알고 싶을 때 - os.environ

시스템은 제각기 다른 환경 변수 값을 가지고 있는데, os.environ은 현재 시스템의 환경 변수 값을 리턴한다. 다음을 따라 해 보자.  

```python
>>> import os
>>> os.environ
environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …})
>>>
```
os.environ은 환경 변수에 대한 정보를 딕셔너리 형태로 구성된 environ 객체로 리턴한다.  
자세히 보면 여러가지 유용한 정보를 찾을 수 있다.  

돌려받은 객체는 다음과 같이 호출히ㅏ여 사용할수 있다. 다음은 필자 시스템의 PATH 환경 변수 내용이다.  

```python
>>> os.environ['PATH']
'C:\\ProgramData\\Oracle\\Java\\javapath;...생략...'
```

### 디렉터리 위치 변경하기 - os.chdir

os.chdir를 사용하면 다음과 같이 현재 디렉터리 위치를 변경할 수 있다.  

```python
>>> os.chdir("C:\WINDOWS")
```

### 디렉터리 위치 돌려받기 - os.getcwd

os.getcwd는 현재 자신의 디렉터리 위치를 리턴한다.  

```python
>>> os.getcwd()
'C:\WINDOWS'
```

### 시스템 명령어 호출하기 - os.system  

시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수도 있다. os.system("명령어")처럼 사용한다. 다음은 현재 디렉터리에서  
시스템 명령어 dir을 실행하는 예이다.  

```python
>>> os.system("dir")
```

### 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen

os.popen은 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 리턴한다.  

```python
>>> f = os.popen("dir")
```

읽어 들인 파일 객체의 내용을 보기 위해서는 다음과 같이 하면 된다.  

```python
>>> print(f.read())
```

### 기타 유용한 OS 관련 함수

**함수**|**설명**|
---|---|
os.mkdir(디렉터리)| 디렉터리를 생성한다.|
os.rmdir(디렉터리)| 디렉터리를 삭제한다.|
os.unlink(파일)| 파일을 지운다.|
os.rename(src,dst)|src라인 이름의 파일을 dst라는 이름으로 바꾼다.|

## zipfile

zipfile은 여러 개의 파일을 zip 형식으로 합치거나 이를 해제할 떄 사용하는 모듈이다.  

다음과 같은 3개의 텍스트 파일이 있다고 하자.  

```python
a.txt
b.txt
c.txt
```

이 3개의 텍스트 파일을 하나로 합쳐 mytext.zip이라는 파일을 만들고, 이 파일을 원래의 텍스트 파일 3개로 해제하는 프로그램을 만들려면  
어떻게 해야할까?  

zipfile.zipFile()을 사용하여 해결해 보자.  

```
import zipfile

# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()
```

ZipFile 객체의 write() 함수로 개별 파일을 추가할 수 있고 extreactall() 함수를 사용하면 모둔 파일을 해제할 수 있다.  
합친 파일에서 특정 파일만 해제하고 싶다면 다음과 같이 extract()함수를 사용하면 된다.  

```python
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('a.txt')
```

만약 파일을 압축하여 묶고 싶은 경우에는 compression, compresslevel 옵션을 사용할 수 있다.  

```python
with zipfile.ZipFile('mytext.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
    (... 생략 ...)
```

compression에는 4가지 종류가 있다.  

- ZIP_STORED -> 압축하지 않고 파일을 Zip으로만 묶는다. 속도가 빠르다.
- ZIP_DEFLATED -> 일반적인 ZIP압축으로 속도가 빠르고 압축률은 낮다.(호환성이 좋다.)
- ZIP_BZIP2 -> bzip2 압축으로 압축률이 높고 속도가 느리다.
- ZIP_LZMA -> lzma 압축으로 압축률이 높고 속도가 느리다. (7zip과 동일한 알고리즘으로 알려져 있다.)

compressionlevel은 압축 수준을 의미하는 숫자값으로 1 ~ 9를 사용한다. 1은 속도가 가장 빠르고 압축률이 낮고, 9는  
속도가 가장 느리지만 최대 압축을 한다.  

## threading

컴퓨터에서 동작하고 있는 프로그램을 프로세스라고 한다. 보통 1개의 프로세스는 한가지 일만 하지만 스레드를 사용하면  
한 프로세스 안에서 2가지 또는 그 이상의 일을 동시에 수행할 수 있다.  

```python
# thread_test.py
import time

def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("working:%s\n" % i)

print("Start")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("End")
```

long_task 함수는 수행하는데 5초의 시간이 걸리는 함수이다. 위 프로그램은 이 함수를 총 5번 반복해서 수행하는 프로그램이다.  
이 프로그램은 5초가 5번 반복되니 총 25초의 시간이 걸린다.  

하지만 앞에서 설명했듯이 스레드를 사용하면 5초의 시간이 걸리는 long_task 함수를 동시에 실행할 수 있으니 시간을 줄일 수 있다.  

다음과 같이 프로그램을 수정해 보자.  

```python
# thread_test.py
import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t) 

for t in threads:
    t.start()  # 스레드를 실행한다.

print("End")
```

이와 같이 프로그램을 수정하고 실행해 보면 25초 걸리던 작업이 5초 정도에 수행되는 것을 확인할 수 있다. threading.Thread를 사용하여 만든  
스레드 객체가 동시 작업을 가능하게 해주기 때문이다.  

하지만 위 프로그램을 실행해 보면 "Start"와 "End"가 먼저 출력되고 그 이후에 스레드의 결과가 출력되는 것을 확인할 수 있다. 그리고 프로그램이  
정상 종료되지 않는다. 우리가 기대하는 것은 "Start"가 출력되고 그다음에 스레드의 결과가 출력된 후 마지막으로 "End"가 출력되는 것이다.  

```python
# thread_test.py
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")
```

스레드의 join 함수는 해당 스레드가 종료될 때까지 기다리게 한다. 따라서 위와 같이 수정하면 우리가 원하던 출력을 보게 된다.
