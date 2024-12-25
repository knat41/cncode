class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"


class GradeLevel:
    def __init__(self, grade_name):
        self.grade_name = grade_name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def display_rooms(self):
        print(f"Grade {self.grade_name}:")
        for room in self.rooms:
            print(f"  {room}")


class School:
    def __init__(self):
        self.grade_levels = {}

    def add_grade_level(self, grade_name):
        self.grade_levels[grade_name] = GradeLevel(grade_name)

    def add_room_to_grade(self, grade_name, room_number, room_type):
        if grade_name not in self.grade_levels:
            self.add_grade_level(grade_name)
        self.grade_levels[grade_name].add_room(Room(room_number, room_type))

    def display_school(self):
        for grade_name, grade in self.grade_levels.items():
            grade.display_rooms()


# สร้างโรงเรียนและเพิ่มข้อมูล
school = School()

# กำหนดประเภทห้องเรียน
junior_types = {
    1: "Gifted",
    2: "Top Star",
    3: "Top Star",
    **{i: "Regular" for i in range(4, 16)}
}

senior_types = {
    1: "SMTE",
    2: "Top Star",
    3: "Top Star",
    **{i: "Science" for i in range(4, 10)},
    10: "Arts",
    11: "Arts",
    12: "Chinese",
    13: "Japanese",
    14: "Japanese",
    15: "French/Korean"
}

# เพิ่มข้อมูลระดับชั้น ม.1 - ม.6
for grade in range(1, 7):
    for room_number in range(1, 18):
        if grade <= 3:  # ม.ต้น
            room_type = junior_types.get(room_number, "Regular")
        else:  # ม.ปลาย
            room_type = senior_types.get(room_number, "Regular")
        school.add_room_to_grade(f"M.{grade}", room_number, room_type)

# แสดงข้อมูลโรงเรียน
school.display_school()
