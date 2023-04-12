import wikipedia
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--movie', help='Provide the movie name')
args = parser.parse_args()

def get_movie_plot(movie: str):
    try:
        plot = wikipedia.page(movie).content

        start_index = plot.index('== Plot ==')
        end_index = plot.index('== Cast ==')
        return plot[start_index+10 : end_index]
    except wikipedia.exceptions.PageError:
        return 'Page not found'


if __name__=='__main__':
    print(get_movie_plot(args.movie))