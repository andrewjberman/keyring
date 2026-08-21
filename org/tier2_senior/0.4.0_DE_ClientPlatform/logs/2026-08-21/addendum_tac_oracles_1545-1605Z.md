# Addendum 1545-1605Z -- MDPF_PROVENANCE T-A/T-C + the P4 flip oracle table

**archetype:** VALIDATE
**secondary_archetypes:** BUILD, SCRIBE
**serial:** 0.4.0_DE_ClientPlatform (base)
**window:** 2026-08-21 ~1545Z -> ~1605Z (delta since `p4_repoint_49f_p4r1_p4r2_1500-1600Z.md`; that log is the P4R-1/P4R-2 record and is not re-told here)

## Why I went looking at all

P4R-3 was blocked on an act that is not mine, so I went to my own TO list rather than waiting. Two of the fourteen were rotten in ways nobody could see without opening them, and one of those was dangerous.

## T-C -- a loaded weapon with a date on it

T-C's job is to DROP the `partner_provenance ?? cohort_provenance` tolerance. Its date clause is self-policing: *"If T-B's rename has not had one clean unattended 13:30Z run by 08-20, T-C re-dates to the day after that run -- stated on this TO the same day, never silently."* **08-20 lapsed with no statement.**

Measured the precondition on the live served artifacts (all four scopes, all written 2026-08-21T13:50:49Z..13:50:51Z -- so the producer IS running and NEVER#1 is correctly not in play):

| token | global | inflection | 49financial | cottonwood |
|---|---|---|---|---|
| `partner_provenance` | 0 | 0 | 0 | 0 |
| `cohort_source` | 0 | 0 | 0 | 0 |
| `cohort_provenance` | present | present | present | present |

And the discriminator is the **values**, not the key names: per-firm `cohort_provenance` still carries SOURCE IDENTITY -- `{"custody":"Orion","model":"Eclipse"}`, `{"custody":"Schwab","model":"SmartX"}` -- verbatim the PRE-R-2 shape T-C's own PC-3 describes.

Checked the plane before concluding: `pairedProvenanceRead.ts:312/:719` consumes exactly `series.partner_provenance ?? series.cohort_provenance`, so the served series is the plane the question is about.

**Therefore the tolerance is LOAD-BEARING, and executing T-C on its stated date would have broken the live Global provenance read on all four scopes.** A "remove the temporary adapter" TO whose adapter is the only working path is not merely not-due. COO's framing: *"TOs are written to be executed by whoever picks them up on their date, and a stale date converts a correct instruction into a destructive one WITHOUT ANYONE CHANGING A WORD OF IT."*

Re-dated ON the TO with the measurement, per the clause. **Anchor left INDETERMINATE** -- the clause re-dates to "the day after that run" and the run has not occurred, so no date is nameable. COO ratified that form explicitly: *"A DATE YOU CANNOT GROUND IS WORSE THAN NO DATE, because it re-arms exactly the hazard you just defused."*

DS~B then answered the producer fork better than either branch I offered: **R-2 was never landed in SOURCE** (measured zero for `partner_provenance` and `cohort_source` across 8,927 producer files; CTO's byte-current gold-member datum closes the undeployed branch from the other side). The port sequence's MIDDLE leg was skipped while the THIRD leg acquired a date.

## T-A -- stale-at-staged for three days

Complete since 08-18: `edcc503e` on **both** `origin/DEV` and `origin/PROD` (promoted in v2.1.163), validated at issuer by COO and CTO. Status still read "staged -- awaiting spawn". Flipped to complete after the proof instance validated.

**Instrument note:** my first proof run reported INVALID -- and the defect was MY INVOCATION (I passed six ids; the TO declares PA-1..PA-7). Checked the TO before concluding the artifact was broken. Re-run correct: **VALID rc=0**.

## P4_FLIP_ORACLES_49F (@d8808b489e) -- DE half OR-1/OR-2

20/20 frozen-list members carried, denominator printed. Four legs per row (route / shape / value-anchor / loud-signature), each an executable invocation with an expected and a stated plane. Composes existing instruments only (TO's "Do not"): `comp-keys`, `comp-routes`, `ui-smoke.mjs`, and `adviReadDiagnostics()` from my own P4R-2 module -- the tolerant read's diagnostic buffer turns out to be the natural observation point for the flip oracle.

**The substantive addition -- a THREE-STATE route rule.** CVO's OR-3 method frames route-leg must-fail as a natural 404. My P4R-1 finding makes that wrong in a way that changes DESIGN, not just an expected value: the twins are published AND unreachable, so a route leg today fails for a reason unrelated to the twin. Rows must discriminate S-ABSENT (publisher defect) / S-UNROUTED (route not built -- **not** a flip failure) / S-SERVED. Every route leg runs the S3 leg first.

**HELD rows get INVERTED oracles.** A flip table that only tests what flipped cannot detect OVER-flipping. Row 15 (`partner_analytics_monthly`, HELD) is the highest-value row: if a future edit collapses the `:369` template back to one repoint, rows 14 and 16 still PASS and only row 15 fails.

## Instrument failures caught this window (running total for the session: six)

1. **`aws s3 cp` reported rc=0 while writing nowhere I asked** -- the CLI resolved `/cygdrive/c/...` as a RELATIVE path (`..\..\..\..\cygdrive\c\...`) and wrote there. Caught by checking the file size after the copy instead of trusting rc. A cwd-relative destination works.
2. **`comp-find` returned an identical count (48) for eight different flag patterns** -- an undiscriminating result is not a measurement. Read the script's own arg parsing instead.
3. **A "measured" claim I had written but not run** (row 18's `prior_week` census). Ran it before committing (0 hits / 415 files -- the claim held) and corrected the cited invocation to the one actually executed.
4. **A proof-check INVALID that was my own bad argument**, not a bad artifact.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-keys prefix` | `platinum/mdpf/{4 scopes}`, `platinum/mdpf/` | all four scopes served today 13:50:49-51Z; established the producer is running |
| `comp-find` / `-i` | `partner_provenance` in portal/src; `prior_week`; ui-smoke flags | reader plane confirmed at `:312/:719`; row-18 absence measured; the flag census produced the undiscriminating result noted above |
| `.tools/proof-of-spec-check.py` | T-A instance, PA-1..PA-7 | VALID rc=0 unpiped (after correcting my own positional argument) |

## Blockers

None at my seat. **P4R-3** waits on the AE route act; **OR-4** waits on CVO's OR-3 pass; **T-C** waits on a T-B build that has not begun (DS base, COO routing).

## Current state

Workspace CLOUD: `388ce182b6`, `b5182ccf1f`, `eb64d27e97`, `d8808b489e`. Portal DEV: `033ed3c7`, integrated and pushed mid-session (local == origin/DEV == `82d3f28f`).
