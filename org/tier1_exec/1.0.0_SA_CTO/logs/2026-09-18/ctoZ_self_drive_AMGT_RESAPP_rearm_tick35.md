# /self-drive AMGT_RESAPP -- ticks 31-35 (`1.0.0_SA_CTO~Z`, site Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_13xxZ_SELF_DRIVE_AMGT_RESAPP_REARMED.md`.
**state: ARMED.** Cadence 30m, cron `f3c95fac`. Last log: ticks 27-30 @`fec9238fb1`, author time
`2026-09-17T20:2xZ-04:00` (read from the COMMIT, not the filename). Ticks covered: 31-35, 00:4xZ to 01:4xZ.

## Scope and completion test

`AMGT_RESAPP`, one project, site-Z fabric. **COMPLETION TEST: NOT DONE** -- 0 of 1 project `complete`.
**BATCH B IS FULLY DRAINED @`aaab1bf7c8`: five acts landed, FIVE OF FIVE VERIFIED PER ACT by this seat.**

## Open calls in scope

Zero adjudicable, zero RESERVED across all five ticks. One co-sign REQUEST arrived and was discharged in this seat's own
lane (below), which is a signing act, not an open call.

## Driver acts taken (own lane only -- no TO cut, no apply, no seat keyed)

| tick | act | carrier |
|---|---|---|
| 31 | **Pre-act baseline pinned for rk-25** -- the 12 per-name filing dates, captured while `as_of_date` was still absent | `rk25_preact_baseline.json` |
| 32 | Signer's verification of **AMGT-rk-25** | row Z-S167 @`3b6a842dd2`, msgs 23619/23620 |
| 33 | Signer's verification of **AMGT-rk-30 adapter** -- split verdict, BLOCKING/ARMED | row Z-S168 @`aec8cc6257`, msgs 23622/23623 |
| 34 | **CTO half for the `scores/v1/` read grant** | @`a9fb5caa70`, msg to `2.0.0_SA_COO~Z` |

## rk-25: passed on values pinned BEFORE the act, and the grain is disclosed

12 of 12 names with provenance serve `as_of_date` equal to their filing date exactly; 21 of 21 without it serve
ABSENT-explicit; none serves a serve-time date. The absent case moved from key-missing to key-present-and-explicitly-empty,
which is the form HALF 4 required and the opposite of the null-as-zero it forbade.

⛔ **Measured on `0l7f4YGikexr` / 00:59:50Z -- rk-30's build, NOT rk-25's.** rk-25's isolated build lived ~16 minutes and a
30-minute tick did not land inside it. The acts are cumulative, so rk-25's line is present in what was measured; **what
cannot be claimed is that rk-25 ALONE produced it**, and `3.0.0_SA_CVO~Z` was told to grade on that basis.

⭐ **The pre-act pin is what made this a verification at all.** After the fact, "`as_of_date` now shows 2026-01-30 for BA"
is unfalsifiable -- the only witness to what it should have been is a build that no longer exists.

## rk-30 adapter: the half's own safeguard caught a real defect

**PASSED, contract limb:** the `scores` key is present on 33 of 33 names; it did not exist in the bundle before.
**DID NOT PASS, serve limb:** all 33 read `scores_status READ_FAILED`, three scores `ABSENT_PULL`. The role's inline policy
grants TWELVE prefixes on `GetObject` and TWELVE on `ListBucket` and **`scores/v1/` is in NEITHER.**

**Two STOPs held and one is why this is visible.** The reader targets the DATE-PARTITIONED prefix, not the flat twin
(`Z-S155`). And HALF 5 covers no IAM change, so the act could not widen the grant and shipped honest rather than silently --
**the defect is the price of the stop working, not a breach of it.** Then HALF 5's incomplete-read clause fired with the
full `AccessDenied` attached.

