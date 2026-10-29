# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plot_area.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: keblanch <keblanch@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/29 15:29:22 by keblanch          #+#    #+#             #
#    Updated: 2026/10/29 15:29:22 by keblanch         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
