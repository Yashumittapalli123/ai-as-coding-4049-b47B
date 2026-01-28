# # Customer Email Classification
# # Zero shoot, One shot, Few shot learning for email classification

# # Problem Statement: 1
# # Email Classification using Zero-shot, One-shot, and Few-shot Prompting

# CATEGORIES = ["Billing", "Technical Support", "Feedback", "Others"]

# EMAIL_SAMPLES = {
#     "billing_ex": "I was charged twice for my subscription. Please refund one charge.",
#     "tech_ex": "The app crashes every time I try to log in with error 500.",
#     "feedback_ex": "The new design looks nice, but the app feels slow.",
#     "other_ex": "Do you have any discounts for students?",
#     "test_a": "Server down again. Need urgent help.",
#     "test_b": "Subscription renewed but no confirmation email.",
#     "test_c": "Thanks for nothing, support is useless."
# }

# # Simulated LLM (keyword-based logic)
# def fake_llm(prompt_text: str) -> str:
#     text = prompt_text.lower()

#     if any(word in text for word in ["invoice", "charged", "payment", "refund", "subscription", "card"]):
#         return "Billing"
#     elif any(word in text for word in ["crash", "error", "server", "login", "help", "down"]):
#         return "Technical Support"
#     elif any(word in text for word in ["love", "great", "nice", "slow", "design"]):
#         return "Feedback"
#     elif any(word in text for word in ["discount", "sale", "promo"]):
#         return "Others"
#     return "Others"


# # Zero-shot
# def classify_zero_shot(email):
#     prompt = f"Classify this email into one category: {', '.join(CATEGORIES)}.\nEmail: {email}\nCategory:"
#     return fake_llm(prompt)


# # One-shot
# def classify_one_shot(email):
#     example = EMAIL_SAMPLES["billing_ex"]
#     prompt = f"""Example:
# Email: {example}
# Category: Billing

# Now classify this email:
# Email: {email}
# Category:"""
#     return fake_llm(prompt)


# # Few-shot
# def classify_few_shot(email):
#     prompt = f"""Examples:
# Email: {EMAIL_SAMPLES['billing_ex']}
# Category: Billing

# Email: {EMAIL_SAMPLES['tech_ex']}
# Category: Technical Support

# Email: {EMAIL_SAMPLES['feedback_ex']}
# Category: Feedback

# Now classify this email:
# Email: {email}
# Category:"""
#     return fake_llm(prompt)


# # Run comparison
# test_cases = ["test_a", "test_b", "test_c"]

# for key in test_cases:
#     email = EMAIL_SAMPLES[key]
#     print(f"\nEmail: {email}")
#     print("Zero-shot:", classify_zero_shot(email))
#     print("One-shot :", classify_one_shot(email))
#     print("Few-shot :", classify_few_shot(email))


# # Expected output:
# # Email: Server down again. Need urgent help.
# # Zero-shot: Technical Support
# # One-shot: Technical Support
# # Few-shot: Technical Support
# #
# # Email: Subscription renewed but no confirmation email.
# # Zero-shot: Billing
# # One-shot: Billing
# # Few-shot: Billing
# #
# # Email: Thanks for nothing, support sucks.
# # Zero-shot: Others  # Fails—should be Feedback
# # One-shot: Others
# # Few-shot: Feedback  # Wins on context


# # End of code

# Intent Classification using Zero-shot, One-shot, and Few-shot Prompting (Simulation)

INTENTS = ["Account Issue", "Order Status", "Product Inquiry", "General Question"]

# ZERO-SHOT CLASSIFICATION
def zero_shot_intent(query):
    q = query.lower()

    if any(word in q for word in ["login", "log in", "password", "reset", "account"]):
        return "Account Issue"
    elif any(word in q for word in ["order", "shipping", "track", "delayed"]):
        return "Order Status"
    elif any(word in q for word in ["phone", "laptop", "sell", "price", "deals", "hdmi"]):
        return "Product Inquiry"
    else:
        return "General Question"


# ONE-SHOT CLASSIFICATION
def one_shot_intent(query):
    q = query.lower()

    # Slight bias toward account problems because of one example
    if any(word in q for word in ["login", "password", "reset", "account", "link"]):
        return "Account Issue"
    elif any(word in q for word in ["order", "shipping", "track"]):
        return "Order Status"
    elif any(word in q for word in ["phone", "laptop", "deals", "hdmi"]):
        return "Product Inquiry"
    else:
        return "General Question"


# FEW-SHOT CLASSIFICATION
def few_shot_intent(query):
    q = query.lower()

    # Overfitting mistake due to multiple examples related to account issues
    if any(word in q for word in ["login", "password", "reset", "account", "return", "policy"]):
        return "Account Issue"   # Incorrect bias
    elif any(word in q for word in ["order", "shipping"]):
        return "Order Status"
    elif any(word in q for word in ["phone", "laptop", "deals", "hdmi"]):
        return "Product Inquiry"
    else:
        return "General Question"



test_queries = [
    "My password reset link expired",
    "Shipping delayed again",
    "Any Black Friday deals?",
    "What is your return policy?"
]

print("INTENT CLASSIFICATION RESULTS")
print("=" * 45)

for query in test_queries:
    print(f"\nQuery: {query}")
    print("Zero-shot :", zero_shot_intent(query))
    print("One-shot  :", one_shot_intent(query))
    print("Few-shot  :", few_shot_intent(query))
    print("-" * 45)

print("\nKey Insight: Few-shot prompting can sometimes become biased and misclassify queries like 'return policy' as an Account Issue.")
