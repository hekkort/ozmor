# 🦅 Skirvel Hawks

![Skirvel Hawk](/images/skirvel-hawk.png)

## Messengers of the Sky Realms

Skirvel Hawks are revered for their unerring sense of direction. These sleek, blue-plumed birds can travel 300 leagues without rest, guided by geomagnetic pulses. They are often trained by skyward couriers and used to deliver sealed messages between floating cities.

> "If a Skirvel takes flight with your words, know they will reach even the moonlight watchtowers." — *Skypost Lorebook*

---

## Known Traits

- Can navigate even in magical fog or voidlight.
- Form lifelong bonds with handlers.
- Used in ancient High House diplomacy.
- Sensitive to sky-metal and leyline interference.
- Wings shimmer faintly under starlight due to trace celestial alloys.

---

## Additional Lore

It is said that the first Skirvels were bred in the aeries of **House Veyr**, where they were infused with trace amounts of sky-metal to enhance their navigational senses. These birds were once thought extinct following the **Fracture of the Aether Spine**, but rediscovered by storm-herders near the ruins of Cloudmere.

Legends hold that Skirvels do not serve just anyone — they must first recognize a person’s "sky-thread," an unseen tether of purpose. If a hawk refuses a message, it is said to be fate itself intervening.

During the **Siege of Aelarion**, a single hawk named **Vareth's Wing** flew through storms and battlefields to deliver the call for aid — a journey now sung in bardic halls as *"The Last Flight of Dawn."*

In modern times, rogue hawks with broken bands are believed to carry lost words: royal decrees, unsent warnings, even final confessions. These birds never land, circling the ruins of sky-cities long since fallen, seeking a true heir to the broken banners.

---

## Timeline of Flight and Folklore

- **-701 A.S.** — First mention of “sky-silvered hawks” in House Veyr breeding ledgers.
- **-345 A.S.** — Skirvels used to negotiate the Treaty of the Seven Isles.
- **1 A.S.** — Vareth’s Wing delivers final plea to the Aether Wardens.
- **98 A.S.** — Scholar Eylin claims Skirvels avoid falsehood; sparks debate in the High Forums.
- **312 A.S.** — A rogue hawk lands atop the Skygrave Tower, igniting prophecy rumors.

---

## Bestiary Entry

> *Class*: Arcane Avian

> *Habitat*: Floating city aeries, high cliffs, ley-currents  

> *Temperament*: Loyal, alert, easily startled by distortion magic  

> *Threat Level*: Minimal (unless bonded and protective)  

> *Interaction Protocol*: Approach calmly; offer open hands and sky-metal token. Never speak lies in its presence.

---

## SkirvelHawk Class (Python)

```python
import random
class SkirvelHawk:
    def __init__(self, name="Unnamed Hawk", bonded=False):
        self.name = name
        self.bonded = bonded
        self.exhaustion = 0  # Measured in leagues flown without rest
        self.carrying_message = False
    def bond(self, handler_name):
        """Attempt to bond with a handler. Works only once and randomly."""
        if self.bonded:
            return f"{self.name} is already bonded and loyal."
        if random.random() > 0.7:
            self.bonded = True
            return f"{self.name} accepts {handler_name} as its bonded handler."
        return f"{self.name} rejects the bond — your sky-thread is not aligned."
    def fly(self, leagues):
        """Simulates a flight journey. Increases exhaustion."""
        self.exhaustion += leagues
        if self.exhaustion > 300:
            return f"{self.name} veers off course — exhaustion takes hold."
        return f"{self.name} soars {leagues} leagues with swift precision."
    def deliver_message(self, message_truthful=True):
        """Delivers a message. May refuse if falsehood detected."""
        if not self.bonded:
            return f"{self.name} refuses to carry your words — the bond is unproven."
        if not message_truthful and random.random() > 0.5:
            return f"{self.name} screeches and drops the scroll — it senses deceit."
        self.carrying_message = True
        return f"{self.name} takes flight with the message, wings gleaming like moonlight."
    def rest(self):
        """Recovers exhaustion."""
        self.exhaustion = 0
        return f"{self.name} rests and preens atop a wind-touched perch."
```

# Example usage

```
hawk = SkirvelHawk(name="Vareth's Wing")
print(hawk.bond("Aelarion Courier"))
print(hawk.fly(180))
print(hawk.deliver_message(message_truthful=True))
```
