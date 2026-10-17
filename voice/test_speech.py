from voice.speech import SpeechRecognizer


speech = SpeechRecognizer()

print("================================")
print("       VOICE TEST")
print("================================")
print()
print("Speak after 'Listening...' appears.")
print("Press Ctrl+C to stop.")
print()

try:

    while True:

        text = speech.listen()

        if text:
            print(f"You said: {text}")

except KeyboardInterrupt:

    print()
    print("Voice test stopped.")