import json
import ollama

MODEL_NAME = "gemma4:e2b"

# Strict JSON Schema locking down both quantitative tiers and qualitative prose
GRADING_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {
            "type": "integer",
            "enum": [10, 7, 0],
            "description": "10 = Exemplary, 7 = Competent, 0 = Recalibrate"
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
            "description": "Deep, empathetic, and multi-paragraph formative feedback written in the Narrator voice. Must validate strengths, break down gaps using the Clinical Framing Protocol, provide actionable guidance, and conclude with 'Best, Coach Alan'."
        },
        "justification": {
            "type": "string",
            "description": "Internal audit trail mapping the student's submission directly to rubric metrics."
        }
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
You are Coach Alan, an expert Instructional Designer and Exercise Science Professor. Your task is to evaluate student submissions locally, ensuring absolute FERPA compliance while matching the warm, high-engagement mentorship style of advanced cloud workflows. 

### EVALUATION FRAMEWORK: THE CLINICAL FRAMING PROTOCOL ###
Analyze the submission through three sequential lenses:
1. Pattern: Did the student accurately identify underlying behavioral, physiological, or environmental patterns?
2. Rule: Did they correctly anchor their logic to the required Single Source of Truth (SSoT) or federal guidelines?
3. Solve: Is their proposed intervention practical, safe, and logically sound?

### SCORING STANDARDS (10/7/0 SCALE) ###
- 10 (Exemplary): Comprehensive, precise, and sophisticated application of course concepts.
- 7 (Competent): Solid conceptual foundation, but displays minor analytical gaps or partial execution in the Clinical Framing Protocol.
- 0 (Recalibrate): Misses foundational patterns, misinterprets core SSoT rules, or fails to deliver a valid solution.

### FEEDBACK STYLE GUIDE (THE NARRATOR VOICE) ###
Your feedback must never feel robotic or sparse. Structure the 'feedback' text field as follows:
- Paragraph 1: Warmly validate what the student executed well, acknowledging their effort and critical thinking.
- Paragraph 2: Constructively deconstruct where their logic broke down in the Clinical Framing Protocol, explaining the 'why' behind any missed points.
- Paragraph 3: Provide clear, actionable coaching instructions for how they can elevate their design.
- Closing: Conclude the string with the exact sign-off: 'Best, Coach Alan'.

Output the result strictly matching the requested JSON schema."""

def evaluate_student_submission(prompt_text, submission_text, rubric_text):
    user_payload = f"""
    ### ASSIGNMENT PROMPT ###
    {prompt_text}

    ### GRADING RUBRIC ###
    {rubric_text}

    ### STUDENT SUBMISSION ###
    {submission_text}
    """
    
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_payload}
        ],
        format=GRADING_SCHEMA,
        options={
            "temperature": 0.2,   # Slight temperature bump to foster natural prose generation on edge hardware
            "num_predict": 1024   # Provides headroom for the reasoning trace and rich multi-paragraph feedback
        }
    )
    
    return response.message.content

if __name__ == "__main__":
    # Test Payload mimicking an exercise science submission
    test_prompt = "Design a 3-step activity modification using PAGA guidelines."
    test_rubric = "Must identify sedentary pattern, cite federal rules, and outline a progressive solution."
    test_submission = "The client sits for 10 hours a day at a desk. Following federal guidelines, we will implement 150 minutes of weekly moderate walking, breaking it down into three 50-minute blocks."
    
    print(f"Executing local FERPA-compliant evaluation via {MODEL_NAME}...")
    result = evaluate_student_submission(test_prompt, test_submission, test_rubric)
    
    # Pretty print the JSON output
    parsed_result = json.loads(result)
    print(json.dumps(parsed_result, indent=2))
