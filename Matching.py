def find_longest_match(search_buffer, lookahead_buffer):
    best_position = 0
    best_length = 0

    # Try every possible position in the Search Buffer
    for distance in range(1, len(search_buffer) + 1):

        length = 0

        # Compare with the Look-Ahead Buffer
        while length < len(lookahead_buffer):

            start_index = len(search_buffer) - distance

            # Allow overlapping matches
            source_index = start_index + (length % distance)

            if search_buffer[source_index] != lookahead_buffer[length]:
                break

            length += 1

        # Keep the longest match
        if length > best_length:
            best_length = length
            best_position = distance

    return best_position, best_length