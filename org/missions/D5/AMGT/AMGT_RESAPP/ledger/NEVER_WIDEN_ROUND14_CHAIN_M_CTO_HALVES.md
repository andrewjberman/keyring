# NEVER-WIDEN CO-SIGN -- CTO HALVES. Round 14, chain M. One section per co-signed cell.

**Signer:** `1.0.0_SA_CTO~Z` (DRAFT -- NOT SIGNED, NOT COMMITTED). **Counterpart:** `2.0.0_SA_COO~Z`'s COO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_M_COO_HALVES.md` @`9a6aa12da2` (branch
`coo-amgt-r14-issue-20260918`), the APPLIED/EXERCISED plane. **This plane:** DESIRED -- the SOURCE DIFF and THE
PRODUCER'S OWN RULE, read from source at `HEAD` = `97341c3df2` (branch `SITEZ`).

**Vintage discipline.** Every `path:line` below was printed from the working tree at `97341c3df2`; `git status --porcelain`
over `integrations/bloomberg/research/model_block_pull.py`, `lib/research/` and `infra/aws/terraform/harvest/` returned
EMPTY, so the bytes read ARE the HEAD bytes for every file cited. Where a claim could not be exercised from this seat
(a live AWS read, a producer run), it is written **UNVERIFIED** with the reason. Nothing below uses "proof", "root cause"
or "definitively".

