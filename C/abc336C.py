N = int(input())

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

base5 = base10int(N - 1, 5)

ans = ""

for i in base5:
    ans += str(int(i) * 2)

print(ans)