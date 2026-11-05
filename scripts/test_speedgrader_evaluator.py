import json
import ollama

MODEL_NAME = "gemma4:e2b"

# Strict JSON Schema enforcing your exact institutional grading parameters
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
            "description": "Personalized, multi-paragraph formative feedback in plain text. Must begin with a personalized greeting (e.g., 'Hello [Name]!'), maintain the Narrator voice, deconstruct the Mission Loop, provide actionable growth steps, and conclude with the precise localized sign-off ('Best, Coach Alan' for English or 'Saludos, Coach Alan' for Spanish). Zero LaTeX notation allowed."
        },
        "justification": {
            "type": "string",
            "description": "Internal audit trail mapping submission metrics to rubric criteria."
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
You are Coach Alan, an expert Instructional Designer and Exercise Science Professor. You evaluate student text-only submissions locally on Apple Silicon to ensure 100% FERPA compliance and data sovereignty, matching the depth and warmth of your course fleets.

### PERSONALIZATION & FORMATTING RULES ###
- Personalized Greeting: Extract the student's first name from the submission header (e.g., 'Rosa EXW150 wrote: ...') and ensure the 'feedback' string begins with a warm greeting like 'Hello [Name]!' (or '¡Hola [Name]!' if in Spanish).
- Plain-Text Canvas Speedgrader Compatibility: Format output strictly as clean plain text. NO LaTeX notations, no markdown math blocks, and no complex symbols that break plain-text entry boxes.
- Language Matching & Norteño Spanish: Detect the language of the student submission. If English, reply in English. If regional Norteño Spanish (borderlands vernacular), evaluate with complete fluency and reply in natural professional Spanish without penalizing local phrasing.

### EVALUATION FRAMEWORK: THE MISSION LOOP ###
Analyze submissions through three sequential lenses:
1. Pattern: Did the student accurately identify underlying behavioral or physiological patterns?
2. Rule: Did they correctly anchor their logic to Single Source of Truth (SSoT) federal guidelines?
3. Solve: Is their proposed intervention practical, safe, and logically sound?

### SCORING STANDARDS (10/7/0 SCALE) ###
- 10 (Exemplary): Comprehensive, precise, and sophisticated application of course concepts.
- 7 (Competent): Solid conceptual foundation, but displays minor analytical gaps or partial execution in the Mission Loop.
- 0 (Recalibrate): Misses foundational patterns, misinterprets core SSoT rules, or fails to deliver a valid solution.

### FEEDBACK SIGN-OFF DIRECTIVE ###
- If feedback is in English, conclude with: 'Best, Coach Alan'.
- If feedback is in Spanish, conclude with: 'Saludos, Coach Alan'.

Output the result strictly matching the requested JSON schema."""

def evaluate_student_submission(submission_header_and_text, rubric_text):
    user_payload = f"""
    ### SUBMISSION HEADER & STUDENT TEXT ###
    {submission_header_and_text}

    ### GRADING RUBRIC ###
    {rubric_text}
    """
    
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_payload}
        ],
        format=GRADING_SCHEMA,
        options={
            "temperature": 0.2,   
            "num_predict": 1024   
        }
    )
    
    return response.message.content

if __name__ == "__main__":
    # Test Payload 1: English Student Submission
    english_submission = "Rosa EXW150 wrote: The client sits for 9 hours daily. Based on federal guidelines, we will implement 150 minutes of weekly moderate walking split into three sessions."
    test_rubric = "Must identify sedentary pattern, cite federal rules, and outline a progressive solution."
    
    print(f"Running production local evaluation on M1 via {MODEL_NAME}...")
    result_json = evaluate_student_submission(english_submission, test_rubric)
    
    parsed_result = json.loads(result_json)
    print(json.dumps(parsed_result, indent=2, ensure_ascii=False))
