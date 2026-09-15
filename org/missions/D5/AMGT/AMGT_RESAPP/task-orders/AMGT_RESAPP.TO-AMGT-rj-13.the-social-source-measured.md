# AMGT_RESAPP task order -- `AMGT-rj-13` -- THE SOCIAL SOURCE, MEASURED -- one security, one supported method, a cap and a window, and the numbers a feed would need

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rj-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~22</issued_to>
<issued_by>2.0.0_SA_COO~W</issued_by>
<placeholders>NONE</placeholders>

**You are `0.9.0_WK_AMGT_RESAPP~22`.** Same worktree (sparse cone), same rules as `rj-8`, which you have just finished; this is the SECOND
and last order of chain E. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~22;`.

## 1. THE CELL, inlined in full -- `AMGT-rj-13` (S13; PRD s.9a-2's "measure, then build" row; C-LISTING-NOT-CAPABILITY; interface S-1)

**THE RULE (PRD v0.8 @`1170b4da69`, s.4 row S13 and s.9a-2):** S13 is the ONLY surface whose verb is "measure, then build": *"its
substrate is a catalogue nobody has exercised. Its first cell may honestly deliver a measurement rather than a feature."* The CRO's
social brief `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_SOCIAL_SERP_20260915_W.md` @`36a08d3d1a` -- READ IT
FIRST -- names the SUPPORTED input methods (the old plan's "cashtag search" is NOT a callable method: the X endpoint inventory lists
URL / profile / username methods and no keyword-post discovery):
- X official-account posts: `/datasets/v3/scrape`, dataset `gd_lwxkxvnf1cynvib9co`, `type=discover_new`, `discover_by=profiles_array`,
  profile `url` inputs -- posts FROM selected profiles, not the wider conversation.
- Reddit discussion search: `/datasets/v3/scrape`, dataset `gd_lvz8ah06191smkebj4`, `type=discover_new`, `discover_by=keyword`, inputs
  `keyword`, `date`, `num_of_posts` (a bounded `num_of_posts` is necessary; omission means all matches).
- Asynchronous collection: `/datasets/v3/trigger` is the generic route; persist the returned job / snapshot identity and retrieve the
  result through the documented delivery flow; never resubmit discovery on every poll.
The brief's acceptance: *"One security, one declared supported method, a stated result cap and time window; measure actual delivery,
quality, latency and cost"*; *"Failure, zero matches, stale matches, capped results and still-running"* are distinguishable states.
**THE CUT NAMES: Reddit discussion search (the wider conversation), ONE security, `num_of_posts` at most 50, a 30-day window**, with the
X official-account method recorded as the second candidate and NOT run.

**WHAT EXISTS (the CRO's audit @`1906df40bd`):** `lib/research/social/measure.py` (a request-description builder; `:206-218` has NO HTTP
client and returns 4), `schema.json`, `validator.py` (the social item contract: `item_id, platform, account.handle, account.official,
posted_at, text, url, admitted, rule_reason, source_line`); the Bright Data credential in Secrets Manager (`comp-secrets list` to name
it; the SERP zone is a different product from the datasets API -- name which key you use); the account-discovery pass
`IDENTITY_SOCIAL_ACCOUNT_PASS_20260914_Z.json` (263 inferred links, not account-page confirmed). No feed is built here.

**DELIVER, in this order:**
1. `lib/research/social/collect.py`: ONE bounded job -- the Reddit keyword discovery for ONE security (the subject's company name and
   its ticker as two keywords in one job, or two jobs -- say which), `date` = the last 30 days, `num_of_posts` at most 50, through
   `/datasets/v3/trigger`; the job identity persisted immediately to your deliverables and to the pool measurement record; the result
   retrieved through the documented delivery flow with bounded polling (interval and max wait printed); the records validated against
   `lib/research/social/schema.json` (through `validator.py`) with per-item `admitted` / `rule_reason` from the EXISTING rule (no new rule
   is written); the five states (failure, zero matches, stale matches, capped results, still-running) each a distinct outcome in the
   record.
2. `social/v1/_measurement/{as_of}.json` (INTERFACE S-1): `{as_of, security_key, method: {platform: reddit, dataset, discover_by, inputs,
   cap, window}, job: {id, submitted_at, completed_at, state}, delivery: {records, valid, admitted, rejected_by_rule, stale, capped},
   latency_seconds, cost: {usd, unit}, quality: {relevance_sample: [10 items with admitted and rule_reason]}, second_candidate: {platform:
   x, discover_by: profiles_array, profile_urls_from: the account pass, status: NOT_RUN}, method_version}` -- `Metadata {document-sha256,
   schema-version}`, read-back; a JSON schema (`additionalProperties: false`).
3. A row for the finding, whatever it is: the measured delivery, quality, latency and cost are the numbers a later round's feed cell
   needs; the header's social half stays "no source measured" until that cell (rj-9 renders it so).
4. Unit tests with the client stubbed: the five states, the cap, the window, the validator pass-through.

**BOUND:** ONE job (two at most, stated); `num_of_posts` at most 50; USD cap printed before the call and the job aborted if the
estimate exceeds USD 5; NO feed, NO schedule, NO second security; the X method NOT run; the SERP zone NOT used (a different measurement,
the CRO's audit); no portal edit.

## 2. WHERE THIS CAME FROM

**ROUND 11**, decomposition v1.3 s.19 @`73938cdae4`, on PRD s.9a-2's S13 row and the CRO's social brief @`36a08d3d1a` (carried by the
follow-up @`865e4fc113` item 1), the audit @`1906df40bd` (no social HTTP client exists), FWD-11 / FWD-16's social half. Reader of S-1: a
later round.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/social/
lib/research/identity/
org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_SOCIAL_SERP_20260915_W.md
org/tier1_exec/4.0.0_SA_CRO/deliverables/IDENTITY_SOCIAL_ACCOUNT_PASS_20260914_Z.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~6/MEASUREMENT_PLAN.md
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~19/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rj-13.the-social-source-measured.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL** (RULING 1). The CRO's brief and account pass, the old plan and the `~19` deliverables
  are READ-ONLY; `lib/research/social/` is yours (add `collect.py`, the schema for S-1 and tests; do not rewrite `schema.json`'s item
  contract or the admission rule).
- **COMMITTING:** as in `rj-8`.

## 4. BOUNDS

Egress @`dfa63b6d92` (Bright Data's datasets API). Secrets ONLY through `comp-secrets get <name> --reveal`. No non-ASCII in anything
that reaches AWS (post text is normalised before storage and the normalisation recorded). **THE REFUSAL CLAUSE** and **SURPRISE ROWS**
as in `rj-8`; continue the `W22` sequence.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rj-13"><invocation>python -m unittest discover -s lib/research/social/tests -p "test_*.py" -q 2>&1 | tail -3; python -c "import io; c=io.open('lib/research/social/collect.py',encoding='utf-8').read(); print('dataset', c.count('gd_lvz8ah06191smkebj4'), 'discover-by-keyword', c.count('keyword'), 'num_of_posts-cap', c.count('num_of_posts'), 'trigger-route', c.count('/datasets/v3/trigger'), 'x-dataset-run', c.count('gd_lwxkxvnf1cynvib9co') and c.count('profiles_array'), 'usd-guard', c.count('usd'), 'states', sum(c.count(s) for s in ('FAILED','ZERO','STALE','CAPPED','RUNNING')), 'nonascii', sum(1 for ch in c if ord(ch)>127))"</invocation><expect>the suite ends OK with 0 failures and 0 errors (the five states, the cap, the window, the validator pass-through); dataset at least 1; discover-by-keyword at least 1; num_of_posts-cap at least 1; trigger-route at least 1; x-dataset-run 0 (the X method is named in the record, never run here); usd-guard at least 1; states at least 5; nonascii 0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rj-13"><invocation>timeout 115 python -m lib.research.social.collect --security-key BA_US_Equity --as-of 2026-09-15 --cap 50 --window-days 30 --write-pool 2>&1 | tail -14</invocation><expect>lines: METHOD reddit keyword with the dataset, the keywords, the cap 50 and the window; ESTIMATE with the USD cap check (under 5); JOB with the id and submitted_at persisted BEFORE polling; POLL with the interval, the waits and the final state (COMPLETE, or STILL_RUNNING at the max wait -- recorded as that state, a valid measurement outcome); DELIVERY with records, valid, admitted, rejected_by_rule, stale, capped; LATENCY seconds; COST usd; QUALITY with a 10-item relevance sample; OK: uploaded social/v1/_measurement/2026-09-15.json with read-back. A job without a persisted id, or a poll that resubmits discovery, is NOT met; a STILL_RUNNING outcome is met when the retrieval flow is documented in the record and a second retrieval is named in a row</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rj-13"><invocation>.tools/aws s3api get-object --bucket opal-data-harvest --key social/v1/_measurement/2026-09-15.json .scratch/rj13.meas.json --query "[ContentLength,Metadata]" --output json; python -c "import json,io,jsonschema; d=json.load(io.open('.scratch/rj13.meas.json',encoding='utf-8')); s=json.load(io.open('lib/research/social/measurement.schema.json',encoding='utf-8')); jsonschema.validate(d,s); print('schema-valid True method', d['method']['platform'], d['method']['discover_by'], 'cap', d['method']['cap'], 'job-state', d['job']['state'], 'records', d['delivery']['records'], 'admitted', d['delivery']['admitted'], 'second_candidate', d['second_candidate']['status'], 'cost', d['cost'])"</invocation><expect>Metadata with document-sha256 and schema-version 1; schema-valid True; method reddit keyword with cap 50; a job-state in the five states; records and admitted printed (0 is a valid measured outcome, distinguished from failure by the state); second_candidate NOT_RUN; cost printed with its unit. A record without the job identity is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rj-13"><invocation>git log --format="%h %an %s" -3 -- lib/research/social/ | cut -c1-140; git diff --stat SITEZ...HEAD -- lib/research/social/schema.json lib/research/social/validator.py | cat; echo "item-contract-diff-lines: $(git diff SITEZ...HEAD -- lib/research/social/schema.json lib/research/social/validator.py | wc -l)"; python -c "import io,glob; fs=glob.glob('lib/research/social/*.py'); print('raw-secretsmanager-reads', sum(io.open(f,encoding='utf-8').read().count('get_secret_value') for f in fs), 'serp-zone-use', sum(io.open(f,encoding='utf-8').read().count('serp_brightdata') for f in fs))"</invocation><expect>commits by this serial; item-contract-diff-lines 0 (the item schema and the admission rule are untouched); raw-secretsmanager-reads 0; serp-zone-use 0. A rewritten admission rule is NOT met</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~22/AMGT_RESAPP.TO-AMGT-rj-13.the-social-source-measured.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json` (the checker compiles `expect` as a REGEX over the evidence), graded by YOUR WORKTREE'S
OWN `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4` (rc 0 is the verdict); keep the job log and the measurement record
beside it; flip `<status>` to `complete`; commit with `--only -- <paths>`. Report once. **If a criterion cannot be met, leave the order
OPEN and file a row.**

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>11</round>
<slot>~22</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<authority>PRD v0.8 @`1170b4da69` (ADMITTED) s.4 row S13 ("measure, then build"), s.9a-2's social row, C-LISTING-NOT-CAPABILITY and C-VENDOR-EGRESS (standing; the session egress word @`dfa63b6d92`); the CRO's social brief @`36a08d3d1a`, audit @`1906df40bd` and follow-up @`865e4fc113` item 1; FWD-11 / FWD-16; decomposition v1.3 s.19 @`73938cdae4` (cell rj-13, chain E second; interface S-1). Cell set: s.19a; fan-out: s.19e.</authority>