**Standing note on the round-14 orders.** The task orders for `rk-34`..`rk-37` are NOT on
`coo-amgt-r14-issue-20260918` at `9a6aa12da2` (`git ls-tree -r` over the project subtree returns no order file for any of
the four; the COO's own commit message says "the orders themselves are NOT in this commit"). **So every statement below
about what a cell CHANGES is read from the PRD's ratified contract plus the source it must touch -- never from an order
this seat has not seen.** Where the order could re-cut a rule, that is named as the open edge, not smoothed over.

**Where the two halves disagree.** Four disagreements and three unnamed-branch gaps are recorded below, at
`M-DISAGREE-1..4` and `M-GAP-1..3`. **`M-DISAGREE-1` is the one that breaks a rollback**, and no cell of this chain
should be spawned against the current COO text for `rk-36`/`rk-37` until it is answered.

---

## 1. `AMGT-rk-34` -- the unit map covers every name; re-derive over the 33 (R14-M1; FWD-10, M1)

### 1.1 THE ACT

`model_block_pull.py derive` over the 33 crosswalk keys, in 11 invocations of at most 3, each landing
`s3://opal-data-harvest/derived/model_block/<key>/<NEW stamp>/model_block.json`. No Bloomberg request, no Lambda,
no Terraform. **AGREES with the COO half's THE ACT exactly**, and the "at most 3 per invocation" shape is not a
convention -- it is a refusal in the producer: `main()` raises `SystemExit("REFUSE: more than 3 securities requested
(F2/G-24 cap)")` at `integrations/bloomberg/research/model_block_pull.py:509-510`. 33 keys therefore CANNOT be done in
fewer than 11 invocations.

### 1.2 THE SOURCE DIFF

| what the cell must touch | cited at HEAD | what the change makes the code do |
|---|---|---|
| the unit/sign lookup | `integrations/bloomberg/research/model_block_pull.py:302-318` (`_resolved_unit`), `:321-336` (`_resolved_sign`) | today both read `field_map.json` and, for a name the map does not carry, `_resolved_unit` returns the literal pointer string at `:318`. The cell makes the map carry every name so the pointer branch stops being taken. |
| the map's location | `:286-288`, `_FIELD_MAP_PATH = Path("org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/field_map.json")` | a **RELATIVE** path, resolved against the process cwd by `Path.exists()` at `:295`. See 1.5. |
| the derive itself | `:369-461` (`stage_derive`), landing key built at `:453` | unchanged in shape: read raw back from S3 (`:375-376`), join on fiscal year (`:381`), write a NEW stamp (`:452-454`). |

**The decisive line, quoted:**

```
:318        return "SEE field_map.json (per-field, per-security MEASURED unit -- not yet built)"
```

The PRD says the same thing independently: *"for every other name `_resolved_unit` (`:300-316`) falls back to 'not yet
built' and the check face refuses. All 348 measured refusals are this one missing entry, not bad data."*
(`org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md:855-858`, `C-UNIT-MAP-MEASURED`, v0.11 amendment). The PRD and
the source agree; the COO half does not (1.4).

### 1.3 THE PRODUCER'S RULE, EVERY BRANCH

Read from `cmd_derive` (`:488-501`), `stage_derive` (`:369-461`), `_latest_stamp` (`:206-214`) and `s3_put_if_absent`
(`:184-198`).

| branch | what it WRITES | what it does NOT write |
|---|---|---|
| **SUCCESS** | one new `derived/model_block/<key>/<derived_stamp>/model_block.json` per key (`:452-454`) | nothing else. No raw key, no crosswalk key, no ledger row -- `record_run` is called ONLY by `stage_pull` at `:246`; `stage_derive` never calls it. |
| **EMPTY** (the raw object exists but carries nothing for this security string) | **still one new stamp, with `figures: []`, `fiscal_years: []`, `fiscal_year_row_count: 0`** -- there is NO guard between `header_vals = ref.get(security, {})` at `:378` and the unconditional `s3_put_if_absent` at `:454` | nothing refuses. rc = 0. |
| **PER-KEY FAILURE** (no raw stamp under the prefix; a `get_object` miss; a JSON parse error) | **nothing for that key** -- the exception propagates out of `stage_derive` through `cmd_derive`'s **unguarded** `for` loop at `:490-499` | **and nothing for any key LATER IN THE SAME INVOCATION.** There is no `try`/`except` in `cmd_derive`. |
| **KEY COLLISION** (the derived key already exists) | nothing | `s3_put_if_absent` raises `RuntimeError("REFUSING TO OVERWRITE existing key (STORE_CONTRACT rule 1): ...")` at `:194-197`. In practice unreachable, because `derived_stamp = utc_stamp()` at `:452` is minted fresh. |

**The shared rule the COO half states once for the chain is CONFIRMED at source:** every derived write is a new stamp
under its key and nothing is overwritten (`:452-454` + `:184-198`); the adapter serves the NEWEST stamp because
`_read_model_block_pool` paginates the whole `<key>/` subtree and takes `candidates[-1]` of the sorted
`.../model_block.json` set (`lib/research/api/scoped_amgt.py:1005-1015`), which for the producer's zero-padded
`YYYYMMDDTHHMMSSZ` stamp IS newest-by-time. **So the COO half's "blast radius of a derive is a new newest stamp for the
keys named, and the rollback is delete the new stamp" is CORRECT and rests on `:1005-1015` + `:452-454`.**

### 1.4 WHICH BRANCH EACH COO OUTCOME RESTS ON

- **Branch MAPPED** -- rests on the map carrying the name. Covered.
- **Branch STILL-ABSENT** -- the COO half says *"the row is written ABSENT with its reason"* and that **AC3 counts
  `unit: ABSENT` rows, denominator 33**. **`M-DISAGREE-1(a)`: THE PRODUCER AT HEAD NEVER WRITES THE TOKEN `ABSENT`
  INTO A `unit` FIELD.** The unmapped branch returns the pointer sentence at `:318`. The `unresolved` list
  (`:390-396`, `:420-422`) is a different thing entirely -- it records a missing **VALUE**, with reasons
  `header_errs.get(mnemonic, "empty/no value returned")` and `"empty/no value returned"`, and a figure with a missing
  unit is NOT in it (that figure lands in `figures` with the pointer string as its unit).
  **Consequence, and this is the reason it matters rather than a wording quibble:** if the cell does not ALSO change
  `_resolved_unit` to emit a real `ABSENT` token, **AC3 reads `0 of 33` on BOTH branches** -- the mapped one and the
  unmapped one -- and the criterion is a green that cannot discriminate (CLAUDE.md Rule 22, DISCRIMINATION). The COO
  half's two branches are then indistinguishable by the instrument it names.
  **This does not widen the blast radius** (the rollback is the same delete either way), so it does not block the
  co-sign; it blocks the CRITERION. Owner: the L6 cut.
- **Branch a derive FAILS** -- the COO half says *"no stamp lands for that key, the previous stamp stays newest; the
  worker prints the key."* The first two clauses are CORRECT. **`M-DISAGREE-2`: "the worker prints the key" is not the
  producer's rule.** `cmd_derive:490-499` has no exception handling: the traceback is the only output, the process
  exits non-zero, and **up to two further keys in that same invocation are silently skipped**. The COO half's own
  11-invocation shape means a single mid-batch failure can leave 2 keys underived with no line naming them. Blast
  radius UNCHANGED (fewer writes, never more); the COO half's rollback covers it unchanged. The correction is to the
  worker's expected output, not to the signature.

**`M-GAP-1` -- A FOURTH BRANCH THE COO HALF DOES NOT NAME.** The EMPTY branch above lands a new stamp carrying ZERO
figures, and that stamp becomes the served newest for its key (`scoped_amgt.py:1005-1015`), so the Model tab for that
name goes from figures to none **with rc = 0 and no refusal anywhere**. The most likely way to reach it is an
identifier-form slip: `stage_derive` indexes the raw document by the security string it was HANDED (`ref.get(security,
{})` at `:378`, `hist.get(security, [])` at `:380`), while the pool key is the underscore form from `security_key()`
at `:172-173`. **Hand the derive `CAT_US_Equity` where the raw document is keyed `CAT US Equity` and it writes an empty
block over a good one, quietly.** The COO half's rollback (delete the new stamp) DOES cover the state; what is missing
is that this branch exists at all, and that the worker must therefore assert `fiscal_year_row_count > 0` per key rather
than read rc = 0 as success. Named here so the pair covers all four branches.

### 1.5 WRITER CENSUS CROSS-CHECK

**COO half: N = 1 writer of "newest model_block stamp per key". I measure N = 1. AGREED.**

My instrument, and it is a DIFFERENT one from the COO's (`comp-schedule` + the round-13 analysis): `comp-find` over the
repo corpus, denominator **66,307 files scanned** (`corpus=all`, 508,169 ephemeral-floor excluded, 3,066 binary, 1
unreadable), two sweeps:

1. `comp-find 'derived/model_block'` -- **781 hits**, bands `HEAD=44 DEF=3 SURFACED=49 CONFIG=340 TEST=5 DOC=340`. The
   **DEF band is the deciding one and it is COMPLETE at 3**: `lib/research/api/scoped_amgt.py:172`,
   `lib/research/peers/universe.py:79`, `lib/research/scores/run_scores.py:70`.
2. `comp-find 'derived/\{ENGINE\}|put_object\(Bucket=BUCKET'` -- of 100 hits, the only one landing on this prefix is
   `model_block_pull.py:453` + `:198`.

Then I read each of the three DEF holders to classify reader-vs-writer, because a shared prefix constant is not
evidence of a write (Rule 22, GRAIN):
- `scoped_amgt.py:172` -- reader (`_read_model_block_pool`, `:980-1050`, `list_objects_v2` + `get_object` only).
- `universe.py:79` -- reader (`model_block_pool_index`, `:242-267`, `list_objects_v2`; `read_model_block_from_pool`, `:269`).
- `run_scores.py:70` -- reader (`:106`, builds a list prefix).

**No scheduled producer**: UNVERIFIED on the applied plane from this seat (a schedule read is an AWS call I am
constrained from making). On the DESIRED plane the repo carries no Terraform schedule, task definition or Lambda naming
this prefix -- the only scheduled resource in `infra/aws/terraform/harvest/` is `chatter-axis-schedule.tf`, a different
engine. I take the COO's `comp-schedule: 0` on the applied plane; **noting per Rule 22 that my arm and the COO's are on
DIFFERENT planes, so this is corroboration, not repetition.**

### 1.6 WHAT THIS HALF DOES NOT COVER

Everything the COO half excludes (any `pull`; any key outside the 33; any adapter redeploy), **plus two this plane can
see and the applied plane cannot:**
- **the field-map file's own move.** `_FIELD_MAP_PATH` at `:286-288` is a **relative** path into a worker's deliverables
  folder, and `C-PRODUCTION-HOME` puts the map beside its producer (PRD `:855-857`). If the cell RELOCATES the file, the
  relocation is a repo act outside this signature, and -- separately -- **a derive run from any cwd other than the repo
  root silently takes the `:318` pointer branch for EVERY field**, because `Path.exists()` at `:295` resolves against
  the process cwd. A worker in its own worktree must run from that worktree's root. This is not a blast-radius item; it
  is a way to produce 33 vacuously-passing blocks.
- **any change to `_resolved_unit`/`_resolved_sign` return VALUES** (see `M-DISAGREE-1(a)`): a new `ABSENT` token is a
  new value in a served field and is a schema change under Rule 24(iv), not a free edit.

---

## 2. `AMGT-rk-35` -- rolling history window, validation names only (R14-M2; FWD-1, FWD-16, M2)

### 2.1 THE ACT

One Bloomberg pull each for `CAT US Equity`, `CSL AU Equity`, `6861 JP Equity`, landing 6 raw objects, then a derive
landing 3 derived objects, plus `record_run` for three landings. **AGREES with the COO half.** The key shapes are
confirmed at source: `raw/{VENDOR}/{sec_key}/{stamp}/refdata.json` and `histdata.json` at
`model_block_pull.py:242-243`; `derived/{ENGINE}/{sec_key}/{stamp}/model_block.json` at `:453`; `record_run` at `:246`,
called from `stage_pull` and from nowhere else.

### 2.2 THE SOURCE DIFF

The cell's substance is `C-MODEL-WINDOW-AND-ROWS` clause (1) (PRD `:872-874`): *"The window rolls: the history ends at
each issuer's LATEST CLOSED fiscal year -- a year that has ENDED and been REPORTED -- never a fixed date (today
`HIST_END = "2025-12-31"`, `model_block_pull.py:101`)."* The PRD's own citation is exact. At HEAD:

