"""
This module sets up the Flask application and defines routes.
"""

from flask import Flask, render_template, request, redirect, url_for
import json
import os
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def load_questions():
    """
    Load test questions from a JSON file.
    """
    with open(os.path.join(os.path.dirname(__file__), 'tests/test_questions.json')) as f:
        return json.load(f)

questions = load_questions()

# List of psychology quotes
quotes = [
    "The greatest discovery of my generation is that a human being can alter his life by altering his attitudes. - William James",
    "The mind is everything. What you think you become. - Buddha",
    "Knowing yourself is the beginning of all wisdom. - Aristotle",
    "The unexamined life is not worth living. - Socrates",
    "Your visions will become clear only when you can look into your own heart. Who looks outside, dreams; who looks inside, awakes. - Carl Jung"
]

@app.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/personality_test', methods=['GET', 'POST'])
def personality_test():
    """
    Display the personality test form and handle form submissions.
    """
    if request.method == 'POST':
        results = {}
        for question in questions:
            results[question['id']] = int(request.form.get(question['id']))
        
        scores, overall_score = calculate_scores(results)
        quote = random.choice(quotes)
        return render_template('results.html', scores=scores, overall_score=overall_score, quote=quote)

    return render_template('personality_test.html', questions=questions)

def calculate_scores(results):
    """
    Calculate detailed personality scores based on the test results.
    """
    trait_categories = {
        'extraversion': 0,
        'agreeableness': 0,
        'conscientiousness': 0,
        'neuroticism': 0,
        'openness': 0
    }

    # Assume each trait has 3 questions
    trait_question_count = 3

    for key, value in results.items():
        trait = key.split('_')[0]
        trait_categories[trait] += value

    overall_score = 0
    for trait in trait_categories:
        trait_categories[trait] = round((trait_categories[trait] / trait_question_count) * 20, 1)  # Scale to 100%
        overall_score += trait_categories[trait]

    overall_score = round(overall_score / len(trait_categories), 1)

    return trait_categories, overall_score

@app.route('/results')
def results():
    """
    Display the results of the personality test.
    """
    quote = random.choice(quotes)
    return render_template('results.html', quote=quote)

@app.route('/about')
def about():
    """
    Render the About Us page.
    """
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
