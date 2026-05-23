memory = []


while True:

    command = input("Memory Agent > ")


    if command.lower().startswith("remember"):

        item = command.replace("remember", "").strip()

        memory.append(item)

        print(f"Saved to memory: {item}")


    elif command.lower() == "show memory":

        print("Agent memory:")

        for item in memory:

            print(f"- {item}")


    elif command.lower() == "exit":

        print("Memory Agent shutting down.")

        break


    else:

        print("Try: remember <something>, show memory, or exit")