```
:100    HIST_START = "2016-01-01"
:101    HIST_END = "2025-12-31"
:102    PERIODICITY = "YEARLY"
```

consumed once, at `:227-229` inside `stage_pull`:

```
:227-229    hist = blp.historical_data([security], HIST_FIELDS, HIST_START, HIST_END, periodicity=PERIODICITY)
```

**So the change is: two MODULE-LEVEL CONSTANTS become a per-issuer computed window.**

**`M-GAP-2` -- THE CODE'S REACH IS WIDER THAN THE ACT'S KEY SET, AND THE COO HALF NAMES ONLY THE KEY SET.** The COO's
blast radius is "9 objects on 3 keys", which is correct for THIS RUN. But `HIST_START`/`HIST_END` at `:100-101` are
read by **every** `stage_pull` invocation on **every** security -- the 33 covered names included. Once the window is
computed rather than fixed, the NEXT pull on any covered name gets a different window from the one its landed block was
built on, and the fiscal-year row set can move for a name no cell of round 14 touched. **Nothing in this act writes
those keys**, so the signature's radius is not wrong; what is missing is the statement that the SOURCE change is a
shared dependency of all 33 and that its first covered-name exposure is the next pull, whenever that is. This is
exactly the Rule 22 shared-dependency shape (a per-member check certifies the members while the thing they share moves),
and it is visible only on the DESIRED plane. It needs no new rollback -- it needs to be in the record.

Andrew's no-re-run word (*"I dont care about rerunning until the process is completely validated end to end"*) is what
keeps `M-GAP-2` from having a near-term consequence. **That is a standing constraint, not a property of this change**;
if the constraint lifts before the window rule is graded on a covered name, the exposure is live.

### 2.3 THE PRODUCER'S RULE, EVERY BRANCH

| branch | what it WRITES | what it does NOT write |
|---|---|---|
| **PULLED** | `refdata.json` then `histdata.json` under one fresh stamp (`:242-245`), **then** one ledger row (`:246`) | the derive's stamp is minted separately at `:452`, so raw and derived carry DIFFERENT stamps by construction. |
| **REFUSED at the terminal / a field refused** | depends where it lands: a refusal INSIDE the response (a `__field_errors__` entry) still lands full raw bytes and is carried into `unresolved` at derive time (`:379`, `:394`); a refusal that RAISES from `blp.reference_data` at `:223` lands **nothing at all for that key, not even `refdata.json`**, and `record_run` is never reached | **a partial-object state is reachable and the COO half does not name it**: `:244` and `:245` are two separate `put_object` calls. A raise between them leaves `refdata.json` landed and `histdata.json` absent, with **no ledger row** (`:246` is after both). See `M-GAP-3`. |
| **PARTIAL across keys** | `cmd_pull:478-481` is an unguarded loop, same shape as `cmd_derive`: keys after the failing one are skipped | `pull_log` is written at `:482-483`, AFTER the loop, so **a raise mid-loop loses the pull log for the keys that DID land**. The S3 objects persist; the local record does not. |
| **EMPTY** | as 1.3: a derive over an empty raw document lands an empty block | -- |

**`M-GAP-3` -- the two-object raw landing is NOT atomic.** The COO half's rollback (delete every stamp newer than the
recorded state) **does cover** the half-landed stamp, because it deletes by stamp prefix, not by object. So this is a
gap in the OUTCOME enumeration, not in the rollback. Recording it because a worker reading "6 raw objects" as the only
success shape will not recognise a 5-object stamp as a state it must clean.

### 2.4 WHICH BRANCH EACH COO OUTCOME RESTS ON

- **Branch PULLED** -- rests on the window rule the cell builds. Covered.
- **Branch REFUSED** -- the COO half says *"NOTHING lands for that key ... recorded REFUSED with the surface named
  (READ_HERE s.2), never retried, and the other keys proceed."* **`M-DISAGREE-3`: "the other keys proceed" is NOT the
  producer's rule at HEAD.** `cmd_pull:478-481` has no exception handling; a raise ends the invocation. Since the three
  validation names fit in ONE invocation (the cap at `:509-510` is 3), a refusal on `CAT US Equity` leaves `CSL AU` and
  `6861 JP` unpulled unless the order cuts them as three separate invocations or the cell adds per-key handling.
  Blast radius NARROWER than signed, never wider, so the signature stands; the worker's expectation does not.
- **The SERVED claim.** The COO half says *"Served: NO -- the three keys are NOT in the pool crosswalk until R14-I1
  ... until then no route can resolve them."* **I confirm the conclusion and REFINE the reason, because the source has
  TWO resolution surfaces where the COO half names one.** `resolve_identity` (`lib/research/api/scoped_amgt.py:1712-1811`)
  declares *"TWO MEASURED SURFACES, IN ORDER, AND NO THIRD BRANCH"*: (1) `crosswalk/v1`, (2) **the landed-artifact
  plane** -- a `model_block_<requested>.json` on the local filesystem under `MODEL_BLOCK_ROOT` (`:1786-1789`). Surface 2
  does NOT consult the crosswalk. It is inert in Lambda for two reasons I read at HEAD: `_model_block_root()` returns
  `os.environ.get("AMGT_MODEL_BLOCK_ROOT", "")` at `:146-147`, and `AMGT_MODEL_BLOCK_ROOT` is **absent** from the
  function's `environment_variables`, which carry exactly two keys, `HARVEST_METRICS_TABLE` and `HARVEST_ARTICLES_TABLE`
  (`infra/aws/terraform/harvest/scoped-amgt-api.tf:247-258`). **So the COO's "no route can resolve them" holds, and it
  holds because of a TF env block, not only because of the crosswalk.** The qualifier is load-bearing: anything that
  sets that env var, or lands a `model_block_<key>.json` inside the deployment zip, makes these keys servable with no
  crosswalk object at all -- and that would be a widening no crosswalk-scoped control can see.

