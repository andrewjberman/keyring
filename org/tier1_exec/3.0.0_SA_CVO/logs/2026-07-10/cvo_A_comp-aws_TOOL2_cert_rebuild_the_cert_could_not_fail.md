# CVO~A — comp-aws TOOL-2: the cert could not fail. Rebuilt so a verdict must say what it observed. CTO-GREEN.

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Date:** 2026-07-10 ~15:12–15:55Z · **Agent:** 3.0.0_SA_CVO~A (lane A)
**Task:** CTO GO 151926Z (NFRA_TOOLPASS tool-2, comp-aws). Do-er role, NOT verifier.
**Gate:** CTO GREEN @ 155254Z on commit `37b76f7ec` (verified independently, did not re-run my tests).
**HEAD at start:** `34f835110` · **Landed:** `37b76f7ec`

## The role inversion (load-bearing)
Andrew killed the validation harness. Per-tool method: CTO+Andrew front-run for purpose+branch coverage;
I own continued analysis + THE CODE FIX + the mutant-kill bar; CTO gates the diff; I brief COO. **I am the
do-er, not the verifier** — I did not certify my own fix. Why no harness: a harness must encode the right
answer, and if I can compute it mechanically I've written a second implementation that may share a predicate
(`comp_route.py:761-766` is comp-which's own floor-check, seeded with a string that never enters the broken
branch — green forever, guarding the bug).

## The disease: a verdict that could not say what it observed
comp-aws's cert `score` graded the derive against frozen hand-audit fixtures and could not fail:
- **A1** `main()` discarded every handler return → nonzero only on an uncaught exception. `score --class
  zzqq-nope` exited 0 and `.tools/comp-aws` logged it PASS (launcher pipes `$?` to comp_log_auto). Success
  token bound to the wrong step; audit log poisoned.
- **A2** the 6 s3 "false positives" all EXIST — precision was measuring fixture staleness (16d), not compiler
  accuracy. An F1 against a frozen fixture is an aging clock.
- **A3** ec2 leg `_f1(tp, 0, fn)` — fp hardcoded 0 → `declared_f1` structurally 1.0000, blind to a phantom
  instance. A control that has only ever printed one value is not a control.
- **A4** `count_match` (111 vs 168) computed, printed, never scored. **A5** 27/30 classes unmeasured,
  UNSCORED byte-identical to INVALID. **A6** no vintage printed. **A7** unmappable ARN → rc0. **A8** `--class`
  derive silently emits no edges. **A9** `derive` persists nothing.

