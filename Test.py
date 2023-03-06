
url = 'https://geekbrains.ru/teacher/lessons/79615'
# url_parts = url.split('/')
# print(url_parts)

_t_protocol, _, domain, *resource_address = url.split('/')[:3]
print(_t_protocol, domain, resource_address)
#print(_t_protocol[:-1])
t_protocol = _t_protocol[:-1]
#print(t_protocol)
print(t_protocol, domain, resource_address)