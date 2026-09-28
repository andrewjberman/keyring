# self-drive ticks 119-121, `1.0.0_SA_CTO~Z`, 2026-09-26 ~18:50-20:30Z

**Arming record:** `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md` @`f3b85ff6a5`.
**state: ARMED.** Prior log ticks 116-118 @`81f2aaa8b1`. **Floor exceeded AND substantive delta.**

Broker still DOWN for this seat. Filesystem inbox only; watcher re-armed 4x this block (125-128).

---

## 0. BOTH OWED HALVES ARE DISCHARGED

| act | hash |
|---|---|
| **`AMGT_RESAPP` tt-2 CTO never-widen half** -- owed since the round opened | **`392fee249c`** |
| **`AMGT_CORPUS` round-7 CTO halves, acts A and B** | **`8b27c6f2cc`** |
| GOAL clause-3 finding | `70b65a680a` |
| prior log | `81f2aaa8b1` |

**Nothing in my queue is now blocked on me.** tt-2's preconditions are met (both halves committed, tt-1
drained @`00ffce7fbf`); CORPUS round 7's two drain acts are cleared to run under limb 4.

## 1. THE CLAUSE-3 FINDING: THE GOAL'S COMPLETION SENTENCE IS UNREACHABLE BY CONSTRUCTION

`opal-data-harvest`'s universe holds **89** names; the application's population is **95**. Strict subset,
6 absent: **AIA Group, AMD, Alphabet GOOGL US, Eli Lilly LLY US, Quanta Services PWR, UnitedHealth UNH US.**

**One folder read at two times, not two folders.** `universe_source` @`628b975b49` reads
`...\Asset Management\Research` at `read_finished_at 2026-09-10T23:18Z`, 89 folders. The app's pinned
population reads the **same** corpus root at `2026-09-26T13:29:01Z`, 95. **Sixteen days.**

**THE SHAPE OF THE SIX FALSIFIED MY OWN DIAGNOSIS.** I had said clause 3 was ceilinged by the missing
ex-US slug rule. Four of the six are plainly US-listed -- exactly the names the US rule resolves most
easily. **They are absent because they POSTDATE the snapshot.** A missing-rule cause predicts the
opposite shape. And AMD is one of round 45's two served control fixtures: **a name can be load-bearing
in the application and absent from the backfill universe at once, because nothing joins the two
populations.**

**THE JOIN'S CONTROL IS THE ZERO.** In-app-not-in-harvest 6; in-harvest-not-in-app **0**. Inconsistent
folder spellings would have produced non-zero on BOTH sides, so 89 of 89 matching exactly is what
licenses reading the 6 as absence rather than a naming artifact.

**AND I CORRECTED TWO FIGURES I HAD PUBLISHED TWICE, INCLUDING TO THE CVO, WHICH ACCEPTED THEM:**
denominator **89 not 95**; without a symbol **64, not "45 NEITHER"**; and the dominant blocker is
**57 of 89 carrying no `bloomberg_ticker` at all** -- `infer_sa_symbol`'s FIRST UNRESOLVED branch --
not the ex-US rule I named. **The 25 was true and I carried it into a population it never measured.**

## 2. THE tt-2 HALF -- AND THE CONDITION I SET CAUGHT A REAL DEFECT

I read `_posture_markdown` @`:660` at HEAD: **five branches, MECE and total** over
(`posture` falsy/truthy) x `status` x `verdict`.

**Branch (i) has TWO arms carrying the markers in OPPOSITE directions.** Non-SERVED: `:701` header form
**without** the `Nothing is rendered in its place.` tail, `:703` tab form **with** it. SERVED+absent:
`:711` tab form **without** the disclaimer, `:715` header form **with** it.

> **So the expected outcome is FOUR EXACT STRINGS, not "two lines."** A half that said "the export gains
> the page's second line" would be graded PASS by an instrument that only counted lines, and would never
> catch the tail and the disclaimer landing on the wrong arm. That is stop limb 6.

**THE CONDITION I MADE OF THIS SIGNATURE PAID OFF.** `2.0.0_SA_COO~Z` re-read its own half against the
landed rule and found branch (ii) **both too wide and vacuous** -- *"a SERVED posture"* includes
SERVED+absent, which DOES change, and *"already carried both forms"* was impossible at base. It amended
to three states @`52128e2a19` **before** telling me the rule was readable. **The re-read found a defect
instead of ratifying one**, and its line refs match my own read digit for digit.

**BOTH FALSIFIERS RE-RUN BY ME, not adopted:** AC1 `missing=0 on 95 of 95, OK 95 of 95, rc=0`, cases
`285/285`; AC2 `rc=1` on both planted controls, `missing=1 extra=0`. **AC2 is a control on the
INSTRUMENT** -- at base the same predicate read OK on both, so without it the fix would have left a
verdict unable to see the clause it certifies.

## 3. THE CORPUS HALVES -- ONE GATE, ONE NEGATIVE ARM, ONE NEAR MISS

**ACT A: I signed on the RULE, not the report.** `CASE_BAND_LOW 0.33` and `CASE_BAND_HIGH 3.0` are
**unchanged** and the decision is one comparison @`:1256`, so **the band verdict is bit-identical by
construction, not by observation.** `CASE_BAND_BASIS` is the only addition, at two sites.

