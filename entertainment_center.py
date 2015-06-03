import media
import favorites_movie

# Create movie instance
toy_story = media.Movie("Toy Story", "Toys Come to Life",
                        ("http://upload.wikimedia.org/wikipedia/"
                         "en/1/13/Toy_Story.jpg"),
                        "https://www.youtube.com/watch?t=17&v=vwyZH85NQC4",
                        "John Lasseter", "You've Got a Friend in Me")

life_is_beautiful = media.Movie("Life is Beautiful",
                                ("Story of Jewish Italian survivor"
                                 "of the Nazi death camps"),
                                ("http://www.gstatic.com/tv/thumb/"
                                 "movieposters/22005/p22005_p_v7_aa.jpg"),
                                "https://www.youtube.com/watch?v=3Y_p7KmAiLM",
                                "Roberto Benigni", "La vita e bella")

moulin_rouge = media.Movie("Moulin Rouge",
                           ("A celebration of love takes place in"
                            "the infamous Parisian nightclub"),
                           ("http://www.gstatic.com/tv/thumb/movies/"
                            "25691/25691_aa.jpg"),
                           "https://www.youtube.com/watch?v=dtEgAx80NC4",
                           "Baz Luhrmann", "Come What May")

saving_private = media.Movie("Saving Private Ryan",
                             ("Captain Miller takes his men behind enemy"
                              "lines to find Private Ryan"),
                             ("http://t2.gstatic.com/images?q=tbn:ANd9GcQ01Dc"
                              "S2fYHc9W3qTS8WHnAGaGNnMBOmhHKgfqvhYu4yICimnFw"),
                             "https://www.youtube.com/watch?v=RYExstiQlLc",
                             "Steven Spielberg", "Hymn To The Fallen")

matrix = media.Movie("The Matrix",
                     ("Neo believes that Morpheus, an elusive figure consider"
                      "ed to be the most dangerous man alive, can answer his"
                      "question -- What is the Matrix?"),
                     ("http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-"
                      "aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle"),
                     "https://www.youtube.com/watch?v=a94b1yZOBes",
                     "Andy Wachowski", "Rock Is Dead")

despicable_me = media.Movie("Despicable Me",
                            ("A man who delights in all things wicked, superv"
                                "illain Gru hatches a plan to steal the moon"),
                            ("http://t2.gstatic.com/images?q=tbn:ANd9GcStk75A_"
                                "FacVc2kXVb8vdTAU6x-fmRjV2X0-6yxHF5iksQmzKwB"),
                            "https://www.youtube.com/watch?v=fNPcZWsTgf0",
                            "Pierre Coffin", "Despicable Me")

# Create list of movie to show on the webpage
movies = [toy_story, life_is_beautiful, moulin_rouge,
          saving_private, matrix, despicable_me]

# Open webpage with a list of movies
favorites_movie.open_movies_page(movies)
