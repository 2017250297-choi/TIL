def solution(n, k):
    facto = [1]
    for i in range(2, n):
        facto.append(facto[-1] * i)
    k_ = k
    nums = [i for i in range(1, n + 1)]
    answer = []
    while facto:
        count_ = 0
        while k_ - facto[-1] > 0:
            k_ -= facto[-1]
            count_ += 1
        facto.pop()
        answer.append(nums.pop(count_))
    if nums:
        answer.append(nums.pop())

    return answer


print(solution(3, 6))


def solution(skill, skill_trees):
    # skill N
    # skill_trees : L*M
    count = 0
    for sk in skill_trees:
        sk_dic = {x: i for i, x in enumerate(sk)}  # 최대 26
        print(sk_dic)
        idx = 0
        ok = True
        for s in skill:  # 최대 26
            new_idx = sk_dic.get(s, len(sk))
            if new_idx < idx:
                ok = False
                break
            idx = new_idx
        if ok:
            count += 1
    return count


def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer


import time

c = time.time()
print(solution(b, a))

print(time.time() - c)
