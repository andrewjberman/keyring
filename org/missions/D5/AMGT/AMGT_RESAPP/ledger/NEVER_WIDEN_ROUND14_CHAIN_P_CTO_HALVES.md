# NEVER-WIDEN CO-SIGN -- CTO HALVES. Round 14, chain P. One section per co-signed cell.

**Signer:** `1.0.0_SA_CTO~Z`. **SIGNED as recorded in the CTO SIGNATURE block at the end of this file.** **Counterpart:**
`2.0.0_SA_COO~Z`'s COO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_P_COO_HALVES.md` @`9a6aa12da2`
(branch `coo-amgt-r14-issue-20260918`), the APPLIED/EXERCISED plane. **This plane: DESIRED -- the
SOURCE DIFF and THE PRODUCER'S OWN RULE**, every branch read from source at HEAD.

**Vintages.** Repo HEAD = `c898937600` on `SITEZ`, and every `path:line` below is read at HEAD
unless a `@<commit-ish>` says otherwise. Identity registry = `registry@c1cf124537835573`
(`lib/opal_naming.py registry_hash()[:16]`, read in-process).

**Reading rule (CLAUDE.md s.5 NEVER-1).** A half names the act's BLAST RADIUS, never the producer's
decision. Where this half and the COO half disagree, the disagreement is stated LOUDLY and is the
finding -- it is never smoothed over. Where a claim could not be exercised, it is marked UNVERIFIED
with the reason. "proof / root cause / definitively" appear nowhere below except where the text says
EXERCISED and names the arm and its negative control.

**CELLS COVERED: 2** -- `AMGT-rk-51` (R14-P2) and `AMGT-rk-52` (R14-P3). `AMGT-rk-50` (R14-P1) is
NOT co-signed by the issuer and therefore carries no CTO half; section 0 records only what rk-51's
own outcomes inherit from it, because the COO half's expected outcome for rk-51 rests on rk-50's
output and a half may not rest on an uncovered act silently.

---

## 0. PRECONDITION READ -- what rk-51 inherits from the UNCOVERED rk-50

The COO half's header states rk-50 writes "the three validation names' raw bytes and R-1 pool
objects -- keys no served route resolves until `rk-31` lands", marks it NOT co-signed, and leaves it
as drafted. Three source facts bear on rk-51 and are recorded here because no other half records
them:

1. **`peers/v1/<key>/<as_of>.json` acquires a SECOND writer this round, and nothing counts it.** At
   HEAD the writer of that key is `lib/research/peers/engine.py` (`PEERS_PREFIX` at `:76`; the
   `--write-pool` batch at `:1436-1443`, the partition argument documented at `:1232`). rk-50 writing
   an SA-shaped R-1 object makes **N = 2** writers of that property. MEASURED with `comp-find
   'peers/v1' lib infra data .tools portal --limit 40`: 28 hits over 10,413 files scanned
   (corpus=all), four DEF-band `PEERS_PREFIX` definitions of which exactly one
   (`lib/research/peers/engine.py:76`) sits in a writer; `lib/research/api/scoped_amgt.py:156`,
   `lib/research/posture/comparable.py:39` and `lib/research/scores/run_scores.py:71` are readers.
   Neither half prints a writer census for `peers/v1`, because the cell that adds the second writer
   is the uncovered one. **A new pair is owed on rk-50 before it writes, or the second writer lands
   uncounted.**
2. **The readers of `peers/v1` are wider than the Peers page.** `lib/research/posture/packs.py:114`
   and `lib/research/posture/judge.py:437` both fetch `peers/v1/%s/%s.json` into the POSTURE
   evidence pack. Changing what the newest `peers/v1` object holds for a name therefore reaches the
   posture surface, not only the peers surface. This is stated for the record; it is rk-50's blast
   radius, not rk-51's.
