# /work 04:27Z -- LD-0067 bridge LOCAL end-to-end Docker quarantine COMPLETE (/goal directive)
**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE, DIAGNOSE
**Date:** 2026-05-26
**Serial:** 0.7.0_AE_CloudOps
**Trigger:** Andrew /goal directive 04:08Z -- "Finish the end-to-end docker container setup (local, no EC2) for downloading external cases for compiler R&D."
**Tier-0 commit hash at completion:** `151538a97` (bridge end-to-end completion commit)

---

## §1 -- Goal scope (per Andrew /goal directive)

LOCAL end-to-end Docker quarantine for compiler R&D external case downloads. Explicitly:
- ✓ IN-SCOPE: v1 bridge mechanism (already shipped `f5b1bcda2`) + CV-A3 deny-list + CV-A4 fail-closed audit + CV-A6 host-side validator + 5-AC smoke acceptance
- ✗ OUT-OF-SCOPE: WB-2..WB-7 (ECR push + EC2 dedicated runner + IAM hard-constraint + EventBridge cron + Trivy pipeline + production RAVC2) -- those queue per `CASE_FIND_QUARANTINE_IMPL.md` §3-§8 if Andrew later promotes to production

Per CASE_FIND_SECURITY_PROTOCOL.md v0.3 §6.3.6 + canonical §5 invariants. CV-A3/A4/A6 design specs in `CASE_FIND_QUARANTINE_IMPL.md` §4-§5 (commit `46939bf22`); local impl carries the mechanism implementation per citation discipline.

---

## §2 -- Deliverables shipped (5 new artifacts + 1 modified)

| Artifact | Spec authority | Coverage |
|---|---|---|
| `projects/case_find_bridge/validate_insight.py` | canonical §5 + CV-A6 | Host-side regex scan of emitted JSON for banned patterns (eval/exec/__import__/compile, strings >500c, host paths). 5/5 unit tests pass. |
| `projects/case_find_bridge/deny_list.py` | CV-A3 | Per-workspace sqlite cache with 7-day TTL. CLI for --check/--add/--remove/--list/--gc. |
| `projects/case_find_bridge/case_find_unblock.py` | CV-A3 unpoisoning | Audited removal via AUDIT_UNBLOCK row referencing original block_audit_id + signoff-token + reason. |
| `projects/case_find_bridge/audit_log.sh` | CV-A4 | Sourced helper providing audit_event() + audit_preflight_check(). Fail-closed: write failure sets refuse-marker + exits 99. |
| `projects/case_find_bridge/run_quarantine.sh` | orchestration | Wired Phase 0 preflight + deny-list pre-check + per-phase audit + Phase 5 host-validator + auto-deny-list-add on BLOCK + new exit codes (5=DENY_LIST_HIT, 99=AUDIT_FAILURE). |
| `.gitignore` runtime-state add | (deferred via BLOCKED-ASK to COO; AE not in BASE_EXEC lane) | exclude `projects/case_find_bridge/{reports,.case-find-state}/` |

Commit: `151538a97` (bridge 5 files; 599 insertions; 8 deletions).

---

## §3 -- 5 bug-fix sub-iterations in-flight during smoke acceptance

Worker-internal self-correction discipline per LD-0072. Each bug surfaced during smoke iteration + diagnosed + fixed without inter-agent escalation:

| # | Bug | Symptom | Fix |
|---|---|---|---|
| 1 | `if ! python --check` semantic | exit 0 (not-denied) entered DENY_LIST_HIT branch | Explicit `$DENYLIST_EXIT` capture + case statement (denied=1, error=2, ok=0 disambiguation) |
| 2 | MSYS_NO_PATHCONV path mangling on python.exe args | python.exe received `/c/Users/...` path → prepended `C:\c\Users\...` → "No such file" | `cygpath -w` for `DENY_LIST_PY` + `VALIDATE_INSIGHT_PY` + `REPORT_FILE_WIN`. Same pattern as prior docker build context fix `e753824ad`. |
| 3 | Validator ERROR misclassified as BLOCK | exit 2 (validator infra error) triggered deny-list-add path | `case "${VALIDATOR_EXIT}"` distinguishing 0/1/2; ERROR exits script 2 WITHOUT deny-list pollution |
| 4 | Validator absolute-path false-positive on container sandbox `/exam/blob` | Scanner's structural metadata `path` field treated as host-context leak | Regex tightened to host-roots only: `^/(home\|root\|Users\|etc\|var\|usr\|opt\|bin\|sbin\|lib\|mnt\|media\|sys\|proc\|boot\|srv)/` |
| 5 | `.gitignore` runtime-state add | reports + .case-find-state pollution risk | Lane-routed to COO via `[BLOCKED-ASK]`; AE not in BASE_EXEC lane |

