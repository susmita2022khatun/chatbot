class Negotiation:
    def __init__(self, products, weights, reservation_values, urgency_factors, concession_speed, rounds):
        self.products = products
        self.weights = weights
        self.reservation_values = reservation_values
        self.urgency_factors = urgency_factors
        self.concession_speed = concession_speed
        self.rounds = rounds
        self.last_buyer_offer = None  

    def Kt(self, round_num):
        index = min(round_num - 1, len(self.concession_speed) - 1)
        return (round_num / self.rounds) ** self.concession_speed[index]

    def seller_proposal(self, round_num):
        proposal = {}
        for i in range(len(self.products)):
            min_val, max_val = self.reservation_values[i]
            if self.last_buyer_offer is not None and self.last_buyer_offer[i] > 0:
                proposal[i] = max(max_val - self.Kt(round_num) * (max_val - min_val), self.last_buyer_offer[i] + 10)
            else:
                proposal[i] = max_val - self.Kt(round_num) * (max_val - min_val)
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

    def negotiate(self):
        for round_num in range(1, self.rounds + 1):
            print(f"\nRound {round_num}:")
            
            seller_offer = self.seller_proposal(round_num)
            print(f"  Seller offer: {seller_offer}")

            buyer_offer = {}
            for i in range(len(self.products)):
                buyer_price = float(input(f"Enter your offer for {self.products[i]}: "))
                buyer_offer[i] = buyer_price
            
            self.last_buyer_offer = buyer_offer

            buyer_score = self.compute_score(buyer_offer)
            seller_score = self.compute_score(seller_offer)

            print(f"  Your offer: {buyer_offer}, Score: {buyer_score}")
            print(f"  Seller offer: {seller_offer}, Score: {seller_score}")

            if buyer_score > 0.8 and seller_score > 0.8:
                print("Negotiation successful!")
                return
            
            if buyer_score < seller_score:
                print("You might want to increase your offer.")
            elif buyer_score > seller_score:
                print("Your offer is good, consider keeping it or slightly increasing it.")

            user_input = input("Do you want to continue negotiation? (yes/no): ")
            if user_input.lower() != 'yes':
                print("Negotiation terminated by user.")
                return
        
        print("Negotiation failed.")

def main():
    products = ["Laptop", "Warranty"]
    weights = [0.7, 0.3] 
    reservation_values = [(500, 1000), (50, 200)] 
    urgency_factors = [0.1, 0.1]  
    concession_speed = [0.5, 0.5] 
    rounds = 10  

    negotiation = Negotiation(products, weights, reservation_values, urgency_factors, concession_speed, rounds)
    negotiation.negotiate()

if __name__ == "__main__":
    main()
