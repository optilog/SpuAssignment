def parse_spu(instance):
    """Software Package Upgrades (SPU) instance parser.

    Basic parser for the SPU described in the example.

    :param instance: Input instance to be parsed
    :type instance: str | pathlib.Path
    :raises ValueError: When some error in the parsed file is found.
    :raises ValueError: _description_
    :raises ValueError: _description_
    :return: Number of packages, list of packages' names and dictionary
        with dependencies and conflicts.
    :rtype: (int, List[int], Dictionary)
    """

    n_pckgs = -1
    pckgs = []
    pckgs_dict = {}

    with open(instance, "r") as fh:
        for line in fh.readlines():
            l = line.strip().split()
            if l[0] == "p":
                # Header
                n_pckgs = int(l[2])
            elif l[0] == "n":
                # Packages
                pckgs.append(l[1])
                pckgs_dict[l[1]] = {"d": [], "c": []}
            elif l[0] == "d":
                try:
                    pckgs_dict[l[1]]["d"].append(l[2:])
                except KeyError:
                    raise ValueError(f"Package {l[1]} not declared")
            elif l[0] == "c":
                try:
                    pckgs_dict[l[1]]["c"].append(l[2])
                except KeyError:
                    raise ValueError(f"Package {l[1]} not declared")
            elif l[0] == "#":
                pass
            else:
                print(f"Unknown line: '{line}'")

    if len(set(pckgs)) != n_pckgs:
        raise ValueError(
            f"Wrong number of packages. Header: {n_pckgs}; Real: {set(pckgs)}"
        )

    return n_pckgs, pckgs, pckgs_dict
