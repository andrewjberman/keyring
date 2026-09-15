# LGIC_NAMING -- round 2 remediation slug

Author: 3.0.0_SA_CVO. Round: v2. Fabric: laptop. Recorded: 2026-09-15T01:07:23Z.

Input: `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468` (42 rows; 7 compiled at this L8). Adjudication: `ADJUDICATION_v3.md` (C-S13..C-S17), same slug. Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND2_L8_L9_20260915.md`.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. There is one row per item graduated this round (C-S14, W6-S4, W4-S1, W4-S2), plus the two rows owed from round 1's late carriers: S14 (C-S11) and S15 (C-S12). The four line-ending rows were dismissed (C-S16) and are not here. Every row is OPEN.

```json
[
 {
  "id": "LGIC_NAMING-C-S14",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "ROUND-2 L9, FWD-1, GRADUATED -- CVO OBSERVATION: all three namer differences (i03, i10, i11) are one reading of FN1's noun-phrase clause. Namer B wrote the phrase as named, vendor token included, although that token already sits in the system slot. The clause's text admits it, and its own example 'the Orion ingest' is item i03. So the split is the schema's.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v3.md (same slug) row LGIC_NAMING-C-S14",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND2_L8_L9_20260915.md (same slug)",
   "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-namer-a.tsv@eaafb46486",
   "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-namer-b.tsv@59f68115a4",
   "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n3-compare.md@ba8250b32a"
  ],
  "remedy": "One of two rulings. (a) Amend FN1 so the function never repeats a token already written in the system or scope slot, which is the ruled table's reading. (b) Rule namer B's reading legal and amend the three ruled names. Then re-run LN-e-1..LN-e-3 in the next issuance. FWD-1 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W6-S4",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "LN-e-5 round 2's E5R-AC1 invocation (check_ln_r2.py e5-correct) prints VERDICT: FAIL-MISREAD, not the expected PASS-ALL-CORRECT: the reader marked the key's firm-or-none token on 16 of 18 N3 names; i09 (mdpf-demo-publish-failure-alarm) is marked none where N3_KEY_R2.json reads demo, and i11 (pathfinder-etfs-ingest-task) is marked pathfinder where the key reads none.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W6-S4",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v3.md (same slug) row LGIC_NAMING-C-S15",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_NAMING_ROUND2_L8_L9_20260915.md (same slug)"
  ],
  "remedy": "Rule the class of demo (the spine's tick-list row 17) and whether FWD-2's 'unaided' reader may know that the first token is the system. Then re-key N3 and re-run LN-e-4/LN-e-5. The one-referent limb of FWD-2 is REALIZED; its reading limb is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W4-S1",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "LN-f-1-r2's worker face paraphrases the bd step as 'the vendor Black Diamond in a system or source position, and the firm 49 Financial otherwise -- as the rule says', but GRADING_RULE R3's test is ADJACENCY to a firm token, not position; read literally, the paraphrase reverses the reading of the 12 bd-* roles whose bd sits first with no firm token next to it. The r2 record follows R3's text.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W4-S1",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v3.md (same slug) row LGIC_NAMING-C-S17"
  ],
  "remedy": "Align LN-f-1's face paraphrase of the bd step with GRADING_RULE R3 (adjacency, not position) at any re-cut of the cell. No attribution moves.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-W4-S2",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "LN-f-1-r2 says both 'grade by GRADING_RULE.md' and 're-grade under NAMING_SCHEMA.json v1.6', and they part on the function slot. v1.6 resource.function (FN1, v1.5) writes an agent noun as its verb and never a kind word in the function. GRADING_RULE.md, written at v1.4 and not re-cut, reads the function as free vocabulary (R5) and keeps another type's kind in it (R6). 31 of LN-f-1's 68 canonical forms carry a kind word there. The r2 record follows the rule.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-W4-S2",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v3.md (same slug) row LGIC_NAMING-C-S17"
  ],
  "remedy": "One of two rulings. (a) A grade's canonical form applies FN1: GRADING_RULE.md gains a step and is re-cut to v1.6, and 31 of 68 LN-f-1 forms change their function slot. (b) FN1 binds a namer only, and the rule stays. No firm, scope or pattern catch moves either way.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S14",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "prd-signoff.py refuse exited rc=1 when a foreign commit landed on the shared index 16 s after the review commit. It left the new signoff JSON written to the worktree but uncommitted, and prd-signoff.py status then read that uncommitted file and reported the brief half REFUSED while HEAD still held the v1.4 SIGNED record.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-S14",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_NAMING-C-S11 (@8f291c8770)"
  ],
  "remedy": "Make prd_signoff_lib read the signoff directory at HEAD (git ls-tree + git show) for all four callers: prd-signoff.py status, to-pipeline-gate.py LIMB 6, prd-header-notify.py and prd-stamp.py. Prove it on a doctored pair: an uncommitted SIGNED file must not admit, and a committed one must.",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 },
 {
  "id": "LGIC_NAMING-S15",
  "project": "LGIC_NAMING",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The namers' briefing for the round-2 re-run carries 2 of the 18 ruled names verbatim: i05's bucket in the registry seed, and i15's ruled name as SY1's worked example in NAMING_SCHEMA.json v1.6. An identical answer on those two items can come from copying the briefing, so it is not independent evidence that two people derive the same name.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md@4c0866f468#LGIC_NAMING-S15",
   "org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/adjudications/ADJUDICATION_v2.md row LGIC_NAMING-C-S12 (@8f291c8770)",
   "org/standards/NAMING_SCHEMA.json@2706014705 :125 system.vendor_through_tiers"
  ],
  "remedy": "Replace NAMING_SCHEMA.json :125's worked example (orion-inf-build-gold-profile, item i15's ruled answer) with a name outside the N3 item set before any further namer run. Round 2's FWD-1 grade already reads i15 as not independent (C-S13, C-S14).",
  "owner": "1.0.0_SA_CTO",
  "round": "v2",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v2"
  },
  "closed": false
 }
]
```
