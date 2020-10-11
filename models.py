from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    calories = Column(Float)
    saturated_fat = Column(Float)
    trans_fat = Column(Float)
    cholesterol = Column(Float)
    sodium = Column(Float)
    carbohydrate = Column(Float)
    sugar = Column(Float)
    protein = Column(Float)
    ingredient_type_id = Column(Integer, ForeignKey('ingredient_type.id'))
    ingredient_type = relationship("IngredientType", back_populates="ingredients")

class IngredientType(Base):
    __tablename__ = "ingredient_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    #ingredients = relationship("Ingredient", backref="type", lazy='dynamic')
    ingredients = relationship("Ingredient", back_populates="ingredient_type")