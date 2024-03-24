## 관계형 DB를 위한 서비스 - RDS

SQL을 쿼리어로 사용하는 관계형 DB를 위한 서비스이다.

EC2 상에 DB를 만들어 사용할 수 있지만 RDS가 나은점은 다음과 같다:

1.  DB를 위한 인프라 자동 구축/업데이트
2.  지속적인 백업과 복구 지원 - 서버와 분리되어 더 엄중한 보호와 관리를 받아야한다.
3.  모니터 대시보드 지원 - 트래픽 등을 시각적으로 확인가능
4.  성능향상을 위한 read-replicas 지원
5.  Multi AZ 지원(고가용성)
6.  수평/수직 확장성
7.  EBS 백업 지원

단점은 SSH로 접속이 불가능하여 서비스 중간에 RDS를 새로 적용하기는 어렵다는 것이다.

## RDS의 기능 - Storage Auto Scaling

DB용량의 한계치에 도달할 때 자동으로 용량을 늘려준다.(수직 확장성)

단, 최대 용량 한계치를 지정해줘야한다. 예측 불가능한 트래픽이 있을 때 유용하다.

### Read Replica



  
실제 서비스에서 DB에는 write보다 read 요청이 압도적으로 많이 온다. 따라서 읽기전용 복제 DB를 만들어서 read 요청을 분산 시킬 수 있다. 단, write를 반영하는 데에는 원본 DB 보다 느릴 수 있다.

read replica는 SQL 문중 오직 Select만 처리가능하며 insert, update, delete는 처리하지 못한다.

### multi AZ



  
말 그대로 다른 AZ에 백업을 한다. 수동설정이 필요없다. 가용성을 높여주지만 확장성에는 영향을 주지 않는다. 하지만 read replica도 multi az로 승격하여 쓰일 수는 있다.

### RDS 사용해보기


데이터베이스를 만든다. standard create를 선택하고 어떤 DBMS를 사용해서 만들지 선택한다.



template와 availability and durability 옵션을 선택한다. template는 사용 목적에 따라 선택한다. availability and durability 옵션은 추후 변경할 수 있으므로 먼저 single DB instance로 생성한다.



사용자 이름과 비밀번호를 설정한다. DB에 접근할 때 필요하므로 잘 기억해 두어야한다.



인스턴스 설정은 무료인 t2.micro를 선택한다. (include previous generation classes를 활성화 해야 나온다.)


저장공간 설정을 한다. 가장 저성능 저비용인 gp2 type을 선택한다.

Allocated storage는 최초로 할당된 저장공간 크기이고, maximum storage threshold는 용량의 증가 한계선을 정하는 것이다.


연결성을 설정한다. EC2 인스턴스와 연결하여 사용할 수도 있다. public acess를 비허용 할 경우 아마존 EC2 인스턴스와 VPC에 연결된 경우에만 데이터베이스에 접근가능하다.



보안 그룹과 포트 설정을 한다. DB의 포트는 기본 3306번을 사용한다.



인증선택을 한다. 선택한 것은 비밀번호와 사용자ID를 입력하면 접속할 수 있는 옵션이다.


모니터링 옵션을 선택한다. 향상된 모니터링을 선택하면 얼마나 자주 모니터링할지, 



inital database name과 자동 백업 옵션을 지정한다. **inital database name는 추후 DB에 접속하기 위해 반드시 알고 있어야한다.**

back retention period는 백업데이터를 얼마나 오래 보관할지 정한다.


backup replication을 통해 다른 region에 DB를 복제해 더 높은 가용성을 확보할 수 있다.

log exports를 이용해 오류 로그 등을 기록하고 확인할 수 있다.


DB가 만들어진 이후에는 여러가지 작업이 가능하다.

1\. Covert to Multi-AZ deployment:

다른 AZ에 DB의 복제본을 추가하여 가용성을 증대시킨다.

2\. Create read replica:

read replica를 만든다.

3\. take snap shot:

DB의 snap shot을 만들어 백업해 둘 수 있다.

4\. migrate snapshot:

DB의 스냅샷을 다른 region으로 이동시킬 수 있다.