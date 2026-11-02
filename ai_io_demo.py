import json

# This script simulates a basic AI tool's input validation and output generation.
# It demonstrates what kind of data an AI tool might accept and what it should return.

def process_ai_request(request_data):
    """
    Simulates an AI tool processing a request.

    Args:
        request_data (dict): The input data for the AI tool.

    Returns:
        dict: The processed output from the AI tool, or an error message.
    """
    # --- Input Validation: What the AI tool ACCEPTS ---
    accepted_formats = ['text', 'json']
    required_keys = ['prompt', 'format']

    if not isinstance(request_data, dict):
        return {"error": "Invalid input: Request must be a JSON object."}

    for key in required_keys:
        if key not in request_data:
            return {"error": f"Invalid input: Missing required key '{key}'."}

    if request_data['format'] not in accepted_formats:
        return {"error": f"Invalid input: Unsupported format '{request_data['format']}'. Accepted formats are: {', '.join(accepted_formats)}."}

    if not isinstance(request_data['prompt'], str) or not request_data['prompt'].strip():
        return {"error": "Invalid input: 'prompt' must be a non-empty string."}

    # --- AI Processing Simulation ---
    prompt = request_data['prompt']
    output_format = request_data['format']

    # Simulate AI generating a response based on the prompt
    # In a real scenario, this would involve complex AI models.
    simulated_response = f"AI processed your prompt: '{prompt}'. Here is a simulated response."

    # --- Output Generation: What the AI tool RETURNS ---
    if output_format == 'text':
        return {"result": simulated_response}
    elif output_format == 'json':
        # Simulate returning structured data if requested
        return {"status": "success", "data": {"response": simulated_response, "details": "Additional AI insights could go here."}}

# --- Example Usage ---

# Example 1: Valid text input
valid_text_request = {
    "prompt": "Explain the concept of recursion.",
    "format": "text"
}
print("--- Valid Text Request ---")
print(json.dumps(process_ai_request(valid_text_request), indent=2))

# Example 2: Valid JSON input
valid_json_request = {
    "prompt": "Generate a short story about a space cat.",
    "format": "json"
}
print("\n--- Valid JSON Request ---")
print(json.dumps(process_ai_request(valid_json_request), indent=2))

# Example 3: Invalid input - missing key
invalid_missing_key = {
    "prompt": "What is the capital of France?"
    # 'format' is missing
}
print("\n--- Invalid Request (Missing Key) ---")
print(json.dumps(process_ai_request(invalid_missing_key), indent=2))

# Example 4: Invalid input - unsupported format
invalid_format = {
    "prompt": "Summarize this article.",
    "format": "xml"
}
print("\n--- Invalid Request (Unsupported Format) ---")
print(json.dumps(process_ai_request(invalid_format), indent=2))

# Example 5: Invalid input - empty prompt
invalid_empty_prompt = {
    "prompt": "",
    "format": "text"
}
print("\n--- Invalid Request (Empty Prompt) ---")
print(json.dumps(process_ai_request(invalid_empty_prompt), indent=2))
