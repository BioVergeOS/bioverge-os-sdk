from bioverge.simulation import Simulation

# Example: run a tomato simulation with heat and nutrient chaos
sim = Simulation(
    species="Tomato",
    params={"Initial Biomass (mg)": 100, "Leaf Count": 3},
    env={"Temperature": 30, "Humidity": 70, "pH": 6.9, "Light": 6000, "CO2": 500}
)
sim.apply_chaos("heat")
sim.apply_chaos("nutrient")
result = sim.run()
print("Simulation result:", result)
