## 사용자 입력

사용자가 입력한 값을 어떤 변수에 대입하고 싶을 떄는 어떻게 해야 할까?  

### input의 사용
```python
>>> a = input()
Life is too short, you need python
>>> a
'Life is too short, you need python'
>>>
```

input은 입력되는 모든 것을 문자열로 취급한다.  

### 프롬프트를 띄워서 사용자 입력 받기

사용자에게 입력받을 떄 "숫자를 입력하세요"라든지 "이름을 입력하세요" 라는 안내 문구 또는 질문이 나오도록 하고 싶을 떄가 있다.  
그럴 때는 input()의 괄호 안에 질문을 입력하여 프롬프트를 띄워주면 된다.  
> input("질문내용")

다음 예를 직접 입력해 보자.
```python
>>> number = input("숫자를 입력하세요: ")
숫자를 입력하세요:
```
위와 같은 질문을 볼수 있을 것이다.

숫자를 입력하라는 프롬프트에 3을 입력하면 변수 number에 3이대입된다. print(number)로 출력해서 제대로 입력되었는지 확인해보자.  

```python
>>> number = input("숫자를 입력하세요: ")
숫자를 입력하세요: 3
>>> print(number)
3
>>>
```

input은 입력되는 모든 것을 문자열로 취급하기 때문에 number는 숫자가 아닌 문자열임에 주의하자.  
```python
>>> type(number)
<class 'str'>
>>>
```

## print 자세히 알기
지금껏 print문이 수행해 온 일은 우리가 입력한 자료형을 출력하는 것이었다. print의 사용예는 다음과 같다.  

```python
>>> a = 123
>>> print(a)
123
>>> a = "Python"
>>> print(a)
Python
>>> a = [1, 2, 3]
>>> print(a)
[1, 2, 3]
```
이제 print문으로 할 수 있는 일에 대해서 조금 더 자세하게 알아보자.  

### 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다

```python
>>> print("life" "is" "too short") # 1
lifeistoo short
>>> print("life"+"is"+"too short") # 2
lifeistoo short
```
위 예에서 1과 2는 완전히 동일한 결과값을 출력한다. 죽 따옴표로 둘러싸인 문자열을 연속해서 쓰면 + 연산을 한 것과 같다.  

### 문자열 띄어쓰기는 콤마로 한다

```python
>>> print("life", "is", "too short")
life is too short
```
콤마(,)를 사용하면 문자열 사이에 띄어쓰기를 할수 있다.

### 한줄에 결과값 출력하기

앞절의 구구단 프로그램에서 보아쓷ㅅ이 한 줄에 결과값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다.  

```python
>>> for i in range(10):
...     print(i, end=' ')
...
0 1 2 3 4 5 6 7 8 9
```
