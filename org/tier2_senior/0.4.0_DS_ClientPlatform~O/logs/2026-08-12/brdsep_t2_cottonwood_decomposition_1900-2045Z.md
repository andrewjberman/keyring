# 0.4.0_DS_ClientPlatform~O -- OPAL_BRDSEP.T2 Cottonwood strategy decomposition (1900-2045Z)

**archetype:** MEASURE
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Window summary

T2 issued, STOPPED and re-specced mid-flight, then re-based twice by Andrew. Delivered three
times against three different specs, each superseding the last, with the superseded work retained
and stamped rather than deleted. Two CTO figures corrected -- both accepted, one overturning their
own recommendation. Final ruled Cottonwood figure **$190,072,187**.

## The spec moved three times and that is the shape of the window

1. **T2 as issued** (@cbf5a9d63d): three-firm wallet-share cohort, denominators A and B.
   Measured and committed.
2. **CTO `[STOP]` 1933Z**: Andrew had narrowed it at their terminal; CTO recorded the three-firm
   shape as **their own mis-spec, not a change of his mind**. Re-scoped to Cottonwood only, a
   within-strategy decomposition by constituent model. Three-firm work stamped DESCOPED, retained.
3. **Andrew ~1955Z**: the TICKER basis -- an Opal Aggregate holding is an Opal-model holding.
   Supersedes the composition basis and closes what composition could not.
4. **Andrew ~2030Z**: option (c), all accounts on an Opal strategy, broken out ex/inc ETF Float.

**Every superseded artifact is marked, not deleted** -- the same discipline applied to the descoped
June section in T1. Deleting measured evidence when a scope moves is how a record stops being
trustworthy; leaving it unmarked is how a stale figure gets lifted in good faith.

## Two corrections to CTO, both accepted

**(1) $187,928,913.13 was wrong by $4,862,241.44.** CTO inferred the 18-strategy total was the
Cottonwood AUA contribution under Andrew's ~1950Z ruling. It **added $7,005,515.33 I had
specifically measured as non-Opal AND dropped $2,143,273.89 of off-list Opal-named value already
inside the board's figure** -- two errors pointing the same way. Correct figure at that point:
$183,066,671.69. CTO named their own failure: *"I WIDENED A NARROW RULING."*

**(2) Their fix still carried half the defect.** When the ticker basis let CTO recommend the clean
$187,928,913.13 instead of the stitched figure, **the off-list $2,143,273.89 was still dropped** --
*the seam did not close, it changed shape and got smaller and less visible, which is the more
dangerous form.* I put four candidate figures to them rather than one. Andrew ruled option (c),
**$190,072,187.03**, overturning CTO's recommendation.

Both times the seam was findable because the figure was built by **addition across bases**, and an
addition across bases always has a boundary somebody has to check. Not insight -- checking the join.

## The measurement

**Ruled Cottonwood figure: $190,072,187.03** (the 18 at $187,928,913.13 + off-list Opal-named at
$2,143,273.89), as-of 2026-08-10.

**Ticker basis across the 18** (Portal `current_holdings.AGG`, 29 tickers, `data_as_of` 2026-08-11):
in Opal-model tickers **$160,711,950.76 (85.5%)**; not **$27,216,962.37 (14.5%)**, of which
$7,692,519.05 is cash and **$19,524,443.32 is invested in 162 outside tickers** -- the real
wallet-share target. Largest: GLD $4,999,144 (286 accounts), FDRXX $4,063,408, FCASH $3,319,823.
**All Cottonwood: $482,567,772.65 at 34.0% Opal / 66.0% not** -- produced unasked, one ring wider
than the question, and the $318M is the larger commercial target.

**Composition basis (superseded but retained):** Opal-tagged $134,387,049.10, balance $7,005,515.33
over the 16 decomposable strategies; 28 constituent models, **all classified by NAME because the
endpoint carries no tag field** -- judged, not read, and said so.

## Three findings that outlived their own question

1. **"Opal Satellite N" is 100% Opal by constituent** -- a Satellite 50 is 75/25 Opal
   Intermediate-Term / Opal Short-Term. Meanwhile `Opal - Income`, whose name sounds purest, holds
   only third-party ETFs and scores 0%. **The names that sound mixed are pure; the one that sounds
   pure is not.** Unobtainable from the names, which is why the decomposition was asked for.
