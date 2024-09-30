"""This module contains the database configuration and models for the FastAPI application."""
from app.config.settings import DATABASE
from peewee import AutoField, CharField, DateField, ForeignKeyField, Model, MySQLDatabase, TimeField

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

class Role(Model):
    """
    Represents a role in the database.
    
    Attributes:
        idRole (int): The unique identifier of the role.
        nameRole (str): The name of the role.
        permissions (str): The permissions of the role.
    """
    idRole = AutoField(primary_key=True)
    nameRole = CharField(max_length=255)
    permissions = CharField(max_length=255)

    class Meta:
        """Defines the metadata for the Role model."""
        database = database
        db_table = "roles"
        
class Family(Model):
    """
    Represents a family in the database.
    
    Attributes:
        idFamily (int): The unique identifier of the family.
        nameFamily (str): The name of the family. 
    """
    idFamily = AutoField(primary_key=True)
    nameFamily = CharField(max_length=255)

    class Meta:
        """Defines the metadata for the Family model."""
        database = database
        db_table = "families"
        
class User(Model):
    """
    Represents a user in the database.

    Attributes:
        idUser (int): The unique identifier of the user.
        nameUser (str): The name of the user.
        passwordUser (str): The password of the user.
        emailUser (str): The email address of the user.
        photoUser (str): The photo of the user.
        rolId (int): The role of the user.
        familyId (int): The family of the user.
    """
    idUser = AutoField(primary_key=True)
    nameUser = CharField(max_length=255)
    passwordUser = CharField(max_length=255)
    emailUser = CharField(max_length=255)
    photoUser = CharField(max_length=255)
    rolId = ForeignKeyField(Role, backref='users')
    familyId = ForeignKeyField(Family, backref='users')

    class Meta:
        """Defines the metadata for the User model."""
        database = database
        db_table = "users"
        
class Notification(Model):
    """
    Represents a notification in the database.
    
    Attributes:
        idNotification (int): The unique identifier of the notification.
        messageNotification (str): The message of the notification.
        dateNotification (date): The date of the notification.
        userId (int): The user of the notification.
    """
    idNotification = AutoField(primary_key=True)
    messageNotification = CharField(max_length=255)
    dateNotification = DateField()
    userId = ForeignKeyField(User, backref='notifications')

    class Meta:
        """Defines the metadata for the Notification model."""
        database = database
        db_table = "notifications"
        
class Pantry(Model):
    """
    Represents a pantry in the database.
    
    Attributes:
        idPantry (int): The unique identifier of the user.
        userId (int): The unique identifier of the user of the pantry.    
    """
    idPantry = AutoField(primary_key=True)
    userId = ForeignKeyField(User, backref='pantries')

    class Meta:
        """Defines the metadata for the Pantry model."""
        database = database
        db_table = "pantries"
        
class IngredientInventory(Model):
    """
    Represents a table the amount of an ingredient in the database.
    
    Attributes:
        ingredientId (int): The unique identifier of the ingredient.
        nameIngredient (str): The name of the ingredient.
        amountIngredient (str): The amount of the ingredient.
        unitIngredient (str): The unit of the ingredient.
        dateExpirationIngredient (date): The date expiration of the ingredient.
        pantryId (int): The unique identifier of the pantry.
    """
    ingredientId = AutoField(primary_key=True)
    nameIngredient = CharField(max_length=255)
    amountIngredient = CharField(max_length=255)
    unitIngredient = CharField(max_length=255)
    dateExpirationIngredient = DateField()
    pantryId = ForeignKeyField(Pantry, backref='ingredient_pantries')

    class Meta:
        """Defines the metadata for the IngredientPantry model."""
        database = database
        db_table = "ingredient_pantries"
        
class CategoryRecipe(Model):
    """
    Represents a category recipe in the database.
    
    Attributes:
        idCategoryRecipe (int): The unique identifier of the category recipe.
        nameCategoryRecipe (str): The name of the category recipe.
        descriptionCategoryRecipe (str): The description of the category recipe.
    """
    idCategoryRecipe = AutoField(primary_key=True)
    nameCategoryRecipe = CharField(max_length=255)
    descriptionCategoryRecipe = CharField(max_length=255)

    class Meta:
        """Defines the metadata for the CategoryRecipe model."""
        database = database
        db_table = "categoryRecipes"
        
