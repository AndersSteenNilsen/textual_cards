from textual.app import App, ComposeResult
from collections.abc import Iterable

from textual.widgets import Header, Footer, SelectionList
from textual_cards.question_model import Question
from textual.binding import Binding
from textual_cards.question_loader import load_questions
from textual.widgets.selection_list import Selection


class QuizApp(App):
    """A Textual app to ask questions."""

    BINDINGS = [
        Binding(key='n', action='skip', description='Next question/skip'),
        Binding(key='e', action='enter_answer()', description='Enter answer'),
        Binding(key='ctrl+q', action='quit', description='quit'),
    ]
    questions: Iterable[Question] = iter(load_questions('tests/test_data/questions.md'))
    question: Question = next(questions)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(self.question.topic)
        yield SelectionList[int](
            *(Selection(choice, i) for i, choice in enumerate(self.question.choices))
        )

        yield Footer()

    def on_mount(self) -> None:
        self.query_one(SelectionList).border_title = self.question.topic

    def action_enter_answer(self):
        self.query_one('SelectionList').remove()
        question: Question = next(self.questions)
        self.mount(
            SelectionList(
                *(Selection(choice, i) for i, choice in enumerate(question.choices))
            )
        )
        self.set_focus(self.query_one(SelectionList))