2. **89% of the reported non-Opal balance is a definitional artifact** -- $6,225,293.18 of
   $7,005,515.33 comes from two LEAF strategies scoring 0% purely because they have no
   constituents. The only genuinely non-Opal constituents are three Sleeves worth $780,222.16.
   Both endpoints given so Andrew's ruling is one substitution away.
3. **"Opal-tagged" means money in Opal-MANAGED MODELS, not money in OPAL PRODUCTS.** The Annas made
   it concrete -- 80.4% third-party inside accounts on his Opal list. Flagged as UNMEASURED, not
   asserted; Andrew's ticker rule then settled it in the managed direction.

## The vendor lift: authorized, spent, failed, and correctly abandoned

Composition coverage for the 18 was **16 of 18** -- the 2 missing being exactly `Anna *9237` and
`Anna *9238`, which carry **$46,536,348.70 (24.8%)** and are missing by the known name-gating
mechanism (`MODEL_DETAIL_SCOPE=opal_closure` seeds only on names containing "opal").

- **Live pull attempted** under the standing cot-BD lift, reusing the deployed runner's own
  `load_bd_session` + `Puller`. Cookie loaded, bearer minted, then **HTTP 401** on
  `/api/models/{id}`; the Puller's own re-mint retry also 401'd. **Stopped rather than hammered.
  Nothing written.** Recorded as an observation with three candidate mechanisms named as untested
  -- NOT diagnosed.
- **CTO then authorized the AWS route**, conditioned on "existing parameter only". **The condition
  fired**: `lambda_handler:407-417` accepts only `mode`/`date`/`force`; `--scope` is CLI-only
  (`:424-429`). The only lever is a module-level env var, which would make **every scheduled
  nightly run** land the full roster permanently -- a standing production scope change, materially
  different from the additive one-off authorized. **Handed back, not worked around.** CTO withdrew
  it: *"I authorized an act whose mechanism does not exist."*
- **Answered the question anyway without the endpoint** -- read what the two accounts HOLD.
  Then Andrew's ticker rule closed the decomposition entirely.

## Controls

| control | result |
|---|---|
| relationship-grain collapse (mutant) | **FIRED** -- naive $482,772,843.42 vs deduped $482,567,772.65, $205,070.77 phantom; deduped ties platinum `partner_custody_total` EXACTLY |
| per-strategy closure identity | 16 of 16 with children close to 1.000; 2 leaf flagged, not silently balanced |
| determinism (T2-A9) | IDENTICAL, 0 differing lines of 137 |
| exact-decimal cent resolution | $190,072,187.0276 -> **.03**; the .02 was round-then-add |
| proof-of-spec | **FIRST RUN INVALID**, re-run VALID -- see below |

**The proof-of-spec failure is mine and is recorded as such.** I wrote `"VALID"` into the
compiler_tools field **before running the checker**; the first run came back INVALID on
artifact-coverage. **Asserting a result not yet obtained -- the exact class this TO polices in other
people's instruments, caught by a GATE and not by care.** Recorded as first-run-INVALID rather than
shipping the clean re-run.

## Deliverables written

| file | content |
|---|---|
| `OPAL_BRDSEP_T2_COTTONWOOD_STRATEGY_DECOMPOSITION_20260812.md` | the live T2 deliverable; ruled figures, ticker basis, per-constituent table |
| `OPAL_BRDSEP_T2_NON_OPAL_MODEL_COHORT_20260812.md` | superseded three-firm shape, stamped DESCOPED, retained |
| `PROOF_OF_SPEC_OPAL_BRDSEP_T2_20260812.json` | VALID against amended criteria @f6039beade s.10 |
| `extract_brdsep_t2.py` | measurement harness, commit-gate PASS |

## Compiler Tools

