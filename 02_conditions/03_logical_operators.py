#  Logical and operator start
age = 18
cnic = True

if age >= 18 and cnic == True :
    print("you are eligible to marry")
else :
    print("you are not eligible to marry")


username = "Shoaib"
password = "admin123"

if username == 'Shoaib' and password == 'admin123' :
    print("Login successfully. you have access to this project. you can use it.")
else :
    print("Loing declined. you are not eligibal for project services.please try again")

# Logical and operator end

# Logical or operator start

spoone = True
plate  = True
glass = False

if (spoone and plate) or glass :
    print("You are eating in the afternoon")
else :
    print("you are not eating in the afternoon")

# Logical or operator end

# Logical not operator start

is_logged_in = False

if not is_logged_in:
    print("Please login first")

# Logical not operator end

