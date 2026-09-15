# AMGT_RESAPP task order -- `AMGT-rj-5` -- ONE STORE: THE READER, THE PRODUCER, THE GENERATION -- the ranking reads the pool and publishes whole generations

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~19</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~19`.** Same worktree (sparse cone), same rules as `rj-4`, which you have just finished; this is the
SECOND order of chain B. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~19;`.

## 1. THE CELL, inlined in full -- `AMGT-rj-5` (rows `Z-S96` / `Z-S101`; C-ONE-STORE, C-RANKING-GENERATION; interfaces P-1 and G-1)

**THE CONTRACTS (PRD v0.8 @`1170b4da69`, SIGNED):**
*C-ONE-STORE: "The pool `s3://opal-data-harvest` is THE article store. The chatter axis producer and the coverage reader READ the pool
through ONE shared adapter: the association at `publication-links/v1/{security_key}/{publisher}/{digest}.json` (its `security_key`,
`publisher`, `article_key`), the body at `publications/v1/{publisher}/{digest}.json`, where `article_key = publisher + ':' +
article_id` is the stable identity and `digest = sha256(article_key)`; the publication time is the body's `published` field (the
canonical schema has no `published_at` ... the consumer maps `published` to its own `published_at` at its boundary and never
substitutes `fetched_at`, the retrieval vintage, or the link's `first_discovered_at`); one article counts ONCE per associated
security however many links or retries carry it; a missing body, a malformed record, an access denial and a partial read stay
DISTINGUISHABLE from a quiet day and from an empty feed; the DynamoDB articles table is RETIRED as a source once both readers are
repointed, and nothing writes it after that."* The field-level contract and the acceptance examples are the CRO's brief
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_POOL_READERS_20260915_W.md` @`0e7de170e3` -- READ IT FIRST.
*C-RANKING-GENERATION: "A ranking run for one axis and one date publishes a COMPLETE GENERATION, and the reader selects that
committed generation: either an immutable generation plus a current pointer, or a bounded replacement ... an upsert that leaves
prior rows in place is neither. Zero winners, a changed winner and a failed or interrupted write are three DISTINGUISHABLE states:
a successful empty product clears the earlier membership; a producer or read failure leaves the prior generation current and says
so; no mixed generation is ever readable. Every generation carries its run id, its source coverage vintage and its payload hash."*
Measured defect (the CRO's brief @`5ae6dd04b5`): `batch_writer(overwrite_by_pkeys=['axis_date','ticker'])` never removes rows
absent from a new ranking -- AAA#1, BBB#1, CCC#2 after a replacement run, all three rows after an empty one.

**THE CUT NAMES: an IMMUTABLE GENERATION PARTITION plus a CURRENT POINTER.** Rows are written under `axis_date =
<AXIS>#<date>#<generation_id>` (`generation_id` = a run id, ULID or timestamp+hash), then ONE pointer item at `axis_date =
<AXIS>#<date>`, `ticker = "_CURRENT"` carrying `{generation_id, run_id, coverage_vintage, payload_hash, row_count, state:
COMPLETE | EMPTY | FAILED, written_at}`; a successful empty product writes an EMPTY pointer (the earlier membership is no longer
readable through the pointer); a failed or interrupted run leaves the prior pointer in place and writes a FAILED marker beside it
(`ticker = "_FAILED#<run_id>"`); the reader (INTERFACE G-1; chain A's `rj-9` implements the route) reads the pointer, then the
generation partition -- never a bare date partition. Prior generations are never deleted by the producer.

**THE SEAM (06:1x-06:3xZ):** `lib/research/metrics/chatter_axis.py:109-111` (`HARVEST_ARTICLES_TABLE`, `ticker_date_index`), the
query `:205-215`, `WINDOW_DAYS = 30` (`chatter_gate.py:45`), `TOP_N = 10` (`:48`), the write `default_write_rows :383-393`;
`scoped_amgt.py:685-703 read_coverage_set` (chain A's to change in `rj-9`; NOT yours); the harvester `lib/opal_data_harvest/`
(`catalog.py:68-79` the two key layouts; `article.schema.json`; `security-article.schema.json`; `uploads.py` metadata). NO S3
reader of these prefixes exists anywhere under `lib/research/`. The harvester's association key form was measured by you in `rj-4`
and is mapped through `crosswalk.aliases` (X-1).

**DELIVER, in this order:**
1. **The ONE shared adapter** `lib/research/coverage/pool_reader.py` (INTERFACE P-1): `list_links(identity) -> [link]` over every
   alias of the identity, `read_body(article_key) -> body`, `coverage_items(identity, days) -> {items: [{title, url, publisher,
   published_at (from the body's `published`), article_key}] newest first, store_item_count, states: {missing_body, malformed,
   denied, partial}, read_at, key_forms}`; ONE article counts once per identity across aliases and retries; each of the four failure
   states is a distinct counter and a distinct exception class, never a silent zero; bodies validated against the harvester's schema
   (`jsonschema`; the schema files are read from `lib/opal_data_harvest/` and are part of the package -- `rj-10`'s seam).
2. **The producer on the pool.** `chatter_axis.py` builds its 30-day histogram per `security_key` over the union universe (U-1 from
   the pool; the `universe.json` fallback) from P-1; the DynamoDB articles read path and the `HARVEST_ARTICLES_TABLE` knob REMOVED;
   the row shape from `rj-1` kept.
3. **The generation writer.** `default_write_rows` replaced by the generation write above; a `--dry-run` CLI `python -m
   lib.research.metrics.chatter_axis --as-of <date> --dry-run` printing the per-name counts, the denominators (names read, names
   with links, bodies read, per-state counts) and the top-10 rows with the pointer that WOULD be written (generation_id, run_id,
   coverage_vintage, payload_hash, row_count, state); NO live write in this cell (`rj-10`'s QA invoke is the live proof).
4. **The difference control** script in your deliverables: for BA, COST, HD and one name with no links -- pool links, pool bodies
   in the window, per-state counts, and the DynamoDB table's item count for the same ticker (read ONCE via the old index, for the
   record; the two stores are expected to DIFFER).
5. **Unit tests** with a local fake of the two prefixes: links, none, a missing body, a malformed body, a denied read, a partial
   listing, the window boundary, an alias carrying the same article twice (counted once); and the writer against a fake table:
   the measured defect reproduced with the OLD write (three rows survive) and the NEW write passing all three states (replacement
   -> only the new membership readable through the pointer; empty -> EMPTY pointer; failure -> the prior pointer stays, a FAILED
   marker beside it).

**BOUND:** no edit to `scoped_amgt.py` (chain A's; the coverage route lands in `rj-9` over P-1); no live DynamoDB write (the one
table read is the control); no deploy; the harvest's collection mechanism and cadence are Andrew's.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on row `Z-S96` (`1.0.0_SA_CTO~W`) and its disarm `Z-S101` @`008ca40b6c`, the
slug @`e28f0b546c` item 4, the CRO's pool-readers brief @`0e7de170e3` and ranking-retries brief @`5ae6dd04b5`, the connection brief
@`0f9a04e81e` seams 1 and 5, and Andrew-direct ~05:04Z @`7cf62a165f`. Readers of P-1: rj-9, rj-10; of G-1: rj-9, rj-10, rj-3.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/coverage/
lib/research/metrics/chatter_axis.py
lib/research/metrics/chatter_gate.py
lib/research/metrics/tests/
lib/research/identity/
lib/opal_data_harvest/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json
org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_POOL_READERS_20260915_W.md
org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_RANKING_RETRIES_20260915_W.md
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-5.one-store-the-two-readers-on-the-pool.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). `lib/opal_data_harvest/`, `lib/research/identity/`, `universe.json` and
  the CRO's briefs are READ-ONLY. `lib/research/api/scoped_amgt.py` is NOT in your grant.
- **COMMITTING:** as in `rj-4`.

## 4. BOUNDS

Egress @`dfa63b6d92` (Opal's own S3 and one DynamoDB read). Secrets ONLY through `comp-secrets`. No non-ASCII in anything that
reaches AWS. **THE REFUSAL CLAUSE** and **SURPRISE ROWS** as in `rj-4`; continue the `W19` sequence.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-5"><invocation>.tools/aws s3api list-objects-v2 --bucket opal-data-harvest --prefix publication-links/v1/ --delimiter / --query "CommonPrefixes[].Prefix" --output text | tr "\t" "\n" | cat; .tools/aws s3api list-objects-v2 --bucket opal-data-harvest --prefix publications/v1/ --query "length(Contents)" --output text</invocation><expect>the association-key prefixes (at least three, carrying BA, COST and HD in the harvester's form, mapped by crosswalk.aliases) and a publications/v1 object count at least 80. Zero prefixes is a STOP and a BLOCKING row</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-5"><invocation>python -c "from lib.research.coverage import pool_reader as p; import json; [print(k, json.dumps({x:y for x,y in p.coverage_items(k, 30).items() if x!='items'}), 'items', len(p.coverage_items(k,30)['items']), 'first', json.dumps((p.coverage_items(k,30)['items'] or [{}])[0])[:170]) for k in ('BA_US_Equity','COST_US_Equity','HD_US_Equity','ZZZ_NOPE_US_Equity')]"</invocation><expect>for BA_US_Equity, COST_US_Equity and HD_US_Equity: store_item_count at least 20 each, items at least 1 each, the first item carrying title, a canonical https url, publisher, published_at and article_key, states all 0 or a listed count, key_forms naming the harvester's form(s); for ZZZ_NOPE_US_Equity: store_item_count 0, items 0, no exception, states 0. An item lacking url or published_at, an item counted twice across aliases, or a control with items, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-5"><invocation>python -m lib.research.metrics.chatter_axis --as-of 2026-09-15 --dry-run 2>&1 | tail -24</invocation><expect>denominator lines (names read N from the universe object, names with links at least 3, bodies read at least 80, per-state counts), per-name counts with BA, COST and HD each at least 1 within the 30-day window, a top-10 list of rows each carrying security_key beside ticker, and the POINTER that would be written: generation_id, run_id, coverage_vintage, payload_hash (a 64-hex sha256 over the sorted rows), row_count equal to the rows listed, state COMPLETE; NO DynamoDB table read in the output. A row without security_key, or a pointer without payload_hash, is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-5"><invocation>python -c "import io; s=io.open('lib/research/metrics/chatter_axis.py',encoding='utf-8').read(); print('producer-table-knob', s.count('HARVEST_ARTICLES_TABLE'), 'producer-gsi', s.count('ticker_date_index'), 'producer-pool-reader', s.count('pool_reader'), 'overwrite-upsert', s.count('overwrite_by_pkeys'), 'pointer-item', s.count('_CURRENT'), 'failed-marker', s.count('_FAILED'), 'states', s.count('COMPLETE') + s.count('EMPTY') + s.count('FAILED'))"; git diff --stat SITEZ...HEAD -- lib/research/api/scoped_amgt.py | cat; echo "adapter-diff-lines: $(git diff SITEZ...HEAD -- lib/research/api/scoped_amgt.py | wc -l)"</invocation><expect>producer-table-knob 0, producer-gsi 0, producer-pool-reader at least 1, overwrite-upsert 0 (the upsert-and-never-clear writer is gone), pointer-item at least 1, failed-marker at least 1, states at least 3; adapter-diff-lines 0 (this cell did not touch scoped_amgt.py -- chain A owns it). A surviving overwrite_by_pkeys, or any adapter diff, is NOT met</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rj-5"><invocation>python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/difference_control.py" 2>&1 | tail -8</invocation><expect>four lines (BA, COST, HD, the control), each printing pool-links N, pool-bodies-in-window M, per-state counts and table-items T (read ONCE from opal-harvest-articles via the old index, for the record), the three commissioned names showing N at least 20 and T 0 (nothing in the repo writes the table), the control N 0. The two stores differ; equal numbers would be the surprise</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rj-5"><invocation>python -m unittest discover -s lib/research/coverage/tests -p "test_*.py" -q 2>&1 | tail -3; python -m unittest lib.research.metrics.tests.test_chatter_axis -q 2>&1 | tail -3; python -c "import io; t=io.open('lib/research/metrics/tests/test_chatter_axis.py',encoding='utf-8').read(); print('defect-reproduced', t.count('AAA') + t.count('overwrite_by_pkeys'), 'three-states', t.count('EMPTY') + t.count('FAILED') + t.count('COMPLETE'), 'alias-once', t.count('alias'))"</invocation><expect>both suites end OK with 0 failures and 0 errors; defect-reproduced at least 1 (the old write's surviving rows are the negative control), three-states at least 3, alias-once at least 1. A writer test without the empty and failed arms is NOT met</expect></criterion>
  <criterion id="AC7" cell_refs="AMGT-rj-5"><invocation>git log --format="%h %an %s" -4 -- lib/research/coverage/ lib/research/metrics/ | cut -c1-140; python -c "import io,glob; fs=glob.glob('lib/research/coverage/*.py'); print('files', len(fs), 'nonascii', sum(sum(1 for ch in io.open(f,encoding='utf-8').read() if ord(ch)>127) for f in fs), 'put_object-sites', sum(io.open(f,encoding='utf-8').read().count('put_object') for f in fs), 'delete-sites', sum(io.open(f,encoding='utf-8').read().count('delete_object') + io.open(f,encoding='utf-8').read().count('delete_item') for f in fs))"</invocation><expect>commits by this serial touching the two paths; nonascii 0; put_object-sites 0 and delete-sites 0 in the reader (it reads only). A write or delete in the reader is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/AMGT_RESAPP.TO-AMGT-rj-5.one-store-the-two-readers-on-the-pool.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6,AC7` (rc 0 is the verdict); keep the dry-run output and
the difference control beside it; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion
cannot be met, leave the order OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~19</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) C-ONE-STORE and C-RANKING-GENERATION (the CRO's briefs @`0e7de170e3`, @`5ae6dd04b5`; Andrew-direct ~05:04Z @`7cf62a165f`), row `AMGT_RESAPP-Z-S96` @`7efd49fc2f` and its disarm `Z-S101` @`008ca40b6c`, the slug REMEDIATION_v10 @`e28f0b546c` item 4, `1.0.0_SA_CTO~W`'s L10 round-10 analysis @`8d5fe78265` s.6 item 2, the connection brief @`0f9a04e81e` seams 1 and 5, decomposition v1.3 s.19 @`73938cdae4` (cell rj-5, chain B second; interfaces P-1, G-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>
