from mailtm import Email
import sys, os, random
wd=os.getcwd()
wd=wd.replace("\\", "/")
n=10
pwd=""
for i in range(n):
    pwd+=str(random.randint(0,9))
def listener(message):
    print("\nSubject: "+message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])
#get domains 
test = Email()
print("\nDomain: " + test.domain)
#Make new email address
test.register(username=None, password=pwd)
print("\nEmail Adress: " + str(test.address))
print("\nPassword: " + str(pwd))
with open(wd+"/emails.txt", "a") as r:
    r.write("\nEmail: " + str(test.address) +". And password: " + str(pwd))
#start listening
def starter():
    test.start(listener)
    print("\nWaiting for new emails...")
if len(sys.argv)>=2:
    args=sys.argv[1]
else:
    args=False
if args == "listen":
    starter()
else:
    print("Try to add listen if you want to list incoming emails")