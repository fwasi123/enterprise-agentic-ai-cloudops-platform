# Enterprise Agentic AI CloudOps Platform
while True:


    issue = input("Describe infrastructure issue: ").lower()


    if "cpu" in issue:

        print("High CPU detected.")

        print("Recommendation: Scale VM or investigate running processes.")


    elif "memory" in issue:

        print("Memory pressure detected.")

        print("Recommendation: Restart workloads or increase memory allocation.")


    elif "disk" in issue:

        print("Disk issue detected.")

        print("Recommendation: Clean storage or expand disk capacity.")


    elif "docker" in issue:

        print("Docker issue detected.")

        print("Recommendation: Restart containers and inspect logs.")


    elif "kubernetes" in issue:

        print("Kubernetes cluster issue detected.")

        print("Recommendation: Check pod health and node status.")


    elif "network" in issue:

        print("Network issue detected.")

        print("Recommendation: Validate firewall rules and connectivity.")


    elif "exit" in issue:

        print("Autonomous AI shutting down.")

        break


    else:

        print("Unknown issue. Escalating to engineering team.")
