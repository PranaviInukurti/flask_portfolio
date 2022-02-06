import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

randomadvice = []
randomadvice_list = [
    "Take time to know yourself.",
    "A narrow focus brings big results.",
    "Show up fully.",
    "Don't make assumptions and don't judge a book by its cover.",
    "Be patient, but persistent.",
    "In order to get, you have to give.",
    "Luck comes from hard work.",
    "Be your best at all times.",
    "Don't try to impress everyone because not everyone will like you regardless.",
    "Don't be afraid of being afraid.",
    "Listen in order to learn.",
    "Life's good, but it isn't fair.",
    "No task is beneath you.",
    "You can't always get what you want.",
    "Don't make decisions when you are angry or ecstatic.",
    "Don't worry what other people think.",
    "Use adversity as an opportunity.",
    "Do what is right, not what is easy.",
    "Dreams remain dreams until you take action.",
    "Treat others the way you want to be treated.",
    "When you quit, you fail.",
    "Trust you instincts, the worst enemy of success is self-doubt.",
    "Learn something new every day.",
    "Make what is valuable important.",
    "The way you see yourself is the way you treat yourself and the way you treat yourself is what you become, "
    "so believe in yourself.",
]


def _find_next_id():
    return max(randomadvice["id"] for randomadvice in randomadvice) + 1


def _init_randomadvice():
    id = 1
    for randomadvice in randomadvice_list:
        randomadvice.append({"id": id, "randomadvice": randomadvice, "Helpful": 0, "Not Helpful": 0})
        id += 1


@api_bp.route('/randomadvice')
def get_randomadvice():
    if len(randomadvice) == 0:
        _init_randomadvice()
    randomadvice = random.choice(randomadvice)
    return randomadvice


if __name__ == "__main__":
    print(random.choice(randomadvice))
