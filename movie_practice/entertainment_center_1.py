import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
                     
airborne = media.Movie("Airborne",
                      "Mitchell is moved to a new town and finds trouble and love",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BZmM4YzU2OWUtM2VkYy00Y2I5LTk3NzgtNmI3M2MyODM5YzY1XkEyXkFqcGdeQXVyMjA0MDQ0Mjc@._V1_UY1200_CR83,0,630,1200_AL_.jpg",
                      "https://www.youtube.com/watch?v=Mz2CMDCD3WQ")
                      

happy_gilmore = media.Movie("Happy Gilmore",
                      "A wannabe hockey pro finds a new calling in golf, to save his grandmother house.",
                      "http://img.moviepostershop.com/happy-gilmore-movie-poster-1996-1020189601.jpg",
                      "https://www.youtube.com/watch?v=y1emDAYCfVQ")


#print(airborne.title)
#print( airborne.storyline)
#airborne.show_poster()
#airborne.show_trailer()

movies = [toy_story, avatar, airborne, happy_gilmore]

fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print("show documentation about the class Movie:" + media.Movie.__doc__)
print("name: " + media.Movie.__name__)
print("module: " + media.Movie.__module__)

