from fastapi import FastAPI
from pydantic import BaseModel
from producer import publish_to_microservice_a  # Importing the function from the producer_b module

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post('/send_message_to_a')  # Define endpoint for sending messages to Microservice A
async def send_message_to_a_endpoint(message: Message):
    publish_to_microservice_a(message.message)  # Call the function to publish message to Microservice A
    return {"status": "Message sent successfully to Microservice A"}
