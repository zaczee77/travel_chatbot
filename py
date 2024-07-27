from transformers import GPT2LMHeadModel, GPT2Tokenizer # type: ignore
import torch # type: ignore

class TravelChatbot:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.model.eval()

    def generate_response(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(inputs, max_length=150, num_return_sequences=1)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def create_itinerary(self, days, budget, preferences):
        # Sample logic for creating an itinerary based on user input
        destinations = ["Paris", "New York", "Tokyo", "Sydney"]
        activities = ["Sightseeing", "Shopping", "Beach", "Hiking"]

        itinerary = {
            "Destination": destinations[0],
            "Duration (days)": days,
            "Places to Visit": activities[:2],
            "Accommodation": "Hotel",
            "Food": "Local Cuisine",
            "Budget": budget
        }
        return itinerary
