# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: keblanch <keblanch@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/29 16:11:49 by keblanch          #+#    #+#             #
#    Updated: 2026/10/29 16:11:49 by keblanch         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def rec_harvest(day: int) -> None:
    if day > 1:
        rec_harvest(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    rec_harvest(int(input("Days until harvest: ")))
    print("Harvest time!")
