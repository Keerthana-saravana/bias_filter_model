
print("PROMPTING TECHNIQUES WITH PUBLIC LLM")
print("=" * 50)

topic = input("Enter a topic: ")

zero_shot = f"Explain {topic} in simple words."

few_shot = f"""
Example 1:
Topic: Artificial Intelligence
Answer: AI enables machines to perform intelligent tasks.

Example 2:
Topic: Machine Learning
Answer: ML helps computers learn from data.

Topic: {topic}
Answer:
"""

role_based = f"Act as a teacher and explain {topic} to a beginner."
step_by_step = f"Explain {topic} in three simple steps."

prompts = {
    "Zero-Shot Prompting": zero_shot,
    "Few-Shot Prompting": few_shot,
    "Role-Based Prompting": role_based,
    "Step-by-Step Prompting": step_by_step
}

for technique, prompt in prompts.items():
    print("\n" + "=" * 50)
    print("TECHNIQUE:", technique)
    print("\nPROMPT:")
    print(prompt)

    if technique == "Zero-Shot Prompting":
        response = f"{topic} is a concept that can be explained using simple instructions."

    elif technique == "Few-Shot Prompting":
        response = f"Following the examples, {topic} can be explained in a similar format."

    elif technique == "Role-Based Prompting":
        response = f"As a teacher, I would introduce {topic} using simple language and examples."

    else:
        response = f"Step 1: Understand {topic}.\nStep 2: Learn its main concepts.\nStep 3: Practise with examples."

    print("\nRESPONSE:")
    print(response)

print("\nExperiment completed!")
