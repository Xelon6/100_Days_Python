class job:
    name=None
    salary=None
    hours=None
    
    def __init__(self, name,salary,hours):
        
        self.name = name
        self.salary = salary
        self.hours = hours
    
    def infos(self):
        print()
        print(f"Job Type:\t {self.name}")
        print(f"Salary:\t\t € {self.salary}")
        print(f"Hours worked:\t {self.hours} h")


class doctor(job):
    
    speciality=None
    xp=None
    
    def __init__(self,salary,hours, speciality,xp):
        
        super().__init__("Doctor",salary,hours)
        self.speciality = speciality
        self.xp = xp
    
    def infos(self):
        print()
        super().infos()
        print(f"Speciality:\t {self.speciality}")
        print(f"Work experience: {self.xp} years")
        print()
    
class teacher(job):
    
    subject=None
    position=None
    
    def __init__(self,salary,hours,subject,position):
        
        super().__init__("Teacher",salary,hours)
        self.subject = subject
        self.position = position
        
    def infos(self):
        print()
        super().infos()
        print(f"Subject(s):\t {self.subject}")
        print(f"Position:\t {self.position}")
        print()



print("=========Jobs=========")
print()

lawyer=job("Lawyer","Too much","60")
lawyer.infos()

teach = teacher("not enough","too many","Maths, Coding","Classroom Teacher")
teach.infos()

doc = doctor("Enough for a Porsche","Enough","Teeth","15")
doc.infos()