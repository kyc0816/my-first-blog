from googlevoice import Voice
from googlevoice.util import input

user = 'katejohnsonfromkenya@gmail.com'
password = 'ghlwkd10%'

voice = Voice()
voice.login(user, password)

# number = input('Number to send message to: ') # use these for command method
# message = input('Message text: ')

voice.send_sms('821029339435', 'hi')