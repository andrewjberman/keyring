# AMGT_RESAPP round 105 (workstream AIFILL) -- L10 slug HELD

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T04:40Z.

**Gate:** `python .tools/round-close-check.py --project AMGT_RESAPP --round 105 --workstream AIFILL` reads `verdict=REFUSED`:
`PROOF-BAD AMGT_RESAPP.TO-AMGT-fc-4.the-revalidate-command-checks-every-stored-document: FAIL row(s) AC1`.

**What it is:** the worker ~433's proof instance
(`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~433/AMGT_RESAPP.TO-AMGT-fc-4.the-revalidate-command-checks-every-stored-document.proof_of_spec.json`)
still records AC1 FAIL from the run before amendment 98f59d6f87. This seat re-ran the amended check: `AIFILL FC-4 ARMS: YES (11 of 11)`. The code is sound and
the instance is stale.

**Un-parks when:** the issuer re-seats the fc-4 proof instance (or the CTO rules on it) and round-close-check reads MAY-CLOSE. Owner: 2.0.0_SA_COO~R2.

**Compile already committed:** `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/adjudications/ADJUDICATION_v129.md`, `remediations/REMEDIATION_v42.md`.
FWD-41's five-name read is graded NOT MET there (C-S143). Round 104 workstream AIFILLLAND (ar-5, ar-6) reads MAY-CLOSE on its own.
