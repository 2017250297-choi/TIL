# git을 이용한 협업
1. issue를 제시한다. (여기!)
2. issue를 해결하기위한 각자의 [작업공간 (branch)를 만든다](/by_Category/Git_and_GitHub/collaborate/branch_merge.md#branch).
3. 작업후 각자의 작업을 [합친다(pull request → merge)](/by_Category/Git_and_GitHub/collaborate/branch_merge.md#merge)
# issue
이슈는 프로젝트에서 해결해야할 문제들을 말한다. 버그, 기능추가등의 개선사항, 버그와 개선을 위한 작업 단위들을 포함한다.
## GitHub issue 등록하고 관리하기
Repo의 issue 탭에 들어가서 new issue를 누르고 내용을 작성한다.

![](https://velog.velcdn.com/images/97ckdtn/post/00163bfe-5dda-4337-af76-b5998ae177ed/image.png)
Assiginess: 담당할 사람을 할당한다.
Lables: issue의 분류를 표시한다.
Projects: 프로젝트에 issue를 추가한다.
파란 네모로 표시한것이 고유한 issue 번호이다.
issue가 해결되거나 필요없어지면 close issue를 눌러 종료한다.
**commit message에 issue 번호를 넣으면** 해당 이슈와 관련된 commit으로 판별되며 issue 댓글란에 추가된다.