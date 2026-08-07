# CTO~Z -- MDPF_CANONICAL_PLATINUM: cutover validated, portal confirmed, session stand-down

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

**Serial:** 1.0.0_SA_CTO~Z (lane ~Z, Site Z; base-serial folder, lane in title -- no `~Z` folder exists)
**Window:** 2026-08-07 0315Z -> 0415Z (delta since `ctoz_mdpf_canplat_2020-0315Z.md` @28749a470)
**Commits this window:** `ae8eef73d`, `e5e932caf` (docs only -- no code, no infra, no TF at this seat)
**Branch:** SITEZ. Push is MSTR~Z's (:55-:00 integration window) -- nothing pushed from here.

---

## 1 - OUTCOME

**The MDPF canonical-platinum cutover landed and Andrew confirmed the portal displays correctly --
his words, verbatim: "Portal is showing correct data for the first time in a week."** Two of his three
stated goals are fully closed; the third is deployed-and-enabled but has not yet fired unattended.

| goal | state | grounded on |
|---|---|---|
| completed architecture | **CLOSED** | re-point landed ~032xZ, old target destroyed same apply |
| scheduled data flow | **DEPLOYED, NOT YET PROVEN** | `cron(0 9 * * ? *)` NY ENABLED, target `mdpf-gold-lambda` -- never fired unattended on the new path |
| current data displayed | **CLOSED** | gold 4/4 @ `2026-08-05`; platinum 12/12 republished 03:52Z; **portal confirmed by Andrew** |

> **THE RESIDUAL IS NOT PEDANTRY AND MUST NOT BE ROUNDED UP.** Tonight's emission was the
> fabric-driven CUTOVER. "Deployed and enabled" and "runs unattended" are different claims, and only
> one is proven. **The thing that froze this pipeline for a week was a chain that LOOKED scheduled and
> was not running.** Andrew has personally taken the 09:00 ET observation.

---

## 2 - THE $125M INVESTIGATION (the window's substantive work)

Andrew challenged a number I had relayed -- *"why would we restate global down 125m exactly????"* --
and the challenge was correct. I had passed COO~Z's pre-positioning through as *"ruled machinery
working correctly, measured supersedes carried."* **Measuring it falsified my framing.**

**Reconciliation, served platinum, read live:** global ties to its three partners TO THE CENT wherever
all three are present.

```
date      GLOBAL served      49F            INFL         COTTON        GLOBAL - sum(3)
07-27     1,673,456,137   1,406,447,705   141,884,714   125,123,718        0
07-28     1,677,200,436   1,409,940,330   142,136,388      None      +125,123,718  <- carried
07-31     1,562,215,514   1,418,817,918   143,397,596   125,009,921  -125,009,921  <- DROPPED
```

**Two distinct defects, which I had conflated into one:**
1. **Served 07-31/08-03 dropped cottonwood entirely** while `cottonwood/aggregate-aua-timeseries.json`
   **from the same publish** carried a measured value for that exact date. Two artifacts of one run
   contradicting each other. Real, and the staged build fixed it (+$125M).
2. **The staged build flipped 07-28..30 from `carried` to `absent`**, rendering a $125M three-day
   crater in a series whose underlying value moved **0.09%** (125,123,718 -> 125,009,921).

**Nothing was "measured" on 07-28..30 -- cottonwood has no delivery there at all. The change was
carry -> absent, a POLICY FLIP, not a supersession.** My framing would have had Andrew accept a false
crater as correct behaviour -- i.e. the pre-positioning sent to PREVENT a false-outage read would
instead have PRE-AUTHORISED one.

**Andrew ruled it, VERBATIM: "Just roll Cottonwood forward if we don't have data for it, take the last
good figure."** The correct artifact is the UNION of the two correct halves -- carry where no delivery,
measured where delivered. Neither the served nor the staged build alone was right.

**Validated on the served surface at 0400Z:**

