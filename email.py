from fastapi import (BackgroundTasks, UploadFile, Form,
                     File, Depends, HTTPException, status)
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import dotenv_values
from pydantic import BaseModel, EmailStr
from .models import User
from typing import List
import jwt


config_credentials = dotenv_values(".env")

conf = ConnectionConfig(
    MAIL_USERNAME=config_credentials["EMAIL"],
    MAIL_PASSWORD=config_credentials["PASS"],
    MAIL_FROM=config_credentials["EMAIL"],
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Desired Name",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True
)


class EmailSchema(BaseModel):
    email: List[EmailStr]


async def send_mail(email: EmailSchema, instance: User):

    token_data = {
        "username": instance.username,
        "id": instance.id

    }

    token = jwt.encode(token_data, config_credentials["SECRET"])

    template = f"""
        <!DOCTYPE html>
        <html>
            <head>

            </head>
            <body>
            <div style = "display: flex; align-items: center; justify-content:
            center; flex-direction: column">
            <h3>Account Verification </h3> <br>
            <p>Thanks for choosing EasyShopas, please click on the button below
            to verify your account </p>
            <a style="marign-top: 1rem; padding: 1rem; border-radius: 0.5rem; font-size: 1rem; text-decoration: none; background; #0275d8; color: white;" href-"http://localhost:8000/verification/?token={token}">
            Verify your email 
            </a>
                <p>Please kindly ianore this email if vou did not register for EasyShopas and nothing will happend. Thanks</ p>
            </body>
        </html>

    """

    message = MessageSchema(
        subject="Account verification",
        recipients=email
    )
