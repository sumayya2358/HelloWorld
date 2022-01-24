a = "hello ,world"
print(a[-5:-2])

txt = ' best things are free '
print( "the" not in txt)
print(txt.upper())
print(txt.lower())
print(txt.strip())
print(txt.replace("f" ,"p"))
print(txt.split(" , "))

txtt = 'yes'
new_txt = txt +' '+ txtt
print(new_txt)

quantity = 3
itemno = 567
price = 50
myorder = "i want {} pieces of item {} for {}dollars"
print(myorder.format(quantity, itemno, price))
myneworder = "i want to pay {2} dollars for {0} pieces of item {1}"
print(myneworder.format(quantity, itemno, price))

