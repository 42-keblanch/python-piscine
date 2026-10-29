# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_water_reminder.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: keblanch <keblanch@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/29 16:05:11 by keblanch          #+#    #+#             #
#    Updated: 2026/10/29 16:05:11 by keblanch         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    days: int = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
