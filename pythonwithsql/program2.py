from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, session

# Create Declarative Base
Base = declarative_base()

# Student Table with 5 Columns
class Student(Base):
    __tablename__ = "students1"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    age = Column(Integer)
    department = Column(String(100))
    email = Column(String(100))

    def __repr__(self):
        return f"""
        Student(
            id={self.id},
            name='{self.name}',
            age={self.age},
            department='{self.department}',
            email='{self.email}'
        )
        """

# MySQL Connection
# Format:
# mysql+pymysql://root:password@host/database_name

DATABASE_URL = "mysql+pymysql://root:Goldenjef8@localhost/pythonclass"

engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

# Create Session
Session = sessionmaker(bind=engine)
session = Session()

# Create Table
Base.metadata.create_all(engine)

student1 = Student(
    name="Vignesh",
    age=23,
    department="Data Science",
    email="vignesh@gmail.com"
)

session.add(student1)
session.commit()

# -----------------------------------
# UPDATE Operation
# -----------------------------------
student_update = session.query(Student).filter_by(name="Vignesh").first()

if student_update:
    student_update.department = "AI & ML"
    student_update.age = 24

    session.commit()

    print("\nStudent Updated Successfully\n")

# Display After Update
print("After Update:\n")

students = session.query(Student).all()

for student in students:
    print(student)
    student_delete = session.query(Student).filter_by(name="Vignesh").first()

    if student_delete:
        session.delete(student_delete)
        session.commit()

        print("\nStudent Deleted Successfully\n")
#
#     # Final Records
#     print("Final Records:\n")
#
#     students = session.query(Student).all()
#
#     for student in students:
#         print(student)
#
#     # Close Session
#     session.close()