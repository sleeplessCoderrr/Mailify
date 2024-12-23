# Dependencies and model loading
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_path = "../model/email_generator/"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)


# Result class
class Result:
    def __init__(self, person_mail, generated_mail, email_subject):
        self.person_mail = person_mail
        self.generated_mail = generated_mail
        self.email_subject = email_subject

# Request class
class Request:
    def __init__(self, purpose, name, receiver, receiver_mail, goal_categories, email_about):
        self.purpose = purpose
        self.name = name
        self.receiver = receiver
        self.receiver_mail = receiver_mail
        self.goal_categories = goal_categories
        self.email_about = email_about

    def generate(self):
        
        result = generator(
            prompt,
            max_length=200,  
            do_sample=True,  
            early_stopping=True,
        )
        subject = generator(
            prompt,
            max_length=50,  
            do_sample=True,  
            early_stopping=True
        )

        mail = Result(
            self.receiver_mail, 
            result[0]['generated_text'], 
            subject[0]['generated_text']
        )
        
        return mail;
