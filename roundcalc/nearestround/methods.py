from decimal import *
def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    pos_nums.reverse()
    return pos_nums

def h_6(num1):
    s = str(int(num1)/1000000)
    s1 = s.split('.')
    n1 = s1[0]
    n2 = s1[1]
    tens = int(n2[0])
    getcontext().prec = 100
    res1 = round(Decimal(num1),-6)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h_5(num1):
    s = str(int(num1)/100000)
    s1 = s.split('.')
    n1 = s1[0]
    n2 = s1[1]
    tens = int(n2[0])
    getcontext().prec = 100
    res1 = round(Decimal(num1),-5)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h_4(num1):
    s = str(int(num1)/100000)
    s1 = s.split('.')
    n1 = s1[0]
    n2 = s1[1]
    tens = int(n2[0])
    getcontext().prec = 100
    res1 = round(Decimal(num1),-4)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h_3(num1):
    s = str(int(num1)/10000)
    s1 = s.split('.')
    n1 = s1[0]
    n2 = s1[1]
    tens = int(n2[0])
    getcontext().prec = 100
    res1 = round(Decimal(num1),-3)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h_2(num1):
    tens = int(num1 % 100) // 10
    getcontext().prec=100
    res1 = round(Decimal(num1), -2)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h_1(num1):
    tens = int((num1*10) % 10)
    getcontext().prec = 100
    res1 = round(Decimal(num1),-1)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]


def h_0(num1):
    nu = str(int(num1))
    tens = int(nu[-1])
    getcontext().prec=100
    res1 = round(Decimal(num1),0)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h1(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[1])
    getcontext().prec=100
    res1 = round(Decimal(num1),1)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h2(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[2])
    getcontext().prec=100
    res1 = round(Decimal(num1),2)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h3(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[3])
    getcontext().prec=100
    res1 = round(Decimal(num1),3)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h4(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[4])
    getcontext().prec=100
    res1 = round(Decimal(num1),4)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h5(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[5])
    getcontext().prec=100
    res1 = round(Decimal(num1),5)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h6(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[6])
    getcontext().prec=100
    res1 = round(Decimal(num1),6)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h7(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[7])
    getcontext().prec=100
    res1 = round(Decimal(num1),7)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h8(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[8])
    getcontext().prec=100
    res1 = round(Decimal(num1),8)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h9(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[9])
    getcontext().prec=100
    res1 = round(Decimal(num1),9)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h10(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[10])
    getcontext().prec=100
    res1 = round(Decimal(num1),10)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h11(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[11])
    getcontext().prec=100
    res1 = round(Decimal(num1),11)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h12(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[12])
    getcontext().prec=100
    res1 = round(Decimal(num1),12)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h13(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[13])
    getcontext().prec=100
    res1 = round(Decimal(num1),13)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h14(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[14])
    getcontext().prec=100
    res1 = round(Decimal(num1),14)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h15(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[15])
    getcontext().prec=100
    res1 = round(Decimal(num1),15)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h16(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[16])
    getcontext().prec=100
    res1 = round(Decimal(num1),16)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]

def h17(num1):
    nu = str(num1).split('.')
    s = nu[1]
    a = get_pos_nums(int(s))
    tens = int(a[17])
    getcontext().prec=100
    res1 = round(Decimal(num1),17)
    if tens>5:
        st = 'which is greater than 5'
        st1 = 'So round up the number'
    elif tens==5:
        st = 'which is equal to 5'
        st1 = 'So, round up the number'
    else:
        st = 'which is less than 5'
        st1 = 'So, round down the number'
    return [res1,st,st1,tens]






        






