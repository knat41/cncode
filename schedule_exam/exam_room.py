class ExamRoom:
    def __init__(self, room, supervisor, location):
        """
        :param room: ชื่อห้องสอบ เช่น "4/1"
        :param supervisor: ชื่อผู้ควบคุมสอบ เช่น "อ.สมชาย"
        :param location: สถานที่สอบ เช่น "อาคารเรียนรวม 1"
        """
        self.room = room
        self.supervisor = supervisor
        self.location = location

    def __str__(self):
        return f"Room: {self.room}, Supervisor: {self.supervisor}, Location: {self.location}"


class Subject:
    def __init__(self, code, name, duration, exam_time):
        """
        :param code: รหัสวิชา เช่น "ว31102"
        :param name: ชื่อวิชา เช่น "คณิตศาสตร์พื้นฐาน"
        :param duration: จำนวนเวลาสอบในนาที เช่น 60
        :param exam_time: ช่วงเวลาสอบ เช่น "8:30-9:30"
        """
        self.code = code
        self.name = name
        self.duration = duration
        self.exam_time = exam_time
        self.exam_rooms = []  # รายการของ ExamRoom

    def add_exam_room(self, room, supervisor, location):
        """
        เพิ่มห้องสอบในวิชา
        :param room: ชื่อห้องสอบ เช่น "4/1"
        :param supervisor: ชื่อผู้ควบคุมสอบ
        :param location: สถานที่สอบ
        """
        self.exam_rooms.append(ExamRoom(room, supervisor, location))

    def __str__(self):
        exam_rooms_str = "\n  ".join(str(room) for room in self.exam_rooms)
        return (f"Subject Code: {self.code}, Name: {self.name}, Duration: {self.duration} minutes, "
                f"Exam Time: {self.exam_time}\n  Exam Rooms:\n  {exam_rooms_str}")


# ตัวอย่างการใช้งาน
subject1 = Subject(
    code="ว31102",
    name="คณิตศาสตร์พื้นฐาน",
    duration=60,
    exam_time="8:30-9:30"
)

# เพิ่มข้อมูลห้องสอบ
subject1.add_exam_room("4/1", "อ.สมชาย", "อาคารเรียนรวม 1")
subject1.add_exam_room("4/2", "อ.สมหญิง", "อาคารเรียนรวม 2")
subject1.add_exam_room("4/3", "อ.สมฤดี", "อาคารเรียนรวม 1")

# แสดงผล
print(subject1)
