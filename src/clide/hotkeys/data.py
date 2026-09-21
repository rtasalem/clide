from dataclasses import dataclass, field

@dataclass
class Hotkey:
  keys: str
  description: str

@dataclass
class HotkeySection:
  title: str
  hotkeys: list[Hotkey] = field(default_factory=list)

HOTKEY_SECTIONS: dict[str, HotkeySection] = {
  'applications': HotkeySection(
    title='Apps',
    hotkeys=[
      Hotkey('Cmd + Space', 'Launch Raycast'),
      Hotkey('Opt + Cmd + Space', 'Clipboard history (Raycast)'),
      Hotkey('Ctrl + Opt, Cmd + C', 'Caffeinate Mac indefinitely (Raycast)'),
      Hotkey('Ctrl + Opt, Cmd + D', 'Decaffeinate Mac indefinitely (Raycast)'),
      Hotkey('Ctrl + D', 'Define word (Raycast)'),
      Hotkey('Ctrl + Cmd + Space', 'Search Emoji & Symbols (Raycast)'),
      Hotkey('Opt + Cmd + F', 'Search files (Raycast)'),
      Hotkey('Ctrl + Cmd + 5', 'Screenshot and recording option (default settings)'),
      Hotkey('Cmd + Shift + 5', 'Full screenshot (Shottr)'),
      Hotkey('Cmd + Shift + 4', 'Area screenshot using cross-hairs (Shottr)'),
      Hotkey('Cmd + Shift + 3', 'Scrolling screenshot (Shottr)'),
      Hotkey('Cmd + Shift + 2', 'Any window screenshot (Shottr)'),
      Hotkey('Ctrl + Opt + Cmd + O', 'OCR screenshot (Shottr)'),
      Hotkey('Ctrl + Opt + Cmd + P', 'Start/stop pomodoro timer (TomatoBar)'),
      Hotkey('Ctrl + Ctrl', 'Start/stop voice dictation (Cloudless Voice)')
    ]
  ),
  'system': HotkeySection(
    title='System',
    hotkeys=[
      Hotkey('Ctrl + Opt + S', 'Sleep'),
      Hotkey('Opt + Cmd + Esc', 'Force Quit Applications')
    ]
  ),
  'window_management': HotkeySection(
    title='Window Management',
    hotkeys=[
      Hotkey('Cmd + R', 'Right half'),
      Hotkey('Cmd + L', 'Left half'),
      Hotkey('Cmd + Shift + U', 'Upper half'),
      Hotkey('Cmd + Shift + D', 'Bottom half'),
      Hotkey('Cmd + 1', 'Top left quarter'),
      Hotkey('Cmd + 2', 'Top right quarter'),
      Hotkey('Cmd + 3', 'Bottom left quarter'),
      Hotkey('Cmd + 4', 'Bottom right quarter'),
      Hotkey('Cmd + G', 'Centre'),
      Hotkey('Cmd + Up Arrow', 'Next display'),
      Hotkey('Cmd + ;', 'Maximise (not true full screen)'),
      Hotkey('Cmd + M', 'Minimise'),
      Hotkey('Cmd + W', 'Close')
    ]
  )
}
