from another.py_day_test import MessageUser

obj = MessageUser()
obj.add_user("justin", 123.24, Email="rkm.ggits@gmail.com")
obj.add_user("john", 545.464)
obj.add_user("rkm", 78.25)
obj.add_user("shubham", 457.5)

print(obj.get_details())

obj.make_messages()

