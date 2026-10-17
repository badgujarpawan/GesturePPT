import time

from voice.worker import VoiceWorker


worker = VoiceWorker()

print("================================")
print("       VOICE WORKER TEST")
print("================================")
print()
print("Speak a PowerPoint command.")
print("Try: next slide")
print("Press Ctrl+C to stop.")
print()

worker.start()

try:

    while True:

        command = worker.get_command()

        if command:

            print(
                f"MAIN RECEIVED: {command.name}"
            )

        time.sleep(0.1)

except KeyboardInterrupt:

    print()
    print("Stopping worker...")

    worker.stop()

    print("Worker stopped.")