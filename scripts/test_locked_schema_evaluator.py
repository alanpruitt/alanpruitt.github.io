import ollama

MODEL_NAME = "gemma4:e2b"

# Strict JSON Schema enforcing your grading scale and categories
GRADING_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {
            "type": "integer",
            "enum": [10, 7, 0],
            "description": "10 = Exemplary/Complete, 7 = Competent/Solid Attempt, 0 = Recalibrate/Minimal Attempt"
        },
        "performance_tier": {
            "type": "string",
            "enum": ["Exemplary", "Competent", "Recalibrate"]
        },
        "pattern_status": {"type": "string", "enum": ["PASS", "FAIL"]},
        "rule_status": {"type": "string", "enum": ["PASS", "FAIL"]},
        "solve_status": {"type": "string", "enum": ["PASS", "FAIL"]},
        "feedback": {
            "type": "string",
            "description": "Constructive formative critique. Must be signed off at the end with 'Best, Coach Alan'."
        },
        "justification": {"type": "string"}
    },
    "required": [
        "score", 
        "performance_tier", 
        "pattern_status", 
        "rule_status", 
        "solve_status", 
        "feedback", 
        "justification"
    ]
}

SYSTEM_PROMPT = """### SYSTEM ROLE ###
You are Coach Alan, an expert AI Grading Assistant for exercise science course fleets. Evaluate the student submission using the Clinical Framing Protocol (Pattern, Rule, Solve). 

Assign scores strictly based on the 10/7/0 scale:
- 10 (Exemplary): Complete, correct, well-reasoned solution fulfilling all rubric criteria.
- 7 (Competent): Solid attempt with minor gaps or partial rule application.
- 0 (Recalibrate): Minimal attempt, missing core patterns or failing to apply rules correctly.

CRITICAL INSTRUCTION FOR FEEDBACK: Every formative feedback string generated in the 'feedback' key must conclude with the exact sign-off: 'Best, Coach Alan'.

Output the result strictly matching the requested JSON schema."""

def evaluate_with_locked_schema(prompt, submission, rubric):
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
        format=GRADING_SCHEMA,  # Enforces structural compliance and enum locking at the sampler level
        options={
            "temperature": 0.1,  
            "num_predict": 1024   # Headroom for reasoning trace + strict JSON generation
        }
    )
    
    return response.message.content

if __name__ == "__main__":
    test_prompt = "Design a 3-step activity modification using PAGA guidelines."
    test_rubric = "Must identify sedentary pattern and cite federal rules."
    test_submission = "The client sits all day. We will implement 150 minutes of weekly moderate walking based on federal guidelines."
    
    print(f"Running locked-schema evaluation on M1 via {MODEL_NAME}...")
    result = evaluate_with_locked_schema(test_prompt, test_submission, test_rubric)
    print(result)
