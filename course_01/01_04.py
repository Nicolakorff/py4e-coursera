def computepay(h, r):
    if h > 40 :
        reg = r * h
        otp = (h - 40.0) * (r * 0.5)
        pay = reg + otp
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours: ")
rt = input("Enter Rate: ")
fhrs = float(hrs)
frt = float(rt)

p = computepay(fhrs, frt)
print("Pay", p)
