# AMGT_RESAPP task order -- `AMGT-rk-24` (producer half) -- the batch's own promised UNRESOLVED-SOURCE objects, actually written

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-24</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~33</issued_to>
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

**You are `0.9.0_WK_AMGT_RESAPP~33`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. **YOU HOLD CHAIN FP-B, ONE order.** (Split from a single "chain FP" at the cut, for throughput: this
order touches only `batch.py`; a sibling order on a SEPARATE chain FP-A, `0.9.0_WK_AMGT_RESAPP~26`, touches
only `analyze.py` -- disjoint files, safe to run concurrently.) Your first act prints
`git rev-parse --abbrev-ref HEAD` and confirms `org/`, `.tools/` and `lib/research/filings/batch.py` exist at
the paths below; if any is absent, STOP with a BLOCKING row.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~33;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-24` producer half (FWD-18; S139 corrected by S146)

**THE MEASURED STATE, from row `AMGT_RESAPP-Z-S146`** (correcting the seat's own earlier `S139`): the store
already carries a NAMED no-CIK marker for all 21 unfiled names (`universe/v1/2026-09-16.json`'s
`filing_identity: {cik: null, form_expected: none, source: none}`), and `AMGT-rk-18` AC2/AC3 correctly graded
their named-reason arm on THAT carrier through `batch.py`'s own `plan()` function -- not on a log line, and
the reasoning was already sound. **What survives is narrower and still real:** `batch.py`'s `plan()`
(`:80-111`) correctly computes the `unresolved` list, and its log line at `main()` promises
`"UNRESOLVED-SOURCE: %d name(s), each an explicit object at .../UNRESOLVED-SOURCE.source.json"` -- but
`main()` (`:159-202`) only ever iterates `planned["fetchable"]`. **`planned["unresolved"]` is computed and
printed as a count, and then never iterated. Not one `UNRESOLVED-SOURCE.source.json` object is ever written.**
The page's thesis drafting_reason for these 21 names therefore reads the generic `NoSuchKey`, not the no-CIK
reason the store already holds.

**RULED (this cell's producer half):** `main()` gains a second loop, after the fetchable loop, over
`planned["unresolved"]`. For each entry, build the SAME shape `fetch.py`'s own
`unresolved_source_object(security_key, reason, ...)` already produces on a no-CIK miss (reuse that helper --
do not hand-roll a second shape) and write it via `crosswalk.write_pool()` to
`fetch.pool_key(entry["security_key"], None, "source")`, mirroring `run_one()`'s existing write pattern for
the RESOLVED branch (`:130-152`) exactly, just for the unresolved branch. Print a `BATCH DONE` style summary
line naming how many `UNRESOLVED-SOURCE` objects were written this run.

**No new vendor call** -- writing these objects touches no external API; `plan()`'s classification logic is
already correct and is NOT edited by this order.

---

**ISSUER AMENDMENT 1 (found by the worker, `0.9.0_WK_AMGT_RESAPP~33`, row `AMGT_RESAPP-Z-W33-S1`/`S2`;
independently re-confirmed by `2.0.0_SA_COO~Z` against the live `universe/v1/2026-09-16.json` before this
amendment was written).** Two real defects in the RULED text above, neither a defect in the worker's own
code, which correctly implemented what was written:

1. **The population is 237 unresolved, not 21** -- `universe/v1/2026-09-16.json` carries 250 names today
   (this project's universe has grown well past round 12's 33-keyed pilot scope; this order's original text
   assumed the smaller figure without re-measuring). **Of those 237, 59 carry `security_key: null` --
   NO IDENTITY WAS EVER MINTED for these names at all** (`resolution: "UNRESOLVED"`,
   `resolution_reason: "the coverage row's bloomberg_ticker status is 'UNRESOLVED' ... the identifier is NOT
   guessed from the folder name"`). **This is a DIFFERENT, upstream absence class from "no CIK"** -- it is
   exactly the identity gap `AMGT-rk-21` (chain ID, this same round) is resolving, not this cell's. Writing
   `fetch.pool_key(None, None, "source")` for these 59 produces the LITERAL key
   `filings/v1/None/UNRESOLVED-SOURCE.source.json` for every one of them -- **a real collision bug**, verified:
   `pool_key(security_key, accession, suffix) -> "%s%s/%s.%s.json" % (POOL_PREFIX, security_key, ...)` string-
   interpolates `security_key` with no null guard. **The write loop is RE-CUT: it skips (never writes) any
   `entry` whose `security_key` is falsy, counting them separately and printing that count named
   `"no-identity, out of scope (see AMGT-rk-21)"` rather than silently attempting the write.** The true target
   population for THIS cell is the 178 unresolved entries that DO carry a `security_key` but no CIK.
2. **The 120s worker timeout cannot accommodate the pre-existing fetchable loop (13 real EDGAR+LLM calls,
   itself already slow at this population size, unrelated to this order) plus the new unresolved-write loop
   placed after it** -- confirmed: 2 of 2 attempts hit `rc=124` with only 1 of 13 fetchable entries processed,
   never reaching the new loop. **Fix: `main()` gains a `--skip-fetch` flag that runs ONLY the unresolved-write
   loop** (a pure S3 write path, no vendor call, genuinely fast), independent of the fetchable loop's own
   runtime. The CRITERION invokes with `--skip-fetch`; a full, unbounded production run (fetchable AND
   unresolved) is the worker's own follow-through act, reported but not itself a timed criterion (per the
   dispatch skill's own rule: "never name a whole-corpus sweep as a criterion's invocation").

