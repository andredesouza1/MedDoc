from ST_sentence_match import sorted_sentence_pairs_by_output, sorted_sentence_pairs_by_score


def binary_search_score(target, arr):
    left = 0
    right = len(arr) - 1
    result_index = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # If the middle element is greater than or equal to the target,
        # update the result index and search on the left half.
        if arr[mid][2] >= target:
            result_index = mid
            right = mid - 1
        # If the middle element is less than the target, search on the right half.
        else:
            left = mid + 1
    
    return result_index


if __name__ == "__main__":
    print(len(sorted_sentence_pairs_by_score))
    
    min_score_index = binary_search_score(0.5, sorted_sentence_pairs_by_score)
    print(sorted_sentence_pairs_by_score[min_score_index:])

print(sorted_sentence_pairs_by_score[min_score_index:])

