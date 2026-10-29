# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_age.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: keblanch <keblanch@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/29 15:30:51 by keblanch          #+#    #+#             #
#    Updated: 2026/10/29 15:30:51 by keblanch         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plant_age():
    age: int = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