**Criteria AC1-AC3 below are RE-CUT to these corrected denominators and the `--skip-fetch` invocation. Nothing
else in this order's grant, paths, or bounds moves.**

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.4's `R13-F` row @`9419550eb1`,
grounded in rows `AMGT_RESAPP-Z-S139` and its correction `AMGT_RESAPP-Z-S146` (both `4.0.0_SA_CRO~Z`). The
adapter half of this same cell (surfacing the reason on the thesis route) is a SEPARATE order,
`AMGT_RESAPP.TO-AMGT-rk-24.thesis-route-no-cik-reason.md`, on chain B -- **do not touch `scoped_amgt.py` from
this order.**

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/batch.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~33/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-24.batch-unresolved-objects.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You may READ `lib/research/filings/fetch.py` and
  `crosswalk.py` freely (reuse their existing helpers) but WRITE only `batch.py` among repo files. The S3
  pool write (`filings/v1/<key>/UNRESOLVED-SOURCE.source.json`, 21 objects) is not a repo path and needs no
  `<paths>` entry. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~33 <0.9.0_WK_AMGT_RESAPP~33@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

Same standing bounds as your prior order this chain: PORTAL FROZEN (not your surface); COLLECTION STAYS OFF;
NO alarm/monitor/notification; secrets through `comp-secrets` only; **NO NEW VENDOR CALL**; no non-ASCII in
anything you write; **PUSH: never**. **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is
REFUSED with its measurement and a row; never repaired, widened, or satisfied by a route this order did not
name. **A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-count the 21
yourself against `universe/v1/2026-09-16.json` (or its current latest, named) rather than trusting this
document's number. **SURPRISE ROWS:** your row continues `AMGT_RESAPP-Z-W33-S<k>` from wherever your prior
order's `<k>` left off; `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row; append by
textual splice inside the one fenced JSON array (never re-serialize it) and never edit an existing row.
**Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-24"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
from lib.research.filings import batch
document, source = batch.load_universe('universe/v1/2026-09-16.json')
planned = batch.plan(document)
unresolved = planned['unresolved']
no_identity = [e for e in unresolved if not e.get('security_key')]
in_scope = [e for e in unresolved if e.get('security_key')]
print('unresolved_total', len(unresolved))
print('no_identity_out_of_scope', len(no_identity))
print('in_scope_target', len(in_scope))
"</invocation><expect>unresolved_total, no_identity_out_of_scope and in_scope_target sum correctly (no_identity_out_of_scope + in_scope_target == unresolved_total) and are all printed fresh, never cited from this document as a constant -- at this amendment's own cut these read 237/59/178, but this order's PASS does not depend on those exact numbers matching, only on the split being computed and printed</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-24"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3
from lib.research.filings import batch, fetch
document, source = batch.load_universe('universe/v1/2026-09-16.json')
planned = batch.plan(document)
in_scope = [e for e in planned['unresolved'] if e.get('security_key')]
print('in_scope_count', len(in_scope))
s3 = boto3.client('s3')
found = 0
missing = []
for entry in in_scope:
    key = fetch.pool_key(entry['security_key'], None, 'source')
    try:
        s3.head_object(Bucket='opal-data-harvest', Key=key)
        found += 1
    except Exception:
        missing.append(entry['security_key'])
print('objects_found', found)
print('objects_missing', missing[:10], '... (%d more)' % max(0, len(missing) - 10) if len(missing) > 10 else '')
none_key_object_exists = False
try:
    s3.head_object(Bucket='opal-data-harvest', Key='filings/v1/None/UNRESOLVED-SOURCE.source.json')
    none_key_object_exists = True
except Exception:
    pass
print('none_key_collision_object_exists', none_key_object_exists)
"</invocation><expect>objects_found equals in_scope_count and objects_missing is empty AFTER the fix runs; none_key_collision_object_exists is False both before and after (the re-cut write loop must never produce this literal key) -- before the fix, objects_found reads 0 (the planted-negative baseline); the worker records both the before and after run</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-24"><invocation>cd "$(git rev-parse --show-toplevel)" && timeout 100 python -m lib.research.filings.batch --universe universe/v1/2026-09-16.json --write-pool --skip-fetch 2>&1 | tail -5</invocation><expect>a `--skip-fetch` run (the unresolved-write loop only, no vendor call, independent of the slow fetchable loop) completes within the bound and prints a summary line naming how many UNRESOLVED-SOURCE objects were written this pass, matching AC1's `in_scope_target` denominator -- if `--skip-fetch` does not exist as a flag, the worker names the actual flag/mechanism it built to achieve the same isolation and re-runs this exact invocation against it</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~33/AMGT_RESAPP.TO-AMGT-rk-24.batch-unresolved-objects.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence),
graded by YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the
verdict); flip `<status>` to `complete`; commit with `--only -- <paths>`. **Report once. This is chain FP-B's
only order.**

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
