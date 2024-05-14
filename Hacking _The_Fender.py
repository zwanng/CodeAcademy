import csv
import json

# A new list to save passwords have been compromised.
compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    password_row = line
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt','w') as compromised_user_file:
  for content in compromised_users:
    compromised_user_file.write(content + '\n')

# Open a new JSON file in write-mode called boss_message.json
with open('boss_message.json','w') as boss_message:
  boss_message_dict = {"recipient":"The Boss","message":"Mission Success"}
  json.dump(boss_message_dict,boss_message)

'''safely recover the compromised users, we'll want to remove the
"passwords.csv" file completely.'''
with open('new_passwords.csv','w') as new_passwords_obj:
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)
