# NFRA_OPLGTW task order -- `OG-m-1` -- ROUND 2 (E11, READ ONLY): re-measure the 08335338 completion-marker storm and who writes it

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~13</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time read; no cron, alarm, monitor or cadence is created.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only calls only (s3api list-object-versions / get-object, logs filter-log-events, lambda get-function, ssm get-command-invocation); nothing is written to AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the rows (S4, S5, W4-S12) carry measured mechanisms; this cell re-measures them.
EGRESS CLASS, declared: NONE beyond Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `OG-m-1` (decomposition addendum R2-E, item E11)

**This cell READS. It changes nothing.** The remedy is a later cell cut from what you measure.

Background, from rows `NFRA_OPLGTW-S4`, `-S5` and `-W4-S12` in
`org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` (read all three first):
- The Schwab silver producer writes a completion marker per business date at
  `s3://opal-data-assets/schwab/08335338/meta/complete/date=YYYY-MM-DD.json`. The bucket is versioned, so every PUT is
  one object version.
- An S3 notification (`infra/aws/terraform/opal-assets/silver.tf:758-763`, id `advi-49f-silver-complete-accelerator`,
  events `s3:ObjectCreated:*`, prefix `schwab/08335338/meta/complete/`, suffix `.json`) invokes the Lambda
  `advi-49f-gold-dispatch` on every PUT. `silver.tf:747` calls it "an ACCELERATOR ONLY"; the production trigger is the
  floor schedule, cron(45 12 * * ? *) UTC.
- On 2026-09-15 (S4) each date was PUT about ten times within ~40 s, and each PUT dispatched the whole 49F gold chain:
  108 dispatches in 14 days, 61 refused by the chain lock, 40 classified UNKNOWN. S5: the first dispatch of a burst ran
  before the silver it names existed.
- OG-c-1 built "exactly one qualified closure" and OG-c-2 deployed it (2026-09-16). W4-S4 records that the rule does NOT
  stop writes: a new date, an incomplete record, and an incomplete-to-qualified change all still write.
- Context, NOT an acceptance value: read at drafting, the 19 marker keys hold 195 versions; each date from 09-10 to
  09-25 has 10 or 11. For date=2026-09-25 the 10 versions were written 09:46:08Z..09:46:52Z with sizes growing from
  5,500 to 16,521 bytes. The bodies carry the fields `closure`, `date`, `declared_source`, `declared_tables`,
  `disagreement`, `emitted_at`, `master`, `run_id`, `schema`, `written_tables`.
- W4-S12 said the dispatcher classifies by the FIRST line of the SSM output. At the issuance base,
  `infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py:90-101` (`_classify`) scans EVERY line for a
  line starting `CHAIN OK`, `CHAIN REFUSED` or `CHAIN ABORT`, and only falls back to the first line in the UNKNOWN
  label. So an UNKNOWN on a run whose chain log ends `CHAIN OK` means the terminal line was NOT in the output the
  dispatcher read. Test that; do not assume it.

**What you measure.** Window: the 13 days ending at your read time (the dispatcher's log group
`/aws/lambda/advi-49f-gold-dispatch` keeps 14 days). Record the window as ISO UTC `start` and `end`.
1. **PUTs per date.** `.tools/aws s3api list-object-versions --bucket opal-data-assets --prefix schwab/08335338/meta/complete/`
   (the CLI paginates for you; COUNT CLIENT-SIDE, never with `--query length()`). Per key, the number of versions whose
   LastModified is inside the window.
2. **What each PUT said.** For the three newest dates, fetch every version (`get-object --version-id`) and record ONLY
   `closure` (its status value), `emitted_at`, `run_id` and the length of `written_tables`. Never copy any other field.
3. **Dispatches.** `filter-log-events` over the window with filter `"Event:"`, fully paginated; count invocations by
   trigger source (`advi.49f.scheduled-floor`, `aws:s3` records, other) and by outcome (CHAIN OK, CHAIN REFUSED, CHAIN
   ABORT, UNKNOWN, host start, other). Every invocation lands in exactly one class of each; say how you joined an
   invocation to its outcome line.
