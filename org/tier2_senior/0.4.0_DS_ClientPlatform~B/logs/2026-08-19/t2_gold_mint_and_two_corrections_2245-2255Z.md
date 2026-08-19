# T2 gold MINTED + verified, and two corrections landed on me (2245-2255Z)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~B` | **Window:** 2245Z -> 2255Z
**Commits:** `b5fb0e7f6f` (mint + assertion + both records). Unpushed.

---

## Summary

Both grounds for the T2-1 mint withhold were discharged within the hour, so I minted rather than
waiting for a second word: DS base minted and value-verified WP-1's silver partition, and COO's
conditional (*"hold the mint ... yours unblocks when theirs lands"*) was met. Two corrections landed
on my work in the same window and both improved it.

## The mint

Producer re-run against the **LIVE minted silver** with no `--silver` override, so the artifact's
declared upstream and its actual upstream are the same object.

| key | bytes | etag |
|---|---:|---|
| `gold/advi/dimensions/dim_portfolio_group/date=2026-08-18/data.parquet` | 10,411 | `b26d6cce17f530ad` |
| `gold/advi/dimensions/bridge_group_account/date=2026-08-18/data.parquet` | 197,188 | `d937238efba43e2d` |

Verified on the **served artifacts read back from S3**, never on the producer's rc=0: dim 201x8,
bridge 29,907x10, Travis served book $392,556,451.10 / 318 accounts / advisor-book (ties expected),
`is_primary` non-null 0 of 29,907, bridge money columns `[]`, manifest carrying basis + ruling +
`additive=false` + `ABSENT-UPSTREAM`. **Negative control:** `date=1999-01-01` raises
`FileNotFoundError`, so the successful read discriminates.

**NEVER#3 held and re-checked AFTER the write:** `platinum/advi/49financial/` still 0 keys. I
re-checked post-mint rather than relying on the pre-mint reading, because "I only wrote gold" is
exactly the kind of claim that should not rest on intent.

## Two corrections, both landing on me

1. **DS base: supervision explains 19 of 24, not all 24.** I had told them the sleeve term was "the
   entire explanation" of their residual. It is not -- the other 5 keys are the known dual-fee
   account `z0813542821` (ruled in the estate since 2026-07-14). Complete grain statement is **six**
   terms with 0 unexplained. **I generalised from the three accounts I had chased to their whole
   residual without re-running their measurement.** The finding was real; the scope claim was not,
   and the scope claim is the half that travels -- "fully explained" CLOSES a question, and closing
   one wrongly is worse than leaving it open.

2. **DS base: my book key is not unique, so SUM would double-count.** I measured their specimen
   rather than reasoning from my code: `z0813542821` carries 2 rows per key in each of 5 groups with
   market value CONSTANT; rows surviving dedup = 1; group `Neil Tjon-Hing` books $22,479,576.71 on
   **both** tools. Right by construction, now **pinned** by `assert_book_key_collapsible()` so a
   future switch to SUM fails loud. Their keeper distinction: **"constant within key" and "safe to
   sum" are different properties, and this key satisfies only the first.**

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `.tools/commit-gate.sh` | producer after the upload wiring + assertion | PASS -- clean |
| `.tools/proof-of-spec-check.py` | T2 instance after the mint update | PASS -- VALID rc=0, 5/5 |
| live S3 read-back (`pandas`/`boto3`) | both minted keys + manifests + a nonexistent partition | PASS -- values tie, negative control raises |
| `aws s3 list-objects-v2` | `platinum/advi/49financial/` post-mint | PASS -- KeyCount 0, NEVER#3 intact |

**What worked:** running the producer against the live minted upstream instead of the local copy --
that is what makes "declared upstream == actual upstream" a fact rather than a claim. **What
failed:** nothing. **Gap found:** none new this window.

## Blockers

**None.** T2-3 remains FAIL pending BD dim 436 -- CTO has routed it to COO as a template-390224
amendment with an Andrew-word gate on the vendor-config change, and explicitly said *"nothing for
you to do."*

## Current State

- T2 gold LIVE at `s3://opal-data-49financial/gold/advi/dimensions/{dim_portfolio_group,bridge_group_account}/date=2026-08-18/`.
- `platinum/advi/49financial/` = 0 keys. Serving untouched, P4 through CTO.
- T1-ORACLE and T2-DIMS both delivered; proofs VALID rc=0; T2 at 4/5 with only the dim-436 FAIL open.
- CTO banked the supervision finding as **ADDENDUM A6** in the parity pre-registration @`c7bfcb2917`,
  and the mutant-vintage lesson into their next protocol pass.

## Next Steps

1. [`2.0.0_SA_COO`] Two open, both non-blocking and both mine to wait on: the AE publisher
   invocation contract (tonight or behind WP-5), and whether to backfill other dates (DS base offers
   daily bronze back through 2026-08-03, so it is cheap now both legs are wired).
2. [`4.0.0_SA_CRO~A`] The qt6 group-grain re-run -- T1's L1 authority leg, still the only thing
   between T1-1 and a fully-measured verdict.
3. [`0.4.0_DS_ClientPlatform~B`] On dim 436 landing: re-run the producer; `is_primary` populates and
   T2-3 closes with no further build.
