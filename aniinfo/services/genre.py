from aniinfo.dto.anime import ParsedAnime
from aniinfo.models.genre import Genre as GenreModel
from aniinfo.services.common import transliterate_from_uk


async def genres_by_parsed(anime: ParsedAnime) -> list[GenreModel]:
    parsed_genres = anime.genres
    genres = []
    for parsed_genre in parsed_genres:
        genre = await GenreModel.get_or_create(
            name=parsed_genre
        )
        genres.append(genre[0])
    return genres