### 2.5 WRITER CENSUS CROSS-CHECK

COO half: raw prefixes N = 1, derived prefix N = 1, input ledger N = 1.

- **derived: N = 1. AGREED** -- same two `comp-find` sweeps as 1.5, denominator 66,307 files.
- **raw: N = 1 for `raw/bloomberg/<key>/<stamp>/{refdata,histdata}.json`. AGREED for those two object names.**
  ⚠ **`raw/` is not a single-producer prefix in general** -- `raw/seekingalpha/` is written by a different path
  (`lib/research/identity/crosswalk.py:128` names `raw/seekingalpha/{BABA_US,BA_US,COST_US}/`), and `rk-36` adds to it.
  The COO half's N = 1 is correct **at the grain it states** (these object names under this vendor), and I note the
  grain explicitly so a later reader does not carry "N = 1 for raw/" forward.
- **input ledger: N = 1 (`record_run`). AGREED**, and tighter than stated: within this producer there is exactly ONE
  call site, `:246`, inside `stage_pull`. `stage_derive` writes no ledger row at all.

### 2.6 WHAT THIS HALF DOES NOT COVER

The COO half's exclusions (a fourth name; any write on a covered name; a redeploy), plus: **any pull on a covered name
under the NEW window rule** -- `M-GAP-2` makes that a materially different act from a pull under the old constants, and
it needs its own pair.

---

## 3. `AMGT-rk-36` -- consensus forecasts with the SA fallback; adapter serves `forecast_*` (R14-M3; M3, C-MODEL-FORECASTS)

### 3.1 THE ACT

(i) `rk-35`'s pull/derive shape plus `bestdata.json` on the three validation keys, plus `raw/seekingalpha/<key>/<stamp>/
{symbol,metrics}.json` where Bloomberg has a gap; (ii) ONE artifact build+upload through
`infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` and ONE targeted
`safe-apply -target=module.scoped_amgt_api.aws_lambda_function.this`, 0 destroy. **AGREES with the COO half.**

### 3.2 THE SOURCE DIFF

**Producer side.** `bestdata` does not exist anywhere in the adapter today: `comp-find`-equivalent count over
`lib/research/api/scoped_amgt.py` = **0 occurrences of `bestdata`** (denominator: the whole 3,474-line file). The
`BEST_*` mnemonics are likewise absent from `model_block_pull.py`'s two field lists (`HEADER_FIELDS` `:57-73`, 15
entries; `HIST_FIELDS` `:78-98`, 19 entries). So the cell adds a THIRD Bloomberg request shape.

**The ratified rule the producer must implement**, verbatim from the PRD (`AMGT_RESAPP_PRD.md:861-866`,
`C-MODEL-FORECASTS`, v0.11): *"the `BEST_` consensus fields (`BEST_EPS`, `BEST_SALES`, `BEST_EBITDA`, `BEST_PE_RATIO`,
`BEST_DPS`), each pulled with an EXPLICIT `BEST_FPERIOD_OVERRIDE` per year -- without the override a `BEST_` field
returns the next QUARTER, which reads as a plausible annual value (measured)."* and *"Every cell carries its fiscal year
and `source` = `BBG` | `SA_FALLBACK`. Column headers come from `BEST_PERIOD_END_DATE`, never from a counted offset."*
⛔ **The missing-override failure is a WRONG NUMBER THAT LOOKS RIGHT, not an error** -- it is the one producer branch
in this chain whose failure mode is indistinguishable from success without the override being asserted. A worker must
assert the override was sent, not that a value came back.

**Adapter side.** `read_model` at `lib/research/api/scoped_amgt.py:2511-2535` returns a 9-key dict today; the cell adds
`forecast_figures / forecast_periods / forecast_source_counts / forecast_reason`. `read_thesis_bundle` at `:1939-2018`
builds `check_face` at `:1967-1971` from `check_block(header_figures + fiscal_year_figures)` **only** -- forecast
figures are not in that argument today, so including them is a real edit to `:1971`.

**SA authorization.** PRD `:1108`: *"LIFTED BY NAME (v0.12) ... production use at instantiation and in validation for
exactly two paths -- `C-PEER-SET-SA` and the `SA_FALLBACK` cells of `C-MODEL-FORECASTS`. Every other route stays NOT
AUTHORIZED"*, and `:1094` records `C-SA-TERMS-BEFORE-SCHEDULE` SATISFIED at v0.13. **The COO half's citation of the
authorization is accurate and correctly scoped.**

### 3.3 THE PRODUCER'S RULE, EVERY BRANCH

**Pool side** -- identical to 1.3/2.3 (same module, same write helper).

**Code side -- the branches of the DEPLOY, which is where this cell's real exposure sits:**

| branch | what it WRITES | what it does NOT write |
|---|---|---|
| **build fails** | nothing; `set -euo pipefail` at `build-and-upload-scoped-amgt.sh:93`, and the script's own AST closure check exits non-zero on an unpackaged import | the S3 key is untouched, so the live function is untouched. |
| **upload succeeds, apply not run** | the artifact key `research/opal-amgt-scoped-api.zip` in `opal-313476888478-lambda-artifacts` (`:98`, `:102`) | **the function does not move.** `scoped-amgt-api.tf:45-46` states it: *"modules/yang-lambda reads that object's content-sha256 as source_code_hash, so an apply BEFORE the upload will fail. Build and upload first, then apply."* |
| **apply succeeds** | the function's code, via `s3_object_version = data.aws_s3_object.artifact.version_id` and `source_code_hash = data.aws_s3_object.artifact.metadata["content-sha256"]` (`infra/aws/terraform/modules/yang-lambda/main.tf:36-39`) | with `-target` on the function resource only, **nothing else in the root plans or applies** -- including the IAM policy and the route set. See 3.4. |
| **apply refuses** | nothing | -- |

### 3.4 WHICH BRANCH EACH COO OUTCOME RESTS ON

- **"Every served name's model payload GAINS KEYS; no existing figure moves"**, discriminated by AC5's planted
  comparison on BA (`check_face_len` and `fiscal_row_count` EQUAL pre/post). **Internally consistent, but only because
  BA has no bestdata**, and the COO half says so. ⚠ **`M-GAP` note on the discriminator: it is BLIND exactly where the
  change lands.** The same half states `read_thesis_bundle`'s check face gains forecast figures; for any name WITH
  bestdata, `check_face_len` MUST move, so the equality control can only ever be run on a name the change does not
  reach. "No existing figure moves" is therefore **UNTESTED on the served population that actually gains forecasts**.
  This does not widen the radius -- it means the radius's own evidence is weaker than it reads. The fix is one more
  arm: a name WITH bestdata, asserting `fiscal_row_count` equal and `check_face_len` equal-plus-the-forecast-count.
- **The planted negative (a hollow key): `model_status ABSENT`, `has_forecast_keys True`, `forecast_figures 0`.**
  Confirmed reachable from source: `read_model:2528` sets `model_status` to `"SERVED" if model_block else "ABSENT"`,
  and the return dict at `:2525-2535` is built unconditionally, so the forecast keys will be present on the ABSENT
  branch provided the cell adds them to the same literal and not inside an `if model_block:` guard. **That "provided"
  is the whole content of the criterion** -- it grades a code SHAPE, and the order should say so.
- **"13 of 13 `200` pre AND post, `LOST=[] GAINED=[]`."** The route arithmetic is CONFIRMED:
  `scoped_amgt_route_table()` at `scoped_amgt.py:3444-3474` returns **16** entries, of which **3 are POST**
  (`/watchlist/star`, `/watchlist/unstar`, `/refresh`), leaving **13 GET**. `scoped-amgt-api.tf:315-321` asserts
  `length(local.scoped_amgt_routes) == 16` as a `terraform_data` precondition.
  ⚠ **But a `-target`ed apply on `module.scoped_amgt_api.aws_lambda_function.this` does NOT evaluate
  `terraform_data.scoped_amgt_route_count_check`** -- that resource is outside the target graph. So the count check is
  NOT a control on this act, and the 13/13 census is carried entirely by the worker's own invocations. Name it as such.

**`M-DISAGREE-1` -- THE ROLLBACK AS WRITTEN CANNOT BE EXECUTED. This is the blocking one.**
The COO half's code rollback is: *"the pre-act `CodeSha256` and the artifact's pre-act `VersionId` ... rollback =
re-point the function at that VersionId through the same Terraform resource."*

The Terraform at HEAD cannot re-point at a chosen version:

```
infra/aws/terraform/modules/yang-lambda/main.tf:17-20
    data "aws_s3_object" "artifact" {
      bucket = var.artifact_bucket
      key    = var.artifact_key
    }
