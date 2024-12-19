# Depedencies and model loading
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_path = "../model/email_generator/"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

# Request class
class Request:
    def __init__ (self, purpose, name, receiver, goalCategories, emailAbout):
        self.purpose = purpose
        self.name = name
        self.receiver = receiver
        self.goalCategories = goalCategories
        self.emailAbout = emailAbout 

# Email Generator Function
### TODO: Implement the generate_email function:
'''
functionnya udah kepanggil sama api kalo user minta request, nah tolong dong olah datanya, jadi lu bikinin prompnya manual berdasarkan 
purposenya dan goalCategoriesnya, dan email aboutnya terus lu generate emailnya pake model yang udah di load di atas, terus return hasilnya.
bikinnya didalam file ini ajah, dibawah" ini gapapa
'''
def generate_email(request:Request):
    
    
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


def generate_job_application_email(request:Request):
    receiver_name = request.receiver
    sender_name = request.name
    main_point = f"I am writing to apply for the {request.purpose} position. I am confident that my {', '.join(request.goalCategories)} skills make me a perfect fit for this role."
    max_length = 200

    return generate_email(request)

def generate_college_email(request:Request):
    receiver_name = request.receiver
    sender_name = request.name
    main_point = f"I am writing to apply for the {request.purpose} program. I am confident that my {', '.join(request.goalCategories)} skills make me a perfect fit for this program."
    max_length = 200

    return generate_email(request)