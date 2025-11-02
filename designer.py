"""
Pillar 3: Multi-Agent Creative Team - Agent Implementations

This file contains all the specialist agents:
- Historian: Analyzes the original 1977 Apple II brochure ✅ DONE
- Designer: Creates design mockup ✅ DONE
- Copywriter: Writes website copy (next)
- Developer: Generates final HTML/CSS/JS code (next)

Each agent is a simple function that:
1. Receives the current state
2. Does its specialized work (calls GPT-4o)
3. Returns an updated state with its contribution

This is the LangGraph pattern: agents are just functions that transform state.
"""

import os
from typing import Dict
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from state import WebDesignState

# ============================================================================
# LOAD ENVIRONMENT VARIABLES FIRST
# ============================================================================
load_dotenv()

# Verify API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "your_openai_api_key_here":
    raise ValueError(
        "❌ OPENAI_API_KEY not found in .env file!\n"
        "Please create a .env file with: OPENAI_API_KEY=sk-proj-xxxxx"
    )

print(f"✓ API Key loaded: {api_key[:8]}...{api_key[-4:]}")

# ============================================================================
# INITIALIZE THE LLM (GPT-4o)
# ============================================================================
llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME", "gpt-4o"),
    temperature=float(os.getenv("TEMPERATURE", "0.7")),
    api_key=api_key
)

print(f"✓ LLM initialized: {os.getenv('MODEL_NAME', 'gpt-4o')}")
print()


# ============================================================================
# AGENT 1: HISTORIAN
# ============================================================================

def historian_agent(state: WebDesignState) -> Dict[str, str]:
    """
    THE HISTORIAN - Research Specialist
    
    Role: Analyzes the original 1977 Apple II brochure to extract:
    - Design philosophy and visual style
    - Tone and messaging approach
    - Key themes and values
    - Technical specifications presentation style
    
    This agent runs FIRST and provides context for all other agents.
    
    Input: state["brochure_url"] - URL or description of the brochure
    Output: Updates state["analysis"] with detailed findings
    """
    
    print("🔍 HISTORIAN AGENT: Analyzing 1977 Apple II brochure...")
    
    brochure_url = state["brochure_url"]
    
    system_prompt = """You are a design historian specializing in vintage technology marketing.

Your job is to analyze the 1977 Apple II brochure and extract key insights about:

1. DESIGN PHILOSOPHY
   - Visual style (colors, layout, typography)
   - Use of imagery and graphics
   - Overall aesthetic approach

2. MESSAGING & TONE
   - How they positioned the product
   - Language style (technical vs accessible)
   - Target audience assumptions

3. KEY THEMES
   - What values did they emphasize? (simplicity, power, accessibility)
   - What problems were they solving?
   - What made it revolutionary?

4. TECHNICAL PRESENTATION
   - How did they explain technical specs?
   - Balance between features and benefits
   - Visual aids and diagrams

Be specific and detailed. Your analysis will guide a design team recreating
this style for a modern website.

Format your response as clear sections with specific observations."""

    user_prompt = f"""Analyze this 1977 Apple II brochure: {brochure_url}

Focus on extracting actionable insights that will help a modern design team
recreate the aesthetic and messaging style for a website.

Think like a historian who's briefing a creative team before a project kickoff."""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    try:
        response = llm.invoke(messages)
        analysis = response.content
        
        print("✅ HISTORIAN AGENT: Analysis complete!")
        print(f"   Generated {len(analysis)} characters of analysis")
        
        return {"analysis": analysis}
        
    except Exception as e:
        print(f"❌ HISTORIAN AGENT: Error - {e}")
        return {
            "analysis": f"Error analyzing brochure: {str(e)}. Using fallback analysis."
        }


# ============================================================================
# AGENT 2: DESIGNER
# ============================================================================

def designer_agent(state: WebDesignState) -> Dict[str, str]:
    """
    THE DESIGNER - Visual Design Specialist
    
    Role: Creates a detailed design mockup for the website based on the
    Historian's analysis. This is a TEXT description of the visual design,
    not actual code (the Developer will create the code later).
    
    The Designer specifies:
    - Layout structure (hero, sections, footer)
    - Color palette (specific hex codes)
    - Typography (fonts, sizes, hierarchy)
    - Imagery and graphics style
    - Spacing and visual rhythm
    - Interactive elements
    
    This agent runs AFTER Historian but PARALLEL with Copywriter.
    
    Input: state["analysis"] - Historian's findings
    Output: Updates state["design_mockup"] with detailed design description
    
    Why this matters:
    The Designer translates historical insights into concrete visual
    specifications that the Developer can implement.
    """
    
    print("🎨 DESIGNER AGENT: Creating design mockup from analysis...")
    
    analysis = state["analysis"]
    
    system_prompt = """You are a senior web designer specializing in retro-modern aesthetics.

Your job is to create a DETAILED design mockup (text description) for a website
that captures the essence of the 1977 Apple II brochure while being suitable
for modern web standards.

Your design mockup should specify:

1. LAYOUT STRUCTURE
   - Overall page structure (sections from top to bottom)
   - Grid system and spacing
   - Content hierarchy

2. COLOR PALETTE
   - Primary, secondary, and accent colors (with hex codes)
   - Background colors
   - Text colors
   - How colors reflect the 1977 aesthetic

3. TYPOGRAPHY
   - Font families (suggest modern equivalents to 1977 style)
   - Font sizes and hierarchy (H1, H2, body text)
   - Line heights and letter spacing

4. IMAGERY & GRAPHICS
   - Photography style
   - Illustration approach
   - Diagram/technical visual style
   - Image treatments (filters, overlays)

5. SPACING & RHYTHM
   - Padding and margins
   - Vertical rhythm
   - Whitespace usage

6. INTERACTIVE ELEMENTS
   - Button styles
   - Hover states
   - Transitions and animations (subtle, period-appropriate)

Be extremely specific. The Developer needs to be able to implement this
without asking questions.

Output format: Organized sections with clear specifications."""

    user_prompt = f"""Based on this historical analysis of the 1977 Apple II brochure:

{analysis}

Create a detailed design mockup (text description) for a modern single-page
website that authentically recreates the 1977 aesthetic.

Think like a designer presenting a comprehensive design system to developers."""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    try:
        response = llm.invoke(messages)
        design_mockup = response.content
        
        print("✅ DESIGNER AGENT: Design mockup complete!")
        print(f"   Generated {len(design_mockup)} characters of design specifications")
        
        return {"design_mockup": design_mockup}
        
    except Exception as e:
        print(f"❌ DESIGNER AGENT: Error - {e}")
        return {
            "design_mockup": f"Error creating design: {str(e)}. Using fallback design."
        }


