a = int(input())
b = int(input())
c = int(input())

maiorAB = ((a+b+abs(a-b))/2)

print(f"{(maiorAB+c+abs(maiorAB-c))/2} eh o maior")