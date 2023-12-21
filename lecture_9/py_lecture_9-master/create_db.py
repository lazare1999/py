from database import Base, engine
from models import Item, Users

print("Creating database ....")

Base.metadata.create_all(engine)
