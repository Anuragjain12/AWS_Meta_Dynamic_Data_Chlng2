import requests
import json
import os
res=requests.get("http://169.254.169.254/latest/meta-data/")
aws_url="http://169.254.169.254/latest/meta-data/"
list_1=list(res.iter_lines())
res_dict={}

def calling_url(aws_url,app):
    url_f=aws_url+app
    res_f=requests.get(url_f)
    if "/" in app:
        n_f=aws_url+app
        res_nest=requests.get(n_f)
        list_f=list(res_nest.iter_lines())
        for j in list_f:
            calling_url(n_f,j)
    else:
        res_dict[app]=list(res_f.iter_lines())
        #print(app+':'+res_f.contenti)



for i in list_1:
    new_url=aws_url+i
    calling_url(aws_url,i)
    #print(res_dict)
    with open('insta.json', 'w') as json_file:
        json.dump(res_dict, json_file)

#print(res_dict)
os.system("cat insta.json | jq -r")
print("\n")
print(res.content)
print("\n")
value = raw_input("Please enter a string from below list :\n")
print('You entered: ' + value)
#choice=aws_url+value
#get_choice=requests.get(choice)
#print(get_choice.content)

print(res_dict[value]) 
 
