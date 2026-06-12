from dataset import movies


def recommend_movies(user_preferences):

    recommendations = []

    for movie in movies:

        score = len(
            set(user_preferences) &
            set(movie["genre"])
        )

        if score > 0:
            recommendations.append(
                (movie["name"], score)
            )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations