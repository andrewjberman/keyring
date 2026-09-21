# AMGT_RESAPP task order -- `AMGT-rk-51` -- Peers V over the SA set at floors 5/5 on its own Bloomberg FIELDS, and peers_v's empty absent_reason fixed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-51</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~52</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the fields pull and the
  score run are hand invocations over three named securities; the standing no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes S3 objects only, under the credentials this box already holds,
  to ONE already-provisioned bucket, opal-data-harvest (bronze raw Bloomberg bytes at the builder's registry-gated address, and the
  scores/v1 objects the adapter already reads); it grants no permission, provisions nothing, touches no Lambda role
  and applies no Terraform.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~52`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/`, `lib/research/scores/` and
`integrations/bloomberg/mcp/blp_client.py` exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN P's
TAIL, a queue of TWO orders in this sequence: `AMGT-rk-51` (this one), then `AMGT-rk-52` (the page).** **BEFORE YOU
BEGIN, confirm `AMGT-rk-50` has drained:** its order's `<status>` reads `complete` at HEAD AND
`s3://opal-data-harvest/peers/v1/CAT_US_Equity/` carries an object whose `basis` is `sa` -- if either is false, STOP
and file a row rather than scoring a set that does not exist. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~52;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-51` (R14-P2; FWD-8; slug row S162 parts (1) and (3))

**THE ANALYSIS ROW, verbatim** (`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a `:138`):
*"P2 Peers V over the SA set at floors 5/5 on its own Bloomberg `FIELDS`, and peers_v's empty `absent_reason` fixed"*.
**The ruling it implements, s.3.2 `:72-79`, verbatim:** *"floors 5 peers / 5 per measure, `|M| >= 3` unchanged. Part (2)
-- SEDOL-stem peer identity -- is OVERTAKEN by his Seeking-Alpha design ... Part (1) -- peers_v's EMPTY `absent_reason`
-- is a one-field fix. This seat's L4 reading, for the CVO to sign: the measure runs AS WRITTEN on its own Bloomberg
`FIELDS` pulled for the SA peer tickers -- SA chooses WHO, the measure's own fields say WHAT; feeding it SA's metrics
would be a translation layer."* Signed into ratified text as **`C-PEERS-V-FLOORS`**, PRD v0.13 @1699960261 `:643-650`:
MIN_PEERS_FOR_V 8 -> 5, MIN_PEERS_PER_MEASURE 6 -> 5, MIN_MEASURES_FOR_V 3 unchanged; *"the asserts carry this
citation in place of the earlier ruling; they are floors, never loosened below 5 / 5 / 3. Peers V's `absent_reason` is
never empty"*; the FIELDS are pulled for the SA peer tickers as `<TICKER> US Equity` (`:648-650`).

**THE MEASURED CURRENT STATE, file:line @4de34f0d95 (code byte-identical at 1699960261):**
- `lib/research/scores/peers_v.py:62-64` `MIN_PEERS_PER_MEASURE = 6`, `MIN_MEASURES_FOR_V = 3`, `MIN_PEERS_FOR_V = 8`;
  `:69-70` two asserts naming Andrew's OLD floors (`>= 3`, `>= 8`); `:74-82` `FIELDS` (16 Bloomberg mnemonics);
  `:83-85` `BEST_FPERIOD_OVERRIDE_VALUE = "BF"`, `FUND_CRNCY_OVERRIDE_VALUE = "USD"`, `NAME_MNEMONIC = "NAME"`.
- **The empty reason, exactly:** `score_peers_v()` `:211-277` returns, on suppression (`:270-275`), a dict with
  `"state": ABSENT_SOURCE` and its sentence under the key **`"reason"`** -- NOT `absent_reason` -- and, when measured
  (`:276-277`), `"V"` with NO `value` and NO `absent_reason` key at all. `classify.py:32-47` defines the record shape
  every score shares: `{state, value, absent_reason}` (`measured()` `:32-36`, `absent()` `:39-47`). `run_scores.py:177-185`
  `_peers_v_record()` stores that return VERBATIM as the `peers_v` record, so the adapter (`scoped_amgt.py:2381-2434`
  `read_scores()`, which serves each record *"verbatim"*) and the page read an ABSENT record with `absent_reason`
  missing -- **on 33 of 33 today**, while `robustness` (`run_scores.py:133-157`) and `divergence` emit real reasons from
  the same producer. That asymmetry is the defect.
