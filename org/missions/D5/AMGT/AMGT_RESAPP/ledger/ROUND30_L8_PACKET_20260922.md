# AMGT_RESAPP round 30 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** SITEZ after `56f34cd1ed`, LOCAL; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).
**Written:** 2026-09-22 ~22:0xZ.

**DRAIN-END, complete: 8 of 8 terminal, 0 open.** Seven `complete`, one `superseded` (rk-122 -- see s.1, the flip is
an issuer act with its reason on the record face, not a grade).

Round 30 is the Lenovo trial's WAVE 2, issued as ONE slug of seven cells @`bf5c280e48` on the CTO's round-29 analysis
(msg 24328) and its ruling, plus `rk-123` as a routed `direct_act` addendum @`010ef26367`. Decomposition s.38, s.38x,
s.38y.

⭐ **The headline is not a trial stage. It is that Andrew's Security Analysis page stopped being blank** -- and the
round's dominant defect (s.4) is one class, it is this seat's, and it was caught twelve times by workers rather than
once by the issuer.

## 1. Round state, final

| cell | drain | terminal state | second instrument (this seat's own) |
|---|---|---|---|
| rk-116 Lenovo model block (LIVE) | `d807972562` + `eaceef15b3` | complete | First spawn STOPPED at AC0 -- **my cut error**: I built its worktree before the CTO half was signed, so the pair was unreadable (W116-S1). Rebuilt from HEAD, re-spawned, **0 of 6 requests spent on the false start.** Landed: first-ever `bestdata` bronze, 15 `BEST_*` figures, `fiscal_year_join {method: fiscal-period (fye_join), max_gap_days: 93}`, `currencies {quote: HKD, reporting: USD, mixed: true, converted: false}`, 228/228 `currency_basis`. |
| rk-117 Lenovo daily price (LIVE) | `56f34cd1ed` | complete | See s.2 -- verified tonight on the SERVED reader, not the worker's object diff. |
| rk-118 Lenovo filings battery | `b8585b189d` | complete | ONE run, `UNRESOLVED-SOURCE` with a per-step reason. A clean negative: the battery reached no source and said which step failed and why, rather than inventing one. |
| rk-119 Lenovo Seeking Alpha | `1d6c739a43` | complete | **AC0 REFUSED the pull and that is the success.** No measured ADR/ratio basis existed for a HK-listed name, so the cell spent **0 of 10** sized requests and stopped. A refusal that costs nothing is the cheapest possible outcome and the criterion fired exactly as written. |
| rk-120 identity cleanup + schema gate | `5201fad3b3` | complete | Needed **two issuer amendments**, both mine (`ae4b5d95ba`, `c69c628c9f`). Amendment 1 was **WRONG** and the worker refused it (W120-S3, BLOCKING) -- see s.4.2. |
| rk-121 battery keys read identity | `2facd37a47` | complete | `keys_from_crosswalk` now reads the landed identity block. |
| rk-122 amgt edge behavior | `8cae02a96a` (by `0.0.0_AB_MSTR~Z`) | **superseded** | AC0/AC1/AC2 PASSED here; AC3/AC4 are the apply + live re-read and were **designed to be unreachable from this seat's lane** (s.6 of the order says so). Carried by rk-123. Its patch and plan are what rk-123 applied, and `W122-S1` was independently corroborated by the AE seat on a different instrument. |
| rk-123 amgt edge behavior APPLY | `6c41b5d70e` (by `0.7.0_AE_CloudOps`) | complete | See s.3. |

## 2. The live acts and their denominators

### rk-117 -- Lenovo dense daily `PX_LAST`, the act under a pair

- **Landed:** `s3://opal-data-harvest/bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/20260922T212739Z.json`.
- **Content, read by ME from the object itself, not from the worker's report:** **2459 rows, 2459 DISTINCT dates**,
  `2016-01-04 .. 2025-12-31`, first `PX_LAST` 7.46, last 9.26, **0 null prices**, range 3.6-13.6, and the per-year
  counts are 243-248 across ten years -- the HKEX trading-day shape. Fields are exactly `{date, PX_LAST}`.
- ⭐ **THE FRESHNESS CLAIM, RE-TAKEN ON A DIFFERENT INSTRUMENT.** The worker proved it by a pre/post object diff. I
  proved it through **the SERVED code path itself** -- `scoped_amgt._bloomberg_bronze_stamps` over the whole swept
  key set: **134 keys swept, 37 securities carrying a stamp, and EXACTLY ONE (`992_HK_Equity`) carries tonight's
  stamp.** 992 reads `20260922T212739Z`; BABA is unmoved at `20260916T201821Z`. So the "36 of 36 other partitions
  unmoved" control is corroborated by a route that shares no code with the worker's check.
  ⚠ **My first call of that reader returned `{}` and I nearly reported it.** I had fed it SECURITY keys; it takes S3
  OBJECT keys (`:3189`). A wrong-argument empty dict reads exactly like "the route sees nothing." I corrected the
  input, not the conclusion. Same shape as the CTO's own wrong-prefix zero in msg 24418.
- **Budget:** 2 of 2 sized requests, never exceeded (1 predecessor probe + 1 pull; see `W117-S5`, which is the
  criterion contradicting its own pair).
- **Ledger:** `20260922T2126Z_amgt-rk117-lenovo-daily-px`, opened before the pull, 1 leg, **CLOSED at 21:31:22Z and
  verified BY ME IN THE SHARED TREE AFTER THE DRAIN** -- 7 `.open_deploys/` entries, none of them rk117. That read
  is deliberate: it is the control `Z-S234` says is the only sound one.
- **Branch: KEEP.** No rollback trigger fired.
- ⚠ **THE IRREVERSIBILITY, restated because it survives this round** (CTO @`3c9c171dd4`): the served route takes a
  **MAX**, so a bad object cannot be undone by publishing a better one -- only a delete lowers the stamp, and that is
  destructive and human-word-reserved. The mitigation is therefore a PRECONDITION, and it is why the content read
  above (rows, range, first/last) is in the acceptance and not merely in the report.

### rk-116 -- the model block

First-ever `bestdata` bronze for the estate. The figure-labelling ruling (Q2: label reporting vs quote currency,
convert NOTHING) is satisfied: `currencies.converted` is `false` and `mixed` is `true`, with 228 of 228 figures
carrying a `currency_basis`.

## 3. rk-123 -- the page defect is FIXED, and this is the round's real deliverable

Every `/api/scoped/amgt/*` request now reaches the portal API instead of falling through to the SPA origin.

| path | BEFORE | AFTER |
|---|---|---|
| `/api/scoped/amgt/lists` | 200 `text/html` 1000b | **401 `application/json` 51b** |
| `/api/scoped/amgt/freshness` | 200 `text/html` 1000b | **401 `application/json` 51b** |
| `/api/scoped/amgt/security/BA_US_Equity/thesis` | 200 `text/html` | **401 `application/json`** |
| `/api/scoped/amgt/security/992_HK_Equity/thesis` | 200 `text/html` | **401 `application/json`** |
| `/api/scoped/advisor-intelligence/ping` (control) | 401 `application/json` | unchanged |
| `/api/general/health` (control) | 401 `application/json` | unchanged |

**THREE INSTRUMENTS, and they are genuinely different:** the AE seat's own AC0-AC5 (29 behaviors, amgt LAST at index
28, `auth-validator-edge:20`, 8 of 8 fields identical to the investor-reporting template, WAF 0 of 18 rule-fields
moved, 12 of 12 probes across two reads after the propagation window); the CTO's independent live GETs at 21:11:02Z;
and this seat's read. **Causation is settled by the AE seat's MUTANT:** `/api/scoped/amgtXYZZY/lists` and a nonsense
route BOTH still return `200 text/html`, so the flip is the new behavior **MATCHING**, not a global change.

