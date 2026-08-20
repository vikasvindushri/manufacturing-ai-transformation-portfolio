# Manufacturing AI Portfolio

Three practical AI transformation projects designed for a Manufacturing / Quality / Operations AI Specialist portfolio.

## Projects

1. **AI Quality & 8D Assistant**
   - Extracts structured information from quality incidents
   - Generates a draft 8D analysis
   - Suggests 5-Why and corrective-action candidates
   - Keeps human validation in the loop

2. **Manufacturing Knowledge Assistant (RAG)**
   - Searches engineering/quality knowledge semantically
   - Returns evidence-backed answers with source references
   - Includes a simple local TF-IDF retrieval implementation
   - Designed so Gemini/other LLMs can be added later

3. **Low-Code Manufacturing AI Agent**
   - Demonstrates an AI-driven workflow for manufacturing fault triage
   - Classifies an issue, identifies likely causes, recommends diagnostic checks
   - Creates a structured action record
   - Includes a workflow architecture suitable for AppSheet/Power Apps/Workspace Studio

## Business capabilities demonstrated

- Generative AI literacy
- Manufacturing process improvement
- Quality / RCA / 8D / PFMEA thinking
- AI use-case identification
- Retrieval-augmented generation concepts
- Structured extraction
- Human-in-the-loop governance
- Low-code/no-code solution design
- ROI and adoption thinking
- Python, pandas and lightweight analytics
- Stakeholder-ready documentation

## Run

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Run the demos:

```bash
python project_1_quality_8d_assistant/app.py
python project_2_manufacturing_rag_assistant/app.py
python project_3_low_code_ai_agent/app.py
```

No API key is required for the portfolio demos. They intentionally use deterministic/local logic so recruiters can clone and run them immediately.

For production, replace the local generation/retrieval layer with an approved enterprise model such as Gemini and an enterprise-approved knowledge source.

## Suggested GitHub positioning

Repository name:

`manufacturing-ai-transformation-portfolio`

Suggested profile description:

> Practical AI transformation projects applying Generative AI, RAG, low-code automation, quality engineering, and continuous improvement to manufacturing operations.

## Governance note

These demonstrations are decision-support prototypes. AI outputs must be validated by qualified personnel before being used for engineering, quality, safety, production, or customer decisions.
