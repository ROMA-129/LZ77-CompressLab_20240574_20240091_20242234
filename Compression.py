from Matching import find_longest_match   
#define compress function with fixed sliding window for optimal search speed
def compress(text, search_buffer_size=13, lookahead_buffer_size=6):
    tags = []  
    i = 0  
    n = len(text) 
    
    while i < n: 
        search_buffer_start = max(0, i - search_buffer_size) 
        search_buffer = text[search_buffer_start:i] #slice and extract the search window from the text
        
        lookahead_buffer_end = min(n, i + lookahead_buffer_size) 
        lookahead_buffer = text[i:lookahead_buffer_end] #slice upcoming characters to look for matches 
        
        position, length = find_longest_match(search_buffer, lookahead_buffer) 
        
        if i + length < n:
            next_symbol = text[i + length]
            tag = (position, length, next_symbol)
            i+=length+1
        else:
            next_symbol = None
            tag = (position, length, next_symbol)
            i+=length

        tags.append(tag)
        
    return tags

