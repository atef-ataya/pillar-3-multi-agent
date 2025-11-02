"""
Pillar 3: Multi-Agent Creative Team - Demo Runner

Beautiful CLI interface for running the creative team workflow.
Perfect for screen recording demos!

Features:
- Clean, readable output
- Progress indicators for each agent
- Real-time status updates
- Final statistics
- Automatic file saving

Usage:
    python3 run_creative_team.py
"""

import os
import sys
import time
from datetime import datetime
from typing import Optional

from state import WebDesignState
from workflow import run_workflow_streaming, get_workflow_stats, validate_state


# ============================================================================
# CLI STYLING
# ============================================================================

class Colors:
    """ANSI color codes for terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def print_header():
    """Print the demo header"""
    print("\n" + "="*70)
    print(f"{Colors.BOLD}{Colors.CYAN}THE ARCHITECT'S PLAYBOOK: MULTI-AGENT CREATIVE TEAM{Colors.END}")
    print(f"{Colors.BOLD}Building a 1977 Apple II Website with AI Agents{Colors.END}")
    print("="*70 + "\n")


def print_section(title: str):
    """Print a section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'─' * 70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{title}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'─' * 70}{Colors.END}\n")


def print_agent_start(agent_name: str, description: str):
    """Print when an agent starts"""
    icons = {
        "historian": "🔍",
        "designer": "🎨",
        "copywriter": "✍️",
        "developer": "💻"
    }
    icon = icons.get(agent_name, "⚙️")
    
    print(f"{icon}  {Colors.BOLD}{agent_name.upper()}{Colors.END}: {description}")
    print(f"   {Colors.CYAN}Working...{Colors.END}", end="", flush=True)


def print_agent_complete(agent_name: str, chars: int, duration: float):
    """Print when an agent completes"""
    print(f"\r   {Colors.GREEN}✓ Complete{Colors.END} - Generated {chars:,} chars in {duration:.1f}s")


def print_error(message: str):
    """Print an error message"""
    print(f"\n{Colors.RED}{Colors.BOLD}❌ ERROR:{Colors.END} {Colors.RED}{message}{Colors.END}\n")


def print_success(message: str):
    """Print a success message"""
    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ {message}{Colors.END}\n")


# ============================================================================
# PROGRESS TRACKING
# ============================================================================

class ProgressTracker:
    """Tracks progress through the workflow"""
    
    def __init__(self):
        self.start_time = time.time()
        self.agent_times = {}
        self.current_agent = None
        self.current_agent_start = None
    
    def start_agent(self, agent_name: str):
        """Mark when an agent starts"""
        self.current_agent = agent_name
        self.current_agent_start = time.time()
    
    def complete_agent(self, agent_name: str):
        """Mark when an agent completes"""
        if self.current_agent_start:
            duration = time.time() - self.current_agent_start
            self.agent_times[agent_name] = duration
            return duration
        return 0.0
    
    def get_total_time(self):
        """Get total elapsed time"""
        return time.time() - self.start_time


# ============================================================================
# WORKFLOW EXECUTION
# ============================================================================

