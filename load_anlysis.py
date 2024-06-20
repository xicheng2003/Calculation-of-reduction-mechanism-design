from math import tan, cos, radians

def calculate_forces(T, d, alpha, beta):
    F_t = 2 * T / d * 1000
    F_r = F_t * tan(alpha) / cos(beta)
    F_a = F_t * tan(beta)
    return F_t, F_r, F_a

def force_analyze(gear):
    alpha = radians(gear.alpha)
    beta = radians(gear.beta)

    F_t1, F_r1, F_a1 = calculate_forces(gear.T, gear.d1, alpha, beta)
    F_t2, F_r2, F_a2 = calculate_forces(gear.T, gear.d2, alpha, beta)

    def print_forces(name, F_t, F_r, F_a):
        print(f"\t{name}：")
        print(f"\t\t{name}圆周力F_t = {F_t:.7} N")
        print(f"\t\t{name}径向力F_r = {F_r:.7} N")
        print(f"\t\t{name}轴向力F_a = {F_a:.7} N")

    print_forces("小齿轮", F_t1, F_r1, F_a1)
    print_forces("大齿轮", F_t2, F_r2, F_a2)




