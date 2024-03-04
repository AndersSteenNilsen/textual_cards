from dataclasses import dataclass


@dataclass
class Question:
    topic: str
    question: str
    choices: dict[str, bool]
