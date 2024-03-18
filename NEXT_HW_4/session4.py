import random
usermax=int(input())


comlist=[]
for i in range(1, usermax+1):
    comlist.append(i)

choice=random.choice(comlist)
print("준비가 되었으면 Enter를 누르세요")

print("당신이 생각한 숫자는", choice, "입니까?")
test=input("제가 맞췄다면 '맞음', 제가 제시한 숫자보다 크다면 '큼', 작다면 '작음'을 입력해주세요cnt=0
while test!='맞음':
    idx=comlist.index(choice)
    if test=='큼':
        comlist=comlist[idx+1:]
        choice=random.choice(comlist)
        
    elif test=='작음':
        comlist=comlist[:idx]
        choice=random.choice(comlist)
           
    else:
        print("다시 입력해주세요")
    print("당신이 생각한 숫자는", choice, "입니까?")
    test=input("제가 맞췄다면 '맞음', 제가 제시한 숫자보다 크다면 '큼', 작다면 '작음'을 입력해주세요 :")
        
    cnt+=1
   
print(cnt+1,"번 만에 맞췄습니다!")

