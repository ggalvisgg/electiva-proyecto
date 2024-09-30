"""This module contains the service functions for the notification class."""
from app.models.notification_model import Notification

def create_notification_service(notification):
    """
    Creates a new notification in the database.

    Args:
        notification (Notification): An object containing the notification details.
        
    Returns:
        NotificationModel: The created notification record.
    """
    notification_record = Notification.create(
        idNotification=notification.idNotification,
        message=notification.message,
        dateNotification=notification.dateNotification
    )
    return notification_record

def get_notification_service(notification_id: int):
    """
    Retrieves a notification by its ID.

    Args:
        notification_id (int): The unique identifier of the notification.

    Returns:
        DICT: A dictionary containing the notification's details.
        
    Raises:
        DoesNotExist: If the notification with the given ID does not exist.
    """
    notification = Notification.get_by_id(notification_id)
    return {
        "id": notification.idNotification,
        "message": notification.message,
        "date": notification.dateNotification
    }

def get_all_notifications_service():
    """
    Retrieves all notifications from the database.

    Returns:
        List: A list of dictionaries containing the data of each notification's details.
    """
    notifications = list(Notification.select())
    return [
        {
        "id": notification.idNotification,
        "message": notification.message,
        "date": notification.dateNotification
        }
        for notification in notifications
    ]

def update_notification_service(notification_id: int, notification_data: Notification):
    """
    Updates an existing notification's details by its ID.

    Args:
        notification_id (int): The ID of the notification to update.
        notification_data (Notification): An object containing the updated notification details.
        
    Returns:
        NotificationModel: The updated notification record.
        
    Raises:
        DoesNotExist: If the notification with the given ID does not exist.
    """
    notification = Notification.get_by_id(notification_id)
    notification.message = notification_data.message
    notification.dateNotification = notification_data.dateNotification
    notification.save()
    return notification

def delete_notification_service(notification_id: int):
    """
    Deletes a notification from the database by its ID.

    Args:
        notification_id (int): The ID of the notification to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the notification with the given ID does not exist.
    """
    notification = Notification.get_by_id(notification_id)
    notification.delete_instance()
    return {"message": "Notification deleted successfully"}
