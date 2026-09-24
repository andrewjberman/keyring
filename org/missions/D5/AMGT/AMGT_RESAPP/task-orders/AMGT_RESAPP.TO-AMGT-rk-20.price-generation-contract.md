# AMGT_RESAPP task order -- `AMGT-rk-20` -- the price producer conforms to the reader's completeness contract; the 2026-09-15 rows are republished

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-20</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~27</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence; the standing
  collection-stays-off / no-monitor moratorium is unaffected and no schedule is read or written.
comp-iam: DECLARED-NOT-APPLICABLE -- this order writes only to already-provisioned resources (the existing
  S3 bucket/prefixes and DynamoDB table this project already reads and writes) under the existing Lambda
  execution role; it grants no new permission and provisions no new resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~27`, continuing.** You hold `AMGT-rk-19`'s adapter half already drained; this
is the THIRD of six orders in chain B's queue (reordered at the cut -- `AMGT-rk-30` now runs second, for
throughput). Your first act this order re-confirms
`git rev-parse --abbrev-ref HEAD` and that the paths below exist.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~27;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-20` (FWD-15; S137/S144; RULED at s.3.2: "the producer conforms to the reader; the reader does not loosen")

**THE MEASURED STATE.** `integrations/bloomberg/research/price_axis_pull.py` writes rows via
`build_movement_rows()` (`:167-231`) into a bare `axis_date = f"{axis}#{as_of_key}"` partition through a
direct `put_item()` loop (`:337-346`) -- **zero occurrences of `_CURRENT`, `generation_id` or
`GENERATION_COMPLETE`** anywhere in the file. The reader's completeness contract
(`read_generation_pointer()`, `scoped_amgt.py:376`; `_find_latest_served_pointer()`, `:509`) requires a
`ticker='_CURRENT'` sort-key pointer with `generation_id` and `state == GENERATION_COMPLETE` before ANY
pointer-based reader can see a generation as done. The producer never writes it, so its real, complete
2026-09-15 rows (32 tickers, previously verified) are structurally invisible, and `read_rankings()`
(`:535`) falls back to 2026-09-10, `dated: true`.

**RULED, and the reader is NOT touched:**
1. `price_axis_pull.py` routes its writes through `lib.research.price.generation.compute_price_axis()`
   (replacing `build_movement_rows()` and the `:337-346` write loop), mirroring
   `lib/research/metrics/chatter_axis.py`'s own WORKING chain: `build_generation` (`:656`),
   `default_write_generation` (`:704`), `compute_chatter_axis` (`:779`), wired in `main()` at
   `:1006-1010` with `write_fn = None if args.dry_run else default_write_generation`. **This is the real
   precedent to copy -- NOT `model_block_pull.py`, which does not use `generation.py` at all** (a correction
   made and applied fresh at this cut, not carried forward from a stale assumption).
2. The landed 2026-09-15 rows are REPUBLISHED, never re-pulled (no vendor call). Write a NEW function
   (do not extend `backfill_legacy_generation.py`'s existing `compute_price_axis()`-based recompute path,
   which is LOSSY for `BREAKOUT_PRICE#` rows -- their already-good `baseline_mean`/`pct_jump` were computed
   from the full interior series at pull time, and feeding only their bare 2-point shape back through
   `compute_price_axis()` would fall below `min_breakout_observations` and demote them). The new function:
   generalise `backfill_legacy_generation.py`'s `read_legacy_partition()` axis literal to read the bare
   `TRENDING_PRICE#2026-09-15` and `BREAKOUT_PRICE#2026-09-15` partitions verbatim, attach
   `security_key`/`identity_status` via `build_identity_index()`, hand-construct a generation dict matching
   `build_generation()`'s exact return shape directly from the already-ranked rows (skip `build_rows`, which
   expects raw `ranked`+`detail`, not fully-formed rows), and call `default_write_generation()` directly.
   `as_of_date` is kept as the date the prices are FOR (2026-09-15), never today's run date.
3. This republish moves the Lead Panel's served date -- served output, **fresh never-widen co-sign**, ledger
   entry opened before the first live act, rollback read from the LIVE pre-act hash of THIS act.
4. **Criterion:** the page's own Price call (`read_rankings()`, `scoped_amgt.py:535`) returns `as_of_date`
   2026-09-15, `dated: false`. Store existence alone is not the bar.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.3.2 @`9419550eb1`, rows
`AMGT_RESAPP-Z-S137`/`S144`. PRD v0.10, ADMITTED, s.3.2 is cut-level, no PRD change.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/price_axis_pull.py
lib/research/price/backfill_legacy_generation.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-20.price-generation-contract.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You may READ `lib/research/price/generation.py` and
  `lib/research/metrics/chatter_axis.py` freely (they are your precedent, not your grant to edit) but WRITE
  only the two files above among repo files. **`lib/research/api/scoped_amgt.py` is NOT in your grant for
  this order** -- the reader is explicitly not touched. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~27 <0.9.0_WK_AMGT_RESAPP~27@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

Same standing bounds as your prior order this chain: PORTAL FROZEN (not your surface); COLLECTION STAYS OFF;
NO alarm/monitor/notification; secrets through `comp-secrets` only; **no vendor call** (this order republishes
already-landed rows -- no Bloomberg pull); no non-ASCII; **PUSH: never**. **THE REFUSAL CLAUSE:** a criterion
you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never repaired, widened, or satisfied
by a route this order did not name. **A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its
denominator.** **SURPRISE ROWS:** your row continues `AMGT_RESAPP-Z-W27-S<k>` from wherever your prior order
left off; `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row; append by textual splice
inside the one fenced JSON array (never re-serialize it) and never edit an existing row. **Found something
off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-20"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.api.scoped_amgt import read_rankings
result = read_rankings('BREAKOUT', 'PRICE', None, 20)
print('as_of_date', result.get('as_of_date'))
print('dated', result.get('dated'))
"</invocation><expect>BEFORE this order's republish runs, as_of_date reads 2026-09-10 and dated reads true (the pre-fix baseline this criterion also records); AFTER the republish, as_of_date reads 2026-09-15 and dated reads false -- the worker records BOTH runs, before and after, of this exact invocation</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-20"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3
table = boto3.resource('dynamodb').Table('<the price generation table -- name it from generation.py's own default table_name at the cut>')
resp = table.get_item(Key={'axis_date': 'BREAKOUT_PRICE#2026-09-15', 'ticker': '_CURRENT'})
item = resp.get('Item')
print('pointer_exists', item is not None)
print('generation_id', (item or {}).get('generation_id'))
print('state', (item or {}).get('state'))
"</invocation><expect>after the republish, a `_CURRENT` pointer exists for `BREAKOUT_PRICE#2026-09-15` with a real `generation_id` and `state == GENERATION_COMPLETE` -- the worker replaces the table name placeholder with the real one read from `generation.py`'s own default before running this, and records that substitution</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~27/AMGT_RESAPP.TO-AMGT-rk-20.price-generation-contract.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. **Do not stop here** -- `AMGT-rk-23` is handed to you next as a
continuation; wait for it.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->
<!-- added by the issuer 2.0.0_SA_COO~Z 2026-09-19 on row AMGT_RESAPP-Z-W57-S2: this round-13 order was terminal-by-proof (VALID instance, graded at L9) but carried no record face, so a --round-filtered acceptance read could not see it -->
<status>complete</status>
<round>13</round>
<slot>~27</slot>
<fabric>site-z</fabric>
