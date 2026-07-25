# NFRA_TOOLUNIFY REC-1c — Lane A: live-AWS-plane 18-tool exercise batch + 24-residual-dir closure

**author:** `0.8.0_AE_CloudComp~A` · 2026-07-25 · **status:** DELIVERED, awaiting CVO~Z verification
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY (off-main-fabric census group)
**dispatch:** `1.0.0_SA_CTO~Z`, 20260725T060155Z, "DISPATCH NFRA_TOOLUNIFY REC-1c LANE-A — exercise batch
(18 tools, live-AWS affinity) + your 24-residual open item"
**addendum:** `1.0.0_SA_CTO~Z`, 20260725T060431Z, "label your mutation types, provisional pending L0b"
**builds on:** `REC1_EXERCISE.md` + `REC1B_EXERCISE.md` (same directory) — method, dispatch-idiom map, and
the already-CLOSED acceptance gate (positive control `comp-manifest-check` / mutant `comp-stitch-refresh`)
are inherited, not re-run.
**sidecar:** `REC1C_A.sidecar.json` (this directory) — per-invocation raw results, mutation-type labels.

> **Mutation-type labels here are PROVISIONAL, pending the L0b change-type vocabulary
> (`infra/system/ontology/IMPLEMENTATION_LEVELS_AND_SEQUENCING.md` §4/L0b) — this sweep records candidate
> vocabulary, it does not settle it.** Per CTO~Z's addendum: labels used are `EMPTY` / `NONEXISTENT` /
> `MALFORMED` / `STALE`, and `UNKNOWN` is first-class ("could not synthesize a safe bad input, or could not
> reach a terminal verdict within the light-cycle budget" is `UNKNOWN`, never a `MATCH`, never dropped).

---

## 1 · Denominator

**18 of 18 dispatched tools exercised, 0 skipped.** 16 reached a terminal, classifiable verdict; 2 rows are
`UNKNOWN` by the addendum's own first-class rule (not silently dropped, not forced to MATCH/MISMATCH — see
§3 rows for `comp-deadgrant`/`comp-deadgrant.py` and `comp-drift`). Read-only throughout: no
`--write`/`--write-only` flags fired, no `--force`, no apply, no commit-triggering call. Full verbatim
stdout/stderr for every invocation is in the sidecar.

## 2 · Method (inherited from REC-1/1b, applied here)

Per tool: identify the real dispatch idiom (bash-wrapper vs python-shebang-direct — confirmed by reading
`head -1` of every wrapper in `.tools/` before the first invocation, not assumed from the register), feed a
mismatched/stale/empty/nonexistent input, capture exit code + full stdout/stderr, classify OBSERVED as
LOUD / FAIL-OPEN / SILENT-EMPTY per REC1_EXERCISE.md §3's definitions, compare to D.md's DECLARED value.

**Dispatch-idiom check run FIRST, this pass** (`head -1 .tools/comp-X` for all 18): 11 are bash-wrapper
(`comp-lambdamap`, `comp-routes`, `comp-iam-usage`, `comp-deadgrant`, `comp-denytest`, `comp-tagauthz`,
`comp-pii`, `comp-keys`, `comp-debris`, `comp-drift`, `comp-firmsep-sweep`), 7 are python-shebang-direct
(`comp-deadgrant.py`, `comp-denytest.py`, `comp-tagauthz.py`, `comp-secrets`, `comp-clobber`, `comp-dups`,
`comp-firmsep-sweep.py`). **One self-caught idiom mismatch this pass** (§4, method note) reproduces
REC-1 §6's exact class.

## 3 · Results — all 18

