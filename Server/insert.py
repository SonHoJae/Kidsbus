from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_declarative import Base, Parent, Child, Location, Attentance

engine = create_engine('sqlite:///kidsbus_database.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

new_location = Location(name = "북문", latitude ="35.892520",longitude = "128.609681")
session.add(new_location)
session.commit()

new_location = Location(name = "반월당 11번출구", latitude ="35.865540",longitude = "128.594239")
session.add(new_location)
session.commit()
new_location = Location(name = "홈플러스 칠성점", latitude ="35.881383",longitude = "128.595800")
session.add(new_location)
session.commit()
new_location = Location(name = "대구시청", latitude ="35.871433",longitude = "128.601444")
session.add(new_location)
session.commit()
'''
# Insert a Person in the person table
new_parent = Parent(name ="호재",account = "sonhj97",password = "1234",birth_date = "19910707", phone_number = "010-9309-1329", location = new_location)
session.add(new_parent)
session.commit()

# Insert an Address in the address table
new_child = Child(name = '아이',gender='M',birth_date ='200000',parent = new_parent)
session.add(new_child)
session.commit()


new_child = Child(name = '아이2',gender='W',birth_date ='19980607',parent = new_parent)
session.add(new_child)
session.commit()

new_attendance = Attentance(date = "10/24/2016", is_attended = 'True', child_id = 1)
session.add(new_attendance)
session.commit()
'''