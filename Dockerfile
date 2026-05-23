FROM python:3.12-slim


WORKDIR /app


COPY cloudops_agent.py .


CMD ["python", "cloudops_agent.py"]
