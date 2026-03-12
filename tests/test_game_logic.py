from logic_utils import check_guess
#FIX: Added test cases to see if new features worked
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_direction_not_backwards():
    # A high guess should tell the user to go lower, and a low guess should say higher.
    high_outcome, high_message = check_guess(60, 50)
    low_outcome, low_message = check_guess(40, 50)

    assert high_outcome == "Too High"
    assert "LOWER" in high_message.upper()

    assert low_outcome == "Too Low"
    assert "HIGHER" in low_message.upper()
