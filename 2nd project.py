import random

avg_time_on_interai=5
class Company:
    #defiyng the variables of the class
    def __init__(self, company_name, num_of_softwares, avg_time_spent_on_software):
        self.company_name=company_name
        self.num_of_softwares=num_of_softwares
        self.avg_time_spent_on_software=avg_time_spent_on_software

    def calculate_worthness(self):
        #this is the worh measure for a company to join Interai.
      avg_call_time=self.avg_time_spent_on_software * self.num_of_softwares
      worthness= avg_call_time/avg_time_on_interai
      return worthness

#main
#defying the objects (I chose these numbers because I thought they match the variables):
company1=Company('Interai',random.randint(1,10),random.randint(1,10))
company2=Company('Facebook',random.randint(1,10),random.randint(1,10))
company3=Company('Google',random.randint(1,10),random.randint(1,10))
company4=Company('Al_Hagal',random.randint(1,10),random.randint(1,10))
company5=Company('Github',random.randint(1,10),random.randint(1,10))

#a list with the original scored made to ensure the resultes in the rated list (derug)
companies_original_derug=[company1.company_name,company1.calculate_worthness(),company2.company_name,company2.calculate_worthness(),company3.company_name,company3.calculate_worthness(),company4.company_name,
                          company4.calculate_worthness(),company5.company_name,company5.calculate_worthness()]

#companies list to run the for loop and compare to the ordered worthness list
companies=[company1,company2,company3,company4,company5]

#list of the worthness of each object:
worth_lst=[company1.calculate_worthness(),company2.calculate_worthness(),company3.calculate_worthness(),company4.calculate_worthness(),company5.calculate_worthness()]

#I've sorted the list so it will be ordered from the lowest score to the highest one.
worth_lst.sort()

#created an empty list to fill with correct company names respectively to the sorted worthness list.
derug=['','','','','']

#2 for loops to run over the worth list and compare it to the worth in the objects list, if the scores are equal AND the name of he company
#is not alredy in the derug list, the company name is inserted to the derug list in the same index as its worth in the worthness list.
for i in range(len(worth_lst)):
    for j in range(len(companies)):
     if (worth_lst[i]==companies[j].calculate_worthness() and ((companies[j].company_name)not in derug)):
          derug[i]=companies[j].company_name
          j=0



#the original rating and companies name to ensure the results
print("The original company rating is:"+ str(companies_original_derug))
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