- `run_scores.py:35-55` (docstring) records the STRUCTURAL mismatch: the landed R-1 member rows carry the scanner's
  factor vocabulary, never the Bloomberg `FIELDS`, so every measure classes ABSENT; `:160-174` `_peer_row_map()` keys the
  members; `:216-232` `run()` iterates EVERY keyed crosswalk name (33) and writes `scores/v1/<key>/<as_of>.json` for
  each -- there is no per-name scoping today. `main()` `:241-257` takes only `--as-of` and `--dry-run`.
- `AMGT-rk-50` lands, for each validation name, an R-1 object with `basis: "sa"`, `subject.sa_slug`, and 5 `members`
  each carrying `sa_slug`, `sa_company` and `name_agreement` (`lib/research/peers/sa_peers.py`, the sibling order).
  `run_scores._latest_peer_set()` `:118-130` already picks that newest object.
- `integrations/bloomberg/mcp/blp_client.py:135-145` `reference_data(securities, fields, overrides=None, timeout_s=30.0)`
  -> `{security: {field: value}}`, a security-level error as `{"__error__": msg}` (`:143-144`), a field-level error
  omitted; overrides applied at `:158-163`. Loaded by path as `integrations/bloomberg/research/model_block_pull.py:147-157`
  does. `health()` `:125`.
- `lib/research/api/tests/test_score_modules.py:1-14` is a `unittest` suite (40 tests at `af7cdb40d6`); the Peers V block
  `:322-349` -- `test_v_suppressed_when_fewer_than_eight_peers` (`:331-337`) builds 5 peers and asserts suppression,
  which at floor 5 will now COMPUTE: that test moves to 4 peers and is renamed for the new floor.
