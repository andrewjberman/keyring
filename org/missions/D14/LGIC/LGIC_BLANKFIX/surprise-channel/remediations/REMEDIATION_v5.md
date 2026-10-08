# LGIC_BLANKFIX -- remediations, round 6

<sweep_watermark>2026-10-08T20:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-08 ~20:4xZ. Graduated at this compile (ADJUDICATION_v5.md): 3 rows, 1 ARMED, none closed.
Clocks advanced in REMEDIATION_v4.md: S6 and S7 REMEDIATED. S8 stays OPEN: the repeat limb of
`deliverables/0.9.0_WK_LGIC_BLANKFIX~2/check_all_roots_round5.py` reads `repeat=identical`, but on the trunk at 7b9efd885f the same script
prints `FAIL: investor-reporting/ycharts: the saved run differs from the live run` and `ok=False`. Commit 51f4545acd shifted two
`[where]` line numbers in `generate.tf` (253 to 260, 270 to 277); the verdicts did not change. S8's remedy is unchanged in kind:
compare without the line number, or on a pinned commit. Carried open from REMEDIATION_v1.md: W2-S2 (no commit has touched the
test or GRADING_RULE.md since round 5).

```json
[
  {
    "id": "LGIC_BLANKFIX-W1-S14",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "lib/opal_naming_scope.root_items enumerates only names written as literals, so a root that builds its names in a local, through a module (opal_name, partner-firm-table, served-guard) or in a generated .json file prints names=0 or a partial count. The registry reads names=0 as a root with nothing to name, and a mapped root's check never grades the missing names.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 7b9efd885f row W1-S14",
      "adjudication row LGIC_BLANKFIX-C-S16"
    ],
    "remedy": "P1. The CTO rules how the enumeration follows a local, a module call and a .json input. Until then, no entry says names: none on a names=0 reading alone, and the 11 roots keep their DECLARES-NAMES verdict. Done when the enumeration reports the names of the 11 roots and of the 5 partly-read roots, or each of them is refused by name.",
    "owner": "1.0.0_SA_CTO",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-10-08T23:20Z"
    }
  },
  {
    "id": "LGIC_BLANKFIX-W1-S15",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CLAUDE.md rule 30 (line 197) says the commit-time naming gate grades names 'WARN today'; org/mcp/naming-gate.enforce is present, so the gate refuses with rc=1. A seat that reads the law expects a warning and gets a refusal.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 7b9efd885f row W1-S15",
      "adjudication row LGIC_BLANKFIX-C-S16"
    ],
    "remedy": "P2. CLAUDE.md is locked; the CTO carries the correction to Andrew for a law-edit order. Done when rule 30 states the mode the switch file sets.",
    "owner": "1.0.0_SA_CTO",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-S10",
    "project": "LGIC_BLANKFIX",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "BF-u-1's 74 drafted root-map entries leave 180 fields UNDECIDED (source 51, fills 49, scope 33, exceptions 26, system 19, why 2), so 73 of the 74 cannot land and FWD-7 and FWD-2 breadth stays at 13 of 87 roots.",
    "evidence": [
      "org/missions/D14/LGIC/LGIC_BLANKFIX/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD 7b9efd885f row S10",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/ROOT_MAP_ROUND6_NOTES_20261008.md @6091606dd8",
      "adjudication row LGIC_BLANKFIX-C-S16"
    ],
    "remedy": "P1. The round-7 analysis cuts the measurement of the 180 fields and rules on the CRO's recommendation to retire the two empty roots as dead Terraform. Done when every drafted entry either loads or names the one field still owed and its owner.",
    "owner": "1.0.0_SA_CTO",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v7"
    },
    "closed": false
  }
]
```
