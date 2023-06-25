from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session


gr_id=1
sub_id=3
result=session.query(Group.name, Student.fullname, Grade.grade) \
    .select_from(Student)\
    .join(Group)\
    .join(Grade)\
    .where(and_(Group.id==gr_id,Grade.discipline_id==sub_id))\
    .all()
print(result)