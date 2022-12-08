# 내장 함수

## abs

abs(x)는 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 리턴하는 함수이다.  

```python
>>> abs(3)
3
>>> abs(-3)
3
>>> abs(-1.2)
1.2
```

## all

all(x)는 반복 가능한(iterable) 데이터 x를 입력 값으로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다.  

> 반복 가능한 데이터란 for 문에서 사용 가능한 자료형을 의미한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.


```python
>>> all([1, 2, 3])
True
```
리스트 [1, 2, 3]은 모든 요소가 참이므로 True를 리턴한다.  

```python
>>> all([1, 2, 3, 0])
False
```
리스트 [1, 2, 3, 0] 중에서 요소 0은 거짓이므로 False를 리턴한다.

```python
>>> all([])
True
```
만약 all의 입력 인수가 빈 값인 경우에는 True를 리턴한다.

## any

any(x)는 반복 가능한(iterable) 데이터 x를 입력으로 받아 x의 요소 중 하나라도 참이 있으면 True를 리턴하고, x가 모두 거짓일 때에만 False를 리턴한다.  
all(x)의 반대이다.  

```python
>>> any([1, 2, 3, 0])
True
```
리스트 [1, 2, 3, 0] 중에서 1, 2, 3이 참이므로 True를 리턴한다.  

```python
>>> any([0, ""])
False
```
리스트 [0, ""]의 요소 0과 ""은 모두 거짓이므로 False를 리턴한다.  

```python
>>> any([])
False
```
만약 any의 입력 인수가 빈 값인 경우에는 False를 리턴한다.  

## chr

chr(i)는 유니코드 숫자값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수이다.  
> 유니코드는 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준이다.

```python
>>> chr(97)
'a'
>>> chr(44032)
'가'
```

## dir

dir은 객체가 지닌 변수나 함수를 보여 주는 함수이다. 다음 예는 리스트와 딕셔너리가 지닌 함수(메서드)를 보여 주는 예이다.  

```python
>>> dir([1, 2, 3])
['append', 'count', 'extend', 'index', 'insert', 'pop',...]
>>> dir({'1':'a'})
['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]
```

## divmod  

divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴하는 함수이다.  

```python
>>> divmod(7, 3)
(2, 1)
```
몫을 구하는 연산자 //와 나머지를 구하는 연산자 %를 각각 사용한 결과와 비교해 보자.  
```python
>>> 7 // 3
2
>>> 7 % 3
1
```

## enumerate
enumerate는 "열거하다"라는 뜻이다. 이 함수는 순서가 있는 데이터(리스트, 튜플,문자열)을 입력으로 받아 인덱스 값을 포함하는  
enumerate객체를 리턴한다
> 보통 enumerate 함수는 다음 예제처럼 for문과 함께 사용한다.

다음 예를 보자.  
```python
>>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar
``` 
순서 값과 함꼐 body,foo,bar가 순서대로 출력되었다. 즉 위 예제와 같이 enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와  
그 값을 쉽게 알 수 있다.  

for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할떄 enumerate함수를 사용하면 매우 유용하다.  

## eval

eval(expression)은 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴하는 함수이다.  

```python
>>> eval('1+2')
3
>>> eval("'hi' + 'a'")
'hia'
>>> eval('divmod(4, 3)')
(1, 1)
```

## filter

filter란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 이와 비슷한 기능을 한다.  
> filter(func,iterable)
filter함수는 첫 번째 인수로 함수를, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다. 그리고 가능한 데이터(iterable)의  
요소 순서대로 함수(func)를 호출했을 때 반환 값이 참인 것만 묶어서 리턴한다.

```python
#positive.py 
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))
```
> 결괏값:[1,2,6]

위에서 만든 positive 함수는 리스트를 입력으로 받아 각각의 요소를 판별해서 양수 값만 리턴하는 함수이다.  
filter 함수를 사용하면 위 내용을 다음과 같이 간단하게 작성할 수 있다.  

```python
#filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
```
> 결괏값:[1,2,6]

fiter(positive, [1,-3,2,0,-5,6])는 [1,-3,2,0,-5,6])는 [1,-3,2,0,-5,6]의 각 요소값을 순서대로 positive 함수에 적용하여  
반환 값이 참인 것만 묶어서 리턴한다. 즉 1,2,6 요소만 x > 0문장이 참이 되므로 [1,2,6]이라는 결괏값이 출력된다.  

이함수는 lambda를 사용하면 더욱 심플해진다.  

```python
>>> list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
[1, 2, 6]
```
