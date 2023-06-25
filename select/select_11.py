from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session


st_id=4
tech_id=3
result=session.query(Student.fullname, Teacher.fullname, func.round(func.avg(Grade.grade),2)) \
    .select_from(Student)\
    .join(Grade)\
    .join(Discipline)\
    .join(Teacher)\
    .where(and_(Student.id==st_id, Teacher.id==tech_id))\
    .group_by(Student.fullname, Teacher.fullname) \
    .all()
print(result)