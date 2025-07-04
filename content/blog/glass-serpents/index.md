# 🐍 Glass Serpents

![Glass Serpent](/images/glass-serpent.png)

## The Unseen Dangers

Almost invisible against stone and sky, Glass Serpents are thin, translucent reptiles that coil around the high spires of Lorithal. They rely on vibration and heat to detect prey. Travelers are warned never to linger near spire vents after dusk.

> "I saw my reflection blink — and then it was gone." — *Last entry of Scribe Halen Mor*

---

## Known Traits

- Nearly undetectable unless disturbed.
- Can grow up to 15 meters in length.
- Said to guard ancient magic etched into the spires.
- Reflective skin refracts light and heat signatures.
- Tongue flicks emit a faint chime audible only to those marked by magic.

---

## Additional Lore

Legends say the Glass Serpents were not born — but **grown**, left behind by the Architect-Mages who shaped the floating cities. Their translucent bodies are not just camouflage, but vessels of old spells, some of which are still active. Those bitten sometimes vanish entirely, as if plucked from time.

Old texts from the House of Silence describe rituals to summon or repel them — involving mirrored surfaces, whispered numbers, and the burning of moon-lichen. A few daring scholars believe the serpents are not creatures at all, but remnants of failed illusions, granted form by ambient magic.

In the ruins of **Kyreth's Rise**, a spire-city swallowed by stormclouds, explorers reported seeing hundreds of them, spiraling upward in ritualistic dance — mirroring each other's movements like shards of the same being.

Some believe they are **time-locked guardians**, programmed to awaken when certain star patterns align. One theory suggests their coils align with leyline vortices, amplifying arcane currents.

---

## Timeline of Sightings

- **-110 A.S.** — First recorded vanishing attributed to serpent bite.
- **-75 A.S.** — House of Silence texts refer to "the glass ones" as errors of light.
- **12 A.S.** — An entire skyship disappears near Cradle Spire after dusk.
- **157 A.S.** — First successful repulsion ritual reported by Mage-Librarian Ven Ator.
- **344 A.S.** — A living Glass Serpent captured briefly within a mirrored cage; vanished upon direct eye contact.

---

## Bestiary Entry

> *Class*: Arcane Beast  

> *Habitat*: Floating spires, especially near thermal vents and leyline nexuses  

> *Temperament*: Reactive, not aggressive unless provoked  

> *Threat Level*: High  

> *Interaction Protocol*: Avoid reflections, burn moon-lichen, do not speak aloud near mirrored surfaces at altitude.

---

## GlassSerpent Class (Python)

```python
import random
class GlassSerpent:
    def __init__(self, name="Unnamed Serpent", length=15.0):
        self.name = name
        self.length = length  # in meters
        self.visible = False
        self.leyline_synced = random.choice([True, False])
    def detect_prey(self, vibration, heat):
        """Returns True if prey is detected based on vibration and heat signature."""
        return vibration > 5 and heat > 30
    def coil_behavior(self):
        """Describes current behavior based on leyline alignment."""
        if self.leyline_synced:
            return f"{self.name} is coiling in rhythmic loops around a spire tip."
        return f"{self.name} lies dormant, barely visible."
    def bite(self, target):
        """Simulates a bite. Target may vanish if fate_roll triggers."""
        fate_roll = random.random()
        if fate_roll > 0.85:
            return f"{target} vanishes from reality. No trace remains."
        return f"{target} is bitten, dazed but still present."
    def reflect_check(self):
        """Returns eerie message if the serpent is near reflective surfaces."""
        return "You see your reflection blink… but your eyes did not move."
```
# Example usage
```
serpent = GlassSerpent(name="Echo")
print(serpent.coil_behavior())
print(serpent.bite("Explorer Kael"))
```
