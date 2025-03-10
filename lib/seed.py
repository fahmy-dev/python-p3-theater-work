from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Audition, Role

engine = create_engine('sqlite:///theater.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear data
session.query(Audition).delete()
session.query(Role).delete()
session.commit()

# Create roles
role1 = Role(character_name="Hamlet")
role2 = Role(character_name="Macbeth")

session.add_all([role1, role2])
session.commit()

# Create auditions
audition1 = Audition(actor="John Doe", location="New York", phone=1234567890, role=role1)
audition2 = Audition(actor="Jane Smith", location="Los Angeles", phone=9876543210, role=role2)

session.add_all([audition1, audition2])
session.commit()

print("Database seeded successfully!")