<preflight>
ALL RUN 2026-09-15 06:4xZ at this cut (decomposition v1.3 s.19g).
comp-schedule: RUN (--drift) -- 5 of 5 carriers within budget (16.0 s of 90); REACHED-DENOMINATORS C1=23, C2=8, C3=12, C4=21, C5=334; C2 = 8 OPEN deploy-ledger entries (none this project's; rj-10 opens one and closes it inside the round); C3 = 12 standing NEVER clauses (no monitor, no alarm); NO new scheduled producer is cut this round (every batch is a local Windows task DISABLED at creation, Andrew's box word @187f003998); BLIND on C4 and C5 in the tool's own voice.
comp-iam: RUN (gaps) -- 838 call(s) verdicted across 98 mapped role(s) over 474 .tf files; 629 UNRESOLVABLE-RESOURCE, 142 GRANTED, 51 GRANTED-BROAD (EXCLUDED, NOT CLEARED), 14 UNGRANTED, 2 GRANTED-ACTION / UNGRANTED-RESOURCE; 15 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 32 services; BLIND on 266 calls in 26 role-UNMAPPED services. The round's IAM delta lives in rj-10 alone: READ grants by prefix on opal-data-harvest for two roles, the DynamoDB articles grants REMOVED, no Scan, no wildcard resource; every other cell acts under the operator's own credentials and takes no AWS grant.
comp-adversary: RUN (compose on the decomposition, --no-packet) -- 48 commit pins, 13 repo paths, 17 file:line cites, 14 tool mentions; 23 hex runs not parsed (named); T11 NOT RESOLVED (293 uncited siblings, CAP 25 declared); stage 4 disabled by the caller. The round's adversarial surfaces: filing text, vendor responses and pool objects are DATA inside a model prompt (rj-6, rj-11 say so in the prompt; the verbatim gate runs against the PASSAGE; held-uncited claims never render); Posture is marked machine and read by no trade consumer; the Lusha response is scrubbed to name/title/link; the social job is capped in posts and USD.
comp-cache: DECLARED-NOT-APPLICABLE -- no portal surface in this cell.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell moves nothing on the live plane: its writes are local code, tests and pool objects under the operator's credentials (a QA one-shot is not a production act); the round's one live move is rj-10's, covered by the co-sign.
</preflight>
