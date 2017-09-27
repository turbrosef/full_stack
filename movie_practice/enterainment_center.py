import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy who's toys come alive",
						"http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline, toy_story.title)

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(avatar.storyline)

# media.Movie.show_trailer(avatar) works the same as below
# avatar.show_trailer()


movies = [toy_story, avatar]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)