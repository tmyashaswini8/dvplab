n=3
marks=[]
for i in range(0,n):
    test_mark=float(input("Enter the marks:"))
    marks.append(test_mark)
marks.sort(reverse=True)
print("Best of average test marks:",marks[0],marks[1])
