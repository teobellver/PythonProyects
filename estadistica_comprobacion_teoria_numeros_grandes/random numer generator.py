import random, sys
arg1=sys.argv[1]
def appending_process():
    num=random.randint(0,5)
    print(num)
    with open("./estadistica/resource file.txt", "a") as r:
        r.write(str(num)+ ",")

for x in range(int(arg1)):
    appending_process()

