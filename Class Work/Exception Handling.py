try:
    a=int(input("Enter the a: "))
    b=int(input("Enter the b: "))
    s=input("Enter the string: ")
    l=[1,2,3,4,5]
    d={"name":"rushi","course":"python"}
    print(d)
    k=input("Enter the key: ")
    print(d[k])
    print(l)
    ind=int(input("Enter the index value: "))
    print(l[ind])
    c=None
    c=c+s
    d=None
    print(a+s)
    print(a/b)

except ZeroDivisionError:
    print("b cannot be zero")

except ValueError:
    print("Please enter Integer value")

except TypeError:
    print("enter the same type")

except IndexError:
    print("Enter the Index between the range")

except KeyError:
    print("Key is not present")

else:
    print("All inputs are perfect no exceptions you can run the remaining code")

try:
    a = int(input("Enter the a:"))
    b = int(input("Enter the b:"))
    s = input("Enter the string")
    l = [1,2,3,4,5,6,7]
    d = {"Name":"Tarak", "Course": "Python"}
    print(l)
    print(d)
    ind = int(input("Enter the index value: "))
    key = input("Enter the Key value: ").title()
    print(d[key])
    print(l[ind])
    print(a+s)
    print(a/b)
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("All inputs are perfect no exceptions you can run the remaining code")

try:
    a = int(input("Enter the a:"))
    b = int(input("Enter the b:"))
    d = None
    d = a/b
    l = [1,2,3,4,5,6,7]
    ind = int(input("Enter the index value: "))
    val = None
    val = l[ind]
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("All inputs are perfect no exceptions you can run the remaining code")
finally:
    print(a,b,l)

try:
    a = int(input("Enter the a:"))
    b = int(input("Enter the b:"))
    d = None
    d = a/b
    l = [1,2,3,4,5,6,7]
    ind = int(input("Enter the index value: "))
    val = None
    val = l[ind]
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("All inputs are perfect no exceptions you can run the remaining code")
finally:
    print(a,b,l)