from textual_cards.question_model import Question
from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode

from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin


def load_questions(path: str) -> Question:
    content = open(path).read()
    md = (
        MarkdownIt('commonmark', {'breaks': True, 'html': True})
        .use(front_matter_plugin)
        .use(footnote_plugin)
        .enable('table')
    )
    md_nodes = md.parse(content)
    md_tree = SyntaxTreeNode(md_nodes)

    topic: str = md_tree.children[0].children[0].content
    question: str = md_tree.children[1].children[0].content
    choices_raw: list[str] = [
        n.children[0].children[0].content for n in md_tree.children[2].children
    ]
    choices = {}
    for choice in choices_raw:
        if '*' in choice:
            choices[choice.replace('*', '').strip()] = True
        else:
            choices[choice.strip()] = False
    return Question(topic, question, choices)
