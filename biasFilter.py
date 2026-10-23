
def check_text(text):
    toxic_words = ["hate", "stupid", "idiot", "kill"]
    biased_words = ["all women are", "all men are", "all people from"]

    text = text.lower()

    toxicity = any(word in text for word in toxic_words)
    bias = any(word in text for word in biased_words)

    if toxicity and bias:
        print("Warning: Toxic and Biased Text")
    elif toxicity:
        print("Warning: Toxic Text Detected")
    elif bias:
        print("Warning: Biased Text Detected")
    else:
        print("Text is Safe")

text = input("Enter AI-generated text: ")
check_text(text)