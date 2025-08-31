import statistics, threading, time, subprocess 
#maybe use sys for user selection of ammount of numbers to be tested?
nums=[]
threads=list()
with open("./estadistica/resource file.txt", "a") as f:
    f.write("{")
def activate():
    subprocess.run('python3 "./estadistica//worker.py" 1000', shell=True, check=True)

t0=time.time()
# 100000 took 13.147917747497559 seconds
#range(10) took 11.453364849090576 seconds
#range(50) took 7.491348505020142 seconds 
rango=1000
for i in range(int(rango/100)):
    t=threading.Thread(target=activate)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
with open("estadistica/resource file.txt", "a") as f:
    f.write("}")

with open("./estadistica/resource file.txt", "r") as f:
    lista=f.read()
    for char in lista:
        if char=='{' or char== '}' or char== ',':
            pass
        else:
            nums.append(int(char))



tf=time.time()-t0
with open("./estadistica/main.txt", "a") as r:
    r.write("\nthe range of: "+ str(rango) + " took:"+ str(tf))
print("The result was: " +str(statistics.mean(nums)) + ".Processing took:  " + str(tf) + " seconds" +". For " + str(rango) + " Numbers.")