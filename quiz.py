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

def run_b11_quiz():
    questions = [
        {
            "question": "What is Feature Construction?",
            "options": [
                "The process of extracting or summarising information (features) from raw data.",
                "Transforming skewed data into a bell curve.",
                "Creating a new neural network.",
                "Deleting all missing values."
            ],
            "answer": "The process of extracting or summarising information (features) from raw data."
        },
        {
            "question": "Why did we create the 'FamilySize' feature specifically?",
            "options": [
                "To capture the 'Social Context' with a single, stronger predicting number.",
                "To make the dataset smaller and easier to load.",
                "Because Neural Networks cannot read more than 3 columns.",
                "To count how many lifeboats were available."
            ],
            "answer": "To capture the 'Social Context' with a single, stronger predicting number."
        },
        {
            "question": "What does Standardization achieve in Step 5?",
            "options": [
                "It adjusts the scale of all numbers so the neural network treats them equally.",
                "It deletes all columns that don't follow standard rules.",
                "It sorts the passengers alphabetically by name.",
                "It adds 1 to every single number in the table."
            ],
            "answer": "It adjusts the scale of all numbers so the neural network treats them equally."
        },
        {
            "question": "In the Titanic project, what is the 'Target' we are trying to predict?",
            "options": [
                "Survival (Yes / No)",
                "The ticket Fare amount",
                "The passenger's Age",
                "How many siblings they had"
            ],
            "answer": "Survival (Yes / No)"
        }
    ]
    run_quiz(questions)
