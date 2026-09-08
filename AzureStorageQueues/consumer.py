import time
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient

STORAGE_ACCOUNT = "myappqueue"
QUEUE_NAME = "order-processing"

queue_url = (
    f"https://{STORAGE_ACCOUNT}.queue.core.windows.net/{QUEUE_NAME}"
)

credential = DefaultAzureCredential()

queue = QueueClient(
    queue_url=queue_url,
    credential=credential
)

while True:

    messages = queue.receive_messages(
        messages_per_page=1,
        visibility_timeout=30
    )

    found_message = False

    for message in messages:

        found_message = True

        print(f"[CONSUMER] Received: {message.content}")

        # Simulate actual business processing
        print(f"[CONSUMER] Processing: {message.content}")

        time.sleep(2)

        # Processing succeeded
        queue.delete_message(message)

        print(f"[CONSUMER] Deleted: {message.content}")

    if not found_message:
        time.sleep(2)