3. **The SA producer's terminal branches are four, not two.** `integrations/seekingalpha/detectors.py
   classify()` `:39-48` returns `OK` (200 with a body at or above 8 bytes), `FAILURE` (200 under 8
   bytes -- the missing-Referer trap, `empty_body()` `:19-23`), `REHARVEST` (403, body at or under
   600 bytes, carrying the PerimeterX marker, `reharvest_signal()` `:26-36`) and `AUTH_FAIL`
   (everything else: a non-challenge 403, a 401, any other status -- `:45-48`). PRD `C-PEER-SET-SA`
   (`prd/AMGT_RESAPP_PRD.md:631`) names only the REHARVEST stop. `rest_fetch.py` stops the run on
   REHARVEST at `:282`, `:318`, `:341`, `:362`, `:389` and writes `REHARVEST_NEEDED` at `:464-467`.
   For rk-51 this is adequate: its ABSENT arm keys on "the R-1 object is ABSENT", which is true under
   FAILURE and AUTH_FAIL as well as REHARVEST, so the COO half's ABSENT branch covers all four.

---

## 1. `AMGT-rk-51` -- peers V from SA with floors; scores for the three validation names (R14-P2; FWD-8, S162 (1), C-PEERS-V-FLOORS)

### 1.1 THE ACT, restated

Two arms in one cell. **Arm A (bronze):** ONE Bloomberg reference-data pull for `peers_v.py`'s own
`FIELDS` tuple on the three validation names, landed raw at the `lib/opal_naming.py address()` output
for `bloomberg` / `global` (or `amgt`) / `bronze` / `peers-v-fields` / `<key>`, gated on that output
printing an `opal-data-harvest` bucket. **Arm B (pool):** `run_scores` writing
`s3://opal-data-harvest/scores/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json`.

**This agrees with the COO half's THE ACT paragraph.** It does not agree with the COO half's BLAST
RADIUS, and the disagreements are section 1.4.

### 1.2 THE SOURCE DIFF

**(a) `lib/research/scores/peers_v.py` -- the floors.** PRD `C-PEERS-V-FLOORS` (`:643-650`) amends
`MIN_PEERS_FOR_V` 8 -> 5 and `MIN_PEERS_PER_MEASURE` 6 -> 5, `MIN_MEASURES_FOR_V` unchanged at 3. At
HEAD those constants are `peers_v.py:62-64`:

```
    62  MIN_PEERS_PER_MEASURE = 6   # "guards drop a measure at ... fewer than 6 peers"
    63  MIN_MEASURES_FOR_V = 3      # "suppress V at |M| < 3"
    64  MIN_PEERS_FOR_V = 8         # "or |K| < 8"
```

**The cell cannot be done by editing `:62-64` alone.** `:69-70` are import-time asserts pinned to the
SUPERSEDED numbers:

```
    69  assert MIN_MEASURES_FOR_V >= 3, "MIN_MEASURES_FOR_V must never drop below Andrew's ruled |M| >= 3 floor"
    70  assert MIN_PEERS_FOR_V >= 8, "MIN_PEERS_FOR_V must never drop below Andrew's ruled |K| >= 8 floor"
```

**EXERCISED, in memory, on a patched copy of the HEAD bytes -- the repo file was not edited.**
Substituting only `MIN_PEERS_FOR_V = 5` and `MIN_PEERS_PER_MEASURE = 5` and compiling the result
raises `AssertionError: MIN_PEERS_FOR_V must never drop below Andrew's ruled |K| >= 8 floor` at
import. **Negative control, same runner, same call:** the unmodified HEAD bytes compile clean. So the
edit is `:62-64` AND `:69-70` together; `:70`'s message text must be re-cited to the PRD's source
(Andrew-direct ~18:0xZ, *"It's now 5 instead of 8, we'll fit to the SA shape"*), which `:646` already
directs ("The asserts carry this citation in place of the earlier ruling"). PRD `:1683` cites the
floors at `peers_v.py:62-70` -- the ten-line span, asserts included -- so the PRD is correct and it is
the COO half that does not mention the asserts.

**(b) `peers_v.py:270-277` -- the record shape.** The COO half names an `absent_reason` defect here.
The span is EXACT. The diagnosis is not. At HEAD:

```
   270      if K < MIN_PEERS_FOR_V or len(M) < MIN_MEASURES_FOR_V:
   274              "reason": "suppressed: |K|=%d (need >= %d) or |M|=%d (need >= %d)" % (...),
   277      return {"V": V, "K": K, "M": M, "measures": measures_out, "state": classify.MEASURED}
```

