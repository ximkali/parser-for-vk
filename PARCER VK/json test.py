import pandas as pd
import json



with open(R'C:\Users\\Дима\Desktop\\PARCER VK\meowkyit\meowkyit.json',encoding="utf-8") as file:
    templates = json.load(file)
    


with open(R'C:\Users\Дима\Desktop\PARCER VK\meowkyit\respons_comments',encoding="utf-8") as file1:
    templates = json.load(file1)


with open(R'C:\Users\Дима\ria\test.csv','w+',encoding="utf-8") as file2:
    file2.writelines("id,from_id,date,count_likes,text")
    for item in templates["response"]["items"]:
        string = "{},{},{},{},{}\n".format( item["id"],item["from_id"],item["date"],item["likes"]["count"],item["text"])
        file2.write(string)


websites = pd.read_csv(r"C:\Users\Дима\ria\test.txt",header = None)
  
# adding column headings
websites.columns = ['id', 'from_id', 'date', 'count_like', 'text']
  
# store dataframe into csv file
websites.to_csv(r'C:\Users\Дима\ria\test1.csv', 
                index = None)








# print("id,from_id,date,count_likes,text")
# for item in templates["response"]["items"]:
#     print(int(item["id"]),item["from_id"],int(item["date"]),int(item["likes"]["count"]),str(item["text"]),sep=',')