Patterns 2 + 5 are owned-paths/path-mangling class issues that consistently surface during Windows-host Git Bash work; banked.

---

## §4 -- WB-6 5-AC acceptance evidence

Per `CASE_FIND_QUARANTINE_IMPL.md` §7 (adapted for local scope -- no WB-2 EC2 dependency):

| AC | Test | Evidence | Result |
|---|---|---|---|
| AC1 | Truly-benign URL → CLEAN exit 0 | smoke #4 on `https://github.com/sindresorhus/is-fullwidth-code-point` → all 5 phases OK + validator PASS + exit 0 | ✓ PASS |
| AC2 | Synthetic insight with `eval(` → validator BLOCK exit 1 | Test JSON `{"reports":[{"findings":[{"detail":"Detected eval(user_input) at file.py line 42"}]}]}` → validator emits `validator_status: BLOCK` with json_path `reports[0].findings[0].detail`; exit 1 | ✓ PASS |
| AC3 | Deny-list HIT path → exit 5 + audit | Pre-staged URL `https://github.com/synthetic/blocked-fixture` via `deny_list.py --add` → `run_quarantine.sh` exit 5; audit log row `DENY_LIST_HIT 20260526042709-1505302` | ✓ PASS |
| AC4 | `case_find_unblock` audited removal lifecycle | `case_find_unblock.py URL --signoff-token TOKEN --reason TEXT` → AUDIT_UNBLOCK row with `original_block_audit_id` reference; subsequent `--check` returns `denied=false` | ✓ PASS |
| AC5 | Audit log contains all 8 phase boundaries per successful run | Tail of `.case-find-state/audit.log` shows: QUARANTINE_REQUEST → PHASE_3A_START → PHASE_3A_END → PHASE_3B_START → PHASE_3B_END → PHASE_5_VALIDATOR_START → PHASE_5_VALIDATOR_PASS → QUARANTINE_COMPLETE | ✓ PASS |

---

## §5 -- Out-of-scope (explicit non-goals per /goal LOCAL constraint)

Production-grade hardening queued per `CASE_FIND_QUARANTINE_IMPL.md` §3-§8 if Andrew later promotes to production:

- WB-2 full: ECR push + digest ledger + dedicated EC2 runner + IAM hard-constraint
- WB-2 CV-A1: network-layer egress firewall (iptables/nftables; requires EC2)
- WB-4 full: CloudWatch alarm wiring + SNS routing (requires AWS)
- WB-5: Trivy CVE scan in image-build pipeline
- WB-7: Production RAVC2 to ws CTO + ws COO + CL-CVO

For LOCAL R&D, the current setup is end-to-end usable. CL CVO `/case-find` consumer interface can build against this bridge per Andrew Path-1 directive 2026-05-26T~0040Z.

---

## §6 -- Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-blast` | Not run | Bridge code changes localized to `projects/case_find_bridge/*.{sh,py}` (5 files). No portal/Lambda/EC2/IAM/Terraform graph impact. |
| `comp-iam gaps` | Not applicable | No iam.tf change (CV-A5 IAM hard-constraint is WB-2 production scope). |
| `comp-pipescript deployed` | Not applicable | Not gold/silver/bronze script. |

---

## §7 -- Authority + cross-references

- **/goal directive** (Andrew 2026-05-26T04:08Z) -- "Finish the end-to-end docker container setup (local, no EC2) for downloading external cases for compiler R&D"
- **LD-0067** (Andrew direct 2026-05-25T~22:35Z) -- security quarantine protocol; AE owns WS-B
- **LD-0081** (`12b97229e`) -- CASE_FIND v0.3 + TELEMETRY v0.4 spec amendments
- **LD-0084** (MSTR `4ae1fa61f`) -- WS-B impl-spec authoring + WB-1.1 hook patch authorization
- **CASE_FIND_QUARANTINE_IMPL.md v0.1** (`46939bf22`) -- impl-spec carries CV-A3/A4/A6 design; this commit implements the local-scope subset
- **Prior bridge commits:** `f5b1bcda2` (v1 ship), `e753824ad` (Win path fix), `3107931c1` (zip apk add), `0db237e60` (smoke validation log), `151538a97` (this end-to-end completion)

---

## §8 -- Next-step dispatch

1. RAVC2-Request to ws COO with /goal completion evidence
2. BLOCKED-ASK to ws COO for `.gitignore` runtime-state lane fix (AE-not-in-BASE_EXEC)
3. CC MSTR + ws CTO + ws CVO
4. Goal-stop hook auto-clears on RAVC2-Accept

-- 0.7.0_AE_CloudOps
2026-05-26
