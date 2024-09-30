"""This module contains the service functions for the role class."""
from app.models.role_model import Role

def create_role_service(role):
    """
    Creates a new role in the database.

    Args:
        role (Role): An object containing the role details.
        
    Returns:
        RoleModel: The created role record.
    """
    role_record = Role.create(
        idRole=role.idRole,
        name=role.nameRole,
        permissions=role.permissions
    )
    return role_record

def get_role_service(role_id: int):
    """
    Retrieves a role by its ID.

    Args:
        role_id (int): The unique identifier of the role.

    Returns:
        DICT: A dictionary containing the role's details.
        
    Raises:
        DoesNotExist: If the role with the given ID does not exist.
    """
    role = Role.get_by_id(role_id)
    return {
        "id": role.idRole,
        "name": role.nameRole,
        "permissions": role.permissions
    }

def get_all_roles_service():
    """
    Retrieves all roles from the database.

    Returns:
        List: A list of dictionaries containing the data of each role's details.
    """
    roles = list(Role.select())
    return [
        {
        "id": role.idRole,
        "name": role.nameRole,
        "permissions": role.permissions
        }
        for role in roles
    ]

def update_role_service(role_id: int, role_data: Role):
    """
    Updates an existing role's details by its ID.

    Args:
        role_id (int): The ID of the role to update.
        role_data (Role): An object containing the updated role details.
        
    Returns:
        RoleModel: The updated role record.
        
    Raises:
        DoesNotExist: If the role with the given ID does not exist.
    """
    role = Role.get_by_id(role_id)
    role.nameRole = role_data.nameRole
    role.permissions = role_data.permissions
    role.save()
    return role

def delete_role_service(role_id: int):
    """
    Deletes a role from the database by its ID.

    Args:
        role_id (int): The ID of the role to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the role with the given ID does not exist.
    """
    role = Role.get_by_id(role_id)
    role.delete_instance()
    return {"message": "Role deleted successfully"}
