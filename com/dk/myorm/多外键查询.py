import 多外键关联 as mulitfor

from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=mulitfor.engine)
Session = Session_class()

a1 = mulitfor.Address(street='kangqiao',city='shanghai',state='china')
a2 = mulitfor.Address(street='pudong',city='shanghai',state='china')
a3 = mulitfor.Address(street='sanlin',city='shanghai',state='china')
a4 = mulitfor.Address(street='gaohang',city='shanghai',state='china')

c1 = mulitfor.Customer(name='han1',billing_address=a1,shipping_address=a2)
c2 = mulitfor.Customer(name='han2',billing_address=a2,shipping_address=a3)
c3 = mulitfor.Customer(name='han3',billing_address=a3,shipping_address=a4)

# Session.add_all([a1,a2,a3,a4])
# Session.add_all([c1,c2,c3])

Session.commit()

data = Session.query(mulitfor.Customer).filter(mulitfor.Customer.name=='han1').first()

print(data.name,data.billing_address,data.shipping_address)