control = int(input("enter value "))

print("""Time Calculator
1-	Add 2 times   
2-	Find the difference between 2 times  
3-	Convert to Hours  
4-	Convert to Minutes  
5-	Convert Minutes to Time  
6-	Convert Hours to Time  
7-	Convert Days to Time  
8-	Exit  

Enter an option:  
""")
if control in [1,2]:
    str1 = input("enter value 1")
    str2 = input("enter value 2")
    if control == 1:
        dayres = 0
        hourres = 0
        time1 = str1.split(":")
        time2 = str2.split(":")
        minres = time1[2]+time2[2]
        if minres >= 60:
            hourres += 60//minres
        hourres += time1[1] + time2[1]
        dayres += time1[0] + time2[0]
    else:
        
elif control in [3,4]:
    pass
elif control in [5,6,7]:
    pass
elif control ==8:
    pass

    
