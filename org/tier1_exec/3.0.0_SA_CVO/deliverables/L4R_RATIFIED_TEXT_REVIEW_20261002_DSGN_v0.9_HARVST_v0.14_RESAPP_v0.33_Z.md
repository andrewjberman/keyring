# L4-R ratified-text half -- DSGN_AMGTV1 v0.9 (REFUSE), AMGT_HARVST v0.14 (SIGN), AMGT_RESAPP v0.33 (SIGN)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~19:0xZ
**Deliveries:** `1.0.0_SA_CTO~Z` msgs 28629, 28630 and 28631, all at PRD commit `82d1cb21e2`, plus ask 28632. The half hashes,
recomputed by this seat with `.tools/prd_signoff_lib.py half_hashes`, equal each delivery: DSGN `4d4a49148dc5`, HARVST
`cfc0a9f245b0` and RESAPP `593b18ac3493`.
**Pin:** Andrew-direct ~17:33Z, `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261002_173xZ_SECURITY_ANALYSIS_UIUX_WALK_BRIEFS_TO_CTO_Z.md`
(6,080 B, read to EOF: verbatim plus N1-N10). Fold record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_SECURITY_ANALYSIS_UIUX_20261002.md`
(10 rulings).
**Method:** the ratified-text sections (ENDPOINT + CONTRACTS, cut by `prd_signoff_lib.top_sections` / `half_of_section`) at the last
pin this seat signed, diffed against `82d1cb21e2`:
- DSGN: v0.8 @`7912f7aee2`, +103/-20.
- HARVST: v0.13 @`7d73abbe0e`, +38/-0.
- RESAPP: v0.32 @`c505327bd7`, +50/-0.

Every quote was verified by printing the cited bytes, not by grep: the N1 quote at the record's verbatim block, and "finbert not
being sure is not a vote" at `NEWS_SCANNER_DEEP_DIVE_20260916.md` section 6 (:359-366, wrapped across two lines).

## 1. AMGT_HARVST v0.14 -- SIGN

FWD-16 (FinBERT tone per article version, keyed to `record_hash`) and FWD-17 (30/90/365-day articles_total, voters and tone in gold;
all-neutral reads voters 0 and tone null, never 0.0) carry N8 and N10 and Andrew's 09-16 rule. Each is EXERCISED by an act on demand:
the one-time corpus scoring, and a planted all-neutral name as the negative arm. No vendor is reached: the scorer is Opal's own
`opal-news-ai-sentiment` (fold ruling 6). The banner above FWD-16 is the addendum form signed at v0.13.

Notes, which do not block:
- **The threshold.** "voters (articles whose FinBERT label is not neutral and whose confidence clears the stated threshold)". Andrew's
  pinned rule (09-16 section 6) is that a 0.0 / neutral score is not a vote; he names no threshold above it. Any threshold above 0 is
  the CTO's addition. It must be stated as a NUMBER in the gold artifact, or an unstated value passes vacuously.
- **The window end.** FWD-17 ends a window "at the as-of date"; RESAPP FWD-36 ends it "at the last trading day". These agree only if
  gold's as-of date is the last trading day (T-1). Worth one word at the next bump.

## 2. AMGT_RESAPP v0.33 -- SIGN

- FWD-36 serves the windows and tone from HARVST gold, "never computed at request time". This agrees with HARVST FWD-17 on fields
  and windows, and with DSGN FWD-26 (the page never computes a window).
- FWD-38 is the served half of N6's "easy to read" and of the register's disagreement rows.
- This seat's own read today (DSGN ADJUDICATION_v30 `Z-C-S36`) is a live instance of FWD-38's ACCEPT ("no two served figures for one
  thing disagree"): rankings `places_moved` null vs overlay -3 for AMD.

Notes, which do not block:
- **FWD-37's earnings branch.** "a name with no burst still carries its earnings markers once pulled" is conditional on a pull that,
  per the fold record, waits on a vendor word. Read as written, FWD-37 is gradeable now on its interim branch: the kind served with its
  reason. That grade must not be read as exercising the earnings path (ABSENT != EXERCISED). If the CTO means the earnings path
  itself, the outcome needs the wait qualified with Andrew's word (L2).
- **The window end:** as in section 1.

## 3. DSGN_AMGTV1 v0.9 -- REFUSE

The amendments to FWD-5, 12, 20 and 22 and the new FWD-25, 26 and 27 trace to N1-N10:
- **FWD-12 LIGHT** is the CTO's pick between the two styles N1 offers. The SOURCE quotes N1 verbatim with one marked elision. FWD-20's
  band clause follows it.
- **FWD-5 earnings markers** stay gradeable, through the designed empty state.
- **The HeroDialog** is a pre-existing modal pattern. N6's "e.g. the topic cloud analyses pop up modal" is an example, not a pin. The
  Market Overview modal is a custom `KeywordSentimentModal`, not a HeroDialog, so the two are not the same component. That is
  acceptable under "e.g.".

Two defects, both inside FWD-21, make the outcome contradict itself and its producer:

1. **FWD-21's ACCEPT was not restated with its DONE WHEN.** At `82d1cb21e2` the DONE WHEN reads "the selected ROLLING window (30D,
   90D or 365D; FWD-26)", and FWD-26 replaces "Earlier month" / "Later month". But the ACCEPT still reads: "The PM says which names
   were collected most this month, steps back two months and says what changed." A built page cannot meet both. A grader reading the
   ACCEPT would fail a correct build, because there is no month to step back to.
   **Fix:** restate the ACCEPT for the windows, e.g. "The PM says which names were collected most in the window, switches 30D to
   90D and says what changed." The SOURCE should also gain N7, N8 and N10.
2. **The no-tone case contradicts HARVST FWD-17, the producer of the tone it reads.** DSGN FWD-21: "a name with no scored articles is
   neutral and says so on hover". HARVST FWD-17 ACCEPT: "a name nobody voted on reads 'no clear tone', not neutral". It also serves
   tone null, never 0.0. A name with no scored articles is a name nobody voted on, so the two halves prescribe opposite words. DSGN is
   also silent on the commoner case: scored articles, all neutral, voters 0.
   **Fix:** "a name whose served tone is null (no voters) is filled apart from the ramp's neutral centre and reads 'no clear tone' on
   hover". This is Andrew's "not being sure is not a vote" carried to the face.

Neither defect is wording under the section hash: both are ENDPOINT acceptance text. Under the proportionate rule, an ENDPOINT change
re-signs, so this seat signs the next bump on these two fixes alone.

-- 3.0.0_SA_CVO~Z
