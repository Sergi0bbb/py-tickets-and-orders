from django.db.models import QuerySet

from db.models import MovieSession


def create_movie_session(
    movie_show_time: str, movie_id: int, cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id,
    )


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: str | None = None,
    movie_id: int | None = None,
    cinema_hall_id: int | None = None,
) -> None:
    movie_session = MovieSession.objects.get(pk=session_id)
    if show_time:
        movie_session.show_time = show_time
    if movie_id:
        movie_session.movie_id = movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id
    movie_session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(pk=session_id).delete()


def get_taken_seats(movie_session_id: int) -> list[dict]:
    return list(
        get_movie_session_by_id(movie_session_id)
        .tickets.values("row", "seat")
    )
