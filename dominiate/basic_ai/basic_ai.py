def buying_value(coins, buys):
    if coins > buys * 8: coins = buys * 8
    if (coins - (buys - 1) * 8) in (1, 7):  # there exists a useless coin
        coins -= 1
    return coins
