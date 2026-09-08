hat we’re going to build is production like messaging queue 

Azure Queue Storage is designed specifically for this producer/consumer decoupling pattern

                 YOUR MAC
        ┌──────────────────────┐
        │                      │
        │  producer.py         │
        │      │               │
        │      │ send          │
        │      ▼               │
        │  Azure Queue         │
        │      │               │
        │      │ receive       │
        │      ▼               │
        │  consumer.py         │
        │      │               │
        │      │ process OK    │
        │      ▼               │
        │    DELETE            │
        │                      │
        └──────────────────────┘
        
We’ll eventually move consumer.py to your Azure VM:


Mac
 │
 │ producer
 ▼
Azure Queue
 │
 │ consumer
 ▼
Azure VM




1 First install the Python SDK

python3 -m venv queue-lab
source queue-lab/bin/activate

#then

pip install azure-storage-queue azure-identity

2. Create the producer

producer.py

3. Create the consumer

consumer.py

4. Now watch the automation

Terminal 1 — Producer

[PRODUCER] Sent: Process Order #1
[PRODUCER] Sent: Process Order #2
[PRODUCER] Sent: Process Order #3
[PRODUCER] Sent: Process Order #4
[PRODUCER] Sent: Process Order #5



Terminal 2 — Consumer

[CONSUMER] Received: Process Order #1
[CONSUMER] Processing: Process Order #1
[CONSUMER] Deleted: Process Order #1

[CONSUMER] Received: Process Order #2
[CONSUMER] Processing: Process Order #2
[CONSUMER] Deleted: Process Order #2


Flow:-

Producer
   │
   ├── #1 ──────┐
   ├── #2 ──────┤
   ├── #3 ──────┤
   ├── #4 ──────┤
   └── #5 ──────┤
                ▼
          Azure Queue
                │
                ▼
            Consumer
                │
                ▼
             Process
                │
                ▼
             DELETE










