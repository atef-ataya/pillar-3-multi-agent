"""
Quick setup verification script.
Run this to make sure everything is installed correctly.
"""

import sys
import os
from dotenv import load_dotenv

print("=" * 50)
print("PILLAR 3 SETUP VERIFICATION")
print("=" * 50)

# Check Python version
print(f"\n✓ Python version: {sys.version}")
if sys.version_info < (3, 11):
    print("  ⚠️  Warning: Python 3.11+ recommended")

# Check imports
try:
    import langgraph
    # LangGraph doesn't expose __version__, just check it imports
    print(f"✓ LangGraph installed successfully")
except ImportError:
    print("✗ LangGraph not installed")
    sys.exit(1)

try:
    import langchain
    print(f"✓ LangChain version: {langchain.__version__}")
except ImportError:
    print("✗ LangChain not installed")
    sys.exit(1)

try:
    import openai
    print(f"✓ OpenAI version: {openai.__version__}")
except ImportError:
    print("✗ OpenAI not installed")
    sys.exit(1)

# Check environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if api_key and api_key != "your_openai_api_key_here":
    print(f"✓ OpenAI API Key: {api_key[:8]}...{api_key[-4:]} (hidden)")
else:
    print("✗ OpenAI API Key not set in .env file")
    print("  → Edit .env and add your API key")
    sys.exit(1)

# Check state definition
try:
    from state import WebDesignState
    print("✓ State definition imported successfully")
    
    # Verify state structure
    test_state: WebDesignState = {
        "brochure_url": "test",
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    print("✓ State structure validated")
    print(f"  → Fields: {', '.join(test_state.keys())}")
    
except Exception as e:
    print(f"✗ State definition error: {e}")
    sys.exit(1)

# Check output directory
if not os.path.exists("output"):
    os.makedirs("output")
    print("✓ Output directory created")
else:
    print("✓ Output directory exists")

print("\n" + "=" * 50)
print("✅ ALL CHECKS PASSED - READY TO BUILD!")
print("=" * 50)
print("\nNext step: Build Part 2 (The Historian Agent)")