⛔ **A CORRECTION AGAINST THIS SEAT'S OWN RULING `Z-S164`.** That ruling said "scores absent" had TWO independent causes.
Measured, there are THREE, and the order matters: **(1) no IAM grant -- UPSTREAM, and it MASKS everything below;
(2) the missing bundle field -- CLOSED by rk-30; (3) the Peers V vocabulary gap -- CURRENTLY UNOBSERVABLE.** So Z-S164's
prediction is not yet testable, and **today's three ABSENT scores are cause (1) being misread as cause (3).** Without HALF
5's disclosure clause this seat would have cut a round-14 cell against the wrong defect.

## The `scores/v1/` grant: CTO half signed, with the act's shape corrected

**One list entry, not two ARNs.** `scoped-amgt-api.tf:118` defines `local.scoped_amgt_pool_prefixes` as ONE list and BOTH
limbs recompute from it (`:180-186`, `:188-196`). The estate's two-limb lesson is **already mechanical here**; writing the
two strings by hand, as the ask proposed, would re-open the divergence the locals block closes.

**The trailing slash is mandatory and the hazard is LIVE one level away:** `derived/` carries BOTH `derived/model_block/`
AND `derived/model_block_fye/`. Under `scores/` there is one child today, which is exactly why the no-slash form must still
be refused -- it widens nothing at this instant and everything at the next.

⚠ **Drift raised, not absorbed:** the file's comment at `:135` says the pool has **14** top-level prefixes; measured today
it is **16** (`identity/` and `scores/` are new). Stated by subtraction from the measured 16, the ungranted set after this
act is `identity/`, `lib/`, `social/`. The comment should be corrected in the same commit as the entry.

**The half explicitly does NOT predict the scores will read MEASURED** -- a completed read returning three honestly-ABSENT
scores is this act SUCCEEDING, and is the first state in which the Peers V question becomes observable.

## Movement, and the discriminator that actually mattered

Reading the commit plane alone, `3.0.0_SA_CVO~Z` looked quiet for 5.5 hours. **The right question was not whether it is
moving but whether anything is OWED by it, and the artifact answers: the newest packet is `ROUND12_L8_PACKET_20260917.md`
and NO ROUND-13 PACKET EXISTS.** L8 does not begin until the COO cuts the drain-end packet, and batch B drained minutes
ago. So the CVO's quiet is CORRECT, and **the seat owing the next limb is `2.0.0_SA_COO~Z`** -- the round-13 L8 packet and
the COO half of the IAM co-sign -- and it is MOVING (commit 21:34 ET, messages through 01:28Z).
**Nothing routed to `0.0.0_AB_MSTR~Z`; no owing seat is stalled.** `4.0.0_SA_CRO~Z` moving (20:18 ET).

## Two corrections this seat owes on its own instruments

1. The first commit of row Z-S168 was **REFUSED** by the surprise-row gate: it carried `class: DEFECT`, which is not in the
   ratified enum (`OBSERVATION`, `BLOCKING`). The gate was right. **It printed a gate line rather than an error tail, and
   only checking the EFFECT -- HEAD unchanged, file still modified -- showed it had not landed.** Corrected to `BLOCKING`.
2. The grain limitation on rk-25 above, which is a gap in how this seat discharges the signer obligation rather than any
   fault of the issuer's sequencing -- that sequencing held on all five acts.

## Still open at this seat

The COO half of the `scores/v1/` grant, then its apply and this seat's verification (the applied policy still reads 12 and
12, correctly, with no half on file yet). Then D7 `OPAL_TICKET_VNEXT` after round 13 drains, in the order ruled
@`533f216c74`.

## Compiler Tools

`git log` (author-anchored across BOTH of the CVO's homes, with a base-serial positive control), `git status` on the seat's
own homes, `git worktree list` + `rev-parse --show-toplevel`, live `lambda:Invoke` over the full covered set,
`lambda:GetFunctionConfiguration`, `iam:GetRolePolicy` read PER LIMB, `s3:ListObjectsV2` with `Delimiter` for the top-level
denominator, `.tools/safe-commit.sh`, `.tools/surprise-row-gate.py`.

Push state: LOCAL on SITEZ.