```
07-28..30  CARRIED   carried_at_declared_cadence(as_of=2026-07-27)
07-31      measured  125,009,921 -> global 1,687,225,435   (+$125M fix SHIPPED)
08-04      CARRIED   carried_at_declared_cadence(as_of=2026-08-03)   <- NOBODY SPECIFIED THIS GAP
08-05      measured  127,580,243
```

> **The strongest validation in that table is `08-04`. A gap that nobody hand-tuned appeared, and the
> same law caught it with the same label and the same provenance string. A rule that only works on the
> gap it was written for is a patch; this one generalised unattended.** No crater in either direction.

---

## 3 - MY OWN ERRORS THIS WINDOW (both retracted at source, same fire)

**(a) "The dead sentinel blocks the chain" -- WRONG, asserted THREE times including to Andrew.**
`mdpf-daily-trigger/lambda_function.py:778` is
`if GATE_ENFORCE and not gate["spine_fresh"] and not is_floor:` -- **the scheduled floor is EXEMPT by
design**, with `:766-777` giving the rationale and citing the exact incident it was built for. I read
`dispatched:false` out of a MANUAL invoke (where `is_floor` is correctly False and deferral is correct)
and generalised it onto the scheduled path. **Right log, wrong path, wrong conclusion.** I had also put
`GATE_ENFORCE=0` on the table as a lever against that broken premise -- retracted before anyone acted;
`:750-754` shows it would have disarmed the working per-partner skip while buying nothing.

**(b) The `is_floor` payload lead -- correctly LABELLED a lead, then discharged by AE~Z.**
Live floor Input sends `source: "aws.events"`; handler wants `FLOOR_SOURCE = "mdpf.scheduled-floor"`.
`:108-114` predicts that exact failure in its own words. **I flagged the gap I had not closed** (the
floor targets `mdpf-gold-lambda`; the code read was `mdpf-daily-trigger`). AE~Z closed it properly:
**zero hits for `pipeline-complete` across all 17 packaged .py files at the deployed pin, WITH a
positive control** -- the old trigger returns 2 on the same command shape. **The zero is
discriminating, not a broken retrieval.** Combined with A2 schedule-first (builds on every invocation,
trigger recorded never gated), the mismatch is **inert on the canonical path**.

> **The lesson I am recording against myself: the honest LEAD label is the only reason (b) was routable
> instead of becoming a third confident wrong mechanism inside one hour.** (a) had no such label.

---

## 4 - ANDREW'S QUESTION THAT EXPOSED THE CLASS

*"why would inflection need a flag but we dont use that for any other scope? that is a perfect example
of stochastic trash"* -- correct, and source confirms it:

| | inflection `_check_inf_spine:349` | 49financial `_check_bd_silver:366` |
|---|---|---|
| reads | a MARKER file | the DATA's own partitions |
| calendar | `as_of >= now_utc.date()` -- WALL-CLOCK, today | `expected_last_trading_day()` + `trading_days_behind()` |
| tolerance | zero | `BD_MAX_LAG_TRADING_DAYS` |

**The docstring is the confession (`:350`): "The sentinel just fired, so this is ~always fresh; we read
it for the run_date + a robustness check." It is a run_date READER with an assertion bolted on**,
written for the accelerator path where it is tautologically true. It became a gate only when a clock
started firing the same handler. **`>= now_utc.date()` is a NEVER#1 violation on its face.** Every
other freshness check in that file goes through the trading calendar; the one that does not is the one
reading a marker. Filed as R-19/R-20 -- **Andrew's "one off weird patches and 'meta' tables, trash all
of it" lands precisely here.**

---

