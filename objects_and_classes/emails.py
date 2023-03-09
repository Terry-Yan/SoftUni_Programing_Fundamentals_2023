class Email:
    def __init__(self, sender_value, receiver_value, content_value):
        self.sender = sender_value
        self.receiver = receiver_value
        self.content = content_value
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


line = input()
emails = []

while line != "Stop":
    line_args = line.split()
    sender = line_args[0]
    receiver = line_args[1]
    content = line_args[2]

    email = Email(sender, receiver, content)
    emails.append(email)

    line = input()

indexes_of_emails_to_be_sent = [int(element) for element in input().split(", ")]

for index, email in enumerate(emails):
    if index in indexes_of_emails_to_be_sent:
        emails[index].send()

    message = emails[index].get_info()
    print(message)