The suppressed branch returns key **`reason`** (a populated string), NOT `absent_reason`; the
MEASURED branch at `:277` returns neither `reason` nor `absent_reason` nor `value`. **EXERCISED**
(same in-memory runner, floors at 5/5/3): the MEASURED branch's keys are exactly
`['K','M','V','measures','state']` and the suppressed branch's are those plus `reason`; `'absent_reason'
in out` is `False` on BOTH branches and `'value' in out` is `False` on both. The consumer's promise is
`lib/research/api/scoped_amgt.py:2381-2389` -- "ALWAYS RETURNS ALL THREE SCORE KEYS ... each a
`classify.py`-shaped record (`state`/`value`/`absent_reason`)" served "verbatim" at `:2424-2433`. The
shape `classify.py` mints is `{"state","value","absent_reason"}` (`classify.py:34` measured, `:45`
absent). **So the defect is not "the reason is None" -- it is that the key does not exist, on both
branches.** PRD `:647` ("Peers V's `absent_reason` is never empty") is satisfiable only by adding the
key, and the MEASURED branch needs it too or the adapter's own docstring stays false for a scored
name.

**(c) `lib/research/scores/run_scores.py` -- arm B's producer.** Unchanged by this cell as the COO
half describes it, and that is the problem in 1.4. Relevant lines: `POOL_BUCKET = crosswalk.POOL_BUCKET`
`:68`; `SCORES_PREFIX = "scores/v1/"` `:72`; `_latest_crosswalk_doc()` `:81-92`; `keyed_security_keys()`
`:95-99`; `_peers_v_record()` `:177-185`; `run()` `:216-238`; the key line `:227` `pool_key =
"{0}{1}/{2}.json".format(SCORES_PREFIX, security_key, as_of)`; the put `:231`
`crosswalk.write_pool(pool_key, payload, bucket=POOL_BUCKET, client=client)`; the CLI `:241-257`.

**(d) `lib/opal_naming.py` -- arm A's address.** `address()` `:1558-1566` composes `key()`
`:1542-1555` with `_home_bucket()` `:249-261`, which reads `tiers.json homes[tenancy][tier]`. Scope
long forms resolve through `_long_scope()` `:1530-1539`.

**(e) `lib/research/identity/crosswalk.py:609-657` -- the pool put.** `write_pool()` heads the key,
and puts only when `head is None` or the stored `document-sha256` differs (`:627`), conditioned
`IfNoneMatch: "*"` on a first mint and `IfMatch: <ETag>` on a replacement (`:628`), then reads back
and compares digest and length (`:638-649`).

### 1.3 THE PRODUCER'S RULE, every branch

**Arm A -- `address()`, EXERCISED read-only against the on-disk registry (no AWS, no vendor, no
write), `registry@c1cf124537835573`:**

| call | branch taken | what it writes |
|---|---|---|
| `address("bloomberg","global","bronze","peers-v-fields","CAT_US_Equity")` | SUCCESS | prints `s3://opal-data-assets/bloomberg/global/bronze/peers-v-fields/CAT_US_Equity` |
| `address("bloomberg","amgt","bronze",...)` | **RAISE** | `ValueError: scope 'amgt' resolves to no scopes.json row` (`_long_scope`, `:1534`) -- nothing printed |
| `address("bloomberg","global","gold",...)` | RAISE | `ValueError: no home bucket for tier gold of scope global: 'bloomberg'` (`:1564-1565`) |

Corroborated by a DIFFERENT instrument: `comp-find 'opal-data-harvest' infra/logic/registry --limit 20`
returns **2 hits across 6 files scanned**, both CONFIG-band PROSE basis strings in `systems.json`
(`:217` `long_basis`, `:220` `owner_basis`). **No scopes.json row, no tiers.json home and no `bucket`
field anywhere in the registry names `opal-data-harvest`**, so no argument tuple can make `address()`
print it at this registry vintage. The `global` scope's tenancy is `COMPOSITE` and
`tiers.json homes.COMPOSITE.bronze` is `{"home":"shared","bucket":"opal-data-assets","rule":"R4"}`.

**So the COO half's REGISTRY GATE is CORRECT and I confirm it: arm A's live write is DEAD until the
two R20 rows land.** One refinement the half does not carry: its remedy is "the criterion records the
builder's line as REFUSED-BY-REGISTRY", and on the `amgt` alternative the half itself offers there is
**no builder line to record** -- `address()` raises before printing. The worker must record the
EXCEPTION TEXT on that arm. The half covers the outcome by intent and not by grammar.

**Arm B -- `run_scores.run()`, read from source at `:216-238`:**

