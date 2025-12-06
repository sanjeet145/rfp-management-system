# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Replace these with your actual database details
# DATABASE_URL = "postgresql://username:password@localhost:5432/mydatabase"

# # Create an engine instance
# engine = create_engine(DATABASE_URL, echo=True)  # echo=True will log SQL queries

# # Create a base class for model definitions
# Base = declarative_base()

# # Create a session maker
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Example of creating a session
# session = SessionLocal()

# # Optionally, you can define models here
# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)

# # Create the tables in the database (if they don't exist)
# Base.metadata.create_all(bind=engine)

# # Closing the session
# session.close()
