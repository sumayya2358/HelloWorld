m = ["apple", "banana", "cherry"]
m.insert(2, "watermelon")
print(m)
a = ("apple", "banana", "cherry" )
b = list(a)
b[1] = "kiwi"
a = tuple(b)
print(a)
q = ('apple', 'banana', 'cherry')
w = ('orange',)
q += w
print(q)
e = ('apple', 'banana', 'cherry')
r = list(e)
r.remove('apple')
e = tuple(r)
print(e)
n = ('aa','dd')
del n# tuple n deleted so no print
thisdict = {"brand": "ford", "model":"mustang" , "year":1964 }
thisdict["year"] = 2018
print(thisdict)
t = {"name": "ken", "age": 32 , "place":"kiyose"}
t.update({"place": "tokyo"})
print(t)




