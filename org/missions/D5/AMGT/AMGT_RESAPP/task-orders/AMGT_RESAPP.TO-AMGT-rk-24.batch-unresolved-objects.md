# AMGT_RESAPP task order -- `AMGT-rk-24` (producer half) -- the batch's own promised UNRESOLVED-SOURCE objects, actually written

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-24</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~26</issued_to>
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

**You are `0.9.0_WK_AMGT_RESAPP~26`, continuing.** You already hold `AMGT-rk-19`'s producer half; this is the
SECOND and LAST order in chain FP's queue. Your first act this order re-prints
`git rev-parse --abbrev-ref HEAD` and confirms `lib/research/filings/batch.py` exists at the path below.
Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~26;`. **NEVER RUN AN INSTALL.**

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

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.4's `R13-F` row @`9419550eb1`,
grounded in rows `AMGT_RESAPP-Z-S139` and its correction `AMGT_RESAPP-Z-S146` (both `4.0.0_SA_CRO~Z`). The
adapter half of this same cell (surfacing the reason on the thesis route) is a SEPARATE order,
`AMGT_RESAPP.TO-AMGT-rk-24.thesis-route-no-cik-reason.md`, on chain B -- **do not touch `scoped_amgt.py` from
this order.**

## 3. SURFACES -- what you may read and write

<paths>
lib/research/filings/batch.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~26/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-24.batch-unresolved-objects.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** You may READ `lib/research/filings/fetch.py` and
  `crosswalk.py` freely (reuse their existing helpers) but WRITE only `batch.py` among repo files. The S3
  pool write (`filings/v1/<key>/UNRESOLVED-SOURCE.source.json`, 21 objects) is not a repo path and needs no
  `<paths>` entry. Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~26 <0.9.0_WK_AMGT_RESAPP~26@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

Same standing bounds as your prior order this chain: PORTAL FROZEN (not your surface); COLLECTION STAYS OFF;
NO alarm/monitor/notification; secrets through `comp-secrets` only; **NO NEW VENDOR CALL**; no non-ASCII in
anything you write; **PUSH: never**. **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is
REFUSED with its measurement and a row; never repaired, widened, or satisfied by a route this order did not
name. **A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-count the 21
yourself against `universe/v1/2026-09-16.json` (or its current latest, named) rather than trusting this
document's number. **SURPRISE ROWS:** your row continues `AMGT_RESAPP-Z-W26-S<k>` from wherever your prior
order's `<k>` left off; `"project": "AMGT_RESAPP"` and `"fabric": "site-z"` on every new row; append by
textual splice inside the one fenced JSON array (never re-serialize it) and never edit an existing row.
**Found something off-task? APPEND ONE ROW AND KEEP WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-24"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.batch --universe universe/v1/2026-09-16.json --dry-run 2>&1 | grep -E "BATCH:|UNRESOLVED-SOURCE:"</invocation><expect>the printed BATCH line's unresolved_source count and the UNRESOLVED-SOURCE line's name(s) count agree with each other and are both nonzero (21 at this cut, re-measured live, never assumed) -- this is the pre-fix denominator this order must not silently change</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-24"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3
from lib.research.filings import batch, fetch
document, source = batch.load_universe('universe/v1/2026-09-16.json')
planned = batch.plan(document)
unresolved = planned['unresolved']
print('unresolved_count', len(unresolved))
s3 = boto3.client('s3')
found = 0
missing = []
for entry in unresolved:
    key = fetch.pool_key(entry['security_key'], None, 'source')
    try:
        s3.head_object(Bucket='opal-data-harvest', Key=key)
        found += 1
    except Exception:
        missing.append(entry['security_key'])
print('objects_found', found)
print('objects_missing', missing)
"</invocation><expect>after this order's fix runs the batch for real (write-pool, not dry-run), objects_found equals unresolved_count and objects_missing is empty -- before the fix, objects_found reads 0 (the planted-negative baseline this order must move to nonzero); the worker records BOTH the before and after run of this same invocation</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-24"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.filings.batch --universe universe/v1/2026-09-16.json --write-pool 2>&1 | tail -5</invocation><expect>a real (non-dry-run) batch run prints a summary line naming how many UNRESOLVED-SOURCE objects were written this pass, and that count matches AC1's printed denominator -- run this ONCE only, after AC1 and AC2's before-state are recorded, since it is the act that changes the store</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on
this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~26/AMGT_RESAPP.TO-AMGT-rk-24.batch-unresolved-objects.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence),
graded by YOUR WORKTREE'S OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the
verdict); flip `<status>` to `complete`; commit with `--only -- <paths>`. **Report once. This is chain FP's
last order** -- your queue is complete after this drains.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
