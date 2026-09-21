# IRPT_FNTEND -- round 9 remediation slug

Author: 3.0.0_SA_CVO. Round: v9. Fabric: laptop. Recorded: 2026-09-21T19:00:39Z.

Input: `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8` (round 9's 17 new rows, filed against issuance `07faf174d2`, decomposition cut `6f56917cef`). Adjudication: `ADJUDICATION_v3.md` (C-S109..C-S115), same slug. L8 packet: msgs 99139/99140 (`2.0.0_SA_COO~F`).

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. NEW FILE, not a mutation of `REMEDIATION_v5.md` -- both rows below are freshly minted this round (their ids were absent from every prior remediation file; a remediation row's clock is a birth property and is never retrofitted onto a row that never carried one).

STATES: 2 rows, both OPEN / ARMED. Round 9 also closed four OPEN rows minted at round 8 (`IRPT_FNTEND-W2-S35`, `W4-S19`, `W4-S20`, `S68`) -- recorded as an in-place clock advance on `REMEDIATION_v5.md` itself (the gate's own admitted move), not here.

```json
[
 {
  "id": "IRPT_FNTEND-W3-S43",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "eslint.config.js's globalIgnores(['dist','.runtmp/**','.frontend-dev/**']) does not exclude .vite/**, so a transient, gitignored .vite/deps* Vite dev-server build cache -- left behind by any test run that starts a real dev server -- gets scanned by `bun run lint` and produces spurious 'Definition for rule ... was not found' errors against vendor bundle code that was never authored by this project. ESCALATED FROM EXPOSURE TO INCIDENT AT THIS L9: independently re-run by 3.0.0_SA_CVO's own verification fork at HEAD, live, not inherited from the filer -- `bun run lint` returned 166 problems (66 errors, 100 warnings), and all 66 errors trace to `.vite/deps_temp_*/...js` paths. Per CLAUDE.md Rule 22's negative mirror (absent != exercised-against): this was a suspected hazard until measured; it is now a measured one. FE-s-52's own 5 named lint-error fixes are independently confirmed correct and unaffected -- this defect sits beside them, in the tool's own scan surface, not in the delivered fix.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W3-S43",
   "portal f4c9ec46:eslint.config.js globalIgnores(['dist','.runtmp/**','.frontend-dev/**']) -- no .vite exclusion",
   "portal .gitignore:17 ignores .vite (confirming the cache is legitimately untracked, not a stray commit)",
   "3.0.0_SA_CVO verification fork, this L9, 2026-09-21: `cd portal && bun run lint` at HEAD -> 166 problems (66 errors, 100 warnings), all 66 errors sited under .vite/deps_temp_*/...js"
  ],
  "remedy": "eslint.config.js's globalIgnores gains a .vite/** (or equivalent) exclusion so a concurrent dev-server's build cache cannot be scanned by lint. Outside this round's grant (no FE-s-50..60 cell touches eslint.config.js).",
  "owner": "1.0.0_SA_CTO",
  "round": "v9",
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v9"
  },
  "closed": false
 },
 {
  "id": "IRPT_FNTEND-W8-S2",
  "project": "IRPT_FNTEND",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "fe-s-42/_captures.ts's readDeliverablesTree() reads `git status --porcelain` over the WHOLE deliverables/ tree, unscoped to what the test's own driver could write, so any concurrent unrelated write into that tree (here: a worker's own result.md, written moments earlier by a sibling cell) produces a false failure on F42-AC7 / fe-s-32's capture-verdict check. ACCEPTED ON THE MERITS, CITATION CORRECTED: 2.0.0_SA_COO~F's drain note (msg 99139) attributed the whole-tree, unscoped-by-design choice to 'RULING X'; the file's own header comment (verified by 3.0.0_SA_CVO's verification fork) instead names 'RULING AC' ('THE PROOF, READ FROM THE WORKING TREE ON PURPOSE -- the defect is dirt in the working tree'). RULING X governs an unrelated round-7 test-scoping census in this same project. The substantive judgment -- that the unscoped read is a deliberate design choice trading false-positive safety for precision under concurrent writes, not a code bug -- is independently corroborated by the file's own docstring regardless of which ruling letter is cited, so the underlying disposition stands: ACCEPTED AS FILED. Left ARMED because, left alone, it will continue to occasionally false-fail under future concurrent writes to deliverables/ -- a known, accepted, standing characteristic, not a bug queued for a fix.",
  "evidence": [
   "org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md@1605b02ff8#IRPT_FNTEND-W8-S2",
   "org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/__tests__/fe-s-42/_captures.ts header comment: 'THE PROOF, READ FROM THE WORKING TREE ON PURPOSE (RULING AC: the defect is dirt in the working tree)' -- not 'RULING X' as the drain note cited",
   "2.0.0_SA_COO~F msg 99139 (this project's L8 hand-off): 'that check's design is deliberate, RULING X; accepted as filed, no code change'",
   "3.0.0_SA_CVO verification fork, this L9, 2026-09-21: citation cross-check against the file's own docstring"
  ],
  "remedy": "None needed on the merits -- accepted as a standing, deliberate design trade-off. If ever revisited: scope readDeliverablesTree() to only the paths the test's own driver could write, rather than the whole deliverables/ tree, so a sibling cell's concurrent, unrelated write cannot false-fail it.",
  "owner": "2.0.0_SA_COO~F",
  "round": "v9",
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~F",
   "at": null
  },
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~F",
   "round": "v9"
  },
  "closed": false
 }
]
```
