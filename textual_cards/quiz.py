from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, SelectionList
from textual_cards.question_model import Question
from textual.binding import Binding
from textual_cards.question_loader import load_questions
from textual.widgets.selection_list import Selection


class QuizApp(App):
    """A Textual app to ask questions."""

    BINDINGS = [
        Binding('n', 'skip', 'Next question/skip'),
        Binding(
            'Enter',
            'chec answer and go next',
        ),
        Binding('^C', 'exit'),
    ]
    question: Question = load_questions('tests/test_data/questions.md')

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(self.question.topic)
        yield SelectionList[int](
            *(Selection(choice, i) for i, choice in enumerate(self.question.choices))
        )

        yield Footer()

    def on_mount(self) -> None:
        self.query_one(SelectionList).border_title = 'Shall we play some games?'