def run_creative_team(brochure_url: str = "https://archive.org/details/1977-intro-apple-ii-2/"):
    """
    Run the complete creative team workflow with beautiful CLI output.
    
    Args:
        brochure_url: URL of the brochure to analyze
    """
    
    # Print header
    print_header()
    
    # Show input
    print(f"{Colors.BOLD}Input:{Colors.END}")
    print(f"  📄 Brochure: {brochure_url}")
    print(f"  🎯 Goal: Generate a complete website\n")
    
    # Initialize progress tracker
    tracker = ProgressTracker()
    
    # Phase tracking
    phase_descriptions = {
        "historian": "Analyzing 1977 Apple II brochure for design insights",
        "designer": "Creating visual design specifications",
        "copywriter": "Writing website copy in Steve Jobs' voice",
        "developer": "Synthesizing into production-ready HTML/CSS/JS"
    }
    
    # Track state - initialize with full structure
    current_state: WebDesignState = {
        "brochure_url": brochure_url,
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    
    try:
        # Run workflow with streaming
        print_section("⏳ PHASE 1: HISTORICAL ANALYSIS")
        
        for agent_name, updated_state in run_workflow_streaming(brochure_url):
            # Start tracking
            if agent_name not in tracker.agent_times:
                if agent_name == "designer":
                    print_section("⏳ PHASE 2: PARALLEL CREATIVE WORK")
                elif agent_name == "developer":
                    print_section("⏳ PHASE 3: CODE GENERATION")
                
                description = phase_descriptions.get(agent_name, "Processing...")
                print_agent_start(agent_name, description)
                tracker.start_agent(agent_name)
            
            # Accumulate state - merge updates into current state
            current_state.update(updated_state)
            
            # Determine output length based on what this agent produces
            output_field = {
                "historian": "analysis",
                "designer": "design_mockup",
                "copywriter": "copy",
                "developer": "code"
            }.get(agent_name)
            
            if output_field and output_field in current_state:
                chars = len(current_state.get(output_field, ""))
                duration = tracker.complete_agent(agent_name)
                print_agent_complete(agent_name, chars, duration)
        
        # Workflow complete!
        # Print results
        print_section("🎉 WORKFLOW COMPLETE!")
        
        stats = get_workflow_stats(current_state)
        
        print(f"{Colors.BOLD}📊 Content Generated:{Colors.END}")
        print(f"   Historian:   {stats['analysis_chars']:>6,} characters")
        print(f"   Designer:    {stats['design_chars']:>6,} characters")
        print(f"   Copywriter:  {stats['copy_chars']:>6,} characters")
        print(f"   Developer:   {stats['code_chars']:>6,} characters (~{stats['code_lines']:,} lines)")
        
        print(f"\n{Colors.BOLD}⏱️  Performance:{Colors.END}")
        total_time = tracker.get_total_time()
        print(f"   Total time:  {total_time:.1f} seconds")
        print(f"   Avg/agent:   {total_time/4:.1f} seconds")
        
        # Validate
        if not validate_state(current_state):
            print_error("Some agents may have incomplete output")
            return None
        
        # Save output
        print(f"\n{Colors.BOLD}💾 Saving Output:{Colors.END}")
        
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"   Created directory: {output_dir}/")
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"apple_ii_website_{timestamp}.html"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(current_state["code"])
        
        file_size = len(current_state["code"])
        print(f"   Saved to: {Colors.GREEN}{filepath}{Colors.END}")
        print(f"   File size: {file_size:,} bytes")
        
        # Success message
        print("\n" + "="*70)
        print(f"{Colors.GREEN}{Colors.BOLD}✓ SUCCESS!{Colors.END} {Colors.GREEN}Your Apple II website is ready!{Colors.END}")
        print("="*70)
        
        print(f"\n{Colors.BOLD}Next Steps:{Colors.END}")
        print(f"  1. Open {Colors.CYAN}{filepath}{Colors.END} in your browser")
        print(f"  2. Scroll to see animations in action")
        print(f"  3. Hover over cards and buttons")
        print(f"  4. Resize window to test responsiveness")
        
        print(f"\n{Colors.BOLD}🎬 Perfect for your demo video!{Colors.END}\n")
        
        return current_state
        
    except KeyboardInterrupt:
        print_error("Workflow interrupted by user")
        return None
        
    except Exception as e:
        print_error(f"Workflow failed: {str(e)}")
        import traceback
        print(f"{Colors.YELLOW}Traceback:{Colors.END}")
        print(traceback.format_exc())
        return None


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point"""
    
    # Check for custom brochure URL
    brochure_url = "https://archive.org/details/1977-intro-apple-ii-2/"
    
    if len(sys.argv) > 1:
        brochure_url = sys.argv[1]
    
    # Run the workflow
    result = run_creative_team(brochure_url)
    
    # Exit with appropriate code
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()