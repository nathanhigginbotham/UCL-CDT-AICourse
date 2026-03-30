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
            "question": "What does feature engineering mean?",
            "options": [
                "Creating new features or transforming existing ones to make better models",
                "Buying faster computers to train models",
                "Deleting data we don't like",
                "Drawing diagrams"
            ],
            "answer": "Creating new features or transforming existing ones to make better models"
        },
        {
            "question": "Why would we create a new variable like Rooms_Per_Person?",
            "options": [
                "Because the model couldn't figure out the relationship as easily from the separate numbers",
                "To make the table larger so the model complains less",
                "Because computers require at least 10 columns to run",
                "Because average rooms wasn't a number"
            ],
            "answer": "Because the model couldn't figure out the relationship as easily from the separate numbers"
        },
        {
            "question": "Why might we log-transform a feature like Population?",
            "options": [
                "To squish extreme outliers so they don't confuse the model",
                "To delete the population column safely",
                "Because population isn't real",
                "To change words into numbers"
            ],
            "answer": "To squish extreme outliers so they don't confuse the model"
        },
        {
            "question": "What happens when our engineered features are good?",
            "options": [
                "The model's predictions get more accurate (error goes down)",
                "The computer breaks",
                "We get a 100% error rate",
                "The model runs slower but predicts worse"
            ],
            "answer": "The model's predictions get more accurate (error goes down)"
        }
    ]
    run_quiz(questions)
