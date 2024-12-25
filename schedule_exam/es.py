import json
import csv
from datetime import datetime, time

class ExamRoom:
    def __init__(self, room, supervisor, location):
        self.room = room
        self.supervisor = supervisor
        self.location = location

    def __str__(self):
        return f"Room: {self.room}, Supervisor: {self.supervisor}, Location: {self.location}"

class Subject:
    def __init__(self, code, name, duration, start_time):
        self.code = code
        self.name = name
        self.duration = duration
        self.start_time = start_time
        self.exam_rooms = []

    def add_exam_room(self, room, supervisor, location):
        self.exam_rooms.append(ExamRoom(room, supervisor, location))

    def __str__(self):
        exam_rooms_str = "\n    ".join(str(room) for room in self.exam_rooms)
        return (f"  Subject Code: {self.code}, Name: {self.name}, Start Time: {self.start_time}, "
                f"Duration: {self.duration} minutes\n    Exam Rooms:\n    {exam_rooms_str}")

class ExamDay:
    def __init__(self, date):
        self.date = date
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self):
        subjects_str = "\n".join(str(subject) for subject in self.subjects)
        return f"Exam Date: {self.date}\nSubjects:\n{subjects_str}"

def export_to_json(filename, exam_days):
    data = {}
    for exam_day in exam_days:
        date_str = exam_day.date.isoformat()
        data[date_str] = [
            {
                "code": subject.code,
                "name": subject.name,
                "start_time": subject.start_time.strftime("%H:%M"),
                "duration": subject.duration,
                "exam_rooms": [
                    {
                        "room": room.room,
                        "supervisor": room.supervisor,
                        "location": room.location
                    } for room in subject.exam_rooms
                ]
            } for subject in exam_day.subjects
        ]
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def export_to_csv(filename, exam_days):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Exam Date", "Subject Code", "Subject Name", "Start Time", "Duration", "Room", "Supervisor", "Location"])
        for exam_day in exam_days:
            for subject in exam_day.subjects:
                for room in subject.exam_rooms:
                    writer.writerow([
                        exam_day.date,
                        subject.code,
                        subject.name,
                        subject.start_time,
                        subject.duration,
                        room.room,
                        room.supervisor,
                        room.location
                    ])

def main():
    # Create exam days
    exam_day1 = ExamDay(datetime(2024, 12, 25).date())
    exam_day2 = ExamDay(datetime(2024, 12, 26).date())

    # Create subjects
    subject1 = Subject(
        code="ว31102",
        name="คณิตศาสตร์พื้นฐาน",
        duration=60,
        start_time=time(8, 30)
    )
    subject2 = Subject(
        code="ว31103",
        name="ฟิสิกส์พื้นฐาน",
        duration=90,
        start_time=time(10, 0)
    )
    subject3 = Subject(
        code="ว31104",
        name="เคมีพื้นฐาน",
        duration=60,
        start_time=time(8, 30)
    )

    # Add exam rooms
    subject1.add_exam_room("4/1", "อ.สมชาย", "อาคารเรียนรวม 1")
    subject1.add_exam_room("4/2", "อ.สมหญิง", "อาคารเรียนรวม 2")
    subject2.add_exam_room("4/3", "อ.สมฤดี", "อาคารเรียนรวม 1")
    subject3.add_exam_room("4/4", "อ.สมชาติ", "อาคารเรียนรวม 3")

    # Add subjects to exam days
    exam_day1.add_subject(subject1)
    exam_day1.add_subject(subject2)
    exam_day2.add_subject(subject3)

    # Display exam schedules
    print(exam_day1)
    print(exam_day2)

    # Export to JSON
    export_to_json("exam_schedule.json", [exam_day1, exam_day2])

    # Export to CSV
    export_to_csv("exam_schedule.csv", [exam_day1, exam_day2])

if __name__ == "__main__":
    main()
