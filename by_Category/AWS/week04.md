## 1. Scalability vs Availability

>**Scalability(확장성): 시스템이 커지거나 작아질 수 있는 능력** 
<br><br>
사용자 수, 데이터 양, 처리량 등이 증가할 때 시스템의 성능과 처리 능력을 유지하거나 향상시키는 능력. 확장성 있는 시스템 디자인과 구현이 필요하다.

>**Availability(가용성): 시스템이 정상적으로 작동하고 사용 가능한 상태를 유지하는 능력**
<br><br>
여러 가용 영역에 애플리케이션 및 인프라를 배포함으로써 서비스를 항상 이용 가능한 상태로 유지하는 것. 시스템의 안정성을 높이고 장애 대응 능력을 강화하는 것이 중요하다.
<br>ex: 여러AZ에서 서비스 실행

둘 다 중요한 개념이며, 분산 시스템을 설계하고 구현할 때 모두 고려해야 한다.

### Horizonatal / Vertical Scalability
수평적 확장은 인스턴스, 서버 등을 여러개로 늘리는 것을 밀한다.(scale-out) 

수직적 확장은 인스턴스의 성능을 향상 시키는 등의 방식으로 확장성을 확보한다.(scale-up)

## 2. Elastic Load Balancer
유저의 요청이 몰릴 때, 요청을 받아 EC2들에게 요청을 분산시켜 할당한다.
1. 요청을 분산해준다(EC2와 연동)
2. 단일 엔드 포인트 제공(route 53): 유저가 일일히 인스턴스마다 다른 ip로 접속하지 않아도 된다.
3. 인스턴스 헬스체크
4. HTTPS 제공(ACM과 연동)
5. 고가용성 제공
6. 공개 트래픽(사용자~ELB)과 내부 트래픽(ELB~EC2)을 분리해 보안강화

### ELB의 종류
* Classic Load Balancer: ELB 이전 세대의 로드 밸런서로 잘 사용되지 않는다.(deprecated) 
* Application Load Balancer: application 계층(HTTP, FTP...)에서 라우팅 결정을 내린다. 따라서 url, 쿼리스트링, 헤더 등 사용자 요청을 기준으로 분산이 가능하다. 
가장 많이 쓰인다.
* Network Load Balancer: TCP/전송계층(4)에서 트래픽을 라우팅한다. 데이터의 내용을 들여다보지 않아 복호화할 필요가 없고 포트번호, 전송 프로토콜에 따라 트래픽을 나누는데, 따라서 속도가 빠르지만 섬세한 라우팅은 불가능하다.
* Gateway Load Balancer: 방화벽, 서드파티 어플리케이션등을 사용할 때 쓴다.
### ELB의 보안그룹
ELB의 보안그룹 설정은 user와 ELB 사이의 보안그룹/ ELB와 인스턴스들 사이의 보안그룹을 설정해야한다. 전자는 모든 src ip 에서의 80,443번 포트 접속을 허용해주면된다.

후자는 조금 특이한데, 인스턴스들을 오직 로드밸런서에게만 공개하는 형태로 설정한다. 또한 src IP가 아니라 특정 보안그룹을 출처로 허용할 수 있다.

### ALB 사용해보기
#### 0. ALB의 속성
    * http 요청을 여러 타깃 그룹(EC2,EC2 그룹 등)에 나누어 줄 수 있음
    * 한 머신 안에서도 여러 어플리케이션에 나눠 줄 수 있음
    * HTTP/2 및 웹소켓 지원
    * HTTPS로 리다이렉트 지원
    * URL, hostname, 쿼리스트링, 헤더 등에 기반해 다른 타깃 그룹으로 보낼 수 있다.
#### 1. 인스턴스 여러개 편하게 만들기 - userdata

작성해두면 인스턴스 시작 후 자동으로 실행되는 
bash 명령어를 지정하여, 여러개의 인스턴스를 만들 때 한번에 동일하게 설정할 수 있다.
```python
#!/bin/bash
apt-get update
apt-get install -y nginx
cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to Nginx</title>
</head>
<body>
<h1>Hello World!</h1>
<p>AWS deployed by Me!</p>
<p>private ip is $(hostname -f)</p>
</body>
</html>
EOF
sudo systemctl start nginx
```

#### 2. ELB 만들고 설정하기
create load balancer - ALB 선택
internet-facing, IPv4 선택
mapping에 모든 zone 추가

**보안 그룹 설정**
외부 사용자~ELB간의 보안 설정이다. 인바운드 규칙에서 80번(HTTP) 포트만 모든 src IP에 대해 허용한다.

**target group**
인스턴스를 선택하여 새로운 타겟그룹을 만든다. 타겟 그룹에 처음에 생성한 인스턴스들을 넣고 타겟그룹을 ELB와 연결한다.


## 2. ELB에서 SSL(TLS) 적용하기
SSL(TLS)은 인터넷 상에서 정보를 안전하게 전송하기 위한 프로토콜이다. 개인정보 보호, 데이터 무결성, 식별(identification)을 보장한다.  서버와 클라이언트 간의 안전한 접속을 만들어주며 전송 데이터를 암호화하여 안전성을 보장한다.

### ? - 안전한 키 공유
암호화를 위한 대칭키는 서버와 클라이언트가 함께 가지고 있어야하는데, 이를 해커가 감청하고 있을 수 있는 네트워크를 통해 보낼 수는 없는 노릇이다.

이를 해결하기 위해 비대칭키(공개키-비밀키) 알고리즘을 사용한다. 하지만 이는 리소스를 많이 사용한다.

### ! - 대칭키를 비대칭 키로 전달하자
브라우저가 요청을 보내면 서버는 CA로 부터 인증 받은 '공개키가 포함된 인증서'를 브라우저에게 보낸다. 브라우저는 이 공개키를 이용해 대칭키(사전 마스터 키)를 암호화 해 서버에 보내고, 서버는 이를 비밀키로 복호화해 사전 마스터 키를 얻는다.

\*CA는 인증서를 발급하고, 인증서의 소유자의 신원을 보증하며, 인증서가 유효하다는 증거를 제공하는 조직이다.

### ELB에 HTTPS 적용
user-ELB 간의 연결에 적용하면 된다. ELB-targetgruop은 내부 사설망이므로 외부에서 접근할 수 없어 http 통신을 해도 된다.

1. 도메인 받기: route 53 등 사용
2. ACM에서 도메인에 대한 인증서 발급받기
3. ALB 에서 Add listener -> protocol: https, security