| # | Tool (subcommand) | Declared `failure_mode` | Mutation type | Observed | Verdict |
|---|---|---|---|---|---|
| 1 | `comp-lambdamap check` | FAIL-OPEN (MED) | STALE (live source-map vs TF+disk state) | rc=1, explicit `DRIFT` list (3 WRONG_SOURCE_DIR, 3 MISSING_ENTRY) | **MISMATCH** — LOUD observed, FAIL-OPEN declared (reverse-direction; see §4a) |
| 2 | `comp-routes trace` | LOUD (MED) | NONEXISTENT | rc=0, `No match for: ...` (explicit text, rc=0) | **MISMATCH** — FAIL-OPEN |
| 3 | `comp-iam-usage reach-check` | LOUD (MED) | NONEXISTENT | rc=0, JSON `"verdict":"UNKNOWN"` + `"error":"get_role failed..."` | **MISMATCH at exit-code layer, by design** (see §4b) |
| 4 | `comp-deadgrant` | LOUD (MED) | self-test: n/a (positive control) · `--account` probe: NONEXISTENT | self-test rc=0 6/6-style PASS; `--account 000000000000 --limit 1` rc=0, 0 candidates, mutation never reached the account-dependent branch | self-test **MATCH** (positive control); account probe **UNKNOWN** (see §4c) |
| 5 | `comp-deadgrant.py` | LOUD (MED) | NONEXISTENT | identical output to #4's `--account` probe (byte-identical stdout) | **UNKNOWN**, same reason as #4 — confirms wrapper/`.py` parity |
| 6 | `comp-denytest` | LOUD (MED) | EMPTY (missing `--change-type`/`--from-plan`) then NONEXISTENT (full args) | rc=1 `FAIL: supply --from-plan...`; second probe rc=1 explicit `<NO VERDICT: ... NoSuchEntity>` | **MATCH** (both probes) |
| 7 | `comp-denytest.py` | LOUD (MED) | EMPTY | rc=1, byte-identical stderr to #6's first probe | **MATCH** |
| 8 | `comp-tagauthz check` | LOUD (MED) | EMPTY (missing `--default-tags-tree`) | rc=1, explicit `ERROR: --default-tags-tree is REQUIRED ... Failing closed (rc=1)` | **MATCH** |
| 9 | `comp-tagauthz.py check` | LOUD (MED) | EMPTY | rc=1, byte-identical to #8 | **MATCH** |
| 10 | `comp-secrets get` | LOUD (MED) | NONEXISTENT | rc=1, `comp-secrets: no secret named/matching '...'` (after a self-caught idiom-mismatch retry, see §4d) | **MATCH** |
| 11 | `comp-pii scan` | LOUD (MED) | NONEXISTENT | rc=1, `Component not found: ...` | **MATCH** |
| 12 | `comp-keys exists` | LOUD (MED) | NONEXISTENT | rc=0, per-firm `ABSENT` labels, tool's own documented BLIND caveat: "a typo'd or wrong prefix reads as a true (loud) zero, not an error" | **MISMATCH at exit-code layer, by design** (see §4e) |
| 13 | `comp-clobber --live` | LOUD (ADVISORY, MED) | NONEXISTENT | rc=1 via **unhandled** `botocore.errorfactory.NoSuchBucket` traceback | **MATCH-but-flagged** (see §4f) |
| 14 | `comp-debris` | LOUD (MED) | self-test: n/a (positive control) · `--types`: MALFORMED | self-test rc=0, all PASS incl. an explicit trading-calendar MUTANT check; `--types nonexistent_type_zzz_9999` rc=0, stderr DOES say `unknown type '...' (known: lambda,ddb,s3,ec2,events)`, but still prints a full "0 resources" report and exits 0 | self-test **MATCH**; `--types` probe **MISMATCH** (see §4g) |
| 15 | `comp-dups` | LOUD (MED) | MALFORMED (`--class` value not in the documented enum) | rc=0, ran the **full unfiltered scan**, zero acknowledgment anywhere (stdout or stderr) that `--class` was invalid | **MISMATCH — SILENT-EMPTY as to the mutation** (see §4h) |
| 16 | `comp-drift` | LOUD (MED) | NONEXISTENT | partial/timeout-bounded (150s budget) — no upfront target validation; seam-1 `comp-heat drift` returned `CLEAN`, seam-2 `comp-pipescript deployed` returned `MATCH`, for a target that does not exist; seam-3 (`globgrph derive marker-oracle`, live network) did not complete in budget | **UNKNOWN** (terminal RC undetermined — my own timeout, not the tool's exit; partial observation flagged in §4i, not adjudicated) |
| 17 | `comp-firmsep-sweep` | LOUD (default, LOW) | NONEXISTENT | rc=1, `cannot resolve secret '...': ResourceNotFoundException` | **MATCH** |
| 18 | `comp-firmsep-sweep.py` | LOUD (default, LOW) | NONEXISTENT | rc=1, byte-identical to #17 | **MATCH** |

**Tally, one primary verdict per dispatched tool (18/18): 8 MATCH, 6 MISMATCH, 1 MATCH-but-flagged
(crash-quality gap), 3 UNKNOWN.** (Two extra offline positive-control self-tests — `comp-deadgrant
--self-test`, `comp-debris --self-test`, both PASS — and one supplementary `comp-denytest` full-args probe
are recorded in the sidecar alongside their tool's primary row but are not separately tallied here, since
they are not a second dispatched tool.) Two of the three UNKNOWN rows are the wrapper/`.py` pair for the
same underlying non-result, so this is 2 distinct causes: the `comp-deadgrant` account-branch under-reach,
and `comp-drift`'s timeout.

## 4 · Findings requiring narrative

### 4a · `comp-lambdamap check` — first REVERSE-direction mismatch (declared FAIL-OPEN, observed LOUD)

Every prior REC-1/1b mismatch was declared-LOUD-observed-quieter. This is the first case running the other
way: the register declares `comp-lambdamap` `FAIL-OPEN` (MED confidence), but `check` against the estate's
own live, real drift state (no synthetic input needed — same "today's actual state already contains the
condition" class as REC-1's stitch mutant) produced an explicit, itemized, nonzero-exit `DRIFT` report —
squarely LOUD by this project's own definition. Two readings, not adjudicated here: (a) the register's
`failure_mode` may have been derived from a different subcommand (`sha`/`derive`/`parity`/
`reconcile-deployed` — the register is one row per tool, and REC-1b's §4b already established that a
single row can collapse materially different subcommand behavior); (b) `check`'s own FAIL-OPEN-shaped
behavior may live elsewhere (e.g., does it exit 0 when the underlying comparison itself errors, as opposed
to when it succeeds and finds drift?) — not tested this pass. Flagged as a concrete follow-up candidate for
whoever picks up subcommand-granularity register work.

### 4b · `comp-iam-usage reach-check` — FAIL-OPEN at the exit-code layer, but deliberately so

`rc=0` with a `"verdict":"UNKNOWN"` JSON field is, by REC-1's own definition, FAIL-OPEN ("nothing a script
gating on exit code alone would catch"). But the tool's own printed Rule-22a fix-or-carry block states the
design intent directly: *"an unreadable/unparseable policy is UNKNOWN, never 'no reach' (an unparsed Deny
!= silence)"* — i.e., this tool was deliberately built to prefer a well-labeled `UNKNOWN` over a false
verdict, and a script that greps `"verdict"` rather than gating on exit code alone would catch it fine.
This is the same shape as REC-1's `comp-iam service` finding and REC-1b's `comp-surface-check scan`
missing-input finding: **declared LOUD, observed FAIL-OPEN-at-exit-code, well-instrumented-in-substance.**
Recorded as a MISMATCH against the coarse three-value taxonomy, not as a defect in the tool.

### 4c · `comp-deadgrant --account` probe — UNKNOWN, not a MATCH, and why

Read `comp-deadgrant.py:490` before concluding anything: `a.account` (the `--account` value) is only
consumed inside the axis-A/axis-B candidate-simulation branch, reached **only if the earlier sweep finds at
least one dead-reach × fail-silent-reader candidate**. `--limit 1` (the light-cycle-bounded sample size)
found zero candidates, so the account-dependent code path never executed — the clean `rc=0` result is
uninformative about whether a mismatched `--account` would be caught, not evidence either way. Per the
addendum's explicit instruction, this is recorded as `UNKNOWN`, not forced into MATCH or MISMATCH.
**Separately, source-grounded and NOT gated on reaching that branch:** the earlier `lambdas in account: 191`
line comes from `list_functions`, which is **not** scoped by `--account` at all (it lists whatever the
active boto3 session's credentials resolve to, regardless of the flag's value) — so a wildly wrong
`--account` value has zero visible effect on the fleet enumeration stage specifically, silently. This is a
real, source-confirmed observation, distinct from the UNKNOWN verdict above (which is about the
per-candidate simulation branch, never reached this pass).

### 4d · `comp-secrets get` — self-caught dispatch-idiom mismatch (repeats REC-1 §6's exact class)

First invocation attempt used `bash .tools/comp-secrets get ...` (the majority-pattern idiom). `comp-secrets`
is confirmed idiom-2 (python-shebang-direct, per D.md §3.1 and this pass's own `head -1` check) — the bash
misdispatch produced a nonsensical, unrelated failure (`aws: error: the following arguments are required:
--secret-id` followed by `.tools/comp-secrets: line 16: tool: command not found`), attributable entirely to
bash trying to parse Python source as shell, not to the tool's own logic. Caught before recording a verdict,
corrected to `python3 .tools/comp-secrets get ...`, and the corrected run is what's tabulated in §3 row 10.
Logged per this project's own "do not silently discard a method failure" discipline (REC-1 §6 precedent) —
this is the second exerciser-side idiom mismatch across REC-1/1b/1c combined (REC-1 hit it twice on
`comp-freshness`/`comp-glob`; the idiom map was read correctly for all 17 other tools this pass, so the
miss here was a one-off slip, not a map gap).

### 4e · `comp-keys exists` — FAIL-OPEN at exit-code layer, self-documented

Structurally identical shape to REC-1's §5.1 `comp-freshness` finding: the tool's own `COVERAGE`/`BLIND`
disclosure block states outright that a wrong prefix "reads as a true (loud) zero, not an error" — the word
"loud" there is the tool author's own informal usage, not this project's LOUD/FAIL-OPEN/SILENT-EMPTY
taxonomy; by that taxonomy this is FAIL-OPEN (`rc=0` regardless of ABSENT vs PRESENT). Third instance of
this specific pattern across the census (after `comp-freshness` in REC-1, `comp-surface-check scan`'s
missing-input case in REC-1b) — worth CTO~Z/CVO~Z treating as a named, recurring register-vs-behavior class
rather than three unrelated findings.

### 4f · `comp-clobber --live` — LOUD via an unhandled exception, not a designed error path

`rc=1` technically satisfies "nonzero exit" and so is tabulated MATCH against declared LOUD, but the actual
mechanism is a **raw, uncaught `botocore.errorfactory.NoSuchBucket` traceback** eight frames deep
(`clobber_scan.py:182`, `live_confirm()`), not an explicit, designed error message. A script gating on exit
code alone still catches this fine (hence MATCH in §3), but a human reading only the last output line sees
a bare botocore internal exception, not an actionable message — a real, if minor, robustness gap distinct
from the failure_mode classification itself. Flagged as a quality item, not re-classified.

### 4g · `comp-debris --types` — MISMATCH, and the self-test result stands beside it

The `--self-test` positive control (offline, no AWS) passed cleanly, including a named
`MUTANT.wall_clock_control_WOULD_have_flagged` case that explicitly proves the trading-calendar fold
changes the verdict (excellent, deliberate instrumentation — the closest thing in this batch to another
tool building its own Rule-22a-style control into itself). Separately, the `--types` probe is a genuine
MISMATCH: the tool DOES detect and print the invalid type to stderr (`unknown type '...' (known:
lambda,ddb,s3,ec2,events)`), but then proceeds to print a full, normally-formatted "0 resources" report to
stdout and exits 0 — indistinguishable, to anything gating on exit code (or even a stdout-only read), from
"ran clean, zero debris found." Fourth instance of the declared-LOUD/observed-FAIL-OPEN-on-bad-input
pattern this census (after `comp-freshness`, `comp-surface-check scan`, `comp-keys exists`).

### 4h · `comp-dups --class` — the worst instance of this pattern so far: no acknowledgment at all

Unlike `comp-debris` (§4g), which at least printed the invalid-value note to stderr before proceeding,
`comp-dups --class NONEXISTENT_CLASS_ZZZ_9999` produced **zero signal anywhere** that the class filter was
invalid — no stderr line, no stdout note — and ran the complete, unfiltered TF-label-collision scan as if
`--class` had never been passed. This is SILENT-EMPTY as to the specific mutation (not merely FAIL-OPEN):
there is no observable difference between "you asked for an invalid class and I ignored it" and "you asked
for a valid class with zero matches." Fifth instance of the pattern, and the most severe.

### 4i · `comp-drift` — timeout-bounded partial, flagged not adjudicated

150s (light-cycle-appropriate) budget was not enough to reach a terminal exit; `rc=124` reflects my own
`timeout` wrapper, never the tool's own exit code, and is not recorded as the tool's behavior. What WAS
observed before the budget ran out: the tool applies **no upfront existence check** on its positional
`target` — the raw string is passed straight into each seam adapter's `if target:` branch (confirmed via
source read, `drift_cli.py`), and two adapters returned substantive verdicts for an artifact that does not
exist (`comp-heat drift` → `CLEAN`; `comp-pipescript deployed` → `MATCH`) rather than `NOT FOUND` /
`UNVERIFIABLE`. This is flagged, not adjudicated: it is plausible each downstream seam tool has its own
correct "target not found → benign verdict" logic that is doing something reasonable and only looks odd out
of context; establishing which requires tracing into `comp-heat`/`comp-pipescript` individually, which is
out of this batch's scope. Recorded as an open question for whoever widens the `comp-drift` sample next,
not as a confirmed finding.

## 5 · Cross-batch pattern (new this pass, worth naming explicitly)

**Five separate declared-LOUD/observed-FAIL-OPEN-or-worse-on-a-genuinely-invalid-or-absent-input findings
in one 18-tool batch** (`comp-routes trace`, `comp-iam-usage reach-check` [by design], `comp-keys exists`
[by design, self-documented], `comp-debris --types`, `comp-dups --class`), on top of the two already banked
from REC-1/1b (`comp-freshness`, `comp-surface-check scan`). **Seven confirmed instances now, across three
exercise passes, all sharing the identical shape: `rc=0` regardless of whether the input resolved to
something real.** Two of the seven are deliberate, well-labeled safety choices (`comp-iam-usage`,
`comp-keys`); the rest range from "prints the problem but proceeds anyway" (`comp-debris`) to "zero
acknowledgment at all" (`comp-dups`, the most severe). This is no longer a scattered set of one-off
findings — it reads as a shape the estate's tools default to on this specific input class, worth CTO~Z/
CVO~Z treating as a named methodology theme (parallel to REC-1b's `role_flags`-confidence-vs-`failure_mode`-
confidence axis finding) rather than re-litigating per tool.

## 6 · What this lane did NOT do

No apply, deploy, re-point, or write to any production S3 key, DynamoDB table, Secrets Manager value, or
Terraform-managed resource. No `--write`/`--write-only` flag fired (`comp-firmsep-sweep`, `comp-lambdamap
derive` both have write-coupled modes; neither was invoked). No commit to `org/tier1_exec/1.0.0_SA_CTO/**`
(CTO~Z's BASE_EXEC lane, per the established convention in REC-1/1b — this file is written to disk for
CTO~Z to commit). Did not chase `comp-drift`'s per-seam-adapter behavior into `comp-heat`/`comp-pipescript`
themselves (§4i, out of batch scope). Did not widen `comp-lambdamap` to its other four subcommands beyond
`check` (§4a flags this as a candidate follow-up, not executed here — light-cycle discipline, one
subcommand per tool this pass, consistent with REC-1/1b's own per-tool depth).

---

## 7 · Secondary item — 24-residual Lambda-source-dir closure

**Status at dispatch time:** `A.md`'s ADDENDUM 2 (CVO~Z, 20260725T00:1xZ) had already exhaustively re-cut
the 24-node `residual_unexplained` bucket into three groups — **GROUP1 (11): deployed under another name**
(closed, cited per-node in `A_lambda_enumeration.json`) — **GROUP2 (9): no live counterpart under any
name** (the finding itself established, but not yet split into decommissioned-vs-never-deployed) —
**GROUP3 (4): genuinely uncertain, deliberately not forced.** This dispatch's ask — "per dir,
deployed-under-another-name / decommissioned-leftover / never-deployed, with grounding" — is therefore
GROUP1-closed-already, and this section closes GROUP2 (the finer split) and GROUP3 (full resolution) with
fresh grounding: current `infra/aws/terraform/**` presence + `git log -S<name> -- infra/aws/terraform` (was
this literal name ever declared in Terraform, at any point in history, not just today) for all 13 remaining
names. `# rail-checked` marker used for these repo-history greps (a historical `git log -S` sweep over
`infra/*.tf` is not answerable by `comp-aws`/`comp-iam`, which model current relationships/permissions, not
"did this literal string ever appear in Terraform history").

### 7.1 · GROUP2 (9) — split into DECOMMISSIONED-LEFTOVER vs NEVER-DEPLOYED

| Source dir | Classification | Grounding |
|---|---|---|
| `bd-49f-freshness-probe` | **DECOMMISSIONED-LEFTOVER** | Deployed via `a875ce9895` (ADVI_BDAPIMIG P1-C), torn down via `9781bbb266` ("teardown(bd freshness): remove bd_49f_freshness_probe stack ... git-recoverable; CTO GO 222919Z") |
| `bd-cot-freshness-probe` | **DECOMMISSIONED-LEFTOVER** | Deployed via `33cf3ec713` (ADVI_COTETL.L4-GUARD), torn down via `9d13da303f` / `858554332d` ("teardown(cot freshness) ... git-recoverable; CTO GO 215352Z, Andrew clean-house") |
| `bd-served-vintage-alarm` | **DECOMMISSIONED-LEFTOVER** | Deployed via `3b6f56691f` (ADVI_BDAPIMIG.P1(d)), torn down in the SAME commit as the freshness-probe above (`9781bbb266`, one combined bd-freshness-stack teardown) |
| `inf-gold-freshness-guard` | **DECOMMISSIONED-LEFTOVER** | Deployed via `a3c0248e7d` (WS-5 PPLINF), torn down via `dd7d2da955` ("teardown(inf freshness) ... 11 destroy, git-recoverable; Andrew-flagged Class-A clean-house, CTO GO 211316Z") |
| `mdpf-freshness-checker` | **DECOMMISSIONED-LEFTOVER** | Deployed via `44101d16dd` (MDPF OPS1 D3), torn down via `e836f4c89a` ("teardown(mdpf freshness) ... 22 destroy, git-recoverable; CTO GO 225710Z, Andrew clean-house") |
| `opal-assets-absence-check` | **DECOMMISSIONED-LEFTOVER** | Deployed via `18ba785b52`/`4a39f9ed66` (OPAL_STNDRD.Z1 phase-3, "checker LIVE v0.1.0"), torn down via `c32875f7a5` ("teardown(opal-assets freshness) ... inert debris per CTO 010019Z, git-recoverable") |
| `market_query` | **NEVER-DEPLOYED** | Zero TF reference, current or historical (`git log -S -- infra/aws/terraform` = no hits). Source dir traces only to the repo's original mega-commit (`38057ad7e9`, "Initial commit"); no `feat`/`deploy`/`teardown` commit exists for it at all |
| `schwab-bronze-freshness` | **NEVER-DEPLOYED** | Zero TF reference, current or historical. Authored recently (`339f089f34`, "feat(schwab-sdd): ... INDEPENDENT bronze freshness oracle, Andrew-direct 2026-07-13") — source exists, no infra was ever provisioned for it, and there is no teardown commit (distinguishes it from the six DECOMMISSIONED rows above, which each have an explicit teardown commit) |
| `security-sweep-daily` | **NEVER-DEPLOYED** | Zero TF reference, current or historical, no teardown commit |

**This directly answers the dispatch's "9 guard dirs the estate map's sixth-instance question hangs on":**
6 of the 9 were real, deployed freshness/absence guards that a CTO-approved "clean-house" pass **deliberately
tore down** (every one of the six teardown commits self-describes as `git-recoverable`) — so for those six,
the sixth-instance question's answer is **NO, not served elsewhere; they were the freshness net, and a
sovereign-approved decision removed it**, not an extraction/rename. Only the remaining 3
(`market_query`, `schwab-bronze-freshness`, `security-sweep-daily`) were genuinely never wired to
infrastructure at all — source-only, at no point in this repo's history.

### 7.2 · GROUP3 (4) — fully resolved

| Source dir | Classification | Grounding |
|---|---|---|
| `bd-49f-etf-ownership-daily-canonical` | **NEVER-DEPLOYED** | Explicit, source-confirmed via its own authoring commit `9e89b0d702`: *"built + local-proven on 06-15..06-18, NOT deployed (data gated on Andrew silver-fire)"* — the author's own words, not an inference. A live sibling exists under a different name (`bd-49f-etf-ownership-daily`, no `-canonical` suffix, per A.md's original note), but the `-canonical` variant itself was never deployed under any name — zero TF trace, current or historical |
| `data_refresh` | **DEPLOYED-UNDER-ANOTHER-NAME** | `infra/aws/terraform/data-refresh/main.tf` is a CURRENT, live TF file declaring `function_name = "opal-data-refresh-api"` (line 36) and `function_name = "portal-time-machine"` (line 100) — matches A.md's own original candidate list (`opal-data-refresh-api`) with a live TF citation now, resolving what A.md had left as "no single confident match" |
| `mdpf-manifest` | **NEVER-DEPLOYED (as a standalone Lambda)** | Zero TF reference, current or historical. Authoring commit `f030ac80dc` ("the manifest -- the ONLY failure surface, with the gate for every rule it claims") reads as a shared validation module description, not a standalone-service description; whether it is imported as a library by another deployed Lambda was not traced (out of this item's scope) — the narrow, source-grounded claim is limited to "never had its own TF-declared Lambda resource" |
| `test_seeking_alpha_unauth` | **NEVER-DEPLOYED** | Zero TF reference, current or historical, confirming A.md's own original read (handler file literally named `lambda_function_simple.py`) — a manual test/diagnostic scratch artifact, never intended for its own production deployment |

### 7.3 · Closure summary — all 24 now grounded

| Classification | Count | Names |
|---|---|---|
| Deployed under another name | 12 | GROUP1's 11 (`A_lambda_enumeration.json`) + `data_refresh` (§7.2) |
| Decommissioned-leftover | 6 | `bd-49f-freshness-probe`, `bd-cot-freshness-probe`, `bd-served-vintage-alarm`, `inf-gold-freshness-guard`, `mdpf-freshness-checker`, `opal-assets-absence-check` |
| Never-deployed | 6 | `market_query`, `schwab-bronze-freshness`, `security-sweep-daily`, `bd-49f-etf-ownership-daily-canonical`, `mdpf-manifest`, `test_seeking_alpha_unauth` |
| **Total** | **24** | **0 remaining unresolved** |

No node was forced into a classification it didn't earn — every row above cites either a live TF file, a
specific commit hash pair (deploy + teardown), an explicit author statement, or a confirmed zero-hit search
across the full git history, never a bare assertion.

---

## 8 · Handoff

- **`1.0.0_SA_CTO~Z`**: §5's cross-batch pattern (5 new + 2 banked = 7 confirmed declared-LOUD/observed-
  FAIL-OPEN-or-worse instances on invalid/absent input, spanning three exercise passes) is a candidate
  register-wide theme, not a per-tool curiosity. §4a's reverse-direction mismatch (`comp-lambdamap`) and
  §4i's `comp-drift` no-upfront-validation observation are both flagged as open follow-ups, not closed
  findings. §7.3's closure table resolves the 24-residual item completely — 6 of the 9 "guard dirs" were
  real and deliberately torn down (not lost/renamed), which is a direct, sourced answer to part of the
  open sixth-instance investigation.
- **`3.0.0_SA_CVO~Z`**: every §3 row and every §7 classification is independently re-derivable from the
  sidecar's verbatim invocations (mine) and from `git log -S<name>` / a TF-tree grep (yours, same commands
  cited inline, no script handoff needed — these are single-command checks, not a parse pipeline like
  REC-1b's denominator table).
