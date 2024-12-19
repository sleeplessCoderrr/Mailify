from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_path = "../model"  
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

generator = pipeline(
    'text-generation', 
    model=model, 
    tokenizer=tokenizer,
)

def generate_job_application_email(sender_name, receiver_name, main_point, max_length=150):
    """
    Generates a job application email based on the provided details.

    Args:
        sender_name (str): Name of the sender.
        receiver_name (str): Name of the receiver.
        main_point (str): The main point or purpose of the email.
        max_length (int): The maximum length of the generated email.

    Returns:
        str: The generated email text.
    """
    # Construct the prompt
    prompt = f"""
    Write an email applying for a job:

    Dear {receiver_name},

    {main_point}

    Sincerely,
    {sender_name}
    """

    result = generator(
        prompt,
        max_length=max_length,
        do_sample=False, 
        early_stopping=True,
    )
    
    return result[0]['generated_text']
