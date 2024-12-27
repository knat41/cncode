import json
import csv
from datetime import datetime, time, timedelta
from typing import List, Dict

# Base Interface สำหรับการพัฒนา Dependency Injection
class DataStorage:
    def save(self, data):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

# Implementation สำหรับจัดการข้อมูลในไฟล์ JSON
class JSONStorage(DataStorage):
    def __init__(self, filename: str):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

# Manager สำหรับจัดการครู
class TeacherManager:
    def __init__(self):
        self.teachers: Dict[str, Teacher] = {}

    def add_teacher(self, teacher: 'Teacher') -> None:
        self.teachers[teacher.teacher_id] = teacher

    def get_teacher(self, teacher_id: str) -> 'Teacher':
        return self.teachers.get(teacher_id)

    def import_teachers_from_file(self, filename: str) -> None:
        """Import teachers from a tab-delimited text file."""
        with open(filename, 'r', encoding='utf-8') as file:
            next(file)  # Skip header line
            for line in file:
                fields = line.strip().split('\t')
                if len(fields) < 3:
                    continue
                teacher_id, full_name, department = fields
                first_name, last_name = full_name.split(' ', 1)
                teacher = Teacher(first_name, last_name, department, teacher_id)
                self.add_teacher(teacher)

# Manager สำหรับจัดการห้องสอบ
class RoomManager:
    def __init__(self):
        self.rooms: List[ExamRoom] = []

    def add_room(self, room: 'ExamRoom') -> None:
        self.rooms.append(room)

    def get_available_room(self, capacity_required: int) -> 'ExamRoom':
        for room in self.rooms:
            if room.is_available and room.capacity >= capacity_required:
                room.is_available = False
                return room
        return None

# Validator สำหรับตรวจสอบ
class ScheduleValidator:
    @staticmethod
    def is_room_conflict(subject1: 'Subject', subject2: 'Subject') -> bool:
        """
        ตรวจสอบเวลาทับซ้อนของเวลา
        """
        return (subject1.start_time <= subject2.start_time < subject1.end_time or
                subject2.start_time <= subject1.start_time < subject2.end_time)

