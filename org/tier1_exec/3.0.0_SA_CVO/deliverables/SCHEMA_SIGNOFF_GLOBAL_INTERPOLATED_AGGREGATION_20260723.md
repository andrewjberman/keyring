# TANDEM SCHEMA SIGN-OFF + PERSPECTIVE -- Global interpolated-backfill aggregation

**Verifier:** `3.0.0_SA_CVO` · **2026-07-23** · **archetype:** VALIDATE
**Andrew-named** (CTO relay 023059Z; chain Andrew -> CTO/CRO -> CVO review -> COO decomposition).
**Two producers reviewed IN TANDEM:** CTO aggregation spec `@7ed8a6fd0` · CRO interpolation design
`org/tier1_exec/4.0.0_SA_CRO/briefs/COTTONWOOD_INTERPOLATED_BACKFILL_DESIGN_SPEC_20260723.md`.
**Incumbent carrier grounded at source:** `data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py`
(read this session; last-touch Jul 2, so run-vintage == the shape below).

---

## VERDICT: **SCHEMA NOT YET AGREED -- DO NOT BUILD EITHER SIDE.** Design is sound on both; the two
specs describe **five incompatible shapes for one channel**, and three of them are the *exact*
"two treatments of one concept" class this tandem check exists to stop (the by_model NULL-vs-0.0
artifact from tonight). None is a disagreement about the METHOD; all are shape. **They are cheap to
reconcile now and silent-breaking after build.** Perspective on the guards is strong-with-two-holes.

---

# PART 1 -- SCHEMA AGREEMENT (the tandem surface I own)

## >> S1 (P0) -- THE ENUM STRING DISAGREES, AND IT SILENTLY DEFEATS THE TAINT RULE. <<
- **Incumbent code, Andrew-established:** the literal is **`interpolated_estimate`**
  (`build_aggregate_aua_timeseries.py:482`, `:530` basis-provenance comment; 49financial precedent).
- **CRO** aligns exactly (`§3.1`, `§6` "extend the convention, do not fork") -> emits `interpolated_estimate`.
- **CTO** writes `provenance: measured|interpolated|absent` (`§2`) and `point_class: measured|interpolated` (`§4`).

CTO's aggregator derives `point_class` by **any-component-interpolated**. If the producer stamps
`interpolated_estimate` and the aggregator tests `== "interpolated"`, **the test never matches -> every
interpolated point derives `point_class = measured` -> renders SOLID, unlabeled, and passes into
measured-only consumers.** That is precisely §5.1's "planted interpolated point renders unlabeled"
mutant -- **live in the current spec pair, not hypothetical.** **Resolution: `interpolated_estimate`
is canonical (it is the incumbent + CRO). CTO's spec adopts it, or the schema declares one explicit
mapping table and both sides cite it.** One string; it is the whole ballgame.

## >> S2 (P0) -- GUARD 1 CONTRADICTS THE ACTUAL CARRIER. The served shape is PARALLEL ARRAYS. <<
CTO guard 3.1: *"values and provenance ship in one dated tuple, not parallel arrays a consumer can
split"* -- the construction the "no unlabeled read possible" claim rests on.
**The incumbent served slice is parallel per-date arrays** (`:573-578`): `model_aua: []`,
`non_model_aua: []`, `partner_custody_total: []`, **`cohort_provenance: []`** -- four independent
arrays indexed by date position. **A consumer CAN read `model_aua[i]` without `cohort_provenance[i]`;
the arrays are exactly "splittable."** And CRO `§3.1` explicitly **extends this parallel-array channel.**
So guard 1 is either (a) a **breaking re-shape** of the served series into per-date tuples -- a v1
contract change CTO's own "v1-frozen-additive" discipline forbids -- or (b) aspirational, in which case
**"an unlabeled read is impossible" is FALSE** and the headline guard does not hold. **This must be
decided before build: tuple-reshape (and own the migration) OR keep parallel arrays (and replace guard 1
with an index-alignment validator + a consumer-contract that reads the pair or refuses).** It cannot be
both.

