name = input("What is your name? ")

goal = input("What do you want to build today? ")


print(f"\nHello {name}!")


if "agent" in goal.lower():

    print("Excellent choice. We will build an AI agent.")

elif "website" in goal.lower():

    print("Great. We will build a website.")

elif "app" in goal.lower():

    print("Awesome. We will build an application.")

else:

    print("Interesting project!")


print("Your Azure AI assistant is learning.")
