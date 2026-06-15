from logic_utils import check_guess, parse_guess

# --- Existing tests (fixed: check_guess returns a tuple, not a plain string) ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Glitch 2: check_guess hint messages were swapped ---

def test_too_high_hint_says_go_lower():
    # Guess is above secret — player needs to go lower, not higher
    _, message = check_guess(80, 50)
    assert "LOWER" in message, f"Expected 'LOWER' in hint, got: {message}"

def test_too_low_hint_says_go_higher():
    # Guess is below secret — player needs to go higher, not lower
    _, message = check_guess(20, 50)
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint, got: {message}"


# --- Glitch 1: parse_guess missing range check ---

def test_parse_guess_above_100_is_rejected():
    ok, value, err = parse_guess("101")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_below_1_is_rejected():
    ok, _, _ = parse_guess("0")
    assert ok is False

def test_parse_guess_negative_is_rejected():
    ok, _, _ = parse_guess("-5")
    assert ok is False

def test_parse_guess_boundary_1_is_valid():
    ok, value, err = parse_guess("1")
    assert ok is True
    assert value == 1
    assert err is None

def test_parse_guess_boundary_100_is_valid():
    ok, value, err = parse_guess("100")
    assert ok is True
    assert value == 100
    assert err is None

def test_parse_guess_empty_string_is_rejected():
    ok, _, _ = parse_guess("")
    assert ok is False

def test_parse_guess_non_number_is_rejected():
    ok, _, err = parse_guess("abc")
    assert ok is False
    assert err is not None

def test_parse_guess_decimal_is_accepted():
    # "5.7" should parse as int 5, not be rejected
    ok, value, err = parse_guess("5.7")
    assert ok is True
    assert value == 5