## S3 (P1) -- PROVENANCE GRANULARITY: per-firm scalar (CTO) vs per-cohort array (incumbent + CRO).
Incumbent `cohort_provenance` is **per-date, per-COHORT**: `{custody: measured|rollforward, model_1a:
measured, sma_1c: interpolated_estimate}` (`:480-482`). CTO `§4` flattens to **one scalar
`by_firm.{firm}.provenance`.** These are different grains. It matters for the real Cottonwood case my
own sweep tonight measured: **`fact_holdings` is measured 06-09->07-20 while `fact_model_assignment` is
07-21/22 only** -- so in 06-09->07-20 Cottonwood's VALUE is measured but its ASSIGNMENT is interpolated.
The per-cohort channel represents that natively; CTO's single scalar must **collapse** it, and CRO `§5`
does collapse (assignment taint dominates -> whole point `interpolated_estimate`). **The collapse rule
is correct but UNSTATED in CTO's schema.** Fix: schema states the per-firm scalar is the *derived
taint-collapse* (any-cohort-interpolated) of the preserved per-cohort vector -- never a second,
independently-written field. Two writers, one derived-from-the-other, never two sources.

## S4 (P1) -- CONTAINER SHAPE: `by_firm: {<firm>: {...}}` (CTO) vs `partners: {firm_id: {...}}` dict
already in code (`:568` `.items()`). Same idea, different key name -> an aggregator written to CTO's
`by_firm` will not find the producer's `partners`. Pick one key. (Incumbent is `partners`.)

## S5 (P1) -- INTERP-METADATA FIELD NAMES forked three ways.
| concept | CTO `§4` | CRO / incumbent |
|---|---|---|
| method tag | `interp.method_version` | `backfill_method` (`:409`), union `backfill_methods` (`:454`); CRO `cot_snapshot_flow_fuzzy_20260723` |
| period | `meta.interpolation.affected_period` + a separate `interp.window_id` | CRO `affected_period [start,end]`; **no `window_id`** |
| confidence | `interp.confidence` | CRO `confidence` scalar (`§5`) -- **agree** |
`method_version` is a new name for the existing `backfill_method`; `window_id` has no counterpart and
may be `affected_period` named twice. **Canonicalize to the incumbent names** (`backfill_method`,
`affected_period`); keep `confidence`.

## S6 (P1) -- TWO ENFORCEMENT HANDLES for one quarantine. CRO `§3.3` filters measured-only consumers on
**`source=interpolated`** (the append-spec `source` key); CTO guard 3.1 filters on **`provenance`
class**; the incumbent channel is **`cohort_provenance`**. **Three field names for "is this point
interpolated?"** A consumer filtering on `source` while the aggregator tags `cohort_provenance` misses.
**One canonical quarantine key, cited by every measured-only consumer.** This is S1 wearing a second hat
and it is the same failure family.

## S7 (P2) -- ABSENT vs NULL. CTO provenance enum includes `absent`; incumbent uses **null**
`cohort_provenance` for unlabeled regions (`:484`, `:542`); CRO says `null/absent`. Two spellings of
"no label here." Pick one token; a mixed `absent`/`null` is a miniature of the artifact this check
exists to prevent.

---

# PART 2 -- PERSPECTIVE (CTO ask 1: any path to a measured-only consumer or an unlabeled render?)

**Two real paths beyond the schema mismatches above (S1 and S2 are themselves the two biggest paths in).**

## >> P-A (P1) -- THE ABSENCE FLOOR IS PER-MODEL IN CTO, PER-ACCOUNT IN CRO. The looser one re-admits a
YANG_SITTW sibling. << CTO guard 2: no interpolated point *"before the model's creation date."* CRO
`§5` + `§8.2`: no point before model creation **AND** before the **account's first-existence date**
(*"an account created 07-06 has no interpolated history before 07-06"*). **CTO's floor is weaker:** an
account created 07-06 on a model created 05-28 could receive interpolated points 05-28->07-06 under
CTO's guard (model existed) that CRO's rule forbids (account did not exist). **That is the exact shape
of the logged fabrication both specs cite** (`YANG_SITTW.TO-1`: $19.67M invented where the true value
was $0). **The binding floor is `max(model_creation, account_first_existence)` per point, enforced by
BOTH producer and validator.** CTO's schema ceiling must carry the per-account floor, not only the
per-model one.

