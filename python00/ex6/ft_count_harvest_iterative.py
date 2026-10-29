# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: keblanch <keblanch@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/29 16:11:13 by keblanch          #+#    #+#             #
#    Updated: 2026/10/29 16:11:13 by keblanch         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    i: int
    for i in range(days):
        print(f"Day {i + 1}")
    print("Harvest time!")
