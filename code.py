
# MA-157
# Oyvind Husabo

import math

def cube_newton(a):
    x0 = a-1

    for x in range(0,200):
        fx = x0**3 - a          # f(x)

        # Det var denne du mente?
        fd = 3*(x0*x0)          # f'(x)
        x0 = x0 - fx/fd
        print("a = %s, f(x) = %s" %(x0, fx))

        if fx < 1e-10:
            break

    print ("Finished after %s iterations. Cuberoot of %s is %s" %(x, a, x0))



def exponential_3root(a):
    q, m = math.frexp(a)

    q_root = q**(1.0/3.0)
    factor = 0.79370052598                  # 1.0 / cuberoot(2)

    # assignment A3-I 3)
    if m % 3:
        mod = m % 3
        if mod == 2:
            m = m - 2
            q_root *= (factor * 2.0)
        if mod == 1:
            m = m - 1
            q_root *= (factor * 1.58740105197)      # cuberoot of 2^2
        m = m / 3
    else:
        m = m / 3

    print ("Estimated cuberoot of %s is %s" %(a, math.ldexp(q_root, math.trunc(m))))


# includes answer to A3-II part 4.
def final_3root(a):
    q, m = math.frexp(a)

    # finding the factor.
    factor = 0.79370052598                  # 1.0 / cuberoot(2)
    #factor_m1 = 1.0 / 1.58740105197        # 1.0 / cuberoot(4)
    #factor_m2 = 1.0 / 1.2599210498953948   # 1.0 / cuberoot(2)

    # set an initial starting point. A+Bq has the same result as using the value from the minimized integral.
    #A = 0.44494
    #B = 0.555059
    #x0 = A + B*q

    # initial guessing value
    x0 = 0.89685

    # 3 iterations of the mantissa
    x0 = (1/3.0)*((q/(x0*x0)) + 2*x0)
    print("1: %s" %(x0))
    x0 = (1/3.0)*((q/(x0*x0)) + 2*x0)
    print("2: %s" %(x0))
    x0 = (1/3.0)*((q/(x0*x0)) + 2*x0)
    print("3: %s" %(x0))

    # make the exponent m divisible by 3 and multiply the mantissa by factors.
    if m % 3:
        mod = m % 3
        if mod == 2:
            m = m - 2
            x0 *= (factor * 2.0)
        if mod == 1:
            m = m - 1
            x0 *= (factor * 1.58740105197)
        m = m / 3
    else:
        m = m / 3

    #finalroot = x0 * (2**m)
    finalroot = math.ldexp(x0, math.trunc(m))
    return finalroot

    print ("Cuberoot of %a with 3 iterations of q: %s" %(a, finalroot))

#print (final_3root(27))
#print (final_3root(512))
#print (final_3root(8))
cube_newton(16)