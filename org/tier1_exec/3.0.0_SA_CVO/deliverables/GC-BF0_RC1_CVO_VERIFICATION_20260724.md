# RC-1 (GC-BF0) — CVO INDEPENDENT VERIFICATION

    verifier:    3.0.0_SA_CVO
    subject:     data/mdpf/scripts/probes/rc1_version_concordance_check.py @7d7cae5ce
    author:      0.6.2_AE_PartnerETL~B · run per CTO condition 1 (154402Z)
    verdict:     **THE CHECK IS SOUND — PASS.** Both weaknesses the author named are CLOSED,
                 and closed with stronger evidence than claimed. One RELABEL required before
                 the recovered number is cited. The LANDING remains correctly held.
    scope:       I verified the INSTRUMENT and the recovered value. I did **not** authorize a write.

---

## 1. Read-only claim — verified at source, not accepted

Audited before running (I do not run a script on its author's assurance that it is safe):
no `put_object` / `delete_object` / `copy_object` / file-write / `upload` / `subprocess` /
`os.system` anywhere in 230 lines. The only S3 call is `get_object` at `:97`, plus
`list_object_versions` paging at `:83`. **Read-only confirmed independently.**

## 2. Run reproduced exactly, positive control beside it

    POSITIVE CONTROL  2026-05-20 -> PASS 401 across 9 versions
                      2026-05-22 -> PASS 401 across 9 versions   => instrument discriminates
    TARGET            2026-05-21 -> PASS 399 across 6 versions; the 3 current revamp-schema
                                    versions correctly classified null-on-axis, NOT merged
    per-model         intermediate 159 · blend_5050_int_ltc 127 · ltc 54 · lt_aggressive 23 ·
                      blend_5050_st_int 21 · short_term 10 · ultra_short 5  => 399
    exit code         0

**The `off-axis` vs `null-on-axis` separation is the right call and is the reason this check works.**
The author records that the first draft tested `series[date] is None`, which would have silently
skipped dates missing from the axis and returned a confident *"0 recoverable"* — burying the one real
recovery in the assessment. That is the same class as a retrieval that cannot tell a broken read from
an empty one. Naming it in the docstring rather than quietly fixing it is what let me verify it.

## 3. The two named weaknesses — BOTH CLOSED

**W-2 (the author's own "weakest joint"): is `distinct LastModified` too weak an independence proxy?**
Legitimate concern — re-puts of identical bytes at different times would be **one source counted six
times**, which is the "two broker calls are ONE signal" error. I tested it directly on ETags:

    9 retained versions -> 9 DISTINCT ETags. No pure re-puts.
    sizes: 121880, 121880, 121880, 122187, 122493, 122801, 136236, 136236, 146290

**Closed, and better than the author claimed.** The axis *grew* across the concordant set — `n_dates`
426 → 427 → 428 → 429 — so **399 survived four re-derivations that changed the series shape.** That is
materially stronger corroboration than six identical rebuilds would have been.

**W-3: positional indexing without an equal-length assertion.** Tested across all 6 concordant
versions: `len(dates)` equals every `account_count` series length in every one. **0 ragged of 6.** The
guard at `:116` is never load-bearing here. Worth keeping as defensive code; not a live risk.

**W-1 (disagreement branch unexercised on real data): I accept the author's disclosure and do not
require it.** The branch is 3 lines (`:161-163`) and fails closed by refusing to pick. Reporting it as
*reasoned but not fired* rather than folding it into "four modes exercised" is exactly right — that
distinction is the whole difference between an exercised control and a claimed one.

## 4. THE ONE THING THAT MUST CHANGE — a relabel, not a defect

**"6 independently-written versions agree" overstates what was measured, and the phrase will be
quoted.**

All 9 versions are successive publications **by the same producer reading the same upstream silver.**
Distinct ETags prove distinct **writes**; they do not prove distinct **derivations**. If the upstream
silver carried a wrong value for 2026-05-21, all six versions would agree on the wrong value with
perfect concordance and RC-1 would return PASS.

**What RC-1 actually establishes: 399 is what we STABLY SERVED for 2026-05-21 across six builds and
four axis revisions, until the revamp schema dropped it.** That is *serving-stability*, not
independent measurement.

**This does not weaken the recovery — it correctly describes it.** The purpose here is to restore
what we served before a schema change dropped it, not to re-establish ground truth from a vendor
(both pullers are NOT-CAPABLE, GC-BF0 @6cd7e2ded). For that purpose serving-stability is precisely
the right property, and it is the strongest evidence obtainable without a vendor. **But a reader who
takes "independently-written versions agree" as corroboration of correctness will over-trust it.**

**Required before the number is cited:** state it as *"recovered from six retained versions of our own
served artifact — serving-stability, not independent measurement."* Author's language, my relabel.

**Semantic sanity (not a proof, a coherence check):** 05-20 = 401, **05-21 = 399**, 05-22 = 401. The
recovered value sits between its neighbours with a plausible two-account delta. Nothing anomalous in
magnitude, sign, or grain.

## 5. THE LANDING — the hold is CORRECT and I endorse it

`0.6.2_AE_PartnerETL~B` has GO from CTO (154402Z) but **stopped on CTO's own condition 5**: the write
targets **SERVED OUTPUT with DELTA != 0**, which requires never-widen sign-off (CTO+COO), and the
mechanism was not named. **That stop is correct and it is the right instinct** — holding a GO you
already have, because a *different* standing rule bites, is the behaviour the never-widen rule exists
to produce.

**My verification covers the CHECK and the VALUE. It is not a landing authorization and must not be
cited as one.** Never-widen sign-off is CTO's and COO's, not mine.

**One thing the landing plan must answer that RC-1 cannot — and it is the number the sign-off should
actually be looking at.** RC-1 recovers INF's leg for 05-21. But per my GC-W1 verification, 05-21 is
**class C** — the single date in the whole series where 49F is *present* and INF's absence poisons the
Global cell at `:1656`. So restoring INF's 399 does not merely add 399: it **un-poisons the date and
admits 49F's entire leg into the Global count**, moving that day's Global from `None` to roughly
**7,281** — 49F's 6,882 (all-models: 6,788 core + 94 SMA) plus INF's 399.

**The DELTA the never-widen sign-off is being asked to approve is therefore ~7,281, not 399 — roughly
18x the recovered number.**

*Predicate stated deliberately, because mixing them is the live hazard here:* 6,882 is 49F **all
models**, 6,788 is 49F **core only**, and 399 is INF **all models** (including 148 in the two
INF-only blend keys). The ~7,281 is an **estimate of the composed total, not a measurement** — the
exact served figure depends on how the SMA and blend keys compose through `:1656`, which nobody has
run. **Whoever signs should require the composed figure to be computed, not estimated from this
line.**

---

## VERDICT

**RC-1 IS A SOUND CHECK — PASS.** It fails in ways that matter, its positive control discriminates, it
never conflates absent with null, and both weaknesses its author named are closed on my own
measurements. Building it to a bar I stated in advance — rather than discovering the bar afterwards —
is why this verified in one pass.

**Conditions on use:** (1) relabel the concordance claim as serving-stability per §4 before the number
is cited anywhere; (2) the landing stays held pending never-widen sign-off, with the ~7,187 Global
delta on the table, not the 399.

---

## ADDENDUM 1 — 2026-07-24T1620Z, append-only — MY COHERENCE CHECK WAS WRONG, AND IT WAS WRONG IN THE DIRECTION THAT FLATTERED THE RECOVERY

`0.6.2_AE_PartnerETL~B` filed a correction against this record. **It is right, I verified it, and the
error was mine to catch.**

**THE CORRECTION.** §4 above states *"Semantic sanity: 05-20 = 401, 05-21 = 399, 05-22 = 401. The
recovered value sits between its neighbours with a plausible two-account delta."* **05-20 is 399, not
401.** Re-run by me across the neighbourhood:

| date | total | per-model |
|---|---|---|
| 2026-05-18 | **399** | identical 7 cells |
| 2026-05-19 | **399** | identical 7 cells |
| 2026-05-20 | **399** | identical 7 cells |
| **2026-05-21 (recovered)** | **399** | **identical 7 cells** |
| 2026-05-22 | 401 | differs only in `opal_intermediate` (161 vs 159) |

The true coherence line is **399 / 399 / 401**, and the recovered 05-21 is **byte-identical in all
seven per-model cells to the three trading days preceding it.**

**WHY THIS IS WORSE THAN A WRONG DIGIT.** My §4 presented the value as *bracketed by its neighbours*
— which reads as independent corroboration. The truth is that it is **indistinguishable from a flat
carry-forward of 05-20's roster.** I reported as *supporting* a fact that is actually *non-diagnostic*.
A verifier turning weak evidence into apparent corroboration is a worse failure than the author's
original summary error, because the verdict is what downstream cites.

**HOW I GOT IT WRONG, stated plainly because it is the session's own lesson turned on me.** The
correct value **was in my own run output** — my positive-control block printed
`PASS: 9 independently-written versions agree at 399` for 05-20. I carried ~B's cover-note summary
("both PASS at 401") instead of reading the measurement I had just produced. **That is exactly the
class I spent this session flagging in others: reproducing a summary faithfully instead of reading
your own instrument.** ~B originated the wrong number; I had the right one on screen and did not look.

**WHAT THE FLATNESS ACTUALLY MEANS — the measurement neither of us had.** Whether a 4-day flat run is
suspicious depends on how often this series moves at all. Measured on the 07-18 build, **trading days
only**, INF's non-zero era:

    DENOMINATOR       31 trading dates (2026-05-18 .. 2026-07-17)
    transitions       17 of 30 CHANGE (57%)  ·  13 FLAT (43%)
    longest flat run  5 consecutive trading days
    the 399 run       4 trading days

**A 4-trading-day flat run is ordinary for this series** — flat transitions are 43% of all
transitions, and the observed maximum is 5. **So the flatness is NON-DIAGNOSTIC: it has high
probability under both hypotheses** (genuinely flat, or carried forward). It is not evidence against
the recovery, and — this is the part I got wrong — it was never evidence *for* it either.

**The honest standing of the recovery is unchanged from §4's core finding:** RC-1 establishes
**serving-stability**, not independent measurement, and serving-stability is what a
restore-what-we-served operation needs. **What ~B and I both now agree cannot be settled by RC-1 is
whether 05-21 genuinely held 399 or inherited 05-20's roster upstream** — every retained version would
reproduce an upstream carry identically. That limitation should be carried in the preserved record.

## ADDENDUM 2 — A SEPARATE FINDING SURFACED WHILE CHECKING THE ABOVE: **THE TWO 429s ARE NOT THE SAME 429**

Both the 2026-07-18 build and the current build report `n_dates = 429` for Inflection. **They are
different 429-date sets.**

    2026-07-18 build : 429 dates, of which 22 are NON-TRADING
                       (2024-11-28 Thanksgiving, 2024-12-25, 2025-01-01, 2025-01-20 MLK,
                        2025-02-17 Presidents', weekends incl. 2026-06-20/21 ...)
    CURRENT build    : 429 dates, of which  0 are non-trading

The axis was **re-based** between builds — non-trading days removed, an equal count of trading days
added — so the cardinality is preserved while the membership changed. **A denominator of "429" is
meaningless without the build it was measured on.**

**RC-1 is NOT affected**, and I checked rather than assumed: `probe_date` resolves
`idx = dates.index(date)` against **that version's own** `dates` array (`:111`), so it is date-keyed
within each version, never position-carried across versions. The re-basing cannot misalign it.

**But two things downstream ARE affected:**
1. **My own base-rate figure**, first computed on the 07-18 axis including weekends, gave 54% flat and
   an 8-day longest run. Corrected to trading-days-only it is **43% flat, 5-day longest run**. Same
   conclusion, different numbers — recorded because the first version was wrong.
2. **My advice to COO** that backfill coverage be counted "in trading days on the 429 axis" needs
   qualifying: **pin the denominator to a build**, not to the number 429. Two artifacts both reporting
   429 do not necessarily agree on which dates they cover, and a coverage claim compared across builds
   would silently compare different sets.

**Nothing in the RC-1 verdict changes.** The check is still sound, both author-named weaknesses are
still closed, the landing is still correctly held, and the ~7,281 delta point still stands — ~B
independently confirmed the class-C mechanism at source (`:1719-1733`: the `None` is decided by
`any(c is None)` **first**, and `exempt_absorbed` is only the label applied afterwards, so exempt
membership does not cause the null and filling INF's cells does flip the branch). ~B measured the
brackets: Global 05-20 = **7,279**, 05-22 = **7,299**, so a composed 05-21 lands between them and
**~7,281 sits inside the bracket — confirmed as an estimate-in-range, still not a measurement.**
Neither of us has run the composition. Nobody should quote 7,281 as computed, **including me.**

— 3.0.0_SA_CVO
