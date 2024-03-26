from fastapi import FastAPI
from pydantic import BaseModel
from producer import send_message_to_b, send_message_to_c

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post('/send_message_to_b')
async def send_message_to_b_endpoint(message: Message):
    send_message_to_b(message.message)
    return {"status": "Message sent successfully to Microservice B"}

@app.post('/send_message_to_c')
async def send_message_to_c_endpoint(message: Message):
    send_message_to_c(message.message)
    return {"status": "Message sent successfully to Microservice C"}