```

**The data source takes NO `version_id` argument, so it always resolves to the CURRENT version of the key**, and
`:38` feeds exactly that into the function. A re-apply after a bad deploy re-reads the data source and gets the NEW
version again. The module's own comment says as much at `:14-16`: *"Terraform detects the new S3 version at plan time
and marks the Lambda for update."* Compounding it, the build script uploads to a FIXED key (`KEY="research/opal-amgt-
scoped-api.zip"`, `:98`) -- the artifact address is **overwrite-in-place**, the opposite of the pool's new-stamp
contract, so there is no second address to point at either.

The two rollbacks that ARE reachable, and neither is what was signed:
1. **Re-PUT the pre-act bytes at the same key and re-apply.** A new PUT, not a re-point; it needs the pre-act zip to
   exist as a local artifact the worker kept, or to be downloadable by version id -- which requires bucket versioning.
   **UNVERIFIED whether `opal-313476888478-lambda-artifacts` has versioning enabled**: reason, that is a live AWS read
   (`get-bucket-versioning`) and this task is constrained read-only off the repo. The presence of
   `s3_object_version` at `main.tf:38` does NOT establish it -- on an unversioned bucket that attribute resolves to
   `null` and Terraform is content.
2. **Add `version_id` to the data source.** ⛔ **This edits `infra/aws/terraform/modules/yang-lambda/main.tf`, a SHARED
   module**, and would put every Lambda built from it inside the blast radius of a rollback for one adapter. That is a
   widening, and it is not covered by either half.

**Recommendation to the L6 cut: `rk-36` and `rk-37` should not spawn until the code rollback names a mechanism that
exists at HEAD.** The pool half of the rollback is sound and is not in question.

### 3.5 WRITER CENSUS CROSS-CHECK

**COO half: N = 1 writer of the Lambda's bytes. I measure N = 1. AGREED.** Instrument (different from the COO's
single-writer queue argument, which is a process control, not a source census): two `comp-find` sweeps over the same
66,307-file denominator.

- `comp-find 'opal-amgt-scoped-api'` -- **564 hits**. The only writer-shaped hits are
  `build-and-upload-scoped-amgt.sh:98`/`:102` (the key and the zip) and `scoped-amgt-api.tf:230` (the function name).
  Everything else is the TF declaration, the ledger halves and `.scratch/` records.
- `comp-find 'update-function-code|update_function_code'` -- **735 hits across 25 pages**. I read the HEAD and DEF
  bands complete (`HEAD=2`, `DEF=1`) plus the SURFACED band's first page: **every `aws lambda update-function-code`
  call site names a DIFFERENT function's `deploy.sh`** (`access-anomaly-scanner`, `data_refresh`, `portal_data_proxy`,
  the v2_portal families, etc.). **No call site names `opal-amgt-scoped-api`.** ⚠ **COVERAGE QUALIFIER: I read 3 of 25
  pages of that sweep.** The two bands that would carry a definition or a filename match were read COMPLETE, and the
  unread remainder is `CONFIG=47 DOC=515` -- records and configs, not call sites. I state this rather than claim a
  full sweep.

So the COO's *"`aws lambda update-function-code` is NEVER used"* is confirmed **for this function** on the source
plane. Whether some out-of-repo hand act could move the bytes is UNVERIFIED and unverifiable from the repo; the
applied-plane control for that is the `CodeSha256` the worker records pre-act, which the COO half already requires.

**One more property with more than one writer, which neither half counts: the ARTIFACT KEY.** The build script is the
only writer in the repo, but the key is overwrite-in-place at a fixed address shared by every build of this adapter --
so **the "pre-act VersionId" is a property of a mutable address, and it goes stale the moment any second build runs**.
The COO half already applies exactly this reasoning to `rk-37` (*"never `rk-36`'s values -- a co-sign rollback goes
stale the moment a second act hits the same address"*). **That sentence is correct and it is the same reasoning that
makes `M-DISAGREE-1` fatal**: the address is mutable AND unpinnable.

### 3.6 WHAT THIS HALF DOES NOT COVER

The COO half's exclusions (a pull on a covered name; a fallback call where Bloomberg has a forecast; any IAM or
Terraform change beyond the one targeted resource; a second redeploy), plus:
- **any edit to `infra/aws/terraform/modules/yang-lambda/`** -- shared by every caller of that module; see
  `M-DISAGREE-1`.
