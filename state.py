"""
Pillar 3: Multi-Agent Creative Team - State Definition

This file defines the SHARED MEMORY for all agents.
Think of it as the "project folder" that gets passed from agent to agent.

Why TypedDict?
- Type safety: Python will warn you if you try to add wrong data types
- Clear contract: Every agent knows exactly what fields exist
- IDE autocomplete: VS Code will suggest field names
- Runtime validation: LangGraph checks types during execution

The State Flow:
1. Starts with only 'brochure_url' filled
2. Historian adds 'analysis'
3. Designer adds 'design_mockup' (parallel with Copywriter)
4. Copywriter adds 'copy' (parallel with Designer)
5. Developer adds 'code' (waits for both Designer + Copywriter)
6. Final state has all fields filled
"""

from typing import TypedDict


class WebDesignState(TypedDict):
    """
    Shared state for the creative team.
    
    This is the "baton" that gets passed in the relay race.
    Each agent receives this, does their job, and returns an update.
    
    Fields:
        brochure_url: Input - URL or path to the 1977 Apple brochure
        analysis: Output from Historian - key themes, tone, specs
        design_mockup: Output from Designer - text description of website design
        copy: Output from Copywriter - actual website copy in Jobs' voice
        code: Output from Developer - final HTML/CSS/JS code
    """
    
    # INPUT: What we start with
    brochure_url: str
    
    # OUTPUTS: What agents add (initially empty strings)
    analysis: str          # Historian's output
    design_mockup: str     # Designer's output
    copy: str             # Copywriter's output
    code: str             # Developer's output


# Example of how state evolves:
#
# Initial state:
# {
#   "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
#   "analysis": "",
#   "design_mockup": "",
#   "copy": "",
#   "code": ""
# }
#
# After Historian:
# {
#   "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
#   "analysis": "The 1977 Apple II brochure emphasized...",  ← Added
#   "design_mockup": "",
#   "copy": "",
#   "code": ""
# }
#
# After Designer + Copywriter (parallel):
# {
#   "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
#   "analysis": "The 1977 Apple II brochure emphasized...",
#   "design_mockup": "Hero section with Apple II image...",  ← Added
#   "copy": "Personal computing. For everyone.",  ← Added
#   "code": ""
# }
#
# After Developer (final):
# {
#   "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
#   "analysis": "The 1977 Apple II brochure emphasized...",
#   "design_mockup": "Hero section with Apple II image...",
#   "copy": "Personal computing. For everyone.",
#   "code": "<!DOCTYPE html>..."  ← Added - COMPLETE!
# }


# Type validation example (what NOT to do):
#
# BAD - This will cause errors:
# state_update = {"analysis": 12345}  # Wrong! Should be string, not int
#
# GOOD - This is correct:
# state_update = {"analysis": "The brochure emphasized simplicity"}