from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session


result=session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .select_from(Grade).where(Grade.discipline_id==3).join(Student).group_by(Student).order_by(desc('avg_grade')).first()

print(result)