4. **The UNKNOWNs.** For up to 5 UNKNOWN dispatches, read the SSM command they name (`get-command-invocation`): its
   Status, the byte length of `StandardOutputContent`, and whether a `CHAIN ` terminal line is in it. Pair each with its
   chain log under `s3://opal-data-49financial/gold/advi/_logs/` (first and last line only).
5. **Who writes the marker.** Every tracked non-test code file under `data/` or `infra/` that names `meta/complete`
   (7 at drafting: two copies of `conversion_manifest.py` -- `data/assets/scripts/silver/` and
   `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` --, two gateway readers, three Terraform files). Class each
   `writer`, `reader` or `config` from its code. For each writer, compare its bytes with what is DEPLOYED: download the
   deployed Lambda package (`aws lambda get-function`, then its `Code.Location`) and compare the file by content
   (sha256), recording `match` or `differs`. The marker key can also be built without the literal string; read the
   producer's write path and name any writer the string census missed.

Write `MARKER_STORM_READ.md` (the findings in prose, each number with its denominator) and `MARKER_STORM_READ.json`
in your deliverables dir. The JSON shape the checks read:
`{"window":{"start","end"}, "markers":{"versions_total","keys","per_key":{<key>:<count>}},
"dispatch":{"invocations","by_source":{..},"by_outcome":{..}}, "writers":[{"file","role","deployed_as","deployed_bytes"}]}`.
The `.md` ends with ONE section, "What a remedy would have to move", naming each writer and trigger a remedy cell would
touch, and which lane owns each (CLAUDE.md rule 13: `data/*/scripts/{gold,silver,bronze}/*.py` commit-to-deploy is the
DS lane; Lambda infra, PROD triggers and multi-pipeline acts are DT/AE). Propose no fix.

## 2. BOUNDS

1. READ ONLY. No PUT, DELETE, invoke, SendCommand, deploy, Terraform or schedule change. Never trigger the chain.
2. No customer value leaves AWS: from marker bodies take only the four fields in item 2; from chain logs, first and
   last line only.
3. You work in the worktree named in your identity line; commit your two files there under your serial with
   `.tools/safe-commit.sh`. Never push, merge, rebase, `stash`, `checkout --` or `clean`. AWS via the `.tools/aws`
   shim; `MSYS_NO_PATHCONV=1` on the log-group argument.
4. Spec frozen. REFUSE a criterion you cannot meet as written and report its measurement. Anything off-spec is ONE
   surprise row, and you keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W13-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit, the same day as the read)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-m-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/ms.AC1.sh; echo "exit=$?"</invocation><expect>keys differing 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-m-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/ms.AC2.sh; echo "exit=$?"</invocation><expect>RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-m-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/ms.AC3.sh; echo "exit=$?"</invocation><expect>missing 0; no role 0; writers unmeasured 0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- the recorded PUTs per date equal a fresh recount of versions in the window, key by key.
- `AC2` -- the dispatch tally partitions a fresh recount of dispatcher invocations, by source and by outcome (the
  script prints the four numbers and decides equality itself).
- `AC3` -- every code file naming the marker prefix is in the writer census with a role, and every writer's deployed
  bytes are measured.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~13/NFRA_OPLGTW.TO-OG-m-1.marker-storm-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Flip `complete` only when AC1-AC3 PASS by output.
Report once, in your final message.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- READ cell of E11; the remedy cell is cut from this read and is NOT in this issuance. That remedy changes when the 49F
  chain dispatches, so it needs the never-widen sign-off (CTO + COO) with the writer census of `meta/complete/` this
  cell produces (N writers = N rules read, N printed). Its lane follows rule 13 on the file it moves.
- Drafting observation the remedy question turns on: after OG-c-2 (09-16) the per-date PUT count did not fall (10 per
  date through 09-25; growing body sizes point at incomplete-to-incomplete rewrites). Context, never a criterion value.
- Slot ~13, queue position 2 (after `OG-o-3`). No edge to another round-2 cell. Risk SERVED: every criterion re-reads the
  live AWS plane.

<status>complete</status>
<round>3</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
