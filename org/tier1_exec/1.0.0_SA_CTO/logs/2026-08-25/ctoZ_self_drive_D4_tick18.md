# /self-drive D4 -- ticks 17-18 log (2026-08-25 01:16Z - 01:38Z) -- state: ARMED

**archetype:** COORDINATE · **secondary:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick16.md`.
**This window is a single question -- the money-market classification -- answered wrongly FOUR TIMES BY THIS SEAT and correctly once by `0.4.0_DS_ClientPlatform~Z`.**

## SCOPE + COMPLETION

```
D4 -> 2 project(s)   NOT DONE -- 0 of 2.  REACHABLE 2 / UNREACHABLE 0.
claim scan 324 JSONs · 1 of 9 live directives · 0 ahead of origin/SITEZ · 0 open calls at Andrew
```

## ANDREW-DIRECT THIS WINDOW

**~01:21Z, VERBATIM: *"Just fix it now and once its fixed lets rerun the pulls and lock this in."***
Authorization to fix AND re-run. ⚠ **Constrained only by the clock: at 01:21Z local was still MONDAY,
so an L1 re-run then would land under `bbg/2026-08-21/` AGAIN and OVERWRITE the 170-row artifact we
depend on. Ruled: DO NOT re-run L1 before 04:00Z.**

## ⛔ MY FOUR WRONG FRAMINGS OF ONE QUESTION, EACH CAUGHT BY A DIFFERENT SEAT

```
1. "add mmkt to CASH_NAME_MARKERS"   -> moves SALXX into `Cash`, the bucket Andrew REJECTED for its
                                        sibling by name.            caught: 0.4.0_DS_ClientPlatform~Z
2. "no GICS => cash"                 -> books ICT (a Philippine PORT OPERATOR) and MER (an ELECTRIC
                                        UTILITY) as cash: 2.69% of IDVZ, THREE TIMES the error it was
                                        ruled to fix.               caught: 3.0.0_SA_CVO~Z
3. "route both to Fixed Income"      -> that destination DOES NOT EXIST in the producer vocabulary
                                        (`GICS_SECTORS + Cash` only).      caught by my own read
4. "FXFXX stops being Cash /
    is_cash=True rows stay Cash"     -> THE SAME ROWS. FXFXX is 2 of the 4.  caught: 2.0.0_SA_COO~Z
```
⛔ **AND THE PATTERN IN MINE IS DIAGNOSABLE: I reached for the NEAREST AVAILABLE LEVER each time --
a string, a structural field, a routing change, a two-clause spec -- instead of asking why the
PREVIOUS lever had failed.** `0.4.0_DS_ClientPlatform~Z` asked that question and answered it in one
message.

## ⭐ THE CORRECT DIAGNOSIS -- `0.4.0_DS_ClientPlatform~Z`, msg 6678 @01:30:21Z

```
INTENT A  etf_daily_pull.py:97        "is this a line we can SKIP PULLING?"     FXFXX True  = CORRECT
INTENT B  etf_positioning_gold.py:517 "what ASSET CLASS does this RENDER as?"   FXFXX True  = WRONG
```
> *"No single value of `is_cash` can be right for FXFXX. The ruling is not confused -- the FIELD is
> overloaded, and the ruling is the first thing to ask it both questions at once."*
**RULE 24(iii) AT FIELD LEVEL** -- an axis serving one intent, applied all night to VALUE ENUMS and
never to a FIELD. **It explains all four of my failures at once: I was hunting the right VALUE for a
field that cannot express the answer.**

## ✅ THE RATIFIED DESIGN (theirs, published BEFORE typing)

```
INTENT A  is_cash UNCHANGED -- FXFXX stays True, :97 untouched, the HELD FILE stays held
INTENT B  derived separately at gold:
            is_cash=True + SENTINEL identifier      -> Cash / Cash & Cash Equivalents
            is_cash=True + REAL security identifier -> Fixed Income / Ultra Short Duration
```
Signal **already in silver** (FXFXX cusip `31846V328`, check-digit-verified; `Cash&Other` a literal
sentinel in CONV-2's `_VENDOR_ID_SENTINELS`). **No new field, no pull change, the circularity BYPASSED
rather than fought, and the values ADOPTED from the ratified consumer** (`0.4.0_DE_ClientPlatform~Z`:
`Fixed Income`/`Ultra Short Duration` already exist downstream, full chain rendered).
**MY ONE SPEC CALL: the DECLARED SENTINEL SET, not a CUSIP-shape test** -- their own CONV-1 principle
(*declare, do not infer*), and **shape-inference is the exact class that failed four times, all mine.**
Failure direction checked: **declared fails LOUD, inferred fails QUIET.**

## OTHER FINDINGS THIS WINDOW

- **The circularity** (`0.4.0_DS_ClientPlatform~Z`): `:97-98` excludes `is_cash=True` from the pull,
  so **FXFXX is never queried and CANNOT be reclassified by any Bloomberg signal.** *"Its
  classification determines the pull that would determine its classification."* Real, and routed
  around rather than fought.
- **`HB_OAS_EFF_DURTN = 0.3876` on SALXX** -- a fixed-income analytic, already in the pull, populated
  on 1 of 170. A candidate for the intent-B path on UNFLAGGED rows; **qualified against the 169 rows
  that LACK it, which is the check I failed on framing 2.**

## ⛔ AND A REPEAT THAT IS WORSE THAN A FIRST OFFENCE

**I made the multi-recipient "you" error a SECOND time, ninety minutes after correcting it at full
reach with the rule quoted.** Subject *"YOU HAVE THE ACTUAL DIAGNOSIS"* to six seats; plus an
**IMPOSSIBLE SERIAL, `0.4.0_SA_CVO~Z`** -- DS~Z's tier fused to CVO~Z's role.
⭐ **`3.0.0_SA_CVO~Z` declined the credit, having censused 821 messages first** -- *"'I don't think I
said that' is not evidence"* -- and observed that **the impossible serial IS the fingerprint of the
fusion, machine-detectable where the ambiguous "you" is not.**
**Second refusal-of-credit tonight; both times the record is right only because the recipient refused
it.** **Gate candidate routed: a serial that does not resolve should be REFUSED AT SEND** -- the
recipient field is validated, body serials are not.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| comp-find + sed | `CASH_NAME_MARKERS`, `classify()`, `SUB_ASSET_CLASS_VOCAB`, the call site | the vocabulary has NO Fixed Income; the marker list misses MMKT |
| python (executed) | the marker match on the real issuer string | MATCHES = NONE -> SALXX -> Equity, CONFIRMED |
| aws + pandas | SALXX in the 170-row characteristics | `GICS_SECTOR_NAME = nan` |
| directives-check / to-check | scope + completion | NOT DONE 0 of 2 |

## Blockers

None at this seat. **Zero cards at Andrew.** The design is `0.4.0_DS_ClientPlatform~Z`'s and building.
**I have stepped back from proposing the implementation and said so at full reach** -- ratify,
sequence and report only. **04:00Z fire-anyway bound stands** (2.4h out at time of writing).
