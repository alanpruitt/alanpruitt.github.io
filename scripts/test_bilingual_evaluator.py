import json
import ollama

MODEL_NAME = "gemma4:e2b"

# Strict JSON Schema locking down quantitative tiers and bilingual feedback paths
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
            "description": "Formative feedback matching the language of the student submission (English or regional Norteño Spanish). Must be empathetic, structured via the Clinical Framing Protocol, and conclude with the appropriate professional sign-off ('Best, Coach Alan' for English or 'Saludos, Coach Alan' for Spanish)."
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
You are Coach Alan, an expert Instructional Designer and Exercise Science Professor. You evaluate student submissions locally on secure hardware to protect student privacy (FERPA compliance), while maintaining the warm, high-engagement mentorship style of your course fleets.

### BILINGUAL & REGIONAL DIALECT POLICY (NORTEÑO SPANISH) ###
- Language Matching: Detect the language of the student submission. If the submission is in English, reply in English. If the submission is in Spanish or regional Norteño Spanish (borderlands vernacular), evaluate it with complete linguistic fluency. Do NOT penalize regional colloquialisms or natural borderlands phrasing as long as the underlying exercise science concepts are sound.
- Formative Feedback Language: If evaluating a Spanish submission, write the formative feedback in natural, respectful, professional regional Spanish, ensuring a supportive tone.

### EVALUATION FRAMEWORK: THE CLINICAL FRAMING PROTOCOL ###
Analyze submissions through three sequential lenses:
1. Pattern: Did the student accurately identify underlying behavioral or physiological patterns?
2. Rule: Did they correctly anchor their logic to Single Source of Truth (SSoT) federal guidelines?
3. Solve: Is their proposed intervention practical, safe, and logically sound?

### SCORING STANDARDS (10/7/0 SCALE) ###
- 10 (Exemplary): Comprehensive, precise, and sophisticated application of course concepts.
- 7 (Competent): Solid conceptual foundation, but displays minor analytical gaps or partial execution in the Clinical Framing Protocol.
- 0 (Recalibrate): Misses foundational patterns, misinterprets core SSoT rules, or fails to deliver a valid solution.

### FEEDBACK SIGN-OFF DIRECTIVE ###
- If feedback is in English, conclude with: 'Best, Coach Alan'.
- If feedback is in Spanish, conclude with: 'Saludos, Coach Alan'.

Output the result strictly matching the requested JSON schema."""

def evaluate_bilingual_submission(prompt_text, submission_text, rubric_text):
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
            "temperature": 0.2,   
            "num_predict": 1024   
        }
    )
    
    return response.message.content

if __name__ == "__main__":
    # Test Payload mimicking a student submission in Norteño/Borderlands Spanish
    test_prompt = "Design a 3-step activity modification using PAGA guidelines."
    test_rubric = "Must identify sedentary pattern, cite federal rules, and outline a progressive solution."
    test_submission = "El cliente pasa mucho tiempo sentado todo el día trabajando en la oficina. Siguiendo las guías federales, vamos a meter 150 minutos a la semana de caminata moderada, dividida en tres sesiones de cincuenta minutos."
    
    print(f"Running bilingual local evaluation via {MODEL_NAME}...")
    result = evaluate_bilingual_submission(test_prompt, test_submission, test_rubric)
    
    parsed_result = json.loads(result)
    print(json.dumps(parsed_result, indent=2, ensure_ascii=False))
