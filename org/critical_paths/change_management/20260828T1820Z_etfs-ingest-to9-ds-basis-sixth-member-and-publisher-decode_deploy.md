# DEPLOY LEDGER — ETFS_INGEST.TO-9-DS: the SIXTH `industry_group_basis` member + the publisher decode wiring

**STATUS: OPEN — IN PROGRESS.** Opened at start per CLAUDE.md NEVER#6 / NEVER#2, and per
`2.0.0_SA_COO~Z` msg 13697 s3. Nothing half-landed.

| field | value |
|---|---|
| opened | 2026-08-28T18:20Z |
| closed | — |
| seat | `0.4.0_DS_ClientPlatform~Q` |
| TO | `ETFS_INGEST.TO-9-DS.industry-group-truncation-fix` |
| issuer | `2.0.0_SA_COO~Z` |
| authority | **Andrew-direct ~18:02Z** (infer + hard-code, record @`7d4f4700a6`) + **~18:10Z** ("this is fine by me", @`d96d6165ec`). Enum ruled by `2.0.0_SA_COO~Z` msg **13697**. |
| NEVER#1 co-sign | **COMPLETE** — CTO half msg `13676`, COO half msg `13679`. Radius **59 of 189 rows, 7 labels, display text only**. |
| files | `data/etfs/scripts/gold/etf_positioning_gold.py` (vocab + doc), `data/etfs/scripts/gold/etf_positioning_publisher.py` (wiring), `data/etfs/scripts/gold/test_etf_positioning_industry_group.py` (stale prose) |
| rollback | revert the three edits; the decode module stays inert because nothing else imports it |

⚠ **THIS IS NOT ITSELF A DEPLOY.** Unlike `etf_daily_pull.py` (which the site-Z scheduled task runs
from the WORKING TREE), gold and the publisher run as **Lambdas deployed from a package by
`0.7.0_AE_CloudOps`**. **The source edit changes nothing served until an AE apply AND a scheduled
fire.** The ledger is opened anyway because the change MOVES SERVED OUTPUT once deployed, and the
co-sign that authorises that is recorded here.

## THE ENUM CHANGE — AND THE STRUCTURAL FACT IT INTRODUCES

`inferred-from-truncation` becomes the **sixth** member of `INDUSTRY_GROUP_BASIS_VOCAB`. Ruled by
the TO's issuer at 13697; `RESOLVED` is struck from `TO-9-DS` §4 by that same message. Rule 24
record: `dsQ_ETFS_INGEST_TO9_BASIS_ENUM_RULE24_RECORD_20260828.md` @`362c94ea97`.

⛔ **THE VOCAB NOW SPANS TWO PRODUCERS, AND THAT IS NEW:**
```
  GOLD produces      observed · not-applicable-non-equity · field-not-in-source ·
                     security-not-in-characteristics · absent-from-source        (5)
  PUBLISHER produces inferred-from-truncation                                    (1)
```
**Gold can NEVER emit the sixth member** — the decode runs at the serving tier. So the gold test's
headline *"every declared basis is REACHABLE"* stops being true AT GOLD SCOPE. Its actual assertion
is an explicit four-member set equality and still passes, but **the prose overclaims and is being
corrected in the same change rather than left to read as a silent contradiction.**

## SAFETY

- `:128 by_basis = {b: [] for b in VOCAB}` — a new member adds an empty bucket. Additive.
- `:131` asserts an EXPLICIT four-member set, not a count — unaffected.
- `:146` / `:341` are SUBSET checks (`in VOCAB`) — a wider vocab cannot break them; it is what makes
  the publisher's new value legal.
- **PORTAL CONSUMERS NEED NO CHANGE — MEASURED, not assumed.** `portal-proxy.ts:1039,1207`,
  `etfAdapter.ts:86`, `HoldingsTab.tsx:184,916` all type `industry_group_basis` as an opaque
  `string` and pass it through. **None switches on its value**, so a new member cannot be dropped by
  a stale branch. (13697 s3 asked for consumers to be updated in the same change; measured, there is
  nothing to update on that side, and the seam it was protecting against does not exist here.)

## CLOSE CRITERIA

1. Sixth member declared, in the vocab, documented under all four postulates.
2. Publisher emits it only for values the decode actually CHANGED (basis follows the VALUE).
3. `test_etf_positioning_industry_group.py` passes; stale "five-member" prose corrected.
4. ⚠ **SERVED rung stays OPEN** — event-gated on an AE apply plus a scheduled fire. No ad-hoc run.

---
**Author:** `0.4.0_DS_ClientPlatform~Q`
