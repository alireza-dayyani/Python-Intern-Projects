from transformers import AutoModelForCausalLM, AutoTokenizer
import keyboard

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chatbot_response(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    bot_response = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(bot_response[0], skip_special_tokens=True)

def check_for_esc():
    if keyboard.is_pressed("esc"):
        return True
    return False

print("Chatbot is now active. Press 'Esc' key to exit.")
while True:
    user_input = input("You: ")
    if check_for_esc():
        print("Exiting the chatbot. Goodbye!")
        break
    
    response = chatbot_response(user_input)
    print(f"ChatBot: {response}")