""" Stores the information for the object instances to show on the website """
import media
import fresh_tomatoes

""" 
Creates six objects of the type Movie. Each of the objects will be intialized with the 
title, storyline, url to the movie poster and url to the movie's trailer in youtube. 
"""

lampoon_vacation = media.Movie("National Lampoon's Vacation",
                        "A family's road trip across the United States to visit a amusment park takes some WILD turns!",
                        "http://www.impawards.com/1983/posters/national_lampoons_vacation_xlg.jpg",
                        "https://www.youtube.com/watch?v=FHThGmVfE3A")

tommy_boy = media.Movie("Tommy Boy",
                     "A screw up has to save his father's company after his passing.",
                     "http://www.impawards.com/1995/posters/tommy_boy_xlg.jpg",
                     "https://www.youtube.com/watch?v=51f2rrYebKo")
                     
airborne = media.Movie("Airborne",
                      "Mitchell is moved to a new town and finds trouble and love",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BZmM4YzU2OWUtM2VkYy00Y2I5LTk3NzgtNmI3M2MyODM5YzY1XkEyXkFqcGdeQXVyMjA0MDQ0Mjc@._V1_UY1200_CR83,0,630,1200_AL_.jpg",
                      "https://www.youtube.com/watch?v=Mz2CMDCD3WQ")
                      

happy_gilmore = media.Movie("Happy Gilmore",
                      "A wannabe hockey pro finds a new calling in golf, to save his grandmother house.",
                      "http://img.moviepostershop.com/happy-gilmore-movie-poster-1996-1020189601.jpg",
                      "https://www.youtube.com/watch?v=y1emDAYCfVQ")

over_the_top = media.Movie("Over the Top",
                        "A struggling father arm wrestles to battle for the custody of his son",
                        "https://images-na.ssl-images-amazon.com/images/I/516LTiEXFRL.jpg",
                        "https://www.youtube.com/watch?v=l_qa_mLrQmY")

anchorman = media.Movie("Anchorman",
                      "A 70's Achorman was king, until a woman co-anchor challeged for the throne.",
                      "https://s-media-cache-ak0.pinimg.com/originals/c5/61/44/c561448d4b9360e83d91d62e9449866c.jpg",
                      "https://www.youtube.com/watch?v=NJQ4qEWm9lU")



# stores movies in a list to for the fresh_tomatoes.py 
movies = [over_the_top, airborne, tommy_boy, happy_gilmore, anchorman, lampoon_vacation]

# create HTML and opens the a website in the local default browser. It shows the movies listed above
fresh_tomatoes.open_movies_page(movies)
