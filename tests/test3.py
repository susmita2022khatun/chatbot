import random

class Negotiation:
    def __init__(self):
        # Define the negotiation parameters
        self.products = ["Laptop", "Warranty"]
        self.weights = [0.7, 0.3]  # Weights for Laptop and Warranty
        self.reservation_values = {
            0: (500, 1000),  # Reservation values for Laptop
            1: (50, 200)     # Reservation values for Warranty
        }
        self.rounds = 10
        self.concession_speed = [0.9] * self.rounds  # Static for simplicity

    def Kt(self, round_num):
        return (round_num / self.rounds) ** self.concession_speed[round_num - 1]

    def seller_proposal(self, round_num):
        proposal = {}
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            proposal[i] = min_val + self.Kt(round_num) * (max_val - min_val)
        return proposal

    def score(self, proposal, weights):
        total_score = 0
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            total_score += (proposal[i] - min_val) / (max_val - min_val) * weights[i]
        return total_score

    def negotiate(self):
        for round_num in range(1, self.rounds + 1):
            print(f"Round {round_num}:")
            # Seller responds with their offer
            seller_offer = {}
            for i in range(len(self.products)):
                seller_offer[i] = float(input(f"Enter your offer for {self.products[i]}: "))
            print(f"Your offer: {seller_offer}")

            # Buyer proposes an offer
            buyer_offer = self.seller_proposal(round_num)
            print(f"Buyer offer: {buyer_offer}")

            # Calculate scores
            buyer_score = self.score(buyer_offer, self.weights)
            seller_score = self.score(seller_offer, self.weights)

            print(f"Buyer score: {buyer_score}, Seller score: {seller_score}")

            # Check if the seller accepts the offer
            if seller_score >= buyer_score:
                print("Negotiation successful. Buyer accepts the offer.")
                break
            else:
                print("Buyer will adjust the offer for the next round.")
            
            continue_negotiation = input("Do you want to continue negotiation? (yes/no): ")
            if continue_negotiation.lower() != 'yes':
                print("Negotiation terminated by seller.")
                break


def main():
    negotiation = Negotiation()
    negotiation.negotiate()


if __name__ == "__main__":
    main()
