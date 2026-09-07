# #1
word= input("Enter a word: ")
num=int(len(word)/2)
i=0;
j=-1;
while i<num:
    if word[i]!=word[j]:
        print("NO!")
        break;
    else:
        i+=1;
        j-=1;
if i==num:
    print("YES!")
# 2
sen=input("Enter a sentence: ")
count=0
i=0
while i<len(sen):
    if sen[i]==' ':
        count+=1
    i+=1
print("the number of words is",count+1)
#3
sen=input("Enter a sentence: ")
count=0
i=1
initial=sen[0]
while i<len(sen):
    if sen[i]==' ':
        initial+= sen[i+1]
    i+=1
print(initial)