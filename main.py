#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of Breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the 2019 Facebook Data Breach!")


#Introduces Breach

print("Would you like to learn about the Facebook Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains Breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Malicious hackers exploited a vulnerability in Facebook’s platform. Over 530 million Facebook users were affected: phone numbers, full names, locations, email addresses, and other information were exposed and posted to a hacking forum.")
  
  elif topic.lower() == "b":
    print("After the breach, Facebook decided to not notify their users because it was not an issue their users could fix themselves.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my Take

print("\n I'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my Take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("The 2019 Breach relates to the confidentiality pillar of the CIA Triad because personal information given to Facebook by its over 530 million users was leaked.")
  
  elif topic.lower() == "b":
    print("I don’t agree with Facebook’s response because although users may not be able to do anything about the breach, Facebook denies its users the knowledge of what happened with their private information. It shows that the company couldn't care less about the data they collect.")
  
  elif topic.lower() == "c":
    print("My advice for a victim of the 2019 Facebook Data Breach would be to change any accounts that use the same password and strengthen them with password managers.")
    
  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")
  
  #Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
