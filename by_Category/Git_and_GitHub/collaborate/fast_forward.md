# fast-forward
fast-forward는 두 branch의 관계에 따른다. 병합하고자 하는 branch의 commit history 내에 현재 branch의 commit history가 포함되는 관계를 fast-forward라고 한다. 이 경우 `--no-ff` 옵션을 사용하지 않으면 모든 commit이 기준이 되는 branch에 합쳐진다.
![](https://velog.velcdn.com/images/97ckdtn/post/26ae1c73-65f3-456b-a159-4c9ab0e50bd7/image.png)merge 전
![](https://velog.velcdn.com/images/97ckdtn/post/c15a90fa-d09b-4e9f-a351-3741ab57f9ea/image.png)merge 후

`--no-ff`옵션을 사용하면 fast-forward가 가능한 상태여도 그렇지 않은 것 처럼 merge commit을 새로 만든다.
![](https://velog.velcdn.com/images/97ckdtn/post/68d422ac-b196-49e4-9915-a2b786b6e08f/image.png)
