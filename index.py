
import pandas as pd

df = pd.read_excel('leadbook.xlsx')

#target specific sheet
# df = pd.read_excel('leadbook.xlsx', sheet_name=[1])
# target specific column
#df = pd.read_excel('leadbook.xlsx', usecols=["company", "phone", "response"])

#  convert to dictionary: 
# dic_version = df.to_dict()
# # list of companies name
# companies_name_list = dic_version["company"]
# # list of companies phone
# companies_phone_list = list(dic_version["phone"].values())
# for phones in companies_phone_list:
#     phones = "0" +str(phones)
#     print(f"phone number edited is now {phones}")
# print(companies_phone_list)
# # print some of the rows
# print(df.head(2))
print(df)