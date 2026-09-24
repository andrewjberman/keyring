# AMGT_RESAPP task order -- `AMGT-rk-53` -- no rank without signal; every EMPTY generation carries `empty_reason`, written by BOTH generation writers through ONE shared pointer builder, carried by the adapter and shown on the panel

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-53</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~53</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the existing daily
  chatter schedule (aws_scheduler_schedule.chatter_axis_daily, cron 10:00 UTC, chatter-axis-schedule.tf:172-184) is
  neither read nor written; the one producer run this order names is a --dry-run that writes nothing; the
  no-monitor moratorium is unaffected.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs NO live AWS write and NO deploy: its live acts are two
  READS of the existing metrics table opal-harvest-security-metrics (GetItem on the _CURRENT pointer and a Query
  of the served partition, AC7) under the device's existing credentials; it grants no permission, provisions no
  resource and touches no Terraform. The redeploy of the two Lambdas this cell's bytes feed is the COO's ONE
  consolidated deploy after the drains, under its own CTO+COO never-widen pair (section 4).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~53`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the paths in
section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~53;`. **NEVER RUN AN INSTALL** (`bun install` against the EXISTING
`portal/bun.lock` is the one exception, and only if your worktree's `portal/` is populated -- see section 4).

## 1. THE CELL, inlined in full -- `AMGT-rk-53` (R14-L1; FWD-15, L2, L5, V8/D25; `C-SERVER-SIDE-RANKING`)

**The analysis row, verbatim (`ROUND_ANALYSIS.round13.md` s.4 @9c8e04cd9a, row R14-L1 `:139`):** *"a ranking never
includes a member with no signal; every EMPTY generation carries `empty_reason`, written by BOTH generation writers
and shown on the panel"* -- serves FWD-15, L2, L5, V8/D25; co-sign YES (the co-sign covers the COO's consolidated
deploy, section 4, not an act of yours).

**The ratified rule, PRD v0.13 @1699960261 `C-SERVER-SIDE-RANKING` (`:1142-1160`), verbatim in the parts that bind
this cell (`:1150-1160`):** *"NO RANK WITHOUT SIGNAL. A ranking never lists a member with no signal ... Signal, per
subject: CHATTER -- at least one article for the name in the window (score above zero); PRICE -- at least two
observations in the window, the movement gate's own `INSUFFICIENT_OBSERVATIONS` test. A SUCCESSFUL run whose every
member lacks signal, or fails its breakout test, publishes an EMPTY generation carrying `empty_reason`: the dominant
exclusion reason and its count over the printed denominator (today Breakout x Chatter computes
`BELOW_MIN_ABSOLUTE_JUMP` for 191 of 191 and discards it). A FAILED run is not EMPTY: it stays a failure and the
prior generation stays current, as `C-RANKING-GENERATION` already requires. `empty_reason` is part of the pointer
contract: BOTH generation writers (`lib/research/metrics/chatter_axis.py`, `lib/research/price/generation.py`) write
it through ONE shared pointer builder in place of today's two copies, it is covered by the generation's
`payload_hash`, and the adapter carries it to the panel, which shows it in place of an empty list."*
`C-RANKING-GENERATION` (`:566-580`) stays as written: an immutable generation plus a current pointer; zero winners, a
changed winner and a failed write are three DISTINGUISHABLE states.

**THE MEASURED STATE, at HEAD (`chatter_axis.py` last moved @fda8d96c0a, `generation.py` @f838560c46,
`scoped_amgt.py` @e2d89be7da -- cite these lines, do not re-derive them from memory):**
- `lib/research/metrics/chatter_axis.py`: `normalize_scores()` `:400-427` maps an all-equal (all-zero) raw set to
  `score_min` for every member (`:420-421`); `rank_top_n()` `:434-453` sorts by `(-score, key)` and takes the first
  `top_n` -- so ten zero-signal names rank in ALPHABETICAL order and look finished. The product loop in
  `compute_chatter_axis()` (`:779-882`; loop `:812-848`) computes `window_totals` at `:807` and passes it only as row
  detail (`:819`), never as a filter; the movement gate's `excluded` dict is carried on the product (`:846`) and
  NEVER reaches the pointer. Measured on the 18 Sep generation (Lead Panel brief intake L2, L5; validation D25):
  Trending x Chatter ranks ten rows with `window_total_count 0` and `score 0` (Keyence #2, CAT #10 with zero
  articles); Breakout x Chatter computes `BELOW_MIN_ABSOLUTE_JUMP` for 191 of 191 (`movement_gate.py:430`) and the
  reason is discarded at the commit. The existing test arm
  `lib/research/metrics/tests/test_chatter_axis.py:355-407`
  (`test_compute_chatter_axis_all_zero_signal_ranks_trending_and_empties_breakout`) ASSERTS today's behaviour --
  `rows_ranked == TOP_N == 10` on an all-zero input -- and is REWRITTEN by this cell, never deleted silently.
