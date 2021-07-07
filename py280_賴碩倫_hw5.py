#-*-coding:UTF-8 -*-
# 類別作業練習 EX05_hw.py
#
# 測試資料 http://140.112.31.82/wordpress/?p=216

class student:

    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []

    def add(self,grade):
        #do something.
        self.grades.append(grade)

    def avg(self):
        #do something.
        #return avg_grade
        total_grade=0
        for i in self.grades:
            total_grade+=i
        avg_grade=total_grade/len(self.grades)
        return avg_grade

    def fcount(self):
        #do something.
        #return fail_count
        fail_count=0
        for i in self.grades:
            if i < 60:
                fail_count+=1
        return fail_count

def top():
    avg=[]
    for i in dic:
        avg.append(dic[i].avg())
    avg_top=max(avg)
    yield avg_top
    #yield avg_top
    for i in dic:
        if dic[i].avg()==avg_top:
            yield i        

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

dic={'Tom':s1,'Jane':s2,'John':s3,'Ann':s4,'Peter':s5}
for i in dic:
    print("%5s's average grade is %.1f"%(i,dic[i].avg()))
print('')
for i in dic:
    if dic[i].fcount()>1:
        print("%5s has failed %i tests"%(i,dic[i].fcount()))
    else:
        print("%5s has failed %i test"%(i,dic[i].fcount()))
print('')
top_student=list(top())
print(top_student[1],'has the highest average grade:',top_student[0])

