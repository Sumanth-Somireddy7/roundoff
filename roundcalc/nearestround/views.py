from django.shortcuts import render
from .methods import *

# Create your views here.
def roundoff(request):
    try:
        num1 = request.POST['num1']
        per = request.POST['per']
    except:
        num1 = ''
        cas = False
        cas1 = False
        per = ''
        prec = ''
        res = ''
        result = ''
        st = ''
        st1 = ''
        tens = ''
        place = ''
    else:
        if per=='-2':
            try:
                result = h_2(float(num1))
                res = result[0]
                st = result[1]
                st1 = result[2]
                tens = result[3]
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Hundreds'
                place = 'tens'
        elif per=='0':
            try:
                result = h_0(float(num1))
                res = result[0]
                st = result[1]
                st1 = result[2]
                tens = result[3]
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Ones'
                place = "tenth's"
        elif per=='-1':
            try:
                result = h_1(float(num1))
                res = result[0]
                st = result[1]
                st1 = result[2]
                tens = result[3]
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Tens'
                place = "ones"
        elif per == '-6':
            if len(str(int(num1)))>=7:
                try:
                    result = h_6(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                except:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
                else:
                    cas = True
                    cas1 = True
                    prec = 'Millions'
                    place = 'lakhs'
            else:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
        elif per=='-5':
            if len(str(int(num1)))>=6:
                try:
                    result = h_5(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                except:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
                else:
                    cas = True
                    cas1 = True
                    prec = 'Hundred Thousands'
                    place = 'ten thousand'
            else:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
        elif per=='-4':
            if len(str(int(num1)))>=5:
                try:
                    result = h_4(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                except:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
                else:
                    cas = True
                    cas1 = True
                    prec = 'Ten Thousands'
                    place = 'thousand'
            else:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
        elif per=='-3':
            if len(str(int(num1)))>=4:
                try:
                    result = h_3(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                except:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
                else:
                    cas = True
                    cas1 = True
                    prec = 'Thousands'
                    place = 'hundred'
            else:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
        elif per=='1':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=2:
                    result = h1(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Tenths'
                place = 'hundredth'
        elif per=='2':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=3:
                    result = h2(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Hundredth'
                place = 'thousandth'
        elif per=='3':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=4:
                    result = h3(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Thousandth'
                place = 'ten thousandth'
        elif per=='4':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=5:
                    result = h4(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Ten Thousandth'
                place = 'hundred thousandth'
        elif per=='5':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=6:
                    result = h5(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Hundred Thousandth'
                place = 'Millionth'
        elif per=='6':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))==7 or len(str(int(num)))>7:
                    result = h6(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Millionth'
                place = 'Ten Millionth'
        elif per=='7':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=8:
                    result = h7(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Ten Millionth'
                place = 'Hundred Millionth'
        elif per=='8':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=9:
                    result = h8(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Hundred Millionth'
                place = 'Billionth'
        elif per=='9':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=10:
                    result = h9(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Billionth'
                place = 'Ten Billionth'
        elif per=='10':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=11:
                    result = h10(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Ten Billionth'
                place = 'Hundred Billionth'
        elif per=='11':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=12:
                    result = h11(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Hundred Billionth'
                place = 'Trillionth'
        elif per=='12':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=13:
                    result = h12(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Trillionth'
                place = 'ten trillionth'
        elif per=='13':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=14:
                    result = h13(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Ten Trillionth'
                place = 'hundred Trillionth'
        elif per=='14':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=15:
                    result = h14(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Hundred Trillionth'
                place = 'Quadrillionths'
        elif per=='15':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=16:
                    result = h15(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Quadrillionths'
                place = 'Ten quadrillionth'
        elif per=='16':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=17:
                    result = h16(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Ten Quadrillionth'
                place = 'hundred quadrillionth'
        elif per=='17':
            try:
                num1 = float(num1)
                a = str(num1).split('.')
                num = a[1]
                if len(str(int(num)))>=18:
                    result = h17(num1)
                    res = result[0]
                    st = result[1]
                    tens = result[3]
                    st1 = result[2]
                else:
                    num1 = ''
                    cas = False
                    cas1 = False
                    per = ''
                    prec = ''
                    res = ''
                    tens = ''
                    result = ''
                    st = ''
                    st1 = ''
                    place = ''
            except:
                num1 = ''
                cas = False
                cas1 = False
                per = ''
                prec = ''
                res = ''
                tens = ''
                result = ''
                st = ''
                st1 = ''
                place = ''
            else:
                cas = True
                cas1 = True
                prec = 'Hundred Quadrillionth'
                place = 'last but one decimal place'
    return render(request,'nearestround.html',{'res':res,'cas':cas,'cas1':cas1,'per':per,'num1':num1,'prec':prec,'place':place,'st':st,'st1':st1,'tens':tens})

            