## P-B (P1) -- RADIAL/BELL PROTECTION IS AN ASSUMPTION, NOT A GUARD. CTO `§1` protects the radial +
bell curve "by construction (current snapshot)." True **only while the radial's data source is a live
current read.** The leak path: if the radial ever computes its current figure as `timeseries[-1]`, and
there is any lag window where the newest Cottonwood point is interpolated (measured-forward not yet
landed), an interpolated value reaches the fee-basis radial. CTO's own `§2` hedges with "while the
fee-basis figure is current-only" -- **that "while" is the load-bearing conditional and it is
unguarded.** Make it structural: **assert `radial.source != timeseries-tail`** (radial reads the
current-snapshot artifact), and mutant M-B below plants an interpolated tail and confirms the radial
does not move.

**What is genuinely SOUND and I am not re-opening:** additivity-unchanged (value = sum regardless of
provenance; label not haircut) is correct and matches Andrew's "doesn't need to be exact." Supersession
being provenance-derived (overlay window shrinks automatically) is the right construction. CRO's
value-leg/assignment-leg split (value measured where snapshots exist, estimate only on assignment) is
honest and my sweep grounds its period map. The fingerprint-ban reconciliation (`§3`: inference-as-
interpolation is a different product category than inference-as-fact) holds **provided S6's single
quarantine key makes "never crosses into the fact channel" structural rather than promised.**

---

# PART 3 -- MUTANT SET (design-before-build; CTO's four + three the mismatches force)

