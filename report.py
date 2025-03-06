

def print_count_report( file_name, word_count, char_list ):
    print( "============ BOOKBOT ============" );
    print( f"Analyzing book found at {file_name}..." );
    print( "----------- Word Count ----------" );
    print( f"Found {word_count} total words" );
    print( "--------- Character Count -------" );
    for this_char in char_list:
        if this_char["letter"].isalpha():
            print( f"{this_char["letter"]}: {this_char["count"]}" );
    print( "============= END ===============" );
    return;