- The generation carrier is declared TWICE. In `chatter_axis.py`: constants `:142-150`, `GenerationWriteError`
  `:155`, `payload_hash()` `:541-563`, `new_run_id()` `:566`, `new_generation_id()` `:572`, `build_pointer()`
  `:579-615`, `build_failed_marker()` `:618-635`, `assert_pointer_is_index_invisible()` `:638-653`,
  `build_generation()` `:656-701`, `default_write_generation()` `:704-776`. In `lib/research/price/generation.py`:
  *"declared again here rather than imported"* (`:93`), constants `:96-104`, `payload_hash()` `:276-292`,
  `build_pointer()` `:321-355`, `build_failed_marker()` `:358-375`, `build_generation()` `:378-412`,
  `default_write_generation()` `:418-481`. `compute_price_axis()` `:489-594` already excludes thin BREAKOUT series
  (`:516-530`, `REASON_THIN_SERIES` `:108`) and `movement_scores()` excludes `NO_OBSERVATIONS`
  (`movement_gate.py:452`) and `INSUFFICIENT_OBSERVATIONS` (`:412`) -- so the PRICE subject already has the signal
  test the PRD names; what it lacks is `empty_reason` on the pointer.
- `lib/research/api/scoped_amgt.py`: `generation_fields()` `:404-417` carries exactly six pointer fields to the
  response and no `empty_reason`; `_ranking_reason()` `:474-500` renders an EMPTY generation as *"a successful
  ranking with no members"* (`:484-487`) with no reason; `RANKING_EMPTY` `:193`; `read_rankings()` `:541`. The adapter
  imports `chatter_axis` AS `generation_writer` (`:116`, `:179-181`, `:379`) -- that alias is the natural home of
  the ONE shared builder. The lead-panel rankings route is `handler()` `:3285-3290`.
- `portal/src/pages/SecurityAnalysis/components/RankedList.tsx:179-186` (portal nested repo, branch DEV @625a0888):
  the EMPTY branch renders a fixed sentence and reads no reason; `types.ts:176-194` (`RankingSet`) carries
  `ranking_reason` (`:190`) and no `empty_reason`.

**RULED, what you build (four surfaces):**
1. **One shared pointer builder.** Move the generation carrier -- `POINTER_TICKER`, `FAILED_MARKER_PREFIX`, the
   three `STATE_*`, `GENERATION_STATES`, `INDEX_ROW_ATTRIBUTES`, `GenerationWriteError`, `generation_partition`,
   `payload_hash`, `new_run_id`, `new_generation_id`, `assert_pointer_is_index_invisible`, `build_pointer`,
   `build_failed_marker`, `build_generation`, `default_write_generation`, `_to_dynamodb_item` -- into ONE module
   `lib/research/metrics/generation_writer.py`. BOTH writers import from it and delete their copies; every public
   name stays importable from both `chatter_axis` and `price.generation` (re-export), so no caller moves.
   `payload_hash` gains an `empty_reason=None` keyword and folds it into the hashed blob when present
   (`C-SERVER-SIDE-RANKING`: *"covered by the generation's `payload_hash`"*). `build_pointer`/`build_generation`
   gain `empty_reason=None`; a `STATE_EMPTY` generation REFUSES (`ValueError`) without one; a `STATE_COMPLETE`
   generation refuses WITH one. The pointer item carries `empty_reason` as a map
   `{"reason": <str>, "count": <int>, "denominator": <int>}` -- the dominant exclusion reason, its count, over the
   candidates considered. `METRICS_TABLE`'s env knob stays where each writer reads it today.