| # | mutant | must produce | proves |
|---|---|---|---|
| M1 | planted `interpolated_estimate` point in the series | rejected by EVERY measured-only consumer (fee/DDB/identity/freshness) **and** renders yellow-dashed | CTO §5.1 core |
| M2 | same point, but stamped `interpolated` (CTO's string) | **the test above must still catch it OR the build fails** | **S1 -- the enum-mismatch is the mutant** |
| M3 | pre-**model**-creation date | refused by producer AND validator, independently | CTO guard 2 |
| M4 | pre-**account**-existence date (account 07-06, model 05-28, point 06-15) | refused by BOTH | **P-A -- the per-account floor** |
| M5 | interpolated estimate attempts to supersede a correctly-emitted **null/$0** | **FAIL LOUD** | YANG_SITTW replay (CRO §3.4 / §7) as a test, not a promise |
| M6 | read `model_aua[i]` without `cohort_provenance[i]` (parallel-array split) | **impossible, or the read refuses** | **S2 -- guard 1 vs the real carrier** |
| M7 | interpolated tail point + read the radial | radial value **unchanged** | **P-B -- radial source is a live read** |

**Each must be designed so it CAN fail** -- M2/M4/M6 in particular exist because a spec that agrees with
itself would pass them while the two-spec pair does not.

---

## ROUTING (verify-not-fix; I sign off nothing until the shapes are one)
- **CTO:** adopt `interpolated_estimate` (S1); decide guard-1 tuple-reshape vs parallel-array-validator
  (S2); state the per-firm scalar as derived-collapse (S3); align container + field names to incumbent
  (S4/S5); carry the per-account floor (P-A); make radial-source a guard (P-B).
- **CRO:** confirm the producer emits the incumbent `cohort_provenance` per-cohort array (not a per-firm
  scalar) and one quarantine key (S6); confirm the per-account floor is in the producer, not only the
  validator (P-A/M4).
- **COO:** do NOT decompose either spec into build TOs until S1+S2 are resolved -- they change the
  producer's output contract, so a TO written now builds the wrong shape.

## RESIDUAL / not verified
- I did **not** confirm the Global aggregator currently reads Cottonwood at all pre-07-21 (it may
  contribute nothing to Global `model_aua` today, since model_aua needs assignment). If it does not,
  interpolation is purely additive to Global history; if it does, there is an existing value to
  supersede. **COO's decomposition should settle this before the producer TO.**
- CRO's METHOD (backwards value reconstruction, fuzzy assignment, terminal-model washout) is **out of my
  scope** per CTO `§6` and CRO `§9`; I reviewed the SCHEMA and the honesty boundary, not the estimator's
  accuracy.

---

# RECONCILIATION AMENDMENT (CVO, ~0245Z) -- CRO's spec moved 3x DURING this review

**Part 1 above reviewed CRO `@8272fa0ed` (the version I was handed). CRO then re-emitted twice
mid-review** -- `@76c786b5e` supersedes it (folding two CTO review-round notes), with an uncommitted
working edit observed in between. **I re-grounded every finding against the CURRENT file
`@76c786b5e` + CTO `@7ed8a6fd0`. This amendment is authoritative; where it differs from Part 1, the
version moved, not my reading.** Naming the version is the control -- a sign-off that does not pin its
subject is the stale-record class I keep catching.

## >> PROCESS FINDING (P1) -- A TANDEM REVIEW CANNOT CONVERGE IF ONE SIDE RE-EMITS FASTER THAN IT
COMPLETES. << The producer spec changed three times inside one review pass. Folding CTO's notes is
GOOD; the hazard is that **COO decomposing against whichever version it happens to hold is tonight's
exact recurring failure** (a claim about an artifact that moved under its reader). **RECOMMEND: pin a
review version now (`@76c786b5e`); further schema changes re-enter review as a delta, not a silent
fold.** Without the pin, "CVO signed off" resolves to no fixed shape.

## How the convergence changed the findings -- and it did NOT clear the schema
CRO moved onto CTO's inline-tuple shape. That is real progress and it **resolves S3** (both now a
per-firm scalar + the collapse rule) and the **producer half of S2** (inline tuple, no parallel array
at emit). **But the two specs now AGREE WITH EACH OTHER AND DISAGREE WITH THE INCUMBENT CHANNEL THEY
BOTH CLAIM TO "EXTEND, NOT INVENT"** -- a cleaner, sharper defect than the original divergence.

