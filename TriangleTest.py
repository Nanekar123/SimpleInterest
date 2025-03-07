#Rectangle Test
#taking input from user
angle1=int(input("enter angle one"))
if  angle1>0:
    angle2=int(input("enter angle two"))
    if angle2>0:
        angle3=int(input("enter angle three"))
        if angle3>0:
            #cheking it is triangle or not
            if(angle1+angle2+angle3)==180:
                if angle1==60 and angle2==60 and angle3==60:
                    print("eqilateral triangle")
                elif angle1==90 or angle2==90 or angle3==90:
                    print("rightangle triangle")
            else:
                print("angles does not form an triangle")
