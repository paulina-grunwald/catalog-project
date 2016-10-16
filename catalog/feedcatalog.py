from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="Tyler Huynh", email="tylerhuynh100@gmail.com", picture="https://cdn2.iconfinder.com/data/icons/happy-users/100/users09-512.png")
session.add(user1)
session.commit()

# Create category #1 and add items to the category
category1 = Category(name="Diffuse Nebulae", user_id=1)
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Carina Nebula",
                     description="The Carina Nebula (also known as the Great Nebula in Carina, the Eta Carinae Nebula, NGC 3372, as well as the Grand Nebula) is a large complex area of bright and dark nebulosity in the constellation of Carina, and is located in the CarinaSagittarius Arm. The nebula lies at an estimated distance between 6,500 and 10,000 light years from Earth. The nebula is one of the largest diffuse nebulae in our skies. Although it is some four times as large and even brighter than the famous Orion Nebula, the Carina Nebula is much less well known, due to its location in the southern sky. It was discovered by Nicolas Louis de Lacaille in 1751 from the Cape of Good Hope. Source: Wikipedia.com",
                     image = "/static/carina_nebula.jpg",
                     category=category1)
session.add(item1)
session.commit()

# Create category #2 and add items to the category
category2 = Category(name="Planetary Nebulae", user_id=1)
session.add(category2)
session.commit()

item2 = Item(user_id = 1, name = "Bug Nebula",
                     description ="NGC 6302, also called the Bug Nebula, Butterfly Nebula, is a bipolar planetary nebula in the constellation Scorpius. The structure in the nebula is among the most complex ever observed in planetary nebulae. The spectrum of NGC 6302 shows that its central star is one of the hottest stars in the galaxy, with a surface temperature in excess of 200,000 K, implying that the star from which it formed must have been very large (cf. PG 1159 star).",
                     image = "/static/bug_nebula.jpg",
                     category=category2)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Helix Nebula",
             description="The Helix Nebula, also known as The Helix, NGC 7293, is a large planetary nebula (PN) located in the constellation Aquarius. Discovered by Karl Ludwig Harding, probably before 1824, this object is one of the closest to the Earth of all the bright planetary nebulae. The estimated distance is about 215 parsecs (700 light-years). It is similar in appearance to the Cat's Eye Nebula and the Ring Nebula, whose size, age, and physical characteristics are similar to the Dumbbell Nebula, varying only in its relative proximity and the appearance from the equatorial viewing angle. The Helix Nebula has sometimes been referred to as the Eye of God in pop culture, as well as the Eye of Sauron.",
             image = "/static/helix_nebula.jpg",
             category=category2)
session.add(item3)
session.commit()

# Create category #3 and add items to the category
category3 = Category(name="Dark Nebulae", user_id=1)
session.add(category3)
session.commit()

item4 = Item(user_id=1, name="Horsehead Nebula",
             description="The Horsehead Nebula (also known as Barnard 33) is a dark nebula in the constellation Orion. The nebula is located just to the south of the star Alnitak, which is farthest east on Orion's Belt, and is part of the much larger Orion Molecular Cloud Complex. The nebula was first recorded in 1888 by Scottish astronomer Williamina Fleming on photographic plate B2312 taken at the Harvard College Observatory. The Horsehead Nebula is approximately 1500 light years from Earth. It is one of the most identifiable nebulae because of the shape of its swirling cloud of dark dust and gases, which bears some resemblance to a horse's head when viewed from Earth. (Source: Wikipedia.com)",
             image = "/static/horsehead_nebula.jpg",
             category=category3)
session.add(item4)
session.commit()

# Create category #4 and add items to the category
category4 = Category(name="Supernova Remnant", user_id=1)
session.add(category4)
session.commit()

item5 = Item(user_id=1, name="Cygnus Loop Nebula",
             description="The Cygnus Loop (radio source W78, or Sharpless 103) is a large supernova remnant (SNR) in the constellation Cygnus, an emission nebula measuring nearly 3 across. Some arcs of the loop, known collectively as the Veil Nebula or Cirrus Nebula, emit in the visible electromagnetic range Radio, infrared, and Xray images reveal the complete loop.",
             image = "/static/cygnusloop_nebula.jpg",
             category=category4)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Crab Nebula",
             description="The Crab Nebula (catalogue designations M1, NGC 1952, Taurus A) is a supernova remnant and pulsar wind nebula in the constellation of Taurus. The now-current name is due to William Parsons, 3rd Earl of Rosse, who observed the object in 1840 using a 36-inch telescope and produced a drawing that looked somewhat like a crab.[5] Corresponding to a bright supernova recorded by Chinese astronomers in 1054, thenebula was observed later by English astronomer John Bevis in 1731. The nebula was the first astronomical object identified with a historical supernova explosion.",
             image = "/static/crab_nebula.jpg",
             category=category4)
session.add(item6)
session.commit()