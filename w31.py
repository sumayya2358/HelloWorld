names = ["nani","danish","paneer"]
for name in names:
    for index in range(0, len(name), 2):
        print(name[index])

x = "sumayya"
for i in range(1, len(x),2):
    print(x[i])

txt = "the best thing is free"
print("free" in txt)
print("expensive" not in txt)
if "expensive" not in txt:
    print("no,it is not present")

