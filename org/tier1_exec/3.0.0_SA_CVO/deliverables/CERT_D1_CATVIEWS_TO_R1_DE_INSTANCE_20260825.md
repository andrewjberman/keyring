# CERT -- `D1_CATVIEWS.TO-R1-DE` proof instance

**Certifier:** `3.0.0_SA_CVO` · **Date:** 2026-08-25T20:5xZ · **Verdict: CERTIFIED**
**Subject:** ONE task order's proof instance from ONE lane --
`org/tier2_senior/0.4.0_DE_ClientPlatform~C/deliverables/D1_CATVIEWS.TO-R1-DE_PROOF_OF_SPEC.json`
**Requested by:** `2.0.0_SA_COO` (71387). **Executing seat `0.4.0_DE_ClientPlatform~C` is NOT LIVE** --
this is a cert against a FILED instance, not a seat request. No seat was or is held on it.

---

## WHAT I RAN, AT MY OWN SEAT

`python .tools/proof-of-spec-check.py <instance>.json D1R1DE-AC1..AC9` @ HEAD `dfc492aa83`:

```
structural=jsonschema | acceptance rows=9 | violations=0
alignment-frame: decomp id space = 32 distinct cell id(s)
alignment-forward-1  (criterion -> cell):   9/9 criteria carry >=1 cell_ref
alignment-forward-2  (cell_ref -> decomp):  8/8 distinct cell_refs resolve
alignment-backward   (declared cell -> criterion): 8/8 declared cells reachable
VALID   rc=0
```

**BOTH DIRECTIONS CLOSE, WITH DENOMINATORS: 9 criteria / 8 cells / 0 unmapped / 0 untraceable.**
All 9 acceptance rows read PASS. Controls: planted mutant `FIRED-AS-EXPECTED` (TS2339 on the
substituted discriminator); determinism `STABLE` (same fixture, same ref, identical figures).

**AC9 re-derived at the artifact, not accepted from the instance** -- all five portal commits
(`760504f0` `4034239c` `d1f8f38a` `cd2f059c` `7def244d`) carry author `0.4.0_DE_ClientPlatform~C`
and `git branch -r --contains` puts each on **origin/DEV AND origin/PROD**. 5 of 5.

---

## ⛔ LAYER 5 -- THE JUDGMENT THE TOOL EXPLICITLY DOES NOT MAKE

The checker states its own limit: *"Whether the TO's declared set IS the decomp's complete
criterion-bearing set is a CVO cert judgment (enforcement layer 5), NOT asserted here."*

**THE DE LANE'S RENDER-SIDE SET IS COMPLETE.** Every view-plane cell in the decomp is owned and
discharged: `D1-h-v1` `v2` `v3` `v4` (the view tree), `D1-h-p1` (presence predicate), `D1-c-1`
(consumed) + `D1-c-2` (empty fallback), `D1-inv-4` (render-half invariant). 8 of 8. The cells
correctly NOT here -- the gold/registry cells, `D1-f-1`, the `h-r*` and `h-c*` families -- are
named in the TO's `<decomp_context>` sibling as reads and exclusions, which is the right shape.

⛔ **BUT THE PROJECT'S id SPACE IS 32 CELLS AND THIS TO CARRIES 8. `D1-i-1` IS CARRIED BY NO TO --
AND THE DEFECT IT WAS WRITTEN TO CATCH HAS NOW LANDED.**
`D1-i-1` is *"THE TWO CODE CHANNELS, ENUMERATED -- which channel each D1-touched module reaches, and
which one the scheduled floor actually executes."* Independently, and without reference to that cell,
`0.4.0_DS_ClientPlatform~N` measured today (71414) that `mdpf_category_registry.py` reaches **NO**
channel: absent from `build_package.py`'s PACKAGE list (grep 0, positive control 1), absent from both
Lambda layers (2,980 and 1,507 members scanned), top-level unguarded import at
`mdpf_gold_consolidator.py:84`, zero `except ImportError` in the file.
**The decomp ANTICIPATED this class, the cell was carried by nobody, and the defect materialised.
That is the layer-5 finding, and it is the second time a `D1-i-*` gap has been named in a cert on
this project** (the first was mine on the DS instance, @`989a92e806`).

---

## ⛔ WHAT THIS CERT DOES **NOT** SAY -- READ BEFORE CITING IT

**A CERT'S SCOPE IS PART OF THE CERT. A CITATION THAT DROPS THE SCOPE IS NOT A SHORTER TRUE
STATEMENT -- IT IS A DIFFERENT AND LARGER CLAIM.** This project has already had one cert
(`989a92e806`, the DS instance) cited as though it certified the PROJECT; that was corrected at
12:25Z. Do not repeat it with this one.

1. ⛔ **IT DOES NOT SAY D1_CATVIEWS IS DEPLOY-READY. IT IS NOT.** Per 71414, building
   `mdpf-gold-lambda` at any pin carrying the six D1_CATVIEWS commits yields a package that raises
   `ModuleNotFoundError` at import -- every invocation, every scope, every artifact type, before a
   line of handler code runs. **Packaging and render-correctness are INDEPENDENT: a module can be
   perfectly correct and unshippable.** This cert is about the render.
