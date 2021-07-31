import random

avg_time_on_interai=5
class Company:
    #defiyng the variables of the class
    def __init__(self, company_name, num_of_softwares, avg_time_spent_on_software):
        self.company_name=company_name
        self.num_of_softwares=num_of_softwares
        self.avg_time_spent_on_software=avg_time_spent_on_software

    def calculate_worthness(self):
    #this is the worh measure for a company to join Interai. I wannted to compare the average call time with costumer to the average time using inerai.
      avg_call_time=self.avg_time_spent_on_software * self.num_of_softwares
      worthness= avg_call_time/avg_time_on_interai
      return worthness

#main
#creating a dictionary
dict_companies={}
#creating a list with the companies names.
companies_names=['Interai','Facebook','Google','Al_Hagal','Github']
#this for loop had 2 roles: 1. define a company object by using the names list and the random library ranint function.
#2. insert the matching company's name and value to the dictionary.
for i in companies_names:
    company=Company(i,random.randint(1,10),random.randint(1,10))
    #key=company name, value=company worthness.
    dict_companies[company.company_name] = company.calculate_worthness()

#sorting the dictionary from the higest worthness sccore to the lowest.
sorted_dict=dict(reversed(sorted(dict_companies.items(), key=lambda item: item[1])))

#the original rating and companies name to ensure the results
print("The original comanpies list and ratings is:" + str(dict_companies))
#print("The original company rating is:"+ str(companies_original_derug))
print("The sorted company rating list is:", str(sorted_dict))

