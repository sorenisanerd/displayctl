# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-08-25

### Added

- Exposed ApplyMonitorsConfig method parameter in CLI
- Added convenient alias arguments for method selection:
  - `--verify` - Only verify configuration without applying (method 0)
  - `--temporary` / `--temp` - Apply configuration temporarily (method 1)
  - `--persistent` - Apply configuration permanently (method 2)
- Added ApplyMethod enum to replace magic number values
- Enhanced user feedback showing which method is being used
- Improved CLI help with more comprehensive examples

### Changed

- Method parameter now uses enum values instead of magic numbers
- Updated CLI argument parser with mutually exclusive method groups
- Improved error messages to show enum names for better clarity
- Enhanced type safety with ApplyMethod enum

### Fixed

- Fixed D-Bus call formatting and error handling
- Removed trailing whitespace from source files

## [1.0.1] - Previous Release

### Initial Features

- Initial release with basic monitor configuration management
- Save and load monitor configurations
- List and delete saved configurations
- Show current monitor setup
- Support for GNOME's D-Bus DisplayConfig interface

[1.2.0]: https://github.com/sorenisanerd/displayctl/compare/v1.0.1...v1.2.0
[1.0.1]: https://github.com/sorenisanerd/displayctl/releases/tag/v1.0.1
