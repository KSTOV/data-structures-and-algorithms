from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_round_bracket():
    assert validate_brackets("()") == True
    assert not validate_brackets("(") == False

def test_round_bracket_multi():
    assert validate_brackets("()()()") == True
    assert not validate_brackets("))(") == False

def test_curly_bracket():
    assert validate_brackets("{}") == True
    assert not validate_brackets("{") == False

def test_curly_bracket_multi():
    assert validate_brackets("{}{}{}") == True
    assert not validate_brackets("}}{") == False

def test_square_bracket():
    assert validate_brackets("[]") == True
    assert not validate_brackets("[") == False

def test_square_bracket_multi():
    assert validate_brackets("[][][]") == True
    assert not validate_brackets("]][[") == False
