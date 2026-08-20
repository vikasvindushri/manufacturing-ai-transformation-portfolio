import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / "sample_cases.csv"

def classify(symptom):
    s = symptom.lower()
    if any(x in s for x in ["communication", "network", "controller"]):
        return "Controls / Communication"
    if any(x in s for x in ["battery", "voltage", "crank", "power"]):
        return "Electrical / Power"
    if any(x in s for x in ["failure", "quality", "component"]):
        return "Quality / Reliability"
    if any(x in s for x in ["cycle", "delay", "production", "station"]):
        return "Production / Process"
    return "General Manufacturing"

def recommend(category):
    recommendations = {
        "Controls / Communication": [
            "Capture active and historical diagnostic information before clearing faults.",
            "Verify supply, grounds, connectors and network integrity.",
            "Check for temperature/vibration/key-cycle dependency.",
            "Compare software/configuration versions.",
        ],
        "Electrical / Power": [
            "Capture voltage during the event.",
            "Check battery state, connections, grounds and voltage drop.",
            "Verify charging/power-management behavior.",
        ],
        "Quality / Reliability": [
            "Define the failure mode and affected population.",
            "Review warranty/field history and PFMEA.",
            "Separate containment from permanent corrective action.",
            "Validate the failure mechanism with controlled testing.",
        ],
        "Production / Process": [
            "Measure actual cycle time and waiting time.",
            "Identify the bottleneck and sources of variation.",
            "Check material, tooling, staffing and upstream/downstream constraints.",
            "Pilot the improvement and measure before/after performance.",
        ],
        "General Manufacturing": [
            "Clarify the problem statement and collect objective evidence.",
            "Map the current process and identify the bottleneck.",
            "Evaluate whether automation or AI can address the identified cause.",
        ],
    }
    return recommendations.get(category, recommendations["General Manufacturing"])

def run_agent(symptom, severity="Medium"):
    category = classify(symptom)
    return {
        "classification": category,
        "severity": severity,
        "likely_causes": [
            "Process or equipment condition",
            "Electrical/connection/software condition where applicable",
            "Environmental or operating condition",
        ],
        "recommended_checks": recommend(category),
        "human_approval": "Required before engineering, safety, quality or production action.",
    }

def main():
    print("\nLOW-CODE MANUFACTURING AI AGENT\n")
    symptom = input("Describe the manufacturing issue: ").strip()
    severity = input("Severity [Low/Medium/High]: ").strip().title() or "Medium"

    result = run_agent(symptom, severity)

    print("\n--- AI TRIAGE RESULT ---")
    print(f"Category: {result['classification']}")
    print(f"Severity: {result['severity']}")

    print("\nLikely cause categories:")
    for item in result["likely_causes"]:
        print(f"- {item}")

    print("\nRecommended checks:")
    for item in result["recommended_checks"]:
        print(f"- {item}")

    print(f"\nGovernance: {result['human_approval']}")

if __name__ == "__main__":
    main()
