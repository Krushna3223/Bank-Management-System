import random
from pathlib import Path
import json
import string

class Bank:
  database = "data.json"
  data = []
  try:
    if Path(database).exists():
      with open(database) as f:
        data = json.loads(f.read())
    else:
      print("file not exist")    
  except Exception as err:
    print(f"gaya {err}")

  @classmethod
  def __update(cls):
    with open(cls.database,"w") as f:
      f.write(json.dumps(cls.data))

  @classmethod
  def __accGen(cls):
    alpha = random.choices(string.ascii_letters,k=4)
    num = random.choices(string.digits,k=3)
    sc=random.choices("!@#$%^",k=1)
    id = alpha + num + sc
    random.shuffle(id)
    return "".join(id)

      


  def createAcc(self):
    info = {
      "name": input("Enter your name :"),
      "age": int(input("Enter Your age :")),
      "email" : input("Enter email :"),
      "pin": int(input("set your pin (4 num) :")),
      "accNO": Bank.__accGen(),
      "balance":0
    }  

    if info["age"]<18 and len(str(info["pin"])) !=4:
      print("bhag chhotu")
    else:
      print("Account create successfully")
      for i in info:
        print(f"{i} : {info[i]}")
      print("Please note Account no. and pin ")
      Bank.data.append(info)
      Bank.__update()


  def depositmoney(self):
    acc = input("Enter Your Account no. :" )
    pi = int(input("Enter your pin :"))

    # print(Bank.data)
    userData = [i for i in Bank.data if i["accNO"]==acc and i["pin"]==pi]

    if userData == False:
      print("no DATA found")
    else:
      # print(userData)
      amount = int(input("Enter Amount you Want to diposite :"))
      if amount>10000 or amount <0:
        print("no bada no chhota")
      else:
        # print(Bank.userData)
        userData[0]['balance'] += amount
        Bank.__update()
        print("done")
    
  def withdramoney(self):
    acc = input("Enter Your Account no. :" )
    pi = int(input("Enter your pin :"))

    # print(Bank.data)
    userData = [i for i in Bank.data if i["accNO"]==acc and i["pin"]==pi]

    if userData == False:
      print("no DATA found")
    else:
      # print(userData)
      amount = int(input("Enter Amount you Want to withdraw :"))
      if userData[0]['balance']<amount:
        print("mata kar lala")
      else:
        # print(Bank.userData)
        userData[0]['balance'] -= amount
        Bank.__update()
        print("done")

  def showDetail(self):
    acc = input("Enter Your Account no. :" )
    pi = int(input("Enter your pin :"))  
    userData = [i for i in Bank.data if i["accNO"]==acc and i["pin"]==pi]
    print("lere :")
    for i in userData[0]:      
      print(f"{i} : {userData[0][i]}")

  def updateDetail(self):
    acc = input("Enter Your Account no. :" )
    pi = int(input("Enter your pin :"))  
    userData = [i for i in Bank.data if i["accNO"]==acc and i["pin"]==pi]

    if userData == False:
      print("bhag")
    else:
      print("X age|account no | balance X")
      print("fill if you want to updat else empty")

      newData = {
        "name": input("Enter your new name :"),        
        "email" : input("Enter new email :"),
        "pin": int(input("set your new pin (4 num) :"))

      }

      if newData["name"]=="":
        newData["name"] = userData[0]['name']
      if newData["email"] == "":
        newData["email"]=userData[0]['email'] 
      if newData["pin"]=="":
        newData["pin"]=userData[0]['pin'] 

      newData["age"] = userData[0]['age']
      newData["accNO"] = userData[0]['accNO']
      newData["balance"] = userData[0]['balance']

      if type(newData["pin"])==str:
        newData["pin"]=int(newData["pin"])

      for i in newData:
        if newData[i]== userData[0][i]:
          continue
        else:
          userData[0][i]=newData[i]  

      Bank.__update()
      print("doneee") 

  def delete(self):
    acc = input("Enter Your Account no. :" )
    pi = int(input("Enter your pin :"))  
    userData = [i for i in Bank.data if i["accNO"]==acc and i["pin"]==pi]

    if userData == False:
      print("noooooooooooo")
    else:
      check = input("press Y if sure else N : ") 
      if check ==  "n" or check == "N":
        print("good boy")
      else:
        index = Bank.data.index(userData[0])
        Bank.data.pop(index)
        print("gaya acc")
        Bank.__update()








print("Enter 1 for creating Account ")
print("Enter 2 for Deposititing Money ")
print("Enter 3 for withdrawing Money ")
print("Enter 4 for Details ")
print("Enter 5 for updating Details")
print("Enter 6 for deleting Your Account  ")
ch = int(input("Please tell what you want to do :"))


user = Bank()


if ch == 1:
  user.createAcc()
if ch == 2:
  user.depositmoney()
if ch == 3:
  user.withdramoney()
if ch == 4:
  user.showDetail()  
if ch == 5:
  user.updateDetail()   
if ch == 6:
   user.delete()  


