def calculate_due_amount(total_bill, amount_paid):
    if amount_paid >= total_bill:
        return 0.0
    else:
        due_amount = total_bill - amount_paid
        return due_amount
print(calculate_due_amount(100.0, 70.0)) # Output: 30.0