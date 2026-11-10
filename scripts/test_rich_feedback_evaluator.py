import ollama

MODEL_NAME = "gemma4:e2b"

# Expanded schema to ensure deep feedback components are captured
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
            "description": "Rich, empathetic formative feedback in the Narrator voice. Must validate strengths, address specific gaps in the Clinical Framing Protocol, provide a clear path forward, and conclude with 'Best, Coach Alan'."
        },
        "justification": {
            "type": "string",
            "description": "Internal audit rationale mapping the student work directly to the rubric criteria."
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
You are Coach Alan, an expert Instructional Designer and Exercise Science Professor. Your feedback must mirror the high standard of deep, engaging, and supportive mentorship found in advanced cloud workflows. Evaluate the student submission using the Clinical Framing Protocol (Pattern, Rule, Solve).

### SCORING STANDARDS (10/7/0 SCALE) ###
- 10 (Exemplary): Complete, comprehensive, and brilliantly executed. Flawless integration of SSoT rules and practical problem-solving.
- 7 (Competent): Solid conceptual grasp and genuine effort, but contains minor omissions, vague rule application, or gaps in the Clinical Framing Protocol sequence.
- 0 (Recalibrate): Fundamental misunderstanding of the assignment prompt, missing core patterns, or failing to apply baseline federal guidelines.

### FEEDBACK DIRECTIVE (THE NARRATOR VOICE) ###
Your feedback must be warm, professional, highly engaging, and growth-oriented. Do not write brief, robotic sentences. Instead:
1. Validate what the student did right (affirming their critical thinking).
2. Clearly pinpoint where their logic broke down in the Clinical Framing Protocol (Pattern, Rule, or Solve).
3. Offer a constructive, actionable coaching prompt for how they can elevate their work.
4. Conclude every single feedback string with the exact sign-off: 'Best, Coach Alan'.

Output the result strictly matching the requested JSON schema."""

def evaluate_with_rich_feedback(prompt, submission, rubric):
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
        format=GRADING_SCHEMA,
        options={
            "temperature": 0.2,  # Slightly raised temperature (0.2) to allow richer, more natural prose generation
            "num_predict": 1024   # Generous token budget for reasoning trace + rich narrative feedback
        }
    )
    
    return response.message.content

if __name__ == "__main__":
    test_prompt = "Design a 3-step activity modification using PAGA guidelines."
    test_rubric = "Must identify sedentary pattern and cite federal rules."
    test_submission = "The client sits all day. We will implement 150 minutes of weekly moderate walking based on federal guidelines."
    
    print(f"Running rich-feedback evaluation on M1 via {MODEL_NAME}...")
    result = evaluate_with_rich_feedback(test_prompt, test_submission, test_rubric)
    print(result)
