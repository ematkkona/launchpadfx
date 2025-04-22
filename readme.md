# Launchpad FX 🎛️

**Interactive, scriptable, audio-reactive FX engine for Novation Launchpad devices (MK1, MK2, and compatible MIDI controllers).**

---

## ✨ Features

- 🌊 Smooth text scrolling across the Launchpad grid
- 🎵 Real-time audio visualization via FFT
- 📊 Live system performance metrics (CPU, Memory, Network)
- 🎭 Gimmick effects (Pac-Man, Ghost, Smiley)
- 🎛️ Dynamic effects engine (wave, sweep, party mode)
- 🧠 Scriptable FX engine with interactive shell
- ✅ Multi-device support: auto-detect or manually select
- 🧪 Unit tested core functionality
- 💾 Configuration persistence

---

## 🚀 Quickstart

### 📦 Installation (for development)
```bash
git clone https://github.com/yourusername/lpfx.git
cd lpfx
pip install -e .
```

### 🎛️ Run Interactive Shell
```bash
python lpfx/main.py --live
```

### 📜 Run FX Script
```bash
python lpfx/main.py --script example.fx
```

### 🎯 Select Device Interactively
```bash
python lpfx/main.py --select-device
```

> By default, LPFX will auto-detect connected Launchpad devices. Use `--device "Device Name"` to override.

---

## 🧪 Running Tests
```bash
pip install pytest
pytest tests/
```

---

## 📁 Project Structure

```
lpfx/
├── effects/        # Built-in visual/audio effects
├── input/          # Button mapping & input listening
├── modes/          # Preset modes (like Party Mode)
├── scripting/      # Script parser & FX runner
├── main.py         # CLI entry point
docs/
├── devices.md      # Multi-device support & troubleshooting
tests/
├── test_*.py       # Unit tests
```

---

## 📚 Learn More
For device compatibility, config structure, and advanced usage:  
👉 [docs/devices.md](docs/devices.md)

---

## 🪪 License
MIT © 2025 Eetu Mäkinen