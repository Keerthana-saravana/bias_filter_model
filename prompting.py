
import os

os.environ["USE_TF"] = "0"
os.environ["HF_HUB_DOWNLOAD_TIMEOUT"] = "60"

from transformers import pipeline
print("Loading the language model... Please wait.")

llm = pipeline(
    "text-generation",
    model="distilgpt2",
    framework="pt"
)

print("\nPROMPTING TECHNIQUES WITH PUBLIC LLM")
print("=" * 45)

topic = input("Enter a topic: ")

prompts = {
    "Zero-Shot Prompting":
        f"Explain {topic} in simple words:",

    "Few-Shot Prompting":
        f"AI means intelligent machines. ML means learning from data. {topic} means",

    "Role-Based Prompting":
        f"Teacher: Explain {topic} to a beginner. Answer:",

    "Step-by-Step Prompting":
        f"Steps to understand {topic}: 1."
}

for name, prompt in prompts.items():

    result = llm(
        prompt,
        max_new_tokens=50,
        num_return_sequences=1,
        do_sample=False,
        pad_token_id=llm.tokenizer.eos_token_id
    )

    response = result[0]["generated_text"][len(prompt):].strip()

    print("\n" + "=" * 45)
    print("TECHNIQUE:", name)
    print("PROMPT:", prompt)
    print("RESPONSE:", response or "No response generated")

print("\nExperiment completed!")
