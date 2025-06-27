# BioVerge OS SDK

A developer toolkit for running, analyzing, and extending biological simulations on-chain or off-chain.

- Run digital biology experiments programmatically
- Apply environmental and chaos factors
- Expand with NFT and IPFS utilities

## Example

```python
from bioverge.simulation import Simulation
sim = Simulation("Tomato", {"Initial Biomass (mg)": 120}, {"Temperature": 28, "Humidity": 60, "pH": 6.7, "Light": 5500, "CO2": 450})
sim.apply_chaos("pest")
result = sim.run()
print(result)
```

## Installation

```bash
pip install bioverge-os-sdk
```

## License

MIT
