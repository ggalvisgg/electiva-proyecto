"""
This module contains the routes for managing notification data.
"""
from fastapi import APIRouter, Body, HTTPException
from peewee import DoesNotExist
from app.models.notification_model import Notification
from app.services.notification_service import (
    create_notification_service,
    get_all_notifications_service,
    get_notification_service,
    update_notification_service,
    delete_notification_service
)

notification_router = APIRouter()

@notification_router.post("/")
def create_notification(notification: Notification = Body(...)):
    """
    Creates a new notification in the database.

    Parameters:
        notification (Notification): An object containing the notification details.
        
    Returns:
        The created notification object.
    """
    return create_notification_service(notification)

@notification_router.get("/{notification_id}")
def read_notification(notification_id: int):
    """
    Retrieves a notification by its ID.

    Args:
        notification_id (int): The ID of the notification to retrieve.

    Returns:
        Notification: The notification object.

    Raises:
        HTTPException: If the notification is not found.
    """
    try:
        return get_notification_service(notification_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Notification not found") from exc

@notification_router.get("/")
def read_notifications():
    """
    Reads and returns all notifications.

    Returns:
        List[Notification]: A list of all notifications.
    """
    return get_all_notifications_service()

@notification_router.put("/{notification_id}")
def update_notification(notification_id: int, notification_data: Notification = Body(...)):
    """
    Update a notification with the given notification_id and notification_data.

    Parameters:
        notification_id (int): The ID of the notification to update.
        notification_data (Notification): The updated notification data.

    Returns:
        The updated notification object.

    Raises:
        HTTPException: If the notification with the given ID does not exist.
    """
    try:
        return update_notification_service(notification_id, notification_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Notification not found") from exc

@notification_router.delete("/{notification_id}")
def delete_notification(notification_id: int):
    """
    Delete a notification with the given notification_id.

    Args:
        notification_id (int): The ID of the notification to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the notification does not exist.
    """
    try:
        return delete_notification_service(notification_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Notification not found") from exc
