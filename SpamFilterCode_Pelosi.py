# List of common spam keywords/phrases
SPAM_KEYWORDS = [
    "free", "winner", "congratulations", "urgent", "act now", "risk-free",
    "guaranteed", "100% free", "cash bonus", "click here", "subscribe",
    "limited time", "exclusive deal", "earn money", "work from home",
    "no obligation", "trial", "credit card", "mortgage", "investment",
    "double your income", "fast cash", "hidden charges", "win big",
    "lowest price", "amazing", "special promotion", "cheap", "extra income",
    "get paid"
]

def calculate_spam_score(message):
    """Scans the message for spam keywords and calculates score + triggers."""
    score = 0
    triggers = []
    lowered = message.lower()
    
    for keyword in SPAM_KEYWORDS:
        if keyword in lowered:
            score += 1
            triggers.append(keyword)
    
    return score, triggers

def classify_spam(score):
    """Classifies spam likelihood based on score."""
    if score == 0:
        return "Not Spam"
    elif 1 <= score <= 3:
        return "Low likelihood of Spam"
    elif 4 <= score <= 7:
        return "Moderate likelihood of Spam"
    else:
        return "High likelihood of Spam"

def main():
    # Get user input
    message = input("Enter your email message:\n")
    
    # Calculate spam score
    score, triggers = calculate_spam_score(message)
    
    # Classify
    likelihood = classify_spam(score)
    
    # Display results
    print("\n--- Spam Analysis ---")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")
    if triggers:
        print("Triggered words/phrases:", ", ".join(triggers))
    else:
        print("No spam words detected.")

# Run program
if __name__ == "__main__":
    main()
