# Launchpad FX – Multi-Device Support Guide

This guide explains how Launchpad FX supports different Novation Launchpad models (MK1, MK2, etc) and other MIDI-compatible devices.

## Device Detection & Profiles

By default, LPFX will:
- Try to load the last saved device profile from `~/.lpfx_config.json`
- If none is saved, it will auto-detect any connected device with "Launchpad" in its name
- If no Launchpad is found, it will list all available MIDI devices and ask for manual selection

## Manual Selection

You can explicitly set your device:

```bash
python main.py --device "Launchpad MK2 MIDI"
```

Or use the interactive selector:

```bash
python main.py --select-device
```

## Configuration File

All settings are stored in:
```
~/.lpfx_config.json
```
Example:
```json
{
  "device": {
    "name": "Launchpad MK2 MIDI",
    "model": "manual",
    "grid_size": [8, 8],
    "color_range": [0, 1, ..., 127]
  }
}
```

## Notes on Compatibility

- **MK1**: original device, single-color grid
- **MK2**: supports RGB velocity values (0–127)
- You can use LPFX with any 8x8 MIDI grid controller if it supports note_on messages

## Troubleshooting

- If nothing shows up: run `python main.py --select-device` and verify a device is available
- If LEDs flicker or behave weirdly, check if `color_range` fits your model (e.g. [0–3] for MK1)
- Run with `--live` to test effects interactively

---

Still stuck? Join the discussion on GitHub or raise an issue with your device info.