- **SUCCESS.** `run()` takes `(as_of, client, dry_run)` and NOTHING ELSE (`:216`). It lists the newest
  crosswalk object (`:219` -> `_latest_crosswalk_doc` `:81-92`), takes **every** `security_key` the
  crosswalk carries (`:220` -> `keyed_security_keys` `:95-99`, a set comprehension over `records[]`
  with no filter), and loops (`:222`) writing `scores/v1/<key>/<as_of>.json` for **each** (`:227`,
  `:231`). **It writes NOTHING ELSE and it OMITS NOTHING: there is no key argument, no `--key`, no
  `--only`, no `--names`. The CLI at `:241-245` exposes exactly `--as-of` and `--dry-run`.**
- **PARTIAL / per-name absence.** A name with no model block or no peer set is not skipped: it gets a
  record whose three score keys class ABSENT (`_robustness_record` `:133-141`, `_peers_v_record`
  `:177-185`, `_divergence_record` `:188-191`), and **an object is still written for it** (`:225-231`).
  So "ABSENT" never means "no key landed".
- **EMPTY.** No crosswalk object at all -> `RuntimeError` at `:87-89`, before any write.
- **DRY RUN.** `--dry-run` appends `{"put_performed": False, "dry_run": True}` and `continue`s
  (`:228-230`) -- no S3 write on any name. This is the ONLY arm-B invocation that touches nothing.
- **EXCEPTION.** `write_pool`'s read-back raises `ValueError` on a digest or length mismatch
  (`crosswalk.py:640-649`) AFTER the put -- the object is already on S3 when that raise happens.
- **RE-RUN, same date, same content.** `write_pool` `:627` skips the put; `put_performed` False.
  A re-run on a NEW date never skips, because the payload carries `"as_of": as_of` (`run_scores.py:205`),
  so the digest always differs and `head is None` on a fresh key anyway.

**Which branch each COO expected outcome rests on.**

- "*peers_v served with the floor-satisfied flag and the member count as denominator*" rests on arm B
  SUCCESS **plus** arm A having landed Bloomberg `FIELDS` into whatever `_peers_v_record` reads.
  **That branch is UNREACHABLE this round on two independent counts.** (i) Arm A is registry-DEAD, so
  no Bloomberg V field exists anywhere. (ii) Even with arm A alive, `_peers_v_record` `:183-184` reads
  **only** `peer_set_doc["subject"]` and `peer_set_doc["members"]` from
  `peers/v1/<key>/<as_of>.json` (`_latest_peer_set` `:118-130`). **No line of `run_scores.py` reads a
  bronze `peers-v-fields` object.** `run_scores.py`'s own docstring `:35-55` records this as a
  measured, STRUCTURAL mismatch across all 33 names and states that a MEASURED Peers V needs "either a
  Bloomberg pull of the FIELDS tuple in `peers_v.py`, or a translation layer" -- and PRD `:648-650`
  expressly forbids the translation layer. **So arm A's bronze object and arm B's consumer are not
  connected by any code at HEAD.** Unless the cell also writes the Bloomberg fields into the
  `peers/v1` object's `subject`/`members` rows (rk-50's surface, uncovered) or adds a bronze read to
  `run_scores.py` (a source change neither half names), the floor-satisfied branch cannot occur.
- "*`peers_v ABSENT` with `absent_reason` naming the floor or the missing object*" rests on arm B
  SUCCESS. The state is reachable; **the key is not** -- see 1.2(b). At HEAD the served record carries
  `reason`, not `absent_reason`, so an `absent_reason` read by the adapter or the page is undefined
  on BOTH branches.
- "*Either branch: 3 dated keys land*" rests on arm B SUCCESS. **It is wrong by count** -- see 1.4.
- There is no COO-half sentence resting on arm B DRY RUN, EMPTY or EXCEPTION. DRY RUN and EMPTY move
  nothing and need no cover. **EXCEPTION is uncovered and matters**: `write_pool`'s post-put raise
  leaves an object on S3 with the rollback step un-run, so the pre-act state must be on file BEFORE
  the first write, which the COO half's PER-KEY ROLLBACK does require.

