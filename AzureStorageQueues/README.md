Azure Queue Worker — Resilient Producer-Consumer


A hands-on implementation of a producer-consumer messaging system using Azure Queue Storage and Python.

The project demonstrates how to decouple a message producer from a worker using Azure Queue Storage, including message processing, successful deletion, visibility timeout, and retry behavior.

Architecture:-

                         PRODUCER
                            │
                            │ send_message()
                            ▼
                 ┌─────────────────────┐
                 │                     │
                 │    AZURE QUEUE      │
                 │   order-processing  │
                 │                     │
                 │  Order #101         │
                 │  Order #102         │
                 │  Order #103         │
                 │                     │
                 └──────────┬──────────┘
                            │
                            │ receive_messages()
                            ▼
                        CONSUMER
                            │
                            ▼
                     Business Logic
                            │
                       Processing
                            │
                    ┌───────┴───────┐
                    │               │
                 SUCCESS          FAILURE
                    │               │
                    ▼               │
             delete_message()       │
                    │               │
                    ▼               ▼
                 REMOVED          RETRY


Why Azure Queue Storage?

A direct producer-to-worker architecture creates tight coupling:

    Producer ───────────────► Worker

If the worker is unavailable, the producer has nowhere to put the work.

Azure Queue Storage introduces a buffer:

    Producer ─────► Queue ─────► Worker


This allows:

* Asynchronous processing
* Producer/consumer decoupling
* Temporary worker failures
* Message backlog

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Flow

Producer

Continuously generates messages and sends them to Azure Queue Storage.

    producer.py
         │
         │ send_message()
         ▼
    Azure Queue


Consumer

Continuously retrieves messages, processes them, and deletes them only after successful processing.

    Azure Queue
         │
         │ receive_messages()
         ▼
    consumer.py
         │
         ▼
    Process message
         │
         ▼
    Successful?
       /     \
     NO       YES
     │         │
     │         ▼
     │    delete_message()
     │         │
     ▼         ▼
    Retry     Removed


Prerequisites

* Azure subscription
* Azure Storage Account
* Azure Queue
* Python 3
* Azure CLI
* Azure identity with permission to access Queue Storage (Storage Queue Data Contributor)

1. Create Python Virtual Environment
    python3 -m venv queue-lab
    source queue-lab/bin/activate

2. Install Dependencies
   pip install azure-storage-queue azure-identity

3. Authenticate with Azure
4. Configure the Storage Account
      Both applications require the Azure Storage Account name.
      STORAGE_ACCOUNT = "<YOUR_STORAGE_ACCOUNT>"
      QUEUE_NAME = "order-processing"
5. Producer

producer.py continuously generates order messages every 5sec.

Example: 
[PRODUCER] Sent: Process Order #1
[PRODUCER] Sent: Process Order #2
[PRODUCER] Sent: Process Order #3
[PRODUCER] Sent: Process Order #4
   
6. Consumer

consumer.py continuously checks the queue for messages.

For every message:

1. Receive the message
2. Process the message
3. If processing succeeds, delete the message
4. If processing fails, do not delete the message

[CONSUMER] Worker started
[CONSUMER] Waiting for messages...

================================
[CONSUMER] Received: Process Order #1
[CONSUMER] Processing: Process Order #1
[CONSUMER] Deleted: Process Order #1


The END
