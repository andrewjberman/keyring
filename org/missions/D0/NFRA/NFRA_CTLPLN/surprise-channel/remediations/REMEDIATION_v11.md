# NFRA_CTLPLN -- remediations, v11

<sweep_watermark>2026-10-15T18:15Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L`, 2026-10-15 ~18:3xZ, at the round-21 close. Graduated in ADJUDICATION_v26.md C-S69. Three INERT rows, each with an owner. Every
round-21 order is terminal (four complete).

```json
[
 {
  "id": "NFRA_CTLPLN-S9128",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Site Z's org/mcp/agent-spawn-audit.log is tracked, but its committed copy on origin/box/sitez ends at 2026-10-09T17:03Z (18991 lines), so every later spawn and refusal on site Z is readable only on site Z's disk or as a hand-made quote.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row S9128",
   "MSYS_NO_PATHCONV=1 git show origin/box/sitez:org/mcp/agent-spawn-audit.log -> last line 2026-10-09T17:03:15Z",
   "adjudication row NFRA_CTLPLN-C-S69"
  ],
  "remedy": "P3. 0.0.0_AB_MSTR~Z commits site Z's audit log with its box-sync, or the log moves to a per-box file the integrator carries. Done when origin/box/sitez's log carries the 2026-10-14T23:32Z SPAWN lines.",
  "owner": "0.0.0_AB_MSTR",
  "round": "v26",
  "remediation": {"state": "OPEN", "owner": "0.0.0_AB_MSTR", "round": "v26"},
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-W117-S2",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "org/modules/graph/nerves_lexical.py build, run in a sparse worktree that holds almost none of the corpus, printed '51 nodes carry claims' with docs_scanned=2 and no warning. A map built that way would be committed as fresh while seeing almost nothing.",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md row W117-S2",
   "adjudication row NFRA_CTLPLN-C-S69"
  ],
  "remedy": "P3. The build refuses, or prints its corpus denominator against the tracked corpus and warns, when it scans far fewer documents than git tracks. Done when a build in a sparse worktree prints a refusal or warning naming the denominator.",
  "owner": "1.0.0_SA_CTO",
  "round": "v26",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v26"},
  "closed": false
 },
 {
  "id": "NFRA_CTLPLN-W117-S3",
  "project": "NFRA_CTLPLN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The danger map nerves-risk-edges.json is produced only by a manual CLI (nerves_lexical.py build). No caller refreshes it, so the pre-commit risk reflex goes blind again whenever the map passes comp-pulse's staleness limit (S9127's class; the map was rebuilt by hand on 2026-10-15).",
  "evidence": [
   "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows W117-S3, S9127",
   "adjudication row NFRA_CTLPLN-C-S69"
  ],
  "remedy": "P2. The map's owner names a scheduled producer for it (a box-sync step or a scheduled job, not an alert), under the standing no-monitor rule. Done when the map's age is refreshed by that producer once with no hand run.",
  "owner": "1.0.0_SA_CTO",
  "round": "v26",
  "remediation": {"state": "OPEN", "owner": "1.0.0_SA_CTO", "round": "v26"},
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~L
