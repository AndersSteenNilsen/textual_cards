from textual.app import App, ComposeResult
from collections.abc import Iterable

from textual.widgets import Header, Footer, SelectionList
from textual_cards.question_model import Question
from textual.binding import Binding
from textual_cards.question_loader import load_questions
from textual.containers import Container, Vertical
from textual.reactive import reactive
from textual.widgets.selection_list import Selection
from textual.widgets import Label, Static


class QuestionsWidget(Static):

    BINDINGS = [
        Binding(key='e', action='enter_answer()', description='Enter answer'),
    ]
    questions: Iterable[Question] = iter(load_questions('tests/test_data/questions.md'))
    active_question = reactive(next(questions))

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        with Vertical():
            yield Label(str(self.active_question.question))
            yield SelectionList(
                *(Selection(choice, i) for i, choice in enumerate(self.active_question.choices))
            )
    
    def action_enter_answer(self) -> None:
        self.active_question: Question = next(self.questions)
        self.question_text = self.active_question.question


    def on_mount(self) -> None:
        self.query_one(SelectionList).border_title = self.active_question.topic
    
    def watch_active_question(self, question:Question) -> None:
        label = self.query("Label")
        if label:
            label.first().update(question.question)
        
        question_list = self.query(SelectionList)
        if question_list:
            question_list.first().clear_options()
            question_list.first().add_options(Selection(choice, i) for i, choice in enumerate(self.active_question.choices))
        


class QuizApp(App):
    """A Textual app to ask questions."""

    BINDINGS = [
        Binding(key='ctrl+q', action='quit', description='quit'),
    ]


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        #questions: Iterable[Question] = iter(load_questions('tests/test_data/questions.md'))
        yield Header() 
        yield QuestionsWidget()
        yield Footer()


