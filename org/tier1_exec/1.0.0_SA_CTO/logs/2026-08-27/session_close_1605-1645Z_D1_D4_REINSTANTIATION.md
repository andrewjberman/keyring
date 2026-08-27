# 1.0.0_SA_CTO~Z — REINSTANTIATION LOG: everything a fresh CTO~Z needs to begin D1 and D4

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE, VALIDATE

⛔ **READ THIS FIRST: YOU ARE THE FRESH SEAT. I AM THE SEAT THAT WAS CLOSED OUT.** Andrew-direct
2026-08-27, VERBATIM: *"i will close you all out and reinstantiate you fresh."* You have **zero**
memory of this session. Everything below is written on that assumption. The prior log
(`session_close_1350-1605Z.md`, @`58b42c0cf6`) is the narrative; **this one is the operating manual.**

---

## 0. WHAT YOU ARE STARTING

**D1 and D4 execution.** Andrew: *"Ok we are ready to begin on D1 and D4."* His priority set is
**D1 / D4 / D8 (Model Portfolios)**; **D6, D7, D9 are STOOD DOWN by his word** — do not work them.

---

## 1. THE ORDERING EDGE THAT IS NOT IN THE REGISTER — READ BEFORE PLANNING ANYTHING

**E1 — D1 BEFORE D4.** Recovered from the pre-rename title (`"ETF positioning variant (3-8wks,
behind D1)"`) and corroborated from the other end by D4's own live stance (*"the four ETFs join D1's
taxonomy as SMA-category members — one registry serves both"*).

⛔ **GRAIN, AND GETTING THIS WRONG COSTS THE MOST: E1 BINDS D4's TAXONOMY/CANON LAYER ONLY.**
D4's ingest, pull and producer legs consume no D1 output and are **NOT** behind D1. **Reading E1 at
directive level would idle D4's 8 open TOs behind a directive that has 2.**

