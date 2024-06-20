from math import tan,cos,radians

def force_analyze(gear):
    
    alpha=radians(gear.alpha)
    beta=radians(gear.beta)
    F_t1=2*gear.T/gear.d1*1000
    F_r1=F_t1*tan(alpha)/cos(beta)
    F_a1=F_t1*tan(beta)

    F_t2=2*gear.T/gear.d2*1000
    F_r2=F_t2*tan(alpha)/cos(beta)
    F_a2=F_t2*tan(beta)

    print("\t小齿轮：")
    print("\t\t小齿轮圆周力F_t1 = {:.7} N".format(F_t1))
    print("\t\t小齿轮径向力F_r1 = {:.7} N".format(F_r1))
    print("\t\t小齿轮轴向力F_a1 = {:.7} N".format(F_a1))

    print("\t大齿轮：")
    print("\t\t大齿轮圆周力F_t2 = {:.7} N".format(F_t2))
    print("\t\t大齿轮径向力F_r2 = {:.7} N".format(F_r2))
    print("\t\t大齿轮轴向力F_a2 = {:.7} N".format(F_a2))



