from Meals.models import Meal, Order
from django.contrib.auth.models import User
from collections import Counter

NUMBER_OF_SUGGESTIONS = 5


def recommend(main_user: User, users: list[User]) -> list[Meal]:
    """
    Returns a defined number of suggestions for given user
    """
    current_best_user = None
    current_best_coef = 0
    main_user_meals = get_user_meals(main_user)
    for user in users:
        if user == main_user:
            continue
        coefficient = calculate_coefficient(main_user_meals, user)
        if coefficient > current_best_coef:
            current_best_coef = coefficient
            current_best_user = user

    if current_best_user is None:
        return get_most_popular_meals(NUMBER_OF_SUGGESTIONS)

    best_user_meals = get_user_meals(current_best_user)
    # meals ordered by the other user and not ordered by main user
    suggestions = [item for item in best_user_meals if item not in main_user_meals]
    suggestions = suggestions + get_most_popular_meals(NUMBER_OF_SUGGESTIONS - len(suggestions))
    return suggestions[0:NUMBER_OF_SUGGESTIONS]


def calculate_coefficient(meals_a, user: User) -> int:
    meals_b = get_user_meals(user)
    coefficient = 0
    for meal_id in meals_a:
        if meal_id in meals_b:
            coefficient += 1
    return coefficient


def get_user_meals(user: User):
    """
    Returns a set containing meals ordered by the user
    In a set every meal occurs once even if was ordered many times by the user
    """
    orders = Order.objects.filter(user_id=user)
    meals = [order.meal_id for order in orders]
    return set(meals)


def get_most_popular_meals(n: int) -> list[Meal]:
    """
    Returns list of n most popular meals in all database
    ordered by number of occurrences
    """
    orders = Order.objects.all()
    meals = [order.meal_id for order in orders]
    count = Counter(meals).most_common(n)
    most_common_meals = [item[0] for item in count]     # you don't have to understand, just believe
    return most_common_meals
