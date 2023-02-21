result = []
def divider(a, b):
 try:
  if a < b:
   raise ValueError
  if b > 100:
   raise IndexError
  return a/b
 except OSError:
  print("OSError")
 except NameError:
  print("Namerror")
 except ValueError:
  print("Value error")
 except RuntimeError:
  print("run time error")
 except TypeError:
  print("type Error")
 except ZeroDivisionError:
  print("Zero Division Error")


data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
 res = divider(key, data[key])
 result.append(res)

print(result)