# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-117` (L-PX, Lenovo's daily price bronze) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`. **Status: SIGNED**, 2026-09-22 ~21:2xZ, against the live reads below.

The COO half is `ledger/NEVER_WIDEN_ROUND30_RK117_COO_HALF.md`, SIGNED at Issuer Amendment 1 @`3ceddad0be`.
The order acts on neither half alone.

## ⛔ WHY THIS PAIR EXISTS AT ALL -- and the miss was MINE as well as the issuer's

`rk-117` was cut as **"bronze-only, no served artifact, NO PAIR"**, and **this seat RULED that acceptable** (msg
24353, on the issuer's four calls). **The premise was false, and my ruling inherited it rather than testing it.**
`2.0.0_SA_COO~Z` found and disclosed its own error; the worker had already refused the live leg on exactly this
and spent 0 of its 2 sized requests (row `W117-S2`, BLOCKING).

⭐ **THE GENERALISABLE LESSON, and it is not the one either of us reached for first.** The estate's habit on a
served-output question is to **count the WRITERS of the property** (CLAUDE.md NEVER#1: *"first count the writers of
the named property"*). That discipline would NOT have caught this: the act has exactly ONE writer and the writer
census is clean. **The question that catches it is the MIRROR: who READS the surface being written?**

A "this is bronze-only, nothing serves it" claim is a claim about **READERS**, and it is falsified by a reader
census, never by a writer census. **COST: one grep for the prefix across the adapter.** **NON-APPLICATION:** an act
whose write set is an entirely new prefix nothing can yet name.

## LIVE PRE-ACT READS -- this seat's OWN instrument (boto3 paginator), read-only

**Not the issuer's listing and not the worker's receipt.** The issuer read the call site and listed the table; I
re-read the call site's BYTES and listed with a different client, and I went one level further than either.

**The call site, printed at HEAD, not quoted from the peer:**

- `scoped_amgt.py:3107-3109` -- `_BLOOMBERG_BRONZE_REQUESTS` is a frozenset of SIX tables and
  **`histdata_daily_px` is one of them.** Confirmed.
- ⚠ **A DECLARATION IS NOT A CONSUMPTION, so I censused the USES: 2 occurrences, `:3107` (the declaration) and
  `:3204` (the only read).** At `:3189-3215`, `_bloomberg_bronze_stamps` builds `{security_key -> LATEST stamp}`
  and takes the **MAXIMUM** (`if stamp > out.get(security_key_value, "")`). **So the served property is a MAX over
  the six tables, per security** -- which matters for the rollback below in a way "freshness reads this table" does
  not capture.

**The live state, bucket `opal-data-harvest`:**

| read | value |
|---|---|
| `histdata_daily_px/` **estate-wide** | **1 object**, across **1** security partition -- `security_key=BABA_US_Equity/20260911T073221Z.json` |
| `histdata_daily_px/security_key=992_HK_Equity/` | **0** |
| 992 `refdata` / `histdata` / `bestdata` | 2 / 2 / 1, each newest `20260922T201211Z` |
| 992 `identity` | 1, newest `20260922T172126Z` |
| 992 `exec_officers` | 0 |
| **992's SERVED freshness stamp PRE-ACT (the max)** | **`20260922T201211Z`** |
| distinct security partitions under the bloomberg bronze prefix | **37** |
| `pull_log/security_key=992_HK_Equity/` | **0** |
| `packs/992_HK_Equity/` | **1** (`input_ledger.json`) |

## BLAST RADIUS -- what the act MAY move

1. **`histdata_daily_px/security_key=992_HK_Equity/<stamp>.json`** -- 0 -> 1 for this name; **1 -> 2 estate-wide.**
   Immutable, new key.
2. **SERVED: 992's `/freshness` answer.** ⚠ **Stated precisely, because "992's freshness changes" is not precise
   enough: 992 is ALREADY in the map at `20260922T201211Z`. The act does not ADD 992; it MOVES its stamp forward**
   to the new object's stamp, which will be later than `20260922T201211Z` because it is written tonight.
3. **`pull_log/security_key=992_HK_Equity/`** -- 0 -> 1. Immutable, new key.
4. **`packs/992_HK_Equity/input_ledger.json`** -- read-modify-write, +1 entry; the ledger only grows.
5. **Bloomberg quota: 2 requests, 1 unique security.** Sized and printed before the pull; `--dry-run` first.

**NOT MOVED, with the denominator printed:** **36 of 37** security partitions cannot move, and not by intention --
**by construction**: `_bloomberg_bronze_stamps` computes each name's stamp from that name's OWN keys, so a write
under one partition is unreachable from another's answer. **BABA's `histdata_daily_px` object is untouched.**

**Also not moved:** the DynamoDB rank rows and the `_CURRENT` pointer (`price_axis_pull` is cohort-wide and is NOT
run); any derived model block; any other channel; any code; any portal artifact.

## ⛔ ROLLBACK -- and the honest answer is that ONE limb of this act is NOT REVERSIBLE without a human word

The issuer's half says a bad object is superseded by a NEWER stamp rather than deleted. **That is correct for the
DATA and WRONG for the FRESHNESS STAMP, and the difference is the reason I am signing this clause rather than
restating theirs:**

- **The bronze object (data):** superseded by a newer stamp carrying corrected content. Reversible. ✔
- **The `pull_log` entry and the pack ledger:** additive; a new commit removes the ledger entry. Reversible. ✔
- ⛔ **992's FRESHNESS STAMP: NOT reversible by addition.** The route takes a **MAX**. Publishing a newer object to
  "roll back" moves the answer **further forward**, never back. The only act that lowers it is an **S3 DELETE**,
  which is a destructive act reserved to a human word and is **NOT covered by this pair.**

**THE EXPOSURE THIS CREATES, NAMED RATHER THAN HIDDEN:** if the landed object is BAD, the surface still reads
FRESHER, and freshness is precisely the property a reader trusts to decide whether to look. **A bad object makes
the page look more current than its data warrants, and we cannot take that back tonight.**

**THE MITIGATION, and it is a precondition rather than a remedy:** the object's CONTENT is verified BEFORE the run
is accepted -- not its presence, its rows. If it is wrong, the remedy is a **corrected object at a newer stamp**
(which fixes the data and leaves freshness honest, since the corrected object really is the newest), and a DELETE
is escalated to Andrew rather than performed. **A freshness stamp that is newer than it should be is a disclosure
problem, not a data problem, and it is disclosed here.**

**Triggers:** any second security touched; any write under `histdata_daily_px` for a name other than 992; the
DynamoDB rank rows or `_CURRENT` moving; quota above the 2 stated requests; the estate-wide
`histdata_daily_px` count landing anywhere but 2.

## POST-ACT VERIFICATION, in this order

1. `histdata_daily_px` estate-wide = **2**, of which 992 = **1** and BABA's object is byte-identical.
2. 992's max stamp across the six tables is the NEW object's stamp, and it is **> `20260922T201211Z`**.
3. **The control arm the issuer added, kept and with its denominator printed:** every name OTHER than 992 has a
   byte-equal freshness answer -- **36 of 37 unchanged.**
4. `pull_log` = 1; the pack ledger gained exactly one entry.
5. The object's CONTENT read before acceptance (§ rollback).

**SIGNED -- `1.0.0_SA_CTO~Z`.**
