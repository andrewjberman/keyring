# IRPT_BCKEND: remediations, round 170 (workstream ~P)

<sweep_watermark>2026-10-13T03:00Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T03:00:00Z. Follows ADJUDICATION_v71. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_170_P_DRAIN_END_20261013.md` (blob 2a2a48a86b, msg 6762). No judgment criterion.
Graduated, round label v171: 6 rows, OPEN, owner `2.0.0_SA_COO~P2`; ARMED 4.
- **D2-W345-S3 (ARMED):** the live 49 Financial build leaves a temp file carrying client account numbers on every run. The host and the
  persistence of its temp space are not measured.
- D2-W344-S1: the producer pair's ORDER, per this seat's v0.52 condition: both packaged schema copies re-pin and deploy before the builder
  writes account_id.
- D2-W344-S2 (ARMED), D2-W346-S2 and D2-W346-S3 (ARMED), D2-W346-S4: a builder cell and a portal cell, as the packet carries.
Still OPEN: D2-S121 (the release's changed branch unexercised live, CTO).

```json
[
 {
  "id": "IRPT_BCKEND-D2-W345-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The live 49 Financial entry point copies the Tax membership snapshot, which carries client account numbers, to a local system temp file on every build and never removes it.",
  "evidence": [
   "investigation row D2-W345-S3",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_170_P_DRAIN_END_20261013.md"
  ],
  "remedy": "The live 49 Financial entry point (build_49f_meshed via holdings_snapshot.retained_capture) copies the Tax membership snapshot, which carries client account numbers, to a system temp file on every build and never removes it. A builder cell writes it to memory or removes it in a finally. Until then the rule in row D2-S122 holds: no seat calls retained_capture or build_49f_meshed outside the scheduled runner. The cell also names WHICH host runs the scheduled build and whether its temp space persists; that is not measured.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v171",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v171"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W344-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "infra/aws/lambda/investor-reporting/_ids/raw_keys.json, firms.49financial.account.holdings_source (line 11) names smartx fact_allocation_account_map.account_number with citation holdings_snapshot.py:352-353. The live 49F ACCOUNT node id is minted by holdings_49f.py:339 from the Schwab dim_balance.account_id (the custody key as read). The declared holdings_source therefore does not describe the 49F custody node's key. This order added a new node_account_id_member key stating the live rule and left holdings_source unchanged (not in the order's grant to correct).",
  "evidence": [
   "investigation row D2-W344-S2",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_170_P_DRAIN_END_20261013.md"
  ],
  "remedy": "raw_keys.json firms.49financial.account.holdings_source names the smartx allocation map while the live builder reads Schwab dim_balance.account_id. Correct the declared key, with a citation to the live mint, in the builder cell, before anything mints or audits 49 Financial account ids from this file.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v171",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v171"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W346-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "fe-s-15/gen-fixtures.ts does not reproduce its committed job.*.json at HEAD: a regeneration drops the unprojected_grant block and adds status.internal_correlation_id; the five job files were left at HEAD bytes and still carry the old section.",
  "evidence": [
   "investigation row D2-W346-S2",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_170_P_DRAIN_END_20261013.md"
  ],
  "remedy": "fe-s-15/gen-fixtures.ts does not reproduce its committed job files at HEAD, so a regeneration would undo the round-170 hand edit. A portal cell repairs the generator so that it reproduces the committed bytes, before anyone regenerates.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v171",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v171"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W346-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "fe-s-18/gen-fixtures.ts cannot run at HEAD (it reads a bare holdings key that the committed wire map does not carry), so its maps were not regenerated; its partial run drifted fe-s-18-frozen.json beyond the section, which was restored, and that file still carries the old section.",
  "evidence": [
   "investigation row D2-W346-S3",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_170_P_DRAIN_END_20261013.md"
  ],
  "remedy": "fe-s-18/gen-fixtures.ts cannot run at HEAD (it reads a holdings key the committed wire map lacks). Repaired in the same portal cell as D2-W346-S2.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v171",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v171"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_BCKEND-D2-W344-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "TO-IB-pr-493 edits docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json (with its two byte-identical copies). Two Lambdas stage that docs copy and pin its sha256 in infra/aws/lambda/ci/lambda-source-map.json: irpt-ycharts-generate (function key line 3990; docs-copy row lines 4316-4319, pin 3f29017cfc, sha256 0236991c...) and irpt-holdings (function key line 5029; docs-copy row lines 5119-5122, pin 4cc72587d6, sha256 fde5dd41...). Both pins are stale after this edit. lambda-source-map.json is not edited (not in the order's paths).",
  "evidence": [
   "investigation row D2-W344-S1",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_170_P_DRAIN_END_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_PRD_v0.52_RATIFIED_TEXT_REVIEW_20261013.md @cab1de19b0"
  ],
  "remedy": "The two lambda-source-map.json pins of the docs HoldingsSnapshot copy (:4316 irpt-holdings, :5119 irpt-ycharts-generate) are stale. Per this seat's v0.52 condition: the producer pair re-pins and deploys BOTH packaged copies before the gold-runner builder first writes account_id, because the old node schema has additionalProperties false and holdings/snapshot.py validates every answer at serve.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v171",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v171"
  },
  "closed": false
 },
 {
  "id": "IRPT_BCKEND-D2-W346-S4",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The producer ExportBundle fixture and its portal mirrors still name selected_sections S-RET-1, which the producer AnalysisReport no longer carries as a section_id; left unchanged because the mirror agrees with the producer.",
  "evidence": [
   "investigation row D2-W346-S4",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_170_P_DRAIN_END_20261013.md"
  ],
  "remedy": "The producer ExportBundle fixture and its portal mirrors still name selected_sections S-RET-1, a section_id the producer AnalysisReport no longer carries. Align them in the portal fixture follow-up, as was done for AnalysisReport.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v171",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v171"
  },
  "closed": false
 }
]
```
