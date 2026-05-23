# Enterprise Agentic AI CloudOps Platform
while True:

    command = input("CloudOps AI > ").lower()


    if "cpu" in command:

        print("CPU utilization is healthy.")

    elif "memory" in command:

        print("Memory usage is within thresholds.")

    elif "disk" in command:

        print("Disk storage is operational.")

    elif "docker" in command:

        print("Docker containers are running.")

    elif "azure" in command:

        print("Azure VM and Bastion access are operational.")

    elif "incident" in command:

        print("No critical incidents detected.")

    elif "help" in command:

        print("Commands: cpu, memory, disk, docker, azure, incident, exit")

    elif "exit" in command:

        print("CloudOps AI shutting down.")

        break

    else:

        print("Unknown operational request.")
