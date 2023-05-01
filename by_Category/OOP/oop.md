# 객체지향 프로그래밍에 대하여
## 등장 배경
프로그램이 점차 거대해지면서 개발과 테스트가 점점 어려워졌다. 이를 해결하기 위해 패러다임의 변화가 필요했다.

## 객체(Object)
인간이 현실 세계를 인지하는 방법을 적용 - 객체들로 구성된 세상

## 객체지향의 개념과 객체지향 프로그래밍 요소
객체-상태-행동 => 클래스-속성-메소드

## 객체지향의 여러 속성
>클래스, 메시지전달, 상속, 추상화, 캡슐화, 다형성

## 1. 클래스와 인스턴스
> 틀과 풀빵

클래스는 인스턴스를 만들어내기 위한 개념적 존재이자 설계도이다. 즉 인스턴스의 속성과 동작을 정의한다.

객체는 클래스의 인스턴스이고, 클래스에 의해 정의된 속성과 동작를 가진다. 객체는 서로 상호작용할 수 있다.

같은 클래스에서 생성된 객체들은 같은 속성과 메소드를 가지지만, 서로 다른 값을 가질 수 있다.



```python
class Car:
    color='red'
    def drive(self):
        print("Brrrr")
my_car = Car()
print(my_car.color)
my_car.drive()
```

### Dunder method
특수한 기능을 하는 메소드들. 
(\_\_init\_\_, \_\_call\_\_ 등) 

dir(<obj>)로 확인가능하다.
```python
def __init__(self): # 객체가 생성될 때 실행된다
def __srt__(self): # 객체가 str화할 때(출력할때) 동작
def __call__(self): # 객체가 호출될 때 동작
```
**Self 뜻 다시보기**
## 2. 캡슐화
### .get_speed() vs .speed
```python
class Car:
    def __init__(self,model,color,speed):
        self.model=model
        self.color=color
        self.speed=speed
        self.speed_limit=speed*2
    def accelerate(self,dv):
        dv = 0 if 0>dv else dv
        self.speed =min(self.speed_limit, self.speed + dv)
    def brake(self,dv):
        dv = 0 if 0>dv else dv
        self.speed =max(0, self.speed - dv)
    def get_speed(self):
        return self.speed
    color='red'
    def drive(self):
        print("Brrrr")
my_car = Car()
print(my_car.color)
my_car.drive()
```
**데이터와 그 데이터를 다루는 메서드들을 하나로 묶는 것**을 캡슐화라고 한다.

캡슐화된 객체는 외부에서 직접적으로 접근할 수 없으며, **메서드를 통해서만 데이터를 조작**할 수 있다. 이를 통해 데이터의 **보안성과 안정성**을 높일 수 있다.

또한 속성을 단순히 조회만 하는 것이 아니라 기능을 추가하여 조회할 수도 있다.
```python
# 예시 : 단위 변환해 조회
def get_speed(self,uint='mph'):
    if unit == 'mph':
        return self.speed
    elif unit == 'kph':
        return self.speed*100
    else:
        raise ValueError()
```
### getter, setter
객체 내의 중요한 데이터는 외부의 직접접근을 제한하고 getter(조회)와 setter(변경)을 통해 안전하게 접근하는 것이 권장됨.

## 3. 상속
이미 정의된 클래스에서 속성과 메소드를 물려받아 새 클래스를 생성하는 것을 말한다.

예시) Django User
models.Model -> AbstractBaseUser(인증) -> Abstractuser(필드) -> User(다시 보기)

코드 재사용율을 높이고, 계층적인 구조를 만들 수 있다.
## 4. 다형성
오버라이딩 등을 통해 같은 이름의 메서드를 실행시켜도 다른 동작을 하는 것이 다형성이다. 코드의 가독성과 유지보수성을 높여준다.

```python
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print(f"{self.name}, the animal makes some noise.")

class Dog(Animal):
    def __init__(self,name,age,breed):
        self.dog_breed=breed
        super().__init__(name,age)
    def speak(self):
        print(f"{self.name}, the dog barks. Bow-Wow!")
class Cat(Animal):
    def __init__(self,name,age,breed):
        self.cat_breed=breed
        super().__init__(name,age)
    def speak(self):
        print(f"{self.name}, the cat says, Meow Meow!")
```

fk제외하고 첫번째 인자가 verbose_name을 받는걸로 알고있습니다
## 5. 추상클래스
어떤 식으로 사용할지 미리 명시되어있기만한 빈 매서드가 정의된 부모 클래스. 실제로 객체로 만들 일이 없는 클래스이다.
```python
# 추상 클래스
class Shape:
    def get_area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return 3.14*self.radius**2
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def get_area(self):
        return self.side**2
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return self.width*self.height
    
