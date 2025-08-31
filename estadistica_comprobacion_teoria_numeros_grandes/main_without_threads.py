import statistics, random, time
nums=[]
t0=time.time()
rango=1000000

for i in range(rango):
    num=random.randint(0,5)
    print(num)
    nums.append(num)
tf=time.time()-t0
with open("./estadistica/main_wth.txt", "a") as r:
    r.write("\nthe range of: "+ str(rango) + " took:"+ str(tf))
print(str(statistics.mean(nums)) + ". Processing took: " +str(tf) +". For " + str(rango) + " Numbers.")