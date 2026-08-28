# The apply that carried the fold — and the census that inverted my read of the validator — ETFS_INGEST.TO-10-AE — 0.7.0_AE_CloudOps~I

**Date:** 2026-08-28
**Task Order:** ETFS_INGEST.TO-10-AE
**Status:** COMPLETE — 3 of 4 criteria closed; AC3 event-gated and correctly left open
**Session:** 18:35Z – 19:05Z

## Objective

Deploy the `etf-positioning-producer` Lambda package carrying the ETFClassifier fold (`b0e1f33471`,
the GICS decode moved INTO `ETFClassifier` on Andrew's "properly managed within ETFClassifier"),
ahead of the ~13:00Z scheduled fire. The deployed package was 02:43:57Z and the fold is 18:3xZ, so
the running bytes did not carry the decode. Terraform only; `aws lambda update-function-code` banned.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-which` | `comp-which "is the deployed etf-positioning-producer Lambda running the same bytes as the source at HEAD, and what commit was it built from"` | Printed a 3-way near-tie (`comp-aws` / `comp-estate` / `comp-iam`) and explicitly labelled it NOT a ranking. **It did not surface `comp-closure`** — the tool for exactly this question, and the one TO-9-AE's run of the *same* question did surface. |
| `comp-closure` | `comp-closure compile etf-positioning-producer --out <scratch>` | `equivalence=DIVERGENT`, `reach=PRESENCE_ONLY`, `standing=CURRENT`, `members compared=2`. Confirmed `live CodeSha256 == artifact_sha256` (no undeployed artifact pending → no half-state inherited) and named `last_deployed_commit 25f30acc63`, which the content comparison then corroborated independently. |
| `proof-of-spec-check.py` | on this TO's instance, and on TO-9-AE's as a control | `INVALID`, 3 violations — all one upstream root cause. See the finding below. |
| `commit-gate` (via `safe-commit.sh`) | automatic, both commits | `WARN: checked 0 of 1` / `0 of 2 file(s) — NOTHING WAS CHECKED`. Correct and correctly loud: this TO committed only `.md` + a `ci/*.json`. Recorded rather than omitted, because a clean-looking gate line here would be evidence of nothing. The **risk-reflex** did fire substantively on `lambda-source-map.json` (13 recorded claims; citation read before proceeding). |

**What worked:** `comp-closure`'s `live CodeSha256 == artifact_sha256` read is what established the
baseline as *clean* rather than assumed — it ruled out an undeployed-artifact half-state in one call,
before anything was touched.

**What failed:** `comp-which` routed the same question differently than it did 16 hours earlier
because I re-worded it. Its score is token overlap, so a re-phrasing moved the right tool off the
list entirely. Not a defect — but it means a comp-which miss is not evidence a tool doesn't fit.

**Gap found:** `comp-closure` compares **2** members; this package has **3**. The classifier lives in
a different tree, `files[]` is joined to a single `source_dir` and structurally cannot express it —
so **the member this entire TO is about is the one member `comp-closure` cannot see.** The in-zip
`BUILD_MANIFEST.json` is the member list of record. Same gap TO-9-AE filed; still open.

## Deployment Sequence

| # | step | evidence |
|---|---|---|
| 1 | Premise re-established by CONTENT, not the TO's clock | deployed classifier `8138da03…` == `git show 25f30acc63:<path>` (the pre-fold vintage); pin's is `c677e8a5…`, 14027 B. Negative control: `def resolve` at `:262` in the pin, ABSENT from the deployed member. |
| 2 | Confirmed nothing was half-landed beforehand | deployed publisher `62200af2…` == `25f30acc63`'s. Pre-fold publisher **and** pre-fold classifier — self-consistent, serving old labels. |
| 3 | Pin currency measured twice | the 3 PACKAGE members are byte-identical from `b0e1f33471` → `b066be7a92` → the moved HEAD `a951b1bd21`; positive control (all-paths diff) non-empty both times. |
| 4 | Ledger OPENED | `16db6d3529`, before the S3 upload — the first world-touching act. |
| 5 | Built at pin | `b066be7a92` → 162733 B, sha256 `a9093da2…`, 4 zip entries. All 3 members `cmp` clean against git **before** upload. |
| 6 | Exercised the fold on the built bytes | `self_test()` → 7 completions PASS / 0 FAIL, 5 negative controls REFUSED / 0 ACCEPTED. |
| 7 | Rollback handle captured, then uploaded | prior VersionId `hJpn.bewspw6DHf8Suot920st5dxfAhN` (its `content-sha256` == then-live `CodeSha256`); new `7r5NQeGQE9Nj.2G9ARqpZMBfEfIwfiii`, verified on the primitive at 162733 B. |
| 8 | Plan (read-only), saved to a file | `0 to add, 1 to change, 0 to destroy`. |
| 9 | **APPLIED** the reviewed plan file | `.tools/safe-apply.sh … apply tfplan.to10ae` at 18:49:14Z → `0 added, 1 changed, 0 destroyed`. |
| 10 | Re-plan | `-detailed-exitcode` **rc=0** — scored on the exit code, not on the sentence. |
| 11 | AC1 on the live plane | package re-downloaded from `Code.Location`, byte-identical to the built artifact; all 3 members `cmp` clean vs `git show b066be7a92:<path>`; 2 negative controls fired. |
| 12 | Tagged | `etfs-positioning-v1.4.0`, annotated, **cut on the pin** and verified to peel there. |
| 13 | Rule 4 + ledger CLOSED | `355911b9db`. |

## Verification

    CodeSha256    wuu+/cHD5gHb3B1iY3wjGq4rB0ozzF7Hm/ooH086P8I=
               -> qQk9ohLihOInJnvj/NncAms1IuoEIkkjRwpb8EIFouQ=    MOVED — and NOT cited as acceptance
    LastModified  2026-08-28T18:49:14.000+0000    State Active
    UNCHANGED     python3.11 | 512 MB | 120 s | handler etf_positioning_gold.lambda_handler
    CONTENT       live package re-downloaded AFTER the apply; sha256 a9093da2… == the artifact
                  built at the pin. `cmp` byte-identical. THIS is the claim.
    DID-NOT-MOVE  9 of 10 managed resources (denominator: `terraform state list`), INCLUDING
                  aws_cloudwatch_event_rule.etf_positioning_producer_daily —
                  cron(0 13 * * ? *), ENABLED, read on the live primitive after the apply.

**AC4:** pre-state measured on the served artifact (189 rows, 189/189 carry `industry_group`, 180
non-null, basis `observed` 180 / `not-applicable-non-equity` 8 / `absent-from-source` 1). Driving the
**deployed** module over all 189 rows through the publisher's own `_industry_group` branch logic:
189 in / 189 out, **0** rows missing either key, **0** rows lose a value, non-null 180 → 180, 59 rows
changed across 7 labels. ⚠ **The 59 is a PREDICTION** — computed from *today's* served artifact as
input, while the fire's input is *tomorrow's* pull.

## THE FINDING — I had it backwards until I ran the denominator

`proof-of-spec-check` reported my instance `INVALID` on 3 alignment violations: `INGEST-T3-6` and
`INGEST-T5-1` "do not exist" in the decomp, and `<owned_cells>` is "non-id text".

A token census said both cells **do** appear (×2 and ×1). So my first read was *the checker's regex is
too narrow*. **That read was wrong, and the thing that corrected it was a denominator I nearly didn't
run.** `CELL_ID_RE` requires a lowercase segment; across **31** `DECOMP.md` files, **30 use that form
and `etfs-ingest` is the sole outlier** — 29 uppercase `INGEST-T*` ids, of which the checker sees
**zero**. The `id space = 4` it prints is an incidental `ETFS-d-*` / `ETFS-e-*` family in the same
file. **The decomp is the outlier, not the regex.**

Control: the already-filed **TO-9-AE instance fails identically** — pre-existing and systemic to this
project, not introduced here. Consequence: *every* ETFS_INGEST proof-of-spec instance is INVALID on
alignment regardless of row quality. **Not adjudicated** — renaming 29 cells vs widening a
fabric-wide regex have very different blast radii, and that is the decomp author's / CVO's call.

⚠ The one violation that **was** mine — a missing `status_reason` on the event-gated AC3 — is fixed
(4 → 3). *A checker verdict is a claim about my artifact until I check whose artifact it is about.*

## Decisions Made

1. **Pinned at `b066be7a92`** (the TO's own face commit) rather than at the fold, having measured
   that the 3 members are byte-identical between them — so the manifest names a commit that contains
   the fold *and* the TO that ordered it.
2. **Applied a SAVED PLAN FILE**, not a fresh `apply`. What landed is exactly what was reviewed.
3. **Tagged on the pin, explicitly.** HEAD moved twice mid-session (`a2e2bc07b0` → `a951b1bd21` →
   `f91b7592`); a bare `git tag -a` would have recorded a peer's commit — the trap TO-9-AE caught.
4. **Read the tag list instead of assuming the next number** — `v1.3.0` was already taken by a THIRD
   apply this seat's own TO-9-AE log does not record.
5. **Did not run an ad-hoc invoke.** It would destroy the discriminator the scheduled fire exists to
   produce. AC3 stays open; that is the correct state, not an incomplete one.

## Files Modified

| file | commit |
|---|---|
| `org/critical_paths/change_management/20260828T1845Z_…_deploy.md` | `16db6d3529` (OPEN), `355911b9db` (CLOSED) |
| `infra/aws/lambda/ci/lambda-source-map.json` | `355911b9db` |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ETFS_INGEST.TO-10-AE_PROOF_OF_SPEC.json` | this commit |

## Blockers

**NONE at this seat.** The apply landed with the issuer's GO (13708).

**Owned elsewhere, listed so they are not read as mine:**
- [`2.0.0_SA_COO~Z` / `3.0.0_SA_CVO~Z`] The ETFS_INGEST decomp's cell-id form. Surfaced, not
  adjudicated; it invalidates TO-9-AE's filed instance as well as this one.
- [`0.0.0_AB_MSTR~Z`] `etfs-positioning-v1.4.0` and commits `16db6d3529` / `355911b9db` need an
  integrator push. `--follow-tags` is not mine.
- [`0.4.0_DS_ClientPlatform~Q`] AC3's served census after the 2026-08-29 ~13:00Z fire.

## Current State

Deployed, verified against the BUILD INPUT on the live plane, ledger CLOSED, nothing half-landed.
The next ~13:00Z fire will run these bytes. **What that fire produces is not claimed here** — AC3
forbids it, and the 59-of-189 is a prediction, not a bar for it to clear.

## Surprises (channel: `3.0.0_SA_CVO~Z`, class OBSERVATION, standing INERT — none chased)

1. **The ETFS_INGEST decomp's cell-id form** — the finding above. 1 of 31 decomps; blocks
   proof-of-spec validation for the whole project.
2. **The halt gate BLOCKED this `~lane` seat** on messages in the BASE inbox, while
   `docs/architecture/ADHC_HALTGT.md` records that "a `~lane` agent is unhaltable regardless."
   **The gate behaved BETTER than its own documentation predicts.** Worth a read because that doc is
   what a seat consults when deciding whether to trust a HALTGT pass.
3. **`etfs-positioning-v1.3.0` already existed** — a THIRD apply on this package at 02:43:57Z that
   this seat's own TO-9-AE log (which ends at the second, 02:26:49Z) does not record.
4. **The mutant's failure mode changed between TOs.** TO-9-AE's control produced
   `ModuleNotFoundError` from a *missing member*; this fold moved the decode INTO an
   already-shipped module, so the module resolves and only the NAME is missing —
   `ImportError: cannot import name 'resolve'`. **A control inherited from the previous TO would
   have looked for the wrong exception and passed vacuously.**
