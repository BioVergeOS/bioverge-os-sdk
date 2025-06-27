SPECIES_LIST = [
    {"name": "Tomato", "params": ["Initial Biomass (mg)", "Leaf Count"]},
    {"name": "Corn", "params": ["Initial Biomass (mg)", "Height (cm)"]},
    {"name": "E. coli", "params": ["Initial OD600", "Medium Type"]},
    {"name": "Yeast", "params": ["Initial OD600", "Medium Type"]},
    {"name": "Mouse", "params": ["Initial Biomass (g)", "Age (weeks)", "Genotype"]},
    {"name": "Frog", "params": ["Initial Biomass (g)", "Development Stage"]},
    {"name": "Butterfly", "params": ["Initial Biomass (mg)", "Life Stage"]},
    {"name": "Strawberry", "params": ["Initial Biomass (mg)", "Runner Count"]},
    {"name": "Cactus", "params": ["Initial Biomass (mg)", "Spine Density"]},
    {"name": "Custom", "params": ["Describe parameters"]},
]

def get_species_params(species):
    for sp in SPECIES_LIST:
        if sp["name"].lower() == species.lower():
            return sp["params"]
    return []
