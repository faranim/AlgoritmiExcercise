def get_pairs(number_list):
    Queues = (Queue(), Queue())
    pairs = []
    for number in number_list:
        this_type = number % 2
        other_type = (1, 0)[this_type]
        if len(Queues[this_type]) == 0:
            other = Queues[other_type].dequeue()
            if other is not None:
                pairs.append((other, number) if this_type else (number, other))
                continue
        Queues[this_type].enqueue(number)
    return pairs