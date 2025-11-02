# 🚀 QUICK START - Developer Agent Demo

## Get Running in 3 Minutes

### Step 1: Setup (1 minute)

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file from template
cp env.example .env

# Edit .env and add your OpenAI API key
nano .env  # or use any editor
```

**In .env, replace:**

```
OPENAI_API_KEY=sk-proj-xxxxx
```

**With your actual key from:** https://platform.openai.com/api-keys

---

### Step 2: Verify Setup (30 seconds)

```bash
python3 test_setup.py
```

**Expected output:**

```
✓ Python version: 3.11+
✓ LangGraph version: 0.2.45
✓ LangChain version: 0.3.7
✓ OpenAI API Key: sk-proj-...
✓ State definition imported successfully
✓ Output directory exists
✅ ALL CHECKS PASSED - READY TO BUILD!
```

---

### Step 3: Run the Complete Workflow (2-3 minutes)

```bash
python3 agents.py all
```

**This will:**

1. ✅ Analyze the 1977 Apple II brochure (Historian)
2. ✅ Create design specifications (Designer)
3. ✅ Write website copy (Copywriter)
4. ✅ Generate complete HTML/CSS/JS (Developer) ✨ NEW
5. ✅ Save to `output/apple_ii_website.html`

**Expected output:**

```
⏳ Step 1/4: Running Historian...
   ✅ Complete: ~2800 chars

⏳ Step 2/4: Running Designer...
   ✅ Complete: ~3400 chars

⏳ Step 3/4: Running Copywriter...
   ✅ Complete: ~2100 chars

⏳ Step 4/4: Running Developer (FINAL CODE GENERATION)...
   ✅ Complete: ~15000 chars (~450 lines)

🎉 ALL FOUR AGENTS COMPLETE - WEBSITE GENERATED!
💾 Website saved to: output/apple_ii_website.html
```

---

### Step 4: View the Result (10 seconds)

**Option A - Direct Browser:**

```bash
# macOS
open output/apple_ii_website.html

# Linux
firefox output/apple_ii_website.html

# Windows
start output/apple_ii_website.html
```

**Option B - HTTP Server:**

```bash
cd output
python3 -m http.server 8000
# Then open: http://localhost:8000/apple_ii_website.html
```

---

## 🎯 Test Individual Agents

Want to test specific agents?

```bash
# Test only Historian
python3 agents.py historian

# Test Historian + Designer
python3 agents.py designer

# Test Historian + Copywriter
python3 agents.py copywriter

# Test up to Developer (all 4)
python3 agents.py developer

# Demo parallel execution
python3 agents.py parallel
```

---

## 🐛 Common Issues

### ❌ "OPENAI_API_KEY not found"

**Fix:** Create `.env` file:

```bash
cp env.example .env
# Add your API key to .env
```

### ❌ Import errors

**Fix:** Install dependencies:

```bash
pip install -r requirements.txt
```

### ❌ "Permission denied" on output directory

**Fix:** Create output directory manually:

```bash
mkdir -p output
chmod 755 output
```

---

## 📊 What You'll See

### Terminal Output:

- Real-time progress for each agent
- Character counts for each output
- Validation checks (HTML structure, CSS presence)
- File save confirmation

### Generated Website:

- Complete single-page HTML file
- 1977 Apple II aesthetic
- Modern responsive design
- All sections from Copywriter
- Smooth animations
- Production-ready code

---

## 🎬 For Your Video Demo

### Recording Sequence:

**1. Show Setup (15 seconds):**

```bash
python3 test_setup.py
```

**2. Run Workflow (Show terminal):**

```bash
python3 agents.py all
```

**3. Show File Generated:**

```bash
ls -lh output/apple_ii_website.html
wc -l output/apple_ii_website.html
```

**4. Open in Browser (Screen record):**

```bash
open output/apple_ii_website.html
```

**5. Show Code Preview:**

```bash
head -50 output/apple_ii_website.html
```

---

## 💡 Pro Tips

**Faster iteration:**

```bash
# Skip parallel demo, just run all
python3 agents.py all
```

**Debugging:**

```bash
# Test each agent individually first
python3 agents.py historian
python3 agents.py designer
python3 agents.py copywriter
python3 agents.py developer
```

**Different brochure:**
Edit `agents.py` line 372 (or wherever the brochure URL is set):

```python
"brochure_url": "https://your-custom-brochure-url/",
```

---

## ✨ What's Next?

### Phase 2: LangGraph Workflow

- `workflow.py` - TRUE parallel execution
- Designer + Copywriter run simultaneously
- Advanced error handling
- Progress visualization

**Status:** Ready to implement  
**ETA:** 2-3 hours

---

## 📚 Full Documentation

- **README.md** - Complete user guide
- **IMPLEMENTATION_SUMMARY.md** - Technical details
- **Inline comments** - Code documentation

---

## 🎉 You're Ready!

The Developer Agent is complete and tested. Run the workflow above to generate your first AI-created website!

**Have fun building! 🚀**
