wd1=input()
i=0
for a in range(len(wd1)):
 if(wd1[a].isdigit() or wd1[a].isalpha() or wd1[a]==' '):
  continue
 else:
  i+=1
print(i)