# Class สำหรับเก็บข้อมครู
class Teacher:
    def __init__(self, first_name: str, last_name: str, department: str, teacher_id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.teacher_id = teacher_id

    def __str__(self) -> str:
        return f"Teacher ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Department: {self.department}"

# Class สำหรับเก็บข้อมห้องสอบ
class ExamRoom:
    def __init__(self, room: str, supervisor: str, location: str, capacity: int = 40):
        self.room = room
        self.supervisor = supervisor
        self.location = location
        self.capacity = capacity
        self.is_available = True

    def __str__(self) -> str:
        return f"Room: {self.room}, Supervisor: {self.supervisor}, Location: {self.location}, Capacity: {self.capacity}"

# Class สำหรับเก็บข้อมวิชา
class Subject:
    def __init__(self, code: str, name: str, duration: int, start_time: time, num_students: int = 0):
        self.code = code
        self.name = name
        self.duration = duration
        self.start_time = start_time
        self.num_students = num_students
        self.exam_rooms: List[ExamRoom] = []
        self.end_time = self.calculate_end_time()

    def calculate_end_time(self) -> time:
        """
        คำนวณเวลาเลิกสอบจากเวลาเริ่มสอบและระยะเวลาสอบ
        """
        start_datetime = datetime.combine(datetime.today(), self.start_time)
        end_datetime = start_datetime + timedelta(minutes=self.duration)
        return end_datetime.time()

    def add_exam_room(self, room: ExamRoom) -> None:
        if self.get_total_capacity() < self.num_students:
            self.exam_rooms.append(room)

    def get_total_capacity(self) -> int:
        return sum(room.capacity for room in self.exam_rooms)

    def __str__(self) -> str:
        exam_rooms_str = "\n    ".join(str(room) for room in self.exam_rooms)
        return (f"Subject Code: {self.code}, Name: {self.name}, Start Time: {self.start_time}, "
                f"End Time: {self.end_time}, Duration: {self.duration} minutes, Students: {self.num_students}\n"
                f"    Exam Rooms:\n    {exam_rooms_str}")

# Class สำหรับเก็บข้อมวันสอบ
class ExamDay:
    def __init__(self, date: datetime.date):
        self.date = date
        self.subjects: List[Subject] = []

    def add_subject(self, subject: Subject, validator: ScheduleValidator) -> bool:
        """
        ตรวจสอบการทับซ้อนของเวลาสอบก่อนเพิ่มวิชา
        """
        for existing_subject in self.subjects:
            if validator.is_room_conflict(subject, existing_subject):
                print(f"Warning: Time conflict between {subject.code} and {existing_subject.code}")
                return False
        self.subjects.append(subject)
        return True

    def __str__(self) -> str:
        subjects_str = "\n".join(str(subject) for subject in self.subjects)
        return f"Exam Date: {self.date}\nSubjects:\n{subjects_str}"

# Class สำหรับจัดการตารงสอบ
class ExamScheduler:
    def __init__(self, storage: DataStorage, teacher_manager: TeacherManager, room_manager: RoomManager):
        self.storage = storage
        self.teacher_manager = teacher_manager
        self.room_manager = room_manager
        self.exam_days: List[ExamDay] = []

    def load_schedule(self):
        data = self.storage.load()
        self.exam_days = []

        for date_str, subjects in data.items():
            exam_day = ExamDay(datetime.fromisoformat(date_str).date())
            for subject_data in subjects:
                subject = Subject(
                    code=subject_data["code"],
                    name=subject_data["name"],
                    duration=subject_data["duration"],
                    start_time=datetime.strptime(subject_data["start_time"], "%H:%M").time(),
                    num_students=subject_data.get("num_students", 0)
                )
                for room_data in subject_data["exam_rooms"]:
                    room = ExamRoom(
                        room=room_data["room"],
                        supervisor=room_data["supervisor"],
                        location=room_data["location"],
                        capacity=room_data.get("capacity", 40)
                    )
                    subject.add_exam_room(room)
                exam_day.add_subject(subject, ScheduleValidator())
            self.exam_days.append(exam_day)

    def save_schedule(self):
        data = {}
        for exam_day in self.exam_days:
            date_str = exam_day.date.isoformat()
            data[date_str] = [
                {
                    "code": subject.code,
                    "name": subject.name,
                    "start_time": subject.start_time.strftime("%H:%M"),
                    "duration": subject.duration,
                    "num_students": subject.num_students,
                    "exam_rooms": [
                        {
                            "room": room.room,
                            "supervisor": room.supervisor,
                            "location": room.location,
                            "capacity": room.capacity
                        } for room in subject.exam_rooms
                    ]
                } for subject in exam_day.subjects
            ]
        self.storage.save(data)

    def add_exam_day(self, exam_day: ExamDay):
        self.exam_days.append(exam_day)

# ฟังก์ชันหลัก

def main() -> None:
    storage = JSONStorage("exam_schedule.json")
    teacher_manager = TeacherManager()
    room_manager = RoomManager()
    scheduler = ExamScheduler(storage, teacher_manager, room_manager)

    # โหลดข้อมูลจากไฟล์
    scheduler.load_schedule()

    # นำเข้าข้อมูลครูจากไฟล์
    teacher_manager.import_teachers_from_file('teacher.txt')

    # เพิ่มและตรวจว่าครูถุกเพิ่มในระบบ
    for teacher_id, teacher in teacher_manager.teachers.items():
        print(teacher)

    # สร้างวันสอบใหม่
    exam_day = ExamDay(datetime(2024, 12, 25).date())
    subject = Subject("MTH101", "Mathematics", 60, time(8, 30), 35)
    room = room_manager.get_available_room(subject.num_students)

    if room:
        subject.add_exam_room(room)
        exam_day.add_subject(subject, ScheduleValidator())
        scheduler.add_exam_day(exam_day)

    # บันทึกตารางสอบ
    scheduler.save_schedule()

if __name__ == "__main__":
    main()
