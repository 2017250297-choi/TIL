# 백엔드 개발자의 필수덕목
- **인증(가입,로그인,...)**
- DB
- Request에 대한 Response처리: API개발. 예외처리
- 배포
# 세션인증이 무엇인가?
django_session에 유저 정보와 세션 정보를 저장.

1. 사용자 인증정보 서버에 전달.
2. 인증처리 후 세션 생성
3. 사용자는 쿠키로 세션 id를 받아온다.
4. 이후 요청에 항상 세션 id 이용

## 세션 인증의 문제
- 매요청마다 인증을 위해 DB에 쿼리
- DB가 두개 이상, 서버가 두개 이상인 경우..?

# 토큰 인증
DB에 저장하지 않아 자원이 절약된다.

SECRET_KEY로 암호화된 토큰을 전달하면, 사용자는 토큰을 이용해 인증한다. ex - JWT
>django-restframe-simplejwt

1. 클라이언트가 인증정보 서버에 전달
2. 서버가 인증처리후 JWT 생성해 전달
3. JWT를 브라우저(localstorage)에 저장, 요청시 헤더에 담아 전달
4. 서버가 JWT 검증하여 인증처리
5. 토큰 만료시 재발급(refresh)

# JWT의 구조
>**헤더.페이로드.서명 + 트레일러**
1. 헤더 : 알고리즘, 로큰 타입이 있다.
2. 페이로드 : 실질적인 인증 정보, 데이터가 저장되어 있다.

헤더와 페이로드는 단순히 인코딩되어있고, 서명은 SECRET KEY로 암호화되어있다.

토큰 구조가 중요한 이유: 직접 조작해서 사요할 수 있기 때문이다.

# 토큰인증의 단점
- DB를 이용한 사용자 정보 조작이 어려울 수 있다.
- 토큰이 너무 커질 수 있다.
- 토큰이 거의 모든 요청에 대해 전송되면 트래픽 악영향.

# Access token, Refresh token
두종류 모두 발급하고, 보통 브라우저 로컬스토리지에 저장된다(js).
- Access token: 요청 보내기용
- Refresh token: Access token 만료시 재발급용

- 