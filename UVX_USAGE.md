# Using DisplayCtl with uvx

This document explains how to use DisplayCtl with `uvx` for the best user experience.

## What is uvx?

`uvx` is a tool for running Python applications in isolated environments. It automatically:
- Creates a virtual environment
- Installs the package and its dependencies  
- Handles system dependencies like `dbus-python`
- Runs the application

## Installation

First, install `uvx` if you don't have it:

```bash
# Install uvx
pipx install uv
# or
pip install uv
```

## Usage with uvx

### One-time execution (no installation)

```bash
# Show current monitor configuration
uvx displayctl current

# Save current configuration  
uvx displayctl save work-setup

# List saved configurations
uvx displayctl list

# Load a configuration (dry-run)
uvx displayctl load work-setup --dry-run

# Load a configuration
uvx displayctl load work-setup

# Delete a configuration
uvx displayctl delete old-setup
```

### Install for repeated use

```bash
# Install displayctl for repeated use
uvx install displayctl

# Now you can use it directly
displayctl current
displayctl save work-setup
displayctl list
```

## Why uvx is Perfect for DisplayCtl

1. **Handles D-Bus Dependencies**: The `dbus-python` package requires system libraries and headers. uvx handles this complexity automatically.

2. **No Global Pollution**: Doesn't install packages globally on your system.

3. **Always Up-to-Date**: Can easily run the latest version from PyPI.

4. **No Setup Required**: Works immediately without any manual dependency installation.

## Alternative Methods

### From source with uvx

If you have the source code locally:

```bash
# Run from local source
uvx --from /path/to/displayctl displayctl current

# Install from local source  
uvx install /path/to/displayctl
```

### Traditional pip installation

```bash
# Install system dependencies first
sudo apt install python3-dbus  # Ubuntu/Debian
sudo dnf install python3-dbus  # Fedora
sudo pacman -S python-dbus     # Arch

# Then install with pip
pip install displayctl
displayctl current
```

## Publishing to PyPI

To make `uvx displayctl` work globally, the package needs to be published to PyPI:

```bash
# Build the package
python -m build

# Publish to PyPI (requires account and credentials)
python -m twine upload dist/*
```

Once published, anyone can use:
```bash
uvx displayctl current
```
