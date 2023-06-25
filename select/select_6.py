from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session


id=1
result=session.query(Group.name, Student.fullname) \
    .select_from(Student)\
    .join(Group)\
    .where(and_(Group.id==id))\
    .all()
print(result)