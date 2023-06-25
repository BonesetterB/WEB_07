from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session

result=session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .select_from(Grade).group_by(Group.id).order_by(desc('avg_grade')).all()
print(result)