# git을 이용한 협업
1. [issue를 제시](/by_Category/Git_and_GitHub/collaborate/git_issue.md)한다.
2. issue를 해결하기위한 각자의 작업공간 (branch)를 만든다.
3. 작업후 각자의 작업을 합친다(pull request → merge)(여기까지)

#branch
# Branch
Branch는 원래 코드와는 상관없이 독립적으로 개발을 진행할 수 있게 해준다. git의 브랜치는 매우 가벼우므로 브랜치를 만들어 작업하고 merge하는 것을 공식적으로 권장하는 매우 중요한 기능이다. 
## git branch: 브랜치 생성 후 작업
`git branch <브랜치 이름>`을 입력하여 브랜치를 생성한다.
브랜치 이름은 `종류/이슈번호_원하는이름`와 같이 짓는다. (예: feature/2_login)
새 branch에 commit을 하려면 해당 branch로 checkout한다: `git checkout <branch명>`

## git branch -D: 브랜치 삭제
`git branch -D <branch명>`을 입력하여 브랜치를 삭제한다. 커밋들은 삭제되지 않고 남아있으며(git checkout 으로 조회 가능) commit들이 이루는 tree의 leaf를 가리키던 branch 포인터가 사라지는 것이다.

#merge
# 브랜치 merge
각자의 작업을 합치는 단계. 현재 branch에 다른 branch의 commit내역을 모두 반영하는 것이다.
실제 프로젝트에서는 flow 방식에 따라 1개이상의 기준이 되는 branch를 정하고 그곳에 merge한다.

1. git-flow: 제품을 배포하는 기준이 되는 Master branch와 개발시 기준이되는 Develop branch가 중심이 된다. 이외에 새로운 기능을 만드는 Feature brach, production을 배포하기 전 QA등을 하는 Release branch, production에서 발생한 긴급한 버그를 고치기 위한 Hotfix branch가 존재한다.![](https://nvie.com/img/git-model@2x.png)

2. github-flow: main branch가 중심이된다. main branch는 어떤때든 배포가 가능한 최신 상태이고, 새로운 작업을 위한 branch의 명칭은 알아보기 쉽게 작성한다. 또한 항상 branch들을 원격repo에도 push하여 모두가 확인할 수 있게한다. 가 기준의 역활만 명확히 하면 이외 branch에 는 크게 관여하지 않는다. 흐름이 비교적 단순하며 Pull request를 권장한다. release branch가 명확하지 않은 시스템에서 사용하기 좋다.

## git merge --no-ff:
기준이 될 branch(main)으로 checkout 한 뒤 `git branch merge <branch명>`을 입력하면 merge를 진행한다. 이때 `--no-ff`옵션을 사용해주면 좋다. 이 옵션은 source tree에서 '[fastforward](/by_Category/Git_and_GitHub/collaborate/fast-forward.md)'가 가능해도 새 커밋 생성 옵션을 선택한 것과 같다. `--log`옵션을 사용할 경우 merge할 branch의 commit message를 새 commit에 기록한다.
이후 쓸모가 없는 branch는 삭제해도 된다.

## merge-conflict
merge 시 충돌이 발생할 경우: [링크](/by_Category/Git_and_GitHub/collaborate/conflict.md)

# 확장된 tracking, Push / Pull 개념
tracking은 단순히 로컬 repo와 원격 repo의 연결이 아니라, `원격 repo의 한 branch`와 `로컬 repo의 한 branch` 간의 연결관계를 의미한다. 따라서 실제로 push/pull을 할때는 어떤 branch를 대상으로 할지 정해야한다. `--set-upstream`옵션을 통해 설정할 수 있다.
```
git push --set-upstream <원격repo이름(origin)> <원격branch명>
```
push시에는 해당 이름의 원격 branch가 없을 때에는 새로 만들어서 tracking을 한다.
Push와 Pull은 모두 브랜치 단위로 이루어지는 것이다.
한번에 모든 branch를 다루고 싶다면 `--all` 옵션을 사용한다.
브랜치 단위가 아닌 전체 저장소를 업데이트 하고 싶다면 `git clone`을 이용하면 된다.

# 개념도
![](/by_Category/Git_and_GitHub/img/git_hub_2.jpg)