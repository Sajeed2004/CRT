class student:
    def __init__(self,marks):
        self.marks=marks
        self.__marks=marks
    def getter(self):
        return self.__marks
    def setter(self,marks):
        self.__marks=marks
s1=student(0)
# set the data
s1.setter(79)
# get the data
s1.setter(99)

ans=s1.getter()
print(ans)