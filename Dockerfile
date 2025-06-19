FROM python:3.11-slim

WORKDIR /app

# Clone the Git repo (or COPY if already inside the image build context)
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/<your-username>/crud-api.git .

RUN pip install --no-cache-dir -r requirements.txt

COPY startup.sh .
RUN chmod +x startup.sh

CMD ["./startup.sh"]
