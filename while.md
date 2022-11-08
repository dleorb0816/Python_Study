## while문

### while문의 기본 구조

반복해서 문장을 수행해야 할 경우 while문을 사용.  

while문의 기본구조  

```python
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```

while문은 조건이 참인동안에 while문 아래의 문장이 반복해서 수행됨.  

"열 번 찍어 안 넘어가는 나무 없다"는 속담을 파이썬 프로그램으로 만든다면 다음과 같이 될 것이다.  

```python
>>> treeHit = 0
>>> while treeHit < 10:
...     treeHit = treeHit +1
...     print("나무를 %d번 찍었습니다." % treeHit)
...     if treeHit == 10:
...         print("나무 넘어갑니다.")
...
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.
```

위에서 while문의 조건문은 ```treeHit < 10```이다. 즉 10보다 작은 동안에 while문 안의 문장을 계속 수행한다.  
while문 안의 문장을 보면 제일 먼저 ```treeHit = treeHit + 1```로 treeHit값이 계속 1씩 증가. 그리고 나무를  treeHit번만큼 찍었음을  
알리는 문장을 출력하고 treeHit가 10이 되면 "나무 넘어갑니다."라는 문장을 출력.  

> treeHit = treeHit + 1은 프로그래밍을 할 때 매우 자주 사용하는 기법이다. treeHit 값을 1만큼씩 증가시킬 목적으로 사용하며,
> treeHit += 1처럼 사용하기도 한다.


### while문 만들기

이번에는 여러가지 선택지중 하나를 선택해서 입력받는 예제를 만들어 보자. 먼저 다음과 같이 여러 줄짜리 문자열을 입력한다.

```python
>>> prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """
>>>
```

이어서 number변수에 0을 먼저 대입한다. 이렇게 변수를 먼저 설정해 놓지 않으면 다음에 나올 while문의 조건문인 ```number != 4```에서  
변수가 존재하지 않는다는 오류가 발생한다.  

```python
>>> number = 0
>>> while number != 4:
...     print(prompt)
...     number = int(input())
...

1. Add
2. Del
3. List
4. Quit

Enter number:
```

while문을 보면 number가 4가 아닌동안 prompt를 출력하고 사용자로부터 번호를 입력받는다. 다음결과 화면처럼 사용자가 값 4를  
입력하지 않으면 계속해서 prompt를 출력한다

> 여기에서 number = int(input())는 사용자의 숫자 입력을 받아들이는 것이라고만 알아두자. int나 input함수에 대한 내용은
> 뒤의 내장 함수 부분에서 자세하게 다룬다.

```python
Enter number:
1

1. Add
2. Del
3. List
4. Quit
```

4를 입력하면 조건문이 거짓이 되어 while문을 빠져나가게 된다.  
```python
Enter number:
4
>>>
```