| # | status after `@76c786b5e` | the surviving point |
|---|---|---|
| **S1** | **SURVIVES, REDIRECTED, still P0** | CTO + CRO now both use `interpolated`. **The incumbent channel uses `interpolated_estimate`** (`:482`; and CRO's own `§206` cites the 49financial precedent as `{measured\|interpolated_estimate}`). **You cannot "extend an existing Andrew-established channel" (CRO `§3.1`, CTO `§34-35` "no new channel invented") while changing its enum value.** AND CRO is now **internally inconsistent**: `§1a.2` says `interpolated`, but `§2/§145/§206/§280` still say `interpolated_estimate` (5 live occurrences). The string is unresolved in THREE places. **Decide: migrate the incumbent 49F channel to `interpolated` (a served-contract change someone must own) OR adopt `interpolated_estimate`. Not both, and not silently.** |
| **S2** | **SURVIVES, RELOCATED to the SERVED boundary, P1** | Producer emits inline tuples -- but **the incumbent SERVED slice is parallel arrays** (`:573-578`: `model_aua[]`, `non_model_aua[]`, `cohort_provenance[]`) and **neither spec reshapes it.** So "no unlabeled read possible" holds producer->aggregator and **breaks aggregator->FE**, where the FE reads the served artifact and CAN split the arrays. The tuple guarantee must reach the served boundary -- which is a breaking v1 reshape nobody has owned. |
| **S4/S5** | **SURVIVE, REDIRECTED, P1** | Same pattern as S1: `by_firm` (agreed) vs incumbent `partners` dict (`:568`); `method_version` (agreed) vs incumbent `backfill_method` (`:409,454`). Pair agrees, diverges from the code it extends. |
| **S6** | **SURVIVES, now INTERNAL to CRO, P1** | Three quarantine handles in one spec: `§1a` `provenance`, `§3.3` `source=interpolated`, `§3.1` `cohort_provenance`. A measured-only consumer filtering the wrong one leaks. |
| **P-A** | **PARTLY ADDRESSED, P1** | CRO added an **account-grain absent guard** (`@76c786b5e`: a transactions-hole degrades the account to `absent`, never silently interpolated) -- good, and it is the per-account floor at coverage grain. **But CTO's SCHEMA ceiling is still per-MODEL only** (`§3` guard 2); the per-account floor lives in CRO prose, not in either machine-checked schema. Put it in both validators. |
| **P-B** | **SURVIVES, P1** | Both now state radial/bell protection consistently, but it is still an ASSUMPTION (`radial reads current snapshot`), not a guard. Make `radial.source != timeseries-tail` structural. |
| **S3** | **RESOLVED** | Both per-firm scalar; collapse rule consistent (CRO `§5`). |

## THE UNIFYING FINDING (this is the one sentence for the record)
**Both specs claim to "extend an existing channel, not invent one," and the shape they have now agreed
on differs from that channel in enum value, container key, field names, and grain.** Changing all four
is not extending -- it is inventing a look-alike that will not interoperate with the 49financial
provenance already in the served artifact. **Either the incumbent channel migrates to the new shape
(owned, versioned, a served-contract change) or the new shape adopts the incumbent's vocabulary.** The
honesty argument in CRO `§3.1` ("we are extending Andrew's channel") is only true under the second choice.

## WASHOUT RE-DERIVATION (CRO asked; it is the `interp.confidence` semantics, so schema-adjacent)
- **Sat-50/60 re-derived from first principles** (weights in CRO `§4`: Sat-50 = 0.75 Int + 0.25 Short,
  Sat-60 = 1.0 Int; washout = Σ min(w_A,w_B) = 0.75): **REPRODUCES.**
- **All 5 pairs internally consistent** (washout + moves = 1.0 each). The other 4 I could **not**
  re-derive from first principles -- the raw B2 weight vectors for Sat-30/40/70/80 are not in the spec,
  only the resulting washout column (`§154-157`). **4 of 5 UNVERIFIED at the weight level, consistent at
  the table level** -- stated, not assumed.
- **The anti-cosine finding CONFIRMED and it is a good one:** the highest-cosine pairs (Sat-60/70 0.976,
  Sat-70/80 0.981) carry the WORST washout (0.50). So keying `confidence` on measured per-pair washout
  rather than basket cosine is correct, and I found no place in `@76c786b5e` still leaning on cosine for
  confidence. This upgrades the terminal-grain claim from argument to measured property, as CTO asked.

## MUTANT SET -- add two
- **M8 (CRO `@76c786b5e`):** a transactions-hole account -> renders `absent` over the gap, never a
  silent interpolated value. (The account-grain analogue of M5.)
- **M2 sharpened:** run the planted point stamped BOTH `interpolated` and `interpolated_estimate` -- the
  taint test must catch both, or the enum split (S1) is proven live.

## VERDICT UNCHANGED: **SIGN OFF NOTHING; DO NOT DECOMPOSE.** The convergence narrowed the gap and is
encouraging, but S1 (now internal to CRO too) and S2 (now at the served boundary) are unresolved, and
the "extend-not-invent" claim is falsified until the incumbent-vocabulary decision is made. **One
schema, pinned at `@76c786b5e` + `@7ed8a6fd0`, with those two decisions recorded, and I sign.**

---

# SIGN-OFF (CVO, ~0253Z) -- PINNED PAIR VERIFIED AT SOURCE. **SCHEMA SOUND. I SIGN.**

**Pinned pair:** CTO ruling record **v0.3 `@be91775dd`** + CRO producer/canonical-schema delta
**`@708661904`** (working tree == both, confirmed). **Every check below is against the artifacts, not
CRO's or CTO's cover note.** All 7 findings + all 6 rulings resolved.

| finding | resolution VERIFIED at source | evidence |
|---|---|---|
| **S1** enum | `interpolated_estimate` everywhere; **zero** residual bare-`interpolated` ENUM VALUES (all 17 bare occurrences are class-ADJECTIVES: "interpolated point/band/estimate"); `by_firm`=0, `method_version`=0 | grep of `@708661904` |
| **S2** served split | **R-2 two-stage** (interim additive `point_class[]` + FE single-accessor with direct-read-failing test; tuple reshape rides the F1 flip inside its gates). CRO's producer emits the incumbent `cohort_provenance` per-cohort channel -- consistent. | CTO v0.3 R-2; CRO `:54` |
| **S3** granularity | **RESOLVED BETTER than my finding** -- per-cohort grain labels custody=measured UNDER model=interpolated_estimate on the SAME date in the 06-08->07-21 band. The finer grain PRESERVES the value-measured/assignment-interpolated split I worried collapsing. | CRO `:54,:66` |
| **S4/S5** container/field | `partners` + `backfill_method` (method id+version as value; `confidence`/`window_id` additive siblings); `by_firm`/`method_version` = 0 | grep |
| **S6** three handles | **consolidated to ONE:** *"one channel, one filter predicate -- no parallel `source` key to keep in sync"*; enforcement handle is the `cohort_provenance` value itself | CRO `:113,:117,:119` |
| **P-A** floor | **prose -> two-lock VALIDATOR**: floor = `max(model_creation_date, account_first_existence_date)`, producer refuses AND schema validator independently refuses, either firing LOUD | CRO `:263-267` |
| **P-B** radial | **R-4 structural guard**: radial/bell producers assert `source != timeseries-tail` | CTO v0.3 R-4 |
| **R-6** washout | **ALL 5 re-derived FIRST-PRINCIPLES** from the now-published B2 weight vectors (washout = Sigma min(w_A,w_B)): Sat-50/60=0.75, Sat-40/50=0.75, Sat-30/40=0.75, Sat-60/70=0.50, Sat-70/80=0.50 -- 5 of 5 REPRODUCE. My earlier 4-of-5-weight-unverified residual is CLOSED. | my re-derivation from CRO `§4` weights |

**Anti-cosine finding** (0.976/0.981-cosine pairs carry the WORST 0.50 washout -> confidence keyed on
washout not cosine) stands, no residual cosine-lean. **The `interpolated_estimate` worst case I flagged
(one mismatch -> `point_class=measured` -> unlabeled render) CANNOT occur:** the string is uniform.

**RESIDUAL, non-blocking (P2):** 3 bare-`interpolated` class-ADJECTIVES remain in CTO's v0.3 ruling-
record prose (`:79/:100/:106`), superseded + demoted, in a document explicitly stamped
ruling-record-not-build-surface with CRO's `@708661904` designated THE canonical build schema
(delta-wins-on-disagreement). These are concept words, not enum values, and feed no code. **They do not
gate this signature.** CTO may tidy `:106` in any future pass; I do not require a v0.4.

## >> VERDICT: SOUND on all three axes for a design-stage schema. I SIGN THE PINNED PAIR. <<
- **MECHANICAL:** the taint chain cannot render a mixed point unlabeled (uniform enum); the quarantine
  is one predicate; the floor is two independent locks. Verified.
- **DECLARATIVE:** "extend-not-invent" is now TRUE by adoption -- the shape IS the incumbent 49financial
  channel, not a look-alike. The canonical-surface ambiguity is closed by designation, not by hoping two
  blocks match.
- **SEMANTIC:** the washout confidence basis is measured (5/5 re-derived), not asserted; per-cohort grain
  is the more honest representation.

**COO may decompose both specs.** My sign-off is on the pinned pair ONLY; per R-5, any later schema
change re-enters review as its own delta and this signature does not extend to it. **What I did NOT
verify (design-stage boundary):** the estimator METHOD's accuracy (CRO's, out of scope) and the BUILT
artifacts (there are none yet -- this signs the SHAPE before build, which is the whole point).

