# import requests
# from faker import Faker
#
# import config
# from config import project_url
#
# # get类型的接口在进行传参的时候有两种方式，第一个是拼接的url地址后面，第二种是通过params参数进行传参。
# # url="http://sky.nnzhp.cn/api/sparrow/student?limit=2&page=1"
# # res=requests.get(url)
# # res.encoding="utf-8"
# # print(res.text)
#
# # url="http://sky.nnzhp.cn/api/sparrow/student"
# # data={
# #     "limit":2,
# #     "page":1
# # }
# # res=requests.get(url,params=data)
# # res.encoding="gbk"
# # #如何响应的状态码
# # print(res.status_code)
# # #获取响应头信息
# # print(res.headers)
# # #获取响应的cookies信息
# # print(res.cookies)
# # #响应数据的编码格式
# # print(res.encoding)
# # #获取响应的文本信息
# # print(res.text)
# # print(type(res.text))
# # #获取响应的json 数据
# # print(res.json())
# # print(type(res.json()))
#
# faker=Faker(locale='zh_CN')
# email=faker.email()
# name=faker.name()
# address=faker.address()
# phone=faker.phone_number()
# # num=config.num
# #注册
# url=project_url+"/api/user/register"
# register_data={
#     "phone":phone,
#     "nick":name,
#     "email":email,
#     "password":"123456",
#     "password2":"123456"
# }
# res=requests.post(url,data=register_data)
# print(res.status_code)
# print(res.text)
# print(res.json())
# #登录
# url=project_url+"/api/user/login"
# login_data={
#     "username":phone,
#     "password":"123456"
# }
# res=requests.post(url,data=login_data)
# print(res.status_code)
# print(res.text)
# #新增学生
# url=project_url+"/api/sparrow/student"
# addstu_data={
#     "name":name,
#     "grade":"一班",
#     "phone":phone
# }
# res=requests.post(url,json=addstu_data)
# print(res.text)
import requests

from config import project_url

url="https://admin-api.macrozheng.com/admin/login"
login_data={
    "username":"admin",
    "password":"macro123"
}
res=requests.post(url,json=login_data)
print(res.status_code)
print(res.text)