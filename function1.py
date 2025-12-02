# function1.py

# 1)함수를 정의
def setValue(newValue):
    x = newValue
    print("함수내부:", x)

# 2)호출
result = setValue(5)
print(result)

# 함수를 정의
def swap(x,y):
    return y,x

# 호출
result = setValue(5)
print(result)

print("--키워드인자--")
def connectURI(server,port):
    strURL = "https://" + 

# 호출
print(coonetURI("naver.com", "80"))
print(connectURI(port="8080", server="naver.com"))
print(dir())
print(globals())

print("--가변인자--")
def union(*ar):
    # 지역변수
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))