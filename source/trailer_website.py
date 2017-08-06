import media
import fresh_tomatoes

# Movies to be shown in the page
ironman = media.Movie("Ironman",
                      "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=8hYlB38asDY&ab_channel=TheMovieChanneI")

limitless = media.Movie("Limitless",
                        "With the help of a mysterious pill that enables the user to access 100 percent of his brain abilities, a struggling writer becomes a financial wizard, but it also puts him in a new world with lots of dangers.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYmViZGM0MGItZTdiYi00ZDU4LWIxNDYtNTc1NWQ5Njc2N2YwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,692,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=vUkAfjfWh5g&ab_channel=eOnefilms")

lego_movie = media.Movie("The Lego Movie",
                         "An ordinary Lego construction worker, thought to be the prophesied 'Special', is recruited to join a quest to stop an evil tyrant from gluing the Lego universe into eternal stasis.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4MDk1ODExN15BMl5BanBnXkFtZTgwNzIyNjg3MDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "hhttps://www.youtube.com/watch?v=fZ_JOBCLF-I&ab_channel=WarnerBros.Pictures")

summer_wars = media.Movie("Summer Wars",
                          "A student tries to fix a problem he accidentally caused in OZ, a digital world, while pretending to be the fiance of his friend at her grandmother's 90th birthday.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYyOTk3OTQzM15BMl5BanBnXkFtZTcwMjU4NDYyNA@@._V1_SY1000_CR0,0,681,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=HjLE8BmWfKA&ab_channel=AwesomenessDreams")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "Danny Ocean and his eleven accomplices plan to rob three Las Vegas casinos simultaneously.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=imm6OR605UI&ab_channel=MovieStation")

scott_pilgrim = media.Movie("Scott Pilgrim vs. the World",
                            "Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkwNTczNTMyOF5BMl5BanBnXkFtZTcwNzUxOTUyMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=7wd5KEaOtm4&ab_channel=UniversalPictures")

# Putting the movies to an array so fresh_tomatoes can display them
movies = [ironman, limitless, lego_movie, summer_wars, oceans_eleven, scott_pilgrim]

# Create and open the movie page through fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
