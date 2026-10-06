import subprocess
import os

def get_timezone(zone: str) -> str:
  result = subprocess.run(
    ['date'],
    env={**os.environ, 'TZ': zone},
    capture_output=True,
    text=True,
    check=True,
  )

  return result.stdout.strip()