Round 6's enrichment cell 2 landed in the right shape: the floor carries `calibration: "uncalibrated"`
with the empty-bin basis, the ceiling `"measured"`, **and neither bound value moves.**

**THE NEGATIVE ARM I ADDED:** `currency_mismatch` / `forward_eps_not_positive` / `no_price` return
BEFORE the band branch, so they must gain **no** `band_basis`. **Exactly 53 of 94 carry it; the other 41
must not.** Counting only the 53 would pass a defect that stamped all 94 -- attaching a band claim to
refusals the band never decided.

**THE NEAR MISS I TESTED because it would have made N=2:** `derive_fye_fixed.py:93` writes
`derived/model_block_fye/`, which a listing of `derived/model_block/` does **not** match -- next
character `_`, not `/`. **The disjointness rests entirely on the trailing slash**, and all 7 DEF-band
constants carry it. N=1 confirmed on a different instrument than the COO used.

**ACT B: the GATE is the substance.** I read the failure arm first -- `_select_stored` @`:920` falls back
explicitly and totally, *"so a table is never left unserved"* -- so no name can be unserved and CRPS-i-1
is the right fix. **But that per-name fallback is benign only in isolation.** Step 2 writes 95 dossier
objects each baking in whichever continuation its name served, so **a partial step 1 yields a corpus
split across `/1` and `/2` terms, written once, on one `as_of` date.** The mix is **recoverable** by
uri+sha and **not declared** -- no dossier field carries `method_version`, so no consumer can reject on
it. **`Z-S45`'s split-brain moved one hop downstream into a write-once artifact**, where the cheap
rollback no longer reaches it because today's names already exist.

**Limb 4: if step 1 is not 95/95, step 2 does not run.** The COO had it as an after-run discriminator; the
dossier rollback lands on the NEXT `as_of` date by its own statement, and that asymmetry is the reason.

## 4. Z-S47: THE EXCLUSION IS RIGHT AND THE EXPOSURE IS NOT CLOSED

`6861_JP` and `CSL_AU` read ABSENT under today's rule where their served blocks read SERVED -- **and the
`histdata` object at exactly the raw stamp those blocks name is still landed** (9,074 B / 8,864 B), with
no raw-stamp selector on the CLI.

> **Two served values cannot be regenerated by any current code path while the raw they were built from
> still exists.** A reproducibility defect in stamp selection, not data loss. Excluding them beats
> destroying two good cases for a field addition -- the same judgment the issuer showed holding the `/2`
> rewrite at round 6, and it cost it a clean "97 of 97."

**Binds the drain report:** round 6's enrichment cell 4 is **1 of 3**, NOT closed.

## 5. AN OFF-TASK HUNCH I CHECKED AND DROPPED WITHOUT FILING

`_management_markdown` (`:548-575`) has the same absence shape as posture, so I checked whether it had the
same two-surface defect. **It does not: `management` reaches ONE surface by the code's own cited
measurement.** No row filed -- the disconfirming evidence was in a comment, found by reading rather than
by investigating. **I did NOT enumerate the shared page header**, so whether any other section is
duplicated into `PostureHeaderLine`'s neighbours is open, and the half says so rather than implying a
sweep.

## Step 0 reads

```
REGISTER: 6 sitez live directives -> 20 projects | ARMED SCOPE 5 / 18 (D6 carved out, arming record s.2a)
COMPLETION TEST: NOT DONE -- 4 of 20 register-scope / 4 of 18 armed-scope status:complete
INBOX: 5 messages read this block, 8 sent; 0 unread at close
OPEN CALLS IN SCOPE: 0 adjudicable | 1 RESERVED (serp = metered SPEND, Andrew's)
```

## Scope state

| project | where it sits |
|---|---|
| `AMGT_RESAPP` | round 45 executing; tt-1 drained, **tt-2 cleared to run**; tt-4 proof drained @`186f3bef34` |
| `AMGT_CORPUS` | round 7 issued (5 orders); **both drain-act halves signed**, act B gated on limb 4 |
| `AMGT_HARVST` | round 7 at **20 of 21**; `v-2` mid-drain at `2.0.0_SA_COO~Y`; CVO holds L8/L9 until it lands |

## Cards at Andrew -- ONE, unchanged

1. **The `serp` BUILD** -- metered, so 92 names is SPEND, excluded BY NAME from his egress term.

## Still owed by this seat

- **Nothing blocked on me.** The next CTO acts are `AMGT_HARVST`'s round-7 analysis (waits on `v-2` and
  the CVO's slug) and the fresh 19-outcome CORPUS pass (round 7's cell `i-5`).
- Round-6 / round-44 broadcasts remain **EMITTED-not-READ**; no ack mechanism exists.

## Compiler Tools

The producer's own `universe` command used as the oracle rather than hand-deriving its census -- a two-sided
set difference whose `0` is the join's positive control -- `corpus_root` compared across both artifacts,
which turned "two populations" into "one folder at two times" -- both tt-1 falsifiers RE-RUN rather than
adopted, AC2 being a control on the instrument and not the product -- the failure arm of `_select_stored`
read BEFORE signing act B, which is what distinguished "no name is unserved" (true) from "a partial run is
recoverable" (false) -- and the writer census re-done on a different instrument than the issuer's, which
found the `model_block_fye` near miss the token census could not see.
