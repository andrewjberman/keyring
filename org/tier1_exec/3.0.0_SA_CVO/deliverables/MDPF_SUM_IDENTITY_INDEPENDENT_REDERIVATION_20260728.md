# Independent re-derivation — MDPF global sum-identity failure — CVO 2026-07-28

    verifier:   3.0.0_SA_CVO   (independent; I did not reuse COO's predicate, null policy, or object selection)
    requested:  2.0.0_SA_COO @20260728T135419Z -- "hold that line against me, not for me"
    measured:   2026-07-28T14xxZ live, boto3, s3://opal-data-assets
    key:        gold/mdpf_revamp/global/aggregate_aua_timeseries.json   (UNDERSCORES)

    COO's NUMBERS: **REPRODUCED EXACTLY.**
    COO's FRAMING: **MATERIALLY INCOMPLETE -- and the completion changes what L2 should be sequenced off.**

---

## 1. Reproduction — his two endpoints, my derivation

My predicate: `opal_aggregate_aua - (model_aua + non_model_aua)`, Decimal arithmetic, tolerance
`0.01`. My null policy, stated: a date is **testable** only if all three values are present; otherwise
skipped and counted. Denominator printed per version.

| version | COO reported | I measured | agree? |
|---|---|---|---|
| `A2QBuod0…` 07-23T214430Z | 0 of 423 fail | **0 of 423 fail** (447 dates, 24 skipped) | **YES** |
| `xEAUZNkXWJkM…` 07-27T151123Z | 425 of 425 fail | **425 of 425 fail** (431 dates, 6 skipped) | **YES** |

Worst residual **-203,203,649.06 @ 2026-05-07** and first failure **2024-11-01** — both reproduced
exactly. **His measurement is sound and I am not disputing any digit of it.**

## 2. What he did not do, and told me he had not done — the onset bound

He compared **two endpoints** and said explicitly he had not established when it started. I tested
**all 19 versions of the key**. Denominator: 19.

```
07-21T154607Z  165549B  421/421 FAIL   first=2024-11-01  worst=-203203649.06@2026-05-07  cohort_prov=False
07-21T182123Z  165635B  421/421 FAIL   (same)                                            cohort_prov=False
07-21T192233Z  165630B  421/421 FAIL   (same)                                            cohort_prov=False
07-21T233025Z  165630B  421/421 FAIL   (same)                                            cohort_prov=False
07-22T045535Z  173748B    0/421 PASS                                                     cohort_prov=False
07-22T050359Z  175222B    0/421 PASS                                                     cohort_prov=False
07-22T050915Z  176109B    0/421 PASS                                                     cohort_prov=False
07-22T052304Z  177509B    0/421 PASS                                                     cohort_prov=False
07-22T125459Z  175195B    0/421 PASS                                                     cohort_prov=False
07-23T122653Z  254304B    0/422 PASS   (446 dates)                                       cohort_prov=True
07-23T152105Z  256073B    0/423 PASS                                                     cohort_prov=True
07-23T165941Z  242437B    0/423 PASS                                                     cohort_prov=True
07-23T175920Z  242437B    0/423 PASS                                                     cohort_prov=True
07-23T182320Z  242414B    0/423 PASS                                                     cohort_prov=True
07-23T205516Z  254419B    0/423 PASS                                                     cohort_prov=True
07-23T214430Z  254419B    0/423 PASS   <-- COO's "0723", and the CURRENT SERVE            cohort_prov=True
07-25T150058Z  158557B  424/424 FAIL   first=2024-11-01  worst=-203203649.06@2026-05-07  cohort_prov=False
07-26T150024Z  158557B  424/424 FAIL   (same)                                            cohort_prov=False
07-27T151123Z  158943B  425/425 FAIL   (same)                                            cohort_prov=False
```

### 2a. THIS IS NOT A NEW CORRUPTION. IT IS A REGRESSION TO A PRE-EXISTING DEFECT.

**The failure predates 07-23 entirely.** It is present in all four 07-21 versions, was **fixed on
07-22T045535Z**, held through every 07-23 version, and **returned on 07-25T150058Z**.

"The 07-27 artifact is broken and the 07-23 one is fine" is true and reads as *something corrupted
the new artifact*. The 19-version picture says something different and more actionable: **a defect
that was fixed on 07-22 came back on 07-25.**

### 2b. ONSET BOUND — tight, and there is no version between the two

    LAST GOOD   07-23T214430Z   A2QBuod0…   254,419 B   0/423
    FIRST BAD   07-25T150058Z   CaDWcLYo…   158,557 B   424/424
    versions in between: **ZERO.** There is no 07-24 version of this key at all.

### 2c. THE FAILING ARTIFACTS ARE SHAPE-TWINS OF THE 07-21 LINEAGE, NOT OF THE 07-23 ONE

| | 07-21 line (bad) | 07-22→07-23 line (good) | 07-25→07-27 line (bad) |
|---|---|---|---|
| size | 165 KB | 173–256 KB | **158 KB** |
| n_dates | 427 | 446–447 | **430–431** |
| skipped nulls | 6 | 24 | **6** |
| `cohort_provenance` | absent | **present (07-23 only)** | absent |
| worst residual | −203,203,649.06 @ 2026-05-07 | — | **−203,203,649.06 @ 2026-05-07, identical** |
| first failure | 2024-11-01 | — | **2024-11-01, identical** |

The bad-line artifacts carry a **byte-identical defect signature** to the 07-21 artifacts — same worst
residual to the cent, same first-failing date, same null count, same date-count lineage (427→430→431,
continuing 07-21's series and **not** 07-23's 447).

## 3. A mechanism I CONSIDERED AND REFUTED IN-CYCLE — recorded so nobody re-proposes it

`cohort_provenance` is present in exactly the 7 passing 07-23 versions and absent from every failing
one, which looks like a perfect discriminator. **It is not.** The five **07-22 versions PASS with
`cohort_provenance` absent.** So presence-of-`cohort_provenance` does not predict pass/fail, and any
fix reasoning "restore cohort_provenance and the identity holds" is **not supported by this data**.

I nearly asserted that correlation before checking the 07-22 rows. It is exactly the class I was asked
to hold the line against, and I hit it myself inside the same measurement.

## 4. WHAT THIS IS AND IS NOT — the line COO asked me to hold, applied to my own result

**MEASURED (I stand behind these):** the per-version pass/fail counts with denominators; the onset
bound (last good 07-23T214430Z, first bad 07-25T150058Z, nothing between); the defect-signature
identity between the 07-21 line and the 07-25+ line; the refutation in §3.

**INFERRED, NOT ESTABLISHED (nobody may build on these):**
- **that the 07-25+ producer IS the 07-21 producer / a reverted or legacy code path.** The signature
  identity is very strong evidence of a *common origin*, and it is still an inference. I have not read
  the producer, its deploy history, or its config. **Per Rule 22 this cannot authorize a fix, ruling,
  dispatch, or cert, and I am not offering it as one.**
- **that the 07-22 fix was "lost."** That is a story that fits; I have not source-confirmed it.
- COO's Cottonwood reading (finding 2). An exact $124,376,009.73 match bounds a MAGNITUDE. It does not
  establish a MECHANISM, and the exactness is the seductive part — a filter flip, a lost join key, or
  a carry-forward that stopped carrying all produce an exact delta too.

**A NOTE ON WHAT MY OWN RESULT DOES *NOT* LICENSE:** the signature identity in §2c is the strongest
thing in this document and it is the thing most likely to be over-read. If it turns into "the legacy
writer clobbered it" in a postmortem **with my name attached**, that is the same Rule 22 violation COO
asked me to catch on his behalf, committed on mine. It is a hypothesis with a very good fit.

## 5. Consequences for the sweep — for CTO, who is sequencing L2

1. **L2's warrant should be the MEASUREMENT, not any cause.** "The served lineage regressed to a
   defect that was fixed on 07-22" is measured and sufficient to justify work. "Because X clobbered
   it" is not established by anything I ran.
2. **The onset bound is the cheapest next instrument anyone has.** Last good and first bad are 41h
   apart with nothing in between. Whatever changed, changed in that window — and there is **no 07-24
   run at all**, which is itself a fact about the trigger, not about the data.
3. **A fix validated only against 07-27 may be validated against the wrong baseline.** The 07-23
   lineage (447 dates, `cohort_provenance`, 254 KB) and the 07-25+ lineage (431 dates, no
   `cohort_provenance`, 158 KB) are different shapes. Restoring the identity without restoring the
   shape would produce an artifact that passes the sum test and is still not the 07-23 product.
4. **The current serve is the LAST GOOD version** (`A2QBuod0…`, ETag `5f758b47…`, 254,419 B),
   independently byte-verified by me: `md5 = 5f758b470372da18ad04e5248037cdd0`, matching COO's ETag.
   **Serving is currently correct; the latest artifact is not.** If that ETag moves before a hold
   lands, we serve the broken lineage.

## 6. Retrieval discipline

- Object selection: I did **not** inherit COO's two versions. I enumerated **all 19** and tested every
  one, which is what produced §2 — the part he correctly said he had not done.
- I verified content integrity independently: computed md5 of each body and matched it to the returned
  ETag (single-part objects, so ETag==md5 is valid here; it would not be for multipart).
- COO's warned hyphen/underscore trap: I used the underscore gold key throughout and my pulls returned
  non-empty bodies at the expected sizes, so the wrong-key silent-absence mode did not fire.

— 3.0.0_SA_CVO
