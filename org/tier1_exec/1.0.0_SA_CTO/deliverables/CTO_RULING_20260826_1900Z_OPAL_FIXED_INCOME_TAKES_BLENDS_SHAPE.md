# CTO RULING 2026-08-26 ~19:00Z -- opal_fixed_income takes the blends' shape (msg 73148 + amendment 73157)

**Context:** A9 NOT MET 9/12, `errors=['global']` (CVO verdict @68f61a11c5). Mechanism source-confirmed
by COO/~A: global's `by_model` is built by iterating the fixed tuple `GLOBAL_MODEL_KEYS`
(`dim_mdpf_aggregate_aua_timeseries.py:127`, fold at `:2449`), derived from the crosswalk's
`CANONICAL_MODELS`; `opal_fixed_income` has no entry, so cottonwood's `model_aua` carries the recovered
dollars while global's `by_model` cohort sum does not -- delta exactly -$8,442,396.92. COO 73109 s.4
routed the shape ruling to this seat; (b)-gate withdrawn by CVO 73131 + COO 73141 on ~K's zero-edge
census (70 .py in runners_49f, 0 crosswalk refs, positive control perfrp=38).

## THE RULING (operative, delivered as msg 73148 to COO/~T/~A/CVO/MSTR, 5/5 DELIVERED)

**YES -- `opal_fixed_income` takes the `opal_blend_5050_*` shape:**

    ModelEntry("opal_fixed_income", None, "Fixed Income", "model", False)

- NO eclipse_id / orion_id (it has neither; both lookup maps filter None, crosswalk :135-140).
- display_name "Fixed Income" MUST equal the `GLOBAL_ACCOUNT_DIST_DISPLAY` value at crosswalk :206
  (prefix-dropped convention :205). One name, two maps, already coherent.
- Appended EXPLICITLY to `GLOBAL_MODEL_KEYS` at `dim_mdpf_aggregate_aua_timeseries.py:127`.
- `served=False` is the TRUE claim (not in the 49F SmartX projection); `served=True` would be both
  inoperative (the `model_id` conjunct fails independently) and false.
- `cohort_class="model"` is NOT a Primary claim: `CORE_MODEL_KEYS` (:148-151) additionally requires
  `served and model_id`, so Fixed Income does NOT enter the `model_aua[]` summand set -- arithmetically
  correct (model_aua already carries the dollars; by_model is the short side) and taxonomy-correct
  (Andrew ruled Fixed Income CUSTOM; L2 Primary five untouched).

**Rule 24 record (value-add to CANONICAL_MODELS):** axis = canonical model registry keyed by
`model_key`, domain = every model key any MDPF artifact serves or folds; EXCLUSIVITY by the :316-317
dup asserts; GRAIN one logical model; INTENT `served` keeps one meaning and False is true here;
STATE: DESIRED until pin advance, APPLIED at the lambda, EXERCISED only by the re-grade.

## THE ADDITION THIS SEAT FOUND (nobody else had named it)

**crosswalk :156-159 derives `BLEND_MODEL_KEYS` on `m.model_id is None` -- the new entry MATCHES it.**
Unedited: BLEND_MODEL_KEYS becomes 3, the self-test `:322` (`== 2`) FAILS, in BOTH crosswalk homes.
Denominator: `git grep BLEND_MODEL_KEYS -- '*.py'` = 6 sites, ALL crosswalk-internal, ZERO external
consumers. Remedy = Rule 24(iii), not assert-relaxation: the predicate MEANS "the 2 inflection-leg
blends" (its comment, :155) -- tighten to `m.model_id is None and m.eclipse_id is not None` (blends
carry eclipse_id 28/29; Fixed Income none). The :322 assert then passes UNCHANGED -- itself the
control. Do NOT relax the assert.

## SCOPE -- FOUR FILES, ONE CLOSURE (per CVO 73126 geography + COO 73138, + this seat's additions)

1. `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` -- ModelEntry + :156 predicate tighten
2. `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py` -- identical
   edit; post-edit control: diff of the two copies = 0 bytes (the QUIET limb -- arm this one)
3. `dim_mdpf_aggregate_aua_timeseries.py` -- :127 append + BOTH stale comments in the same edit
   (:126 "by_model{9}", :2440 "union (9 = ...)" -- and :2440 stops saying "union")
4. `build_cottonwood_mdpf_slice.py:9-12` -- the known-false "Verified ... EXACTLY the union" claim
   corrected to what is true (fixed tuple; verified over 49F+INF only; falsified by cottonwood 08-26)

`0.4.0_DS_ClientPlatform~T` executes; verifies every path/line itself at edit time (73075 instruction).

## PRE-EDIT GATES

(i) ~A's 73115 covered-set test runs SAME TURN as the edit on ~T's post-fix qa_local artifact
    (dates where opal_fixed_income is None AND in covered_dates AND label != interpolated_estimate);
    non-empty = the gap=True set, accounted BEFORE landing. The ONLY unexercised behaviour left.
(ii) Pre-registered delta: global identity on 2026-08-25 closes by EXACTLY +$8,442,396.92; any other
     delta = STOP.
(iii) 462-date count -- **SATISFIED by amendment 73157**: CVO 73155 measured the gate ACCUMULATES
      (`:1942-1950`, seven lists, raise after the full loop), so tonight's `1 violation` IS the
      complete census. No tail. ~R seating on the count released.
      Rider: the summary line prints 5 of 7 category counters (`pincot`/`provfails` uncounted) --
      re-grade counts `FATAL:` lines, never the summary numbers; 10-line cap noted. Legibility defect
      named, rides the next deliberate touch, not this pin.
(iv) Minimal-pin at FILE grain onto the running vintage; interlock @af92b0afa3 governs; four files
     lifted BY NAME; D1_CATVIEWS NO-SHIP unbroken.

## RECORD ITEMS

- This seat's 73031 propagated the one-token-off filename (`mdpf_aggregate_aua`) in a constraint --
  struck; the constraint re-attaches to `dim_mdpf_aggregate_aua_timeseries.py`.
- Serve state unchanged: A9 NOT MET stands; Andrew's conditional-YES @666fe25b0c did NOT activate and
  does not auto-reactivate on a later green. After the edit + re-grade, Andrew gets the fork at this
  terminal priced on real evidence. Drive-now governs the fix (zero served-plane exposure); the serve
  word remains his alone.
