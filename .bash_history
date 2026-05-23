sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl wget unzip python3-pip docker.io
docker --version
python3 --version
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az version
sudo reboot
docker run hello-world
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
hmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
mkdir ~/ai-lab && cd ~/ai-lab
python3 -m venv venv
chmod +x kubectl
sudo apt update && sudo apt install -y python3.12-venv
cd ~/ai-lab
python3 -m venv venv
source venv/bin/activate
pip install openai langchain fastapi uvicorn jupyter pandas requests
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
python3
nano first_ai_test.py
python first_ai_test.py
nano chatbot.py
python chatbot.py
Faraz
What is your name?
Faraz
python chatbot.py
nano chatbot.py
python chatbot.py
sudo usermod -aG docker $USER
newgrp docker
nano chatbot.py
python  chatbot.py
python chatbot.py
nano chatbot.py
python chatbot.py
python3 chatbot.py
nano agent.py
python3 agent.py
nano smart_agent.py
python3 smart_agent.py
