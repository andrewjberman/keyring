# ANDREW-DIRECT 2026-08-25 ~07:3xZ — FIX THE TWO ETF DEFECTS, **THIS AND ONLY THIS**

**Channel:** direct to `0.0.0_AB_MSTR~Z` at the site-Z MSTR terminal
**Recorded by:** `0.0.0_AB_MSTR~Z` (addressed seat), **BEFORE spawning** — the 05:23Z lesson applied
**Push state:** landed LOCAL, rides integration. **This file travels IN THE SPAWN BRIEF**, because a
fresh seat cannot read a commit that has not been pushed.

---

## 1. VERBATIM — HIS QUESTION, THEN HIS INSTRUCTION

> "so i notice that this fabric never completed the "Asset Sub-Categories" for the ETFs, is that a
> data lack or a frontend mapping issue? Furthermore, the SALXX state street money market entry that
> was adjusted in the etf-classification table didnt seem to take, is that a missing terraform apply
> or something or what?"

> "ok i need all of that fixed, bring your fabric back online with the express instruction that they
> are to fix this and only this, verify visually that it is fixed (and confirm pipelines are
> scheduled/robust), commit, push / prod-deploy, and do all necessary logging."

⛔ **"THIS AND ONLY THIS" IS A SCOPE FENCE AND IT IS THE LOAD-BEARING HALF OF THE INSTRUCTION.**
Two defects. Not a third. **No opportunistic cleanup, no adjacent refactor, no new instruments.**
A seat that finds something else FILES it and keeps going — it does not fix it.

## 2. DEFECT A — "ASSET SUB-CATEGORIES" IS A FRONTEND MAPPING ISSUE, NOT A DATA LACK

**ANSWERED. Do not re-derive this.** Measured at `0.0.0_AB_MSTR~Z` before the spawn:

```
portal/src/pages/Positioning/panels/PositioningSummary.tsx
  :358   // Get Asset Sub-Categories from attribution data
  :361   if (attributionData?.portfolios) {          <- the WHOLE panel is gated on this
  :369   const holdings = portfolio.qtd?.holdings || portfolio.ytd?.holdings || []
  :554   // Attribution is a MODELS-only feed (it is keyed by model code and has no ETF
  :555   // counterpart). Disabled rather than fetched-and-ignored in ETF mode, so the
  :556   // Asset Sub-Categories rows simply do not appear instead of appearing empty.
  :562   enabled: caps.attribution                   <- OFF in ETF mode
  :489   if (segmentRows.length === 0) segmentRows.push({ label: '—', values: naValues })
```

>> **THE DATA IS PRESENT AND CORRECT AND THE PANEL READS A DIFFERENT SOURCE.** The served ETF
artifact carries `sub_asset_class` on EVERY holding — 13 values measured on the live bytes:
Information Technology 35 · Financials 31 · Health Care 23 · Industrials 21 · Consumer Staples 16 ·
Communication Services 15 · Consumer Discretionary 14 · Utilities 10 · Energy 9 ·
**Ultra Short Duration 4** · Materials 4 · **Cash & Cash Equivalents 2** · null 3 (ICT/MER/2602335D).
The adapter already passes it through at `etfAdapter.ts:81`. <<

⭐ **IT IS NOT A BUG. It is a DELIBERATE DECISION that predates the ETF path** — the comment says so
in its own words, and "disabled rather than fetched-and-ignored" was the RIGHT call when no ETF
counterpart existed. **It became a defect when the ETF path started carrying the data, without a
line of it changing.** That is the SEVENTH instance of the night's class.

