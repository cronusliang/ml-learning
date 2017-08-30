import fresh_tomatoes
import movie

avatar =  movie.Movie("avatar","a story of a boy and his toys that come to life",
            "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
            "https://s3.cn-north-1.amazonaws.com.cn/u-vid-hd/MnDs5GF3AMs.mp4")


toy = movie.Movie("toy story","a story of a boy and his toys that come to life",
                   "https://en.wikipedia.org/wiki/Toy_Story_(franchise)#/media/File:Toy_Story_Toons_logo.png",
                   "https://www.youtube.com/watch?v=sarLaVnB1Eo")


moves = [avatar,toy]
fresh_tomatoes.open_movies_page(moves)