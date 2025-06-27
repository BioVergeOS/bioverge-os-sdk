class Simulation:
    """
    A class for running biological simulations for a given species,
    parameters, environment, and optional chaos events.
    """
    def __init__(self, species, params, env):
        self.species = species
        self.params = params
        self.env = env
        self.chaos_events = []

    def apply_chaos(self, chaos):
        """
        Add a chaos event. See bioverge.chaos.CHAOS_EVENTS for options.
        """
        self.chaos_events.append(chaos)

    def run(self):
        """
        Run the simulation with current parameters and chaos modifiers.
        Returns a dict with results.
        """
        try:
            biomass = float(self.params.get("Initial Biomass (mg)", 100))
        except Exception:
            biomass = 100

        temp = self.env.get("Temperature", 22)
        humidity = self.env.get("Humidity", 65)
        ph = self.env.get("pH", 6.8)
        light = self.env.get("Light", 5000)
        co2 = self.env.get("CO2", 400)

        multiplier = (
            1.0
            + 0.01 * (temp - 22)
            + 0.005 * (humidity - 65)
            + (0.02 if 6.5 <= ph <= 7.5 else -0.05)
            + 0.00005 * (light - 5000)
            + 0.0001 * (co2 - 400)
        )

        for chaos in self.chaos_events:
            if chaos == "pest":
                multiplier *= 0.55
            elif chaos == "heat":
                multiplier *= 0.7
            elif chaos == "nutrient":
                multiplier *= 0.65
            elif chaos == "power":
                multiplier *= 0.8

        final_biomass = biomass * multiplier
        return {
            "species": self.species,
            "final_biomass": final_biomass,
            "params": self.params,
            "env": self.env,
            "chaos": self.chaos_events,
            "multiplier": multiplier,
        }
