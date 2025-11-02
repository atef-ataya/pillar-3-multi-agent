# 🎨 Pillar 3: Multi-Agent Creative Team

**Build a 1977 Apple II Website Using Collaborative AI Agents**

A demonstration of LangGraph's multi-agent collaboration pattern, where specialized AI agents work together to create a complete website from a historical brochure.

---

## 🌟 The Agent Team

### 1️⃣ **The Historian** 🔍

- **Role:** Research Specialist
- **Input:** Original 1977 Apple II brochure URL
- **Output:** Detailed analysis of design philosophy, messaging tone, and technical presentation
- **Runs:** FIRST (sequential)

### 2️⃣ **The Designer** 🎨

- **Role:** Visual Design Specialist
- **Input:** Historian's analysis
- **Output:** Detailed design mockup (color palette, typography, layout)
- **Runs:** PARALLEL with Copywriter

### 3️⃣ **The Copywriter** ✍️

- **Role:** Content & Messaging Specialist
- **Input:** Historian's analysis
- **Output:** Complete website copy in Steve Jobs' 1977 voice
- **Runs:** PARALLEL with Designer

### 4️⃣ **The Developer** 💻 **← NEW!**

- **Role:** Code Generation Specialist
- **Input:** Analysis + Design + Copy
- **Output:** Complete HTML/CSS/JS single-page website
- **Runs:** LAST (after Designer + Copywriter)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key

### Installation

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 3. Verify setup
python3 test_setup.py
```

### Run the Complete Workflow

```bash
# Run all four agents in sequence
python3 agents.py all
```

This will:

1. ✅ Analyze the 1977 Apple II brochure
2. ✅ Create design specifications
3. ✅ Write website copy
4. ✅ Generate complete HTML/CSS/JS code
5. ✅ Save to `output/apple_ii_website.html`

---

## 🧪 Testing Individual Agents

```bash
# Test individual agents
python3 agents.py historian     # Test only Historian
python3 agents.py designer      # Test Historian → Designer
python3 agents.py copywriter    # Test Historian → Copywriter
python3 agents.py developer     # Test all agents up to Developer

# Test parallel execution demo
python3 agents.py parallel      # Shows Designer + Copywriter running concurrently
```

---

## 📊 Workflow Architecture

```
┌─────────────────────────────────────────────┐
│              START                          │
│   Input: 1977 Apple II Brochure URL        │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
         ┌──────────────────┐
         │   HISTORIAN      │ ← Sequential
         │   (Analysis)     │
         └────────┬─────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌──────────────┐    ┌──────────────┐
│  DESIGNER    │    │ COPYWRITER   │ ← Parallel
│  (Mockup)    │    │  (Copy)      │
└──────┬───────┘    └──────┬───────┘
       │                   │
       └─────────┬─────────┘
                 │
                 ▼
         ┌──────────────────┐
         │   DEVELOPER      │ ← Sequential
         │   (HTML/CSS/JS)  │
         └────────┬─────────┘
                  │
                  ▼
         ┌──────────────────┐
         │   OUTPUT         │
         │  Website File    │
         └──────────────────┘
```

---

## 📁 Project Structure

```
pillar-3-multi-agent/
├── agents.py           # All 4 agent implementations ✅ COMPLETE
├── state.py            # Shared state definition
├── test_setup.py       # Setup verification script
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
├── README.md           # This file
└── output/             # Generated websites (auto-created)
    └── apple_ii_website.html
```

---

## 🎯 What's Next

### Part 6: LangGraph Workflow

Build `workflow.py` to orchestrate agents with TRUE parallel execution using LangGraph's `StateGraph`.

**Key Features:**

- Conditional edges for error handling
- Real parallel execution (Designer + Copywriter simultaneously)
- Progress tracking and metrics
- Production-ready orchestration

**Coming Soon:**

```bash
python3 workflow.py  # LangGraph orchestration
```

---

## 💡 Key Learning Points

### 1. Multi-Agent Collaboration Pattern

- Agents are **functions** that transform state
- Each agent is a specialist with a single responsibility
- State is passed like a "baton" in a relay race

### 2. Parallel Execution

- Designer and Copywriter don't depend on each other
- Both only need the Historian's output
- LangGraph enables true concurrent execution

### 3. State Management

- `TypedDict` provides type safety and IDE support
- Clear contract: every agent knows what fields exist
- Runtime validation prevents errors

### 4. Prompt Engineering

- Each agent has a highly specialized system prompt
- Prompts include role definition, output format, and quality criteria
- Developer agent synthesizes all previous work

---

## 📝 Output Example

After running `python3 agents.py all`, you'll see:

```
⏳ Step 1/4: Running Historian...
   ✅ Complete: 2847 chars

⏳ Step 2/4: Running Designer...
   ✅ Complete: 3421 chars

⏳ Step 3/4: Running Copywriter...
   ✅ Complete: 2156 chars

⏳ Step 4/4: Running Developer (FINAL CODE GENERATION)...
   ✅ Complete: 15847 chars (~450 lines)

🎉 ALL FOUR AGENTS COMPLETE - WEBSITE GENERATED!

💾 Website saved to: output/apple_ii_website.html
🌐 Open this file in any web browser to see the result
```

---

## 🔧 Configuration

Edit `.env` to customize:

- `MODEL_NAME` - Change to `gpt-4` for higher quality (more expensive)
- `TEMPERATURE` - Control creativity (0.7 = balanced)

---

## 🐛 Troubleshooting

**Problem:** "OPENAI_API_KEY not found"

- **Solution:** Create `.env` file from `.env.example` and add your API key

**Problem:** Import errors

- **Solution:** Run `pip install -r requirements.txt`

**Problem:** Generated HTML doesn't render properly

- **Solution:** Check `output/apple_ii_website.html` - the Developer agent includes fallback error messages

---

## 🎬 Video Demo

This project demonstrates **Pillar 3: Collaboration** from The Architect's Playbook series.

**Watch the full tutorial:** [Link TBD]

**Next:** Pillar 4 - Reliability (Observability & Production Monitoring)

---

## 📄 License

Educational project for The Architect's Playbook YouTube series.

---

**Built with:** LangGraph, LangChain, OpenAI GPT-4o

**Author:** Atef Ataya
**YouTube:** [[Your Channel]](https://www.youtube.com/@atefataya/videos)
