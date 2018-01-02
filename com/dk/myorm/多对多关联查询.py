import 多对多关联 as mulittomulit

from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=mulittomulit.engine)

Session = Session_class()

b1 = mulittomulit.Book(name='no game no life',pub_date='2015-12-12')
b2 = mulittomulit.Book(name='re0',pub_date='2016-12-12')
b3 = mulittomulit.Book(name='thb',pub_date='2017-12-12')

a1 = mulittomulit.Author(name='han1')
a2 = mulittomulit.Author(name='han2')
a3 = mulittomulit.Author(name='han3')

b1.authors = [a1,a2]
b2.authors = [a2,a3]
b3.authors = [a1,a2,a3]

# 添加
# Session.add_all([a1,a2,a3,b1,b2,b3])

book_obj = Session.query(mulittomulit.Book).filter(mulittomulit.Book.name=='no game no life').first()
print(book_obj,book_obj.authors)

author_obj = Session.query(mulittomulit.Author).filter(mulittomulit.Author.name=='han1').first()
print(author_obj,author_obj.books)

Session.commit()

