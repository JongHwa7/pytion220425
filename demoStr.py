# demoStr.py

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("P"))
print(strA.count("P, 7"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
strData = "<<< spam and ham >>>"
result = strData.strip("<> ")
print(strData)
print(result)

result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print(":)".join(lst))


