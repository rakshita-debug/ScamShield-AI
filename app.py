print("================================")
print("       ScamShield AI")
print(" AI Scam and Phishing Detector")
print("================================")

message = input("Enter a message or suspicious link: ")

print("\nAnalyzing your message...")

suspicious_words = [
    "urgent",
    "verify your account",
    "password",
    "win prize",
    "click here",
    "bank details",
    "otp",
    "claim your reward"
]

message_lower = message.lower()

detected_words = []

for word in suspicious_words:
    if word in message_lower:
        detected_words.append(word)

if detected_words:
    print("\nWarning: This message may be a scam!")
    print("Suspicious words detected:", ", ".join(detected_words))
else:
    print("\nNo obvious scam keywords detected.")
    print("Still be careful with unknown links and messages.")