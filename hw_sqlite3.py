import sqlite3


class University:
    def __init__(self, name_un):
        self.name_un = name_un
        self.conn = sqlite3.connect('my_database.db')
        self.conn.execute('PRAGMA foreign_keys = ON')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject TEXT,
        grades REAL,
        FOREIGN KEY (student_id) REFERENCES students(id)
        )
        ''')

    def add_student(self, name, age):
        self.cursor.execute('INSERT INTO Students (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()

    def add_grade(self, student_id, subject, grade):
        self.cursor.execute('INSERT INTO Grades (student_id, subject, grades) VALUES (?, ?, ?)',
                            (student_id, subject, grade))
        self.conn.commit()

    def get_students(self, subject=None):
        if subject is not None:
            self.cursor.execute('SELECT name, age, subject, grades FROM Students JOIN Grades '
                                'ON Students.id = Grades.student_id WHERE subject = (?)', (subject,))
            results = self.cursor.fetchall()
            return results

        else:
            self.cursor.execute('SELECT name, age, subject, grades FROM Students JOIN Grades '
                                'ON Students.id = Grades.student_id')
            results = self.cursor.fetchall()
            return results


u1 = University('Urban')

# u1.add_student('Ivan', 26) # id - 1
# u1.add_student('Ilya', 24) # id - 2
# u1.add_student('Anton', 24) # id - 3
# u1.add_student('Sergey', 38) # id - 4
# u1.add_student('Anastasia', 21) # id - 5
#
# u1.add_grade(1, 'Python', 4.8)
# u1.add_grade(2, 'PHP', 4.3)
# u1.add_grade(3, 'Python', 5.0)
# u1.add_grade(4, 'C++', 5.0)
# u1.add_grade(5, 'Pascal', 4.0)

print(u1.get_students())
print(u1.get_students('Python'))
print(u1.get_students('Pascal'))