- `lib/opal_naming.py:1558-1571` `address()`; `AMGT-rk-50` lands its raw under the COMPOSITE `global` scope (Andrew declined an `amgt` scope row
  ~21:1xZ, msg 23774, choosing opal-data-harvest registered as the pool home; no order edits `scopes.json`), so this order does the same:
  `address("bloomberg","harvest","bronze","peers-v-fields","CAT_US_Equity", object="STAMP.json")` builds
  `s3://opal-data-harvest/bloomberg/harvest/bronze/peers-v-fields/CAT_US_Equity/STAMP.json` (measured at the cut with the
  builder over the row's shape). If `rk-50` landed with scope `global` instead (its census names that fallback), use
  the SAME scope it used -- read `rk-50`'s proof_of_spec instance AC2 output for the scope, never assume.

**RULED -- what you build, in this order:**

1. **`lib/research/scores/peers_v.py`:** `MIN_PEERS_FOR_V = 5`, `MIN_PEERS_PER_MEASURE = 5`, `MIN_MEASURES_FOR_V = 3`
   (`:62-64`); the asserts (`:69-70`) become `>= 5`, `>= 5`, `>= 3` and cite `C-PEERS-V-FLOORS, PRD v0.13 @1699960261
   :643-650` in place of the 2026-09-15 ruling; the module docstring's `|K| >= 8` / `fewer than 6 peers` sentences
   (`:7`, `:18-20`) are corrected to the new floors with the same citation. **The one-field fix:** `score_peers_v()`
   returns `classify.py`'s shape -- on suppression `classify.absent(classify.ABSENT_SOURCE, <the existing sentence>,
   V=None, K=K, M=M, measures=measures_out)` so `absent_reason` carries the sentence (and `reason` is gone -- one field);
   when measured `classify.measured(V, V=V, K=K, M=M, measures=measures_out)` so `value` and `absent_reason: None` are
   present. `V`, `K`, `M`, `measures`, `state` stay as keys so every existing caller and test still reads them.
2. **`lib/research/scores/peers_fields_pull.py` (new):** `pull(security_key)` -- reads the newest R-1 object for the key
   (reuse `run_scores._latest_peer_set()`); REFUSES with a printed reason when `basis != "sa"` (no fleet-path use);
   builds `[<subject sa_slug> US Equity] + [<member sa_slug> US Equity x5]`; calls `blp_client.health()` then ONE
   `reference_data(securities, list(peers_v.FIELDS) + [peers_v.NAME_MNEMONIC], overrides={"BEST_FPERIOD_OVERRIDE":
   peers_v.BEST_FPERIOD_OVERRIDE_VALUE, "EQY_FUND_CRNCY": peers_v.FUND_CRNCY_OVERRIDE_VALUE})`; lands the raw response
   (`json.dumps(..., default=str)` bytes) at `address("bloomberg", <scope>, "bronze", "peers-v-fields", security_key,
   object="<utc_stamp>.json")` BEFORE derivation; then per security runs `sa_peers.entity_test(<R-1 sa_company>,
   <Bloomberg NAME>)` -- a DISAGREEING name, or a `__error__`, classes that row `ABSENT_PULL` with both names in the
   reason and the row is NOT fed to the measure; prints `FIELDS-PULL <key> securities N (1 subject + 5 peers) fields 17
   (16 FIELDS + NAME) overrides ...`, `NAME-AGREEMENT k of N`, `RAW-LANDED <address>`. CLI:
   `python -m lib.research.scores.peers_fields_pull pull --security-key K` and `plan --security-key K` (zero calls,
   zero writes, prints the securities, fields, overrides and the builder address).
3. **`lib/research/scores/run_scores.py`:** `_peers_v_record()` gains a second source: when the newest R-1 object has
   `basis == "sa"`, read the newest landed `peers-v-fields` raw object for the key (list the builder prefix, newest by
   stamp), build `subject_row` and `peer_rows` from its per-security field dicts (only rows whose `name_agreement` is
   true), and call `score_peers_v()` on THOSE; the record carries `fields_source: <the raw address>` and
   `peers_source: <the R-1 key>`. When no fields object has landed, or the R-1 basis is not `sa`, the record is
   `classify.absent(ABSENT_SOURCE, "<which of the two is missing, named>")` -- a sentence, never empty. `main()` gains
   `--security-key K` (repeatable): with it, `run()` scores ONLY the named keys and never lists the crosswalk;
   without it the behaviour is unchanged (and you never run it without it -- see BOUNDS). Print one line per key:
   `SCORED <key> peers_v state=<state> value=<v> K=<K> M=<M> absent_reason=<reason or None> -> <pool key>`.
3b. **`run_scores.py` gains a KEY FILTER -- a SOURCE CHANGE this order names (CTO msg 23830):** `run(as_of, client,
   dry_run, security_keys=None)` writes only the keys in `security_keys` when given (`keys = [k for k in keyed if k in
   security_keys]`, refusing with a printed reason any requested key the newest crosswalk does not carry); `main()` gains a
   repeatable `--security-key`; a run with NO `--security-key` REFUSES (rc 2, `refused: no --security-key; a bare run
   iterates every keyed name and is the fleet re-run Andrew barred; pass --all-keyed to override`) unless `--all-keyed` is
   given -- and this order NEVER passes `--all-keyed`. The unit test in `test_score_modules.py` plants a bare run and a
   `--security-key` run against a fake client and asserts the refusal and the one-key write set.

4. **`lib/research/api/tests/test_score_modules.py`:** the Peers V block updated for floors 5/5/3 -- 4 peers SUPPRESS,
   5 peers COMPUTE (the planted negative and its control); `test_absent_reason_never_empty` (2 peers -> `state`
   ABSENT_SOURCE, `absent_reason` non-empty and containing `|K|=2`; a full 5-peer set -> `absent_reason` None,
   `value == V`); `test_fields_name_disagreement_classes_absent_pull` (a stubbed refdata dict whose NAME fails the
   entity test is excluded from `peer_rows` with an ABSENT_PULL row naming both names). NO NETWORK in any test.

**The validation bar (`C-VALIDATION-NAMES`, `:1652-1658`):** pull + score for `CAT_US_Equity`, `CSL_AU_Equity`,
`6861_JP_Equity` -- and ONLY those. A name whose R-1 set is `absent` (as `rk-50` may honestly leave CSL or Keyence)
scores `ABSENT_SOURCE` with the reason *"no SA peer set: <rk-50's reason>"* -- that proves the reason field, and is a
PASS of this cell's honesty clause, not a defect to work around.

**This order moves served output (analysis s.4 co-sign `yes`).** The blast radius is EXACTLY the three NEW keys
`scores/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json` in `opal-data-harvest` (read by the adapter's
`read_scores()` once R14-I1 lands their identity) plus the bronze raw under `bloomberg/<scope>/bronze/peers-v-fields/`;
the 33 covered names' `scores/v1` objects are NOT rewritten (AC5 proves it, before and after). It needs a FRESH
never-widen co-sign (CTO half + your COO's half), each naming that blast radius, the writer count (ONE writer of
`scores/v1`: `run_scores.py`, printed), and a per-key rollback FROM THE LIVE PRE-ACT STATE (the three keys ABSENT --
rollback = delete the three new objects, which AC5's before-read records). **Open your change-management ledger entry
in `org/critical_paths/change_management/` BEFORE your first pool write, close it on completion**, per NEVER-2.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis @9c8e04cd9a s.4 row R14-P2 (`:138`)
and s.3.2 (`:72-79`, slug row S162). PRD v0.13 @1699960261: `C-PEERS-V-FLOORS` (`:643-650`), `C-PEER-SET-SA`
(`:614-641`), `C-PRODUCTION-HOME` (`:1643-1650`), `C-VALIDATION-NAMES` (`:1652-1658`). Both L4-R halves signed at
v0.13 before this order was cut. Depends on `AMGT-rk-50` (the SA peer set).

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain P is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-51`, and that section names this order's blast radius
(the keys/prefixes and, for an adapter cell, the Lambda) and the per-key rollback. Read both before your first live act,
paste both files' sha256 into the change-management entry, and record every pre-act hash the halves tell you to measure
FRESH (never a value copied from another order). Either file absent or its `AMGT-rk-51` section missing: run the read-only and
dry-run criteria, file a BLOCKING row (disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half.

**ISSUER AMENDMENT -- THE REGISTRY GATE (`2.0.0_SA_COO~Z`, 2026-09-18 ~21:3xZ, on Andrew's words relayed by
`1.0.0_SA_CTO~Z` msg 23778):** Andrew, VERBATIM: *"Yeah i hope its clear and foundational in all associated AMGT_RESAPP art
that the opal-data-harvest bucket is the designated folder for all RESAPP data content/pipelines"* and *"then it has to be
structured in said bucket in proper form"*. So: EVERY AMGT_RESAPP byte this order lands -- bronze raw included -- lands in
`opal-data-harvest`, at an address PRINTED BY `lib/opal_naming.py address()`, never typed. MEASURED at the cut: the registry
(`infra/logic/registry/tiers.json:27`) still homes bronze/silver in the shared `opal-data-assets`; the two registry rows that
re-home this project (the home registration + the R20 departure entry) are being placed by `0.0.0_AB_MSTR~Z` on the laptop
fabric and land here by merge. THE RULE, replacing every literal bucket in this order: before ANY live write at a builder
address, print the builder's output for the address the order names with the scope token `harvest` (the L4 RULING,
`1.0.0_SA_CTO~Z` @2560e04f46: vendor bronze is `<vendor>/harvest/bronze/<table>/<partition>/<object>`, our own derivations
`amgt/harvest/<tier>/<table>/...`; NO `global` route and NO `amgt` scope row -- a scope spelled `amgt` is refused by the
builder, and `global` is not this project's route; where this order's older text says `global`, read `harvest`); the naming gate at commit is ENFORCING and its grader is WIDER than the builder, so a
hand-typed key can pass the commit and resolve nowhere -- never type one); the live
arm is LIVE iff that address's bucket is `opal-data-harvest`. If the builder REFUSES or returns any other bucket, DO NOT
WRITE THERE: the offline, read-only and dry-run criteria run in full; each live criterion is recorded with the builder's
printed line as its output and the verdict REFUSED-BY-REGISTRY; ONE surprise row carries it (`spec_asserts`: Andrew's words
above and CTO msg 23778; `world_is`: the builder's exact output at spawn), and the worker keeps working. A write to
`opal-data-assets` of any AMGT_RESAPP object is NOT AUTHORIZED by this order under any branch. Where this order's text below
reads `s3://opal-data-harvest/...` for a builder address, that is the EXPECTED bucket once the rows land, and the address is
still read from the builder's print, never from this text.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/scores/
lib/research/api/tests/test_score_modules.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~52/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-51.peers-v-sa-floors.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `lib/research/peers/` (including `sa_peers.py`, which you IMPORT for
  `entity_test`), `integrations/bloomberg/`, `lib/opal_naming.py` and `lib/research/api/scoped_amgt.py` are read and
  imported, never edited; `read_scores()` serves the record verbatim, so no adapter change is needed -- a criterion that
  seems to need one is REFUSED with a row. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~52 <0.9.0_WK_AMGT_RESAPP~52@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by a NON-SHELL writer). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN for THIS order (it is `AMGT-rk-52`'s surface, your next order). **COLLECTION STAYS OFF -- this cell's
Bloomberg pulls are inside the validation Andrew set as the bar** (`C-VALIDATION-NAMES` `:1652-1658`): at most three
`reference_data` calls, one per validation name, over subject + 5 peers each, 17 fields. **Read
`integrations/bloomberg/READ_HERE.md` first**; `blp_client.health()` before the first pull; if the terminal is signed out,
do NOT sign in (the two-attempt budget is the BBG seat's) -- REFUSE AC4-AC6 with a row and land everything offline
(AC1-AC3). **No Seeking Alpha call from this order** -- WHO the peers are is `rk-50`'s landed object; you never
re-fetch it. **NEVER run `run_scores` without `--security-key`** -- a bare run iterates the 33 and is the fleet re-run
Andrew barred (*"I dont care about rerunning until the process is completely validated end to end"*). **NO alarm,
monitor, SNS/SES-send, notification or freshness checker.** No non-ASCII in anything you write. **PUSH: never.**
LD-0522 puts the push with `0.0.0_AB_MSTR~Z`.
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name. In particular: a MEASURED Peers V for CAT is the
expected outcome, but if the data honestly suppresses it, the record's non-empty `absent_reason` IS the deliverable --
never a loosened floor, never a translated SA metric.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-measure at spawn: objects under
`scores/v1/` for the three validation keys (expected 0) and the count of `scores/v1` objects dated today for the 33
crosswalk keys (expected 0; it must still read 0 when you finish).
**A DRY RUN WRITES NOTHING, ANYWHERE** (`C-PRODUCTION-HOME` `:1646-1647`): `plan` and `--dry-run` perform no request and no put.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W52-S<k>`, `<k>` starting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never re-serialize
it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-51"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m unittest lib.research.api.tests.test_score_modules -v 2>&1 | tail -10</invocation><expect>the footer reads "Ran N tests" with N >= 43 (40 at af7cdb40d6 plus the three new Peers V tests named in section 1 step 4, each listed "ok" in the verbose output above the footer) followed by "OK"; a suite that collects fewer than 43 is a FAIL whatever its status line says</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-51"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import inspect
from lib.research.scores import peers_v as p
src = inspect.getsource(p)
print('floors', p.MIN_PEERS_FOR_V, p.MIN_PEERS_PER_MEASURE, p.MIN_MEASURES_FOR_V)
print('cites C-PEERS-V-FLOORS', 'C-PEERS-V-FLOORS' in src, 'cites 1699960261', '1699960261' in src)
print('old floor text gone', ('|K| >= 8' not in src) and ('fewer than 6 peers' not in src))
"</invocation><expect>floors 5 5 3; cites C-PEERS-V-FLOORS True and cites 1699960261 True (the asserts and docstring carry the new citation); old floor text gone True -- before this order the line reads floors 8 6 3 and the citation reads False</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-51"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.scores import peers_v, classify
def row(n):
    return {'FREE_CASH_FLOW_YIELD': 5.0 + 0.3 * n, 'CRNCY_ADJ_MKT_CAP': 1000.0 + 10.0 * n, 'BEST_PE_RATIO': 15.0 + 0.5 * n, 'BEST_EPS': 6.0 + 0.1 * n, 'PE_RATIO': 17.0 + 0.5 * n, 'TRAIL_12M_EPS': 4.0 + 0.05 * n, 'TRAIL_12M_DVD_PAID': -20.0 - n, 'CF_DECR_CAP_STOCK': -10.0 - n, 'CURRENT_EV_TO_T12M_EBITDA': 10.0 + 0.2 * n, 'TRAIL_12M_EBITDA': 200.0 + 2.0 * n, 'EV_TO_T12M_SALES': 3.0 + 0.2 * n}
few = peers_v.score_peers_v(row(-1), {'P%d' % i: row(i) for i in range(2)}, subject_key='S')
four = peers_v.score_peers_v(row(-1), {'P%d' % i: row(i) for i in range(4)}, subject_key='S')
five = peers_v.score_peers_v(row(-1), {'P%d' % i: row(i) for i in range(5)}, subject_key='S')
for label, r in (('two', few), ('four', four), ('five', five)):
    print(label, 'state', r.get('state'), 'K', r.get('K'), 'value', r.get('value'), 'absent_reason', repr(r.get('absent_reason')), 'has_reason_key', 'reason' in r)
print('planted-negative ok', few['state'] == classify.ABSENT_SOURCE and bool(few['absent_reason']) and '|K|=2' in few['absent_reason'])
print('floor-4 suppressed', four['state'] == classify.ABSENT_SOURCE and bool(four['absent_reason']))
print('floor-5 measured', five['state'] == classify.MEASURED and five['absent_reason'] is None and five['value'] == five['V'])
"</invocation><expect>planted-negative ok True (two peers: state ABSENT_SOURCE, absent_reason a non-empty sentence naming |K|=2, no stray reason key); floor-4 suppressed True; floor-5 measured True (state MEASURED, value equal to V, absent_reason None) -- before this order the two-peer record prints absent_reason None and has_reason_key True</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-51"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.scores.peers_fields_pull pull --security-key CAT_US_Equity 2>&1 | tail -8 && python -m lib.research.scores.run_scores --security-key CAT_US_Equity --as-of "$(date -u +%F)" 2>&1 | tail -6</invocation><expect>FIELDS-PULL CAT_US_Equity securities 6 (1 subject + 5 peers) fields 17 (16 FIELDS + NAME) overrides BEST_FPERIOD_OVERRIDE=BF EQY_FUND_CRNCY=USD; NAME-AGREEMENT k of 6 with each pair printed; RAW-LANDED s3://opal-data-harvest/bloomberg/harvest/bronze/peers-v-fields/CAT_US_Equity/{stamp}.json; then SCORED CAT_US_Equity peers_v state=MEASURED value={float} K=5 M=[at least three measure ids] absent_reason=None -> scores/v1/CAT_US_Equity/{as_of}.json -- or, if the data honestly suppresses, state=ABSENT_SOURCE with K=5 and a non-empty absent_reason naming the measure counts; a BLOCKED health() line is a FAIL recorded as such, never a sign-in</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-51"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, datetime
s3 = boto3.client('s3', region_name='us-east-1')
today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
cw = sorted(o['Key'] for p in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix='crosswalk/v1/') for o in p.get('Contents', []))[-1]
doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=cw)['Body'].read())
covered = sorted({r['security_key'] for r in doc.get('records', []) if r.get('security_key')})
allkeys = [o['Key'] for p in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix='scores/v1/') for o in p.get('Contents', [])]
rerun = [k for k in allkeys if k.split('/')[2] in covered and k.endswith('/%s.json' % today)]
validation = ['CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity']
scored = [k for k in allkeys if k.split('/')[2] in validation]
print('crosswalk', cw, 'covered', len(covered))
print('rerun_of_covered_today', len(rerun), 'of', len(covered), rerun)
print('validation_scored', len(scored), 'of 3', scored)
"</invocation><expect>covered 33 (re-measured from the newest crosswalk, printed); rerun_of_covered_today 0 of 33 with an empty list (no covered name's scores object was written today -- no fleet re-run); validation_scored 3 of 3 listing the three new keys (or fewer, each shortfall named in the report with its reason)</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-51"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.scores.peers_fields_pull pull --security-key CSL_AU_Equity 2>&1 | tail -3; python -m lib.research.scores.peers_fields_pull pull --security-key 6861_JP_Equity 2>&1 | tail -3; python -m lib.research.scores.run_scores --security-key CSL_AU_Equity --security-key 6861_JP_Equity --as-of "$(date -u +%F)" 2>&1 | tail -4; python -c "
import boto3, json
s3 = boto3.client('s3', region_name='us-east-1')
ok = 0
for key in ('CAT_US_Equity', 'CSL_AU_Equity', '6861_JP_Equity'):
    ks = sorted(o['Key'] for p in s3.get_paginator('list_objects_v2').paginate(Bucket='opal-data-harvest', Prefix='scores/v1/%s/' % key) for o in p.get('Contents', []))
    if not ks:
        print(key, 'NO SCORES OBJECT'); continue
    rec = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=ks[-1])['Body'].read())['peers_v']
    honest = (rec.get('state') == 'MEASURED' and rec.get('value') is not None) or (rec.get('state') != 'MEASURED' and bool(rec.get('absent_reason')))
    ok += 1 if honest else 0
    print(key, ks[-1], 'state', rec.get('state'), 'value', rec.get('value'), 'absent_reason', repr(rec.get('absent_reason'))[:160], 'HONEST' if honest else 'EMPTY-REASON')
print('honest_records', ok, 'of 3')
"</invocation><expect>each pull line reads FIELDS-PULL ... or REFUSED: R-1 basis is absent/not sa (rk-50's honest state, named); the read-back prints, for each of the three keys, a served peers_v record that is either MEASURED with a value or ABSENT with a non-empty absent_reason (one that names "no SA peer set" for a name rk-50 left absent), and honest_records 3 of 3 -- an EMPTY-REASON line anywhere is a FAIL</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.
AC1-AC3 are offline and run BEFORE any live call; AC4-AC6 read the LIVE store after your runs, and AC5 is ALSO run
before your first pool write so the before-state (validation_scored 0 of 3) is in your change-management entry.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~52/AMGT_RESAPP.TO-AMGT-rk-51.peers-v-sa-floors.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`; close the change-management entry. **Do not stop here** -- `AMGT-rk-52`
(the page) is handed to you next as a continuation; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>superseded</status>
<superseded_by>the H-chain with AMGT-rk-50: its reader intent (peers floors) is re-cut as a reader cell on silver after the writers and their moves. RULED by 1.0.0_SA_CTO~Z, ROUND_ANALYSIS.round20.md s.2 @ab54fb15e0 (msg 24109): SUPERSEDED is terminal, not acceptance (R4); the remedy stays owed by the successor. Flipped in the round-21 issuance by 2.0.0_SA_COO~Z.</superseded_by>
<round>14</round>
<slot>~52</slot>
<fabric>site-z</fabric>
