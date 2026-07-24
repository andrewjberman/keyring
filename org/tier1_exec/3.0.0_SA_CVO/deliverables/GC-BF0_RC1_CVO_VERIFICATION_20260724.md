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

— 3.0.0_SA_CVO
