from re import search

import requests
from faker import Faker

from config import project_url

# url=project_url+"/api/user/register"
# faker=Faker(locale="zh_CN")
# phone=faker.phone_number()
# print(phone)
# register_data={
#     "phone":phone,
#     "email":faker.email(),
#     "nick":faker.name(),
#     "password":"123456",
#     "password2":"123456"
# }
# file_data={
#     "file":open(r"C:\Users\dell\OneDrive\桌面\微信图片_20251221234118_98_29.jpg","rb")
# }
# res=requests.post(url,data=register_data,files=file_data)
# print(res.text)


# login_url=project_url+"/api/user/login"
# login_data={
#     "username":"15138793911",
#     "password":"123456"
# }
# login_res=requests.post(login_url,data=login_data)
# print(login_res.text)
# token = login_res.json()["token"]
#
# uinfo_url=project_url+"/api/user/user_info"
# headers={
#     "token":token
# }
# uinfo_res=requests.get(uinfo_url,headers=headers)
# print(uinfo_res.json())


macro_login_url="https://admin-api.macrozheng.com/admin/login"
macro_login_data={
    "username":"admin",
    "password":"macro123"
}
macro_login_res=requests.post(macro_login_url,json=macro_login_data)
print(macro_login_res.text)
token = macro_login_res.json()["data"]["token"]

search_url="https://admin-api.macrozheng.com/coupon/list?pageNum=1&pageSize=10&name=%E6%89%8B%E6%9C%BA&type=0"

headers = {
    "authorization":"Bearer "+token
}
search_data={
    "pageNum":1,
    "pageSize":10,
    "name":"手机",
    "type":0
}
search_res=requests.get(search_url,json=search_data,headers=headers)
print(search_res.json())

