from entities.veterinarians.validations import is_valid_matricula, is_valid_name

"""
    If the Matricula has valid format returns True
"""
def test_is_valid_matricula():
    mock_matriula = "MN12345"
    
    result = is_valid_matricula(mock_matriula)
    
    assert result == True

"""
    If the Matricula has invalid format returns False
"""
def test_is_valid_matricula():
    mock_matriula = "M12345"
    
    result = is_valid_matricula(mock_matriula)
    
    assert result == False
    
"""
    If the Matricula has more than 5 digits returns False
"""
def test_is_valid_matricula():
    mock_matriula = "MN1234567"
    
    result = is_valid_matricula(mock_matriula)
    
    assert result == False
    
"""
    If the Matricula doesn't start with MN returns False
"""
def test_is_valid_matricula():
    mock_matriula = "1MN2345"
    
    result = is_valid_matricula(mock_matriula)
    
    assert result == False
    
"""
    If the name has valid format returns True
"""
def test_is_valid_name():
    mock_name = "Lucas"
    
    result = is_valid_name(mock_name)
    
    assert result == True
"""
    If the name has valinvalidid format returns False
"""
def test_is_valid_name():
    mock_name = "Lucas12344"
    
    result = is_valid_name(mock_name)
    
    assert result == False