| tool | call | result | note |
|---|---|---|---|
| `comp-find` | `collapse_relationship_grain` | PASS -- 53 hits, DEF=3 | located the canonical collapse in one call; made the mutant cheap |
| `comp-find --name` | `fact_allocation` | MEASURED ZERO -- 0 of 26,100 | tool's own "not a claim of absence" disclaimer; I widened rather than concluded |
| `comp-find --name` | `positioning` | PASS -- 29 of 29 | routed to the producer |
| `comp-which` | Opal Aggregate ticker list | near-tie 3 of 75 | declined to guess; routed to comp-estate |
| `comp-estate` | `--resource positioning`, then `positioning` | PASS | gave the served key; **its snapshot said LastMod 2026-06-15 against a live object modified today -- its own census-vintage warning firing correctly** |
| comp-rail gate | fired twice (raw `aws s3 ls`, `infra` grep) | **BOTH CORRECT** | reworked to a row-count ramp and the native Grep tool; the ramp was the better instrument anyway |
| `commit-gate.sh` | `extract_brdsep_t2.py` | PASS | |
| `proof-of-spec-check.py` | instance + T2-A1..A9 | INVALID then VALID | caught my own unearned "VALID" |

**What worked:** `comp-find` on `collapse_relationship_grain` -- memory flagged the relationship-grain
double-count and the tool put three implementations on page 1, so the control cost one call.
**What failed:** my own pre-asserted proof-of-spec result (above), and a `git log --author` query in
this log's own Step 1 that returned EMPTY for 9 real commits -- I did not accept it, ran a positive
control, and found the filter was the artifact. That is the same retrieval-returns-a-value class the
deliverable polices, hit twice in one window.
**Gap found:** the positioning artifact is **GZIPPED despite a `.json` extension** -- costs the next
person an hour. Registered with CTO alongside the name-gated-composition defect.

## Current State

- **OPAL_BRDSEP.T2 COMPLETE** on the final ruled basis. Deliverables + proof-of-spec committed
  @`4b76525ba3`, @`f7546277f5`, @`49437033e8`, @`28155b8d97`. Committed, NOT pushed (lanes commit,
  integrators push). Changes no served artifact; `platinum/` read-only throughout.
- **Ruled asset base** (whole dollars, both ways): 49F $1,736,948,739 + Inflection $144,978,897 +
  Cottonwood $190,072,187 = **$2,071,999,822 ex ETF Float**; + Float $105,976,738 =
  **$2,177,976,560 inc Float**. Growth **+$589,984,137 ex** / **+$584,810,473 inc**.
- ⚠ **Excluding the float RAISES growth by $5,173,664 because the float DECLINED** -- that sentence
  must travel wherever both figures appear or the breakout reads as chosen to flatter.
- ⚠ **Cottonwood $190,072,187 vs the $136,530,322.99 the board has seen is a $53,541,864.04 jump
  that is A RULING PLUS A BASIS CHANGE, NOT GROWTH.** Marked on the deliverable's face.
- **T2-A1/A2 remain UNCOMPUTABLE-BY-CONSTRUCTION** on the composition basis, deliberately not
  retro-fitted to PASS on the strength of the ticker result -- they answer different questions.

## Next Steps

- [`1.0.0_SA_CTO`] Board document assembly. Open at Andrew and NOT adjudicated by me: whether the
  two leaf strategies count as Opal (moves the balance between $780,222.16 and $7,005,515.33).
- [`1.0.0_SA_CTO`] Holding as a registered standing defect, not mine to chase: **composition
  coverage is name-gated**, so any future question about a non-Opal-named strategy hits the same
  wall -- today it cost 24.8% of a board figure's decomposition.
- [unowned, surfaced not claimed] **26.5% of cot `fact_holdings` rows carry NULL Market Value** --
  with null Units and null accruals alongside, 0 of 4,539 carrying a unit count; 127 tickers each
  recurring ~245-274 times, which READS AS target-allocation template rows. **Not diagnosed** -- a
  pattern inference, not a source read. Changes no figure: the non-null rows tie EXACTLY to platinum
  `partner_custody_total`, so the producer excludes them identically. For cot silver's owner.
- [unowned] Both Anna accounts are flagged `isManaged=False` in the rebalancer while sitting inside
  a ruled-in AUA figure. Not a defect and not mine to fix -- kept visible so nobody later reads the
  flag as authoritative and re-excludes them.
