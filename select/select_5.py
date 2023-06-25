from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session


teacher_id=1
result=session.query(Teacher.fullname, Discipline.name) \
    .select_from(Discipline)\
    .join(Teacher)\
    .where(and_(Discipline.teacher_id==teacher_id, Teacher.id==teacher_id))\
    .all()
print(result)
