"""
Pillar 3: Multi-Agent Creative Team - ULTRA-ENHANCED 2025 VERSION
Phase 2.0: Production-Quality Modern Websites

This version generates STUNNING modern websites with:
✨ Scroll-triggered animations (IntersectionObserver)
💫 Smooth parallax effects
🎨 Beautiful gradients and shadows
🎭 Microinteractions on every element
📱 Perfect responsive design
⚡ Lightning-fast performance
"""

import os
from typing import Dict
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from state import WebDesignState

# Load environment variables
load_dotenv()

# Initialize LLM - Using GPT-4o for best quality
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

print("✓ API Key loaded:", os.getenv("OPENAI_API_KEY")[:12] + "..." if os.getenv("OPENAI_API_KEY") else "NOT FOUND")
print("✓ LLM initialized:", llm.model_name)


# ============================================================================
# AGENT 1: HISTORIAN (Same as before)
# ============================================================================

def historian_agent(state: WebDesignState) -> Dict[str, str]:
    """THE HISTORIAN - Research Specialist"""
    
    print("🔍 HISTORIAN AGENT: Analyzing 1977 Apple II brochure...")
    
    brochure_url = state["brochure_url"]
    
    system_prompt = """You are a design historian specializing in tech product launches 
from the 1970s and 1980s. Your expertise is in Apple's early design philosophy, 
Steve Jobs' messaging style, and the cultural context of the personal computing revolution."""

    user_prompt = f"""Analyze this 1977 Apple II product brochure: {brochure_url}

Extract insights about:
1. Design Philosophy & Visual Language (colors, typography, layout)
2. Messaging & Tone (Steve Jobs' voice, target audience, themes)
3. Technical Presentation (how specs were communicated)
4. Cultural Context (what was revolutionary in 1977)

Be specific and actionable for a modern design team."""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    try:
        response = llm.invoke(messages)
        print("✅ HISTORIAN AGENT: Analysis complete!")
        print(f"   Generated {len(response.content)} characters")
        return {"analysis": response.content}
    except Exception as e:
        print(f"❌ HISTORIAN AGENT: Error - {e}")
        return {"analysis": f"Error: {str(e)}"}


# ============================================================================
# AGENT 2: DESIGNER (Same as before)
# ============================================================================

def designer_agent(state: WebDesignState) -> Dict[str, str]:
    """THE DESIGNER - Visual Design Specialist"""
    
    print("🎨 DESIGNER AGENT: Creating design specifications...")
    
    analysis = state["analysis"]
    
    system_prompt = """You are a senior product designer specializing in retro-modern aesthetics.
Create detailed specifications for colors, typography, spacing, and layout."""

    user_prompt = f"""Based on this analysis:

{analysis}

Create a comprehensive design specification with:
- Exact hex color codes for warm, retro palette
- Typography system (fonts, sizes in rem)
- Spacing system (in rem units)
- Layout specifications (Grid, Flexbox)
- Animation guidelines
- Responsive breakpoints

Be extremely specific. A developer should be able to implement this pixel-perfect."""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    try:
        response = llm.invoke(messages)
        print("✅ DESIGNER AGENT: Design complete!")
        print(f"   Generated {len(response.content)} characters")
        return {"design_mockup": response.content}
    except Exception as e:
        print(f"❌ DESIGNER AGENT: Error - {e}")
        return {"design_mockup": f"Error: {str(e)}"}


# ============================================================================
# AGENT 3: COPYWRITER (Same as before)
# ============================================================================

def copywriter_agent(state: WebDesignState) -> Dict[str, str]:
    """THE COPYWRITER - Content Specialist"""
    
    print("✍️  COPYWRITER AGENT: Writing copy in Jobs' voice...")
    
    analysis = state["analysis"]
    
    system_prompt = """You are a master copywriter channeling Steve Jobs circa 1977.
Write copy that is simple, revolutionary, empowering, and human."""

    user_prompt = f"""Based on this analysis:

{analysis}

Write complete website copy including:
1. Hero headline and subheadline
2. 3-4 features (headline + description)
3. 2-3 benefits (headline + description)
4. Technical specs (5-7 specs)
5. Final CTA section

Sound like 1977 Steve Jobs - revolutionary yet accessible."""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    try:
        response = llm.invoke(messages)
        print("✅ COPYWRITER AGENT: Copy complete!")
        print(f"   Generated {len(response.content)} characters")
        return {"copy": response.content}
    except Exception as e:
        print(f"❌ COPYWRITER AGENT: Error - {e}")
        return {"copy": f"Error: {str(e)}"}


# ============================================================================
# AGENT 4: DEVELOPER - ULTRA-ENHANCED 2025 VERSION 🚀🚀🚀
# ============================================================================

