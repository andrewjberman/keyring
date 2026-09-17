# AMGT_RESAPP task order -- `AMGT-rk-22` -- management and posture producers over the keyed population -- CUT, WORKER NOT SPAWNED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-22</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~32</issued_to>
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

**You are `0.9.0_WK_AMGT_RESAPP~32` -- THIS ORDER IS CUT BUT YOUR WORKER MUST NOT BE SPAWNED UNTIL ANDREW
ANSWERS CARD 5** (management + posture producer cost, s.21e of the decomposition). This file exists so the
round's issuance is complete and nothing is left by silent omission. **If you are reading this as a live
spawn prompt, STOP IMMEDIATELY and verify with the COO that CARD 5 has actually been answered -- your spawn
should never happen without that confirmation existing as a durable record first.** Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~32;`. **NEVER RUN AN INSTALL.**

## 1. THE CELL, inlined in full -- `AMGT-rk-22` (FWD-17, FWD-19; rk-14 AC4 residue; CARD 5)

**THE MEASURED STATE.** Management serves 5 names (BABA, BA, COST, HD, SAP_GY); posture serves 2 (BABA, BA).
Management is capped at the 12 names carrying a filing; posture can reach the full 33 keyed. Producers:
`lib/research/management/enrich.py::build_document(security_key, as_of, source_path=None, s3=None, ...)`
(`:417`); `lib/research/posture/judge.py::run(security_key, as_of, write_pool=False, ...)` (`:362`, **calls
Anthropic**) + `lib/research/posture/packs.py::build_pack(...)` (`:85`) as its upstream pack builder. **Neither
has a CLI batch driver today** (unlike `model_block_pull.py`/`price_axis_pull.py`) -- writing one is part of
this order's work, once authorized.

**RULED:**
1. Run both producers over the keyed population (management: the 7 more names with a filing beyond today's
   5; posture: the 31 more beyond today's 2), writing a batch driver script if one does not already exist
   under `integrations/bloomberg/research/` by the time this order spawns.
2. **A3.1 item 3's classification:** absence reasons class as `source-lacks` vs `pull-missed` -- a NEW binary
   layer over EXISTING free-text reasons (`enrich.py:424-427`'s `domain_for()`; `judge.py:337`'s
   `_absent_document()` and its call sites `:372-384`), not built from nothing.
3. **Two round-11 remediation rows carry here** (`W18-S15`, `W22-S1`): cannot-say is not no-profile; applies
   to every name this cell runs.

**THIS CELL MAY BE CUT AND COMMITTED. ITS WORKER MUST NOT BE SPAWNED until Andrew answers CARD 5 -- both
producers spend LLM and/or search calls, and this is a population move the COO does not authorize alone.**

## 2. WHERE THIS CAME FROM

**ROUND 13**, decomposition v1.7 s.21c, on `1.0.0_SA_CTO~Z`'s L10 round-12 analysis s.4's `R13-D` row and
s.5's CARD 5 @`9419550eb1`, s.6's remediation rows `W18-S15`/`W22-S1`. PRD v0.10, ADMITTED, no PRD change.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/
lib/research/posture/
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~32/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-22.management-posture-producers.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Scratch is `<your worktree>/.scratch/` only.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~32 <0.9.0_WK_AMGT_RESAPP~32@opal.agent>" -F <msgfile> -- <paths>`.
  Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

PORTAL FROZEN (not your surface). **COLLECTION STAYS OFF -- this does NOT block this cell's own producer
pulls, which are the round's explicitly-CARDED exception once authorized**, exactly as `AMGT-rk-17`/
`AMGT-rk-18` were in round 12. **NO alarm, monitor, SNS/SES-send, notification or freshness checker.**
Secrets through `comp-secrets` only. **NO VENDOR CALL UNTIL CARD 5 IS ANSWERED** -- this is the one order in
this round's issuance that names a vendor call at all, and it is EXPLICITLY GATED. **NEVER call an external
vendor API without Andrew's explicit per-use word; availability is never authorization** (standing hard
stop). No non-ASCII in anything you write. **PUSH: never.**
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row.
**A COUNT BAR IS READ FROM THE LIVE STORE AT THE CUT and PRINTS its denominator** -- re-measure management
(5) and posture (2) fresh at spawn time; they may have moved.
**SURPRISE ROWS:** your row is `AMGT_RESAPP-Z-W32-S<k>`, `<k>` restarting at 1; `"project": "AMGT_RESAPP"`
and `"fabric": "site-z"` on every new row; append by textual splice inside the one fenced JSON array (never
re-serialize it) and never edit an existing row. **Found something off-task? APPEND ONE ROW AND KEEP
WORKING.**

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-22"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3
s3 = boto3.client('s3')
mgmt = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='management/v1/')
posture = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='posture/v1/')
print('management_names', len(mgmt.get('Contents', [])))
print('posture_names', len(posture.get('Contents', [])))
"</invocation><expect>BEFORE this order runs, management_names and posture_names read 5 and 2 respectively (re-measured, may have moved from this document's numbers -- print whatever is actually live); AFTER, both counts increase toward the fixable ceiling (management toward the 12-name filing cap, posture toward 33), with every non-measured name carrying a source-lacks or pull-missed reason, never a silent skip</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-22"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "
import boto3, json
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='opal-data-harvest', Prefix='management/v1/')
sample = [o['Key'] for o in resp.get('Contents', [])][:3]
for k in sample:
    doc = json.loads(s3.get_object(Bucket='opal-data-harvest', Key=k)['Body'].read())
    print(k, doc.get('absence_reason_class', 'FIELD NOT YET NAMED -- worker names its actual field'))
"</invocation><expect>a sampled absent management document carries a two-value classification (source-lacks vs pull-missed, or the worker's actual chosen field/enum names, stated in its report) rather than the free-text-only reason string that exists before this order</expect></criterion>
</proof_of_spec>

**Record the ACTUAL OUTPUT and DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~32/AMGT_RESAPP.TO-AMGT-rk-22.management-posture-producers.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2` (rc 0 is the verdict); flip `<status>` to
`complete`; commit with `--only -- <paths>`. Report once.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `.scratch/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.
