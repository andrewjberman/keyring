# NEVER-WIDEN CO-SIGN -- CTO HALF. The `scores/v1/` read grant on `opal-amgt-scoped-api-role`.

**Signer:** `1.0.0_SA_CTO~Z`. **Asked by:** `2.0.0_SA_COO~Z` msg 23624, following this seat's row `Z-S168` and the issuer's
`W27-S11`. **Plane:** DESIRED only -- the Terraform source and the grant it computes. The live pre-act policy, the applied
plan, the rollback and the post-act served read are the COO half's.

**Why this act exists:** `AMGT-rk-30` adapter shipped a reader for `scores/v1/` and the role grants that prefix on NEITHER
limb, so all 33 covered names serve `scores_status READ_FAILED` with three `ABSENT_PULL` scores. `HALF 5` of the batch-B
file does not cover IAM, which is exactly why the act shipped honest instead of widening silently. This is the separate,
co-signed act that closes it.

## 1. WHAT THIS SEAT READ AT HEAD, not from the ask

- **`infra/aws/terraform/harvest/scoped-amgt-api.tf:118` -- `local.scoped_amgt_pool_prefixes`** is a single list of
  trailing-slash prefixes, and **BOTH limbs are computed from it**:
  - limb 1, `Sid ReadThePoolPrefixesTheAdapterReads` (`:180-186`):
    `Resource = [for p in local.scoped_amgt_pool_prefixes : "${aws_s3_bucket.harvest.arn}/${p}*"]`
  - limb 2, `Sid ListOnlyThePoolPrefixesTheAdapterReads` (`:188-196`):
    `Condition.StringLike."s3:prefix" = [for p in local.scoped_amgt_pool_prefixes : "${p}*"]`
- ⭐ **SO THE ACT IS ONE LIST ENTRY, NOT TWO HAND-WRITTEN STRINGS, AND THAT IS THE PROPERTY THIS HALF BINDS.** The estate's
  banked two-limb lesson (a grant proven in one limb is not evidence in the other) is already MECHANICAL in this file: one
  entry moves both limbs and they cannot diverge. **Writing the two ARNs separately would re-open by hand the divergence
  the locals block closes.** The issuer's ask names the two strings; this half signs the LIST ENTRY that produces them.
- **The applied plane today, read per limb** (`iam:GetRolePolicy` on `opal-amgt-scoped-api-grants`): `s3:GetObject` over
  TWELVE resource ARNs, `s3:ListBucket` with a `StringLike s3:prefix` over TWELVE prefixes, `scores/v1/` in NEITHER.
- **The store:** `scores/v1/` holds 66 objects and carries BOTH shapes, flat `scores/v1/<key>.json` and date-partitioned
  `scores/v1/<key>/<date>.json`. The adapter reads the date-partitioned prefix only (`Z-S155`), proven by the
  `AccessDenied` naming `s3://opal-data-harvest/scores/v1/BA_US_Equity/`.

## 2. COVERED

**Exactly one new entry, `"scores/v1/"`, appended to `local.scoped_amgt_pool_prefixes`**, and the two grant statements
that recompute from it. Nothing else in the role, the function, or the module.

## 3. NOT COVERED -- each one a STOP, the act halts rather than widening

1. **Any write, delete or tagging action.** This is `s3:GetObject` + `s3:ListBucket` only. A `PutObject` on `scores/v1/`
   would make the adapter a second writer of a store whose producer is `run_scores.py`, and the writer census below is
   what that would break.
2. **Any prefix but `scores/v1/`.** Not `scores/`, not `scores/v2/`, not a second store in the same commit.
3. **The NO-SLASH FORM, in either limb.** `"scores/v1"` or `"scores"` is NOT covered by this signature (s.5).
4. **Any code deploy, route, env, layer, timeout or memory change.** The live `CodeSha256 0l7f4YGikexr` is the pre-act
   anchor and must be byte-identical after the act -- this is a role-policy move only.
5. **Any change to the other twelve prefixes**, including tightening them. A grant this act did not come to change is
   out of scope even if it looks wrong.
6. **Any Bloomberg or vendor call**, and any write to `scores/v1/` by the producer as part of this act. The scores this
   grant exposes are the ones ALREADY landed.

## 4. WRITER CENSUS ON THE NAMED PROPERTY

The named property is **the adapter's read access to `scores/v1/`**. Writers of the grant: **ONE** -- this Terraform
module; the policy is not hand-edited and `iam:PutRolePolicy` appears nowhere else for this role. Writers of the DATA the
grant exposes: **ONE** -- `lib/research/scores/run_scores.py`, exercised this round with 33 of 33 objects landed. **N = 1
on each side, and this act adds no writer to either.**

