from tortoise import Model, fields
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    email = fields.CharField(max_length=65, null=False, unique=True)
    password = fields.CharField(max_length=100, null=False, unique=True)
    is_verified = fields.BooleanField(default=False)
    join_date = fields.DatetimeField(default=datetime.utcnow)


class Business(Model):
    id = fields.IntField(pk=True, index=True)
    business_name = fields.CharField(max_length=20, null=False, unique=True)
    city = fields.CharField(max_length=50, null=False, default="Unspecified")
    region = fields.CharField(max_length=50, null=False, default="Unspecified")
    business_description = fields.TextField(null=True)
    logo = fields.CharField(max_length=150, null=False,
                            default="tortoise.jpeg")
    owner = fields.ForeignKeyField("models.User", related_name="business")


class Product(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=20, null=False, index=True)
    category = fields.CharField(max_length=20, index=True)
    original_price = fields.DecimalField(max_digits=10, decimal_places=3)
    new_price = fields.DecimalField(max_digits=10, decimal_places=3)
    percentage_discount = fields.IntField()
    offer_expiration = fields.DateField(default=datetime.utcnow)
    product_image = fields.CharField(
        max_length=150, null=False, default="p_image.jpeg")
    business = fields.ForeignKeyField(
        "models.Business", related_name="products")


user_pydentic = pydantic_model_creator(
    User, name='User', exclude=("is_verified", ))
user_pydenticIn = pydantic_model_creator(
    User, name='UserIn', exclude_readonly=True, exclude=("is_verified", "join_date"))
user_pydenticOut = pydantic_model_creator(
    User, name='UserOut', exclude=("password", ))

Business_pydentic = pydantic_model_creator(Business, name='Business')
Business_pydenticIn = pydantic_model_creator(
    Business, name='BusinessIn', exclude_readonly=True)

Product_pydentic = pydantic_model_creator(Product, name='Product')
Product_pydenticIn = pydantic_model_creator(
    Product, name='ProductIn', exclude=("percentage_discount", "id"))
