
import datetime
import random


def get_time_of_day():
  """Return which part of the day it is."""
  current_hour = datetime.datetime.now().hour

  if 5 <= current_hour < 12:
    return "morning"
  elif 12 <= current_hour < 17:
    return "afternoon"
  elif 17 <= current_hour < 21:
    return "evening"
  else:
    return "night"


def get_greeting(name):
  """Print a greeting for user based upon time."""
  time_of_day = get_time_of_day()

  print("  ---------------")
  if time_of_day == "morning":
    print(f"Good Morning, {name}!")
  elif time_of_day == "afternoon":
    print(f"Good Afternoon, {name}!")
  elif time_of_day == "evening":
    print(f"Good Evening, {name}!")
  else:
    print(f"Good Night, {name}!")

  return time_of_day


def get_recommendation(age, time_of_day):
  """
  Print a recommendation based on the user's age and the current time.
  """
  if age < 18:
    if time_of_day == "morning":
      print("How are you doing today ? Get ready for school !!")
    elif time_of_day == "afternoon":
      print("How are you doing today ? Hope you had fun at school. Time to play and enjoy.")
    elif time_of_day == "evening":
      print("How are you doing today ? Hope you had a nice day. Have a healthy dinner to get strong.")
    else:
      print("Hope you had a fun day. Time to sleep and give your body some rest.")
  else:
    if time_of_day == "morning":
      print("Time to start your day !!")
    elif time_of_day == "afternoon":
      print("Hope you had good time so far today.")
    elif time_of_day == "evening":
      print("Hope you had a productive day at work! Time to relax and have dinner")
    else:
      print("Time to sleep and give your body and mind some good rest")


def motivational_message(time_of_day):
  """
  Print a random motivational quote for the current part of the day.
  Print this only for adults. Motivational quotes is being skipped for kids.
  """
  morning = [
    "With the new day comes new strength and new thoughts. — Eleanor Roosevelt",
    "Either you run the day, or the day runs you. — Jim Rohn",
    "Do not wait; the time will never be 'just right.' Start where you stand. — Napoleon Hill",
    "Every sunrise is a new opportunity to get closer to your dreams. — Unknown"
  ]
  afternoon = [
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "If you spend too much time thinking about a thing, you'll never get it done. Make at least one definite move daily toward your goal. — Bruce Lee",
    "The shortest way to do many things is to only do one thing at a time. — Wolfgang Amadeus Mozart",
    "Don't be busy. Be productive. — Unknown"
  ]
  evening = [
    "Yesterday's the past, tomorrow's the future, but today is a gift. That's why it's called the present. — Bil Keane",
    "The future depends on what we do in the present. — Mahatma Gandhi",
    "When you get into a tight place and everything goes against you… never give up then, for that is just the place and time that the tide will turn. — Harriet Beecher Stowe",
    "You can't make up for lost time—you can only do better moving forward. — Unknown"
  ]
  night = [
    "Rest is a requirement, not a reward. You have worked hard enough today; give your mind and body the permission to fully recharge.",
    "Stars cannot shine without darkness. Use this quiet time to appreciate how much you have grown, even through the difficult moments of the day.",
    "Sleep is the ultimate reset button. Close your eyes knowing that tomorrow brings a completely fresh page and a brand-new start.",
    "Be proud of the effort you put in today. Every small step you took is moving you closer to your goals, even if it does not feel like it yet."
  ]

  if time_of_day == "morning":
    messages = morning
  elif time_of_day == "afternoon":
    messages = afternoon
  elif time_of_day == "evening":
    messages = evening
  else:
    messages = night

  print("Here is a motivational message for you..")
  print(random.choice(messages))

def main():
  """Collect user details and show personalised messages."""
  try:
    print("Hello. How are you ?")
    print("Please provide some more info so that I can help you.")

    # Get and validate Name
    while True:
      name = input("Enter your name: ").strip()
      if name.replace(" ", "").isalpha():
        break
      print("Please enter a valid name (letters only).")

    # Get and validate Age
    while True:
      try:
        age = int(input("Enter your age: "))
        if age > 0:
          break
        print("Age must be a positive number.")
      except ValueError:
        print("Please enter a valid integer for your age.")

    # Get and validate Gender
    while True:
      gender_input = input("Enter your gender (M for Male / F for Female): ").strip().upper()
      if gender_input == "M":
        gender = "Male"
        break
      if gender_input == "F":
        gender = "Female"
        break
      print("Please enter M for Male or F for Female.")

    # Display the collected information
    # print("\n--- User Information ---")
    # print(f"Name: {name}")
    # print(f"Age: {age}")
    # print(f"Gender: {gender}")

    time_of_day = get_greeting(name)
    get_recommendation(age, time_of_day)
    if age >= 18:
      motivational_message(time_of_day)
    print("  ---------------")
  except KeyboardInterrupt:
    """ Graceful exit in case ctrl+c is used.  """
    print("\nProgram stopped by user.")


if __name__ == "__main__":
  main()
