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

## hex

hex(x)는 정수를 입력받아 16진수(hexadecimal)문자열로 변환하여 리젙하는 함수.

```python
>>> hex(234)
'0xea'
>>> hex(3)
'0x3'
```

## id

id(object)는 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴하는 함수이다.  

```python
>>> a = 3
>>> id(3)
135072304
>>> id(a)
135072304
>>> b = a
>>> id(b)
135072304
```

위예의 3,a,b는 고유 주소 값이 모두 135072304이다. 죽 3,a,b가 모두 같은 객체를 가리키고 있다.  
만약 id(4)라고 입력하면 4는 3,a,b와 다른 객체이므로 당연히 다른 고유 주소 값이 출력된다.  

```python
>>> id(4)
135072292
```

## input

input([prompt])은 사용자 입력을 받는 함수이다. 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.  
>> ```[]```기호는 괄호 안의 내용을 생략할 수 있다는 관례 포기법임을 기억하자.

```python
>>> a = input()
hi
>>> a
'hi'
>>> b = input("Enter: ")
Enter: hi
>>> b
'hi'
```

## int

int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수이다. 만약 정수가 입력되면 그대로 리턴한다.  
```python
>>> int('3')
3
>>> int(3.4)
3
```

int(x, radix)는 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다. 예를 들어 2진수로 표현된 "11"의 10진수 값은 다음과  
같이 구할수 있다.  

```python
>>> int('11', 2)
3
```

16진수로 표현된 "1A"의 10진수 값은 다음과 같이 구할수 있다.  

```python
>>> int('1A', 16)
26
```

## isinstance

isinstance(object, class)함수는 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받는다. 입력으로 받은 객체가 그 클래스의 인스턴스인지를 판단하여  
참이면 True, 거짓이면 False를 리턴한다.  

```python
>>> class Person: pass
...
>>> a = Person()
>>> isinstance(a, Person)
True
```

위 예는 a 객체가 Person클래스에 의해 생성된 인스턴스임을 확인시켜 준다.  

```python
>>> b = 3
>>> isinstance(b, Person)
False
```

b는 Person클래스가 만든 인스턴스가 아니므로 False를 리턴한다.  


## len

len(s)은 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다.  

```python
>>> len("python")
6
>>> len([1,2,3])
3
>>> len((1, 'a'))
2
```

## list

list(iterable)는 반복 가능한 데이터(iterable)를 입력받아 리스트로 만들어 리턴하는 함수이다.  

```python
>>> list("python")
['p', 'y', 't', 'h', 'o', 'n']
>>> list((1,2,3))
[1, 2, 3]
```

list함수에 리스트를 입력하면 똑같은 리스트를 복사하여 리턴한다.

```python
>>> a = [1, 2, 3]
>>> b = list(a)
>>> b
[1, 2, 3]
```

## map

map(f,iterable)은 함수(f)와 반복가능한 데이터를 입력으로 받는다. map함수는 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴하는 함수.  

다음 예를 보자.  

```python
# two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)
```

two_times함수는 리스트를 입력받아 리스트의 각 요소에 2를 곱해 리턴하는 함수이다. 실행 결과는 다음과 같다.  
>> 결과값:[2,4,6,8]

위 예제는 map함수를 사용하여 다음처럼 바꿀수 있다.

```python
>>> def two_times(x): 
...     return x*2
...
>>> list(map(two_times, [1, 2, 3, 4]))
[2, 4, 6, 8]
```

이 예제를 해섯해 보자. 먼저 리스트의 첫 번쨰 요소인 1이 two_times 함수의 입력값으로 들어가고 ```1*2```의 과정을 거쳐서 2가 된다.  
다음으로 리스트의 두 번째 요소인 2가 ```2 * 2```의 과정을 거쳐 4가 된다. 따라서 결괏값은 이제 [2,4]가 된다. 총 4개의 요솟값이 모두  
수행되면 [2,4,6,8]이 된다. 이것이 map함수가 하는 일이다.  

>> 위 예에서 map함수의 결과를 리스트로 출력하기 위해 list함수를 사용했다. (map)함수는 map객체를 리턴한다.)

앞의 예는 lambda를 사용하여 다음처럼 간략하게 만들 수 있다.  

```python
>>> list(map(lambda a: a*2, [1, 2, 3, 4]))
[2, 4, 6, 8]
```

