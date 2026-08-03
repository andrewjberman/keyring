# W1 -- rcg_review_prep (procedure contract, v1)

Everything that leads INTO an Andrew review session. Deterministic except stage D.
Unit: one cycle of one sub-scan. Every output cites scan vintage (git HEAD SHA + date).

| Stage | Program | Output |
|---|---|---|
| A scan | bin/scan.py (classes + feature families, full nesting) | feature matrix -> rcg/scans/<vintage>/ (LOCAL) |
| B mark | bin/mark.py (root set -> typed edges -> reachability closure) | ACTIVE marks + active_strength; denominator + BOUNDARY DECLARATION printed |
| C score | bin/model.py score (per-root model) | disposition probs + uncertainty band, stamped model_version |
| D grade | AGENT (grader/INSTRUCTIONS.md binds) | confidence-scored proposals + evidence cards |
| E packet | bin/packet.py | cohort-ordered review packet: disagreements first, >=2 known-cruft + >=2 known-canonical PLANTED CONTROLS included |

Stage F (outside W1): the Andrew session -- ratify / override / rule at cohort grain.
HALT rule: if any planted control is misgraded in packet assembly self-check, the packet
does not ship (quarantine, MODEL_EVAL entry, fix first).
