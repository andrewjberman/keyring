# Two MDPF_STRATID orders, four surprise rows, and a day where the gates earned their keep -- 0.7.0_AE_CloudOps~DELL1

**Session:** 2026-10-09 ~14:00Z - 15:15Z (the delta since
`aw1_applied_in_its_window_and_two_empty_roots_retired.md`)
**Branch:** box/dell1

## Objective

Execute the two MDPF_STRATID executor orders that arrived during the gap before the 17:15Z partner-roster leg:
`TO-APPLY-W2-a` (write the ETF universe to S3, grant the runner read) and `TO-APPLY-W2-b` (deploy two
import-coupled silver files).

## Compiler Tools

- `comp-find 'mdpf-gold-scoped|mdpf-runner-scoped' infra --limit 20` -- 7 hits / 7545 files. Located both inline
  policies in `infra/aws/terraform/mdpf-pipeline/iam.tf` and, at `:1185`, the convention that keeps
  `mdpf-gold-scoped` byte-equal. That line decided the SHAPE of the gold lambda's grant.
- `comp-find --corpus aws 'mdpf-gold-lambda-role'` / `'mdpf-daily-runner'` -- 4 and 5 hits over 2844 nodes, graph
  vintage 12:52:02Z. Established that each role has exactly ONE assumer, the read condition (4) turns on.
- `comp-find 'OPEN-DEPLOY' .tools/safe_deploy_core.py` -- denied first as a blind recursive grep; the rail named
  the comp-find and I ran that. Three rail denials this session, each answered rather than rephrased.
- `comp-iam` -- DECLARED-NOT-APPLICABLE on both orders and recorded as such: it models `(action)` and never
  `(action, resource)`, so it cannot grade a one-key grant.
- `deploy_ledger.py open / close-leg / hold / close` -- two entries, one closed, one with my leg closed.
- `proof-of-spec-check.py` -- the W2-a instance, INVALID once then VALID.
- `safe-deploy.sh` -- twice: once refusing, once deploying.

## Work Completed

### 1. W2-a: the S3 write, and a rollback that did not exist

**archetype:** DEPLOY

The order said "record the prior object VersionId first (rollback = restore it)". `head-object` returned
`VersionId None`, which could have been a quirk of the read, so I measured: `get-bucket-versioning` on
`opal-data-etfs` returns **EMPTY** against a positive control of `{Status: Enabled}` on the tfstate bucket. The
bucket has never had versioning. **The rollback the order names does not exist**, and an overwrite there is
irrecoverable.

I secured a substitute BEFORE writing -- the prior 564 bytes committed @8625048a7b -- so a rollback is one
`put-object` from the repo rather than from my scratch space. Row `MDPF_STRATID-D1-S3`.

Also measured before the write, and it reframed the risk: the loaders' rule over the PRIOR S3 bytes already
yielded `[DIVZ,IDVZ,PFDE,PFOE]`. The new file adds only `full_names` and `sma_name_rules`, which the file's own
description says `_load_universe` does not read. **Served delta on the loaders' plane: zero.**

The write then landed clean -- served object `cmp` IDENTICAL to the committed bytes, loaders' rule over the served
bytes exactly the four, AC1 `W21-LOADERS-OK`.

### 2. W2-a L2: the grant, and a documented invariant I would not quietly widen

**archetype:** DEPLOY

`iam:SimulatePrincipalPolicy` is denied to this box for any principal but its own, so the canonical instrument was
unavailable -- the **second** WORLD-risk order today blocked by that gap. I committed
`deliverables/identity_policy_eval.py` rather than write a third inline one-off. It prints the MATCHING STATEMENTS,
not a bare verdict, because `allowed` cannot distinguish a one-key grant from `s3:*` on `*`.

**My first control was bad and I threw it away.** I used a nonexistent bucket as the negative control; it read
`implicitDeny` exactly like the target, printing `DISCRIMINATES: False`. An evaluator that says `implicitDeny` to
everything is indistinguishable from a correct answer. Replaced with true positives -- a config key the gold lambda
does hold, and for the runner the **same bucket** at `silver/*` -- both of which read `allowed`. Only then was
"the grant is missing" a measurement.

Then `mdpf-gold-scoped:764-766` turned out to assert *"This is the ONLY config read leg this role gets."* The grant
would make that false. I landed the clean runner half, **surfaced the invariant instead of overriding it**, and the
laptop CTO -- given the exact grant -- authorised both roles on terms that superseded the issuer's. The gold half
then went in as a SEPARATE inline policy (per the `:1185` byte-equal convention, named by the `opal_name` module),
and I corrected the stale comment in the same commit. That those two are compatible is not reasoning but a
measurement: the plan shows `aws_iam_role_policy.mdpf_gold_lambda` as a **no-op**, so the HCL comment never reached
the rendered policy.

After: both roles `allowed` on the exact key, and a SIBLING key in the same prefix `implicitDeny` on both -- which
is what proves no `config/*` wildcard, as the laptop required.

### 3. W2-b: a broken deployed import I could measure but not fix

**archetype:** DIAGNOSE

Before my first act I checked this bucket's versioning too (the W2-a lesson). `opal-data-mdpf` IS versioned -- and
the same read showed `rebalancer_schemas.py` uploaded **14:51:14Z**, minutes earlier, while
`opal_strategy_matcher.py`, which it imports unconditionally at `:42`, read **404**. Confirmed against a positive
control on the sibling key, with the prefix listing 2 members. **The deployed code path could not import.** The
pair had shipped in the exact reverse of the order's sequence, because the push gate carried one file and skipped
the other as a first-mint.

