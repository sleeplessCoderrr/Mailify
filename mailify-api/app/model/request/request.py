class Request:
    def __init__(self, purpose, name, receiver, receiver_mail, goal_categories, email_about):
        self.purpose = purpose
        self.name = name
        self.receiver = receiver
        self.receiver_mail = receiver_mail
        self.goal_categories = goal_categories
        self.email_about = email_about