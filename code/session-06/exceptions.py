# try:
#     d = {}
#     # a = d[1]
#     x = 4 / 0
#     b = d.no_implemented_func()
# except (KeyError, ZeroDivisionError, AttributeError, Exception) as ex:
#     print(ex)

# try:
#     d = {}
#     # a = d[1]
#     # x = 4 / 0
#     b = d.no_implemented_func()
# except KeyError as ex:
#     print("NO pasanada", ex)
# except ZeroDivisionError as ex:
#     print("Dude divicion entre cero porfavoor!!!",ex)
# except AttributeError as ex:
#     print("Wrong atributo", ex)
# except Exception as ex:
#     print("Algo le paso a tu app", ex)

# else and finally
try:
    d = {}
    a = d[1]
except KeyError as ex:
    print("NO pasa nada", ex)
finally:
    # del object 
    print("print from finally")

def sum(num1, num2):
    if num1 == 0 or num2 == 0:
        raise ValueError("Values entered are not valid...")
    raise Exception("OOP!! bad connection")
    return num1 + num2

try:
    print(sum(2, 3))
    print(sum(2, 0))
except ValueError as ex:
    print("Value error")
except Exception as ex:
    print("General exception", ex)