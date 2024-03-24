# ERD
Entity Relationship Diagram

> 고연차, 숙련개발자인지 판단하는 척도

하지만 일단 ERD를 잘 그려서 프로젝트를 어필하는 자리에 넣으면 좋은 무기가 될 수 있다. 그리고 언젠가는 해야하니 배우는 게 이득이다.

## 0. 잘 작성하는 법
1. 연습 많이 하기
2. 추상화,논리,비식별관계 등의 단어에 겁먹지 말라: 이론과 실제는 다르다.
3. 자신이 관심있는 서비스나 영역의 ERD를 그려보면서 연습

## 1. PK/FK
**프라이머리-키는** 중복된 값을 가지지 않는다.(unique) 따라서 **한 레코드를 대표하여 식별**할 수 있는 값을 가진 필드이다.

대개 정수형태며, 번호 혹은 유일한 값을 지정함.
<hr>

**외래키는** **다른 테이블의 PK를 참조**하는 필드이다. 즉 타 테이블의 PK 데이터를 확보한다.

**PK/FK를 활용하지 않으면** 불필요하거나 중복된 데이터를 보유하게 되고 테이블읠 칼럼(필드)가 계속 증가하게 된다.

ex) 아티클 마다 유저 데이터 따로 적어주기

## 2. 일대일 관계
- 어느 데이터에 종속되는 데이터가 하나만 있을 때 사용
    > 예시: 사용자와 프로필의 관계

- 장고에서는 OnetoOneField()
- 그러나 보통 **ForeignKey with unique=True**로 구현, 
현재 장고에서는 이렇게 작성하는 것을 **추천**


## 3. 일대다 관계
- 어느 데이터에 종속되는 데이터가 여러개 있을 때 사용
    > 예시: 사람과 은행계좌의 관계. 
    <br>나는 여러개의 계좌를 가질 수 있지만 계좌는 여러 주인을 가질 수 없다.
- 장고에서는 **ForiegnKey()**

## 4. 다대다 관계
- 어느데이터에 종속되는 데이터가 여러개 있고 다른 데이터에도 종속될 수 있음.
    > 예시: 회사원과 회의 세션의 관계.
- 일대다 관계로 양쪽이 연결된 임시 테이블(양쪽의 PK만 필드로 가짐)로 구현
- Django에서는 ManyToManyField 지원하지만 한계가 존재하므로 **forienkey를 이용해 구현**한다.

## 5. 식별/비식별관계
식별관계는 외래키가 PK역할도 같이 해주는 경우를 말한다. 비식별관계는 왜래키가 PK 역할을 하지 않는다.

```python
# 식별관계, onetoone
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, primary_key=True, unique=True)# null=False(기본)
    grade = models.IntegerField()

```
식별 관계는 반드시 왜래키의 데이터에 종속되어야 한다 (예시: 군인은 반드시 소속이 있다)
```python
class Soldier(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
# Department(부모)의 데이터가 먼저 만들어져야 한다.
```
비식별 관계는 반드시 종속될 필요가 없다.(예시: 회사원은 소속 부서가 없을 수 있다.)
```python
class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SETNULL, null=True)
# Department의 데이터를 반드시 필요로 하지 않음
```

**구상할 때** 이렇게 누락되어도 되는지, 누락된 값이 존재할 때 어떻게 처리를 할것인지 **미리 고민**해보아야 한다.

### 둘중 선택하기
1. 두 데이터간의 종속성이 강할 경우엔 식별관계로 지정하는 것이 편하다.
2. 하나의 데이터를 날려버려도 다른데이터가 의미를 잃지않고 재사용가능하면 비식별 관계로 지정하는 것이 편하다.
### 현업에서는...
대부분의 관계는 비식별 관계로 처리하게 되는 경향이 있다. (데이터 정합성, 구현/운영의 용이성)
> **Q**:그러면 비식별관계에서 on_delete=CASCADE 옵션을 안 적용해줘도 괜찮지 않을까요?<br><br>
**A**:네. on_delete 옵션의 다양성도 참고해보세요. models.CASCADE(기본), models.SET_NULL, models.PROTECT 등

### 비식별관계에서의 조인연산(select_related)
```python
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

posts = Post.objects.select_related('author').all()

for post in posts:
    print(post.title, post.content, post.created_at, post.updated_at, post.author.name, post.author.email)

```
# 연습
## 스벅 메뉴판 보면서 구상하기
1. 카테고리
2. 상세분류 - 신규출시, 시즌한정, 지역한정
3. 음료의 이미지들
4. 음료 설명, 영양정보

* 음료-이미지: 일대다
* 메뉴-카테고리-음료: 다대다(일대다대일)
* 알러지-음료/알러지테이블-음료: 다대다(일대다대일)
* 영양정보-음료: 일대일(unique=True)

> **컨벤션 - 테이블 명은 항상 복수로 해주자**

### 구상할 때 유심히 볼 부분
- 일대일/일대다/다대다 관계 찾기
- 자료형(Data Type), Nullable 확인
- 테이블 공통 field 확인 (예: created_at, updated_at) 클래스 상속이용해 중복 줄일 수 있다.
- 추가로 분리 가능한 데이터 찾기: 예시 - 제주한정, 시즌한정 여부(추후 필드 자체가 의미없어질 수 있음) => 특성테이블 따로 개설해 정합성 확보 가능

## 새마을식당 보면서 구상하기
1. DB가 필요한 것과 아닌것 구분
2. 없어질 수도 있는것은 데이터로 관리
3. 카테고리 테이블
4. 음식 테이블-pk,이미지,이름,설명,카테고리
5. 매장테이블-명칭, 위치, 상세주소,전화번호, 영업시간,휴일,주차,좌석,이미지


# Q&A
1. restful과 ERD의 연결고리?<br>그런거는 없다.
2. 장고에서 모델을 시각화하는 라이브러리 존재하므로 이용하면 좋다.(추후공유)
3. ERD를 잘 읽는 법: 모든 서비스에서 코어가 되는 테이블들이 반드시 존재한다. 보통 이러한 테이블을 중점으로 확장하는 식으로 개발이 이루어지니 읽을 때도 비슷한 순서로 관계를 보면 된다.
4. 레코드가 너무 많을 때 테이블을 분리하는 하는 경우는 별로 없다. 조회시 어느 테이블을 봐야할지 옵션을 정해야하기 때문.
5.  같은 테이블에서 다대다관계인 경우: pk만 있는 테이블에 두번 일대다로 표현하면 될것 같다.