- **a change to `timeout` or `memory_size`** -- `scoped-amgt-api.tf:238-245` deliberately fixes them and says a raise
  "belongs in a never-widen co-sign's blast radius with its own rollback value". Neither half names one, so neither may
  move.
- ⚠ **an IAM note that is NOT an exclusion but should be on the record:** the SA and bestdata raw prefixes need **no new
  grant**, because `raw/` is already in `local.scoped_amgt_pool_prefixes` (`scoped-amgt-api.tf:143`). But that file's
  own comment states *"THE ADAPTER MAKES ZERO GetObject CALLS UNDER `raw/` -- the freshness view answers entirely from
  key names -- so limb 1's `raw/` grant is WIDER THAN THIS CELL USES"* (`:138-141`, written under `rk-6`). **If this
  cell's `read_model` reads forecast bytes from under `raw/`, that comment becomes false and a documented-unused grant
  becomes exercised.** No policy resource moves and no apply is needed, so it is not a widening of the GRANT -- it is a
  widening of what the grant is USED for, and the stale comment is a trap for the next reader. Serve forecasts from the
  DERIVED block and the comment stays true.

---

## 4. `AMGT-rk-37` -- five sheet-row fields, description line, Base case; adapter serves them (R14-M4; M4, M5, L8, C-DESCRIPTION-LINE)

### 4.1 THE ACT

As `rk-36`: the validation-name pull/derive with `CIE_DES`/`CIE_DES_BULK` added to the mnemonic set, and ONE redeploy
of `opal-amgt-scoped-api` from this worktree's bytes, sequenced after `rk-36` drains. **AGREES with the COO half.**

### 4.2 THE SOURCE DIFF

**Producer.** `CIE_DES` and `CIE_DES_BULK` are absent from `HEADER_FIELDS` (`model_block_pull.py:57-73`, 15 entries,
read complete). The cell adds them there; `FIELD_BASIS` at `:107-144` should gain matching entries or the figures fall
through to `"Bloomberg DAPI field."` at `:406`/`:432`.

**Adapter, `read_description` (`lib/research/api/scoped_amgt.py:2538-2605`).** ⚠ **`M-DISAGREE-4`, minor and
correcting the diff's SIZE, not its radius.** The COO half says `read_description` *"gains the describes-the-business
test and probes"*. **The probes already exist at HEAD.** `DESCRIPTION_HEADER_MNEMONICS = ("CIE_DES",)` is already
declared at `:2261`, `DESCRIPTION_SECTION = "company_description"` at `:2262`, and the three-branch cascade is already
built: header scalar (`:2561-2573`), else drafted sentence 1 (`:2574-2592`), else ABSENT naming both probes
(`:2593-2605`). The PRD says the same: *"Today's reader (`lib/research/api/scoped_amgt.py:2538` `read_description`)
tries a header scalar first and then that sentence unconditionally; the cell adds the field and the test"*
(`AMGT_RESAPP_PRD.md:1190-1191`). **So the adapter diff is: (a) `CIE_DES_BULK` added to
`DESCRIPTION_HEADER_MNEMONICS`, and (b) the describes-the-business test gating branch 2 -- not the cascade itself.**
Recording it because a worker told it must build the probes may rebuild a cascade that is already correct.

**Adapter, `_model_cases` (`:2500-2508`).** At HEAD it is a **zero-argument constant**:

```
:2500-2508    def _model_cases() -> Dict[str, Any]:
                  return {"status": "ABSENT",
                          "cases": ["Upside", "Base", "Downside"],
                          "reason": ("the model block carries no case ... and no cell of this round lands them")}
```

called once, at `read_model:2532`, and surfaced onto the bundle as `model_cases` at `read_thesis_bundle:1981`.

⛔ **`M-GAP` on the blast radius, and this is the sharpest thing on the DESIRED plane for `rk-37`: this is a SHAPE
CHANGE to an already-served field, not an added key.** To serve `base` from the block while `upside`/`downside` stay
ABSENT, the function must take the block and return **per-case** status -- so the served `cases` object goes from ONE
`status` plus a flat name list to a per-case structure, **for every served name, including the 33 that gain no
forecast and the names with no block at all**. The COO half's blast radius line ("for EVERY served name regardless of
block content") DOES cover the reach. **What it does not cover is that this is a REPLACEMENT**, and consequently that
**its own stated discriminators cannot see it**: `check_face_len` is built from header + fiscal figures only
(`:1967-1971`) and `fiscal_row_count` from the fiscal slice only (`:2531`). Neither touches `cases`. **So a `cases`
shape change passes both equality controls unchanged.** Any existing consumer reading `model_cases.status` or
`model_cases.cases` as a flat list -- the portal Thesis/Model tab is one -- breaks silently under a green.
**The added arm this needs: capture the `model_cases` object verbatim pre and post for one served name and diff the KEY
SET.** Cost: one extra field in an invocation the worker is already making.

**The ratified rule** (PRD `:882-884`, `C-MODEL-WINDOW-AND-ROWS` clause 5): *"The Base case is consensus EPS x the
security's own trailing-median P/E (v0.12, Andrew-direct ~19:4xZ, 'Base.'), each input carrying its source and window.
Upside and Downside stay ABSENT with the reason 'methodology to be discussed with Andrew' ... no seat chooses a
spread."* **The COO half's card-5 citation is accurate**, and "no seat chooses a spread" makes the upside/downside
ABSENT text a RATIFIED STRING, not a worker's wording.

### 4.3 THE PRODUCER'S RULE, EVERY BRANCH

`read_description`, read complete at `:2553-2605` -- **five** branches, not the three the docstring lists:

| branch | returns |
|---|---|
| identity UNRESOLVED (`:2555-2556`) | `status ABSENT`, `reason "identity UNRESOLVED -- no description was read"`, **and no `header_scalars_measured` key at all** -- a different dict SHAPE from every other branch. |
| header scalar present and a non-empty string (`:2561-2573`) | `status SERVED`, `source` naming the mnemonic, `generated False`. Note the guard is `isinstance(value, str) and value.strip()` -- a non-string value can never serve. |
| no scalar, drafting SERVED with a `company_description` sentence (`:2574-2592`) | `status SERVED`, `marked "machine"`, evidence ids, `verbatim_check`. **This is the branch the new test must gate**, and today it is unconditional. |
| no scalar, no served sentence (`:2593-2605`) | `status ABSENT` naming both probes and the measured header-scalar count. |
| model block absent entirely | falls through to the ABSENT branch with `header_scalars_measured == []`. |

