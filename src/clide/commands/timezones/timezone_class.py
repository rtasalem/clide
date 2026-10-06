from dataclasses import dataclass

@dataclass
class Timezone:
  city: str
  country: str
  zone: str
  flag: str
