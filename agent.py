while True:

    command = input("Agent command: ").lower()


    if "status" in command:

        print("Azure VM: Running")

        print("Docker: Installed")

        print("Python AI environment: Ready")


    elif "docker" in command:

        print("Docker is ready for containers.")


    elif "azure" in command:

        print("Azure CLI and VM lab are ready.")


    elif "exit" in command:

        print("Goodbye.")

        break


    else:

        print("I do not know that command yet.")
