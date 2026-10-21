class Student:
    university = 'UWA'
    def __init__(self, sid, name): # constructor (method)
        self.sid = sid # attribute
        self.name = name # attribute
        self.units = []
    def setID(self, sid): # method
        self.sid = sid
    def setName(self, name): # method
        self.name = name
    def printInfo(self): # method
        print('The name of student is', self.name, ', the ID is', self.sid)
    def enrollUnit(self, unit):
        self.units.append(unit)
    def printUnits(self):
        for u in self.units:
            u.printInfo()

class Unit:
    def __init__(self, code, name): # constructor (method)
        self.code = code # attribute
        self.name = name # attribute
        self.students = []
    def setCode(self, code): # method
        self.code = code
    def setName(self, name): # method
        self.name = name
    def printInfo(self): # method
        print('The name of unit is', self.name, ', the code is', self.code)
    def addStudent(self, student):
        self.students.append(student)
        student.units.append(self)
    def printStudents(self):
        names = []
        for s in self.students:
            names.append(s.name)
        info_str = ' '.join(names)
        print(info_str)

s1 = Student('11111111', 'Tim')
s2 = Student('22222222', 'April')
s3 = Student('33333333', 'Bob')

u1 = Unit('1401', 'Python')
u2 = Unit('1402', 'Database')

u1.addStudent(s1)
#s1.enrollUnit(u1)

u1.addStudent(s2)
#s2.enrollUnit(u1)

u2.addStudent(s1)
#s1.enrollUnit(u2)

u2.addStudent(s3)
#s3.enrollUnit(u2)

