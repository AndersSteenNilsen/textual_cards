from textual_cards.question_loader import load_questions
from textual_cards.question_model import Question


def test_load_questions():
    """Test load_questions function."""
    first_expected = Question(
        topic='Programming languages',
        question='What does the acronym "API" stand for?',
        choices={
            'Application Programming Interface': True,
            'Advanced Programming Interface': False,
            'Automated Programming Instruction': False,
            'Application Process Integration': False,
        },
    )
    assert load_questions('tests/test_data/questions.md')[0] == first_expected
    assert len(load_questions('tests/test_data/questions.md')) == 9
