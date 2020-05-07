largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        i_num = int(num)
        if largest < i_num:
        	largest = i_num
        if smallest is None:
            smallest = i_num
        elif i_num < smallest:
        	smallest = i_num 
    except:
        print("Invalid input")
        continue


print("Maximum is", largest)
print("Minimum is", smallest)