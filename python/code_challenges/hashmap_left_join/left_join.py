def left_join(hash_1, hash_2):
    combined_hash = []

    for key in hash_1:
        combined_hash.append(key)
        combined_hash.append(hash_1[key])

        if key in hash_2:
            combined_hash.append(hash_2[key])
        else:
            combined_hash.append(None)
    return combined_hash