**Floor behaviour under 5/5/3, EXERCISED on the patched copy with synthetic rows (pure function; no
vendor, no AWS):** five complete peers -> `state=MEASURED, K=5, M=[1,2,3,4,5,6]`; five peers with ONE
peer missing ONE measure's input -> that measure drops with `absent_reason` "dropped: only 4 of 5
peers carry measure 1 (FCF / mkt cap), need >= 5" and `M=[2,3,4,5,6]`; four peers -> `state=ABSENT_SOURCE,
K=4, M=[], reason="suppressed: |K|=4 (need >= 5) or |M|=0 (need >= 3)"`. **Consequence worth stating
in the order:** with SA supplying exactly 5 peers and the per-measure floor also at 5, a measure
survives only when ALL FIVE peers carry it, so `|M| >= 3` demands three measures with zero gaps
across the whole set. `MIN_PEERS_PER_MEASURE` is a `< 5` test at `:241`, so 5-of-5 is the pass and
4-of-5 is a drop. This is the ruled shape (PRD `:644-646` records the CRO's stated consequence), not a
defect -- but it makes "floor-satisfied" a materially tighter branch than "the SA call returned five
tickers".

### 1.4 WRITER CENSUS CROSS-CHECK

**The COO half prints N = 1 writer of `scores/v1/<key>/<as_of>`. I MEASURE N = 1. AGREED.**
Instrument, and it DIFFERS from the COO's (`comp-schedule` at the cut): a corpus census,
`comp-find 'SCORES_PREFIX'` -- **26 hits over 66,307 files scanned, corpus=all**, 508,169
ephemeral-floor / 1 unreadable / 3,066 binary NOT searched and so not covered by this zero. Two DEF
hits: `lib/research/scores/run_scores.py:72` and `lib/research/api/scoped_amgt.py:165`. Only the first
feeds a put (`:227` -> `:231`); `scoped_amgt.py:2410` is a READ
(`read_pool_object(SCORES_PREFIX, key)`). Cross-checked with `comp-find 'scores/v1' lib infra data
.tools portal --limit 40` -- **8 hits over 10,413 files scanned** -- whose only non-source hits are
`infra/aws/terraform/harvest/scoped-amgt-api.tf:149-161`, a `s3:GetObject` / `s3:ListBucket` READ
grant. **No writer but `run_scores.py`.**

**"No schedule writes it" -- CORROBORATED, different instrument.** `comp-find 'run_scores'` over the
same 66,307-file corpus returns **32 hits, DEF band 0**: every hit is a docstring, a ledger, an inbox
message or a tool log. No Terraform resource, no Lambda handler, no cron entry and no Python caller
references `run_scores` anywhere in the repo. It is a hand-invoked module
(`python -m lib.research.scores.run_scores`). Coverage qualifier, stated because it bounds the claim:
this census is `.gitignore`-bounded and repo-only; it is NOT evidence about a schedule that exists
only in the live AWS plane, which I did not read.

**READER census of the same property, which the COO half does not print and which the served claim
needs:** `comp-find 'read_scores'` -- 25 hits / 66,307 files -- gives ONE definition
(`scoped_amgt.py:2374`) and ONE caller (`scoped_amgt.py:2016`, `bundle["scores"] = read_scores(...)`).

**DISAGREEMENT 1 -- BLAST RADIUS, arm B: the COO half says 3 new `scores/v1` keys; the producer at
HEAD writes ONE PER CROSSWALK KEY.** `run()` derives its key list from the newest crosswalk
(`:219-220`) and has no filter (`:216`, `:241-245`). Once chain I's `rk-31` lands the three validation
names, the newest crosswalk carries **33 + up to 3 = up to 36** keys, and one bare `run_scores`
invocation writes **up to 36** dated objects, not 3.

**DISAGREEMENT 2 -- the NOT-COVERED clause forbids exactly what the unmodified producer does.** The
COO half's `NOT COVERED` reads "any `scores/v1` write on a covered name; a run over the 33". At HEAD
**a run over the 33 IS the only run `run_scores` can perform.** So either (a) the cell adds a key
filter to `run_scores.py` -- a SOURCE CHANGE this half would then have to cover and which neither
half names -- or (b) the act as written is uncovered by its own pair the moment it runs.
**Recommendation: the order must add an explicit key-selection argument to `run_scores.run()` and
`main()`, and this half must name that diff, before arm B is permitted to run live.**

**DISAGREEMENT 3 -- "the 33 covered names' `scores/v1` objects are NOT rewritten (AC5 ... unchanged by
ETag)" is TRUE of the OLD KEYS and FALSE of the SERVED VALUE.** `write_pool` never touches an existing
key when the date differs (`crosswalk.py:620-628`), so every 2026-09-17 object's ETag is indeed
unchanged -- the COO's AC5 baseline will pass. But `read_pool_object` `:1185-1191` sorts the prefix
and takes `candidates[-1]`, the NEWEST dated key, and `read_scores` `:2410` serves that one. A new
`<as_of>` object under a covered name's prefix **becomes** the newest and **changes what the Model tab
route serves for that name, immediately, with no deploy.** An ETag-on-the-old-keys discriminator
cannot see this: it would read DELTA=0 while the served value moved. **This is the shared-dependency
shape (CLAUDE.md Rule 22): the per-key arm passes and the property the keys share has moved.** The
discriminator that WOULD see it is `read_scores(<covered key>)`'s `as_of` and `peers_v` before and
after, or a `list_objects_v2` of each covered prefix comparing the LAST key, not every key's ETag.

**AGREED -- pool addressing.** "Pool objects stay at their `opal-data-harvest` prefixes, where every
reader keys" is CORRECT and does not depend on the registry gate: `POOL_BUCKET = "opal-data-harvest"`
is a hardcoded literal at `lib/research/identity/crosswalk.py:67`, re-exported at `run_scores.py:68`.
Arm B does not call `address()` at all. **Corollary the half does not draw: the REGISTRY GATE stops
arm A and has NO EFFECT ON ARM B.** A worker that reads "the live arm is DEAD" as covering the whole
cell will stop; a worker that reads it as covering only the bronze address will proceed to arm B --
and arm B is the one with the 36-key blast radius. **The order must state which arms the gate stops.**

### 1.5 WHAT THIS HALF DOES NOT COVER

- Any edit to `run_scores.py` (including the key filter recommended above) -- **a new pair.**
- Any write to `scores/v1` under a covered name, deliberate or as a side effect of an unfiltered run.
- Any bronze write to `opal-data-assets`, which is covered by NO half on either plane.
- The registry edit that lands the two R20 rows. That changes `address()`'s output for every caller in
  the estate, not only this cell, and it is `0.0.0_AB_MSTR~Z`'s act under its own pair.
- Any Bloomberg call. **UNVERIFIED and deliberately so:** I did not call Bloomberg, so I have no
  measurement of what the `FIELDS` tuple returns for `CSL AU` or `6861 JP`, and this half asserts
  nothing about field availability on a non-US line.
- Any change to `peers/v1` content (rk-50's surface), any adapter redeploy, any IAM or Terraform act,
  any schedule.
- **UNVERIFIED, reason stated:** the live pool state. I read no S3. Every count above (33 covered
  names, the newest crosswalk's key list) is taken from the COO half and from
  `run_scores.py`'s docstring `:4-6`, and is a HELD value on this plane, not a measured one. The
  worker's fresh pre-act `list_objects_v2` is the measurement, and if it disagrees with 33 the
  blast-radius arithmetic above must be recomputed before the act.

---

## 2. `AMGT-rk-52` -- the peers page serves the SA-shaped object (R14-P3; FWD-8) -- co-signed AT PROMOTE, not at build

### 2.1 THE ACT

Build only. The worker edits `portal/src/pages/SecurityAnalysis/tabs/PeersTab.tsx`,
`portal/src/pages/SecurityAnalysis/cscTable.ts` and `portal/src/pages/SecurityAnalysis/types.ts` on
its portal branch, plus one harness fixture; proves them with `./node_modules/.bin/tsc -b` and the
harness; the page is graded by a JUDGMENT criterion at L9. **No deploy, no promote, no gitlink bump.**
**This agrees with the COO half exactly.**

### 2.2 THE SOURCE DIFF

All three files exist at HEAD (`PeersTab.tsx` 8,008 bytes; `cscTable.ts` 6,194; `types.ts` 39,002).
What they do today, and therefore what "serves the SA-shaped object" must change:

- **`PeersTab.tsx:1-19`** states its own contract: it reads INTERFACE R-1 served whole on the `/peers`
  route and renders "one column per declared CSC column in R-1's order", with R-1's `csc_columns`
  map deciding present vs. absent. It consumes `usePeerSet` (`:24`), `buildCscTable` (`:27`) and the
  `PeerSet` type (`:28`). **The columns are R-1's, not the component's** -- so an SA-shaped object
  reaches the page through R-1's `csc_columns`, and the page change is a rendering change, not a
  source change.
- **`cscTable.ts:29-32`** is where the SA shape actually bites. `MEMBER_FIELD_FOR_CODE` is a hardcoded
  one-entry map, `{mkt_val_sec: 'market_cap_musd'}`, documented at `:11-18` as MEASURED on the landed
  R-1 objects on 2026-09-15 over twelve member keys. **An SA-shaped member row carries different
  keys, so every present column but Mkt Cap will render "not carried" until this map is extended.**
  PRD `C-PEER-SET-SA:623` requires 17 of 17 CSC columns with Preferred + Minority collapsed into one
  `other_cap_struct` column, and `:626` requires a per-cell `source` of `SA` | `BBG` |
  `SA_FALLBACK:<field>`. `cscTable.ts` at HEAD has no `source` concept at all. **That is the diff.**
- **`types.ts`** carries the `PeerSet` type both files import. Extending the member row and adding the
  per-cell `source` discriminant lands here.

**The change makes the code do:** render SA's 17-column shape with each cell's source labelled, rather
than the scanner-factor shape with one carried column. `tsc -b` is the mechanical check that
`types.ts`, `cscTable.ts` and `PeersTab.tsx` agree after the change.

### 2.3 THE PRODUCER'S RULE

There is no producer. The only runtime act the COO half names is **one S3 GET of
`peers/v1/CAT_US_Equity/<newest>.json` to build the fixture** -- a read, whose branches are: SERVED
(a fixture is built) or **404 / no object (the branch the half does not state)**. `CAT_US_Equity` is a
round-14 NEW validation name; the five fixtures on disk are `BABA_US_Equity`, `BA_US_Equity`,
`COST_US_Equity`, `HD_US_Equity` and `SAP_GY_Equity`
(`portal/src/pages/SecurityAnalysis/__harness__/tabsFixture.*.json`), and `peers/v1/CAT_US_Equity/`
holds an object only after rk-50 runs. **The 404 branch moves nothing and so widens nothing** -- the
blast radius is unaffected and the half stays sound -- but the worker should be told to expect it and
to fall back to an existing fixture rather than treat it as a blocker.

`tsc -b` and the harness write only build artifacts inside the portal worktree. Nothing served moves.
**AGREED with the COO half in full.**

### 2.4 WRITER CENSUS CROSS-CHECK

The COO half prints no writer census for this round because nothing is written to a served surface,
and prints **N = 1 (the integrator's push)** for the LATER promote. **I agree with both.** The three
files are portal source under `portal/`, a git submodule; the only writer of the served bundle is the
CI deploy the integrator's push to the shared branch triggers (LD-0367/0368 as the half cites).
**UNVERIFIED, reason stated:** I did not read the CI workflow or the PROD branch protection, so
"N = 1" for the promote is the COO's measurement carried forward on this plane, not independently
re-derived. It is not load-bearing this round, because this half covers no promote.

### 2.5 WHAT THIS HALF DOES NOT COVER

- The portal push, the DEV->PROD promote and the gitlink bump -- **each needs its own pair at the
  time, as the COO half says.** This half authorizes none of them.
- Any headless authenticated session (MFA blocks it as a class; card 6).
- Any change to `read_peer_set` (`lib/research/api/scoped_amgt.py:1244-1278`) or to the `/peers`
  route. The COO half's header cites that span as the whole-object read that makes
  `peers/v1/<key>/<as_of>.json` served once `rk-31`'s crosswalk lands; **I confirm the citation at
  HEAD** -- `read_peer_set` is defined at `:1244` and returns at `:1278`, serving the document whole
  via `read_pool_object(PEERS_PREFIX, ...)` at `:1262`, and `read_pool_object:1185-1191` resolves the
  NEWEST dated key. Nothing in rk-52 changes it.
- Any write to `peers/v1`.

---

## 3. SUMMARY OF DISAGREEMENTS BETWEEN THE HALVES

| # | Cell | COO half says | Source at HEAD says | Severity |
|---|---|---|---|---|
| 1 | rk-51 | 3 new `scores/v1` keys | `run()` `:216-238` has no key filter; writes one per crosswalk key (up to 36) | **BLOCKING** |
| 2 | rk-51 | NOT COVERED: "a run over the 33" | a run over the 33 is the only run the CLI `:241-245` can perform | **BLOCKING** |
| 3 | rk-51 | the 33 are not rewritten (ETag) | true of old keys; the SERVED newest object moves (`:1185-1191`, `:2410`) | **BLOCKING** |
| 4 | rk-51 | fixes the `absent_reason` defect at `:270-277` | the key is `reason`, and is absent entirely on the MEASURED branch `:277` | material |
| 5 | rk-51 | floors amended per C-PEERS-V-FLOORS | `:69-70` asserts trip at import unless also edited (EXERCISED) | material |
| 6 | rk-51 | "floor-satisfied" outcome | no code path connects arm A's bronze to `_peers_v_record` `:183-184`; branch unreachable | material |
| 7 | rk-51 | registry gate -> "the builder still prints `opal-data-assets`" | true for `global`; `amgt` RAISES and prints no line | minor |
| 8 | rk-51 | gate makes "the live arm DEAD" | it stops arm A only; arm B never calls `address()` (`crosswalk.py:67`) | material |
| 9 | rk-50 (uncovered) | -- | `peers/v1` gains a 2nd writer (`engine.py:76` + rk-50) and posture reads it | needs its own pair |
| 10 | rk-52 | one S3 GET of `CAT_US_Equity`'s newest | 404 branch unstated; CAT has no fixture and no object until rk-50 runs | minor |

**Nothing in this draft is signed.** Items 1-3 should be resolved in the ORDER before rk-51 is
spawned, because each is a place where the act as the pair describes it and the act the code performs
are different acts.

Drafted `1.0.0_SA_CTO~Z`, 2026-09-18. Repo HEAD `c898937600` (SITEZ); COO counterpart @`9a6aa12da2`;
registry `c1cf124537835573`.

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


## CTO SIGNATURE -- chain P

**Drafted by a reviewing subagent of this seat; the BLOCKING item was RE-VERIFIED at source by `1.0.0_SA_CTO~Z`:**
`lib/research/scores/run_scores.py:216-238` -- `run(as_of, client, dry_run)` derives its key list from the NEWEST crosswalk
(`:219-220`) and writes one object per key (`:227`, `:231`); `main()` exposes only `--as-of` and `--dry-run` (`:241-245`).
There is no key filter at HEAD.

- `AMGT-rk-52`: **SIGNED.**
- `AMGT-rk-51` arm B: **WITHHELD.** The COO half signs "3 new `scores/v1` keys"; the only run this producer can perform is
  over EVERY keyed name -- 33 today, 36 once `rk-31` lands its three -- while the same half's NOT-COVERED clause forbids
  exactly that run, so the cell as signed is unexecutable in both directions at once. A key filter is a SOURCE CHANGE
  neither half names. **And the stated discriminator is blind to it:** the reader takes the newest dated key
  (`read_pool_object:1185-1191`, served at `read_scores:2410`), so a new dated key moves the Model tab's served value with
  no deploy while a per-key ETag check reads DELTA = 0. **TO SIGN:** the cell adds the key filter, the half re-states the key
  set as the three, and the discriminator reads the SERVED value rather than per-key ETags.
- Arm A's registry gate stops arm A only; arm B never calls `address()` (`crosswalk.py:67` hardcodes the bucket), so the
  standing clause above binds arm B by reading, not by gate.

Signed `1.0.0_SA_CTO~Z`, 2026-09-18, against the COO halves at `9a6aa12da2`.

---

## RE-SIGNATURE -- 2026-09-18 ~23:3xZ, against the COO halves at `541d395e0d` (msg 23855's re-cut)

`2.0.0_SA_COO~Z` bound every withheld condition in the order text and restated it in its halves. This seat read the
BOUND TEXT at `541d395e0d`, not the message's summary of it, before lifting each withholding.

- **`AMGT-rk-51` arm B: WITHHOLDING LIFTED -- SIGNED.** Step 3b makes the key filter a NAMED SOURCE CHANGE:
  `run(security_keys=...)` plus a repeatable `--security-key`, with a bare run REFUSING unless `--all-keyed` (never
  passed), unit-tested (`541d395e0d` chain P `:25-28`). The key set is now the three validation names, which is what the
  half signs. The discriminator is re-cut to `rerun_of_covered_today 0 of 33` -- no new dated key for a covered name --
  instead of a per-key ETag, which my half measured as blind to this act because the reader takes the newest dated key.

Re-signed `1.0.0_SA_CTO~Z`, 2026-09-18 ~23:3xZ.
