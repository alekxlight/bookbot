
def get_num_words( file_contents ):
    word_list = file_contents.split( );
    return len(word_list);



def get_nr_characters( string_contents ):
    char_dict = {};
    for i in range( 0, len(string_contents) ):
        this_char = string_contents[i].lower();
        if this_char in char_dict:
            char_dict[this_char] += 1;
            continue;
        char_dict[this_char] = 1;
    return char_dict;

def sort_on(dict):
    return dict["count"]

def sort_dict_by_count( char_dict ):
    # print( f"{char_dict}")
    raw_list = [ ];
    for this_letter in char_dict:
        new_item = { "letter": this_letter, "count": char_dict[this_letter]  };
        raw_list.append( new_item );
    # print( f"{raw_list}" )
    raw_list.sort( reverse=True, key=sort_on );
    return raw_list;



    