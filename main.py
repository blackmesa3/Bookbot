from stats import get_book_cc
from stats import get_book_wc
from stats import dicksorter
def get_book_text(filepath):
    with open(filepath) as f:
        Text = f.read() 
    return Text  
def main():
    import sys
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    directory = sys.argv[1]
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at "+ directory +"...")
    print ("----------- Word Count ----------")
    print ("Found " +get_book_wc(directory)+ " total words")
    print ("--------- Character Count -------")
    temp = (get_book_cc(directory))
    dicksorter(temp)
    return 

main()

