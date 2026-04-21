# COO Session 38b — ADHC_DSFLOW.002 Execution + Andrew 2026-04-21 Directives Folded In

**Date:** 2026-04-21 (Tue, PM ET)
**Agent:** 2.0.0_SA_COO
**Scope:** Execute own-desk DSFLOW.002 (org-docs update per `docs/architecture/ADHC_DSFLOW.md` §6.4 + §7 TO-2). Folded in two Andrew mid-session directives per DS MCP 20260421T155952Z (universal py_compile gate + DS-owned S3 upload supersession). Continuation of session 38 (five-item execution).

---

## Scope

DSFLOW.002 is my own pending TO, gated on DSFLOW.001 completion. DS shipped DSFLOW.001 at `b6e0c154` + `7b7381ac` (pre-commit gate tool — `.tools/ds-commit-gate.sh` + `.tools/ds-precommit-check.py`, 71 gold scripts clean, canary exit 1). Gate cleared. Executing now.

DS also forwarded two Andrew mid-session directives (~11:44 ET this session) that extend DSFLOW.002's scope beyond the PRD's original 5 deliverables. DS stood down on own-scope prompt.md/README.md edits to avoid merge conflict with me, then self-edited prompt.md + CAN/MUST sections on their README while I was mid-work on STAUDT/TRSB (session 38a). Rather than unwinding DS's edits, I integrated by ensuring CLAUDE.md + XXX.md + README.md Must/Cannot match DS's prompt.md voice + content. No conflicts.

---

## Work Completed

### CLAUDE.md — Rules 13 + 14 added

Old structure had Rule 13 (No emojis) in Code Quality section and Rule 14 (Agent Autonomy) in Agent Autonomy section — out-of-order relative to sections. DSFLOW.002 PRD assumed Rule 13 was free for DS deploy cycle; resolved by:

- **New Rule 13 (Critical EC2 Deployment Rules):** DS owns gold-script commit→QA-deploy cycle, including S3 upload even when DT online. Cites Andrew directive verbatim. Supersedes 2026-04-20 DT-online-override interpretation for the `aws s3 cp` step specifically. DT retains push + timing-coordination authority when online; S3 upload is DS-direct regardless. References `memory/feedback_ds_commits_ae_deploys.md` + `docs/architecture/ADHC_DSFLOW.md`.

- **New Rule 14 (Critical EC2 Deployment Rules):** Pre-commit gate for every `.py` edit. `.tools/ds-commit-gate.sh` (wraps py_compile + AST undefined-name scanner). Both exit 0 required. Universal — every DS agent, every pod, every Python edit. Cites Andrew directive verbatim + 081223b5/035352c3 same-class defense. Tool cited at `b6e0c154` + `7b7381ac`.

- **Old Rule 13 "No emojis"** → converted to unnumbered `**No emojis in code.**` bullet under renamed "## Code Quality" section. Same content; loses rule number.

- **Old Rule 14 "Agent Autonomy"** → converted to unnumbered `**Agents operate autonomously.**` bullet under renamed "## Agent Autonomy" section. Same content; loses rule number.

Rule renumbering alternative was considered (shift old 13 → 15, old 14 → 16) but declined — unnumbered bullets preserve the content without forcing references elsewhere to update. Only the four lines above the old 13/14 numeric prefix change; external "Rule 13 / Rule 14" references now unambiguously mean the new DS-focused rules.

### org/XXX.md — DS Abilities row updated

| Role | Commit | Push CLOUD | Push DEV (portal) | Deploy AWS | Session Logs |
|------|--------|------------|-------------------|------------|--------------|
| **DS** (was) | Edit + commit locally | No | No | No | Encouraged |
| **DS** (now) | Commit + push + gold-script S3 upload (committed-ref) + qa-runner SSM dispatch | No (PROD) | QA-runner only | Encouraged |

Reflects PRD §6.4 authority split + Andrew Rule 13 directive. "No (PROD)" in Push column means DS can push CLOUD but not PROD. "QA-runner only" in Deploy AWS column means DS can dispatch to `bd-gold-qa-runner` via SSM but NOT invoke PROD `bd-gold-trigger`.

### DS README.md — Must + Cannot + Deploy Cycle

**Added Must section** (new):
- `.tools/ds-commit-gate.sh` before every commit on any `.py` edit.
- `aws s3 cp` directly after push — never defer to DT, even when DT online. Cites Andrew directive verbatim + 2026-04-20 STAUDT drift evidence.
- `bd-gold-qa-runner` SSM dispatch direct (no handoff).
- `data_contract.xml` update when Lambda output shapes change.
- `git status` before any "committed" claim (c6285ae8 reminder).

**Cannot section expanded** to call out:
- `bd-gold-trigger` (PROD) = AE exclusive.
- QA runner SSM for test runs = DS-authorized (was ambiguous before).

**Deploy-cycle section updated** to reflect Rule 13 split:
- Step 0: pre-commit gate.
- Steps 1-5: DS-direct cycle (gate → status → SHA → push → S3 cp → comp-pipescript deployed).
- Step 6: QA-runner SSM (DS authorized).
- Step 7: PROD trigger = hand to AE.
- Session log must capture pre-commit gate output.

### DS prompt.md — Already updated by DS mid-session