## Unknowns resolved by EXECUTION (source proves possibility; execution proves actuality)
- **U2** (the crux — it's a RECALL miss, the metric CTO's ruling keeps): `market-update-lambda-role` was
  GENUINELY REMEDIATED. Policy doc v2 = 4 statements, zero wildcard; 3 inline scoped incl an explicit Deny on
  bd secrets. `simulate-principal-policy` (independent instrument, not CTO's head-bucket predicate):
  DeleteObject / cross-bucket GetObject / DeleteItem all `implicitDeny`; pos control opal-news-lambda-role
  DeleteTable `allowed`; neg control rc255. So A2-iam stands, on the policy DOCUMENT. BUT `broad_managed`
  is right for the wrong reason — substring-matches a policy NAME, blind to all 376 inline policies. Census
  (denominators printed): 168 roles, 376 inline, **0** effective-wildcard → blindness REAL BUT LATENT.
  Honesty limit banked in-code: that 0 is a floor under MY predicate (svc:* on scoped resource, Get*,
  NotAction, Condition uncaught), not a proof.
- **U3**: 0/6 fixtures carry `as_of`; all 3 carry `meta.tf_commit_at_audit` (commit-ish > date). Vintage
  resolver: meta.as_of → git-last-commit-of-fixture → UNKNOWN(fail-closed). NEVER mtime.
- **U4** (gated A9's wording): comp-kuzu's canonical surface = `kuzu_nessie_db` (Nessie); bare `snapshot`
  feeds the NON-canonical tarball `kuzu_db`. **CTO's proposed A9 wording "use snapshot to publish" would have
  perpetuated A9.** Banner now names `--commit-to-nessie`/`iceberg-commit`/nightly and says bare snapshot
  does NOT refresh the queried surface.
- **U1/U5** stand as unknowns. 27/30 UNMEASURED never "clean"; L3 UNTESTED, never PASS.

## Two findings BEYOND the A-list
- **A11** (found by RUNNING CTO's D9 consumer-enumeration lesson, not reading): `cmd_iceberg_commit` read
  `e["src"]/e["dst"]` while both edge producers emit `{source,target}` → every `graph_edges` row written with
  EMPTY endpoints (required=True satisfied by ""). Stale duplicate of `derive_runner.commit_to_iceberg`,
  2 lifetime invocations. FIXED + FAIL-CLOSED. Recommended for DEPRECATION. Write path UNEXERCISED.
- **Declarative drift**: all 3 fixtures loaded by hardcoded filename, every filename disagrees with
  `meta.fixture_version` (s3 file v1.1/meta 1.5; iam v0.1/0.2; sfn v0.1/0.2) → surfaced as `filename_version_skew`.

## CTO's own A1 remedy was inverted — caught by exercise
CTO's literal Part-7 bar `sys.exit(args.fn(args) or 0)` inverts: `cmd_derive` returns the graph DICT (the
nightly's contract, `derive_runner.py:100` in-process), so SUCCESS→rc1+graph-to-stderr, FAILURE→rc0. Built
`cmd_derive_cli` as a CLI seam owning the rc; `cmd_derive`'s return byte-identical. CTO confirmed at source.

## The fix (commit 37b76f7ec)
Six edits + the A11 write-guard. `score` offline/deterministic; precision+f1 → `UNAVAILABLE`; **UNRECONCILED
is the third state** (nonzero rc) — neither compiler-fp nor fixture-gap until a human looks; `--reconcile-fixture`
is the separate networked pass that classifies EXISTS/ABSENT and writes a gap report, NEVER amending the
fixture. `_f1` DELETED. Exit codes PASS0/FAIL1/INVALID2/DERIVE-ERROR3/UNSCORED4. `FIXTURE_STALE_DAYS=14`
(CTO-confirmed; STALE advisory-never-rc — age-fails-cert would rebuild the aging clock).

Live verdicts: `score --class s3` → RECALL 1.0 / ATTR 1.0(62) / UNRECONCILED 6 / PRECISION UNAVAILABLE, rc1
(was `0.9118 BELOW 0.95, rc0`); `stepfunctions` → PASS, rc0 (the negative arm holding in production).

## Mutant-kill bar — not run green, INJECTED red
`org/modules/graph/tests/test_comp_aws_cert_mutants.py`, 23 tests. All 5 named mutants injected and confirmed
RED, then all-green on restore — incl CTO's own A2 mutant (auto-absorb extant extras → precision structurally
1.0 → cert can never fail; the trap he struck his own bar to avoid). A green suite is not evidence a test can
catch anything; each was shown to catch its mutant. One test failure during the pass was a real bug in MY code
(`path.relative_to(WS)` throws for a fixture outside the tree) — fixed, not silenced.

## Workflow closed
CTO GREEN 155254Z → I sent COO the implementation package 155436Z (naming/.tools, grain-ladder manifest entry,
subcommand-doc audit, A11 deprecation-recommendation, predicate-note-stays-open) + flagged the NFRA_TERRAFORM
adjacency (comp-aws derive's drift ledger IS what TO-1/TO-2 want; usable-but-27-classes-uncertified). I hand a
package, not TOs (Rule 8). Nothing stranded; no deploy, no ledger.

## Compiler Tools
| Tool | Call | Result | Note |
|---|---|---|---|
| comp-symbols | `comp_aws_cli.py` | 69 fns, 2691 lines | oriented the file before editing (HUD-routed from a grep) |
| comp-grep | `'comp-aws'` / `'comp_aws_cli'` | consumer census | A9/A1 safety: `derive_runner.py:100` is the ONLY code consumer of cmd_derive's return; no CI/hook branches on rc |
| comp-surface-check | auto (safe-commit) | `OK: no critical surface` | advisory; read directly per LD-0273 |
| off-rail (NFRA_TOOLPASS §6) | raw `aws iam/s3api simulate-principal-policy`, `git show/log` | U2/U3/A9 ground truth | assurance oracle must NOT share comp-aws's predicate — named exemption, marker carried |

Off-rail was structural + by design here: ground truth for a tool under test may not share the tool's
predicate (§6 ruling). Each `aws` probe carried a positive AND negative control; denominators printed on every
scan (168 roles, 376 inline, 30 classes, 6 fixtures). Caught my OWN retrieval defects twice mid-pass —
`head`-swallowed rc, MSYS-vs-native `/tmp` split, `MSYS_NO_PATHCONV` on the aws launcher — each corrected, not
papered over.

— 3.0.0_SA_CVO~A
