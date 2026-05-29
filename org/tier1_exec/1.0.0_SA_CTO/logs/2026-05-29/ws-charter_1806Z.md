# ws-charter cycle — 2026-05-29 1806Z

**archetype:** COORDINATE

**CLASS:** CLEAN-SWEEP (authoring lens) — substantive direction-routing tick

## Inbox classification
- **ANDREW_DIRECTION** (sovereign, this cycle): "we need to get back to three projects: FIND_INSURE, ADVI_INFMVP, MDPF_SCOPED." RESUMES FIND_INSURE (was Andrew-PAUSED 2026-05-28 ~1958Z). Routed operationally (no NOVEL PRD authoring required — all three have PRDs).
- **CROSS-FABRIC HAZARD** (from MSTR, picked up on online): opal-trade-submissions DDB drift (by-approver→by-approver-decided / decided_at). Classified + dispositioned at session start (BENIGN — complete TRSB_LEDGER.005 migration, code-parity confirmed). Disposition reported to MSTR; 3 LOW-sev range_key reconciles routed to AE 0.7.0.

## Action taken
1. **Hazard close** — source-audited opal-trade-submissions consuming code: handler writes decided_at on approve+reject (approved_at retained), dashboard queries by-approver-decided, zero live code on the dropped GSI. Reported CLEAN/BENIGN to MSTR; LOW-sev TF range_key drift (market-updates, opal-pm-snapshots, causality-generations) routed AE opportunistic.
2. **3-project drive directive → ws COO** (live, arming /drive): fold FIND_INSURE+ADVI_INFMVP+MDPF_SCOPED into /drive hot-set; /comp-manage + /allocation to MSTR for DS~B (MDPF F1/F4/F5) + DS~C (FIND_INSURE .024 loop) lane spawns — no DS lanes were LIVE at directive time (binding constraint on both).
3. **ADVI_INFMVP smoke-ask → Andrew direct**: only remaining gate is Andrew's manual smoke (F5 cross-view NNA + F1 real-login @ PROD portal-v2.1.103); COO staging 3-step closure for land-on-confirm.
4. **Memory** — wrote `project_three_primary_find_insure_resumed`; superseded `project_advi_infmvp_mdpf_scoped_primary_focus` in MEMORY.md index.

## Project-state sweep
- FIND_INSURE: active, Phase 2A; next = cost-gate-live-verify probe → fire .024 LIVE-DISPATCH loop (DS~C). Phase 1 RAVC2-Accept still pending AE Stage 2 universe fan-out.
- ADVI_INFMVP: active, all features complete + CVO-validated (F5 RIGID gate PASS 23:18Z). Andrew-smoke-gated.
- MDPF_SCOPED: active, S3/S4/S1 done, S2 backfill clean; CVO findings F1/F4/F5 (DS~B), F2 done (RD~B aa8c9de4).
- origin/CLOUD HEAD = 869d8c15e (2026-05-28 19:54Z); nothing landed since online.
- ANOMALY (banked, no action): ADVI_INFLV2.json + ADVI_ORIAPI.json fail JSON parse — both status=complete since 2026-05-01, clean tree, no consumer. Cosmetic latent malformed JSON in archived projects; outside active-sweep scope + direction-only mandate. Flag for opportunistic cleanup, not a TO.

## Follow-on dependencies
- COO drive disposition + /allocation outcome (DS~B/~C spawn) — expect reply next cycle.
- Andrew ADVI_INFMVP smoke result → triggers COO 3-step closure.

## Compiler Tools
None this tick — coordination/direction-routing cycle (no gold-script / portal / IAM surface touched). Source-audit of trading-table parity used Grep/Read (comp-* N/A — uninstrumented trade-pipeline per PRD §5).
