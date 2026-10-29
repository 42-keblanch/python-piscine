# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_harvest_total.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: keblanch <keblanch@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/29 15:24:37 by keblanch          #+#    #+#             #
#    Updated: 2026/10/29 15:27:04 by keblanch         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    harvest: int = 0
    harvest += int(input("Day 1 harvest: "))
    harvest += int(input("Day 2 harvest: "))
    harvest += int(input("Day 3 harvest: "))
    print(f"Total Harvest: {harvest}")
