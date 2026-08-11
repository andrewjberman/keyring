# ANALYSIS -- DS-base 49F P1 builds (B-1/B-2/B-3): state read, push-forward, generalization

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~0955Z** · **archetype:** VALIDATE
**Commission:** Andrew-direct via COO 095120Z ("analyze DS Base's results + what must happen to push
forward + generalization indications"). **This is an ANALYSIS, not a cert-of-built** (that stays
armed post-FINAL). Instances: PROOF_OF_SPEC_P1_{B1_GROUPA,B2_GROUPB,B3_GROUPC}_20260811.json
(11/13/13 rows). Vintages: A@6fba62393b, B@39c41163cd, C@f882b91ce2.

---

## STEP-ZERO (the undone half): TO-vs-SPEC COVERAGE DIFF -- ONE REAL GAP, IN MY OWN SPEC

**METHOD NOTE (COO correction 095628Z folded):** I ran the coverage diff BY HAND -- each instance's
acceptance rows read against my spec's §5 prose -- NOT via `proof-of-spec-check {instance} C1,C2,...`.
That was the right call and avoided the trap COO flagged: the tool's flagged `--expected-criteria`
form exits rc=2, and its natural fallback (drop the arg, re-run 2-arg) prints a clean `rc=0 VALID`
that ALSO says COVERAGE UNCHECKED -- the instrument's cleanest answer available exactly when the
check did not happen. The hand-diff also runs the correct LAYER: the tool checks instance-vs-its-own
-id-list (assignee omission); step-zero needs instance-vs-GOVERNING-SPEC (TO-list omission). The
diff is BIDIRECTIONAL -- I checked both directions: no 49F instance row fails to trace to a §5 bullet
or a folded amendment (no unexpected additions), and one spec artifact has no instance row (below).

I re-read each instance's criterion-id set against the GOVERNING SPEC's §5 battery. Groups B and C
are FULL COVERAGE (13/13 each; every §5 bullet has an id, every id a verdict). Group A has **ONE
UNCOVERED ARTIFACT:**

**A_03 (dim_security) was BUILT (`a03_dim_security.py`, in artifacts_produced) but has NO acceptance
criterion -- in my Group A §5 battery OR in the instance.** My §5 covers A_00/A_02/A_04/A_05/A_06 +
every-artifact-provenance; A_01 is covered only via the F5 amendment's sum-identity; **A_03 has no
bullet at all.** The instance is therefore internally VALID with A_03 unvalidated -- the validator
cannot see it (self-comparison), only this TO-vs-spec read can. **This is a defect in MY spec, not
in DS's build:** the battery row never existed to omit.

**WHY IT MATTERS, not cosmetic:** A_03 carries B_02's accrual-materiality inputs (interest_rate,
coupon dates -> the 112-asset predicate). The 1.6872% materiality number and its DERIVE
recommendation rest on an artifact with zero acceptance coverage. **REMEDY (owner: me, trigger:
now):** add A5-A03 rows to the Group A spec (rowcount + the security-master field-presence + the
rate-bearing predicate's own denominator), and DS backfills the instance rows on next touch. NOT a
P1-close blocker if the fields are spot-checkable, but it IS a spec-battery hole that two more firms
would inherit.

**AND THE STRONGEST SINGLE GENERALIZATION SIGNAL OF THE NIGHT sits right here:** ~A, minting the INF
Group A id set independently, CAUGHT THE SAME GAP -- judgment call (3): "A_03 gains a ROWCOUNT row by
extension of §5's first bullet (its parenthetical is exemplary, not exclusive)." **Two independent
alert readers found the identical hole; the transposition process SURFACED it rather than
propagating it.** That is evidence the method catches gaps -- see (c).

## (a) STATE READ -- what the results MEAN

**SOLID (measured, denominatored, machinery-caught):**
- B_00 boundary tie: 7,238 IN_CLIENT_BOOK rows, collection account excluded BY ID, spot-tie to the
  cent. The boundary_version + disjoint controls fired. Solid.
- B_01: zero silent drops over 95,879 rows; MV-tie 7,216/7,239 at 1bp (p50=p99=$0.00). The 23-account
  residue is THE VENDOR'S OWN TWO PLANES DISAGREEING (worst: a single-position account, clean $1M
  gap) -- carried as a FLAG by the flag-column machinery, not judged. Correct behavior; solid.
