from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Negotiation:
    def __init__(self, products, weights, reservation_values, urgency_factors, concession_speed, rounds):
        self.products = products
        self.weights = weights
        self.reservation_values = reservation_values
        self.urgency_factors = urgency_factors
        self.concession_speed = concession_speed
        self.rounds = rounds
        self.last_buyer_offer = None
        self.round_num = 0
        self.messages = []

        # Load the conversational model
        self.model_name = "microsoft/DialoGPT-medium"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def Kt(self):
        index = min(self.round_num, len(self.concession_speed) - 1)
        return (self.round_num / self.rounds) ** self.concession_speed[index]

    def seller_proposal(self):
        proposal = {}
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            if self.last_buyer_offer is not None and self.last_buyer_offer[i] > 0:
                proposal[i] = max(max_val - self.Kt() * (max_val - min_val), self.last_buyer_offer[i] + 10)
            else:
                proposal[i] = max_val - self.Kt() * (max_val - min_val)
        return proposal

    def compute_score(self, offer):
        score = 0
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            if offer[i] < min_val or offer[i] > max_val:
                score += 0
            else:
                score += (offer[i] - min_val) / (max_val - min_val) * self.weights[i]
        return score

    def negotiate(self, buyer_offer):
        self.round_num += 1
        seller_offer = self.seller_proposal()
        self.last_buyer_offer = buyer_offer

        buyer_score = self.compute_score(buyer_offer)
        seller_score = self.compute_score(seller_offer)

        self.messages.append(f"Round {self.round_num}:")
        self.messages.append(f"  Seller offer: {seller_offer}")
        self.messages.append(f"  Your offer: {buyer_offer}, Score: {buyer_score}")
        self.messages.append(f"  Seller offer: {seller_offer}, Score: {seller_score}")

        if buyer_score > 0.8 and seller_score > 0.8:
            self.messages.append("Negotiation successful!")
            return True

        if buyer_score < seller_score:
            self.messages.append("You might want to increase your offer.")
        elif buyer_score > seller_score:
            self.messages.append("Your offer is good, consider keeping it or slightly increasing it.")

        return False

    def chat_response(self, user_input):
        input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')
        with torch.no_grad():
            output = self.model.generate(input_ids, max_length=150, num_return_sequences=1)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response
