import json
from recommender import recommend_movies


def save_history(user, prefs, results):

    data = {
        "name": user,
        "preferences": prefs,
        "recommendations": results
    }

    try:
        with open(
            "user_data.json",
            "r"
        ) as file:

            history = json.load(file)

    except:
        history = []

    history.append(data)

    with open(
        "user_data.json",
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )


def main():

    print("=" * 50)
    print(" AI RECOMMENDATION SYSTEM ")
    print("=" * 50)

    user = input(
        "Enter your name: "
    )

    print(
        "\nEnter interests separated by comma"
    )

    print(
        "Example: Action,Sci-Fi"
    )

    user_input = input(
        "Your interests: "
    )

    preferences = [
        x.strip()
        for x in user_input.split(",")
    ]

    results = recommend_movies(
        preferences
    )

    print("\nRecommended Movies:")

    if results:

        for movie, score in results:
            print(
                f"{movie} "
                f"(Match Score: {score})"
            )

    else:
        print(
            "No recommendations found."
        )

    save_history(
        user,
        preferences,
        [movie for movie, _ in results]
    )

    print(
        "\nHistory Saved!"
    )


main()