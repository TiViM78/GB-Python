
def join_word(**kwargs):
    flag = False
    res_lst = []
    if 'name' in kwargs and 'lname' in kwargs:
        res_lst = [f"{kwargs['name']} {kwargs['lname']}"]
        flag = True
# один з цікавих моментів циклу. Перебіг між назвою і значенням в одній строці
#    for k,v in kwargs.items():
#        if (k == 'name' or k == 'lname') and flag:
#            continue
#        res_lst.append(v)
    for i in kwargs:
        if (i == 'name' or i == 'lname') and flag:
            continue
        res_lst.append(kwargs[i])
    return res_lst

print(
    join_word(
        name = 'Alex',
        lname = 'Popovich',
        age = 45
    )
)