from Matching import find_longest_match

def compress(text, search_buffer_size=13, lookahead_buffer_size=6):
    tags = []
    i = 0  
    n = len(text)
    
    while i < n:
        search_buffer_start = max(0, i - search_buffer_size)
        search_buffer = text[search_buffer_start:i]
        
        lookahead_buffer_end = min(n, i + lookahead_buffer_size)
        lookahead_buffer = text[i:lookahead_buffer_end]

        position, length = find_longest_match(search_buffer, lookahead_buffer)
        
        if i + length < n:
            next_symbol = text[i + length]
        else:
            next_symbol = None

        tag = (position, length, next_symbol)
        tags.append(tag)
        
        i += length + 1
        
    return tags

