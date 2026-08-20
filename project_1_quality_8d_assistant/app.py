import re
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent / "sample_incidents.csv"

def extract_fields(text: str):
    patterns = {
        "fault_code": r"\b(?:SPN\d+(?:\s*FMI\d+)?|P\d{6}|B\d{6})\b",
        "mileage": r"\b(\d{3,6})\b",
    }
    fault = re.findall(patterns["fault_code"], text, flags=re.I)
    mileage = re.findall(patterns["mileage"], text)
    return {
        "fault_codes": list(dict.fromkeys(fault)),
        "numbers_found": mileage[:5],
    }

def five_whys_hypotheses(complaint: str):
    c = complaint.lower()
    if "communication" in c:
        return [
            "Why did communication fail? Possible intermittent network communication interruption.",
            "Why could communication be interrupted? Possible power, ground, connector, wiring, or network integrity issue.",
            "Why would the issue be intermittent? Possible temperature, vibration, moisture, or connection-dependent condition.",
            "Why was the condition not prevented? Existing diagnostic/connection controls may not detect the intermittent condition.",
            "Why did the issue reach the customer/field? Root cause and detection controls require validation against the failure evidence.",
        ]
    if "speedometer" in c or "speed" in c:
        return [
            "Why is vehicle speed implausible? Possible loss or corruption of vehicle-speed data.",
            "Why could data be corrupted? Possible sensor, harness, connector, network, or controller issue.",
            "Why is the event intermittent? Possible vibration, thermal, moisture, or connection sensitivity.",
            "Why was it not detected earlier? Existing diagnostics may not capture the transient event.",
            "Why did it reach the field? Detection and robustness controls should be reviewed after root cause is confirmed.",
        ]
    return [
        "Why did the customer observe the symptom? Failure mechanism requires confirmation.",
        "What changed before the event? Review environment, operating condition, software, hardware and service history.",
        "What evidence supports each hypothesis? Separate observed facts from assumptions.",
        "What containment is possible? Protect the customer while root cause is investigated.",
        "What validation is required? Reproduce the failure and confirm the mechanism before corrective action.",
    ]

def corrective_actions(complaint: str):
    return [
        "Capture complete diagnostic snapshot before power cycling or clearing faults.",
        "Inspect relevant connectors, grounds, harness routing and physical damage.",
        "Check software/calibration versions and recent configuration changes.",
        "Attempt controlled reproduction across temperature, vibration and key-cycle conditions.",
        "Confirm root cause with evidence before implementing permanent corrective action.",
    ]

def build_8d(row):
    complaint = str(row["complaint"])
    extracted = extract_fields(complaint)
    return {
        "D1 Team": "Quality + Manufacturing/Service + Controls/Diagnostics + Design Engineering",
        "D2 Problem": complaint,
        "D3 Containment": "Capture diagnostics, identify affected units/configurations, and prevent repeat exposure where practical.",
        "D4 Root Cause Hypotheses": five_whys_hypotheses(complaint),
        "D5 Corrective Actions": corrective_actions(complaint),
        "D6 Validation": "Reproduce the failure, verify the corrective action under representative operating conditions, and confirm no unintended effects.",
        "D7 Prevention": "Update control plan, diagnostic guidance, PFMEA/service documentation and lessons learned as applicable.",
        "D8 Closure": "Obtain cross-functional approval after evidence, validation and documentation are complete.",
        "Extracted": extracted,
    }

def main():
    df = pd.read_csv(DATA)
    print("\nAI QUALITY & 8D ASSISTANT\n")
    print("Available incidents:")
    for _, r in df.iterrows():
        print(f"  {r.incident_id}: {r.component} | {r.fault_code}")

    incident_id = input("\nEnter incident ID (e.g., Q-1001): ").strip()
    match = df[df.incident_id.str.upper() == incident_id.upper()]
    if match.empty:
        raise SystemExit("Incident not found.")

    row = match.iloc[0]
    result = build_8d(row)

    print("\n--- DRAFT 8D ---")
    for section, value in result.items():
        print(f"\n{section}:")
        if isinstance(value, list):
            for item in value:
                print(f"  - {item}")
        else:
            print(value)

    print("\nHUMAN VALIDATION REQUIRED: Treat all hypotheses and actions as recommendations, not confirmed engineering conclusions.")

if __name__ == "__main__":
    main()
