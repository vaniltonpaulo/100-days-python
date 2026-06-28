class Course:
    grade_scale = {
        "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0,
        "F": 0.0
    }

    def __init__(self,name,credit,grade):
        self.name = name
        self.credit = credit
        self.grade = grade.upper()

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,value):
        value = value.upper()
        if value not in self.grade_scale:
            raise ValueError("This grade doesnot exists")
        self._grade = value


    @property
    def grade_value(self):
        if self.grade not in self.grade_scale:
            raise ValueError("grade is not valid")
        return self.grade_scale[self.grade]
        
    @property
    def quality_points(self):
        return  self.grade_value * self.credit
        
    def __str__(self):
        return f"{self.name:<20} {self.grade:<3} {self.credit} cr"
    
        # add this method inside the Course class
    def to_dict(self):
        return {"name": self.name, "credit": self.credit, "grade": self.grade}
        
c = Course("Linear Algebra", 5, "a-")
print(c)
print(c.grade_value)
print(c.quality_points)



class Semester:
    def __init__(self,name):
        self.name = name
        self.courses = []
    
    def add_course(self,course):
        return self.courses.append(course)
    
    @property
    def total_credits(self):
        return sum(c.credit for c in self.courses)
    
    @property
    def total_quality_points(self):
        return sum(c.quality_points for c in self.courses)
    
    @property
    def gpa(self):
        if not self.courses:
            raise ValueError("Zero courses present")
        return self.total_quality_points / self.total_credits
        # add this method inside the Semester class
    def to_dict(self):
        return {
            "name": self.name,
            "courses": [c.to_dict() for c in self.courses],   # each course flattens itself
        }
        


fall = Semester("Fall 2025")

fall.add_course(Course("Linear Algebra", 5, "A-"))
fall.add_course(Course("Intro to CS", 6, "B+"))
print(fall.gpa)   # weighted average of the two
        


class Student:
    def __init__(self,name, student_id):
        self.name = name
        self.student_id = student_id
        self.semester = []

    def add_semester(self,semester):
        self.semester.append(semester)
    
    @property
    def cgpa(self):
        if not self.semester:
            raise ValueError("Zero semester present")
        total_points = sum(s.total_quality_points for s in self.semester)
        total_credits = sum( s.total_credits for s in self.semester)
        return total_points /total_credits



