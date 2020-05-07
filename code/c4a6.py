
xh = float(input("Enter Hours:"))
xr = float(input("Enter Rate:"))

def computepay (h,r):
    if h > 40:
        pay  = (h - 40)*r*1.5 + 40*r
    else:
    	pay  = h*r
    return pay
        
print("Pay",computepay(xh,xr))
