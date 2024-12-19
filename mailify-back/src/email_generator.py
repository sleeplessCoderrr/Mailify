from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_path = "../model/email_generator/"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def generate_job_application_email(sender_name, receiver_name, main_point, max_length=150):
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
