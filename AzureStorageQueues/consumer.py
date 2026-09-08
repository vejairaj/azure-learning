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

    account_url=f"https://{STORAGE_ACCOUNT}.queue.core.windows.net",

    queue_name=QUEUE_NAME,

    credential=credential
)



print("[CONSUMER] Worker started")

print("[CONSUMER] Waiting for messages...")

while True:

    try:

        messages = queue.receive_messages(

            messages_per_page=1,

            visibility_timeout=30

        )

        found_message = False

        for message in messages:

            found_message = True

            print()

            print("================================")

            print(f"[CONSUMER] Received: {message.content}")

            try:

                # --------------------------------

                # BUSINESS LOGIC

                # --------------------------------

                print(

                    f"[CONSUMER] Processing: "

                    f"{message.content}"

                )

                time.sleep(2)

                # --------------------------------

                # PROCESSING SUCCESSFUL

                # --------------------------------

                queue.delete_message(message)

                print(

                    f"[CONSUMER] Deleted: "

                    f"{message.content}"

                )

            except Exception as e:

                print(

                    f"[CONSUMER] Processing failed: {e}"

                )

                print(

                    "[CONSUMER] Message will become "

                    "visible again after timeout."

                )

        if not found_message:

            time.sleep(2)

    except Exception as e:

        print(f"[CONSUMER] Queue error: {e}")

        time.sleep(5)
