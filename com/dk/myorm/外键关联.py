from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE
from sqlalchemy import ForeignKey

from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import func


engine = create_engine('mysql+pymysql://root:root@localhost/mydata',encoding='utf-8')
Base = declarative_base()

class Student(Base):
    __tablename__  = 'student'
    id = Column(Integer, primary_key = True)
    name = Column(String(32), nullable = False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return '<%s name:%s>' % (self.id, self.name)

class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey('student.id'))

    student = relationship('Student',backref='my_study_record')

    def __repr__(self):
        return '<%s day:%s status:%s name:%s>' % (self.id,self.day,self.status,self.student.name)


Base.metadata.create_all(engine)

Session_class = sessionmaker(bind = engine)

Session = Session_class()

# s1 = Student(name = 's1',register_date = '2017-12-01')
# s2 = Student(name = 's2',register_date = '2017-12-02')
# s3 = Student(name = 's3',register_date = '2017-12-03')
# s4 = Student(name = 's4',register_date = '2017-12-04')
#
# st1 = StudyRecord(day = 1,status = 'YES',stu_id = 1)
# st2 = StudyRecord(day = 2,status = 'NO',stu_id = 1)
# st3 = StudyRecord(day = 3,status = 'YES',stu_id = 1)
# st4 = StudyRecord(day = 1,status = 'YES',stu_id = 2)
#
# Session.add_all([s1,s2,s3,s4,st1,st2,st3,st4])
# Session.add_all([s1,s2,s3,s4])
# Session.add_all([st1,st2,st3,st4])

# data = Session.query(Student).filter(Student.name == 's1').first()
# print(data)

data = Session.query(StudyRecord).filter().all()
print(data)

Session.commit()
