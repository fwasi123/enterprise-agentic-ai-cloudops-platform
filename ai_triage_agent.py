# Enterprise Agentic AI CloudOps Platform
import random


print("===================================")

print(" Autonomous Incident Triage Agent ")

print("===================================")


def classify_severity(details):

    text = details.lower()


    if "down" in text or "outage" in text or "critical" in text:

        return "SEV1 - Critical"


    elif "slow" in text or "degraded" in text or "latency" in text:

        return "SEV2 - High"


    elif "warning" in text or "intermittent" in text:

        return "SEV3 - Medium"


    else:

        return "SEV4 - Low"



def ask_missing_info(details):

    required_items = ["application", "environment", "impact", "time"]

    missing = []


    for item in required_items:

        if item not in details.lower():

            missing.append(item)


    return missing



def recommend_steps(severity):

    if "SEV1" in severity:

        return [

            "Validate production application health.",

            "Check monitoring dashboards and alerts.",

            "Review logs for critical failures.",

            "Engage CloudOps and App Support teams.",

            "Avoid restarting services without approval."

        ]


    elif "SEV2" in severity:

        return [

            "Review system performance metrics.",

            "Check recent deployments or configuration changes.",

            "Validate container and VM health.",

            "Monitor user impact closely."

        ]


    else:

        return [

            "Continue monitoring.",

            "Document findings.",

            "Escalate if condition worsens."

        ]



def create_incident_id():

    return "INC" + str(random.randint(100000, 999999))



def generate_escalation(details, severity):

    incident_id = create_incident_id()


    message = f"""

===================================

 Incident Escalation Draft

===================================


Incident ID: {incident_id}


Severity: {severity}


Summary:

{details}


Recommended Action:

- Review monitoring dashboards

- Validate infrastructure health

- Escalate to application owner

- Review logs and recent deployments


Status:

Initial triage completed by Autonomous AI Agent.


===================================

"""


    return message



while True:


    print("\nChoose an option:")

    print("1. Analyze Incident")

    print("2. Exit")


    choice = input("Selection: ")


    if choice == "1":


        details = input("\nPaste incident details: ")


        severity = classify_severity(details)


        print("\nDetected Severity:")

        print(severity)


        missing = ask_missing_info(details)


        print("\nMissing Information:")


        if missing:

            for item in missing:

                print(f"- Missing {item}")


        else:

            print("No major information missing.")


        print("\nRecommended Safe Actions:")


        steps = recommend_steps(severity)


        for step in steps:

            print(f"- {step}")


        escalation = generate_escalation(details, severity)


        print(escalation)


    elif choice == "2":


        print("AI Agent shutting down.")

        break


    else:

        print("Invalid selection.")
