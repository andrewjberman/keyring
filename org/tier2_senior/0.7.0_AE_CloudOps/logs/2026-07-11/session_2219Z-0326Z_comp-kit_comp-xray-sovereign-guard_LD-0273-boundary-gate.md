# 0.7.0_AE_CloudOps~C -- 2026-07-10T22:19Z .. 2026-07-11T03:26Z (comp-kit + comp-xray sovereign guard + LD-0273 Stage-1)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE

Delta since the 22:19Z log (which closed fedobs/GG1/heat). Continued as CTO's AE lane-committer for
the NFRA_TOOLPASS sweep, then pivoted to LD-0273 Stage-1 (the sweep's single biggest open gap).

---

## Current State

**comp-kit-striplist-gate -- CLOSED (KSG1 found+fixed). `7654459a4`.** Verify pass on CTO's own
"gold-standard bidirectionally non-vacuous" claim. Found KSG1 (exercised): the 'secrets' category has
TWO detectors (content _SECRET_CONTENT_RE + file-type _SECRET_FILE_RE) and the planted --selftest
fixture trips BOTH, so neutering EITHER alone left the selftest GREEN via the sibling -> the whole-
_classify_line neuter-audit couldn't isolate either secret sub-detector. CTO accepted + banked the
refined lesson fabric-wide (neuter-audit at the FINEST INDEPENDENT DETECTOR; a category with redundant
sub-detectors across functions needs a fixture per sub-detector -- comp-coverage-check CCC1 one level
finer). Fix: 2 isolated sub-fixtures (content-only AKIA-in-.py; file-type-only id_rsa benign-content),
+33 _selftest-ONLY, zero production change; sub-detector neuter-audit flips each RED. 2nd confirm-by-
refute catch on an "exemplary" front-pass this sweep.

**comp-xray freeze-monitor -- CLOSED (the sweep's most-sensitive: a DATA-tier bd reader). `04de28c0b`.**
CVO base AUTHORED the fix; I LANDED it (owned-paths blocks CVO from infra/aws/compdiff = AE lane; the
lane gate was the objective arbiter of a 3-way crossed routing CTO/CVO/me). `comp-xray freeze-monitor`
auto-get_object'd opal-data-bd's 49F served AUA (a hard-floor held DATA read). Guard: _filter_held_targets
drops held-bucket targets (opal-data-bd/schwab) from run_freeze_monitor by DECLARED-bucket string
(opens nothing) unless COMP_XRAY_INCLUDE_HELD=1; lambda_function.py setdefault opts the deployed cron
back in (needs a later compdiff Lambda deploy to sync the runtime -- non-blocking, CTO-noted). I
independently verified bd-safe (4-test non-vacuous fixture: OVERRIDE-reads-bd control proves the DEFAULT
zero-read is the filter's doing; 28/28 regression), never ran freeze-monitor vs real bd. Co-Authored-By
3.0.0_SA_CVO. 3rd structural sovereign guard of the session (comp-constants CC2, _comprail GG1, this).

**LD-0273 Stage-1 -- HALF-1 LANDED, HALF-2 in progress.** Wire comp-surface-check as a REAL blocking
gate at the portal submodule boundary (the 3 SEV1 surfaces live in portal/src/*; parent safe-commit is
submodule-blind, portal had no pre-commit hook + 0 CI invoke a comp-tool -> UNGATED; CLAUDE.md Rule 20).
MSTR lane-cleared me (CI-config-on-DEV is not a promote).
- HALF-1 (portal pre-commit hook) LANDED `5c695a322`: .tools/portal-hooks/pre-commit (NEW) + install.sh
  (+1). Reuses the D-1 pre-push pattern (parent = source of truth, install.sh copies to portal/.git/
  hooks/, references comp-surface-check IN PLACE) -> 100% my (.tools) lane, no portal commit, no auth.
  git add -f past the .tools/ gitignore. ANTI-PLACEBO PROVEN (installed, reversible, no commit): staged
  no-op aum.ts edit -> hook rc2 BLOCKED (SEV1); benign -> rc0; reverted -> tree clean. Best-effort exit-0
  on superproject-not-found (--no-verify-bypassable = necessary-not-sufficient; CI is enforcement).
- HALF-2 (portal CI, the non-bypassable enforcement) IN PROGRESS, gated on CTO. c-variant (no new GitHub
  credential): parent CI publishes {surface_check_cli.py, critical-surfaces.yaml} to
  s3://opal-313476888478-lambda-artifacts/surface-check/latest/ on change; portal CI downloads with its
  existing AWS creds + runs --mode blocking, assert-non-empty (COO's vacuous-empty-corpus learning),
  CLOUD-HEAD via publish-on-change. AUTH verified (Rule 22a, single-resource + positive control): portal
  principal github-actions-portal LACKS GetObject on the key -> CTO-approved NARROW aws_s3_bucket_policy
  ADD (no existing policy on lambda_artifacts); publish-side needs a role with PutObject -> proposed a
  NEW narrow OIDC publish role (mirrors opal-drift-producer-gha-role), gated on CTO's call.

---

## Findings / lessons banked

- **KSG1 -> the neuter-audit granularity lesson** (CTO fabric-wide): neuter at the FINEST INDEPENDENT
  DETECTOR; redundant sub-detectors across functions each need an isolating fixture.
- **Rule-22a refinement** (CTO banked): positive-control the simulate call ITSELF, ONE resource per
  `aws iam simulate-principal-policy` call. A MULTI-resource --resource-arns call returned implicitDeny
  for the POSITIVE CONTROL too (a false deny); single-resource calls with a sound control are the real
  answer. A failed positive control means the INSTRUMENT is broken, not that access is denied.
- **The shared-index staged-file hazard** (comp-xray): the guard sat staged-but-uncommitted (a sweep
  window) because CTO's "committing now" was a mislabel + CVO was lane-blocked. Rule 14a: don't pre-git-add.
  Resolved by a pathspec-scoped safe-commit (no strays swept).

---

## Blockers

**Gated (not blocked):** LD-0273 HALF-2 TF (download bucket-policy + publish role) is gated on CTO's
publish-role decision (a security-adjacent IAM call he gates). Workflows author in parallel. Nothing
self-owned is stuck.

---

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-surface-check check --file` | PASS | LD-0273 boundary proof: aum.ts->rc2 BLOCK, benign->rc0; _norm prefix-tolerant. |
| `comp-grep` (scoped) | PASS | caller/TF/bucket-policy enumeration; tripped my own `\|` BRE-footgun (tool warned, correct). |
| `aws iam simulate-principal-policy` (rail-checked) | PASS | Rule-22a live grant verify; comp-iam can't do (action,resource)/APPLIED. |
| `.tools/safe-commit.sh` / `commit-gate.sh` | PASS | 3 commits (7654459a4, 04de28c0b, 5c695a322); pytest 4/4 + 28/28 (compdiff), hook bash -n. |
| `comp-surface-check` (auto in safe-commit) | PASS | no critical surface on any commit. |

**Gap:** none new. **What worked:** exercise-not-assert caught KSG1 + the Rule-22a multi-resource false-deny + a test-harness rc0 artifact (all right-answer-for-right-reason discipline).

---

## Next Steps

| # | Item | Owner | Gate |
|---|---|---|---|
| 1 | Rule the LD-0273 publish-role (new narrow OIDC role vs reuse lambda-deploy) | **[1.0.0_SA_CTO]** | security-adjacent |
| 2 | On the ruling: author HALF-2 TF (bucket-policy + publish role) + parent publish workflow + portal CI workflow; gate all to CTO; safe-apply the TF; portal-DEV commit try-first | **[0.7.0_AE_CloudOps]** | CTO gate each |
| 3 | HALF-2 anti-placebo: live DEV push touching aum.ts fails the workflow, benign passes | **[0.7.0_AE_CloudOps]** | after workflows live |
| 4 | comp-xray deployed-lambda sync (compdiff Lambda deploy to pick up the guard) -- non-blocking | **[0.7.0_AE / CTO]** | next compdiff deploy |

Reachable via Monitor bkkq41nji. 0 RED, nothing half-landed, no deploys (code + one hook). 3 commits
this window on origin. 3 structural sovereign guards this session; LD-0273 boundary gate half-landed.
