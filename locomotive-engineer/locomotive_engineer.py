import warnings 
warnings.filterwarnings("ignore")
"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(wagon)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    a , c , d , *_ = each_wagons_id
    list_of_wagons = d, *missing_wagons, *_, a, c
    return list(list_of_wagons)



def add_missing_stops(route , **args):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops = list(args.values())
    route["stops"] = stops
    return route




def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    z = {**route , **more_route_information}
    return z


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    transpose = [list(row) for row in zip(*wagons_rows)]
    return transpose