⚠ **THE LIMIT, which is the actor's own and I am carrying it rather than letting it drop: this changed ROUTING, not
AUTHENTICATION and not CONTENT.** An authenticated end-to-end render of `BA_US_Equity` then `992_HK_Equity` has NOT
been taken and is nobody's cell. If auth is also broken the page stays empty -- and `Z-S227` (0 of 5 tabs carry an
`isError` branch) is exactly why that would again be **SILENT**, as it was for this outage.

⭐ **AND THE CTO's msg 24418 CHANGES WHICH NAME TO TEST ON.** Measured per tab: `BA_US_Equity` is **7 of 7**
populated; `992_HK_Equity` is **5 of 7** and has **NO `drafting/v1` document at all** -- and Thesis is the DEFAULT
tab (`SecurityAnalysis.tsx:45`). **So a viewer opening Lenovo lands on the one tab Lenovo has no document for.** The
ABSENT state is handled and should say why, but it will look sparse, and after an outage that looked identical,
"sparse" is easy to misread as "still broken." **Confirm the fix on `BA_US_Equity`.**

## 4. For the grade -- the defects, and the large one is mine

### 4.1 THE DOMINANT DEFECT OF THE ROUND, filed as `Z-S235` with its denominator

**A literal invocation written into a task order and never RUN against the tool that consumes it.**
**12 instances, 6 sub-classes, across 6 of the 8 orders** (rk-116, 117, 118, 119, 121, 123; absent from rk-120 and
rk-122). Eleven are rowed; the twelfth is the row gate refusing `W123` because a SEAT's row carries no `W`.

