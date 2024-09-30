"""This module contains the service functions for the user class."""
from app.models.user_model import User

def create_user_service(user):
    """
    Creates a new user in the database.

    Args:
        user (User): An object containing the user details.
        
    Returns:
        UserModel: The created user record.
    """
    user_record = User.create(
        idUser=user.idUser,
        name=user.name,
        password=user.password,
        email=user.email,
        photo=user.photo
    )
    return user_record

def get_user_service(user_id: int):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The unique identifier of the user.

    Returns:
        DICT: A dictionary containing the user's details.
        
    Raises:
        DoesNotExist: If the user with the given ID does not exist.
    """
    user = User.get_by_id(user_id)
    return{
        "id": user.idUser,
        "name": user.name,
        "password": user.password,
        "email": user.email,
        "photo": user.photo
    }
    
def get_all_users_service():
    """
    Retrieves all users from the database.

    Returns:
        List: A list of dictionaries containing the data of each user's details.
    """
    users = list(User.select())
    return [
        {
        "id": user.idUser,
        "name": user.name,
        "password": user.password,
        "email": user.email,
        "photo": user.photo
        }
        for user in users
    ]
    
def update_user_service(user_id: int, user_data: User):
    """
    Updates an existing user's details by their ID.

    Args:
        user_id (int): The ID of the customer to update.
        user_data (User): An object containing the updated user details.
        
    Returns:
        UserModel: The updated user record.
        
    Raises:
        DoesNotExist: If the user with the given ID does not exist.
    """
    user = User.get_by_id(user_id)
    user.name = user_data.name
    user.password = user_data.password
    user.email = user_data.email
    user.photo = user_data.photo
    user.save()
    return user

def delete_user_service(user_id: int):
    """
    Deletes a user from the database by their ID.

    Args:
        user_id (int): The ID of the user to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the user with the given ID does not exist.
    """
    user = User.get_by_id(user_id)
    user.delete_instance()
    return {"message": "User deleted successfully"}
