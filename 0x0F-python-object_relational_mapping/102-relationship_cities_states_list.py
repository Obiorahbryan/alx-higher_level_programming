#!/usr/bin/python3
# Lists all City objects from the database hbtn_0e_101_usa.
# Usage: ./102-relationship_cities_states_list.py <mysql username> /
#                                                 <mysql password> /
#                                                 <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

# Create connection to database
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

# Create a session to query the database
Session = sessionmaker(bind=engine)
session = Session()

# Query for all City objects sorted by id
cities = session.query(City).order_by(City.id).all()

# Print the id and name of each city and the state it belongs to
for city in cities:
    print("{}: {}. {}".format(city.id, city.name, city.state.name))

# Close the session
session.close()

