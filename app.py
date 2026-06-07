def validate_amount(amount):
    if amount <= 0:
        return False
    return True

def validate_card_number(card_number):
    if len(str(card_number)) != 16:
        return False
    return True

def get_transaction_status(amount, card_number):
    if not validate_amount(amount):
        return "DECLINED - Invalid amount"
    if not validate_card_number(card_number):
        return "DECLINED - Invalid card"
    return "APPROVED"
