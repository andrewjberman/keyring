# LGIC_ENFORCE FWD-5 -- grade from LGIC_BLANKFIX FWD-9's run (1.0.0_SA_CTO, 2026-10-08 ~16:5xZ)

**Bound by:** `org/missions/D14/LGIC/LGIC_BLANKFIX/prd/LGIC_BLANKFIX_PRD.md` PROVENANCE ("when FWD-9 is REALIZED,
`1.0.0_SA_CTO` grades LGIC_ENFORCE's FWD-5 from the same run"). FWD-9 was graded REALIZED in
`org/missions/D14/LGIC/LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round5.md`.
**The run graded:** `3.0.0_SA_CVO`'s, at HEAD `3c07973c5c`, 2026-10-08 ~13:2xZ
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND5_L9_GRADE_BS9_AC2_20261008.md` lines 9-14):
`python lib/opal_naming.py census --all-roots` ->
`ALL-ROOTS ok=True roots_total=87 mapped=13 unmapped=74 completed=13 stopped=0 items=412 right=124 fix=248 not_asked=32 pattern=8 carded=0 refused=0 hole=0`.
Not re-run by this seat.

## Grade: NOT_REALIZED (advanced: a clean, repeatable run exists over 13 of 87 repository roots)

FWD-5's ACCEPT (`LGIC_ENFORCE_PRD.md`, the FWD-5 card), clause by clause:

| Clause | Read | Verdict |
|---|---|---|
| "runs the check over everything -- the stored code and what is actually running" | stored code: 13 of 87 roots print lines; 74 print none. What is running (the live AWS plane, PRD cell E9's `comp-find --corpus aws` arm): not in this run | NOT MET |
| "a ranked list of every name and address that breaks the pattern, each paired with its correct form, totals shown" | totals shown; 248 FIX lines each carry a correct form over the mapped roots (BS9-AC2 MET); "every" fails on the same 74 roots | NOT MET (mapped scope met) |
| "the totals agree with the ranking the naming work produced by hand" | no comparison with the hand ranking was made in this run or its grade | NOT MET (not attempted) |
| "a name the check cannot read stops the run loudly rather than being filed as breaking the pattern" | `stopped=0 refused=0 hole=0`: no unreadable name occurred, so the stop was not exercised. Absent is not exercised-against | NOT SHOWN |

## What would realize it (input to LGIC_ENFORCE's next round, not a cut)

1. The roots: LGIC_BLANKFIX round 6 E1 maps the next roots; FWD-5 reads met on the stored-code half only when every root
   that declares a stored name is mapped.
2. The live plane: one census over the live AWS plane, denominator printed, beside the repository totals.
3. The hand-ranking compare: the run's totals set beside the naming work's hand ranking, each difference explained.
4. The loud stop: one planted name the check cannot read, which must stop the run (a positive control).

## Re-grade 2026-10-09 ~01:2xZ, owed by LGIC_BLANKFIX ROUND_ANALYSIS.round7.md:18-19 (BLANKFIX FWD-5 REALIZED)

**The run graded:** `3.0.0_SA_CVO`'s re-run at `45e2856e41`
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/LGIC_BLANKFIX_ROUND7_L9_GRADE_BV2_BV3_20261008.md:23-24` @5e7cd9edbe):
`ALL-ROOTS ok=True roots_total=87 mapped=63 unmapped=24 completed=63 stopped=0 items=1598 ... hole=285 ... uncounted=301`, rc 0 in 29.5 s.
Not re-run by this seat.

### Grade: NOT_REALIZED (advanced: 63 of 87 roots mapped, up from 13)

| Clause | Read at `45e2856e41` | Verdict |
|---|---|---|
| everything, stored code and what is running | stored code: 63 of 87 roots; 24 unmapped, 301 items uncounted, 285 holes. Live plane: not in the run | NOT MET |
| a ranked list of every breaking name with its correct form, totals shown | totals shown over 63 roots; "every" fails on 24 roots and the 301 uncounted | NOT MET (mapped scope met) |
| totals agree with the hand ranking | not attempted | NOT MET (not attempted) |
| an unreadable name stops the run loudly | `stopped=0`; the 285 holes are filed as holes, not stops. No planted unreadable name was run | NOT SHOWN |

**What moved:** clause 1's stored-code half, from 13 to 63 roots. BLANKFIX round 8 (E1-E5, order: uncounted to 0 first, then holes, largest
root first) moves it further. **What stays this project's own:** the live-plane census, the hand-ranking compare and the planted-name
positive control (items 2-4 above); none is a BLANKFIX cell. Next re-grade: when BLANKFIX's census reads `unmapped=0 uncounted=0`.


## Re-grade 2026-10-09 ~15:2xZ (`1.0.0_SA_CTO~DELL1`, LGIC_ENFORCE now placed on DELL1 by L3 @e0413891af) -- BLANKFIX CLOSED

**The run:** LGIC_BLANKFIX's close (round 12 FWD-9, re-run by the CVO): `86/86 mapped, hole=0, uncounted=1`. The 1 uncounted item is
builder output and does not count (BLANKFIX round-11 ADDENDUM 1). BLANKFIX CLOSED @c23979cd0c.

### Grade: NOT_REALIZED -- clause 1's STORED-CODE half is now MET. Items 2-4 remain this project's own

| Clause | Read | Verdict |
|---|---|---|
| everything: stored code AND what is running | stored code: 86 of 86 roots, 0 holes. Live plane: not run | stored half MET; live half NOT MET |
| a ranked list of every breaking name with its correct form, totals shown | met over every stored root | MET on stored code |
| totals agree with the hand ranking | not attempted | NOT MET |
| an unreadable name stops the run loudly | no planted name run | NOT SHOWN |

**Round 20 (ONE issuance by `2.0.0_SA_COO~B1`, now seated):**
1. **The live plane:** one census over the live AWS plane (`comp-find --corpus aws`, as PRD cell E9 names it), with its denominator
   (nodes scanned) printed beside the repository totals.
2. **The hand-ranking compare:** the run's totals set beside the naming work's hand ranking, each difference explained.
3. **The loud stop:** one planted unreadable name, which must STOP the run (a positive control). Its negative control is a readable
   name that passes.
4. **Rows from BLANKFIX's close** (ROUND_ANALYSIS.round14.md section 2):
   - **D1-W2-S9:** the gate grades 0 strings for a name built by `name()` at a call site. The gate either grades the built name, or
     prints that it did not, so a pass there is never vacuous;
   - **D1-W2-S12:** one planted PATTERN-name commit on a QA branch, read for its grade.
