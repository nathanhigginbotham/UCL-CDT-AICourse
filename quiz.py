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


def run_b05_quiz():
    questions = [
        {
            "question": "What is data splitting?",
            "options": [
                "Dividing a dataset into a training set and a testing set",
                "Deleting data that the model found too difficult",
                "Breaking long code lines into multiple parts",
                "Replacing numbers with categories"
            ],
            "answer": "Dividing a dataset into a training set and a testing set"
        },
        {
            "question": "Why is testing on the same data a model trained on a problem?",
            "options": [
                "The model can cheat by memorizing the data",
                "It takes too much time to run",
                "The model might learn the wrong pattern",
                "Testing must always be done on less data"
            ],
            "answer": "The model can cheat by memorizing the data"
        },
        {
            "question": "What happens to a model's accuracy when tested on new, unseen data?",
            "options": [
                "It usually goes down because making new predictions is harder",
                "It usually goes up because the model likes new data",
                "It always STAYS at exactly 100%",
                "It always drops to exactly 0%"
            ],
            "answer": "It usually goes down because making new predictions is harder"
        },
        {
            "question": "What does generalisation mean?",
            "options": [
                "A model's ability to make good predictions on new, unseen data",
                "Training the model on every single piece of data",
                "Using the same model for everything",
                "Ignoring differences in the data"
            ],
            "answer": "A model's ability to make good predictions on new, unseen data"
        }
    ]
    run_quiz(questions)

