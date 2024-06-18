from math import pi,sqrt
import belt,gear,shaft,coupling,rolling_bearing,key,load_anlysis
def total_design():
    '''
    '''
    print("\n-----------------")
    print("Now,begin the total design\n")
    F=2490#measured in N
    v=1.7#measured in m/s
    D=0.47#measured in m
    nw=v/(D/2)/(2*pi)*60#measured in r/min
    Pw=F*v/1000  #P is the total output power(kW);

    eta_belt=0.95
    eta_coupler=0.99
    eta_rolling_bearing=0.99
    eta_sliding_bearing=0.98
    eta_gear=0.99
    eta_roll=0.96
    eta=eta_belt*eta_coupler**2*eta_rolling_bearing**3*eta_gear**2*eta_roll
    Pd=Pw/eta
    print("总的输出功率为 {} kW;\n总的传递效率为 {:.4}%;\n需要电动机的功率为 {:.3} kW\n".format(Pw,eta*100,Pd))

    nm=1440

    #Calculate the transmission ratio
    i=nm/nw
    i1=1.2
    i3=sqrt(i/(1.2*i1))
    i2=1.2*i3
    print("总传动比为：\n\ti={}".format(i))
    print("各级传动比分别为：\n\ti1={},\n\ti2={},\n\ti3={}".format(i1,i2,i3))
    i=[i1,i2,i3]
    #Calculate the rotate speed

    n1=nm/i1
    n2=n1/i2
    n3=n2/i3
    n4=n3
    print("各轴的转速分别为：\n\tn1={} r/min,\n\tn2={}r/min,\n\tn3={}r/min,\n\tn4={}r/min".format(n1,n2,n3,n4))
    n=[nm,n1,n2,n3,n4]
    #Calculate the power of each roller

    P1=Pd*eta_belt*eta_coupler
    P2=P1*eta_gear*eta_rolling_bearing
    P3=P2*eta_gear*eta_rolling_bearing
    P4=P3*eta_coupler*eta_rolling_bearing
    print("各轴的输入功率分别为：\n\tP1={}kW,\n\tP2={}kW,\n\tP3={}kW,\n\tP4={}kW".format(P1,P2,P3,P4))
    P=[Pd,P1,P2,P3,P4]
    #print(P4*eta_roll*eta_sliding_bearing**2)


    #Calculate the torque of each roller
    T1=9550*P1/n1
    T2=9550*P2/n2
    T3=9550*P3/n3
    T4=9550*P4/n4
    print("各轴的输入功率分别为：\n\tT1={} N·m,\n\tT2={} N·m,\n\tT3={} N·m,\n\tT4={} N·m".format(T1,T2,T3,T4))
    T=[T1,T2,T3,T4]
    return i,n,P,T

i,n,P,T=total_design()
belt=belt.belt(P=P[0],n=n[0],i=i[0])
gear1=gear.gear(P=P[1],n=n[1],i=i[1])
gear2=gear.gear(P=P[2],n=n[2],i=i[2])
shaft1=shaft.shaft(P=P[1],n=n[1])
shaft2=shaft.shaft(P=P[2],n=n[2])
shaft3=shaft.shaft(P=P[3],n=n[3])
shaft4=shaft.shaft(P=P[4],n=n[4])
couple=coupling.coupling(P=P[4],n=n[4])
rolling1=rolling_bearing.rolling(P=P[1],n=n[1],d=shaft1.d)
rolling2=rolling1
rolling3=rolling_bearing.rolling(P=P[2],n=n[2],d=shaft2.d)
rolling4=rolling3
rolling5=rolling_bearing.rolling(P=P[3],n=n[3],d=shaft3.d)
rolling6=rolling5

key1=key.key(T[0],35)
key2=key.key(T[1],60)
key3=key.key(T[2],82)
key3=key.key(T[3],90)

load_anlysis.force_analyze(gear1)