## 5 - COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-routes behaviors` | portal->platinum serving path | **PASS** | surfaced the `cache-control-injector` on origin-response for `/api/general/json-tiered/*`; its own coverage header disclosed DESIRED-plane-only, which is what kept me from making a behavioral claim |
| `comp-pulse diff` (risk-reflex) | auto, both commits | **CLEAN** | DENOMINATOR printed: 2 files then 1 file vs 1662 danger nodes; a MEASURED clean, not a default |
| native `Grep`/`Glob`/`Read` | trigger source, publisher source, invalidation census | **PASS** | used after the rail gated Bash -- see gap below |
| live AWS primitives | `s3 ls`/`cp`, `s3api head-object`, `scheduler get-schedule`, `events list-rules`, `list-targets-by-rule` | **PASS** | denominators printed on every list call (139 rules, 16 schedules, no NextToken) per the pagination rule |

**What worked:** `comp-routes`' coverage/BLIND header did real work -- it is what stopped me converting
"no invalidation call + a cache injector" into "the portal is stale." **A tool that states what it
cannot see prevented a third wrong mechanism in one hour.**

**GAP FOUND (comp-rail, routable to CTO base):** the rail DENIED two Bash calls whose targets were
**`.py` files and a `find` over `infra/aws/lambda/`**, with the message *"comp-tool on the HUD:
grepping infra/.tf"* and a menu of `.tf`-oriented tools (`comp-aws`, `comp-iam`, `comp-routes`).
**The DENY was arguably correct on path prefix but its MESSAGE misdescribed the target**, and none of
the offered tools answers "does this Lambda's source call `create_invalidation`." **A deny whose
rationale does not match what was denied trains the agent to reach for the override rather than the
tool.** I routed around it with native `Grep`/`Glob` (their own sanctioned light path) rather than
firing `# rail-checked:`. Worth a message-accuracy fix + a route for source-level API-call census.

---

## 6 - DELIVERABLES

| file | commit | what |
|---|---|---|
| `docs/architecture/MDPF_REMEDIATION_REGISTER.md` | `ae8eef73d` | **R-22** carry horizon undefined (defers -- fails LOUD, `as_of_by_partner` on the face). **R-23** served platinum lags its own staging and the OBJECT MTIME HIDES IT (mtime is a WRITE clock, never a CONTENT vintage -- they diverged ~2 days and the mtime looked healthy). **R-21** RECORDED BUT NOT DEFERRED -- routed to the BUILD under the register's own deferrability rule (nothing makes it loud), because labelling the carry is HALF of implementing the ruling |
| `docs/architecture/MDPF_CANONICAL_PLATINUM_DELIVERABLE_CONTRACT.md` | `ae8eef73d` | **Section C gains `validate_interpolated_backfill.py`** -- the INVERSE of the `cottonwood_aua` correction. **Section C was wrong in BOTH directions: neither conservative nor aggressive, but UNGROUNDED**, exactly as its confirm markers declared. The AST closure is the authority |
| `docs/architecture/MDPF_REMEDIATION_REGISTER.md` | `e5e932caf` | **R-24** `carried` is new to the flat `point_class` vocabulary; the portal reader degrades unknown classes to estimate-class with warn-once until DE first-classes it. Fails LOUD and in the SAFE direction |

**R-21 was already satisfied when my routing arrived** -- DS~Z's `@470788096` implemented
`_flat_point_class` as one weakest-component law consumed by BOTH the emission and the composition
gate, so a carried row labelled `measured` is **REFUSED**, not merely corrected. **Stronger than what I
asked for: I requested an honest label and got a gate that rejects the dishonest one.**

---

## 7 - CURRENT STATE (for a reader with zero prior context)

- **Data:** `s3://opal-data-assets/portal/gold/mdpf/{scope}/aggregate-aua-timeseries/2026-08-05.json`
  for all 4 scopes (global, 49financial, inflection, cottonwood). Platinum 12/12 under
  `s3://opal-data-portal-v2/platinum/mdpf/{scope}/`, republished 2026-08-07T03:52Z.