# ============================================================================
# NEXT AGENTS WILL GO HERE
# ============================================================================
# We'll add these in Part 4 and 5:
#
# def copywriter_agent(state: WebDesignState) -> Dict[str, str]:
#     """Writes website copy in Steve Jobs' voice"""
#     pass
#
# def developer_agent(state: WebDesignState) -> Dict[str, str]:
#     """Generates final HTML/CSS/JS code"""
#     pass
# ============================================================================


# ============================================================================
# TEST FUNCTIONS
# ============================================================================

def test_historian():
    """Test the Historian agent in isolation."""
    print("\n" + "="*60)
    print("TESTING HISTORIAN AGENT IN ISOLATION")
    print("="*60 + "\n")
    
    test_state: WebDesignState = {
        "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    
    print(f"Input state: brochure_url = {test_state['brochure_url']}")
    print(f"Input state: analysis = '{test_state['analysis']}' (empty)")
    print("\n" + "-"*60 + "\n")
    
    updated_fields = historian_agent(test_state)
    test_state.update(updated_fields)
    
    print("\n" + "-"*60 + "\n")
    print("Output state: analysis =")
    print(test_state["analysis"])
    print("\n" + "="*60 + "\n")
    
    return test_state


def test_designer():
    """Test the Designer agent in isolation."""
    print("\n" + "="*60)
    print("TESTING DESIGNER AGENT IN ISOLATION")
    print("="*60 + "\n")
    
    # First, run Historian to get analysis
    print("Step 1: Running Historian to get analysis...\n")
    test_state: WebDesignState = {
        "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    
    updated_fields = historian_agent(test_state)
    test_state.update(updated_fields)
    
    print("\n" + "-"*60 + "\n")
    print("Step 2: Running Designer with Historian's analysis...\n")
    print(f"Input state: analysis = {len(test_state['analysis'])} characters")
    print(f"Input state: design_mockup = '{test_state['design_mockup']}' (empty)")
    print("\n" + "-"*60 + "\n")
    
    updated_fields = designer_agent(test_state)
    test_state.update(updated_fields)
    
    print("\n" + "-"*60 + "\n")
    print("Output state: design_mockup =")
    print(test_state["design_mockup"])
    print("\n" + "="*60 + "\n")
    
    return test_state


def test_both_agents():
    """Test both Historian and Designer in sequence."""
    print("\n" + "="*60)
    print("TESTING HISTORIAN → DESIGNER PIPELINE")
    print("="*60 + "\n")
    
    # Initial state
    state: WebDesignState = {
        "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    
    # Run Historian
    print("Step 1/2: Historian analyzing brochure...")
    state.update(historian_agent(state))
    
    print(f"\n✓ Historian complete: {len(state['analysis'])} chars\n")
    print("-"*60 + "\n")
    
    # Run Designer
    print("Step 2/2: Designer creating mockup...")
    state.update(designer_agent(state))
    
    print(f"\n✓ Designer complete: {len(state['design_mockup'])} chars\n")
    print("="*60 + "\n")
    
    # Summary
    print("FINAL STATE SUMMARY:")
    print(f"  brochure_url: {state['brochure_url']}")
    print(f"  analysis: {len(state['analysis'])} characters ✓")
    print(f"  design_mockup: {len(state['design_mockup'])} characters ✓")
    print(f"  copy: '{state['copy']}' (not yet)")
    print(f"  code: '{state['code']}' (not yet)")
    print("\n" + "="*60 + "\n")
    
    return state


# ============================================================================
# MAIN - Choose which test to run
# ============================================================================

if __name__ == "__main__":
    import sys
    
    # Check if user specified which test to run
    if len(sys.argv) > 1:
        if sys.argv[1] == "historian":
            test_historian()
        elif sys.argv[1] == "designer":
            test_designer()
        elif sys.argv[1] == "both":
            test_both_agents()
        else:
            print("Usage: python3 agents.py [historian|designer|both]")
    else:
        # Default: test both agents in sequence
        test_both_agents()