2. **It does not assert a SERVED-artifact read.** The instance says so itself and I am ratifying that
   honesty, not papering it: AC2-AC8 prove the RENDER against the contract at ref `23271aac64` using
   fixtures built by exercising the emitter in an isolated extraction. `category_views` is emitted
   but UNPUBLISHED. `D1-c-1` is complete AT THE CONTRACT PLANE, not at the served plane.
3. **It does not close D1_CATVIEWS round 1 as a project**, and it does not discharge the DS lane,
   `D1-i-1`, or `D1-i-2`.
4. **It does not clear any downstream gate by itself**, and it is not a PROD promote (DT lane).

**THE ACCURATE CITATION FORM:** *"TO-R1-DS instance certified @989a92e806; TO-R1-DE instance
certified @<this commit>; D1-i-1/i-2 carried by no TO; NOT deploy-ready per 71414."*

---

## DECLARED, NOT DEFECTS

The instance declares 5 exclusions and 5 surprises rather than burying them, including
`D1-h-v2`'s Alternatives limb as **NOT-YET-EVALUABLE** (no firm carries Alternatives AUM -- 0 of 3),
and AC6's 404 branch as unexercisable locally (local dev returns 401). **A declared
non-evaluable limb is a stronger instance than a manufactured green**, and I am certifying it as
declared, not despite it.

`0.4.0_DE_ClientPlatform~C` caught the missing cert themselves at 12:24Z and **verified rather than
updating their summary.** That is the behaviour the fabric wants and it should not have cost them a
day; the eight-hour wait was a routing gap, not their error.

---

## ADDENDUM 2026-08-25 ~21:1xZ -- THE LAYER-5 CLAIM, MEASURED RATHER THAN ASSERTED

The body above says *"`D1-i-1` is carried by no TO."* True, and now **measured with its denominator
and a firing positive control**, which the original statement did not carry.

Decomp id space **31 cells**; all **6** D1_CATVIEWS TOs scanned over FULL TEXT -- not only
`<decomp_ref>`, because the four legacy TOs (D1b/c/d/e) predate the `cell_refs` convention and
declare ZERO ids, so a structured-block-only scan would have manufactured false orphans.

```
claimed by >=1 TO's decomp_ref/cell_refs ............. 25 of 31
remainder covered in TO PROSE as boundary/exclusion:
  D1-f-1   DE(1) DS(1)   the 15/85 ruled node -- DARK, CTO remit
  D1-g-1   DE(1) DS(2)   boundary: the 5-enum is NOT re-opened
  D1-g-2   DE(1) DS(1)   boundary: siblings
  D1-inv-5 DE(2)         cited as the CONSTRAINT behind this lane's own "NOT CLAIMED" note
ZERO MENTIONS IN ANY OF THE 6 TOs, ANYWHERE:
  D1-i-1   THE TWO CODE CHANNELS, ENUMERATED
  D1-i-2   THE LAMBDA RE-PIN + TF APPLY
POSITIVE CONTROL: D1-h-v1 -> 8 mentions across 6 TOs | D1-b-1 -> 9.
```

**IT IS TWO CELLS, NOT THE WHOLE (i) SURFACE, AND THE NARROWER READ IS THE MORE DAMNING ONE.**
`D1-inv-5` was NOT dropped -- this very lane cites it twice, and it is exactly WHY the instrument
declares *"NOT CLAIMED: a served-artifact read."* **The (i) surface partially worked: its INVARIANT
was honoured by a lane that then correctly declined to overclaim. The two cells never cut are the
two that required an ACT** -- enumerate the channels, and make the change RUN.

⛔ **AND THE HONEST LIMIT OF THIS CERT'S OWN CATCH:** the body named `D1-i-1` **because
`0.4.0_DS_ClientPlatform~N`'s 71414 had already measured the packaging defect an hour earlier.**
The layer-5 limb RECOGNISED a defect already on the table; it did not discover it. **Layer 5 is a
judgment the certifier makes by hand, per TO, and nothing compels it** -- a different session, or
this one on a busier turn, certifies 9/9 and says nothing. That is the same structural weakness
`2.0.0_SA_COO` named in 71452, one level up, and it is not repaired by this cert.

**PROJECT DISPOSITION (not mine, recorded so this cert is never read against it):** D1_CATVIEWS is
**NO-SHIP / DEPLOY-BLOCKED** -- `2.0.0_SA_COO` 71452, `1.0.0_SA_CTO` 71449. Two further defects were
exercised against live data through the production entry point after this cert was issued: an
unsatisfiable exact-float-equality predicate (`$0.01` on `$2.03B`, relative 5e-12, where the sibling
producer uses `RECON_TOLERANCE = 0.01`), and a `shaped_cv` build at `:1190` preceding the emit loop
at `:1228` so **one scope's refusal aborts all four**. **This cert certified the RENDER and said so;
it neither anticipated nor covers either defect.**
