from textual_cards.quiz import QuizApp
from textual_cards.question_loader import load_questions

if __name__ == '__main__':
    questions = load_questions('tests/test_data/questions.md')
    app = QuizApp()
    app.run()