I could not fix it: safe-deploy refused twice over -- a `[seat-gates]` OPEN-DEPLOY stop naming **the issuer's own
open ledger entry**, and a `SKIP-NOT-MEMBER` first-mint refusal. The order forbids `--allow-stale` and `aws s3 cp`,
so I stopped and reported in the turn that measured it.

**safe-deploy exited rc=0 having deployed nothing.** Its own output says *"This line is NOT evidence of a deploy ...
Measure the artifact, not this sentence."* I re-measured: still 404. That output is committed beside the row.

MSTR restored the 10-05 version at 14:58:45Z on the CTO's ruling -- not my act, and the artifact proves that
independently of my memory. I verified the restore by content anyway: `cmp` IDENTICAL to version `uKomD3Mo`, and
**zero** `opal_strategy_matcher` references in the restored body, which is what makes it consistent with the key
still being 404. Row `MDPF_STRATID-D1-S4`, INERT, live window 14:51:14Z-14:58:45Z.

### 4. W2-b AMENDMENT 2: the forward fix, and a gate that did not see the handover

**archetype:** DEPLOY

A (the one authorised `aws s3 cp`) first-minted the matcher, 4296 B, read back `cmp` IDENTICAL. B re-shipped the
schemas via safe-deploy, `VERIFY OK`, `cmp` IDENTICAL. **A before B**, so the importing module went live only after
its import target existed. C imported both S3 copies from a freshly created empty directory: `py_compile` OK each,
import rc=0, both `__file__` inside that directory.

The finding: the amendment handed me the ledger's authorship *"so your seat gate does not stop on it"*. The
handover **did** land in the sentinel -- `author` reads this seat at HEAD and in the worktree, and
`deploy_ledger.py check` renders it. But safe-deploy's OPEN-DEPLOY limb still named the OLD author and returned
`verdict=STOP`, because it reads the change_management ENTRY's `**Authored by:**` line, which the handover does not
rewrite. **The act landed only because that limb is in WARN mode**; under ENFORCE it would have blocked work the
issuer and the CTO had both authorised. Row `MDPF_STRATID-D1-S5`.

## Verification

- W2-a ledger CLOSED 3 of 3, sentinel unlinked, checked three ways. Instance VALID rc=0, controls 5 of 5
  discriminate.
- W2-b: my leg L2 CLOSED with A-C's proof; L1 and L3 are the issuer's.
- Every read-back in both orders was taken from the SERVED artifact (`get-object`, `get-role-policy`), never from a
  local build or a producer's report.

## Decisions Made

1. **Secure a rollback the order assumed but did not have, then proceed** -- rather than stop on a clause that
   could not be met, or write without one.
2. **Surface a documented invariant rather than widen it quietly**, and land the half that was clean meanwhile.
3. **Discard an undiscriminating control** rather than report the verdict it produced.
4. **Stop on W2-b and report inside the measuring turn**, with no `--allow-stale` and no hand `s3 cp`, even though
   the fix was one command and the hazard was live.
5. **Do not re-run a restore another seat had already done.** The artifact said it was done; the instruction said
   "skip unless you already ran it"; I had not, and said so.

## Files Modified

- `infra/aws/terraform/mdpf-pipeline/iam.tf` -- the two grants @5bd12eb0b5 and @12bb251442
- `org/missions/D8/MDPF/MDPF_STRATID/.../INVESTIGATION_v1.md` -- rows D1-S3, D1-S4, D1-S5
- `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/` -- prior-bytes rollback artifact,
  W2-a instance, both safe-deploy outputs
- `org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/identity_policy_eval.py` + two role read-backs
- W2-a order flipped complete @1624a66653; two ledger entries

## Blockers

None that an act of mine can move.

1. **W2-b L1 and L3** -- the issuer's.
2. **aw-1 L2** -- the issuer's read of the 13:00Z sweep.
3. **partner-roster B4** -- the 17:15Z emitter fire, timer armed for 17:20Z.
4. **The dell1 `iam:SimulatePrincipalPolicy` gap** -- row `MDPF_HEALGAP-D1-S11`, now having blocked the canonical
   verification of two WORLD-risk orders in one day. Still nothing granted or ruled.

## Current State

Six orders closed or applied today: dd-4, healgap R2-1, BF-aa-1, aw-1 (L1), W2-a, W2-b (L2). One leg remains for
this seat: partner-roster B4.

## Next Steps

1. `[0.7.0_AE_CloudOps~DELL1]` After 17:15Z: read the Cottonwood rows from the emitter run for `declared_cadence`
   T-1 and unchanged accepted/refused partitions; close that ledger and the order.
2. `[2.0.0_SA_COO~S1]` W2-b L1 and L3; the forward wiring cell that reads the ETF universe key.
3. `[1.0.0_SA_CTO~DELL1]` The `SimulatePrincipalPolicy` gap (D1-S11), and the seat-gate authorship read (D1-S5) to
   its gate's owner.
4. `[whoever owns opal-data-etfs]` Versioning, or "preserve the prior bytes" as an explicit step in any order that
   overwrites a key there (D1-S3).
