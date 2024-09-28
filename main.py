from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from negotiation import Negotiation

app = FastAPI()

# Mount the static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Initialize the negotiation instance
negotiation = Negotiation(
    products=["Laptop", "Warranty"],
    weights=[0.7, 0.3],
    reservation_values=[(500, 1000), (50, 200)],
    urgency_factors=[0.1, 0.1],
    concession_speed=[0.5, 0.5],
    rounds=10
)

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "messages": negotiation.messages})

@app.post("/negotiate")
async def post_offer(request: Request, offer_0: float = Form(...), offer_1: float = Form(...)):
    buyer_offer = [offer_0, offer_1]
    negotiation_completed = negotiation.negotiate(buyer_offer)

    # Get model's response
    user_input = f"User's offer for Laptop: {offer_0}, Warranty: {offer_1}"
    model_response = negotiation.chat_response(user_input)
    negotiation.messages.append(f"AI: {model_response}")

    if negotiation_completed:
        return templates.TemplateResponse("index.html", {"request": request, "messages": negotiation.messages, "completed": True})

    return templates.TemplateResponse("index.html", {"request": request, "messages": negotiation.messages})