- **(a) leg kind `s3-key`, which `deploy_ledger.py` does not accept** -- `W116-S4`, `W118-S1`.
- **(b) `cw._read_pool_latest().get("records")`, but it returns a 2-tuple** -- `W119-S1`, `W121-S1`.
- **(c) `python <script>` sets `sys.path[0]` to the SCRIPT's directory, not cwd** -- `W117-S1` (AC0's helper) and
  `W117-S3`, which reached **the cell's MAIN limb-2 script**, not just a probe.
- **(d) the deploy-tool surface in rk-123** -- `Z-S231` (the literal `safe-apply` cannot complete: terraform prompts,
  stdin is null, dies `error asking for approval: EOF` having applied **nothing**), `Z-S232` (`.open_deploys/` not in
  `<paths>` while the order's own mandated tool writes there), `Z-S233` (AC5 calls a `status` subcommand that does
  not exist -- argparse rc=2, so **AC5 could never PASS**).
- **(e) a criterion contradicting its own arithmetic or its own pair** -- `W117-S4` (`HEAD~1 HEAD` cannot span a cell
  whose execution crossed two sessions with amendments between) and `W117-S5` (**AC0's literal re-probe would have
  spent a SECOND live request against a cell whose own never-widen halves cap it at 2 and name over-spend as a
  ROLLBACK TRIGGER**).
- **(f)** the `W123` row-id shape.

⛔ **THE SHARPEST PART IS NOT THE COUNT -- IT IS THAT (a) AND (b) EACH APPEAR IN TWO DIFFERENT ORDERS OF THE SAME
SLUG.** I did not make those mistakes twice; I **copied one unexercised line into a second order** while cutting
seven at once. Width at L6 multiplies a cut defect by the fan-out.

**Every one was caught by the WORKER, at execution time. None was caught at the cut.** The workers were right every
time -- no worker executed a broken literal and reported success. The cost is worker time, two issuer-amendment round
trips and one full re-spawn, not a wrong result.

**REMEDY ADOPTED AT L6 FROM THIS COMMIT** (in `Z-S235`'s `disarm_owner`, and it disarms the five ARMED members this
seat owns -- `W117-S1/S3/S4/S5`, `W119-S1`): before a slug is issued, **every literal invocation in every order in
that slug is RUN ONCE by the issuer** and its rc plus first output line recorded in the issuance commit; a non-zero
rc that is not the criterion's OWN expected refusal is a cut defect fixed before issuance. **COST:** N invocations per
slug, once. **NON-APPLICATION:** an invocation whose purpose is to run against a state that does not exist until the
cell acts -- exercised for SHAPE (imports, argparse, tool surface), never for outcome.
⚠ **AND THE REMEDY IS HONESTLY SCOPED: it covers 11 of 12.** Sub-class (e)'s `W117-S5` is a contradiction between a
criterion and its own never-widen pair; a shape-only run would not surface it. I name it uncovered rather than fold
it in.

The CTO reached this class independently over rk-123's four instances (msg 24414: *"A template is not verified by
having worked once; it is verified by being run."*). `Z-S235` is the round-wide denominator behind that sentence.

### 4.2 `rk-120` ISSUER AMENDMENT 1 WAS WRONG, AND THE WORKER REFUSED IT -- `W120-S3`, BLOCKING

I instructed `build_universe.py:918`'s `write_pool` call to also pass `document=document`. That union document
(names/holdings/union/both/resolved) would **FAIL `crosswalk.schema.json`**, whose `additionalProperties` is false
over `records`. **The worker refused and was right.** Amendment 2 @`c69c628c9f` struck it; `add_security.py:180`
keeps the change. ⭐ **A worker refusing an ISSUER's written instruction, on evidence, is the control working** -- I
want that graded as such and not as friction.

### 4.3 MY DISPATCH GAP -- no row, so I put it here

I created five round-30 worktrees and spawned only **three** workers. `rk-122` -- the cell Andrew was actually
waiting on -- and `rk-117` sat unworked for roughly **25 minutes** before I noticed. Nothing detected this: a
worktree with no worker in it is invisible to every instrument I run. Disclosed to the CTO and MSTR at the time.

### 4.4 `Z-S234`'s MIRROR, which the estate should keep

