from app import validate_amount, validate_card_number, get_transaction_status

def test_valid_amount():
	assert validate_amount(100) == True

def test_invalid_amount():
	assert validate_amount(0) == False

def test_validate_card_number():
	assert validate_card_number(1234567890123456) == True

def  test_invalid_card_number():
	assert validate_card_number(123456) == False

def test_transaction_approved():
    assert get_transaction_status(100, 1234567890123456) == "APPROVED"

def test_transaction_declined_amount():
    assert get_transaction_status(0, 1234567890123456) == "DECLINED - Invalid amount"

def test_transaction_declined_card():
    assert get_transaction_status(100, 12345) == "DECLINED - Invalid card"
