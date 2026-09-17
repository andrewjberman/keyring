# `/self-drive AMGT_RESAPP` -- ticks 4-5 (`1.0.0_SA_CTO~Z`, 2026-09-16 05:52-06:1xZ)

**archetype:** VALIDATE · **state:** `ARMED` · **job:** `6b00e98e` · **ticks covered:** 4 (quiet) and 5

## Completion test

**NOT DONE** -- `status: active`, **`dep_stage: EXECUTING`**, round 12 issued and draining; 0 of 1 complete.

## ROUND 12 IS ISSUED @`6e4327f77f` -- verified here, not taken from the report

16 orders `rk-1..rk-16`, **all `<status>pending</status>`**; six worker slots `~23..~28` by the `<issued_to>`
census (the authority, never the folder-keyed pending list); `dep_stage` EXECUTING; **0 unmerged branches**.
Six chains, 56 criteria, **one judgment criterion per chain, 6 of 6**.

## Delta: the ONE thing owed by this seat, delivered

**NEVER-WIDEN CTO HALF** for `AMGT-rk-2` -- `ledger/NEVER_WIDEN_ROUND12_MODEL_BLOCK_READ_CTO_HALF.md`
@`4aeaa2bbf6`. AC1's own invocation against it: **blast-radius 2, rollback 7, writer 7 on the CTO half alone**,
so the token bars do not hinge on the COO half matching exactly. `halves` reads 1 until that half lands --
correctly, since AC1 asserts 2 and the cell cannot pass on one.

**Blast radius:** the act writes **nothing to the pool** -- Lambda code, Lambda config, one IAM policy, and the
added prefix is READ-ONLY. Rollback given per key from the live plane at signing: `CodeSha256`
`9ubWPnhz...` at CodeSize `747396`; env restored to exactly two keys with `AMGT_MODEL_BLOCK_ROOT` **ABSENT at
signing, so removing it IS the rollback**; the role's prefix list restored to the nine co-signed at
`@e1c3cf0cb3`, printed in the half.

**Writer census, N printed:** `derived/model_block/` -> **1** (`model_block_pull.py`); `posture/v1/` -> **1**
(`posture/judge.py`); the served response -> **1** (the adapter). Three files carrying write calls were
**discriminated and excluded** -- the helpers take the key as a parameter, so a write call in a file that
mentions a prefix is not a write to that prefix.

## ⛔ THE HAZARD THE CENSUS FOUND

A **second, adjacent store** `derived/model_block_fye/` exists, different writer
(`derive_fye_fixed.py`), and **`derived/model_block` is a string prefix of it**:

```
grant "derived/model_block/"  matches "derived/model_block_fye/"  -> False
glob  "derived/model_block*"  matches "derived/model_block_fye/"  -> True
```

The grant is signed **only in its trailing-slash form**. A glob or slashless form silently widens the act to a
store the half does not cover and **nothing would refuse it** -- policy applies, criteria pass, the adapter
quietly gains read on a derivation store nobody granted. ⭐ **Two stores sharing a stem are one typo apart**, and
this is the shape a writer census catches while a per-member check cannot: both stores are individually fine and
the defect lives in the string relationship between them.

## Tick 4 -- quiet, and the reading that would have caused a wrong act

The COO showed **19 minutes of commit silence, a stale `BLOCKED` summary, and zero orders in the tree**. Every
consumption-side instrument said stalled. **Plane 3 said otherwise:** 16 untracked task orders sat in its
worktree, one per cell. It was mid-issuance. **No nudge sent** -- nudging there would have interrupted a seat
doing exactly the right thing. Four planes read before concluding, as the skill requires.

## Calls

**ADJUDICABLE: 0.** **RESERVED: 2**, unchanged since tick 1 and still the only thing deciding whether this is a
product -- the model-block pull over the 33 keyed names, and the filings batch over 33 rather than 89.

## Peer work recorded

`2.0.0_SA_COO~Z` introduced a `dep_stage` mislabel, **its own gate refused the issuance on it**, and it
**corrected rather than took the available audited override** -- which would have bought a green with a footnote
and left an untrue value in the register. Its general statement is the keeper: **a register value chosen to make
the record read more honestly can make a gate grade the wrong question**, because `dep_stage` is consumed by
machinery and not only by readers. It also failed its own one-judgment-per-chain contract at 1 of 6 and **added
five rather than relaxing the contract** -- the opposite of what round 11 taught.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `get_function_configuration` | pre-act state | the rollback anchor, read live at signing rather than carried |
| `git grep` over `infra/aws/terraform/harvest/` | nine prefixes printed | **comp-iam is blind here** -- 3 ops, all UNRESOLVED-RESOURCE, no S3 row, own banner says FLOOR |
| source read + write-call discrimination | 7 files -> **1 writer** | a mention is not a write; the exclusion is the measurement |
| AC1's own invocation | 2 / 7 / 7 | the criterion run against the artifact before claiming it met |
| `<issued_to>` parse | 16 orders, 6 slots | never `get_agent_status`'s folder-keyed list |

**Gap found:** none in the tools. The finding came from **not trusting one that declares itself a floor**.

## Owed next

**Nothing by this seat.** The COO half, then wave-1 worker drains, then L8/L9 at drain-end. Next tick `13,43`.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`; none requested.
