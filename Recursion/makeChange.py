def make_change(coins, change, know_change_num, min_coins_list):
    min_coins_num = change
    if change in coins:
        min_coins_list[change] = change
        know_change_num[change] = 1
        return 1
    elif know_change_num[change] > 0:
        return know_change_num[change]
    else:
        for i in [c for c in coins if c <= change]:
            coins_num = 1 + make_change(coins, change - i, know_change_num, min_coins_list)
            if coins_num < min_coins_num:
                min_coins_num = coins_num
                min_coins_list[change] = i
            elif coins_num == min_coins_num and min_coins_list[change] == 0:
                min_coins_list[change] = i
            know_change_num[change] = min_coins_num
        return min_coins_num


def get_changes(change, min_coins_list):
    changes_value_list = []
    while change > 0:
        changes_value_list.append(min_coins_list[change])
        change -= min_coins_list[change]
    return changes_value_list


def main():
    coins = [1, 5, 10, 20]
    change = 27
    know_change_num = [0] * 28
    min_coins_list = [0] * 28

    print('Coins value: ' + str(coins)[1: -1])
    print('Change money: ' + str(change))
    print('Change number: ' + str(make_change(coins, change, know_change_num, min_coins_list)))
    print('Changes value: ' + str(get_changes(min_coins_list, change))[1:-1])
    print('Minimum change number list: ' + str(know_change_num))
    print('Minimum change table: ' + str(min_coins_list))


if __name__ == '__main__':
    main()