2. **CHATTER signal filter.** In `compute_chatter_axis()`'s product loop, before `normalize_scores`, drop every key
   whose `window_totals[key] == 0` into `excluded[key] = "NO_SIGNAL_IN_WINDOW"` (the PRD's chatter signal: at
   least one article for the name in the window). Rank only the remainder. A product with no remaining member
   builds an EMPTY generation whose `empty_reason` is the dominant reason in `excluded` (ties broken by reason
   name), `count` its count, `denominator` the candidates considered. `main()`'s per-product line (`:1028-1038`)
   and `_print_generation` (`:931-978`) print, per product, `SIGNAL rows_ranked=N rows_with_zero_signal=Z
   excluded_no_signal=K of candidates=C` and, on an EMPTY product, `empty_reason=<reason> <count> of
   <denominator>`. `TOP_N`, `WINDOW_DAYS` and the score scale (chatter_gate.py) do not move.
3. **PRICE `empty_reason`.** `compute_price_axis()` passes the same dominant-reason summary of its `excluded` dict
   (thin series plus the movement gate's own refusals) into `build_generation` when `rows` is empty.
4. **Adapter and page.** `generation_fields()` carries `empty_reason` from the pointer (None when absent);
   `_ranking_reason()` for `RANKING_EMPTY` appends the reason when present (`"... no members -- empty_reason:
   BELOW_MIN_ABSOLUTE_JUMP 191 of 191"`). `types.ts` `RankingSet` gains `empty_reason?: {reason: string; count:
   number; denominator: number} | null`; `RankedList.tsx`'s EMPTY branch (`:179-186`) renders the reason and its
   count over its denominator in place of the fixed sentence when `empty_reason` is present (the fixed sentence
   stays as the fallback for a pre-contract pointer). Portal edits are COMMIT YES / PROMOTE NO.

**What this cell does NOT change:** the movement formulas and reasons (`movement_gate.py` -- read only);
`MIN_ABSOLUTE_JUMP` for PRICE (`C-PRICE-BREAKOUT-FLOOR`, PRD `:1166`, is the COO's direct act, NOT this cell); the
pointer's partition/key scheme; any prior generation; the live table (nothing is written to it by this order).

**THE VALIDATION BAR (`C-VALIDATION-NAMES`, PRD v0.13 `:1652-1658`):** this cell is proven on a DRY RUN and on
planted members (AC1-AC5) and on IN-PROCESS invocations of the adapter's `handler()` on your worktree's bytes
(AC4, AC7), never on a fleet run, a re-run, or a deploy. The `--dry-run` at AC5 reads the pool and writes nothing.

## 2. WHERE THIS CAME FROM

**ROUND 14**, decomposition s.22 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s L10 round-13 analysis
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round13.md` @9c8e04cd9a s.4 row R14-L1 (`:139`) and the
co-sign discipline (`:158-160`); the Lead Panel brief intake rows L2 and L5
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md:43,46`) and
validation D25 (`:341`). PRD v0.13 @1699960261: `C-SERVER-SIDE-RANKING` (`:1142-1160`), `C-RANKING-GENERATION`
(`:566-580`), `C-VALIDATION-NAMES` (`:1652-1658`), `C-PRODUCTION-HOME` (`:1643-1650`); FWD-15 (`:406-410`).

**ISSUER RULE -- WHERE THE NEVER-WIDEN PAIR LIVES (`2.0.0_SA_COO~Z`, at the cut):** this order is CO-SIGNED. The pair
for chain L is TWO ledger files, one section per cell: the COO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_L_COO_HALVES.md` and the CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_L_CTO_HALVES.md`. "The pair is on file" MEANS: both
files exist in your worktree, each carries a section headed `AMGT-rk-53`, and that section names this order's blast radius
and the per-key rollback. Read both before your first live act and paste both files' sha256 into your report. Either file
absent or its `AMGT-rk-53` section missing: run the read-only, offline and in-process criteria, file a BLOCKING row
(disarm_owner `2.0.0_SA_COO~Z`), and STOP -- never act on one half. ADAPTER SINGLE-WRITER QUEUE: this order does NOT
redeploy `opal-amgt-scoped-api`; its adapter bytes reach the served plane in the NEXT adapter cell's redeploy (`AMGT-rk-61`,
cut from HEAD after this order drains), whose pre/post 13-route census covers them; this order's served-behaviour claims
are proven IN-PROCESS on the worktree bytes as the criteria state.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/metrics/chatter_axis.py
lib/research/metrics/generation_writer.py
lib/research/metrics/tests/
lib/research/price/generation.py
lib/research/price/tests/
lib/research/api/scoped_amgt.py
lib/research/api/tests/
portal/src/pages/SecurityAnalysis/components/RankedList.tsx
portal/src/pages/SecurityAnalysis/types.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~53/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-53.no-rank-without-signal.md
org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_L_*_HALVES.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read `lib/research/metrics/movement_gate.py`,
  `lib/research/metrics/chatter_gate.py`, `infra/aws/terraform/harvest/chatter-axis-schedule.tf`,
  `infra/aws/terraform/harvest/lambda_src/build_zip.py` and
  `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` freely -- the first packages the chatter Lambda by
  IMPORT CLOSURE (`build_zip.py:186`), the second seeds `lib/research/metrics/` whole (`:139`), so the new module
  travels in both zips without a build edit); this block governs WRITES. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~53 <0.9.0_WK_AMGT_RESAPP~53@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`. The
  portal edit is committed INSIDE the portal repo (branch DEV) with the same author line; the superproject gitlink
  is NOT bumped by you.
- **NO DEPLOY BY THIS ORDER.** Never `build_zip.py` + `safe-apply`, never `build-and-upload-scoped-amgt.sh`, never
  `aws lambda update-function-code`, never a live invoke of either function. The redeploy is the COO's (section 4).

## 4. BOUNDS

**BUILD AND PROVE IN-PROCESS; THE COO DEPLOYS.** This cell's bytes feed two Lambdas (`amgt-resapp-chatter-axis` and
`opal-amgt-scoped-api`). RECONCILED BY THE ISSUER: `opal-amgt-scoped-api` is redeployed by `AMGT-rk-61` (cut from HEAD after this order drains, carrying these bytes); `amgt-resapp-chatter-axis` is redeployed ONCE by `2.0.0_SA_COO~Z` after this order drains, under the chain L pair. The older sentence read: both redeployed once by the COO after this order and `AMGT-rk-61` have
drained, under ONE fresh CTO+COO never-widen pair naming the blast radius -- the next EMPTY pointers carry
`empty_reason`, the Trending x Chatter membership SHRINKS to signal-carrying names (possibly to EMPTY), the ranking
response gains one field, the `/security/{key}/*` router changes -- with a rollback read from the LIVE pre-act
`CodeSha256` of EACH function, its change-management entry opened before the first live act. None of that is
yours: your served criteria are IN-PROCESS invocations of `handler()` on the worktree bytes (AC4, AC7).
**SINGLE-WRITER SURFACE:** `lib/research/api/scoped_amgt.py` is edited this round by this order (`generation_fields`,
`_ranking_reason`) and by `AMGT-rk-61` (slot ~61, `handler()`'s `/security` arm) -- disjoint regions of one file.
The COO sequences the two drains; if the spawn prompt says the other edit has landed at HEAD, confirm your worktree
carries it (`git log --oneline -3 -- lib/research/api/scoped_amgt.py`) before you touch the file, or STOP with a row.
PORTAL: COMMIT YES / PROMOTE NO -- DEV serves nothing by design; your page edit is durable, not reachable. **THE
PORTAL DEV PUSH IS RESERVED.** If your worktree's `portal/` is an EMPTY gitlink directory (row
`AMGT_RESAPP-Z-W31-S1`), do NOT reconstruct it: the issuance says whether portal cells run in a worktree provisioned
by `AMGT-rk-60` or in the main tree; file a row and REFUSE AC6 on the page half only; the producer, builder and
adapter halves proceed. **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification or freshness
checker.** Secrets through `comp-secrets` only. **No vendor call** (none is named; the price writer is exercised
OFFLINE on a synthetic series, never through Bloomberg). No non-ASCII in anything you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- the served Trending x Chatter
zero-signal row count (10 of 10 at the cut) and the Breakout x Chatter `excluded` count (191 of 191 at the cut) are
re-measured at spawn by AC7 and AC5; they may have moved.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W53-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-53"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/metrics/tests -q 2>&1 | tail -15</invocation><expect>the battery passes (a final line "N passed", 0 failed) and it carries three NEW arms you add under lib/research/metrics/tests/ using compute_chatter_axis with an injected count_fn and a small universe file: (a) a planted member whose 30-day counts are ALL ZERO is never ranked and appears in the product's excluded dict as NO_SIGNAL_IN_WINDOW while a planted member with one article IS ranked; (b) an input where EVERY member is zero-signal yields state EMPTY on BOTH chatter products with empty_reason {reason: NO_SIGNAL_IN_WINDOW, count: n, denominator: n}; (c) a STATE_EMPTY generation built without empty_reason raises ValueError and a COMPLETE one built with it raises ValueError -- and the pre-existing arm test_compute_chatter_axis_all_zero_signal_ranks_trending_and_empties_breakout (test_chatter_axis.py:355-407 at HEAD) is REWRITTEN to assert rows_ranked 0 on an all-zero input, never deleted; the arm names print their denominators (n of n)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-53"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/price/tests -q 2>&1 | tail -15</invocation><expect>the battery passes (a final line "N passed", 0 failed) and it carries two NEW arms in lib/research/price/tests/test_generation.py on compute_price_axis with write_fn=None: (a) a planted 1-observation series is excluded (INSUFFICIENT_OBSERVATIONS or NO_OBSERVATIONS from the movement gate on TRENDING; INSUFFICIENT_INTERIOR_SERIES_FOR_TRAILING_BASELINE on BREAKOUT) and never ranked while a planted 5-observation series is; (b) an all-thin input yields a BREAKOUT_PRICE generation with state EMPTY and empty_reason {reason: INSUFFICIENT_INTERIOR_SERIES_FOR_TRAILING_BASELINE, count: n, denominator: n}, its pointer carrying the map</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-53"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.metrics import chatter_axis as c, generation_writer as g
from lib.research.price import generation as p
names = ['build_pointer', 'build_generation', 'build_failed_marker', 'default_write_generation', 'payload_hash', 'assert_pointer_is_index_invisible', 'generation_partition']
same = [n for n in names if getattr(c, n) is getattr(g, n) and getattr(p, n) is getattr(g, n)]
print('shared_builder_names', len(same), 'of', len(names), same)
h0 = g.payload_hash([])
h1 = g.payload_hash([], empty_reason={'reason': 'NO_SIGNAL_IN_WINDOW', 'count': 4, 'denominator': 4})
h2 = g.payload_hash([], empty_reason={'reason': 'BELOW_MIN_ABSOLUTE_JUMP', 'count': 4, 'denominator': 4})
print('hash_discriminates_empty_reason', len({h0, h1, h2}), 'of 3 distinct')
import io
for f in ('lib/research/metrics/chatter_axis.py', 'lib/research/price/generation.py'):
    t = io.open(f, encoding='utf-8').read()
    print(f, 'def build_pointer', t.count('def build_pointer('), 'def payload_hash', t.count('def payload_hash('))
"</invocation><expect>shared_builder_names 7 of 7 -- every carrier name resolves to the SAME function object from chatter_axis, price.generation and generation_writer (one builder, two re-exports) -- hash_discriminates_empty_reason 3 of 3 distinct (empty_reason is covered by payload_hash), and both writer files print def build_pointer 0 def payload_hash 0 (the copies are gone; at HEAD each file prints 1 and 1)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-53"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/api/tests/test_generation_and_pool_routes.py -q 2>&1 | tail -15</invocation><expect>the battery passes (a final line "N passed", 0 failed) and it carries one NEW arm: an EMPTY _CURRENT pointer carrying empty_reason {reason: BELOW_MIN_ABSOLUTE_JUMP, count: 191, denominator: 191} on a patched _dynamodb is served THROUGH handler() with a real event (rawPath /api/scoped/amgt/lead-panel/rankings/breakout/chatter, httpMethod GET, headers X-Firm-Id) at statusCode 200 with payload empty_reason equal to that map and ranking_reason containing "BELOW_MIN_ABSOLUTE_JUMP 191 of 191", while a COMPLETE pointer serves empty_reason None -- the existing arm test_6_an_EMPTY_pointer_is_an_empty_membership_distinct_from_ABSENT (:199) still passes unchanged</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-53"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import subprocess, sys, re
r = subprocess.run([sys.executable, '-m', 'lib.research.metrics.chatter_axis', '--dry-run'], capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=110)
out = r.stdout + r.stderr
print(out[-4000:])
sig = re.findall(r'SIGNAL rows_ranked=(\d+) rows_with_zero_signal=(\d+) excluded_no_signal=(\d+) of candidates=(\d+)', out)
print('signal_lines', len(sig), 'of 2 products; zero_signal_rows_total', sum(int(s[1]) for s in sig))
print('empty_reason_lines', len(re.findall(r'empty_reason=[A-Z_]+ \d+ of \d+', out)))
print('rc', r.returncode)
"</invocation><expect>rc 0 and the line "NO LIVE WRITE: --dry-run; rows_written=0 pointers_written=0"; signal_lines 2 of 2 products; zero_signal_rows_total 0 -- no ranked row on either chatter product has window_total_count 0 -- and every product whose rows_ranked reads 0 prints an empty_reason line with its count over the candidates denominator (Breakout x Chatter is expected EMPTY with BELOW_MIN_ABSOLUTE_JUMP 191 of 191 at the cut, Trending x Chatter expected to shrink to the names with links; re-measure); this is the C-VALIDATION-NAMES dry run, no write anywhere</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-53"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && python -c "
import io
for f in ('src/pages/SecurityAnalysis/components/RankedList.tsx', 'src/pages/SecurityAnalysis/types.ts'):
    t = io.open(f, encoding='utf-8', errors='replace').read()
    print(f, 'empty_reason', t.count('empty_reason'))
" && ./node_modules/.bin/tsc -b 2>&1 | tail -20; echo tsc_rc=${PIPESTATUS[0]}</invocation><expect>empty_reason occurs at least once in RankedList.tsx and at least once in types.ts (both read 0 at HEAD), and tsc -b reports no NEW TypeScript error attributable to the two edited files (tsc_rc 0, or an rc whose listed errors predate this order and are named as such); if portal/ is an empty gitlink in this worktree this criterion is REFUSED with a row citing AMGT_RESAPP-Z-W31-S1, never satisfied from the main tree by hand</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rk-53"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import json
from lib.research.api import scoped_amgt
for m in ('trending', 'breakout'):
    ev = {'rawPath': '/api/scoped/amgt/lead-panel/rankings/%s/chatter' % m, 'httpMethod': 'GET', 'headers': {'X-Firm-Id': 'bd'}}
    r = scoped_amgt.handler(ev)
    p = json.loads(r['body'])
    rows = p.get('rows') or []
    zero = [x for x in rows if int(x.get('window_total_count', 0) or 0) == 0]
    print(m, 'status', r['statusCode'], 'ranking_status', p.get('ranking_status'), 'as_of', p.get('as_of_date'), 'generation', p.get('generation_id'))
    print(m, 'zero_signal_rows', len(zero), 'of row_count', len(rows), 'empty_reason_key_present', 'empty_reason' in p, 'empty_reason', json.dumps(p.get('empty_reason')))
"</invocation><expect>an IN-PROCESS invocation of handler() on THIS WORKTREE'S bytes against the LIVE metrics table (two GetItem reads plus one partition Query; nothing written): both routes status 200; empty_reason_key_present True on BOTH payloads (the field the adapter now carries; at HEAD the key is absent) with empty_reason null on every PRE-DEPLOY pointer (the live pointers were written by the un-redeployed producer); the PRE-ACT baseline the COO's deploy will move is printed and recorded: trending zero_signal_rows N of row_count N (10 of 10 at the cut; re-measure) and breakout ranking_status EMPTY with empty_reason null -- this criterion proves the ADAPTER on the worktree bytes and the baseline, never the deployed plane</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order. Every criterion runs BEFORE any deploy; there is no post-deploy criterion on this order -- the served
read after the COO's consolidated deploy is the COO's change-management entry's closing read.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~53/AMGT_RESAPP.TO-AMGT-rk-53.no-rank-without-signal.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); flip
`<status>` to `complete`; commit with `--only -- <paths>`. Report once, naming the pre-act baseline AC7 printed
so the COO's never-widen pair can carry it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>14</round>
<slot>~53</slot>
<fabric>site-z</fabric>