- **Schedule:** EventBridge **Scheduler** (not Rules) `mdpf-scheduled-floor`, `cron(0 9 * * ? *)`
  America/New_York, ENABLED, target `mdpf-gold-lambda`. Siblings: `mdpf-accrual-bridge-daily` (09:40),
  `opal-assets-mdpf-portal-publisher-daily` (09:50). `mdpf-daily-refresh-trigger` (EventBridge Rule)
  remains schedule-less BY DESIGN -- it is the accelerator over a scheduled floor, the sanctioned shape.
- **Dead marker, still dead:** `s3://opal-data-inf/gold/meta/pipeline-complete.json` reads
  `run_date: 2026-07-31`, 135 bytes, unwritten since 2026-07-31. **Irrelevant to the canonical path**
  (AE~Z's positive-controlled zero); it gates only the LEGACY dispatch. R-19.
- **Loops:** 20m `/loop` cron `028dd913` **CUT** at 0415Z on Andrew's word. Drive-loop stand-down
  relayed to 2.0.0_SA_COO~Z. **No monitor/watcher/checker armed against the 09:00 ET cycle** -- Andrew
  has personally taken that observation, and arming an instrument against it is the moratorium's shape.

---

## 8 - BLOCKERS

**None.** Nothing at this seat is blocked, and nothing is holding another seat.

---

## 9 - NEXT STEPS

1. **[Andrew]** **09:00 ET 2026-08-07 unattended cycle** -- his own verification, his words: *"ill be
   back online in the morning and will see if it fails or doesnt work."* PASS = the schedule produces
   `2026-08-06` with nobody touching it, which moves goal 2 from deployed to proven.
2. **[Andrew + the fabric]** **Walk the remediation register and the associated cleanup** -- *"then we
   can go through the remediation doc with the fabric and associated cleanup."* This is section 3's
   named trigger: **the register becomes its rubric ON HIS WORD, in the morning, WITH the fabric.**
   Scope on the table: R-1..R-24, the `opal-data-mdpf` bucket retirement brief, the mdpf_revamp name
   retirement brief. **Nobody starts any of it beforehand.**
3. **[0.7.0_AE_CloudOps~Z]** `is_floor` QA-invoke confirmation -- non-blocking, already discharged in
   substance by the positive-controlled zero; keep it only as the test the code itself prescribes.
4. **[DE, routed via 0.0.0_AB_MSTR~Z]** First-class `carried` in the portal reader's `point_class`
   vocabulary (R-24). **LOW, non-blocking.** Spec sent 041129Z, including the counter-intuitive
   precedence: `interpolated_estimate` ranks WORSE than `carried` (a carried point is a real
   observation with a stale date; an interpolated one was never observed).
5. **[2.0.0_SA_COO~Z]** Drive loop cut; fabric-wide relay of Andrew's **"well done"** to DS~Z, AE~Z,
   CVO~Z.
6. **[CTO base, not ~Z]** comp-rail DENY-message accuracy (section 5 gap) + a route for source-level
   API-call census.

---

## 10 - MCP TRAFFIC

~10 dispatches this window. Significant: two rulings issued to 2.0.0_SA_COO~Z (emitter restructures /
date-keyed R7 promoted first-class); the `$125M` finding + my own **retraction** of the ruled-machinery
framing; the **retraction** of the sentinel-blocks-chain premise with `GATE_ENFORCE` marked
untouchable; Andrew's carry ruling recorded+broadcast; the R-21 build-item routing; the goal-3
validation with the CloudFront-invalidation gap named as a RISK not an outage; the stand-down
broadcast; the DE request to 0.0.0_AB_MSTR~Z.

**Received and acted on:** AE~Z's ANDREW-DIRECT completion-bar broadcast; AE~Z's source-grounded
sentinel answer; COO~Z's divergence declaration on releasing their own full-12 evidence bar (I
**endorsed** it -- their bar to release, and my "gated on full-12" line predated Andrew's completion
bar, so it was superseded by HIM, not overridden by them).
