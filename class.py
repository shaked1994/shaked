import math
import random
class Company:
    def __init__(self, company_name, num_of_softwares, avg_call_time):
        self.company_name=company_name
        self.num_of_softwares=num_of_softwares
        self.avg_call_time=avg_call_time

    def worthness(self):
        #this is the worh measure for a company to join Interai. It consists two variables and the bigger
        # they are the bigger the worthness
      worthness=self.avg_call_time * self.num_of_softwares
      return worthness


ob1=Company('Interai',random.randint(1,10),random.randint(1,10))
ob2=Company('Facebook',random.randint(1,10),random.randint(1,10))
ob3=Company('Google',random.randint(1,10),random.randint(1,10))
ob4=Company('Al_Hagal',random.randint(1,10),random.randint(1,10))
ob5=Company('Github',random.randint(1,10),random.randint(1,10))

ob_lst=[ob1,ob2,ob3,ob4,ob5]

ob_original_derug=[ob1.company_name,ob1.worthness(),ob2.company_name,ob2.worthness(),ob3.company_name,ob3.worthness(),ob4.company_name,ob4.worthness(),ob5.company_name,ob5.worthness()]


worthness1=ob1.worthness()
worthness2=ob2.worthness()
worthness3=ob3.worthness()
worthness4=ob4.worthness()
worthness5=ob5.worthness()

worth_lst=[worthness1,worthness2,worthness3,worthness4,worthness5]
worth_lst.sort()


derug=[0,0,0,0,0]

for i in range(len(worth_lst)):
    for j in range(len(ob_lst)):
     if (worth_lst[i]==ob_lst[j].worthness()):
          derug[i]=ob_lst[j].company_name
          j=0


print("The original company rating is:"+ str(ob_original_derug))
print('worth list is', str(worth_lst))
print('derug is',str(derug))

for i in range (5):
   if i==0:
       print('The lowest rating belong to' ,str(derug[i]),'with the rate of' ,str( worth_lst[i]))

   if i==1:
       print("The second lowest rating belong to",str(derug[i]),"with the rate of" ,str(worth_lst[i]))

   if i==2:
        print("In the third place there's",str(derug[i]),"with the rate of", str(worth_lst[i]))

   if i==3:
        print("The second place belongs to",str(derug[i]),"with the rate of",str(worth_lst[i]))

   if i==4:
      print("And in the first place with the highest rating we have", str(derug[i]),"with the rate of", str(worth_lst[i]))






