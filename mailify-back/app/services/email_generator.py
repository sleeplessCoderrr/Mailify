from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_path = "../../models/email_generatorV2"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

class Result:
    def __init__(self, person_mail, generated_mail, email_subject):
        self.person_mail = person_mail
        self.generated_mail = generated_mail
        self.email_subject = email_subject

class Request:
    def __init__(self, purpose, name, receiver, receiver_mail, goal_categories, email_about):
        self.purpose = purpose
        self.name = name
        self.receiver = receiver
        self.receiver_mail = receiver_mail
        self.goal_categories = goal_categories
        self.email_about = email_about

    def make_email_prompt(self):
        prompt = (
            "You are an expert email writing assistant specializing in crafting professional, "
            "polished, and impactful emails. Compose an email with excellent word choice, "
            "clear structure, and a professional tone."
        )

        prompt += f" The purpose of this email is {self.purpose}. "
        prompt += f"The sender is {self.name}, addressing it to {self.receiver}. "

        if self.goal_categories:
            prompt += (
                f"The email is intended for a purpose categorized under: "
                f"{', '.join(self.goal_categories)}. "
            )

        prompt += (
            f"The email should focus on the topic: '{self.email_about}'. "
            "Ensure the email includes appropriate salutations, concise paragraphs, and a clear call to action. "
            "It should be well-structured, easy to read, and tailored for the recipient's understanding."
        )

        prompt += (
            " Use formal and professional language, maintaining a respectful tone. "
            "Avoid redundancy and include only the essential details to convey the message effectively."
        )

        return prompt

    def make_subject_prompt(self):
        return f"Generate an appropriate subject line for an email to {self.receiver} about {self.email_about}."

    def generate(self):
        print("Generating email...")
        email_prompt = self.make_email_prompt()
        generated_email = generator(
            email_prompt,
            max_length=200,
        )[0]['generated_text']

        print("Generating subject...")
        subject_prompt = self.make_subject_prompt()
        generated_subject = generator(
            subject_prompt,
            max_length=50,
        )[0]['generated_text']

        return Result(self.receiver_mail, generated_email, generated_subject)
