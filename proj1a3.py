'''3. INCLUDE VER 1 AND VALIDATE EACH ENTRY.
   ACCEPT FROM THE USER: DAYS IN FUTURE AND VALIDATE
	DISPLAY: FUTURE DAY+SUPERSCRIPT(st,nd,rd,th), MONTHNAME, YEAR'''




day=int(input("ENTER A DAY"))
month=int(input("ENTER THE MONTH"))
year=int(input('ENTER THE YEAR'))
num=int(input("HOW MANY DAYS AFTER?"))
while num!=0:

    if (year%400==0):
        leap_year=True
    elif (year%100==0):
        leap_year=False
    elif (year%4==0):
        leap_year=True
    else:
        leap_year=False


    mont={1:'jan',5:'may',3:'mar',7:'jul',8:'aug',10:'oct',12:'dec'}
    if month in mont:
        monthlen=31
    elif month==2:
        mont={2:'feb'}
        if leap_year:
            monthlen=28
        else:
            monthlen=29
    else:
        mont={4:'apr',6:'jun',9:'sept',11:'nov'}
        monthlen=30
    
   
        
    if(month<1 or month>12):
        print("INVALID")
    elif(day<1 or day>monthlen):
        print("INVALID DATE")   
   

    if (day<monthlen):
        day+=1
    else:
        day=1
        if month==12:
            month=1
            year+=1
        else:
             month+=1
    num-=1
    
st=[1,21,31]
nd=[2,22]
rd=[3,23]
if day in st:
    print('%dst %s,%d'%(day,month,year))
elif day in nd:
    print('%dnd %s,%d'%(day,month,year))
elif day in rd:
    print('%drd %s,%d'%(day,month,year))
else:
    print('%dth %s,%d'%(day,month,year))

    
