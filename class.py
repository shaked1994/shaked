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

worthness1=ob1.worthness()
worthness2=ob2.worthness()
worthness3=ob3.worthness()
worthness4=ob4.worthness()
worthness5=ob5.worthness()

worth_lst=[worthness1,worthness2,worthness3,worthness4,worthness5]
worth_lst.sort()

derug=[]

for i in worth_lst:

    for j in worth_lst
    if i==ob_lst[i].worthness():
        derug[i]=worth_lst[i]
        derug[ob_lst[i].worthness()]
        lst[i]=ob_lst[i].company_name

     elif:
      i=i+1


