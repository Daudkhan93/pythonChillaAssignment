#first_loop_while
x=2
while (x<6):
    print(x)
    x=x+1

print("**************")


for y in range(1,8):
    print(y)

print("***************")

days=["sun", "mon", "tue", "thur", "fri", "sat"]

for d in days:
    #if (d=="thur"): break                   #loop stop
    if (d=="tue"): continue                  #skips define d
    print(d)