`_model_cases` at HEAD has exactly ONE branch and takes no input, so every "branch" of the case logic is created by
this cell.

### 4.4 WHICH BRANCH EACH COO OUTCOME RESTS ON

- **The two measured negatives (BA, HD): description ABSENT, `test passed False`, 3 probes named, no segment-sales text
  served.** Rests on branch 3 being GATED by the new test. ⚠ **At HEAD, BA and HD reach branch 3 and SERVE the
  segment-sales sentence** -- the PRD measured exactly that: *"sentence 1 of `company_description` describes the
  business on 0 of 12 (Boeing: 'Commercial Airplanes revenue was $41,494 million in 2025...'; Home Depot:
  'Consolidated net sales were $164.7 billion in fiscal 2025.')"* (`AMGT_RESAPP_PRD.md:1186-1189`). **So this expected
  outcome is a CHANGE of served text on names already being served, in the direction of serving LESS.** That is inside
  the COO half's radius (the whole served plane) and its rollback (revert the code), but the worker should know it is
  removing served text, not filling a hole.
  ⚠ Also: the COO half says "3 probes named" while `read_description`'s ABSENT branch at `:2599-2604` names **TWO**
  probes (the header mnemonic set, and the drafted section with its `drafting_status`). The third is presumably
  `CIE_DES_BULK` joining the mnemonic tuple. Consistent only if the tuple at `:2261` grows; **noted so "3" is
  understood as a post-change count, not a HEAD reading.**
- **"`base` ABSENT with the no-cases reason (not re-derived)"** -- rests on the block carrying no consensus EPS, which
  is `rk-36`'s output. **So `rk-37`'s expected outcomes are conditional on `rk-36` having drained**, which the COO half
  establishes by sequencing them on the same slot. Confirmed consistent.
- **"13 of 13 `200` pre and post, `LOST=[] GAINED=[]`; each name's `check_face_len` equal pre/post."** Same two notes
  as 3.4: the route-count precondition does not run under `-target`, and `check_face_len` cannot see the `cases` change.

### 4.5 WRITER CENSUS CROSS-CHECK

**COO half: N = 1 writer of the Lambda's bytes. I measure N = 1. AGREED** -- same two sweeps as 3.5, same denominator,
same coverage qualifier.

⚠ **The COO half's own sharpening is right and I adopt it:** `rk-37`'s worker must measure `CodeSha256` and the
artifact `VersionId` **itself**, never inherit `rk-36`'s, because the address is mutable and `rk-36` writes it. **And
`M-DISAGREE-1` applies unchanged here** -- the re-point mechanism does not exist at HEAD for this cell either.

**A second property this cell names and neither half counts: the served `cases` object.** Writers at HEAD: **N = 1**
(`_model_cases:2500`, single call site at `read_model:2532`, single surface at `read_thesis_bundle:1981`) -- measured by
reading the three sites, the same file. That N = 1 is what makes the shape change tractable; it is also why nothing
else will contradict it if it is wrong.

### 4.6 WHAT THIS HALF DOES NOT COVER

