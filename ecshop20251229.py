# import requests
#
# url="http://192.168.164.129/ecshop/user.php"
# login_data={
#     "username":"aaa",
#     "password":"123456",
#     "act":"act_login"
# }
# login_res=requests.post(url,data=login_data)
# cookie=login_res.cookies.get("ECS_ID")
# print(cookie)
#
# msg_url="http://192.168.164.129/ecshop/user.php"
# msg_data={
#     "msg_type":0,
#     "msg_title":"qwer",
#     "msg_content":"asdf",
#     "act":"act_add_message"
# }
# cookies={
#     "ECS_ID":cookie
# }
# img_data={
#     "message_img":open(r"C:\Users\dell\OneDrive\桌面\微信图片_20251221234118_98_29.jpg",'rb')
# }
#
# msg_res=requests.post(msg_url,data=msg_data,cookies=cookies,files=img_data)
import requests

# import requests
#
# session=requests.session()
# url="http://192.168.164.129/ecshop/user.php"
# login_data={
#     "username":"aaa",
#     "password":"123456",
#     "act":"act_login"
# }
# login_res=session.post(url,data=login_data)
#
# msg_url="http://192.168.164.129/ecshop/user.php"
# msg_data={
#     "msg_type":0,
#     "msg_title":"qwer1",
#     "msg_content":"asdf1",
#     "act":"act_add_message"
# }
# msg_res=session.post(msg_url,data=msg_data)







# login_url="http://192.168.164.129/ecshop/user.php"
# login_data={
#     "username":"aaa",
#     "password":"123456",
#     "act":"act_login"
# }
# login_res=requests.post(login_url,data=login_data)
# cookie=login_res.cookies.get("ECS_ID")
#
# add_url="http://192.168.164.129/ecshop/user.php"
# add_data={
#     "country":1,
#     "province":2,
#     "city":37,
#     "district":421,
#     "consignee":"yjy",
#     "email":"123456@163.com",
#     "address":"znh",
#     "tel":"16585499648",
#     "submit":"新增收货地址",
#     "act":"act_edit_address"
# }
# cookie={
#     "ECS_ID":cookie
# }
# add_res=requests.post(add_url,data=add_data,cookies=cookie)


session=requests.session()
login_url="http://192.168.164.129/ecshop/user.php"
login_data={
    "username":"aaa",
    "password":"123456",
    "act":"act_login"
}
login_res=session.post(login_url,data=login_data)
add_url="http://192.168.164.129/ecshop/user.php"
add_data={
    "country":1,
    "province":2,
    "city":37,
    "district":421,
    "consignee":"yjy",
    "email":"123456@163.com",
    "address":"znh",
    "tel":"16585499648",
    # "submit":"新增收货地址",
    "act":"act_edit_address"
}
add_res=session.post(add_url,data=add_data)
