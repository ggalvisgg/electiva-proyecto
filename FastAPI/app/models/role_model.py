"""
This module contains the Pydantic model for role data.
"""
from pydantic import BaseModel

class Role(BaseModel):
    """
    Role model class.
    Attributes:
        idRole (int): The unique identifier of the user.
        nameRole (str): The name of the user.
        permissions (str): The permissions of the user.
    """
    idRole : int
    nameRole : str
    permissions : str
