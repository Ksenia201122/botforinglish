# slovar={"Юля":"79805564009","Коля":"76885508934"}
# d=slovar["Юля"]
# print(d)
# slovar["Федя"]="76685436754"
# print(slovar)

# b=1
# slovar={}
# while b==1:
#     tovar=input("Какой товар?")
#     cenatovara=input("Сколько стоит?") 
#     if tovar==" " and cenatovara==" ":
#         print(slovar)
#         b=0
#     else:
#         slovar[tovar]=cenatovara

import json
slovar={"1267":{"Привет":"Hello","Пока":"Goodbuy"},"2347":{"Игрушка":"Toy","Апельсин":"oRANGE","я":"i"}}
slovar["6789"]={"ты":"you"}
f=slovar["2347"]
for c in f:
    print(c)
# f["дерево"]="tree"
# file=open("fyle.json","w",encoding="UTF-8")
# json.dump(slovar,file,ensure_ascii=False,indent=4)
# file.close()
# file=open("fyle.json","r",encoding="UTF-8")
# slovar=json.load(file)
# print(slovar)




