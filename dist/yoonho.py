# 파이썬 연습
# print("Hello World!")

# str = "Hello Minsu!!"
# print(str)

# num = 0

# while num<5:
#     print(num)
#     num=num+1

# 카트 = ["과자", "음료수", "과일"]

# for i in 카트:
#     print(i)

# def sum(A1, A2, A3):

# def 별찍기():
#     print("*"*30)
#     print("")
#     print("*"*30)

#     print(별찍기())

# def mysum(a, b):
#     ret = a + b
#     return ret

# ret1 = mysum(3,4)

# print(ret1)

# 곱하기 식
# num1 = input()
# num2 = input()

# results = []

# for i in range(len(num2)-1, -1, -1):
#     result = int(num1) * int(num2[i])
#     results.append(result)

# final_result = int(num1) * int(num2)
# results.append(final_result)

# for result in results:
#     print(result)

# 곱하기 식 끝


# 빼기 식
# A, B = map(int, input().split())
# print(A - B)
# 빼기 식

# 2884번 노션 작성하기
# H, M = map(int, input().split())
# M -= 45
# if M < 0:
#     M += 60
#     H -= 1
#     if H < 0:
#         H = 23
# print(H,M)

# 2739번 구구단
# N = int(input())
# for i in range(1, 10):
#     print(f"{N} * {i} = {N*i}")
                 
# n = ord('a')

# while n != ord('q') :
#     n = input()
#     n = ord(n)
#     print(chr(n))

# n = int(input())
# i = 0
# sum = 0

# while n > sum:
#     i += 1
#     sum += i

# print(i)

# a,b = map(int, input().split())

# for i in range(1, a+1) :
#     for j in range(1, b+1) :
#         print(i, end='')
#         print(j)


# r, g, b = map(int, input().split())

# total = 0

# for i1 in range(r):
#     for i2 in range(g):
#         for i3 in range(b):
#             print(i1, i2, i3)
#             total += 1
# print(total)


# print(len([(i1, i2, i3) for i1 in range(r) for i2 in range(g) for i3 in range(b)]))

h, b, c, s = map(float,input().split())

a=h*b*c*s/8/1024/1024

print(round(a, 1), "MB") 

