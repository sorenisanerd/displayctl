# Release Notes for DisplayCtl v1.2.0

## Summary

Version 1.2.0 brings significant improvements to the CLI interface, making it more user-friendly and robust.

## What's New

### Enhanced Method Parameter Support
- Exposed the ApplyMonitorsConfig method parameter in the CLI
- Added convenient alias arguments:
  - `--verify` - Only verify configuration without applying
  - `--temporary` / `--temp` - Apply configuration temporarily  
  - `--persistent` - Apply configuration permanently

### Code Quality Improvements
- Replaced magic numbers with `ApplyMethod` enum for better type safety
- Enhanced error messages that now show enum names for better clarity
- Improved CLI help with comprehensive examples

### User Experience
- Better feedback showing which method is being used when applying configurations
- Mutually exclusive argument groups prevent conflicting options
- More intuitive command-line interface

## Installation

You can install DisplayCtl v1.2.0 using pip:

```bash
pip install displayctl==1.2.0
```

Or build from source:

```bash
git checkout v1.2.0
python -m build
pip install dist/displayctl-1.2.0-py3-none-any.whl
```

## Usage Examples

```bash
# Apply configuration temporarily (default behavior)
displayctl load work

# Apply configuration permanently
displayctl load work --persistent

# Only verify configuration without applying
displayctl load work --verify

# Use numeric method (backward compatibility)
displayctl load work --method 2
```

## Backward Compatibility

All existing scripts and commands will continue to work unchanged. The new alias arguments are additional convenience features.

## Files Changed

- `pyproject.toml`: Version bump to 1.2.0
- `src/displayctl/__init__.py`: Version update
- `src/displayctl/cli.py`: Major CLI enhancements
- `CHANGELOG.md`: New changelog file

## Package Verification

The built packages are available in the `dist/` directory:
- `displayctl-1.2.0-py3-none-any.whl`
- `displayctl-1.2.0.tar.gz`

## Git Release

- Commit: `e6f91c5`
- Tag: `v1.2.0`
- Ready to push to remote repository
