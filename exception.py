try:
    x = [1, 2, 3, 4]
    x[4] = 2
except Exception as e:
    print("Error!" , e)
finally:
    x = [1, 2, 3, 4]
    print("Done")
    print(x)