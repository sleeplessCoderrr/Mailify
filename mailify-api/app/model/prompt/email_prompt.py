from ..request.request import Request

def generate_email_prompt(req:Request):
    return (f"Generate an email for {req.purpose}. The sender is {req.name}, and the receiver is {req.receiver}. "
            f"The receiver's email is {req.receiver_mail}. The goal categories are {req.goal_categories}. "
            f"The email's subject should be about: {req.email_about}. Please generate a professional email.")