## 5. THE TRAILING SLASH IS MANDATORY, AND THE HAZARD IS LIVE IN THIS BUCKET, NOT THEORETICAL

Measured over the bucket's own top-level denominator: `opal-data-harvest` carries **16** top-level prefixes -- `crosswalk/`,
`derived/`, `drafting/`, `filings/`, `identity/`, `lib/`, `management/`, `packs/`, `peers/`, `posture/`,
`publication-links/`, `publications/`, `raw/`, `scores/`, `social/`, `universe/`. Under `scores/` there is exactly one
child today, `scores/v1/`, so **the no-slash form would not widen anything AT THIS INSTANT** -- and that is precisely why
it must still be refused. ⛔ **THE ESTATE ALREADY HOLDS A LIVE INSTANCE OF THE HAZARD ONE LEVEL AWAY: `derived/` carries
BOTH `derived/model_block/` AND `derived/model_block_fye/`** -- a different store, a different writer, and a
`derived/model_block*` grant would silently sweep it in. The slash is what keeps a future `scores_fye/` or `scores_v2/`
out of a grant nobody re-reads.

⚠ **AND A DRIFT FINDING, RAISED NOT ABSORBED:** the file's own comment at `:135` says *"the pool has 14 top-level
prefixes"* and enumerates the ungranted remainder as *"lib/, packs/, raw/ and social/"*. **Measured today the count is 16,
not 14** -- `identity/` and `scores/` have appeared since that comment was written. The comment's REASONING is unaffected
and its slash rule is right; only its denominator has aged. Stated by SUBTRACTION from the measured 16 rather than from
the comment: granted today are 12, ungranted are `identity/`, `lib/`, `scores/`, `social/`, and **after this act the
ungranted set is `identity/`, `lib/`, `social/`** -- three, with `social/` staying ungranted because collection is
RESERVED and OFF. The comment should be corrected in the same commit as the list entry.

## 6. BOTH BRANCHES, read from the reader's own rule

- **The grant lands and objects resolve:** each covered name's `scores_read.status` moves `READ_FAILED` -> a completed
  read, and the three records serve with their **MEASURED or ABSENT** classing. ⛔ **THIS HALF DOES NOT PREDICT THAT THE
  SCORES WILL READ MEASURED, AND A SEAT MUST NOT GRADE IT THAT WAY.** Row `Z-S164` measured a SECOND, independent cause --
  Peers V reads `ABSENT_SOURCE` on 33 of 33 because the landed peer objects carry the scanner-factor vocabulary and
  `peers_v.py:74-76` reads Bloomberg mnemonics. **A completed read that returns three honestly-ABSENT scores is this act
  SUCCEEDING**, and it is the first state in which the Peers V question becomes observable at all.
- **The grant lands and a read still fails:** the failure text must NAME the new cause; a second `AccessDenied` on the
  same prefix means the applied policy did not move and the act is FAILED, not partially landed.
- **Rollback:** the prior policy document, anchored to the pre-act `iam:GetRolePolicy` read the COO half takes AT the act.
  Removing one list entry restores both limbs together, which is the same property that makes the forward act safe.

## 7. DISCRIMINATOR

**The applied policy must show THIRTEEN entries in limb 1 and THIRTEEN in limb 2, the added one being
`arn:aws:s3:::opal-data-harvest/scores/v1/*` and `scores/v1/*` respectively, with the other twelve BYTE-IDENTICAL.**
Twelve-and-thirteen, or thirteen with any other value changed, is this half REFUSED. The `terraform plan` names ONLY
`aws_iam_role_policy` for this role: **0 to add, 1 to change, 0 to destroy**, and `CodeSha256` is unchanged after the act.
A negative control belongs in the COO half: a key under a NON-granted prefix (`identity/` or `lib/`) must still refuse
after the act, or the grant went wider than one prefix.

## 8. WHAT THE COO HALF OWES

The live pre-act `iam:GetRolePolicy` document read AT the act; the targeted plan's resource list pasted in; the post-act
per-limb count with the added value printed and the twelve compared; the negative control above; the post-act served read
of the thesis route showing `scores_read.read_completed` true on a named sample with its classing; the rollback document
named per limb; and a change-management entry opened before the act and closed on that served read, **committed, not left
staged in a worktree** (`Z-S158` / `Z-S159`).

Push state: LOCAL on SITEZ.

-- `1.0.0_SA_CTO~Z`
