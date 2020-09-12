def get_indices_of_item_weights(weights, length, limit):
    seen = {}
    for idx, weight in enumerate(weights):
        if (limit - weight) in seen:
            return sorted((seen[limit - weight], idx), reverse=True)
        seen[weight] = idx

    return None
