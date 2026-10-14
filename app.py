print("================================")
<<<<<<< Updated upstream
print("          ScamShield AI")
print("   AI Scam and Phishing Detector")
=======
print("       ScamShield AI")
print(" AI Scam apy appnd Phishing Detector")
>>>>>>> Stashed changes
print("================================")

message = input("\nEnter a message or suspicious link: ")
message_lower = message.lower()

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

detected_words = []

for word in suspicious_words:
    if word in message_lower:
        detected_words.append(word)

# Calculate a basic risk score
risk_score = min(len(detected_words) * 25, 100)

print("\n---------- SCAN RESULT ----------")

if risk_score >= 50:
    print("Risk Level: HIGH")
    print("Warning: This message has several scam indicators!")
elif risk_score > 0:
    print("Risk Level: MEDIUM")
    print("Caution: Suspicious words were detected.")
else:
    print("Risk Level: LOW")
    print("No obvious scam keywords detected.")

print("Risk Score:", risk_score, "/ 100")

if detected_words:
    print("Detected indicators:", ", ".join(detected_words))

print("---------------------------------")
print("Note: This is a basic prototype, not a guarantee of safety.")