**THE FIX SHAPE (DE~Z's call, not prescribed here):** in ETF mode compute the sub-category rows from
`positioningData.current_holdings[code].holdings[]` — `sub_asset_class` x `weight` — the same source
the Holdings table already renders. **Do not enable the attribution fetch for ETFs; there is no ETF
attribution feed to fetch.** ⚠ **The `'—'` placeholder at :489 must stop firing for ETFs, and must
still fire where it legitimately should.**

## 3. DEFECT B — SALXX: **TWO INDEPENDENT REASONS, AND NEITHER IS A TERRAFORM APPLY**

**His hypothesis was "missing terraform apply." It is not. Terraform manages the TABLE; it never
manages an ITEM.** Measured with controls both ways:

```
aws dynamodb get-item --table-name etf-classifications --key '{"ticker":{"S":"SALXX"}}'
   -> EMPTY. THERE IS NO SALXX ROW.
positive control  QQQ            -> present   (so the table and the probe work)
negative control  ZZZNOSUCH9999  -> None      (so the probe discriminates)
```
**REASON 1: the row does not exist.** Whatever adjustment was made did not land in this table.

```
grep -i "dynamodb|etf_classification|Table(" data/etfs/scripts/gold/etf_positioning_gold.py -> ZERO
etf_positioning_gold.py:822
   "name": str(r.get("security_name") or (hc["NAME"] if hc is not None else "")) or None
```
**REASON 2: THE ETF POSITIONING PRODUCER NEVER READS THAT TABLE.** The displayed name is the
ISSUER'S OWN STRING from the silver holdings row, with the Bloomberg characteristics `NAME` as
fallback. **So even a correct row would not have taken.**

⛔ **FOUR REMEDIES WERE PROPOSED AND FALSIFIED TONIGHT — DO NOT RE-TRY ANY OF THEM:**
```
1  edit the bd-securities row        NO EFFECT -- producer never reads bd-securities either
2  wire producer -> bd-securities    142 of 150 names WORSE, 0 better (that table stores RAW
                                     vendor strings: "APPLE INC COM", "MICROSOFT CORP COM")
3  run seed-etf-classifications.py   :62 name = ETF_NAME_OVERRIDES.get(ticker, ticker) and SALXX
                                     is ABSENT from the 115-entry dict -> writes the literal
                                     "SALXX", STRICTLY WORSE than today, AND IT LOOKS LIKE IT WORKED
4  title-case the raw string         a FOURTH failure mode (CVO: the all-caps set is 7, not 6, and
                                     it is NOT homogeneous)
```
>> **EVERY CANDIDATE REMEDY CHANGES THE NAME, SO EVERY ONE PRODUCES THE APPEARANCE OF SUCCESS.
>> That is why this needs a rendered check and not a "done".** <<

**HIS TARGET STRING IS A RULING AND IS NOT IN QUESTION: `State Street U.S. Government MMKT`.**
**THE ARCHITECTURAL HOME (CTO~Z to confirm, Rule 17b): display naming is SERVING-tier work.** A
vendor-string -> display-name map belongs at the platinum publisher / producer serving step — NOT in
`bd-securities`, NOT in gold business logic. It must generalise: SALXX will not be the last holding
whose issuer string is unreadable. **FXFXX is the same class and should be handled with it.**

## 4. HIS THIRD AND FOURTH ASKS — NOT OPTIONAL, AND NOT THE SAME THING

- **"verify visually that it is fixed"** — **A RENDER, NOT A DIFF, NOT A GREP, NOT A TYPECHECK.**
  Tonight a bundle-content check with a passing positive control still could not answer the render
  question. **Somebody opens the page and looks at the panel and the SALXX row.**
- **"confirm pipelines are scheduled/robust"** — CLAUDE.md's ad-hoc/scheduled rule: **a pipeline
  whose only trigger is another pipeline's success HAS NO SCHEDULE AND IS A DEFECT.** ⚠ Known and
  in scope to CONFIRM (not to re-litigate): the 11:00Z L1 Bloomberg pull is
  `OPAL_BBGTML_daily_pull`, **a LOCAL WINDOWS TASK ON THIS BOX**, while the 13:00Z gold producer is
  `cron(0 13)` in AWS. **EventBridge has ZERO rules at hour 11.** If this workstation sleeps, the
  producer's own guard SKIPS the day and serves stale — green run, no error.
- **"commit, push / prod-deploy, and all necessary logging"** — full chain. LD-0367: lanes commit,
  **MSTR~Z pushes**. Report push state as "landed LOCAL @hash, rides integration" or
  "on origin/<branch> @hash (ls-remote read)" — **never bare "landed".**

## 5. STANDING CONSTRAINTS THAT DID NOT GO AWAY

**ZERO crons at launch, every serial** · **NEVER#5: no new gates** · **NEVER#6: a begun deploy
finishes in-session or rolls back loud** · **Rule 19: portal main tree stays on DEV, promote in an
ephemeral worktree** · **Rule 26: the apply runs on the device that owns the work** ·
**vendor egress needs Andrew's per-use word — none is needed here, this is repo + S3 + DynamoDB** ·
**`comp-closure` does NOT go on the D4 directives item until Andrew smokes it himself.**

⚠ **HOUSEKEEPING FOUND WHILE MEASURING, FILED NOT FIXED (scope fence):** two leftover promote
worktree DIRECTORIES on disk — `.runtmp/portal-promote-20260820T183300Z/` (five days old) and
`.runtmp/portal-promote-20260825T054423Z/`. `git worktree list` shows 1 registration, so the
registrations were pruned correctly and **the directories persist**. **NOT part of this fix.**