def developer_agent(state: WebDesignState) -> Dict[str, str]:
    """
    THE DEVELOPER - ULTRA-ENHANCED 2025 VERSION
    
    Creates STUNNING modern websites like Stripe, Linear, Vercel with:
    ✨ Scroll-triggered fade-in animations
    💫 Smooth parallax effects on hero
    🎨 Beautiful gradients and shadows
    🎭 Hover animations on every interactive element
    📱 Perfect mobile-first responsive design
    ⚡ Buttery smooth 60fps animations
    """
    
    print("💻 DEVELOPER AGENT: Generating STUNNING 2025 production code...")
    
    analysis = state["analysis"]
    design_mockup = state["design_mockup"]
    copy = state["copy"]
    
    system_prompt = """You are an ELITE front-end developer at Vercel/Linear/Stripe in 2025.

Your websites are STUNNING with modern animations and interactions that make users say "WOW!"

MANDATORY REQUIREMENTS - YOU MUST INCLUDE ALL OF THESE:

1. ✨ SCROLL ANIMATIONS (CRITICAL!)
   ```javascript
   const observer = new IntersectionObserver((entries) => {
       entries.forEach(entry => {
           if (entry.isIntersecting) {
               entry.target.classList.add('fade-in-up');
           }
       });
   }, { threshold: 0.1 });
   
   document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
   ```
   
   ```css
   .animate-on-scroll {
       opacity: 0;
       transform: translateY(30px);
       transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1),
                   transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
   }
   .fade-in-up {
       opacity: 1;
       transform: translateY(0);
   }
   ```

2. 🎨 MODERN CSS FEATURES (CRITICAL!)
   - Gradients on hero: `background: linear-gradient(135deg, #f5e6d3 0%, #d4c4a8 100%);`
   - Box shadows: `box-shadow: 0 10px 40px rgba(0,0,0,0.1);`
   - Backdrop blur: `backdrop-filter: blur(10px);`
   - CSS Grid: `display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));`

3. 💫 BUTTON HOVER EFFECTS (CRITICAL!)
   ```css
   .btn {
       transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
   }
   .btn:hover {
       transform: translateY(-2px);
       box-shadow: 0 10px 25px rgba(0,0,0,0.2);
   }
   ```

4. 🎭 CARD HOVER EFFECTS (CRITICAL!)
   ```css
   .card {
       transition: all 0.3s ease;
   }
   .card:hover {
       transform: translateY(-5px);
       box-shadow: 0 20px 40px rgba(0,0,0,0.15);
   }
   ```

5. 📱 PERFECT RESPONSIVE DESIGN
   - Mobile-first approach
   - Breakpoints: 640px, 768px, 1024px, 1280px
   - Touch-friendly (44px minimum tap targets)

6. ⚡ SMOOTH SCROLL
   ```javascript
   document.querySelectorAll('a[href^="#"]').forEach(anchor => {
       anchor.addEventListener('click', function (e) {
           e.preventDefault();
           document.querySelector(this.getAttribute('href')).scrollIntoView({
               behavior: 'smooth'
           });
       });
   });
   ```

7. 🎨 MODERN DESIGN ELEMENTS
   - Hero section with gradient background
   - Floating cards with shadows
   - Subtle animations everywhere
   - Beautiful typography hierarchy
   - Generous whitespace

QUALITY CHECKLIST - VERIFY YOU INCLUDED:
✅ IntersectionObserver for scroll animations
✅ Fade-in-up animations on all sections
✅ Hover effects on buttons (lift + shadow)
✅ Hover effects on cards (lift + shadow)
✅ Gradient background on hero
✅ Box shadows on cards
✅ Smooth scroll JavaScript
✅ CSS Grid for features
✅ Responsive design (mobile-first)
✅ Modern typography (system fonts)
✅ Transitions on all interactive elements
✅ Loading animations (optional but nice)

CODE STRUCTURE:
- Single HTML file with embedded CSS and JS
- CSS organized: Variables → Reset → Typography → Layout → Components → Animations → Responsive
- JavaScript at bottom for performance
- Clean, commented, production-ready

OUTPUT FORMAT:
- Start with <!DOCTYPE html>
- NO markdown code blocks
- NO explanations
- ONLY the complete HTML code"""

    user_prompt = f"""Create a STUNNING, MODERN 2025 website that would make Stripe/Linear/Vercel designers jealous.

### DESIGN SPECIFICATIONS:
{design_mockup}

### WEBSITE COPY:
{copy}

### HISTORICAL CONTEXT:
{analysis[:500]}...

CRITICAL REMINDERS:
1. MUST include scroll-triggered fade-in animations using IntersectionObserver
2. MUST include hover effects on ALL buttons and cards
3. MUST include gradient backgrounds
4. MUST include box shadows for depth
5. MUST be responsive and beautiful on mobile
6. MUST have smooth, modern animations everywhere

This should look like a 2025 Stripe/Linear landing page with 1977 Apple aesthetics.

Output ONLY the complete HTML code. Start immediately with <!DOCTYPE html>"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    try:
        response = llm.invoke(messages)
        code = response.content
        
        # Clean up markdown if present
        if "```html" in code:
            code = code.split("```html")[1].split("```")[0].strip()
        elif "```" in code:
            code = code.split("```")[1].split("```")[0].strip()
        
        # Ensure DOCTYPE
        if not code.strip().startswith("<!DOCTYPE"):
            code = "<!DOCTYPE html>\n" + code
        
        print("✅ DEVELOPER AGENT: Code generation complete!")
        print(f"   Generated {len(code)} characters (~{code.count(chr(10))} lines)")
        
        # Validation
        validations = []
        if "IntersectionObserver" in code:
            validations.append("✓ Scroll animations (IntersectionObserver)")
        else:
            validations.append("⚠️  Missing scroll animations!")
            
        if "transform:" in code and "transition:" in code:
            validations.append("✓ CSS animations")
        else:
            validations.append("⚠️  Missing CSS transitions!")
            
        if "linear-gradient" in code or "radial-gradient" in code:
            validations.append("✓ Gradients")
        else:
            validations.append("⚠️  Missing gradients!")
            
        if "box-shadow" in code:
            validations.append("✓ Box shadows")
        else:
            validations.append("⚠️  Missing box shadows!")
            
        if ":hover" in code:
            validations.append("✓ Hover effects")
        else:
            validations.append("⚠️  Missing hover effects!")
            
        if "@media" in code:
            validations.append("✓ Responsive design")
        else:
            validations.append("⚠️  Missing media queries!")
        
        for validation in validations:
            print(f"   {validation}")
        
        return {"code": code}
        
    except Exception as e:
        print(f"❌ DEVELOPER AGENT: Error - {e}")
        return {"code": f"<!-- Error: {str(e)} -->"}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def save_website(state: WebDesignState, filename: str = "apple_ii_website_2025.html") -> str:
    """Save the generated website."""
    import os
    
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(state["code"])
    
    print(f"\n💾 Website saved to: {filepath}")
    print(f"📏 File size: {len(state['code'])} bytes (~{state['code'].count(chr(10))} lines)")
    print(f"📍 Absolute path: {os.path.abspath(filepath)}")
    
    return filepath


def test_ultra_enhanced_workflow():
    """Test the ULTRA-ENHANCED workflow."""
    print("\n" + "="*70)
    print("TESTING ULTRA-ENHANCED 2025 WORKFLOW")
    print("Generating a STUNNING modern website with animations & interactions")
    print("="*70 + "\n")
    
    state: WebDesignState = {
        "brochure_url": "https://archive.org/details/1977-intro-apple-ii-2/",
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    
    # Run all four agents
    print("⏳ Step 1/4: Running Historian...")
    state.update(historian_agent(state))
    print(f"   ✅ Complete: {len(state['analysis'])} chars\n")
    
    print("⏳ Step 2/4: Running Designer...")
    state.update(designer_agent(state))
    print(f"   ✅ Complete: {len(state['design_mockup'])} chars\n")
    
    print("⏳ Step 3/4: Running Copywriter...")
    state.update(copywriter_agent(state))
    print(f"   ✅ Complete: {len(state['copy'])} chars\n")
    
    print("⏳ Step 4/4: Running ULTRA-ENHANCED Developer (2025 MODERN CODE)...")
    state.update(developer_agent(state))
    print(f"   ✅ Complete: {len(state['code'])} chars (~{state['code'].count(chr(10))} lines)\n")
    
    print("\n" + "="*70)
    print("🎉 ULTRA-ENHANCED WORKFLOW COMPLETE!")
    print("="*70)
    print(f"\n📊 Final State Summary:")
    print(f"   Historian:   {len(state['analysis'])} chars")
    print(f"   Designer:    {len(state['design_mockup'])} chars")
    print(f"   Copywriter:  {len(state['copy'])} chars")
    print(f"   Developer:   {len(state['code'])} chars (~{state['code'].count(chr(10))} lines)")
    
    # Save
    print("\n💾 Saving ULTRA-ENHANCED 2025 website...")
    filepath = save_website(state)
    
    print("\n" + "="*70)
    print("✨ SUCCESS! Your STUNNING 2025 website is ready!")
    print("="*70)
    print(f"\n📂 File: {filepath}")
    print("🌐 Open in browser to see:")
    print("   ✨ Scroll-triggered fade-in animations")
    print("   💫 Beautiful hover effects")
    print("   🎨 Modern gradients and shadows")
    print("   📱 Perfect responsive design")
    print("\n🎬 This should look AMAZING for your demo! 🚀\n")
    
    return state


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    test_ultra_enhanced_workflow()