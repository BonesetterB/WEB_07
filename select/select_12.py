from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/WEB_07')

from create_basssee import Teacher, Student, Discipline, Grade, Group
from daabee import session


group_id = 3
dis_id = 4
subq = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == dis_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1)).scalar_subquery()

result = session.query(Student.fullname, Discipline.name, Group.name, Grade.grade, Grade.date_of) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(and_(Grade.discipline_id == dis_id, Group.id == group_id, Grade.date_of == subq)) \
        .order_by(desc(Grade.date_of)).all()

print(result)