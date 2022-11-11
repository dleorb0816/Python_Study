## 함수란 무엇인가?

함수란 입력값을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓는 것.  

## 파이썬 함수의 구조

파이썬 함수의 구조는 다음과 같다.  

```python
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
```

def는 함수를 만들 떄 사용하는 예약어이며, 함수 이름은 함수를 만드는 사람이 임의로 만들수 있다.  
함수 이름 뒤 괄호 안의 매개 변수는 이 함수에 입력으로 전달되는 값을 받는 변수이다. 이렇게 함수를 정의한 다음 if, while, for문 등과  
마찬가지로 함수에서 수행할 문장을 입력한다.  

간단하지만 많은 것을 설명해 주는 다음 예를 보자.  

```python
def add(a, b): 
    return a + b
```

이 함수는 다음과 같이 풀이된다.  
> "이 함수의 이름(함수 이름)은 add이고 입력으로 2개의 값을 받으며 결괏값은 2개의 입력값을 더한 값이다."

여기에서 return은 함수의 결괏값을 돌려주는 명령어이다. 먼저 다음과 같이 add 함수를 만들자.  

```python
>>> def add(a, b):
...     return a+b
...
>>>
```
add함수 사용

```python
>>> a = 3
>>> b = 4
>>> c = add(a, b)
>>> print(c)
7
```

변수 a에 3, b에 4를 대입한 다음 앞에서 만든 add함수에 a와 b를 입력 값으로 넣어 준다. 그리고 변수 c에 add함수의 결괏값을 대입하면  
```print(c)```로 c의 값을 확인할 수 있다.  

## 매개변수와 인수

매개변수(parameter)dhk 인수(argument)는 혼용해서 사용되는 헷갈리는 용어이므로 잘 기억해 두자.  
매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.  

## 입력값과 결괏값에 따른 함수의 형태

함수는 들어온 입력값을 받아 어떤 처리를 하여 적절한 결괏값을 돌려준다.  
> 입력값 ---> **함수** ----> 결괏값
함수의 형태는 입력값과 결괏값의 존재 유무에 따라 4가지 유혁으로 나뉜다. 자세히 알아보자.

### 일반적인 함수

입력값이 있고 결괏값이 있는 함수가 일반적인 함수이다. 대부분 다음과 비슷한 형태일 것이다.  

```python
def 함수이름(매개변수):
    <수행할 문장>
    ...
    return 결과값
```

다음은 일반함수의 전형적인 예이다.  