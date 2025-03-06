
# from stats import get_num_words
# from stats import get_nr_characters
import stats
import report
import sys


def get_book_text( file_name ):
    with open( file_name ) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read();
    return file_contents;


def main():
    if len(sys.argv) < 2:
        print( f"Usage: python3 main.py <path_to_book>");
        sys.exit(1);
    # book_file_name = "./books/frankenstein.txt";
    book_file_name = sys.argv[1];
    file_contents =  get_book_text( book_file_name );
    #print( file_contents );
    nr_words = stats.get_num_words( file_contents );
    # print( f"{nr_words} words found in the document");
    char_dict = stats.get_nr_characters( file_contents );
    # print( f"{char_dict}" );
    sorted_dict = stats.sort_dict_by_count( char_dict );
    report.print_count_report( book_file_name, nr_words, sorted_dict );


main();