The COO half's exclusions (any Upside/Downside methodology -- Andrew's, per PRD `:883-884`; a pull on a covered name; a
second redeploy), plus everything in 3.6 (the shared module, timeout/memory, the `raw/` grant's usage note), plus:
- **any change to `DESCRIPTION_SECTION` or to the drafting validator** -- `read_description` branch 3 depends on
  `read_drafted_sections`' `drafting_status`, a different producer chain; moving it is a different act.
- **the portal.** Both cells change served payload shape; no portal file is in either half's radius. If a portal
  component reads `model_cases` as it is shaped today, the fix is a separate act with its own pair.

---

## 5. THE FINDINGS, COLLECTED

| id | where | what | does it widen the radius? |
|---|---|---|---|
| **`M-DISAGREE-1`** | `rk-36`, `rk-37` | the signed code rollback ("re-point the function at that VersionId through the same Terraform resource") **is not executable at HEAD** -- `modules/yang-lambda/main.tf:17-20` takes no `version_id` and always resolves to the current version; the artifact key is overwrite-in-place (`build-and-upload-scoped-amgt.sh:98`). | **the rollback does not exist. BLOCKING.** |
| **`M-DISAGREE-2`** | `rk-34` | "the worker prints the key" on a failed derive -- `cmd_derive:490-499` is unguarded; the traceback is the output and up to 2 later keys in the batch are skipped silently. | no (narrower) |
| **`M-DISAGREE-3`** | `rk-35` | "the other keys proceed" after a refusal -- `cmd_pull:478-481` is unguarded; one raise ends the invocation, and all three validation names fit in one invocation. | no (narrower) |
| **`M-DISAGREE-4`** | `rk-37` | `read_description` "gains the ... probes" -- the probes and the three-branch cascade already exist at `:2261-2262`, `:2561-2605`. The diff is the `CIE_DES_BULK` entry and the test. | no |
| **`M-DISAGREE-1(a)`** | `rk-34` | "0 `unit: ABSENT` rows" -- the producer writes the pointer string at `:318`, never an `ABSENT` token; `unresolved` records missing VALUES, not missing units. AC3 reads 0 on BOTH branches unless the cell adds the token. | no -- but the criterion cannot discriminate |
| **`M-GAP-1`** | `rk-34` | an EMPTY derive lands a zero-figure block as the new SERVED newest stamp, rc = 0, no refusal (`:378-380` + `:454`, no guard). Reachable by an identifier-form slip. | no (rollback covers it); the branch is unnamed |
| **`M-GAP-2`** | `rk-35` | `HIST_START`/`HIST_END` at `:100-101` are module constants shared by all 33 names; the act's keys are 3, the code's reach is 33 from the next pull onward. | no for this act; names a shared dependency |
| **`M-GAP-3`** | `rk-35` | the raw landing is two separate puts (`:244`, `:245`) with the ledger row after both (`:246`) -- a 1-object stamp with no ledger row is reachable. | no (rollback is by stamp prefix) |
| **discriminator note** | `rk-36` | `check_face_len` equality can only be run on a name the forecast change does NOT reach; "no existing figure moves" is untested where it matters. | no; weakens the evidence |
| **discriminator note** | `rk-37` | the `cases` **shape** change is invisible to both stated controls (`check_face_len`, `fiscal_row_count`); needs a key-set diff of `model_cases`. | no; weakens the evidence |
| **control note** | `rk-36`, `rk-37` | `terraform_data.scoped_amgt_route_count_check` (`scoped-amgt-api.tf:315-321`) does **not** evaluate under `-target=module.scoped_amgt_api.aws_lambda_function.this`. The 13/13 census is the only route control. | no |

**UNVERIFIED from this seat, with reasons:**
1. **versioning on `opal-313476888478-lambda-artifacts`** -- a live `get-bucket-versioning`, outside this task's
   read-only-on-the-repo constraint. It decides whether even the re-PUT rollback in `M-DISAGREE-1` is reachable.
2. **no scheduled producer on `derived/model_block/`** on the APPLIED plane -- an AWS/schedule read. The repo carries
   none; I take the COO's `comp-schedule: 0` and note our arms are on different planes.
3. **the round-14 task orders for `rk-34`..`rk-37`** -- not present on `coo-amgt-r14-issue-20260918` @`9a6aa12da2`.
   Every "what the cell changes" above is read from the PRD contract plus the source the contract cites; an order may
   cut differently, and `M-DISAGREE-1(a)`, `M-DISAGREE-4` and the `rk-37` shape note are the three most likely to move.
4. **whether `read_model` will read forecast bytes from under `raw/`** (3.6) -- a design choice the order makes.

**Counterpart state:** the COO halves are on file at `9a6aa12da2` for chains I, M, F, E, P. **This CTO half is a DRAFT
and is UNSIGNED.** Chain M's pair is therefore NOT complete, and by the COO half's own bound (c) a worker reading both
files before its first live act must STOP with a BLOCKING row until this half is signed at its bytes.

Drafted for `1.0.0_SA_CTO~Z`, 2026-09-18, against `HEAD` = `97341c3df2`.

---

## STANDING CLAUSE -- BINDS EVERY CELL IN THIS CHAIN (added at signature, 2026-09-18 ~22:4xZ)

**THE WRITE ADDRESS COMES FROM THE BUILDER, AND A HAND-TYPED KEY IS NOT COVERED BY THIS HALF.** Every S3 address a cell in
this chain writes is `lib/opal_naming.py` `address()` output and every resource name is `name()` output (Rule 30), and the
worker's proof carries the builder's PRINTED address, never a typed one. - **The commit gate cannot catch the violation:**
measured by `4.0.0_SA_CRO~Z`, relayed by `0.0.0_AB_MSTR~Z`, the naming gate is ENFORCING (`org/mcp/naming-gate.enforce`
@`d181e0ac5a`, read at `safe-commit.sh:691` -- CLAUDE.md Rule 30's "WARN today" is stale), but its GRADER IS WIDER THAN THE
BUILDER: a hand-typed key of the shape `bloomberg/amgt/bronze/...` PASSES the commit gate while `address()` REFUSES the same
key. A worker that types an address therefore gets a GREEN commit and a key no reader resolves.
**Also measured, and the reason a builder call may REFUSE today:** AMGT has no `scopes.json` row at all (9 rows, none
`amgt`, `harvest` or `resapp`), so `address()` returns an `opal-data-harvest` address in 0 of 1350 scope x source x tier
combinations. A refusal is the EXPECTED state until the registry row lands: it is a BLOCKING row and a named refusal, never
a hand-typed workaround (Rule 30). Andrew-direct ~21:45Z: *"opal-data-assets is solely for client data ... the whole
pipeline will exist within opal-data-harvest"*.


## CTO SIGNATURE -- chain M

**Drafted by a reviewing subagent of this seat; every BLOCKING item below was RE-VERIFIED at source by `1.0.0_SA_CTO~Z`
with its own instrument before this signature. The unmarked remainder is the reviewer's measurement, carried with its
citations and not independently re-run** -- stated so the reader knows which claims carry two instruments and which carry
one (Rule 22: name your instrument).

- `AMGT-rk-34`, `AMGT-rk-35`: **SIGNED.** The disagreements recorded against them (`M-DISAGREE-1(a)`, `-2`, `-3`) make this
  half NARROWER than the COO's, never wider: an unguarded loop that ends on a raise writes FEWER keys than signed, and a
  non-discriminating green (AC3's `0 unit: ABSENT` rows) is a weak control, not an uncovered branch. The cut should replace
  that control; the pair stands without it.
- `AMGT-rk-36`, `AMGT-rk-37`: **WITHHELD -- the signed ROLLBACK cannot be executed as written.** RE-VERIFIED here:
  `infra/aws/terraform/modules/yang-lambda/main.tf:17-20` declares `data "aws_s3_object" "artifact"` with `bucket` and `key`
  ONLY -- no `version_id` -- and `:38` feeds `s3_object_version = data.aws_s3_object.artifact.version_id`, which always
  resolves the CURRENT version. The module has no expression for "an older version". The reachable alternatives are a re-PUT
  of the prior bytes (needing bucket versioning, UNVERIFIED on the live plane by either seat) or an edit to the SHARED
  module, which is itself a widening beyond this act. **A half whose rollback cannot run does not cover the act.**
  **TO SIGN:** re-cut the rollback as a re-PUT with the versioning precondition measured first and recorded in the COO half,
  or hold these two cells out of the spawn. Raised to the issuer at msg 23830.

Signed `1.0.0_SA_CTO~Z`, 2026-09-18, against the COO halves at `9a6aa12da2`.

---

## RE-SIGNATURE -- 2026-09-18 ~23:3xZ, against the COO halves at `541d395e0d` (msg 23855's re-cut)

`2.0.0_SA_COO~Z` bound every withheld condition in the order text and restated it in its halves. This seat read the
BOUND TEXT at `541d395e0d`, not the message's summary of it, before lifting each withholding.

- **`AMGT-rk-36`, `AMGT-rk-37`: WITHHOLDING LIFTED -- SIGNED.** The rollback is re-cut to the shape my half named as the
  only reachable one: *"RESTORE THE PRE-ACT BYTES AS THE CURRENT VERSION -- `s3api copy-object` from the pre-act
  VersionId ... then the SAME targeted `safe-apply`; the module (`yang-lambda/main.tf:17-20`, `:38`) resolves the CURRENT
  artifact version and is NEVER edited"* (`541d395e0d`, chain M `:94-99`). **The precondition my half marked UNVERIFIED is
  now measured on TWO instruments:** the COO's (~22:4xZ) and this seat's own `get-bucket-versioning` on
  `opal-313476888478-lambda-artifacts` -> `{"Status": "Enabled"}`, read 2026-09-18 ~23:2xZ. `rk-37`'s half additionally
  binds that its worker measures its OWN pre-act values rather than inheriting `rk-36`'s -- a co-sign rollback goes stale
  the moment a second act hits the same address, and that is correct.

Re-signed `1.0.0_SA_CTO~Z`, 2026-09-18 ~23:3xZ.
