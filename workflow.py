"""
Pillar 3: Multi-Agent Creative Team - LangGraph Workflow

This file orchestrates the 4 agents using LangGraph:
1. Historian runs FIRST
2. Designer and Copywriter run in PARALLEL (both read from Historian)
3. Developer runs LAST (waits for Designer + Copywriter)

The workflow uses:
- StateGraph for orchestration
- Conditional edges for parallel execution
- Type-safe state management
- Error handling at each node

This is the CORE of the multi-agent architecture!
"""

from typing import Dict, TypedDict, Literal
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage

from state import WebDesignState
from agents import (
    historian_agent,
    designer_agent,
    copywriter_agent,
    developer_agent
)


# ============================================================================
# WORKFLOW GRAPH DEFINITION
# ============================================================================

def create_workflow() -> StateGraph:
    """
    Create the LangGraph workflow for the creative team.
    
    Workflow Structure:
    
        START
          ↓
      [HISTORIAN]
          ↓
      ┌───┴───┐
      ↓       ↓
  [DESIGNER] [COPYWRITER]  ← Run in PARALLEL
      ↓       ↓
      └───┬───┘
          ↓
     [DEVELOPER]
          ↓
         END
    
    Returns:
        StateGraph configured with all agents and edges
    """
    
    # Create the graph
    workflow = StateGraph(WebDesignState)
    
    # Add all agent nodes
    workflow.add_node("historian", historian_agent)
    workflow.add_node("designer", designer_agent)
    workflow.add_node("copywriter", copywriter_agent)
    workflow.add_node("developer", developer_agent)
    
    # Define the flow
    # 1. Start with Historian
    workflow.set_entry_point("historian")
    
    # 2. After Historian, both Designer and Copywriter can run
    #    They don't depend on each other, only on Historian
    workflow.add_edge("historian", "designer")
    workflow.add_edge("historian", "copywriter")
    
    # 3. After Designer AND Copywriter complete, run Developer
    workflow.add_edge("designer", "developer")
    workflow.add_edge("copywriter", "developer")
    
    # 4. After Developer, we're done
    workflow.add_edge("developer", END)
    
    return workflow


# ============================================================================
# WORKFLOW EXECUTION
# ============================================================================

