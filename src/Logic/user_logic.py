from Entities.User import User
# Define functions for handling user logic

def create_user(session, name, email):
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
