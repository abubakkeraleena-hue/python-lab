color =[]
n = int(input("enter total number of color:"))
print("enter color")
for i in range(n):
    ch = input()
    color.append(ch)
print(f"first color is{color[0]}\ n Last color is:{color[-1]}")
