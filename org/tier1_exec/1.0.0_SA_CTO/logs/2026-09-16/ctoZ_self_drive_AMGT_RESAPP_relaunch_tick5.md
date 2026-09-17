# `/self-drive AMGT_RESAPP` -- relaunch tick 5, the rk-2 regression ruling, amendment 8 validated (`1.0.0_SA_CTO~Z`, 2026-09-16 15:39Z-16:0xZ)

**archetype:** VALIDATE · **state:** `ARMED` · **cadence:** 30m at `17,47` · **job (then):** `884c0211` · **ticks covered:** 5 (+ the
escalation answered between ticks 4 and 5). Authority: `org/XXX.md` Step 1b-F row for `1.0.0_SA_CTO~Z`; this lane adjudicates.

## Completion test

**NOT DONE** -- `status: active`, `dep_stage: EXECUTING`, **6 of 16** orders terminal (rk-1, rk-3, rk-4, rk-9, rk-10, rk-11), 0
`COMPLETION_*`. Sequence: UNPLACED, 0 flags; capacity 1 live COO lane. HEAD `aa97d2ea9f`; PRD v0.10 ADMITTED, both halves current;
round-12 slug ABSENT (correct); MERGE_HEAD absent; porcelain under the project 0; 1 unmerged worker branch = `wk-amgt_resapp-12-25`
@`af7cdb40d6` (rk-5, `~25`, LIVE work: the new `lib/research/scores/` package), not an orphan.

## The escalation (msg 23462, 15:39Z) and the ruling (co-sign AMENDMENT 2 @`aa97d2ea9f`, broadcast 23463-23465)

rk-2's adapter redeploy at **15:19:34Z** (worker `~24`; `apply-rk2.out`: two resources modified, `aws_iam_role_policy.scoped_amgt_api_grants`
and `module.scoped_amgt_api.aws_lambda_function.this` -- exactly the two keys the co-sign names) **regressed `/thesis` and `/overlay`
200 -> 500** on `FileNotFoundError` at import: `lib/research/rules/peer.py:13-18` and `rules/figure.py:44-50` read a repo-relative
`~8` deliverables artifact the zip does not carry. The chatter-axis schedule line in the apply output is an OUTPUT, not a change.

**RULED:** (1) roll back first (the versioned archive `5M.rKCFS...` = sha `9ubWPnhz...`, verified before use and read back after; both
IAM limbs to nine; a change-management entry opened and closed, recording that the 15:19Z act ran with none) on worker `~24`'s
report **or at 16:05Z, whichever first**; fix forward second. (2) The fix is PACKAGING, not a pool read: the two distribution files
are build inputs; module-relative lazy reads; the JSON committed under `lib/research/rules/data/` with provenance; rk-2's grant
widened by `lib/research/rules/` and `org/critical_paths/change_management/`; the whole import closure censused for the class.
(3) rk-2 re-cut with **AC7 non-regression** (pre/post route census over the 11-route table, 200 sets equal) and **AC8 packaging**.
(4) S127: the filings re-run is the issuer's if it makes no vendor call, under CARD 2 if it does -- measured before it runs.
(5) S119: closed for this act; the schedule's ENABLED state pre-exists and goes to the L10 as a bounds question.

**The CTO half's own defect, corrected in AMENDMENT 2:** a function-code redeploy's blast radius is EVERY route the function serves
(11); the half named 2 and was silent on 9, two of which regressed. From now on the act's proof is the pre/post route census, and a
redeploy whose census shrinks is rolled back before anything else. COST one census per redeploy; NON-APPLICATION a policy-only or
env-only act, and a one-route function.

## State of the regression at this tick (15:59Z), measured on a second instrument

| read | value |
|---|---|
| `get-function-configuration` | `CodeSha256 Di6/6ju9...`, size 749036, LastModified 15:19:34Z -- **the regressed build, NOT yet rolled back** |
| direct GET `/security/BA_US_Equity/thesis` | **500** (127 B) |
| direct GET `/security/BA_US_Equity/overlay` | **500** (127 B) |
| worker `~24`'s plane | nothing newer than the 15:19:40Z apply output; 3 porcelain paths, no commit since `de77282136` -- 40 min quiet |
| msg 23463 (the ruling) | READ by `2.0.0_SA_COO~Z` 15:48Z |
| `org/critical_paths/change_management/` | no entry for this act yet; `.open_deploys` absent |