**E2 — D1 BEFORE D3** (the laptop's). Outbound obligation; gates nothing here.

⛔ **THE REGISTER NO LONGER CARRIES EITHER EDGE.** The 2026-08-27 rename deleted the title
parentheticals. **A grep for "D1" inside D4's row RETURNS HITS — both are about ADJACENCY, not
order.** So the search that looks for this returns a confident false positive.
**Ordering evidence:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_SITEZ_DIRECTIVE_DEPENDENCY_ORDER_20260827.md` @`57ae04ffef`
**Do NOT edit the register** — `org/missions/.register-owner` names the laptop MSTR (LD-0341).

---

## 2. D1 — TWO HALVES, DIFFERENT STATES

### 2a. `D1_NAMEDISCOVERY` — decomp done, awaiting certification
- **Decomp:** `workflows/atom_decomposition/runs/d1-namediscovery/20260826T214534Z/DECOMP.md` (149 lines,
  20 cells / 16 criterion-bearing / **0 criteria — NOT-YET-EVALUABLE, no TO cut**).
- **PRD:** `org/tier2_senior/0.4.0_DS_ClientPlatform~R/deliverables/D1_NAMEDISCOVERY_PURPOSE_PRD_v1.md` (v2 @`958c8e4487`)
- **Project:** `org/projects/D1_NAMEDISCOVERY.json`
- **Certifier `3.0.0_SA_CVO`; alternate base `1.0.0_SA_CTO`.**
  ⛔ **DO NOT SELF-CERTIFY.** I had an Andrew-APPROVED rec to certify as alternate and **declined it**
  when `3.0.0_SA_CVO~Z` proved live — the rec's premise was *"no CVO seat on this fabric"* and it was
  false. **An alternate is for an UNAVAILABLE primary, not an unobserved one.** Check liveness first.
- ⭐ **STALENESS RE-DERIVATION — ALREADY DONE, DO NOT REPEAT.** The decomp's §4 says the CE claim has a
  half-life and re-derivation belongs to the certifier. I ran it: **all three scope forks (grain, ETF
  population, input span) are UNMOVED** — everything touching the name space (`20260826_1756Z`,
  `_1806Z`, `_2107Z`) predates authoring and IS its declared basis. Denominator: 8 Andrew-directs since.
  **ONE staleness stands:** the header reads `placement LAPTOP`, superseded ~2h later by
  `ANDREW_DIRECT_20260826_2352Z_PLACEMENT_MAP_D8_AND_MP_TO_SITEZ.md`. **D1 IS SITEZ.**

### 2b. `D1_CATVIEWS` — the register lies about this one
⛔ **`org/projects/D1_CATVIEWS.json` says `dep_stage: EXECUTING`, `blocking: "None."` — AND THE LANE
THAT DID THE WORK DECLARED IT NO-SHIP.** Lane close-out (note: filed under the **BASE** folder, not `~F`):
`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-08-26/session_close_0825T2324-0826T0308Z_LANE_N_d1catviews_cut.md`

**Both assigned lanes are GONE — and it was a CLOSE-OUT, not an abandonment** (MSTR~Z measured
0 processes / 0 markers / NOT REGISTERED; the lane's own log: *"Nothing owed, nothing held, nothing
in flight"*). **So the register's 08-26 "work IN FLIGHT" clause protects a state that had already ended.**

**FOUR ITEMS WERE ESCALATED. THEIR STATE AS OF CLOSE-OUT:**
| item | owner | state |
|---|---|---|
| Finding 2 — RULING: cent float noise vs real upstream inconsistency | `2.0.0_SA_COO` | ✅ **CLOSED** — see below |
| the control proving the fix still refuses a MATERIAL break | `2.0.0_SA_COO` | ✅ **BUILT AND EXERCISED, 40/40** |
| the 08-26 13:30Z acceptance + the **D1-i-2 hold** | **`1.0.0_SA_CTO` = YOU** | acceptance RUN (§4); **hold NOT lifted** |

⭐ **FINDING 2 IS CLOSED — and I nearly wrote it into this log as ORPHANED.** `2.0.0_SA_COO~Z` stopped
me mid-write. Recorded because the correction is more useful than the fact:
- **Ruling settled:** `org/surprise_channel/D1_CATVIEWS/INVESTIGATION_v1.md`, disposition **GRADUATED**,
  disarmed same-turn with every limb independently verified against the sibling-producer positive control.
- **Repair landed IN SOURCE:** `data/mdpf/scripts/gold/mdpf_category_registry.py:1019-1021` —
  `TOL_CENTS = round(RECON_TOLERANCE * 100)` with integer-cent comparison; `:62` imports
  `RECON_TOLERANCE` **from the sibling producer** (one tolerance, two spellings, never re-coined).
  The exact-float-equality defect at `:992` is **GONE**.
- **Control EXISTS and was EXERCISED:** `data/mdpf/scripts/gold/tests/recon_predicate_control.py`
  (13,918 B) — **40 invocations (10 magnitudes × 4 sweeping arms), 0 mismatches.**

⛔ **AND THE TRAP IN THE OLD WORDING, which is why this paragraph exists:** a laptop CTO tick log
records the ruling as *"RECON_TOLERANCE form adopted"*. **That is the DIRECTION. The LANDED
ARITHMETIC IS INTEGER CENTS.** *(CVO's 08-26 row: "Direction upheld, ARITHMETIC REPLACED with integer
cents.")* **A seat implementing the tick log's wording would build a float tolerance that was already
superseded.** Read the source, not the tick log.
*(`COO 72259` is NOT on this fabric — the only estate hit is that tick log, i.e. the third-seat source
I said not to close on. COO~Z closed it on first-party artifacts at three layers instead. That is the
right way to close something you cannot cite directly.)*

---

## 3. D4 — CERTIFIED WITH FINDINGS; TO-MINTING MAY PROCEED

- **Decomp:** `workflows/atom_decomposition/runs/etfs-satellites/20260827T160438Z/DECOMP.md` (23 cells)
- **Certification:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoZ_ETFS_SATELLITES_DECOMP_CERTIFICATION_20260827.md` @`205546c65c`
- ⚠ **THE DECOMP WAS CORRECTED TWICE ON ITS OWN DAY (@`a1c38e8c53`, @`8e188d4f42`). If you find a v1
  copy anywhere, it is wrong.** A fresh reader cannot tell corrected text from original — these are
  the corrections, and **the withdrawn versions are the intuitive ones you will re-derive if you don't know:**
  - **MEMBER SET IS NINE**, not ten. Andrew: *"Opal Ultra Short Term is not a satellite, that was
    erroneously included in a screenshot..."* **Roster membership is not satellite membership.**
  - **IS-A vs HOLDS-A**, not a one-account heuristic. Andrew: *"Some SMA that has a blend of a
    Satellite and Opal Model is not a Satellite, they merely are allocating to a Satellite."*
  - **The Rule 24 (iv) "FAIL" was WITHDRAWN as an over-application** (Andrew caught it). **(iv) PASSES.**
    A value merely not-built-yet is an unbuilt feature, not a stability defect. ⛔ **I amplified the
    withdrawn version to CVO~Z before it was retracted — do not resurrect it.**

### ⛔ 3a. THE FINDING THAT SURVIVES EVERYTHING AND MUST REACH THE TO CUT
**THE REMEDY THAT DELIVERS THE `satellites` MODE DOES NOT DELIVER ITS FIRM GATE.** PRD S6 measured
**ZERO firm-id references in the entire Positioning directory**. `SAT-b-1` (mode, DE alone) and
`SAT-c-1` (firm gate, DE+AE) **MUST be separate TOs with separate owners.** Bundled you get a mode
rendering for **EVERY firm**, or a gate with nothing behind it — **and neither failure announces
itself.** On a multi-tenant surface the first is a client-facing exposure that ships green.

### 3b. MEMBERSHIP HAS NO COMPUTABLE PREDICATE — measured, not suspected
CVO's F1: `SAT-inv-2` (predicate over the roster) and the corrected `SAT-b-2` (IS-A vs HOLDS-A) are
**jointly unsatisfiable** — the roster page is FLAT, and the only roster-evaluable fields are the two
the cell rules out. Their candidate remedy was `hierarchy.children[]`, **marked INFERRED. I falsified it:**
```
84 detail files, 121 child nodes, MAX DEPTH REACHED: 1
child nodes whose id IS a canonical satellite id:  0
POSITIVE CONTROL: 18 of 18 distinct child ids resolve to top-level models -- the test works
```
`Opal Sat 50+ 15% cash` holds `Opal Intermediate-Term` 0.50 / `Opal Short-Term` 0.15 /
`Opal Ultra Short-Term Income` 0.35 — **it never references `Opal Satellite 50`.**
>> **Andrew's criterion is a BUSINESS description, not a structural relation in this feed. The blends
   hold the satellites' INGREDIENTS, not the satellites.** <<
**MY REC (a recommendation, NOT a certification):** v1 ships the **declared nine-name list as data**
with a named owner and review trigger, and `SAT-inv-2` says on its face it is a declared set, not a
derived predicate. **If CVO ruled otherwise, CUT TOs TO THEIR TEXT, NOT MINE.**
⚠ **ONE LEAD NOT CHASED:** `hierarchy.components` was `list[0]` — **empty on every model read.** An
array named `components`, universally empty, on a composition question, is either unused or
unpopulated. **Different remedies.** One look before v1 is final.

---

## 4. THE 13:30Z ACCEPTANCE — RUN, VERDICT RECORDED, HOLD NOT LIFTED

Full evidence: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_D1_D4_START_POINT_EVIDENCE_20260827.md` @`d88235f793`

| | 08-26 13:30:37Z | 08-27 13:31Z |
|---|---|---|
| writes / errors | **8 / 2** | **16 / 0** |
| scopes | 49f, inflection only | **all four** |

`cottonwood: ValueError: no canonical by_model key for Cottonwood model 'Opal Fixed Income'`
`global: SystemExit: global fold SKIPPED: contributing leg(s) ['cottonwood'] failed this cycle`

**Global did not fail on its merits — it was SKIPPED because cottonwood aborted.** That is Finding 2's
*"one scope aborts all four"*, demonstrated in production.
⛔ **DO NOT LIFT D1-i-2 ON THIS.** What fixed the mapping is **UNESTABLISHED** (a green run cannot
distinguish *someone made the reviewed edit* from *the input changed shape*), and **Finding 2's
ordering defect is untouched — the next scope failure aborts the fold again. The hold is against a
CLASS.**

---

## 5. STATE OF THE FABRIC + WHO OWNS WHAT

| seat | holds |
|---|---|
| `3.0.0_SA_CVO~Z` | both certifications (D4 done-with-findings; D1_NAMEDISCOVERY pending). **Their state is authoritative — I deliberately kept no copy.** |
| `2.0.0_SA_COO~Z` | MDPF_COTREMEDIATION (D8) stage-3 decomp; Finding 2 ruling; the orphaned control |
| `0.0.0_AB_MSTR~Z` | tier 0. Integrator — **only they push.** Laptop parity. |
| `0.7.0_AE_CloudOps~Z` | **CLOSED OUT by Andrew. Do not route work there.** |

**Fabrics are AT PARITY:** `origin/SITEZ` **0 behind CLOUD** (was 1,122) as of merge `5edabd600a`.

---

## 6. LIVE ITEMS WITH NO OWNER — these die unless you carry them

1. ⛔ **THE CONFLICT-GUARD FALSE-POSITIVE CLASS.** The gold guard counts `_provenance.process_time`
   / `.trigger` / `meta.generated_at` as **business-diff**, so **every same-day re-run conflicts on
   every pre-existing key BY CONSTRUCTION.** Measured twice: 9 conflicts (6 pure provenance), then
   3 more on the very next run (**all** provenance). **Its detection is right, its classification is
   too broad, and its `reland()` is coarser than its detection — it takes ALL conflict rows, no
   per-key scoping.** Real conflicts hide among manufactured ones.
2. **`partner_roster.json` — FOUR HOMES, THREE CONTENTS. PRODUCTION IS STILL ON `D+2`.**
   | home | sha256 | cadence |
   |---|---|---|
   | `data/mdpf/config/partner_roster.json` | `4c104d9b` | **T-1** (corrected) |
   | `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/partner_roster.json` | `af44aaad` | D+2 |
   | `s3://opal-data-mdpf/code/scripts/gold/partner_roster.json` | `af44aaad` | D+2 |
   | `mdpf-gold-lambda` **bundled in the deployment package** | `e86e4631` | D+2 |
   Fix = **three acts**: emitter edit, F-3 publish, **Terraform redeploy** of `mdpf-gold-lambda`.
   ⚠ **IMPACT UNESTABLISHED:** `_cot_carry_policy` computes its window from `max_lag` **alone** and
   treats cadence as provenance *"NEVER as an addend"* — **so the deployed `D+2` may be inert to
   computation. Determine that before calling it a data fix.**
3. **`transactions` / `realized` are D-0 same-day feeds with NO roster rows at all.**

---

## 7. COMPILER TOOLS

| tool | result | note |
|---|---|---|
| `comp-find -i` | PASS | located the D1_CATVIEWS artifacts + the `D1-i-2` corpus (50 hits / 27,196 files) |
| `comp-which` | PASS | startup exercise |
| rail markers | n/a | 4x `# rail-checked:` — config-field fan-out, roster-copy enumeration, scheduler hunt, lambda field semantics |

**Gap found (routed, unbuilt): NO comp-tool models CONFIG-FIELD FAN-OUT** — which consumers read a
given config file and which copy each resolves. **That gap is exactly what let four diverged roster
homes persist.** `comp-aws` models resource edges, not intra-payload field flow.

---

## 8. THE THREE HABITS THAT PAID, AND WHY THEY BELONG IN YOUR HEAD

Not lessons — **operating instructions**. Each caught a real error today.

1. **VALIDATE AGAINST THE SYSTEM, NOT ITS DESCRIPTION.** Seven errors in one session, all one class:
   a partner-to-partner control void across cadences; the roster's declared `D+2` (falsified by write
   times); a docstring's single-authority claim (falsified by two hashes); a census of the wrong
   EventBridge plane (**`aws events` and `aws scheduler` are different APIs that do not overlap**);
   `git log --since` given a UTC cutoff (**it takes LOCAL time** — returned a clean zero for my own
   commits); hand-dispatching four lambdas when `/mdpf-refresh` already existed; and treating
   `MAX_SESSION_AGE_DAYS=7` as measured when Andrew says *"we do not even know if the cookie would ever die."*
