# AMGT_RESAPP task order -- `AMGT-rk-30` (producer half) -- a real producer run wires rk-5's scores to the pool

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-30</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~29</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order arms no cron, alarm, monitor or cadence.
comp-iam: RUN -- this order's producer half writes to a NEW pool prefix (scores/v1/) not previously used by
  any deployed route; comp-iam was read against the existing Lambda execution role's S3 policy
  (opal-amgt-scoped-api-role and the harvest producer role) and confirmed both already carry a wildcard
  write/read grant over opal-data-harvest that covers any new prefix under the bucket -- no new IAM
  statement is required. If the live policy differs from this expectation at the actual cut, the worker
  files a row rather than widening any grant itself.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~29`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and tests that `org/`, `.tools/` and the
paths in section 3 exist; if any is absent, STOP with a BLOCKING row. **YOU HOLD CHAIN SP, one order, the
whole of `lib/research/scores/` for this round.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~29;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-30` producer half (ADDENDUM 1: R13-L, not deferrable with R13-K)

**THE MEASURED STATE.** `lib/research/scores/classify.py` (`measured()` `:32`, `absent()` `:39`,
`is_measured()` `:50`) is the record-shape contract. `robustness.py`'s
`score_robustness_annual_variant(model_block, tau=TAU_DEFAULT)` (`:385`) reads model-block figures only, no
vendor call; `score_robustness_quarterly(...)` (`:628`) needs a live Bloomberg pull via
`pull_quarterly_inputs()` (`:516`) -- **that variant STAYS A CARD, never this cell's act.**
`peers_v.py`'s `score_peers_v(...)` (`:211`) computes from peer rows via `compute_measures()` (`:184`), over
`AMGT-rk-14`'s repaired peer objects. `divergence.py`'s `score_divergence(...)` (`:107`) and
`check_degeneracy(d_values, floor=DEGENERACY_FLOOR)` (`:94`) gate Divergence D -- that gate has NOT passed
(`AMGT-rk-29`/R13-K, the house forecast producer, is deferred to round 14), so D is ABSENT for every name BY
DESIGN, not by omission.

**None of the three modules is wired into any pipeline today** (confirmed: no runner script under
`lib/research/scores/tests/` or matching `*score*runner*`).

**RULED:** write a runner (new file, e.g. `lib/research/scores/run_scores.py`, your naming, stated in your
report) that, for each of the 33 keyed covered names:
1. Reads that name's model block (already served, 33 of 33) and calls `score_robustness_annual_variant()`.
2. Reads that name's peer rows (from `AMGT-rk-14`'s repaired objects) and calls `score_peers_v()`.
3. Writes Divergence D as `classify.py`'s `absent("house-forecast-not-served", "the house forecast does not
   serve", ...)` for every name, unconditionally, until `AMGT-rk-29` lands.
4. Writes the three records per name to the pool through `classify.py`'s shape, at a key of your choosing
   under a `scores/v1/` prefix (state the exact key shape in your report so the sibling adapter order,
   `AMGT-rk-30` adapter half on chain B, can read it -- **your key shape is load-bearing for that order and
   must not change after you report**).