class Recipe(Model):
    """
    Represents a recipe in the database.
    
    Attributes:
        idRecipe (int): The unique identifier of the recipe.
        nameRecipe (str): The name of the recipe.
        descriptionRecipe (str): The description of the recipe.
        categoryRecipe (str): The category of the recipe.
        difficultyRecipe (str): The difficulty of the recipe.
        timePreparation (time): The time preparation of the recipe.
        instructions (str): The instructions of the recipe.
        nutritionalData (str): The nutritional data of the recipe.
        userId (int): The user of the recipe.
        categoryId (int): The category of the recipe.
    """
    idRecipe = AutoField(primary_key=True)
    nameRecipe = CharField(max_length=255)
    descriptionRecipe = CharField(max_length=255)
    categoryRecipe = CharField(max_length=255)
    difficultyRecipe = CharField(max_length=255)
    timePreparation = TimeField()
    instructions = CharField(max_length=255)
    nutritionalData = CharField(max_length=255)
    userId = ForeignKeyField(User, backref='recipes')
    categoriaId = ForeignKeyField(CategoryRecipe, backref='recipes')

    class Meta:
        """Defines the metadata for the Recipe model."""
        database = database
        db_table = "recipes"
        
class Recipe_Category(Model):
    """ 
    Represents a table bridge between the recipe and the category recipe in the database.
    
    Attributes:
        recetaIdCR (int): The unique identifier of the recipe.
        categoriaIdCR (int): The unique identifier of the category of the recipe.
    """
    recetaIdCR = ForeignKeyField(Recipe, backref='category_recipes')
    categoriaIdCR = ForeignKeyField(CategoryRecipe, backref='category_recipes')

    class Meta:
        """Defines the metadata for the Category_Recipe model."""
        database = database
        db_table = "category_recipes"        
        
class Menu(Model):
    """
    Represents a menu in the database.
    
    Attributes:
        idMenu (int): The unique identifier of the menu.
        dateMenu (date): The date of the menu.
        userId (int): The user of the menu.
    """
    idMenu = AutoField(primary_key=True)
    dateMenu = DateField()
    userId = ForeignKeyField(User, backref='menus')

    class Meta:
        """Defines the metadata for the Menu model."""
        database = database
        db_table = "menus"
        
class Menu_Recipe(Model):
    """
    Represents a table bridge between the menu and the recipe in the database.
    
    Attributes:
        menuIdMR (int): The unique identifier of the menu.
        recipeIdMR (int): The recipe of the menu.
    """
    menuIdMR = ForeignKeyField(Menu, backref='menu_recipes')
    recipeIdMR = ForeignKeyField(Recipe, backref='menu_recipes')
    
    class Meta:
        """Defines the metadata for the Menu_Recipe model."""
        database = database
        db_table = "menu_recipes"        
        
class ShoppingList(Model):
    """
    Represents a shopping list in the database.
    
    Attributes:
        idShoppingList (int): The unique identifier of the shopping list.
        menuId (int): The unique identifier of the menu of the shopping list. 
    """
    idShoppingList = AutoField(primary_key=True)
    menuId = ForeignKeyField(Menu, backref='shopping_lists')

    class Meta:
        """Defines the metadata for the ShoppingList model."""
        database = database
        db_table = "shopping_lists"        
        
class CategoryIngredient(Model):
    """
    Represents a category ingredient in the database.
    
    Attributes:
        idCategoryIngredient (int): The unique identifier of the category ingredient.
        nameCategoryIngredient (str): The name of the category ingredient.
        descriptionCategoryIngredient (str): The description of the category ingredient.
    """
    idCategoryIngredient = AutoField(primary_key=True)
    nameCategoryIngredient = CharField(max_length=255)
    descriptionCategoryIngredient = CharField(max_length=255)
    
    class Meta:
        """Defines the metadata for the CategoryIngredient model."""
        database = database
        db_table = "categoryIngredients"    
                
class Ingredient(Model):
    """ 
    Represents an ingredient in the database.
    
    Attributes:
        idIngredient (int): The unique identifier of the ingredient.
        nameIngredient (str): The name of the ingredient.
        amountIngredient (str): The amount of the ingredient.
        unitIngredient (str): The unit of the ingredient.
        dateExpirationIngredient (date): The date expiration of the ingredient.
        recipeId (int): The recipe of the ingredient.
        categoryIdIngredient (int): The category of the ingredient.
    """
    idIngredient = AutoField(primary_key=True)
    nameIngredient = CharField(max_length=255)
    amountIngredient = CharField(max_length=255)
    unitIngredient = CharField(max_length=255)
    dateExpirationIngredient = DateField()
    recipeId = ForeignKeyField(Recipe, backref='ingredients')
    categoryIdIngredient = ForeignKeyField(CategoryIngredient, backref='ingredients')

    class Meta:
        """Defines the metadata for the Ingredient model."""
        database = database
        db_table = "ingredients"
                
class ShoppingList_Ingredient(Model):
    """
    Represents a table bridge between the shopping list and the ingredient in the database.
    
    Attributes:
        shoppingListId (int): The unique identifier of the shopping list.
        ingredientId (int): The unique identifier of the ingredient.
    """
    shoppingListId = ForeignKeyField(ShoppingList, backref='shopping_list_ingredients')
    ingredientId = ForeignKeyField(Ingredient, backref='shopping_list_ingredients')

    class Meta:
        """Defines the metadata for the ShoppingList_Ingredient model."""
        database = database
        db_table = "shopping_list_ingredients"
