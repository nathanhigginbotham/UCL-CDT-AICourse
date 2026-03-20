import ipywidgets as widgets
import random
from IPython.display import display


def run_quiz(questions):
    radio_buttons = []
    feedback_labels = []
    items = []

    for i, q in enumerate(questions):
        shuffled_options = random.sample(q["options"], len(q["options"]))
        label = widgets.HTML(f"<b>Q{i + 1}: {q['question']}</b>")
        rb = widgets.RadioButtons(options=shuffled_options, layout=widgets.Layout(width="100%"))
        feedback = widgets.HTML("")
        radio_buttons.append(rb)
        feedback_labels.append(feedback)
        items.append(widgets.VBox([label, rb, feedback, widgets.HTML("<br>")]))

    score_output = widgets.HTML("")

    def check_answers(b):
        score = 0
        for q, rb, feedback in zip(questions, radio_buttons, feedback_labels):
            if rb.value == q["answer"]:
                score += 1
                feedback.value = "<span style='color: green; font-size: 1.2em;'>✔ Correct!</span>"
            else:
                feedback.value = (
                    f"<span style='color: red; font-size: 1.2em;'>✘ Not quite.</span> "
                    f"The answer is: <b>{q['answer']}</b>"
                )
        if score == len(questions):
            summary = "Full marks - nice work!"
        elif score >= len(questions) // 2:
            summary = "Good effort - re-read any you missed and try again."
        else:
            summary = "Have another look through the lesson and try again."
        score_output.value = f"<br><b>Your score: {score} / {len(questions)}.</b> {summary}"

    submit = widgets.Button(description="Check answers", button_style="primary")
    submit.on_click(check_answers)
    display(widgets.VBox(items + [submit, score_output]))


def run_b02_quiz():
    questions = [
        {
            "question": "What is classification?",
            "options": [
                "Sorting data into groups",
                "Calculating the average of a dataset",
                "Drawing a scatter plot",
                "Counting the rows in a table"
            ],
            "answer": "Sorting data into groups"
        },
        {
            "question": "What are features?",
            "options": [
                "The measurements used to make a prediction",
                "The correct species label for each flower",
                "The number of training steps",
                "The accuracy score of the model"
            ],
            "answer": "The measurements used to make a prediction"
        },
        {
            "question": "Which model made better predictions on the test flowers?",
            "options": [
                "The trained model",
                "The untrained model",
                "They were exactly the same",
                "Neither model worked"
            ],
            "answer": "The trained model"
        },
        {
            "question": "What does accuracy measure?",
            "options": [
                "The percentage of predictions that were correct",
                "How fast the model trained",
                "The number of flowers in the dataset",
                "How many features the model used"
            ],
            "answer": "The percentage of predictions that were correct"
        }
    ]
    run_quiz(questions)


def run_b07_quiz():
    questions = [
        {
            "question": "How does a decision tree make predictions?",
            "options": [
                "By asking a series of yes/no questions about the data",
                "By calculating the average of all measurements",
                "By randomly guessing the answer",
                "By memorising every flower in the dataset"
            ],
            "answer": "By asking a series of yes/no questions about the data"
        },
        {
            "question": "What does the depth of a decision tree control?",
            "options": [
                "The maximum number of questions the tree can ask",
                "The number of flowers in the dataset",
                "The colour of the tree diagram",
                "How fast the tree trains"
            ],
            "answer": "The maximum number of questions the tree can ask"
        },
        {
            "question": "What is overfitting?",
            "options": [
                "When a model memorises training data and does worse on new data",
                "When a model is too simple to learn anything",
                "When you use too little training data",
                "When the test accuracy is higher than training accuracy"
            ],
            "answer": "When a model memorises training data and does worse on new data"
        },
        {
            "question": "What is a key advantage of decision trees over neural networks?",
            "options": [
                "You can see exactly how they make each decision",
                "They are always more accurate",
                "They don't need any training data",
                "They can only be used for flower classification"
            ],
            "answer": "You can see exactly how they make each decision"
        }
    ]
    run_quiz(questions)