**No vendor call.** `score_robustness_annual_variant()` reads the model block only; `score_peers_v()` reads
already-repaired peer rows only.

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s **ADDENDUM 1** @`509f3f7335`, triggered by
`4.0.0_SA_CRO~Z`'s row `AMGT_RESAPP-Z-S149`. PRD v0.10, ADMITTED, no PRD change
(`C-ROUND12-DIVERGENCE-DEGENERACY` already binds D at the producer). The adapter half of this cell
(`AMGT_RESAPP.TO-AMGT-rk-30.scores-adapter-model-tab.md`, chain B) reads the pool key YOU mint here -- report
your exact key shape clearly. The page half (chain A) is fed only after BOTH this order and the adapter half
land.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/scores/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~29/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-30.scores-producer-runner.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** A READ needs no grant (read the model block pool, the peer
  rows, `lib/research/api/scoped_amgt.py` for `read_management()`'s shape as your record-shape precedent);
  this block governs WRITES, and your write surface is the whole of `lib/research/scores/` (a new runner
  file lives here). The pool write (`scores/v1/...`) is not a repo path and needs no `<paths>` entry.
  Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~29 <0.9.0_WK_AMGT_RESAPP~29@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF.** **NO alarm, monitor, SNS/SES-send, notification
or freshness checker.** Secrets through `comp-secrets` only. **NO NEW VENDOR CALL** -- if a name's model
block or peer rows are missing the inputs `score_robustness_annual_variant()`/`score_peers_v()` need, that
name classes ABSENT with a reason; it never triggers a fresh pull from this order. No non-ASCII in anything
you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row;
never repaired, widened, or satisfied by a route this order did not name.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator.**
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W29-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"` and
`"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING.**

**ISSUER AMENDMENT 1 (2.0.0_SA_COO~Z, 2026-09-17 ~23:5xZ, at grading time):** AC2/AC3's `status` field name
corrected to `state` (the runner's real `classify.py`-shaped field, per its own confirmed output) --
matches the order's own `<expect>` text, which already anticipated a field-name substitution. AC2/AC3's key
listing filtered to the date-partitioned shape (a trailing `/YYYY-MM-DD.json` regex) rather than a raw
top-level prefix listing, since the pool now also carries 31 superseded flat-shape objects (row Z-S155)
whose lexicographic sort order would otherwise put several of them ahead of the canonical shape in the
un-filtered `[:3]`/`[:5]` slice. This is the SAME key-shape trap class row S141/AC-rk-23 already caught
once this round, recurring on a different criterion.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-30"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='crosswalk/v1/')
latest = sorted(o['Key'] for o in resp.get('Contents', []))[-1]
doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=latest)['Body'].read())
keyed = [r['security_key'] for r in doc.get('records', doc if isinstance(doc, list) else []) if r.get('security_key')]
print('keyed_count', len(keyed))
resp2 = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='scores/v1/')
written = [o['Key'] for o in resp2.get('Contents', [])]
print('scores_objects_written', len(written))
"</invocation><expect>AFTER this order's runner executes, scores_objects_written is nonzero and reasonably close to keyed_count (a name may legitimately be ABSENT on all three fields and still get a written object -- the object exists, its fields carry the classification); the worker prints the exact key prefix it actually used if different from `scores/v1/`</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-30"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, re
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='scores/v1/')
keys = [o['Key'] for o in resp.get('Contents', []) if re.search(r'/\d{4}-\d{2}-\d{2}\.json$', o['Key'])][:3]
for k in keys:
    doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read())
    print(k, {kk: (doc.get(kk) or {}).get('state') for kk in ('robustness', 'peers_v', 'divergence')})
"</invocation><expect>every sampled object carries all three keys (robustness, peers_v, divergence -- the worker names its actual field names if different), each a MEASURED or ABSENT status per classify.py's shape; divergence reads ABSENT with a house-forecast reason on every sampled object, unconditionally</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-30"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json, re
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='scores/v1/')
keys = [o['Key'] for o in resp.get('Contents', []) if re.search(r'/\d{4}-\d{2}-\d{2}\.json$', o['Key'])]
missing_field_absent = True
for k in keys[:5]:
    doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read())
    for field in ('robustness', 'peers_v'):
        rec = doc.get(field) or {}
        if rec.get('state') == 'MEASURED' and rec.get('value') in (None, ''):
            missing_field_absent = False
print('planted_negative_holds', missing_field_absent)
"</invocation><expect>planted_negative_holds is True -- no sampled record ever reports MEASURED with a null/empty value; this is the class of bug this whole round's S121 criteria-class ruling exists to catch (a status field that could read MEASURED on invented/missing data)</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~29/AMGT_RESAPP.TO-AMGT-rk-30.scores-producer-runner.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once, and STATE YOUR EXACT POOL KEY SHAPE in the report
(the adapter order depends on it).

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>13</round>
<slot>~29</slot>
