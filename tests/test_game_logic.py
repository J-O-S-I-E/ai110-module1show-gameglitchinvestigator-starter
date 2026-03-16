from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

# FIX: Added test for string inputs to prevent type inconsistency regression; created with AI assistance
def test_guess_handles_string_inputs():
    # This test targets the bug where secret was sometimes str, causing wrong comparisons
    # Now, with int conversion, it should work regardless of input type
    result = check_guess("60", 50)
    assert result == ("Too High", "📉 Go LOWER!")

    result = check_guess(60, "50")
    assert result == ("Too High", "📉 Go LOWER!")

    result = check_guess("60", "50")
    assert result == ("Too High", "📉 Go LOWER!")
