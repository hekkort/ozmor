# 🐻 Gravetooth Bears

![Gravetooth Bear](/images/gravetooth-bear.png)

## Keepers of the Crumbling Valleys

Towering over men, the Gravetooth Bears are named for the jagged crystal formations growing from their jaws. Their roars echo for miles, capable of shaking boulders loose from cliff faces. Despite their fearsome appearance, they are fiercely territorial rather than bloodthirsty.

> "When the valleys grumble, tread lightly — the Gravetooth watches." — *Ranger's Field Journal*

---

## Known Traits

- Often mistaken for small landslides at a distance.
- Worshipped by some valley-dwelling tribes.
- Hibernate within crystal dens during frost moons.
- Roars can trigger rockfalls and minor seismic activity.
- Crystals on their jaws resonate with leyline vibrations.

---

## Additional Lore

Gravetooth Bears are believed to be descendants of an ancient earth-spirit, bound to the land by the druids of the **Second Cycle**. The crystals in their jaws grow with age and serve as a measure of both status and power. Some claim these crystals absorb echoes — and when broken, they release the bear’s memories in haunting roars.

Valley tribes refer to them as **“Echo-Keepers”**, and perform rites during tremors to appease their unseen presence. Breaking a Gravetooth crystal is considered a grievous sin, punishable by exile.

In rare cases, old Gravetooth dens have been found containing **petrified cubs encased in quartz**, untouched by time. One such den, discovered near the ruined Monastery of Qor, was said to cause madness in those who entered without offering a blood-tithe.

Elders of the **Stonewoven Order** suggest Gravetooth Bears are not animals at all, but avatars of the mountains themselves — only animated when balance is threatened. Their appearance often coincides with landslides that uncover forgotten ruins or relics best left buried.

---

## Timeline of Notable Encounters

- **-318 A.S.** — The valley of Tharn collapses; tribe elder speaks of a “crystal roar” before his death.
- **-121 A.S.** — Blood-tithe rituals documented in Qorran scrolls.
- **22 A.S.** — Ranger Ayla survives a Gravetooth encounter by mimicking bear song with a crystal flute.
- **267 A.S.** — Seismologists detect synchronized roars across three valleys during leyline surge.
- **489 A.S.** — Monastery of Qor expedition ends in madness; only the scribe's hand remained, clutching quartz.

---

## Bestiary Entry

> *Class*: Elemental Beast  
> *Habitat*: Mountain valleys, crystal caves, faultline crossings  
> *Temperament*: Defensive, dormant unless provoked or threatened  
> *Threat Level*: Variable (low when hibernating, extreme during territory defense)  
> *Interaction Protocol*: Do not break ground crystals; use low-frequency flutes to signal peace.

---

## GravetoothBear Class (Python)

```python
import random
class GravetoothBear:
    def __init__(self, name="Unnamed Bear", crystal_age=100):
        self.name = name
        self.crystal_age = crystal_age  # Represents years of growth
        self.asleep = True
        self.roar_resonance = crystal_age * 0.3  # Impact potential
    def awaken(self, disturbance_level):
        """Determines if the bear awakens from hibernation."""
        if disturbance_level > 7:
            self.asleep = False
            return f"{self.name} has awakened with a thunderous rumble!"
        return f"{self.name} stirs, but remains dormant."
    def roar(self):
        """Simulates a roar with seismic effects."""
        if self.asleep:
            return f"{self.name} is silent within the crystal den."
        damage = self.roar_resonance * random.uniform(1.0, 2.5)
        return f"{self.name} roars! The valley trembles with a force of {damage:.2f} units."
    def crystal_break(self):
        """Breaks a crystal and unleashes a memory."""
        if self.crystal_age < 50:
            return "A faint growl is heard... but no clear memory escapes."
        return f"A haunting roar echoes from the broken crystal — a memory of {self.name}'s battle with sky-raiders long ago."
    def offer_ritual(self, item):
        """Attempts to calm the bear with a ritual offering."""
        accepted_items = ["blood-tithe", "valley gem", "crystal flute"]
        if item in accepted_items:
            return f"{self.name} senses the offering and returns to slumber."
        return f"{self.name} rejects the offering. The ground begins to quake..."
```
# Example usage
```
bear = GravetoothBear(name="Thrumjaw", crystal_age=230)
print(bear.awaken(disturbance_level=9))
print(bear.roar())
print(bear.crystal_break())
```
