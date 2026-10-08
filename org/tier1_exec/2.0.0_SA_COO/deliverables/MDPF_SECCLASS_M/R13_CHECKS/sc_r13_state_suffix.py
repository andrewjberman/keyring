"""sc_r13_state_suffix.py -- MDPF_SECCLASS round 13 cell SC-e-74 check: clean_name() drops a "/<state>" incorporation suffix.

READ-ONLY, no AWS. 1.0.0_SA_CTO~DELL1 msg 1039 (SECHIST round-1 analysis 0141533760 section 2.2): clean_name() keeps the "/<state>"
incorporation suffix ("Cisco Systems Inc/Delaware"), which etf_positioning_publisher._display_name serves from the table row's name.
The rule: a trailing "/<US state name or postal code>" or "/NEW", optionally closed by "/", repeated, and ONLY directly after a
corporate-form token (Inc, Corp, Co, Ltd, LLC, LP, PLC, ...), is dropped. A slash anywhere else stays (dates, "LARGE/MID", "MUNI/CA").
Every case is also checked for idempotence: clean_name(clean_name(x)) == clean_name(x).
Run from the repo root you are grading.
Prints  STATE-SUFFIX ok=<bool> cases=<n> pass=<n> first_miss=[...]
"""
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "infra/aws/lambda/v2_portal/_shared"))

STRIPPED = [
    ("Cisco Systems Inc/Delaware", "Cisco Systems Inc"),
    ("CISCO SYSTEMS INC /DE/", "Cisco Systems Inc"),
    ("Acme Corp/MD", "Acme Corp"),
    ("ACME HOLDINGS INC/NEW/", "Acme Holdings Inc"),
]
# Controls: today's output, unchanged (measured at dell1 CLOUD 2026-10-08 ~18:2xZ).
UNCHANGED = [
    ("Delaware ST 5% 03/01/2032", "Delaware ST 5% 03/01/2032"),
    ("DELAWARE ST 5 03/01/2032", "Delaware ST 5 03/01/2032"),
    ("Timothy Plan LARGE/MID Cap Growth C", "Timothy Plan LARGE/MID Cap Growth C"),
    ("PIMCO CA INTERMEDIATE MUNI/CA", "PIMCO Ca Intermediate MUNI/CA"),
    ("Call US Natural Gas FD $16.5 Exp 02/04/26", "Call US Natural Gas FD $16.5 Exp 02/04/26"),
    ("New York Times Co", "New York Times Co"),
    ("AT&T INC", "AT&T Inc"),
    ("CISCO SYSTEMS INC", "Cisco Systems Inc"),
]


def main():
    from security_name import clean_name
    cases = STRIPPED + UNCHANGED
    miss = []
    for raw, want in cases:
        got = clean_name(raw)
        if got != want or clean_name(got) != got:
            miss.append((raw, got, want))
    ok = not miss
    print(f"STATE-SUFFIX ok={ok} cases={len(cases)} pass={len(cases) - len(miss)} first_miss={miss[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