- C_01 migration delta printed by DESIGN (-$40,096.14 legacy vs -$53,987.01 headline + $260,585.39
  segregated; delta -$246,694.52) -- the diff-vs-c03 control working. Two feeds classifying
  differently is the finding surface, not a defect. Solid AS A SURFACE (not mine or DS's to close).
- The C_00 FEE-MANAGEMENT-VERIFIED catch: the nonzero UNRESOLVED census caught a $5,964.98 pair
  dropping AND caught that the classification table carries a vocabulary ("FEE-MANAGEMENT-VERIFIED")
  my spec PROSE never named -- machinery caught a declarative-drift. Solid, and a spec-fix signal.

**SOFT (measured but carrying an open decision or an un-turned distribution):**
- B_02 materiality 1.6872% with a DERIVE rec -- rides CTO's card + Andrew's half. Measured, but the
  number rests on the A_03-uncovered dim_security (step-zero above).
- B_03 first distribution UNTURNED (UNEXPLAINED 4,362 / TIE 2,397 / EXPLAINED 479; |var| p50 $190.85
  / p90 $5,916.81 / p99 $93,102.47 / max $204.6M). The census is machinery; the DISTRIBUTION is a
  one-day snapshot and the tail characterization is owed before any 1bp re-set (CTO-ruled, not
  re-litigated here).
- 68 of 137 EXTERNAL rows (50%) ride the conservative external-by-default -- the F4 segregated-NNA
  design contains the bias for NNA, but half the external ledger is a default, not a resolution.

**HONEST NON-COMPUTES (accepted):** C5-C04-PNLCONTROL UNCOMPUTABLE (month-grain identity from one
day is impossible BY CONSTRUCTION; rides the backfill) -- pre-authorized. The right answer.

## (b) WHAT MUST HAPPEN TO PUSH IT FORWARD -- owners + triggers (Andrew-actionable)

**BLOCKS P1-CLOSE:**
| # | Item | Owner | Trigger |
|---|---|---|---|
| 1 | **A_03 acceptance rows** absent from spec+instance (security master unvalidated; B_02 rests on it) | **CVO** (spec) -> DS (instance backfill) | NOW; DS backfills at next runners_49f touch |
| 2 | B-4 (Group D deployed-FE census) + B-5a writer-format -- in flight | DS-base | already running; P1 closes when both land + validate |

**BLOCKS P2 (not P1):**
| # | Item | Owner | Trigger |
|---|---|---|---|
| 3 | Schedule-floor atom UNEXERCISED (the INF-freeze atom) -- no P1 build touched it | AE (Group W wiring) | Group W instantiation, pre-first-fire |
| 4 | B_03 tail characterization before the 1bp re-set question | DS-base | the 525-partition backfill's first full run (P2+) |
| 5 | B_02 canonical_accrued_income (atom-8 named computation) | DS | on the Andrew+CTO DERIVE ruling completing |

**UNOWNED -- NAMED LOUDLY (COO asked for exactly this):**
- **The 50%-external-by-default half of the C_00 ledger has no resolution owner.** F4 segregated the
  NNA bias, but 68/137 EXTERNAL rows are a conservative DEFAULT, not a classification. Nobody owns
  turning that default into a resolution (pair-match extension / swb-column pass / position-delta).
  It is not a P1 blocker (conservative is safe), but at two more firms it compounds -- **recommend
  COO name an owner for the external-default resolution before COT (BD relationship-grain will make
  it worse).**

## (c) GENERALIZATION -- ATTACKED, not confirmed

**COO's frame is CORRECT and I adopt it: reproducing 49F's own spec numbers proves the 49F
implementation matches the 49F spec -- an instrument confirming what it was derived from. The three
49F instances CANNOT evidence transposability; absence of contradiction is not support.** The live
signal is ~A's INF Group A mint. Read as the first real test:

**THE SIX ~A JUDGMENT CALLS, sorted by transposition class:**
| Call | Class | What it tells us |
|---|---|---|
| (1) split the 3-part A_02 bullet into 3 rows | FORMAT-EQUIVALENT | issuance grammar, no semantic change |
| (5) "ALL" rows carry cross-artifact atoms | FORMAT-EQUIVALENT | structural promotion, verbatim intent |
| (4) two-calendar statement-day folds into gap-census | FOLD/SIMPLIFY | one check one frame; my amendment transposed cleanly |
| (2) collection NONEMPTY -> DECLARED-or-ABSENT-with-shape | **RELAXATION (firm-specific)** | the FRM-leg discriminator does NOT transpose -- Orion is not Schwab's ledger. A real divergence. |
| (3) A_03 gains a rowcount row | **ADDITION (gap-fix)** | caught my spec's A_03 hole independently |
| (6) INF-A-A00-PREDICATE added | **ADDITION (firm-specific)** | derived rep-scope predicate replaces the 28-site allowlist; a NEW need |

**THE DISTRIBUTION IS THE SIGNAL: of six calls, 2 format-equivalent, 1 fold, and THREE real
divergences (1 relaxation + 2 additions).** That is a ~50% verbatim / ~50% firm-adapted rate on a
SINGLE group -- NOT "reproduces to the digit." **This is the honest transposability evidence: the
shape transposes with a MEASURABLE divergence rate, and the divergences are named mechanics
(FRM-leg, allowlist), not surprises.** The archetype is a real skeleton, not a clone -- and the
method surfaces where firms differ instead of forcing them into 49F's mold.

**MACHINERY vs ALERT-READER (COO's axis -- what generalizes):** nearly every 49F finding was
MACHINERY-CAUGHT and machinery generalizes: the UNRESOLVED census (FEE-VERIFIED + the dropped pair),
the flag columns (23-account residue), the diff-vs-c03 (migration delta), the recon_status census
(B_03), the materiality census (B_02). **The ONE finding NO machinery caught is the A_03 coverage
gap -- caught only by an alert reader (twice: ~A and me).** That is the honest weak spot: the
archetype carries strong RUNTIME controls but its own SPEC-COVERAGE completeness is not
machine-enforced -- which is exactly what the PROOF-OF-SPEC step-zero (TO-vs-spec) exists to be, and
it is a HUMAN/CVO step, not machinery. **Recommend: the coverage diff becomes a mechanical
per-artifact check (does every produced artifact have >=1 acceptance id?) -- a gate candidate, CTO to
route.**

**NINE ATOMS -- WHAT P1 EXERCISED, WHAT IT DID NOT:** EXERCISED by A/B/C: atom 3 (_manifests), atom
6 (config-as-data, A_05), atom 8 (raw-preference, B_00 authoritative-not-reconstructed), atom 9
(provenance). **UNEXERCISED -- and two firms are about to instantiate them: atom 1 (product root,
P3), atom 2 (_code deploy target, P3), atom 5 (SCHEDULE FLOOR, Group W -- the atom whose absence
froze INF for 9 days), atom 7 (platinum serve, P4).** FOUR of nine atoms are untested by the builds
that "proved the shape." The schedule-floor atom is the highest-risk unexercised one.

**49F-SPECIFIC, MUST NOT TRANSPOSE (name them so a fork is not built believing it ported a shape):**
- the FRM-leg collection-account discriminator (~A already relaxed it -- the type specimen);
- the map-table identity join allocation_id->account_number->zfill(10) (SmartX-specific; INF is
  native-key 100%, COT is BD -- the zfill mechanic must NOT carry);
- the fact_fam positional parse (Schwab CRS; INF uses household_rep_mapping);
- the 3-axis Schwab code system tr_cd x sb_cd x tran_srcde (the classification TABLE transposes in
  FORM, ~A rebuilt it; the code UNIVERSE is firm-specific -- 46 INF transTypeId codes, not 187).

**THE ARCHETYPE-MACHINERY CLASS COO NAMED AS MOST IMPORTANT -- and my A_03 gap IS one:** COO's
template-defect specimen (the broken invocation + single instance_path, inherited by every TO minted
from the template; "fixed three copies before finding the source" = single-homing with better
cosmetics) is the exact class to hunt in the archetype's own machinery, because a spec-level defect
is not one defect -- it is ONE PER FIRM that instantiates. **My A_03 coverage gap is precisely that:
a SPEC omission that INF and COT would each inherit UNLESS each firm's minter happens to catch it by
eye.** ~A caught it -- but by alert-reading, not machinery, which means it is luck-per-firm, not a
closed class. **This elevates my recommendation from nice-to-have to load-bearing: mechanize the
per-artifact coverage check (every produced artifact has >=1 acceptance id) so the catch is
machinery, not a coin-flip on each firm's minter's attention.** That single gate closes the whole
single-homing class for the spec battery -- and it is the highest-value thing in this analysis, per
COO's own frame that an archetype-machinery defect outweighs anything in the three instances.

**UNCOMPUTABLE IS ONE STATUS OVER TWO DISTINCT CAUSES (Rule-24 grain note, from COO's B6 datum):**
the status value UNCOMPUTABLE now covers (i) BY-CONSTRUCTION-uncomputable (C5-C04-PNLCONTROL: a
month-grain identity from one day -- TIME resolves it, it rides the backfill) and (ii)
INSTRUMENT-CANNOT-DISCRIMINATE (B6's IAM deny-limb: an admin policy allowing all s3:PutObject cannot
falsify -- a DIFFERENT instrument resolves it, the exercised upload-readback). **Same status, DIFFERENT
REMEDY = a Rule-24 state-coherence failure on the status enum itself (postulate iv: the values do not
move together under one remedy).** Recommend the proof-of-spec schema SPLIT UNCOMPUTABLE into
`UNCOMPUTABLE-BY-CONSTRUCTION` (rides a named later run) vs `UNVERIFIABLE-BY-INSTRUMENT` (names the
substitute oracle) -- so a reader knows which remedy the row is waiting on. A schema amendment, gate
candidate for CTO.

## VERDICT ON (c)

**NOT "insufficient evidence" -- but NOT "proven transposable" either. The honest read: the shape is
a REAL SKELETON with a MEASURED ~50% firm-adaptation rate at Group A, its divergences are named
mechanics rather than surprises, and the transposition process demonstrably SURFACES gaps (the A_03
catch). That is genuine positive transposability evidence -- from ~A's mint, NOT from the 49F
instances, which COO correctly identified as tautological. The residual risk is the four unexercised
atoms (esp. the schedule floor) and the spec-coverage completeness being a human step, not
machinery.** Confidence: MEDIUM-HIGH on the skeleton, LOW on anything the four unexercised atoms
touch until Groups W/D land at INF too.

-- 3.0.0_SA_CVO
