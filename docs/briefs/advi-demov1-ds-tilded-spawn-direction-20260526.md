# ADVI_DEMOV1 — DS 0.4.0~D spawn-with-direction handoff (F2 account-# pseudonymization + roles + responsibilities)

**From:** 0.4.0_DT_ClientPlatform (TO-009 UAT scribe; brief for Andrew ferrying)
**To (intended spawnee):** 0.4.0_DS_ClientPlatform~D — fresh `.tools\spawn-agent.ps1` invocation
**Date:** 2026-05-26 ~19:30Z
**Authority chain:** Andrew sovereign direct (this brief) → MSTR `/mstr-spawn` → DS~D fresh spawn → ws COO dispatch lane
**Parent project status:** **ADVI_DEMOV1 CLOSED COMPLETE** 2026-05-26 ~19:00Z (commit `767c113ab`) — F2 is a carry-open follow-on per LD-0030 staging, NOT a re-open of the project
**Sibling tracks (FYI, not your scope):** F1 (numbers × 3) → 0.7.0_AE_CloudOps solo; F3 (Black Diamond → Lone Pine label) → 0.4.0_DE_ClientPlatform TO-010

---

## TL;DR

Andrew UAT on portal `03a85441` 2026-05-26 returned PASS-frontend-scope + 3 backend findings split-routed. **F2 is yours.** It's a focused ~1-2h wall scope: extend the JSON-path-aware PII map in `fake_identities.py` to cover account-id-class paths + add a deterministic `real_account_id` → `OPAL{6-digits}` mapper to the Pass-1 table + integrate with your own `factory.seal_real_names()` Path B primitive (TO-006) + re-run R5 leak scanner with the new field-class extension. AE 0.7 coordinates the EC2 transform-runner re-dispatch.

**Your strongest lane fit:** you authored Path B structured-PII-tagging (`115af15f8`, `50176a86e`, `7e9969a5d`) — that's the seal-and-tag infrastructure F2 extends. ~C has deeper original-engine knowledge but F2 fits Path B more cleanly than the attempt-1-through-13 debugging arc.

---

## Roles & responsibilities split for the demo pipeline (project corpus)

| Surface | Owner | Why |
|---|---|---|
| `data/demo/scripts/transform/fake_identities.py` (PII map + faker primitives + Path B seal + `_embeds_real`) | **DS 0.4.0~C/~D primary** | ~C authored the multi-pass deterministic pseudonymizer (TO-002→TO-004 13-attempt arc); ~D wrote Path B structured-PII-tagging primitive + factory.seal_real_names + FN-1 regression-test fixture (TO-006) |
| `data/demo/scripts/transform/demo_transform.py` (engine; JSON-path walk; Pass-1 mapping; Pass-2 rewrite) | **DS 0.4.0~C/~D primary; AE 0.7 collaborator** | DS owns the transform-logic substance (R1 JSON-path-aware walk; R2 PII inventory reconciliation); AE 0.7 has shipped infrastructure-class additions (snapshot-clean helper `3cffa512b`; pre-apply gate integration) |
| `data/demo/scripts/transform/pii_leak_scan.py` (R5 mandatory leak scanner — sole defense) | **DS 0.4.0~C/~D** | R5 ruling: at-rest scan is the only and final guarantee (serve-time pseudonymizer retired per §3.4 finding 1); extending the scanner for new field-classes is DS-lane |
| `data/demo/scripts/transform/test_path_b_disjointness.py` (FN-1 9-case fixture + 49F-density case) | **DS 0.4.0~D** | Your own fixture from TO-006 Phase 3; F2 should extend with account-#-class regression cases (1-2 new cases) |
| EC2 `demo-transform-runner` instance + IAM + opal-data-demo bucket | **0.7.0_AE_CloudOps** | TO-001/.005/.007 owner; you do NOT touch EC2 / IAM / safe-ec2-deploy / `infra/aws/terraform/shared-infra/demo-transform.tf` |
| SSM transform-job dispatch + R5 post-run sweep + JSON-status close coordination | **0.7.0_AE_CloudOps** | They own the end-to-end re-run trigger; you hand off your code + their tests pass + R5 PASS → they SSM dispatch + signal RAVC2 to ws COO |
| Portal frontend (`_partners/demo/`) | **0.4.0_DE_ClientPlatform** | F3 lane (Black Diamond → Lone Pine label); not yours, not AE's |
| Portal DEV→PROD push + pointer-bump + tag | **0.4.0_DT_ClientPlatform** (me) | Rule 19 ephemeral-worktree pattern; standalone TO when DE ships F3 |

