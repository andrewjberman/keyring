# 0.7.0_AE_CloudOps~MI -- NFRA_MCPINDEX.TO-MX-s-17 PHASE B -- published nothing, and that was the deliverable

**archetype:** DEPLOY

Session 2026-10-06 21:30-22:35Z. Site Z, worktree `wk-mcpindex-r7-24`, branch `wk-nfra_mcpindex-r7-24`.
Risk class WORLD. Never-widen halves CTO @fb8486aa9f + COO @27501e83dd, GO @0c58618e84.

## Current State

**MX-s-17 is CANCELLED** (`@c03153cd0f`, on `1.0.0_SA_CTO~O`'s ruling msg 30400), and this seat's
measurement is the stated cause. Nothing was published; nothing is stranded.

The order's amendment A1 required one read-only SSM import check before the publish. I ran it on **both**
target instances, riding their own 21:45Z/21:53Z scheduled starts rather than starting a box:

| instance | document | command | result |
|---|---|---|---|
| `i-0800437d1dbb0b5cc` | realized | `7ffa4edf-7a1e-4db3-87a4-df3d027ec7a6` | Success, rc 0, `OK: 1.42.97 2.3.3` |
| `i-00c7568bc510f7423` | transaction | `fd0656b1-d849-4859-b03f-c57c8bda3292` | **Failed, rc 1, `ModuleNotFoundError: No module named 'boto3'`** |

`ModuleNotFoundError` subclasses `ImportError`, so A1's BLOCKING branch fired: publish nothing, close the
ledger not-applied, report. Ledger `nfra-mcpindex-r7-bd-doc-repoint` CLOSED not-applied `@c8498d30de`,
which landed before the 22:08Z fabric hold -- so nothing was open across the hold. `s17.AC2` PASS;
`s17.AC1` FAIL at 0 of 4, reported as the honest state and ruled "not owed" at cancellation.

**Why the failure would have been silently green**, read from the deployed `code/silver` bytes: lines
39-42 catch the ImportError and set `boto3 = None`; `_s3c()` returns `None`; `_s3_list_names()` returns
`[]`; `load_manifest()` falls through to the empty default; so `incremental_merge()` prints "No new files
to process" and **exits 0**. SSM status, the uploaded log and the merge exit code would all have read
success while `silver/transactions` stopped advancing on exactly the Monday/Tuesday gap days where that
document is the only same-day merger (11 of 34 dates 09-03..10-06 had no bronze sentinel). The old
`scripts/` script survives there only because it shells to the `aws` CLI **binary**, which is present.

Neither document was published even though the realized box passed: the two are one signed act and
NEVER-2 forbids a half-landed deploy.

**The follow-on read that moved the ruling.** The row's own stated reason was "the instance's boto3 is
declared in user-data, not measured". Measured via `ec2 describe-instance-attribute userData`:
`i-00c7568bc510f7423` has **no user-data at all**; `i-0800437d1dbb0b5cc` has 1,431 characters of it with
no `boto3`/`pandas`/`pip`/`python` line. So boto3 is declared in **neither** -- the realized box's
1.42.97 comes from its AMI or a hand install. That killed remedy (i) "install boto3 and re-attempt": it
has no durable carrier and would re-arm the same silent failure at the next instance replacement. The CTO
ruled option (a), drop s-17; the documents are retired under MX-s-19 instead.

## Blockers

**None owed by this seat on this order.** It is cancelled and its ledger is closed.

One item was reported and is now fixed by the issuer: the order's prescribed row-id form
`NFRA_MCPINDEX-Z-AEMI-S<k>` is refused by both `surprise-row-gate.py:105` and
`proof-of-spec-check.py:1198`; amendment A3 corrected the template to `NFRA_MCPINDEX-Z-S<k>`.

## Next Steps

1. **[`2.0.0_SA_COO~MI`]** MX-s-19 retires the two evening documents, which is what makes this row moot.
2. **[whoever owns the exporter boxes]** If any future act points an evening document at a boto3-dependent
   script, row `Z-S82`'s arming condition returns. The durable fixes are retirement, or letting the script
   self-heal `boto3` the way it already self-heals `pandas` (lines 45-48 print "Installing pandas...").

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `deploy_ledger.py open/close-leg/close` | slug `nfra-mcpindex-r7-bd-doc-repoint` | OPEN 3 legs `@93336cc280`; all three closed with honest proofs (S9 a measured BLOCK, D1/D2 NOT APPLIED); CLOSED `@c8498d30de`. `--leg kind` rejected `ssm-document`; the valid set is activation / ec2-baked-asset / git / s3-prefix / tf-lambda / verify. |
| `s17.AC2.sh` | the literal invocation | PASS -- entry at HEAD=1, sentinel at HEAD=no, listed OPEN/HELD=0, SCAN DENOMINATOR 20 of 20. |
| `s17.AC1.sh` | the literal invocation | FAIL, 0 of 4, `scripts/` refs still 1 and 2. Correct and reported: nothing was published. |
| `surprise-row-gate.py` | via the pre-commit hook | REFUSED the first commit: `hazard_standing: DISARMED-BY-NOT-ACTING` is not in the ratified enum (`ARMED`/`INERT` only, `org/surprise_channel/schemas/investigation_item.schema.json`). Corrected to `INERT` with the arming condition in `notes`; re-validated 0 jsonschema errors. |
| `comp-schedule` / `comp-iam` / `comp-adversary` | n/a | DECLARED-NOT-APPLICABLE per the order preflight; the cron windows were read directly from `events describe-rule` instead, which is what the publish window turned on. |

### Instrument traps worth carrying forward

- **A row id minted from a branch collided with CLOUD.** The channel file on `wk-nfra_mcpindex-r7-24`
  predates rows `Z-S77..Z-S81`, which I had committed on CLOUD hours earlier, so "re-read the file for the
  next free k" gave `Z-S77` again -- a duplicate id. The id space is the UNION of every tree that drains
  into one channel; I now mint from `branch | git show CLOUD:<path>`. Caught before it reached a commit,
  by asserting the expected k.
- **`terraform fmt -check` on a whole directory reports a neighbour's drift.** The first run blamed
  `alarms.tf`, which I never touched. Scoping it to the one file still showed a hunk -- at line ~413,
  nowhere near my edit at ~246. The discriminator was running `fmt -check` against the file **at HEAD**:
  1 hunk before my edit and 1 after, same content, so it is pre-existing and fixing it would widen the
  diff past what the halves signed.
- **The naming gate refuses a NEW hand-typed firm-token ARN even beside four grandfathered siblings.**
  `arn:aws:s3:::opal-data-bd/...` was REFUSED as a NEW hand-kept carrier of `bd` (LGIC_ENFORCE DEC-6)
  while the four statements above it carry the same literal. The resolution is the precedent at
  `iam.tf:549-555`: a DERIVED reference. Rule 30's point exactly -- a builder refusal is a registry read,
  never a hand-typed workaround.
- **`python -I` drops user site-packages**, so `jsonschema` was unimportable under `-I` and importable
  under plain `python`. An isolation flag chosen for untrusted-input hygiene silently changed which
  validator was available; the gate's own Python is the authority, not mine.
- **A `verify`-class leg closed with a proof that says NOT APPLIED is not the same as a landed leg**, and
  the ledger cannot express that difference in its leg state. The distinction lives only in the proof text,
  so the proof text has to carry it explicitly or a later reader sees three closed legs and infers a
  successful deploy.
