# สร้างตารางสอบ
exam_schedule = ExamSchedule()

# สร้างครู
teacher1 = Teacher("Dr. Smith", "Mathematics")
teacher2 = Teacher("Dr. Jane", "Physics")
teacher3 = Teacher("Dr. John", "Chemistry")

# เพิ่มวิชา
exam_schedule.add_subject("Math", 30, teacher1)
exam_schedule.add_subject("Physics", 25, teacher2)
exam_schedule.add_subject("Chemistry", 50, teacher3)

# เพิ่มห้องสอบ
exam_schedule.add_room("B101", 40, "Science Building")
exam_schedule.add_room("B102", 20, "Science Building")
exam_schedule.add_room("B103", 60, "Main Building")

# สร้างตารางสอบ
exam_schedule.create_schedule()

# แสดงตารางสอบ
exam_schedule.display_schedule()
