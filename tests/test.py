import random

class Negotiation:
    def __init__(self, products, weights, reservation_values, urgency_factors, concession_speed, rounds):
        self.products = products
        self.weights = weights
        self.reservation_values = reservation_values
        self.urgency_factors = urgency_factors
        self.concession_speed = concession_speed
        self.rounds = rounds

    def Kt(self, round_num):
        # Ensure the index is valid
        index = min(round_num - 1, len(self.concession_speed) - 1)
        return (round_num / self.rounds) ** self.concession_speed[index]

    def buyer_proposal(self, round_num):
        proposal = {}
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            proposal[i] = min_val + self.Kt(round_num) * (max_val - min_val)
        return proposal

    def seller_proposal(self, round_num):
        proposal = {}
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            proposal[i] = max_val - self.Kt(round_num) * (max_val - min_val)
        return proposal

    def compute_score(self, offer):
        score = 0
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            if offer[i] < min_val:
                score += 0
            elif offer[i] > max_val:
                score += 0
            else:
                score += (offer[i] - min_val) / (max_val - min_val) * self.weights[i]
        return score

    def negotiate(self):
        for round_num in range(1, self.rounds + 1):
            print(f"\nRound {round_num}:")
            buyer_offer = self.buyer_proposal(round_num)
            seller_offer = self.seller_proposal(round_num)

            buyer_score = self.compute_score(buyer_offer)
            seller_score = self.compute_score(seller_offer)

            print(f"  Buyer offer: {buyer_offer}, Score: {buyer_score}")
            print(f"  Seller offer: {seller_offer}, Score: {seller_score}")

            if buyer_score > 0.8 and seller_score > 0.8:
                print("Negotiation successful!")
                return
            
            user_input = input("Do you want to continue negotiation? (yes/no): ")
            if user_input.lower() != 'yes':
                print("Negotiation terminated by user.")
                return
        
        print("Negotiation failed.")

def main():
    # Example parameters
    products = ["Laptop", "Warranty"]
    weights = [0.7, 0.3]  # Weights for each product
    reservation_values = [(500, 1000), (50, 200)]  # (min, max) for Laptop and Warranty
    urgency_factors = [0.1, 0.1]  # Urgency factors for both
    concession_speed = [0.5, 0.5]  # Concession speed for both
    rounds = 10  # Total rounds of negotiation

    negotiation = Negotiation(products, weights, reservation_values, urgency_factors, concession_speed, rounds)
    negotiation.negotiate()

if __name__ == "__main__":
    main()
