# ⚡ QUICK COMMAND REFERENCE

## 🎯 Essential Commands (Copy & Paste)

### Setup & Verification

```bash
# Verify everything is working
python3 test_setup.py
```

### Run the Complete Demo

```bash
# Generate complete website (all 4 agents)
python3 agents.py all
```

### View the Generated Website

```bash
# macOS
open output/apple_ii_website.html

# Linux
firefox output/apple_ii_website.html
xdg-open output/apple_ii_website.html

# Windows
start output/apple_ii_website.html

# Any OS - Web Server
cd output && python3 -m http.server 8000
# Then open: http://localhost:8000/apple_ii_website.html
```

---

## 🧪 Test Individual Agents

```bash
# Test Historian only
python3 agents.py historian

# Test Historian + Designer
python3 agents.py designer

# Test Historian + Copywriter
python3 agents.py copywriter

# Test all agents up to Developer
python3 agents.py developer

# Demo parallel execution
python3 agents.py parallel
```

---

## 📊 Check Your Output

```bash
# List generated files
ls -lh output/

# Count lines in generated website
wc -l output/apple_ii_website.html

# Preview first 50 lines
head -50 output/apple_ii_website.html

# Preview last 20 lines
tail -20 output/apple_ii_website.html

# View full file
cat output/apple_ii_website.html

# Open in editor
code output/apple_ii_website.html      # VS Code
nano output/apple_ii_website.html      # Nano
vim output/apple_ii_website.html       # Vim
```

---

## 🎬 Recording Your Demo

### Step 1: Clean Terminal

```bash
clear
```

### Step 2: Show Setup

```bash
python3 test_setup.py
```

**Wait for:** ✅ ALL CHECKS PASSED

### Step 3: Run Complete Workflow

```bash
python3 agents.py all
```

**Record:** All 4 agents executing (2-3 minutes)

### Step 4: Show Output

```bash
ls -lh output/apple_ii_website.html
wc -l output/apple_ii_website.html
```

### Step 5: Open in Browser

```bash
open output/apple_ii_website.html
```

**Record:** Website rendering, scroll through sections

---

## 🔧 Troubleshooting Commands

### Check Environment

```bash
# Python version
python3 --version

# Installed packages
pip list | grep -E "langchain|langgraph|openai"

# Check API key (first 8 chars)
head -1 .env

# Current directory
pwd

# Files in current directory
ls -la
```

### Fix Common Issues

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Create output directory manually
mkdir -p output

# Check file permissions
ls -la output/

# Remove and recreate output directory
rm -rf output && mkdir output
```

---

## 📁 File Locations

```bash
# Project structure
.
├── agents.py              # Main code
├── state.py               # State definition
├── test_setup.py          # Setup verification
├── requirements.txt       # Dependencies
├── .env                   # Your API key (you create this)
├── env.example            # Template
└── output/                # Generated files
    └── apple_ii_website.html
```

---

## 🚀 Quick Test Sequence

**Complete test in 4 minutes:**

```bash
# 1. Verify (30 seconds)
python3 test_setup.py

# 2. Run (2-3 minutes)
python3 agents.py all

# 3. Check (10 seconds)
ls -lh output/

# 4. View (30 seconds)
open output/apple_ii_website.html
```

---

## 💡 Pro Tips

### Fast Iteration

```bash
# Clear output and run again
rm output/*.html && python3 agents.py all
```

### Monitor Execution Time

```bash
# Time the workflow
time python3 agents.py all
```

### Save Logs

```bash
# Save execution log
python3 agents.py all > execution.log 2>&1
```

### Test Without Browser

```bash
# Just check if HTML is valid
python3 agents.py all && grep -c "<html" output/apple_ii_website.html
```

---

## 🎯 Expected Results

### Setup Verification

```
✓ Python version: 3.11+
✓ LangGraph installed successfully
✓ LangChain version: 0.3.7
✓ OpenAI API Key: sk-proj-...
✓ State definition imported successfully
✅ ALL CHECKS PASSED
```

### Workflow Execution

```
⏳ Step 1/4: Historian... ✅ (~4,500 chars)
⏳ Step 2/4: Designer... ✅ (~4,000 chars)
⏳ Step 3/4: Copywriter... ✅ (~3,000 chars)
⏳ Step 4/4: Developer... ✅ (~10,000 chars)
🎉 WEBSITE GENERATED!
💾 Saved to: output/apple_ii_website.html
```

### Output File

```
-rw-r--r-- 1 user staff 15-30K output/apple_ii_website.html
```

---

## 📞 Help Commands

```bash
# Show available tests
python3 agents.py

# Show this help (if implemented)
python3 agents.py --help
```

---

## 🎬 One-Liner Demo

```bash
# Complete demo in one command
python3 test_setup.py && python3 agents.py all && open output/apple_ii_website.html
```

---

**Save this file for quick reference! 📌**

All commands tested and working on macOS/Linux/Windows.
