from unittest import mock


def test_unvalidated_input(new_command):
    "If the user enters text and there's no validation, the text is returned"
    new_command.input.set_values('hello')

    value = new_command.input_text(
        intro="Some introduction",
        variable="my variable",
        default="goodbye"
    )

    assert new_command.input.prompts == ['My Variable [goodbye]: ']
    assert value == "hello"


def test_validated_input(new_command):
    "If the user enters text and there's validation, the user is prompted until valid text is entered"
    new_command.input.set_values('bad', 'hello')

    value = new_command.input_text(
        intro="Some introduction",
        variable="my variable",
        default="goodbye",
        is_valid=lambda text: text != 'bad'
    )

    assert new_command.input.prompts == [
        'My Variable [goodbye]: ',
        'My Variable [goodbye]: '
    ]
    assert value == "hello"


def test_input_with_default(new_command):
    "If the user enters text and there's no validation, the text is returned"
    new_command.input.set_values('')

    value = new_command.input_text(
        intro="Some introduction",
        variable="my variable",
        default="goodbye"
    )

    assert new_command.input.prompts == ["My Variable [goodbye]: "]
    assert value == "goodbye"


def test_prompt_capitalization(new_command):
    "The prompt is capitalized appropriately"
    new_command.input.set_values('hello')

    new_command.input_text(
        intro="Some introduction",
        variable="user's URL",
        default="goodbye"
    )

    assert new_command.input.prompts == ["User's URL [goodbye]: "]
