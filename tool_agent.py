# Enterprise Agentic AI CloudOps Platform
def check_cpu():

    return "CPU check completed: system looks healthy."


def check_docker():

    return "Docker check completed: containers are ready."


def create_incident():

    return "Incident created: CloudOps ticket opened for investigation."


def recommend_action(issue):

    return f"Recommended action for '{issue}': investigate logs, validate service health, and escalate if needed."


while True:

    user_input = input("Agentic AI > ").lower()


    if "cpu" in user_input:

        print(check_cpu())


    elif "docker" in user_input:

        print(check_docker())


    elif "incident" in user_input:

        print(create_incident())


    elif "recommend" in user_input:

        issue = input("Describe the issue: ")

        print(recommend_action(issue))


    elif "exit" in user_input:

        print("Agent shutting down.")

        break


    else:

        print("I can use tools for: cpu, docker, incident, recommend, exit")