---

# R-5 RULING #1 (CVO, ~0433Z) -- DS 3F-BF1 date-restricted candidate set: DELTA, bless-with-conditions

**Durably recorded here because the ruling was message-only (broker 043332Z), and a pin disposition that
gates a co-signed serve must not live only in a message -- the message-only-carrier lesson (my own
DIG-2 / LD-0334 today) applied to my own ruling.**

**Call:** COO 042350Z routed DS's addition to the signed `@708661904` -- a **date-restricted fuzzy-match
candidate set** (`build_cottonwood_interpolated_backfill.py:410-411`, `avail = strategies with
createdAt <= d`). DS correctly did NOT self-absorb it.

**RULING: DELTA (re-enters review), not a within-intent clarification.** Grounded at source, with a
positive control that the signed spec is retrievable (so the empty candidate-restriction grep is a true
absence):
- The signed `@708661904` specifies the floor as **refuse-below-floor**; it says nothing about
  restricting the candidate set or substituting. Substitution-to-existed-on-d is **new behavior**.
- It **changes served content**: `:426-427` -- when the unrestricted best-match strategy did not exist
  on `d`, the producer does NOT refuse; `fuzzy_assign(basket, avail)` picks the best *existed-on-d*
  strategy and EMITS. So it emits MORE points and DIFFERENT assignments. **COO's "strictly more
  conservative -- refuses more, never fewer" is factually wrong at the code level** (COO accepted this).
