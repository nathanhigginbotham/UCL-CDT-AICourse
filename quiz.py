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


def run_b09_quiz():
    questions = [
        {
            "question": "What is the primary function of a hidden layer in a neural network?",
            "options": [
                "To receive data from the outside world",
                "To extract complex patterns between inputs and outputs",
                "To define the final output category",
                "To scale the raw features"
            ],
            "answer": "To extract complex patterns between inputs and outputs"
        },
        {
            "question": "What does a 'Loss Function' tell the model?",
            "options": [
                "How many neurons are in the network",
                "How far its prediction is from the correct target",
                "The exact values of the weights",
                "The speed of the training processor"
            ],
            "answer": "How far its prediction is from the correct target"
        },
        {
            "question": "Which of these components is responsible for 'driving' the weight updates based on the loss?",
            "options": [
                "The Activation Function",
                "The Dataset",
                "The Optimizer",
                "The Features"
            ],
            "answer": "The Optimizer"
        },
        {
            "question": "In our Iris experiment, why did the 'Deep Network' often perform better than the 'SLP'?",
            "options": [
                "It had 16 times as much data",
                "It was running on a faster computer",
                "The hidden layer allowed it to learn more complex relationships",
                "It didn't use an activation function"
            ],
            "answer": "The hidden layer allowed it to learn more complex relationships"
        },
        {
            "question": "If the Loss curve stays flat during training, what might be happening?",
            "options": [
                "The model is learning perfectly",
                "The model is not learning because weights aren't being adjusted effectively",
                "The model has already reached 100% accuracy",
                "The dataset is too small"
            ],
            "answer": "The model is not learning because weights aren't being adjusted effectively"
        }
    ]
    run_quiz(questions)


def run_b10_quiz():
    questions = [
        {
            "question": "What are 'RGB Channels' in an image?",
            "options": [
                "Three layers of colour: Red, Green, and Blue",
                "Three sizes of pictures",
                "Three different AI models",
                "Three types of cameras"
            ],
            "answer": "Three layers of colour: Red, Green, and Blue"
        },
        {
            "question": "A CIFAR-10 image is 32x32 pixels with 3 colour channels. How many numbers make up one image?",
            "options": [
                "32",
                "96",
                "1,024",
                "3,072"
            ],
            "answer": "3,072"
        },
        {
            "question": "What is the main advantage of a CNN for image tasks like CIFAR-10?",
            "options": [
                "It is faster but less accurate",
                "It preserves the spatial patterns in the 2D grid",
                "It only works on black and white images",
                "It doesn't use any convolutional filters"
            ],
            "answer": "It preserves the spatial patterns in the 2D grid"
        },
        {
            "question": "How does a CNN find shapes like wheels or wings?",
            "options": [
                "By sorting the pixels alphabetically",
                "By sliding 'filters' or 'kernels' across the image",
                "By making the whole image one colour",
                "By only looking at the very first pixel"
            ],
            "answer": "By sliding 'filters' or 'kernels' across the image"
        },
        {
            "question": "Which of these models dropped its error (Loss) faster in our experiment?",
            "options": [
                "The Linear (Flat) model",
                "The CNN model",
                "They were exactly the same",
                "Neither model worked"
            ],
            "answer": "The CNN model"
        }
    ]
    run_quiz(questions)
