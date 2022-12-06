# 예외 처리

## 오류는 어떤 때 발생하는가?

오류를 처리하는 방법을 공부하기 전에 어떤 상황에서 오류가 발생하는지 한번 알아보자. 오타를 입력했을때 발생하는 구문  
오류 같은 것이 아닌 실제 프로그램에서 자주 발생하는 오류를 중십으로 살펴보자.  

먼저 존재하지 않는 파일을 사용하려고 시도했을 때 발생하는 오류이다.  

```python
>>> f = open("나없는파일", 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
```

위 예에서 볼 수 있듯이 없는 파일을 열려고 시도하면 FileNotFoundError 오류가 발생한다.  

이번에는 0으로 다른 숫자를 나누는 경우를 생각해 보자. 이 역시 자주 발생하는 오류이다.  

```python
>>> 4 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

4를 0으로 나누려니까 ZeroDivisionError 오류가 발생한다.  

마지막으로 한 가지 예를 더 들어보자. 다음 오류는 정말 빈번하게 일어난다.  

```python
>>> a = [1,2,3]
>>> a[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

a는 리스트 [1,2,3]이므로 a[4]는 a리스트에서 얻을 수 없는 값이다. 따라서 IndexError 오류가 발생한다. 파이썬은 이런 오류  
가 발생하면 프로그램을 중단하고 오류 메시지를 보여 준다.

