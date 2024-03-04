from textual_cards.question_loader import load_questions
from textual_cards.question_model import Question


def test_load_questions():
    """Test load_questions function."""
    expected = Question(
        topic='TOPIC',
        question='Multiple choice',
        choices={'Green 💚': False, 'Red ❤️': True, 'Blue 💙': False},
    )
    assert load_questions('tests/test_data/questions.md') == expected
