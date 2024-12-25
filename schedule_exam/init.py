class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Teacher: {self.name}, Department: {self.department}"


class Subject:
    def __init__(self, code, name, duration, exam_time, exam_rooms):
        """
        :param code: รหัสวิชา เช่น "ว31102"
        :param name: ชื่อวิชา เช่น "คณิตศาสตร์พื้นฐาน"
        :param duration: จำนวนเวลาสอบในนาที เช่น 60
        :param exam_time: ช่วงเวลาสอบ เช่น "8:30-9:30"
        :param exam_rooms: รายชื่อนักเรียนห้องที่สอบ เช่น ["4/1", "4/2", ..., "4/17"]
        """
        self.code = code
        self.name = name
        self.duration = duration
        self.exam_time = exam_time
        self.exam_rooms = exam_rooms

    def __str__(self):
        return (f"Subject Code: {self.code}, Name: {self.name}, Duration: {self.duration} minutes, "
                f"Exam Time: {self.exam_time}, Exam Rooms: {', '.join(self.exam_rooms)}")


# ตัวอย่างการใช้งาน
subject1 = Subject(
    code="ว31102",
    name="คณิตศาสตร์พื้นฐาน",
    duration=60,
    exam_time="8:30-9:30",
    exam_rooms=[f"4/{i}" for i in range(1, 18)]
)

print(subject1)



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
