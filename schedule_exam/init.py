class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Teacher: {self.name}, Department: {self.department}"


class Subject:
    def __init__(self, name, students, teacher):
        self.name = name
        self.students = students
        self.teacher = teacher

    def __str__(self):
        return f"Subject: {self.name}, Students: {self.students}, Supervisor: {self.teacher.name}"


class Room:
    def __init__(self, room_name, capacity, building):
        self.room_name = room_name
        self.capacity = capacity
        self.building = building

    def __str__(self):
        return f"Room: {self.room_name}, Capacity: {self.capacity}, Building: {self.building}"


class ExamSchedule:
    def __init__(self):
        self.subjects = []
        self.rooms = []
        self.schedule = []

    def add_subject(self, name, students, teacher):
        self.subjects.append(Subject(name, students, teacher))

    def add_room(self, room_name, capacity, building):
        self.rooms.append(Room(room_name, capacity, building))

    def create_schedule(self):
        for subject in self.subjects:
            assigned = False
            for room in self.rooms:
                if subject.students <= room.capacity:
                    self.schedule.append({
                        "subject": subject.name,
                        "room": room.room_name,
                        "students": subject.students,
                        "teacher": subject.teacher.name
                    })
                    self.rooms.remove(room)  # ใช้ห้องนี้แล้ว
                    assigned = True
                    break
            if not assigned:
                print(f"Cannot assign a room for subject: {subject.name}")

    def display_schedule(self):
        if not self.schedule:
            print("No schedule created yet.")
        else:
            for item in self.schedule:
                print(f"Subject: {item['subject']}, Room: {item['room']}, "
                      f"Teacher: {item['teacher']}, Students: {item['students']}")
