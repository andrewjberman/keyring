# DEPLOY LEDGER — ETFS_INGEST.TO-9-DS: add `GICS_INDUSTRY_GROUP` (the 4-digit CODE) to the daily pull's `CHAR` list

**STATUS: CLOSED — COMPLETE** at 2026-08-28T17:51Z. Applied in full in-session; the source rung is
verified and the SERVED rung is filed OPEN and event-gated (see CLOSE CRITERIA 4). Opened at start per
CLAUDE.md NEVER#6 / NEVER#2. **Nothing half-landed.**

⛔ **ON SITE Z THIS EDIT *IS* THE DEPLOY.** `integrations/bloomberg/READ_HERE.md` §3: the scheduled
task runs the WORKING TREE, so the change is live the moment the file touches disk; the commit only
fixes the record. That is why this ledger opens BEFORE the edit, not after it.

| field | value |
|---|---|
| opened | 2026-08-28T17:50Z |
| closed | 2026-08-28T17:51Z |
| commit | `8d04433492` -- commit-gate CLEAN (1 of 1 file checked; a real gate, the file is `.py`) |
| lane override | `GIT_COMMIT_AUTHOR_OVERRIDE=ANY_EXEC_OR_AE`, SINGULAR, grounds in the commit body. `integrations/**` is `ANY_EXEC_OR_AE`; this seat is DS. Authorized by `2.0.0_SA_COO~Z` 13608 s2, which named this route and directed it NOT be handed to an AE lane (Rule 27: `0.7.0_AE_CloudOps~Z` holds `D1_CATVIEWS`) |
| push state | **LOCAL @`8d04433492`** -- `git ls-remote origin SITEZ` = `6f7aac9c13`, read 17:51:49Z. Consistent with the PUSH HOLD `0.0.0_AB_MSTR~Z` declared in 13525 s6 |
| in-history | `git merge-base --is-ancestor 8d04433492 HEAD` rc=0. HEAD had advanced to `9c4b6e3ed4` (another seat's `D1_CATVIEWS` commit on the shared tree); the edit is intact |
| seat | `0.4.0_DS_ClientPlatform~Q` |
| TO | `ETFS_INGEST.TO-9-DS.industry-group-truncation-fix` |
| issuer | `2.0.0_SA_COO~Z` |
| authority | **`2.0.0_SA_COO~Z` msg 13608 §2(a), CUT TAKEN** — adopting `1.0.0_SA_CTO~Z` 13578/13585/13606. Upstream sovereign word: Andrew-direct ~17:33Z (ETFClassifier as the centralized beautification source, recorded @`dc60a9dfaa`) |
| file | `integrations/bloomberg/pipeline/etf_daily_pull.py` |
| change | `CHAR` list: **+1 mnemonic**, `GICS_INDUSTRY_GROUP` |
| vendor cost | **ZERO.** One more field on a `ReferenceDataRequest` that already fires daily — the pull's own phrase at `:232` for the identical act. **Does NOT consume and is NOT covered by the spent per-use grant.** |
| rollback | revert the single list entry; the field is additive and no consumer requires it |

## WHY THIS FIELD — IT IS THE ONLY LOSSLESS CARRIER THE VENDOR HAS

The granted Bloomberg call (SPENT, recorded @`4b8dc359ed`) established that **the 30-char cap is a
property of the GICS `*_NAME` FAMILY**, not of the one field we pull: 15 distinct values at exactly
30 across `GICS_INDUSTRY_GROUP_NAME`, `GICS_INDUSTRY_NAME` and `GICS_SUB_INDUSTRY_NAME`, **ZERO above
30**. `GICS_INDUSTRY_GROUP` returns the **4-digit code**, and a number cannot truncate.

**CONTROL that the code is the GICS hierarchy and not an arbitrary vendor id:**
`group//100 == sector` AND `industry//100 == group` AND `sub_industry//100 == industry`,
**11 of 11 securities, 0 mismatch.**

## SAFETY — WHY ADDING A COLUMN CANNOT BREAK A CONSUMER

- `char` becomes a DataFrame column and lands in `bbg/{date}/characteristics.csv` via `put(...)` at
  `:330`. **Additive.**
- The gold reader consumes by NAME, never by position or count:
  `etf_positioning_gold.py:1134` `GICS_INDUSTRY_GROUP_FIELD in chars.columns`, `:1031` keyed lookup.
- No `usecols`, no column-count assertion, no positional read found on the characteristics frame.
- ⚠ **NOT CLAIMED:** that every downstream reader estate-wide was censused. The claim is scoped to
  the ETFS gold/publisher path that consumes this artifact.

## WHAT THIS DOES **NOT** DO — STATED SO THE ENTRY CANNOT BE MISREAD AS THE FIX

⛔ **THIS DOES NOT REPAIR ANY SERVED VALUE.** It lands an authoritative KEY. The display strings for
the truncated labels remain outstanding and are a **sovereign question held by `2.0.0_SA_COO~Z`**
(msg 13613 — card held pending sizing; sizing delivered by this seat in msg 13616).

**Residue as measured by this seat on the served artifact (`generated_at 2026-08-28T13:01:22Z`):**
```
  23 distinct observed values
  15 PROVABLY COMPLETE   (len <= 28 -- cannot be a 30-char truncation artifact without
                          two consecutive spaces inside a GICS name)
   8 INDETERMINATE       (len 29-30 -- NOT settleable without the vocabulary)
     63 of 180 populated rows (35.0%) carry an indeterminate value
```
⚠ **`1.0.0_SA_CTO~Z` 13620's structural point rides this entry:** the values we can source
authoritatively are exactly the ones that were never broken, so a decode table seeded from them
would map complete names to themselves and **fix nothing**. The code lands the half that is
solvable without a sovereign word; it does not pretend to be the other half.

## CLOSE CRITERIA

1. `GICS_INDUSTRY_GROUP` present in `CHAR`, committed.
2. `py_compile` / commit-gate clean on the edited file.
3. Ledger closed with the commit hash and measured push state.
4. ⚠ **Landing in the CSV is EVENT-GATED on the next scheduled pull and is NOT part of this closure**
   — an ad-hoc run is not production evidence (CLAUDE.md). The served-artifact rung stays OPEN.

## RESULT — WHAT IS VERIFIED, AT WHICH RUNG

```
  SOURCE   VERIFIED. CHAR now carries 14 mnemonics; GICS_INDUSTRY_GROUP present AND
           GICS_INDUSTRY_GROUP_NAME retained (the code is added ALONGSIDE the name,
           it does not replace it). Diff: 13 insertions, 0 deletions, no CRLF churn.
           py_compile rc=0. commit-gate: all checks passed, 1 of 1 file.
  DEPLOYED VERIFIED BY CONSTRUCTION on site Z -- the scheduled task runs the working
           tree, so the edit WAS the deploy. Not a separate act, and not a claim that
           anything has yet RUN.
  SERVED   *** OPEN. EVENT-GATED on the next SCHEDULED pull. ***
           No ad-hoc run was fired: an ad-hoc artifact is never production evidence,
           and firing one would destroy the discriminator the scheduled run exists to
           produce. NOTHING here claims the code has landed in characteristics.csv.
```

⛔ **THIS ENTRY CLOSES THE CAPTURE OF AN AUTHORITATIVE KEY. IT CLOSES NO ACCEPTANCE CRITERION OF
`TO-9-DS`.** AC1 (complete served values) and AC2 (basis carries its claim) are untouched and
remain blocked on the sovereign question `2.0.0_SA_COO~Z` holds. AC3 is served-plane and gated on
a scheduled fire. **A deploy that lands a key is not a fix that repairs a value**, and the
distinction is the whole reason this section exists.

---
**Author:** `0.4.0_DS_ClientPlatform~Q`
