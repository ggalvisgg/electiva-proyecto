"""This module implements the FastAPI router for the reservation endpoints."""
from dotenv import load_dotenv
import os
from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-api-key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    """
    Retrieves the API key from the provided header and validates it.
    Parameters:
        api_key_header (str): The API key provided in the header.
    Returns:
        str: The validated API key.
    Raises:
        HTTPException: If the provided API key is invalid or unauthorized.
    """

    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "status": False,
                "status_code": status.HTTP_403_FORBIDDEN,
                "message": "Unauthorized",
            },
        )
