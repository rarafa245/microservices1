from .validator import Message_Validator

def test_check_message():
    conf = {
        'name': 'Rafa',
        'age': 10
    }

    message_validator = Message_Validator()
    response = message_validator.check_message(conf)
    print(response)

    assert response == True
