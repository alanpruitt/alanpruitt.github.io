import ollama

# Configured for local M1 execution using the E2B edge model
MODEL_NAME = "gemma4:e2b"

SYSTEM_PROMPT = """### SYSTEM ROLE ###
You are an AI Grading Assistant. Evaluate the student submission against the rubric and return a valid JSON payload matching the required schema. Do not include extra commentary."""

def evaluate_with_e2b(prompt, submission, rubric):
    user_payload = f"""
    PROMPT: {prompt}
    RUBRIC: {rubric}
    SUBMISSION: {submission}
    """
    
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_payload}
        ],
        format="json", # Enforces grammar-constrained JSON decoding
        options={
            "temperature": 0.1,  
            "num_predict": 1024   # Expanded headroom for reasoning trace + output
        }
    )
    
    return response.message.content

if __name__ == "__main__":
    test_prompt = "Design a 3-step activity modification using PAGA guidelines."
    test_rubric = "Must identify sedentary pattern and cite federal rules."
    test_submission = "The client sits all day. We will implement 150 minutes of weekly moderate walking based on federal guidelines."
    
    print(f"Running evaluation on M1 via {MODEL_NAME}...")
    result = evaluate_with_e2b(test_prompt, test_submission, test_rubric)
    print(result)
