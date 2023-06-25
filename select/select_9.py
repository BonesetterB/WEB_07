from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session


st_id=6
result=session.query(Student.fullname, Discipline.name) \
    .select_from(Student)\
    .join(Grade)\
    .join(Discipline)\
    .where(and_(Student.id==st_id))\
    .distinct() \
    .all()
print(result)