The AE seat ran `deploy_ledger.py close` inside a LINKED WORKTREE; the tool mutates the tree it runs in, the close was
never committed, `worktree remove --force` destroyed it, and **the shared tree was left reading `Status: OPEN`** while
a commit message and an acceptance row both asserted CLOSED. It caught this ITSELF by re-reading the shared tree after
the drain, repaired with identical proofs, and **corrected the row in place rather than overwriting it.**
⭐ **CLAUDE.md NEVER-2 already says the ABSENCE of a `.open_deploys/` entry is not evidence during a worker deploy.
This is its exact MIRROR: the PRESENCE of a CLOSE in a worktree is not evidence either.** Both directions are now
measured on the same surface. I applied it tonight on rk-117 (s.2) and it is the estate's generalisation, not this
cell's.

### 4.5 Carried, unchanged by this round

- **`Z-S230`, the Bloomberg credential exposure: ARMED.** The CODE is fixed (`ab796d0520`); four committed artifacts
  still carry the username. **No scrub** (destructive git on a shared branch, human word per act) and **rotation
  DEFERRED and owned** -- it is not atomic and would break the live Bloomberg legs mid-flight. CTO @`dbb9fedb27`.
- **`W117-S2`, the premise defect, and it is NOT sub-class 4.1.** I cut rk-117 as "bronze-only, no served reader, so
  no pair"; `scoped_amgt.py:3108` lists `histdata_daily_px` in `_BLOOMBERG_BRONZE_REQUESTS`, which the served
  `/freshness` route reads. **The writer census cannot falsify a claim about READERS.** The worker refused the live
  leg (BLOCKING), I wrote and signed a COO half and two amendments, the CTO signed @`3c9c171dd4`. Cost of the check I
  did not run: one reader census of the prefix across the adapter.
- **`Z-S225`** is answered by rk-120. **`Z-S226`** (the CDN behavior) is **REMEDIATED BY rk-123** and I believe its
  standing should flip -- but remediation rows are yours, so I name it rather than write it.
- **`Z-S227`** (0 of 5 tabs carry an `isError` branch) is the **single highest-value open item** and has no cell. It
  is why this outage was silent and why the next one would be.

## 5. Trial stages, stated so a blank tab is never inferred from silence

| stage | state |
|---|---|
| 1 identity | **SERVED** (round 29) -- `crosswalk/v1/2026-09-22.json`, composite FIGI `BBG000BG4QC6`, `field_errors` empty |
| 2 model block | **SERVED** (rk-116) -- first `bestdata` bronze, 15 `BEST_*` figures |
| 3 filings | **UNRESOLVED-SOURCE** (rk-118), with a per-step reason -- a clean negative, not a failure |
| price axis | **SERVED** (rk-117) -- 2459 rows, 10 years |
| Seeking Alpha | **REFUSED AT AC0** (rk-119), 0 of 10 requests -- no measured ADR/ratio basis for a HK-listed name |
| THESIS | ⛔ **NOT SERVED** -- `992_HK_Equity` has no `drafting/v1` document (CTO msg 24418). **It is the page's DEFAULT tab.** |
| 9 publications | ⛔ **NOT SERVED** -- 0 Lenovo objects in SA bronze/silver, verified by me; per the CTO's msg 24290 this stage now FOLLOWS `AMGT_HARVST` rather than running on today's harvester |
| Exec Management | **0 for Lenovo** -- consistent with the roster-shape gap already on record (7 of 33 names), not a new finding |

**Neither NOT-SERVED stage is a defect of round 30.** Both are stages the trial has not run. I would rather they be
named here than inferred from a blank tab later.

## 6. What this seat asks of L9/L10

1. **Grade `Z-S235` as the round's finding** and tell me whether the adopted remedy is the right shape before I cut
   round 31 under it -- it changes my L6 cost, and if you want it narrower or wider, now is when that is cheap.
2. **Flip `Z-S226`** if you agree rk-123 remediates it. Remediation rows are yours; I have not written one.
3. **Grade 4.2 as a control succeeding**, not as friction: a worker refused an issuer instruction on evidence and was
   right.
4. **`Z-S227` needs an owner and a cell.** It is the reason a second fault would be as silent as the first, and it
   currently sits in nobody's round.
5. **Carried to the CTO, not a cell tonight** (msg 24402): read rk-116's landed `bestdata` object for the BEst means
   and counts, then diff the NEXT vintage for the same name -- that answers substrate card S1 on data the firm
   already pays for, before any vendor subscription is considered.

**Push state: LOCAL on SITEZ @`56f34cd1ed` plus this commit; the push is `0.0.0_AB_MSTR~Z`'s (LD-0522).**

-- `2.0.0_SA_COO~Z`
