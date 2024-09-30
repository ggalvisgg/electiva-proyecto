"""This module is the main module of the FastAPI application."""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from app.helpers.api_key_auth import get_api_key
from app.config.database import database as connection
from app.routes.user_route import user_router
from app.routes.shopping_list_route import shopping_list_router
from app.routes.role_route import role_router
from app.routes.recipe_route import recipe_router
from app.routes.pantry_route import pantry_router
from app.routes.notification_route import notification_router
from app.routes.menu_route import menu_router
from app.routes.ingredient_route import ingredient_router
from app.routes.ingredient_inventory_route import ingredient_inventory_router
from app.routes.family_route import family_router
from app.routes.category_recipe_route import category_recipe_router
from app.routes.category_ingredient_route import category_ingredient_router

@asynccontextmanager
async def lifespan(_):
    """Asynchronous context manager for managing the lifespan of the FastAPI application."""
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    """Redirects the root path to the documentation."""
    return RedirectResponse(url="/docs")
#------ USER ROUTES -------
app.include_router(user_router, 
                   tags=["Users"], 
                   prefix="/api/users", 
                   dependencies=[Depends(get_api_key)])
#------ SHOPPING LIST ROUTES -------
app.include_router(shopping_list_router, 
                   tags=["Shopping Lists"], 
                   prefix="/api/shopping-lists", 
                   dependencies=[Depends(get_api_key)])
#------ ROLE ROUTES -------
app.include_router(role_router, 
                   tags=["Roles"], 
                   prefix="/api/roles", 
                   dependencies=[Depends(get_api_key)])

#------ RECIPE ROUTES -------
app.include_router(recipe_router, 
                   tags=["Recipes"], 
                   prefix="/api/recipes", 
                   dependencies=[Depends(get_api_key)])

#------ PANTRY ROUTES -------
app.include_router(pantry_router, 
                   tags=["Pantries"], 
                   prefix="/api/pantries", 
                   dependencies=[Depends(get_api_key)])
#------ NOTIFICATION ROUTES -------
app.include_router(notification_router, 
                   tags=["Notifications"], 
                   prefix="/api/notifications", 
                   dependencies=[Depends(get_api_key)])
#------ MENU ROUTES -------
app.include_router(menu_router, 
                   tags=["Menus"], 
                   prefix="/api/menus", 
                   dependencies=[Depends(get_api_key)])
#------ INGREDIENT ROUTES -------
app.include_router(ingredient_router, 
                   tags=["Ingredients"], 
                   prefix="/api/ingredients", 
                   dependencies=[Depends(get_api_key)])
#------ INGREDIENT INVENTORY ROUTES -------
app.include_router(ingredient_inventory_router, 
                   tags=["Ingredient Inventories"], 
                   prefix="/api/ingredient-inventories", 
                   dependencies=[Depends(get_api_key)])
#------ FAMILY ROUTES -------
app.include_router(family_router, 
                   tags=["Families"], 
                   prefix="/api/families", 
                   dependencies=[Depends(get_api_key)])
#------ CATEGORY RECIPE ROUTES -------
app.include_router(category_recipe_router, 
                   tags=["Category Recipes"], 
                   prefix="/api/category-recipes", 
                   dependencies=[Depends(get_api_key)])
#------ CATEGORY INGREDIENT ROUTES -------
app.include_router(category_ingredient_router, 
                   tags=["Category Ingredients"], 
                   prefix="/api/category-ingredients", 
                   dependencies=[Depends(get_api_key)])
