while True:


    command = input("What do you need help with? ").lower()


    if "azure" in command:

        print("Azure cloud environment is operational.")


    elif "docker" in command:

        print("Docker containers are ready.")


    elif "python" in command:

        print("Python AI environment is active.")


    elif "kubernetes" in command:

        print("Kubernetes tools are installed.")


    elif "ai" in command:

        print("AI agent is learning new skills.")


    elif "help" in command:

        print("Available commands:")

        print("- azure")

        print("- docker")

        print("- python")

        print("- kubernetes")

        print("- ai")

        print("- exit")


    elif "exit" in command:

        print("Shutting down AI assistant.")

        break


    else:

        print("I do not understand that request yet.")