def run_workflow(brochure_url: str) -> WebDesignState:
    """
    Execute the complete creative team workflow.
    
    Args:
        brochure_url: URL or description of the brochure to analyze
        
    Returns:
        Final state with all fields populated
        
    Example:
        >>> state = run_workflow("https://archive.org/details/1977-intro-apple-ii-2/")
        >>> print(state["code"])  # Generated website code
    """
    
    # Create initial state
    initial_state: WebDesignState = {
        "brochure_url": brochure_url,
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    
    # Build and compile the workflow
    workflow = create_workflow()
    app = workflow.compile()
    
    # Execute the workflow
    # LangGraph will handle the parallel execution automatically
    final_state = app.invoke(initial_state)
    
    return final_state


# ============================================================================
# WORKFLOW VISUALIZATION (Optional - for demo)
# ============================================================================

def visualize_workflow():
    """
    Print a visual representation of the workflow.
    Useful for understanding the agent dependencies.
    """
    
    print("\n" + "="*60)
    print("MULTI-AGENT WORKFLOW ARCHITECTURE")
    print("="*60 + "\n")
    
    print("     START")
    print("       ↓")
    print("  ┌─────────┐")
    print("  │HISTORIAN│  ← Analyzes 1977 Apple II brochure")
    print("  └────┬────┘")
    print("       ↓")
    print("   ┌───┴───┐")
    print("   ↓       ↓")
    print("┌────────┐ ┌──────────┐")
    print("│DESIGNER│ │COPYWRITER│  ← Run in PARALLEL")
    print("└───┬────┘ └────┬─────┘")
    print("    ↓           ↓")
    print("    └─────┬─────┘")
    print("          ↓")
    print("   ┌──────────┐")
    print("   │DEVELOPER │  ← Synthesizes everything")
    print("   └────┬─────┘")
    print("        ↓")
    print("       END")
    print("\n" + "="*60)
    print("Key Insights:")
    print("  • Historian runs FIRST (provides context)")
    print("  • Designer + Copywriter run PARALLEL (no dependencies)")
    print("  • Developer runs LAST (needs both Designer + Copywriter)")
    print("  • Total time: ~45-60 seconds")
    print("  • Total cost: ~$0.15-0.20 per run")
    print("="*60 + "\n")


# ============================================================================
# STREAMING EXECUTION (For live progress updates)
# ============================================================================

def run_workflow_streaming(brochure_url: str):
    """
    Execute workflow with streaming updates.
    
    This version yields progress updates as each agent completes,
    perfect for showing live progress in the CLI.
    
    Yields:
        Tuples of (agent_name, state) as each agent completes
    """
    
    initial_state: WebDesignState = {
        "brochure_url": brochure_url,
        "analysis": "",
        "design_mockup": "",
        "copy": "",
        "code": ""
    }
    
    workflow = create_workflow()
    app = workflow.compile()
    
    # Stream the execution
    for output in app.stream(initial_state):
        # output is a dict like: {"historian": {...updated_state...}}
        for agent_name, updated_state in output.items():
            yield (agent_name, updated_state)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_workflow_stats(state: WebDesignState) -> Dict[str, int]:
    """
    Calculate statistics about the generated content.
    
    Returns:
        Dictionary with character counts for each field
    """
    return {
        "analysis_chars": len(state["analysis"]),
        "design_chars": len(state["design_mockup"]),
        "copy_chars": len(state["copy"]),
        "code_chars": len(state["code"]),
        "code_lines": state["code"].count('\n') if state["code"] else 0
    }


def validate_state(state: WebDesignState) -> bool:
    """
    Validate that all required fields are populated.
    
    Returns:
        True if all fields have content, False otherwise
    """
    required_fields = ["analysis", "design_mockup", "copy", "code"]
    return all(state.get(field) and len(state[field]) > 0 for field in required_fields)


# ============================================================================
# MAIN - For testing the workflow directly
# ============================================================================

if __name__ == "__main__":
    import sys
    
    # Show workflow architecture
    visualize_workflow()
    
    # Check if user wants to run it
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        print("\n🚀 Running workflow...\n")
        
        # Run with default brochure URL
        brochure_url = "https://archive.org/details/1977-intro-apple-ii-2/"
        
        try:
            final_state = run_workflow(brochure_url)
            
            # Print results
            print("\n" + "="*60)
            print("✅ WORKFLOW COMPLETE!")
            print("="*60)
            
            stats = get_workflow_stats(final_state)
            print(f"\n📊 Content Generated:")
            print(f"   Historian:   {stats['analysis_chars']:,} characters")
            print(f"   Designer:    {stats['design_chars']:,} characters")
            print(f"   Copywriter:  {stats['copy_chars']:,} characters")
            print(f"   Developer:   {stats['code_chars']:,} characters ({stats['code_lines']:,} lines)")
            
            # Validate
            if validate_state(final_state):
                print("\n✅ All agents completed successfully!")
            else:
                print("\n⚠️  Some agents may have failed - check output")
            
            # Save output
            import os
            output_dir = "output"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            filepath = os.path.join(output_dir, "apple_ii_website.html")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(final_state["code"])
            
            print(f"\n💾 Website saved to: {filepath}")
            print("🌐 Open this file in your browser to see the result!\n")
            
        except Exception as e:
            print(f"\n❌ Error running workflow: {e}")
            sys.exit(1)
    else:
        print("\nℹ️  To run the workflow, use: python3 workflow.py run")
        print("   Or import and use: from workflow import run_workflow\n")