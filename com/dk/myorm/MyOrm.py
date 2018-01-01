import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

from sqlalchemy.orm import sessionmaker

from sqlalchemy import func

# engine = create_engine('mysql+pymysql://root:root@localhost/mydata',encoding='utf-8',echo=True)
engine = create_engine('mysql+pymysql://root:root@localhost/mydata',encoding='utf-8')

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return '<%s name:%s password:%s>' % (self.id,self.name,self.password)

Base.metadata.create_all(engine)    #创建表结构

Session_class = sessionmaker(bind=engine)

Session = Session_class()

#添加数据
# user_obj1 = User(name='han',password='han')
# user_obj2 = User(name='han1',password='han1')
#
# Session.add(user_obj1)
# Session.add(user_obj2)
#
# Session.commit()

# 查询
# data = Session.query(User).filter(User.name=='han').all()
# data = Session.query(User).filter().all()
# print(data)


# 修改
# data = Session.query(User).filter().first()
# data.name='test'
# data.password='test'
# Session.commit()

#回滚
# Session.rollback()

# 统计
# data = Session.query(User).filter().count()
# print(data)

# 分组
# data = Session.query(func.count(User.name),User.name).group_by(User.name).all()
# print(data)

# 删除
data = Session.query(User).filter(User.id==1).one()
print(data)
Session.delete(data)
Session.commit()