- **Material, not marginal:** the band (05-28->07-21) overlaps the model-creation window
  (05-28->07-17), so early-band dates are heavily substituted.
- **11/11 mutants green is necessary, not sufficient** (verified by reading
  `test_interpolated_backfill_mutants.py`): the 11 cover refusal / enum / lock-independence /
  supersession -- **none distinguishes substitute from absent**, because the signed spec had no
  substitution to test.

**Why it is a GOOD delta (bless-with-conditions, not reject):** the substitute is provably closer to
truth (an account could not have been on a strategy that did not exist), and it fixes a latent early-
band **understatement** the signed refuse-behavior would have (dropping real account value from the firm
total). Aligned with Andrew's "show the labeled estimate over a gap."

**TWO CONDITIONS close it (DS/CRO own; I verify + sign into the pin):**
1. **New mutant (DS):** plant an account-date where the unrestricted best-match did not exist on `d` but
   >=1 substitute did -> assert the emitted point is the existed-on-d substitute, labeled
   `interpolated_estimate`, floor-passed (not absent, not the non-existent strategy). Permanent, like M2/M8.
2. **Confidence-regime confirm (DS/CRO):** on the heavily-substituted early band, confidence must
   HONESTLY DEGRADE (the signed refuse-behavior showed `absent` = honest "don't know"; the delta shows an
   estimate, so its confidence must carry that uncertainty). I could not settle this from code alone
   (needs the bronze createdAt set + per-date `avail` counts) -- **stated as a confirm-item, not a pass.**

## CORRECTION to my own ruling (COO 043928Z caught it -- accepted in full)
My closing footnote said "the qt5 sweep shrinks this delta's blast radius over time (supersession)."
**That was an UNVERIFIED ASSUMPTION on my part** -- I asserted a supersession effect without grounding
which LEG supersession touches. Supersession (point_class upgrade) applies to the **value/custody leg
only**. Per **CRO's 042742Z current-stamped ruling (relayed by COO; I did NOT independently ground the
underlying qt5 numbers)** -- 0 real historical Opal assignment changes -- the **assignment/model cohort
this delta governs is PERMANENTLY interpolated** and does not shrink. **Therefore condition 2 is a
PERMANENT honesty mechanism, not transitional** -- no downstream reader may relax it on a
"temporary anyway" read. The correction strengthens the ruling; it does not weaken it.

**DISPOSITION: DELTA, review in progress, NOT BLOCKING** (co-sign pending, nothing serves). On
condition 1 passing + condition 2 adequate, I sign the delta into the pin. **This R-5 signature, when
given, extends the pin to the delta only -- not to any further change.**

-- `3.0.0_SA_CVO`
