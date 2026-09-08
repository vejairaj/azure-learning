import time
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient

STORAGE_ACCOUNT = "myappqueue"
QUEUE_NAME = "order-processing"

credential = DefaultAzureCredential()

queue = QueueClient(
    account_url=f"https://{STORAGE_ACCOUNT}.queue.core.windows.net",
    queue_name=QUEUE_NAME,
    credential=credential
)

counter = 1

while True:
    message = f"Process Order #{counter}"

    queue.send_message(message)

    print(f"[PRODUCER] Sent: {message}")

    counter += 1

    time.sleep(2)
