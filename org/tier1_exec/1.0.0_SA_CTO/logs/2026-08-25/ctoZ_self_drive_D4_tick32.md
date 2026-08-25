# /self-drive D4 -- ticks 31-32 log (2026-08-25 05:15Z - 06:15Z) -- state: ARMED

**archetype:** COORDINATE · **secondary:** VALIDATE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick30.md`.
**BOTH ASKS REACHED PRODUCTION THIS WINDOW.** Also: a one-row cosmetic fix produced SIX failed remedies, my own stop over-reached and was corrected by a peer, and a green CI gate turned out to be green by construction.

## SCOPE + COMPLETION

```
D4 -> ETFS_CANON(scoping) · ETFS_POSITIONING(active) · +ETFS_INGEST(claimed, active)
  COMPLETION TEST: NOT DONE -- 0 of 2.  REACHABLE 2 / UNREACHABLE 0.  open TOs 6
  1 of 9 live directives · device SITEZ · 6 ahead of origin/SITEZ · 0 uncommitted in my lane
  open calls: 0 ADJUDICABLE · 2 RESERVED (Pathfinder weekend stamp · the SALXX tolerance question)
```

## ✅ DELIVERED TO PRODUCTION

```
served artifact   126,863 B @ 04:53:51Z   187 rows · 1D-1Q 181 · YTD 179 · 1Y 177 (94.7%)
origin/DEV        063ff4d7  adapter carries { ...h.returns }
origin/PROD       d9a98bcc  SAME -- READ FROM THE REMOTE, not the local tree
tag               portal-v2.1.165 peels to d9a98bcc   (control: 2.1.164 -> the PREVIOUS head)
```
**Verified by three seats independently. Andrew confirmed the render himself: *"We now have full
performance for everything but still missing SALXX YTD and 1Y."***

## ⛔ THE NAMING WORK -- SIX FAILED REMEDIES IN 25 MINUTES

```
1 DE~Z   named bd-securities, the DOWNSTREAM COPY not the SSOT     (self-caught)
2 COO~Z  read-from-classifier -> would ALL-CAPS 142 CORRECT names to fix 6   *** WORSE ***
3 DS~Z   seeder falls back to the ticker -> renders "SALXX"                  *** WORSE ***
4 CVO~Z  the set is 7, not 6
5 CVO~Z  title-case -> `Bp Plc` · `Gsk Plc` · `Mplx Lp`                      *** WORSE ***
6 DS~Z   act 3 does not fix it either
```
⭐ **CVO~Z's finding settles the DESIGN: *"All-caps is not a defect class; it is a rendering CORRECT
for acronym companies and WRONG for word companies, and NO STRING FUNCTION DISTINGUISHES THEM."***
**So the work is SEVEN DECLARED OVERRIDE ENTRIES -- a list, not a mechanism. Andrew supplied the
pattern himself by giving the target string verbatim.**
⛔ **AND DS~Z's near-miss is the keeper: they scanned the live table for placeholders and got
`name == ticker: 0 of 116`. TRUE, and TRUE BY CONSTRUCTION -- 115 overrides over 116 rows, so every
ticker there is already overridden. THE PLACEHOLDER RATE IS ZERO BECAUSE PLACEHOLDERS CANNOT SURVIVE
THERE, not because the seeder does not produce them.** A reassuring number over a population that
excludes the failure by definition.

## ⛔ MY STOP OVER-REACHED AND `2.0.0_SA_COO~Z` CORRECTED ME

I ruled *"nothing ships -- not the seed, not the overrides, not a transform."* **That lumped two risk
classes.** All four page-degrading proposals were **GENERALISING**; a single declared entry carrying
Andrew's verbatim string **cannot degrade a name it does not name**, and the overrides table is the
SANCTIONED pattern with the VUG fix holding since 2026-08-18 as a live control.
>> **MY STOP WOULD HAVE BANNED THE ONE REMEDY WITH A TRACK RECORD.** <<
✅ **Conceded and withdrawn.** ⛔ **What I still hold is ONE NEW question nobody has answered:
`etf-classifications` is 116 HELD-ETF rows and all 7 mis-cased names are COMMON STOCKS or MMFs --
NONE is an ETF. So the act is putting a NON-ETF into an ETF-SCOPED SSOT.** **Domain question,
Rule 24, one line to answer.**

## ⛔ THE PROMOTE'S CI GATE IS GREEN BY CONSTRUCTION

`0.0.0_AB_MSTR~Z` flagged L3 as *"green by the letter"*. **I read the run; nobody had.**
```
d9a98bcc (PROD)  Deploy to Production   SUCCESS   <- the ONLY workflow that fires on a PROD push
063ff4d7 (DEV)   CI - Build & Validate  FAILURE   <- IDENTICAL content, parity 0 bytes
the failure: ONE error, everything else warnings, BUILD job PASSED
   'PerfrpFigure' is defined but never used     (ADVI_PERFRP, laptop fabric)
red since 0c6e61ed 02:25Z -- ~C/~D commits. Site Z merged in at 05:37Z. INHERITED, NOT INTRODUCED.
```
>> **A headSha-SCOPED CI CHECK AT A PROD MERGE STRUCTURALLY CANNOT SEE THE WORKFLOW THAT VALIDATES
THE CODE. The letter of L3 is satisfied either way, and the NEXT failure could be a type error or a
broken build and pass identically.** << **Daylight cell for the deploy protocol, not an ETF item.**
⭐ **Two minutes of reading converted an UNKNOWN into a BENIGN. Those are different states even when
the artifact is identical, and only one of them is a decision.**

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| git ls-remote + git show origin/PROD:path | production content, from the remote | the fix is on PROD |
| git ls-remote --tags (no grep filter) | tag state | **2.1.165 EXISTS -- my earlier grep was wrong** |
| gh run list --json + run view --log-failed | the CI failure | one unused import; build job passed |
| git log at the red/green boundary | attribution | inherited from ~C/~D, not introduced |

## Blockers

**None at this seat. Both asks DELIVERED TO PRODUCTION.** 2 RESERVED at Andrew (Pathfinder stamp;
the SALXX tolerance -- rec: do NOT bend). Held: the non-ETF-in-an-ETF-table domain question.
Daylight and not ours: the ADVI_PERFRP lint error; the PROD-side CI blind spot.