2. **A ZERO NEEDS A POSITIVE CONTROL.** The `children[]` falsification is only sound because 18 of 18
   child ids resolved to something. **Without that, "0 matches" and "my matcher is broken" are identical.**
3. **PRINT THE DENOMINATOR AND NAME THE PLANE.** Every number above carries what it is out of.
   ⭐ **And the one to generalise: a CONFIG-PROVENANCE FIELD IN THE OUTPUT ARTIFACT is what made four
   diverged roster homes visible.** No census found them; the manifest recorded
   `config_hashes.partner_roster_sha256`, it matched nothing expected, and reading the deployed
   package settled it. **Make the artifact state which config it consumed.**

---

## 9. BLOCKERS

**None.** Nothing in this lane is blocked on another agent. All open items above have either a named
owner or an explicit ORPHANED marker.

## 10. NEXT STEPS

- **[YOU]** cut D4 round-1 TOs against **CVO's certified text** — mode and firm gate SEPARATE (§3a).
- **[YOU]** the D1-i-2 hold, and whether to chase what fixed the `Opal Fixed Income` mapping.
- **[`3.0.0_SA_CVO~Z`]** `D1_NAMEDISCOVERY` certification; the F1 ruling (declared list vs predicate).
- **[`2.0.0_SA_COO~Z`]** the D8 (`MDPF_COTREMEDIATION`) stage-3 decomp. **Finding 2 and its control are CLOSED** (§2b) — do not re-open them.
- **[Andrew]** nothing outstanding at him from this lane.