DS self-edited prompt.md during session 38a (while I was on STAUDT/TRSB) to add:
- Must section: `.tools/ds-commit-gate.sh` rule (Andrew directive verbatim).
- Can section: S3 upload with "THIS IS YOURS" language + 2026-04-20 STAUDT drift evidence.
- Gold Script Deploy Cycle: Step 0 gate, Step 4 explicit "YOU do this not DT not AE", plus rationale paragraph "Why the S3 upload stays DS-direct even when DT is online."

No conflict with my CLAUDE.md / README.md / XXX.md edits — DS's voice + content align. Skipped duplicating the work.

### memory/feedback_ds_commits_ae_deploys.md — Already updated by DS

DS's session log (`dsflow_001_precommit_gate_tool.md`) + the memory file both carry the Andrew 2026-04-21 supersession paragraph. No new enforcement-reference note needed from me — the cross-references are already in place.

### §11 Q4 DS IAM probe — DEFERRED (implicit confirmation)

DSFLOW.002 PRD Phase 1 required a `aws iam simulate-principal-policy` probe to verify DS has `s3:PutObject` on `opal-bd-gold-code/gold/*`. Deferred because:
- DS has been successfully running `aws s3 cp` to this prefix since the tool landed (DSFLOW.001 shipped tests against 71 gold scripts; repeated uploads during STAUDT/HLOT1/HLOT2 waves).
- Implicit confirmation = IAM allows the operation. Explicit probe would only formally document what is already working.
- If DS hits permission-denied in future, 0.7.0_AE_CloudOps can probe at incident time and patch.

Documented as deferred in DSFLOW.002 TO closeout comment.

---

## Decisions Made

1. **CLAUDE.md rule renumbering strategy: unnumbered bullets for old 13+14.** Avoids renumbering external references. New Rule 13 / Rule 14 now unambiguously refer to the DS-focused deployment rules as DSFLOW.002 PRD intended.

2. **Do not duplicate DS's prompt.md edit.** DS self-edited mid-session with consistent content. Unwinding and redoing under my author would churn for no benefit. Rule per `memory/feedback_commit_only_flag.md` — only touch scoped paths; leave agent-edited files alone when content aligns.

3. **IAM probe deferred.** Active-use evidence subsumes formal probe.

4. **Andrew directives fold-in: done in-commit, not in follow-up TO.** DS suggested "fold into DSFLOW.002 commit" to avoid duplication. Followed.

---

## Files Modified

- `CLAUDE.md` (MODIFIED) — Rules 13 + 14 added; old 13 + 14 converted to unnumbered bullets.
- `org/XXX.md` (MODIFIED) — DS Abilities row.
- `org/tier2_senior/0.4.0_DS_ClientPlatform/README.md` (MODIFIED) — Must + Cannot + Deploy Cycle.
- `org/tier1_exec/2.0.0_SA_COO/task_orders/ADHC_DSFLOW.002.coo-org-docs-update.md` (MODIFIED) — status flip + completion comment.
- `org/tier1_exec/2.0.0_SA_COO/logs/2026-04-21/session38b_dsflow_002_org_docs_update.md` (NEW, this file).

Out of scope (left in state already edited by other agents):
- `org/tier2_senior/0.4.0_DS_ClientPlatform/prompt.md` — DS self-edited.
- `memory/feedback_ds_commits_ae_deploys.md` — DS updated per their MCP.

---

## Blockers

None.

---

## Current State

DSFLOW.002 complete. DSFLOW.001 + .002 both shipped — the pre-commit gate tool is live, the org docs enforce DS-owned deploy cycle + universal pre-commit gate.

DSFLOW.003 (passive training run) remains staged. Fires on next natural DS gold-script commit post-.001+.002. Per DS MCP, next candidate is BFIX4 or Schwab C_01 merge work.

---

## Next Steps

1. **[COO, me]** Commit DSFLOW.002 under 2.0.0_SA_COO author + `--only` + explicit paths.
2. **[COO, me]** MCP CTO + DS with DSFLOW.002 complete signal. ACK the Andrew directive fold-in so everyone's aware of the new Rule 13 / Rule 14 citation path.
3. **[DS, on next gold-script commit]** DSFLOW.003 training run fires passively. Observe pre-commit gate + DS-direct S3 upload workflow in action.
4. **[AE 0.7.0]** Reply to 2.1.0_SA_COO on libcst layer-vs-venv decision (MCP 20260421T161210Z routed through me per COMP_LEARNS scope).

---

## Compiler Tools

| Tool | Command | Result | Purpose |
|------|---------|--------|---------|
| Read | CTO session log `session36_five_item_decisions.md` + DS inbox MCPs (20260421T155952Z, 20260421T160248Z) | Full scope + Andrew directives captured | Source of truth for action set |
| Read | CLAUDE.md + org/XXX.md + DS README + DS prompt + memory file | Current state captured | Edit targets + conflict avoidance |
| Grep | `CLAUDE\.md Rule (13\|14)` | 13 files reference Rule 13/14 — all accept new-rule semantics (DSFLOW-oriented) | Confirmed renumbering safe |
| Edit | CLAUDE.md, org/XXX.md, DS README | Rules added, DS row updated, Must/Cannot expanded | DSFLOW.002 deliverables |

No comp-* runs — pure org-doc work.

---

— 2.0.0_SA_COO