**Boundaries you must NOT cross (route to lane owner if you find yourself there):**
- F1 numbers × 3 multiplier in `demo_transform.py` Pass-2 walk — AE 0.7 owns; if you accidentally see F1 work needed, MCP AE 0.7 + ws COO instead of editing
- Anything under `infra/aws/terraform/` or `infra/aws/ec2/` or `EC2_MANIFEST.json` — AE 0.7
- Anything under `portal/src/` — DE / DT
- Any new IAM policy or SSM document — AE 0.7

---

## Project state context (one-paragraph for your orient)

ADVI_DEMOV1 = demo tenant for Advisor Intelligence — clone 49F book into `opal-data-demo` with deterministic pseudonymization. **CLOSED COMPLETE 2026-05-26**: TO-001 (bucket+routing AE~C `16fd50aa6`), TO-002 (transform engine ~C `7d6b1b835`), TO-004 (apply-mode 13-attempt arc ~C peak `469df551f` AC2 cent-parity + R5 leak_count=0), TO-005 (EC2 demo-transform-runner AE~C `206cd4483`+ `611926658`+ `5e32c0f1d`), TO-006 (Path B structured-PII-tagging ~D `115af15f8`+ `50176a86e`+ `7e9969a5d`), TO-007 (snapshot-clean AE `3cffa512b`+ `24c1be41b` IAM), TO-008 (portal frontend DE 0.4 `03a85441`), TO-009 (portal PROD promote DT 0.4 `9a0ea83fb` + tag `portal-v2.1.73`), TO-VAL-FE (Andrew UAT PASS-frontend-scope ~17:30Z).

Andrew UAT surfaced 3 backend findings post-close — F1+F2+F3 split-routed; **F2 is yours**. Project stays CLOSED; follow-ons land on the carry-open trajectory per LD-0030 staging.

---

## F2 — your scope

### What Andrew said (verbatim 2026-05-26 ~17:42Z)

> *"the account numbers in 'Fee Summary' page are still displaying, which must be adjusted. ... make up account strings like OPAL###### (specifically in the fee summary panel, wherever that is sourcing data from maybe you can check and include that in this little brief on the changes)"*

### Data-source trace (already done — pinpoint for you)

- **Frontend renders at:** `portal/src/pages/AdvisorIntelligence/_shared/tabs/FeeSummaryPanel.tsx:488` (column "Account" → `acct.account_id`)
- **Data prop type:** `FeeSummaryByAccount` (`_shared/types.ts`)
- **Source on S3:** `s3://opal-data-demo/platinum/clients/{client_id}/summary.json` at JSON path **`.fee_summary.by_account[].account_id`**
- **Transform-side input:** `s3://opal-data-bd/platinum/clients/{real-client-id}/summary.json` at the same JSON path

### Diagnosis (most likely — confirm in your investigation step)

R1 JSON-path-aware-gap. The PII-field map in `fake_identities.py` does NOT include `.fee_summary.by_account[].account_id` as a rewritable path. BD source has real account numbers (format-class to determine via your investigation); they pass through to demo unchanged. Smoke-D name-class is clean (your Path B + `_embeds_real` working as designed) — but account-#-class slipped through because the path wasn't catalogued.

### Target spec

1. **Add JSON path** `.fee_summary.by_account[].account_id` to the rewritable-path map. Plus do an R1 audit-sweep for ANY other account-id-class JSON paths (likely candidates: `platinum/accounts/{id}/...` keys, `platinum/clients/{id}/book.json` account references, `platinum/clients/{id}/decomposition.json` per-account rows, `cumulative_chart.adv_drill` if it has account refs, anywhere `account_id` JSON-path appears).

2. **Deterministic mapper** `real_account_id` → `OPAL{6-digit-numeric-seeded}` e.g. `OPAL000001`, `OPAL427819`. Same primitive class as advisor-slug + client-z-ID + firm-faker. Pass-1 mapping table extends with `account_id_map: dict[str, str]`. Determinism contract = same real id always maps to same fake id (R1 referential integrity across 22 k files).

3. **Integrate with your Path B primitive.** `factory.seal_real_names()` (your `115af15f8`) should fold account-id-class into the structured-PII-tagging-at-build-time sweep so the `_embeds_real` guard's coverage extends to the new id-class (defense-in-depth). FN-1 fixture (your `50176a86e`, extended in `7e9969a5d`) gets 1-2 new test cases gating account-#-class regression.

4. **Extend `pii_leak_scan.py` (R5)** to assert no `BD-source-account-id-format` strings remain anywhere in `opal-data-demo`. The exact format-class you determine in step 1's investigation (likely 9-digit numerics or BD-internal alphanumeric).

5. **Handoff to AE 0.7** when your changes pass pre-commit gate (Rule 14) + FN-1 9→11 cases PASS locally + R5 dry-run PASS on a single-client sample. AE 0.7 SSM-dispatches the full transform re-run on EC2 + post-run R5 sweep + RAVC2 close to ws COO.

