dataset = [
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Weekday", "No", "No", "No"),
    ("Holiday", "Yes", "Yes", "Yes"),
    ("Weekend", "Yes", "Yes", "Yes"),
    ("Holiday", "No", "No", "No"),
    ("Weekend", "Yes", "No", "Yes"),
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Weekend", "Yes", "Yes", "Yes"),
    ("Holiday", "Yes", "Yes", "Yes"),
    ("Holiday", "No", "Yes", "Yes"),
    ("Holiday", "No", "No", "No"),
    ("Weekend", "Yes", "Yes", "Yes"),
    ("Holiday", "Yes", "Yes", "Yes"),
    ("Holiday", "Yes", "Yes", "Yes"),
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Holiday", "No", "Yes", "Yes"),
    ("Weekday", "Yes", "No", "Yes"),
    ("Weekend", "No", "No", "Yes"),
    ("Weekend", "No", "Yes", "Yes"),
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Weekend", "Yes", "Yes", "No"),
    ("Holiday", "No", "Yes", "Yes"),
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Holiday", "No", "No", "No"),
    ("Weekday", "No", "Yes", "No"),
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Weekday", "Yes", "Yes", "Yes"),
    ("Holiday", "Yes", "Yes", "Yes"),
    ("Weekend", "Yes", "Yes", "Yes")
]


def naive_bayes_classifier(day, discount, delivery):
    total_entries = len(dataset)
    purchase_count = 0
    not_purchase_count = 0
    day_purchase_count = 0
    discount_purchase_count = 0
    delivery_purchase_count = 0
    day_not_purchase_count = 0
    discount_not_purchase_count = 0
    delivery_not_purchase_count = 0
    
    for entry in dataset:
        if entry[3] == "Yes":
            purchase_count += 1
            if entry[0] == day: day_purchase_count += 1
            if entry[1] == discount: discount_purchase_count += 1
            if entry[2] == delivery: delivery_purchase_count += 1
        else:
            not_purchase_count += 1
            if entry[0] == day: day_not_purchase_count += 1
            if entry[1] == discount: discount_not_purchase_count += 1
            if entry[2] == delivery: delivery_not_purchase_count += 1
    
    prob_purchase = (day_purchase_count / purchase_count) * (discount_purchase_count / purchase_count) * (delivery_purchase_count / purchase_count) * (purchase_count / total_entries)
    prob_not_purchase = (day_not_purchase_count / not_purchase_count) * (discount_not_purchase_count / not_purchase_count) * (delivery_not_purchase_count / not_purchase_count) * (not_purchase_count / total_entries)
    
    return prob_purchase, prob_not_purchase

prob_purchase, prob_not_purchase = naive_bayes_classifier("Weekday", "No", "No")

print(f"Probability of Purchase: {prob_purchase}")
print(f"Probability of Not Purchase: {prob_not_purchase}")
