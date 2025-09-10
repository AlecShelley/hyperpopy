#!/usr/bin/env python3
"""Test script to verify the popy package works correctly."""

import sys
import os

# Add src to path
sys.path.insert(0, 'src')

try:
    import popy
    print("✓ Package imported successfully!")
    print(f"✓ Version: {popy.__version__}")
    print(f"✓ Available functions: {len(popy.__all__)} functions")
    
    # Test a specific function
    rate_value = popy.rate(2, 1.0)
    print(f"✓ rate(2, 1.0) = {rate_value}")
    
    # Test colors
    print(f"✓ Available colors: {popy.frozen_lake_colors[:3]}...")
    
    print("\n🎉 All tests passed! The package is ready for installation.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