### Acceptance criteria

- **AC1:** new JSON path `.fee_summary.by_account[].account_id` (+ any other account-id-class paths surfaced by audit) added to PII map; commit on CLOUD via `.tools/safe-commit.sh`
- **AC2:** deterministic `OPAL######` mapper added to Pass-1 mapping table; same real id maps to same fake id across all 22 k files (referential integrity)
- **AC3:** FN-1 fixture extended with account-#-class case(s); 9/9 → 11/11 PASS (or whatever final count) on Path B primitive
- **AC4:** R5 leak-scanner extended for account-#-class; dry-run on a single-client sample PASSes
- **AC5:** AE 0.7 handoff via MCP with the changeset SHA + dry-run R5 PASS evidence
- **AC6:** post-AE-run full R5 PASS (no real account #s anywhere in `opal-data-demo`) — AE 0.7 fires; you ack in RAVC2

### Out-of-scope (DO NOT do these)

- **Do not** touch `demo_transform.py` Pass-2 numeric multiplier (F1 — AE 0.7's lane)
- **Do not** dispatch EC2 SSM job (AE 0.7)
- **Do not** edit any portal/src/ file (F3 — DE)
- **Do not** modify the existing name-class pseudonymization (your `_embeds_real` and Path B seal are working; just extend coverage)
- **Do not** make this a v2 / refactor — minimum-scope extension of the existing primitives

---

## Investigation step (do this first, before coding)

```bash
# 1. Pull a sample from both buckets
aws s3 cp s3://opal-data-demo/platinum/clients/{any-demo-client-id}/summary.json /tmp/demo-summary.json
aws s3 cp s3://opal-data-bd/platinum/clients/{any-bd-client-id}/summary.json /tmp/bd-summary.json

# 2. Compare account_id format
jq '.fee_summary.by_account[].account_id' /tmp/demo-summary.json /tmp/bd-summary.json

# 3. R1 audit sweep — find ALL JSON paths in bd that have account_id-class strings
jq -r '.. | objects | with_entries(select(.key | test("account_id|account_number"))) | select(. != {})' /tmp/bd-summary.json

# 4. Check other artifact classes
aws s3 cp s3://opal-data-bd/platinum/clients/{any-bd-client-id}/book.json /tmp/bd-book.json
aws s3 cp s3://opal-data-bd/platinum/clients/{any-bd-client-id}/decomposition.json /tmp/bd-decomp.json
# repeat jq audit on each
```

This determines (a) the format-class of bd account IDs (so the scanner can detect leaks) and (b) the full set of JSON paths that need mapping coverage.

---

## Coordination interfaces

| Direction | Trigger | Channel | Format |
|---|---|---|---|
| You → ws COO | TO scope received; first orient ack | MCP | RAVC2-Ack ("starting; ETA ~1.5-2h") |
| You → AE 0.7 | Changeset ready; pre-AE-run dry-run R5 PASS | MCP | "handoff with SHA `<...>` + dry-run evidence; please SSM dispatch + post-run R5" |
| AE 0.7 → you | Post-AE-run R5 PASS evidence | MCP | "R5 PASS — leak_count=0 with account-#-class extension" |
| You → ws COO | Final close | MCP | RAVC2-Request with full evidence |
| You + AE 0.7 → ws COO | Close-evidence chain | MCP | ws COO RAVC2-ACCEPT closes F2 carry-open |

**Blocker routing (per LD-0072 /work skill):** if you hit a fork that needs Andrew/CTO/CVO/peer-resource, MCP ws COO with `[BLOCKED-ASK]` + the routing class. COO routes; you stand by.

---

## Discipline you carry from the canonical memory + CLAUDE.md

- **Pre-commit gate (CLAUDE.md Rule 14):** `.tools/ds-commit-gate.sh <files>` before every `git add`/`git commit`. Three checks (py_compile, ds-precommit-check.py, ruff) must exit 0.
- **Commit wrapper (CLAUDE.md Rule 14a):** `.tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~D <0.4.0_DS_ClientPlatform~D@opal.agent>" -m "msg" -- <paths>`. The shared-index contamination pattern WILL fire during multi-agent cycles; the wrapper handles it. Use `--force` with audit only when cleanup races repeatedly (per CLAUDE.md Rule 14a).
- **From-future imports (CLAUDE.md Rule 15):** `from __future__ import annotations` first line of any `.py` you edit in `data/*/scripts/`. Demo scripts live at `data/demo/scripts/transform/` — same rule.
- **Owned-paths:** if your serial isn't in `permitted_agents` for a path, route to COO for the lane add (canonical memory `feedback_tilde_lane_owned_paths_gap_route_to_coo`); don't `--force` past the hook.
- **Track in-flight by artifact, not SLA** (`feedback_track_inflight_to_by_artifact_not_sla`): your evidence to ws COO is commit hashes + dry-run output, never "within SLA."
- **Surface phase artifacts** (`feedback_surface_phase_artifacts_during_execution`): if you do this in multiple phases (audit → code → fixture → scanner), MCP a one-liner to COO at each phase boundary; don't run heads-down to RAVC2.
- **No-Cognito on Opal** (`project_opal_auth_dynamodb_never_cognito`): if any doc you read uses "Cognito" language about portal auth, translate to "DynamoDB user table + auth-handler"; PRD §1/§6.1 has Cognito wording-rot routed to ws CTO for v0.4.2 amendment.
- **SPAWN-WITH-DIRECTION fast-orient template** (`feedback_spawn_with_direction_fast_orient_pattern`): on spawn, run `/watcher` first; classify queue vs disk vs MCP; ack with orient summary in <40min wall; pick cleanest exec first.

---

## Startup sequence (post-spawn — same as my own DT 0.4 pattern today, 9th-fast-lane regime)

1. **`/watcher`** — self-heal inbox-watcher + broker registration per `org/XXX.md` Step 1b
2. **Read `org/XXX.md`** — fabric startup protocol (you've done this before but re-read for current Rule 19 / Rule 14a state)
3. **Read your prompt at `org/tier2_senior/0.4.0_DS_ClientPlatform/prompt.md`** — DS persona; pod members; deploy boundaries
4. **Arm `/work 20m` cron** per LD-0072 + run `/work` once immediately for first tick
5. **Read your own recent logs at `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-24/`** — your last session was LD-0027 spawn → TO-006 Phase 2/2.1/3 ship → standing watch
6. **Read this brief in full** + the ADVI_DEMOV1 PRD at `docs/architecture/ADVI_DEMOV1.md` (focus on R1, R2, R5 rulings + §3.4 Phase 0 findings + §3.5 snapshot-clean)
7. **Run the investigation step above** (4 `jq` commands) — confirms F2 diagnosis empirically
8. **MCP ws COO with [SPAWN-ORIENT]** ack — "DS 0.4.0~D respawned for ADVI_DEMOV1 F2 carry-open; orient complete; starting investigation step; ETA ~1.5-2h to dry-run R5 PASS handoff to AE 0.7"
9. **Execute F2** per the spec above
10. **Hand off to AE 0.7** via MCP when AC1-AC4 + dry-run R5 PASS local
11. **RAVC2-Request to ws COO** when AE 0.7's post-run R5 PASS lands; full evidence chain

---

## References (chronological, for your context-rebuild)

- PRD: `docs/architecture/ADVI_DEMOV1.md` (R1 + R2 + R5 are load-bearing for F2)
- Phase 0 probe brief: `docs/briefs/advi-demov1-phase0-serving-path-pii-probe-20260521.md` (`5ecfa2ceb`)
- DS~C TO-002 ship: `7d6b1b835` — original two-pass deterministic pseudonymizer
- DS~C TO-004 13-attempt arc: peak at `469df551f` 2026-05-24 (AC2 22260 parity + R5 leak_count=0)
- **Your TO-006 chain:** `ee769db89` design → `115af15f8` Phase 2 (Path B primitive + seal_real_names) → `50176a86e` Phase 3 (FN-1 9-case fixture) → `7e9969a5d` Phase 2.1 (49F-density case)
- AE 0.7 TO-007 snapshot-clean: `3cffa512b` (Python) + `24c1be41b` (IAM) + `e04647e32` (pipeline-inventory)
- TO-009 portal ship (mine): `9a0ea83fb` (close) + portal/PROD `b7b201a6` + tag `portal-v2.1.73`
- Project close (COO): `767c113ab` (3-of-3 atomic JSON+REGISTRY+PRD)
- UAT findings brief v2 (mine): `595d2511f` (full F1+F2+F3 split-routing + Andrew clarifications)
- This handoff brief: TBD on commit (will live under `docs/briefs/`)

---

## Closing note from DT 0.4

You're stepping into a clean, well-instrumented codebase that you yourself substantially built (Path B + seal_real_names + FN-1 fixture). F2 is a coverage extension of your existing infrastructure, not a redesign. Expect ~1-2h wall to dry-run R5 PASS handoff to AE 0.7. Andrew direct, ws COO routing, AE 0.7 collab for the EC2 dispatch. Fast-lane regime.

— 0.4.0_DT_ClientPlatform (TO-009 UAT scribe; brief author for Andrew ferrying)
**archetype:** SCRIBE+COORDINATE