The bound is **16:05Z**. The next inbox event or the 16:17Z tick verifies the rollback: `CodeSha256 == 9ubWPnhz...`, both routes 200,
the entry opened and closed, the row filed. ⚠ If the sha still reads `Di6/6ju9` at the 16:17Z tick, the COO has missed the bound and
this seat says so, loud, to `2.0.0_SA_COO~Z` and `0.0.0_AB_MSTR~Z`.

## ISSUER AMENDMENT 8 @`91141aebd2` (15:40Z) VALIDATED on the bytes -- the S124 mechanism applied to the adapter partition

| order | criteria | `cell_refs` present | `<paths>` |
|---|---|---|---|
| rk-6 | 5 (AC4 <- rk-12 AC1, AC5 <- rk-16 AC2) | `AMGT-rk-12` x1, `AMGT-rk-16` x1 | `scoped_amgt.py` yes; a fresh CTO+COO co-sign required before ANY deploy |
| rk-7 | 5 (AC5 <- rk-15 AC1; AC4 <- rk-3 fallback) | `AMGT-rk-15` x1, `AMGT-rk-3` x1 | `scoped_amgt.py` yes |
| rk-15 | 2 | own only | **NARROWED**: `scoped_amgt.py` removed |
| rk-16 | 2 | own only | **NARROWED**: `scoped_amgt.py` removed |

The second-writer observation from S124 is closed: chain A's portal orders no longer carry the adapter file; every adapter
assertion sits on chain B with `cell_refs` to the cell it proves. rk-6 AC4/AC5 read 0 of 0 today (correct pre-state); rk-7 AC5 reads
the deployed `/thesis`, which is 500 until the rollback lands. **Sequence stated:** rk-6 after rk-2 drains; rk-7 after rk-15 drains.
RAVC 4 CLOSE, recorded here; the COO is not messaged again for it (heads-down; the close rides the next carrier).

## Open calls in scope

| call | class | state |
|---|---|---|
| ESCALATION 23462 (rk-2 regression; packaging; S127; S119) | ADJUDICABLE | RULED, AMENDMENT 2 @`aa97d2ea9f`; rollback pending at the COO, bound 16:05Z |
| 23440 · S120 · S124 · S125 | ADJUDICABLE | RULED and APPLIED (amendments 3, 6, 7, 8); closed |
| CARD 1 model-block pull (+ the price pull, one card at the L10) | RESERVED -- vendor budget | at Andrew |
| CARD 2 filings batch (~USD 1.1/filing); S127's re-run if it calls the vendor | RESERVED -- spend | at Andrew |
| CARD 3 portal DEV fast-forward + push (LD-0367/0368) | RESERVED -- shared-branch push | at Andrew via `0.0.0_AB_MSTR~Z`, rec YES now |
| SITEZ push / merge leg (LD-0522) | RESERVED | `0.0.0_AB_MSTR~Z` on his word |

Five adjudicable calls this session, five ruled; the all-reserved tell did not fire.

## Who owes what

`2.0.0_SA_COO~Z`: **the rollback by 16:05Z** (sha verified, both limbs, entry, census, row), then rk-2's re-cut (AC7/AC8, grant
widened) and a fresh `~24` slot; S127's egress measured before any re-run; drains of rk-5; rk-8 on rk-2's landing; the L8 packet.
`3.0.0_SA_CVO~Z`: L8/L9 as completions land; dispositions W25-S1..S5, W26-S4, S115-S127. `0.0.0_AB_MSTR~Z`: CARD 3 and the SITEZ
push at Andrew. This seat: verify the rollback at the next event or tick; the L10 when the slug lands.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `.tools/aws lambda get-function-configuration` | sha `Di6/6ju9`, 15:19:34Z | a SECOND instrument on the COO's regression read; agrees |
| direct GET x2 (boto3 invoke, GET-only) | 500 / 500 | the regression is live at 15:59Z |
| worker apply output parsed (ANSI stripped, python) | 2 resources modified; schedule = output | the discriminator between "changed" and "printed" |
| criteria + `<paths>` re-read (python over `<criterion>` attrs and `<paths>`) | amendment 8 as stated | validated on the bytes |
| `prd-signoff.py status` / `git branch --no-merged HEAD` | ADMITTED / 1 (live rk-5 work) | nothing owed at L4-R; no orphan |

**Gap found:** in the CTO half, by this seat, against itself: a co-sign that counts writers and not routes. Corrected in the
artifact, not just here.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`; none requested.
