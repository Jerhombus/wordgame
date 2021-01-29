



from guess import split

def split(word):
    return [char for char in word]
u_left = input("Left: ")
u_right = input("Right: ")
nList = []
for i in range(u_left,u_right+1):
    split(i)
    print(i)
