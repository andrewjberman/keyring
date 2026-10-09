# LGIC_BLANKFIX -- remediations, round 7

<sweep_watermark>2026-10-08T23:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-08 ~23:2xZ. Graduated at this compile (ADJUDICATION_v6.md): 2 rows, INERT, not closed.

Clocks advanced:
- **S8 REMEDIATED** (REMEDIATION_v4.md). Its done-when holds: `check_all_roots_round5.py` reads `ALL-ROOTS-R5 ok=True ...
  repeat=identical` on the trunk after BF-v-6, with names added to mapped roots.
- **W1-S14 REMEDIATED and DISARMED** (REMEDIATION_v5.md). Its done-when holds by this seat's run at 45e2856e41:
  - `check_declares_names.py` reads `still_zero=0` over the 11 roots, and each prints names or `uncounted` above 0.
  - Of the 5 partly-read roots, transcripts (`uncounted=10`), modules/served-guard (`uncounted=4`) and served-guard-inf
    (`uncounted=1`) print their hidden names as UNCOUNTED. The two now mapped, mdpf-secclass/sector-writer and
    investor-reporting/reporting-read, carry 1 and 4 UNCOUNTED lines.
  - The hazard was a name hidden behind a zero, and it now prints. Grading those names is FWD-2's breadth
    (`uncounted=301`), not this row.

Still OPEN:
- **S10** (REMEDIATION_v5.md): 180 UNDECIDED fields became 47; 50 of 74 entries landed and 24 are held. A keyword read of the 24
  held entries' evidence finds an owner named in 10. The done-when ("every drafted entry either loads or names the one field
  still owed and its owner") is not met.
- **W1-S15:** Andrew's act.
- **W2-S2:** no commit since round 5.

```json
[
  {
    "id": "LGIC_BLANKFIX-W4-S3",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lib/opal_naming_cadence.py builds cadence rows only for literal names, while the scope (after BF-v-4) also counts names built in locals; a local-built schedule in a mapped root then has no cadence row and prints a HOLE that its own expression could fill.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 45e2856e41 row W4-S3",
      "adjudication row LGIC_BLANKFIX-C-S18"
    ],
    "remedy": "P1. The cadence reader resolves the same locals the scope resolves. Done when investor-reporting/intake's irpt-intake-poll prints FIX or RIGHT, or a HOLE whose cause is its expression, not the missing row.",
    "owner": "1.0.0_SA_CTO",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-S11",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "BV4-AC3's instrument check_declares_names.py reads only UNMAPPED lines, so each of the 11 roots that the registry's lane maps reads MISSING and the script prints ok=False although still_zero=0.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 45e2856e41 row S11",
      "adjudication row LGIC_BLANKFIX-C-S18"
    ],
    "remedy": "P2. The instrument reads a mapped root's ROOT line (items) and UNCOUNTED lines as well. Done when it prints DECLARES-CHECK ok=True on the trunk with the 11 roots mapped or not.",
    "owner": "2.0.0_SA_COO~G",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G",
      "round": "v8"
    },
    "closed": false
  }
]
```
