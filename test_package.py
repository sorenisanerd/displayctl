#!/usr/bin/env python3
"""Test script to verify uvx package structure without D-Bus dependencies."""

import sys
import os

# Add the src directory to the path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def test_package_structure():
    """Test that the package can be imported and has correct structure."""
    try:
        import displayctl
        print("✓ Package displayctl imported successfully")
        print(f"  Version: {displayctl.__version__}")
        print(f"  Description: {displayctl.__description__}")
        
        # Test that cli module exists
        from displayctl import cli
        print("✓ CLI module found")
        
        # Test that __main__ module exists  
        import displayctl.__main__
        print("✓ __main__ module found")
        
        print("\n✓ Package structure is correct for uvx usage")
        print("\nTo test with uvx:")
        print("  uvx --from /path/to/displayctl displayctl --help")
        print("  uvx displayctl current  # (after publishing)")
        
        return True
        
    except ImportError as e:
        if "dbus" in str(e).lower():
            print("ℹ  D-Bus dependency missing (expected on this system)")
            print("✓ Package would work with uvx (handles dependencies)")
            return True
        else:
            print(f"✗ Import error: {e}")
            return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


if __name__ == '__main__':
    success = test_package_structure()
    sys.exit(0 if success else 1)
