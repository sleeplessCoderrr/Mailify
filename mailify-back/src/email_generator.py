# Dependencies and model loading
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_path = "../model/email_generator/"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# Request class
class Request:
    def __init__(self, purpose, name, receiver, goalCategories, emailAbout):
        self.purpose = purpose
        self.name = name
        self.receiver = receiver
        self.goalCategories = goalCategories
        self.emailAbout = emailAbout 

# Email Generator Function
def request_invoker(request: Request):
    # Construct the prompt for the model
    prompt = f"""
    Write an email applying for a job:

    Dear {request.receiver},

    {request.emailAbout}

    Sincerely,
    {request.name}
    """

    # Generate the email using the loaded model
    result = generator(
        prompt,
        max_length=200,  # Specify a max length to avoid overly long generations
        do_sample=True,  # Enable sampling for more creative outputs
        early_stopping=True,
    )

    # Return the generated text
    return result[0]['generated_text']
