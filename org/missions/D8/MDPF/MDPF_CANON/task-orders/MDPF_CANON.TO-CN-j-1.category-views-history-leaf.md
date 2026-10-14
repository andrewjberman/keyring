# MDPF_CANON task order -- `CN-j-1` -- THE HISTORY LEAF: ONE READ-ONLY SERVED SERIES PER SCOPE OVER THE DATED CATEGORY-VIEWS OBJECTS (FWD-9, the Client chips)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-j-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~23</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the leaf is built inside the publisher's existing scheduled run (cron(50 13 * * ? *) UTC), and a malformed input is named in its manifest row, not alarmed.
comp-iam: DECLARED-NOT-APPLICABLE for this cell's code -- the leaf is written under platinum/mdpf/* with the same PutObject the 18 gold pairs use and read from portal/gold/mdpf/* with the same GetObject; no grant is added or widened. Measured by simulation on 2026-10-13: PutObject on platinum/mdpf/global/category-views-history.json is ALLOWED for opal-assets-mdpf-egress-publisher-role; GetObject on portal/gold/mdpf/global/category-views/2026-08-27.json is ALLOWED.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r7_cn_j_1.py unit 0 of 6, seam 3 of 8 (S2, S7, S8 are controls that hold) and real 2 of 6 (R0, R2 are controls) at base; a scratch reference publisher reads 6 of 6, 8 of 8 and 6 of 6 (real, on the 91 dated objects of the four scopes); two planted mutants turn red (a missing node read as 0.0 -> U3; a leaf that ignores the pointer -> S3).
EGRESS CLASS, declared: NONE for the worker (it writes no AWS). The deploy is CloudOps's, in its own window, after a never-widen pair.
</preflight>

## 1. THE CELL -- `CN-j-1` (round 7, decomposition v7)

**The rule (CTO ruling msgs 5086-5088, PRD v2.15).** The Model Portfolios AUA Trend draws two Client chips ("Client Supervised", "Client Unsupervised") from
each date's category-views snapshot. The portal serves only the LATEST category-views object per scope (`platinum/mdpf/{scope}/category-views.json`), so
a chip can be drawn at the as-of only. The dated objects (A4 gold, write-once, `portal/gold/mdpf/{scope}/category-views/{YYYY-MM-DD}.json`; measured
2026-10-13: 26, 25, 19 and 21 of them for 49financial, inflection, cottonwood and global, first date 2026-08-27) hold the history. This cell adds ONE
read-only served leaf per scope that carries that history and nothing else:

`platinum/mdpf/{scope}/category-views-history.json` = `{schema, leaf, scope, n_dates, dates[], client_supervised[], client_unsupervised[], omitted[], _provenance}`.

**Where it runs.** `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py` (566 lines; read the module docstring, `derive_publish_set`,
`_publish_one`, `lambda_handler` first -- they are the idiom). The publisher READS `portal/gold/mdpf/` and WRITES `platinum/mdpf/`; today every served leaf is a 1:1
projection of one gold key. This leaf is the one exception, and the docstring must say so (Step 4). It reads only gold keys it already lists; it never reads the
platinum plane except the one pointer read it already makes.

### Step 0 -- the edge read (read-only, your first act; report the result in your final message)

The route is claimed to need no edge change: the Lambda@Edge router rewrites `/api/general/mdpf/*` to `/platinum/mdpf/*` by prefix
(`infra/aws/lambda-edge/public-data-router/index.mjs:51-56`) and the origin grant is prefix-scoped over `platinum/mdpf/*`
(`infra/aws/terraform/shared-infra/s3-portal-v2-import.tf:131`). Not yet read: the CloudFront behaviours and WAF rules. Read them with read-only
`aws cloudfront` / `aws wafv2` get/list calls and report whether any behaviour, function association or WAF rule names an individual leaf
(`aum-metrics`, `category-views`, `account-distribution`, `aggregate-aua-timeseries`) or limits the path to a fixed leaf list. If one does: file a BLOCKING row
(`MDPF_CANON-D1-W17-S<k>`) naming it and STOP before Step 1 -- the leaf would not be reachable without an edge change, which this project may not make before
FIRMBKTS's flip receipt (PRD v2.11 R2). If the read is refused (AccessDenied) file an OBSERVATION row saying so and CONTINUE: the code change is independent of
the edge and the deploy order re-measures before it applies anything.

### Step 1 -- `assemble_history_leaf` (a new module-level function, placed directly before `_publish_one`)

```
HISTORY_LEAF = "category-views-history"
HISTORY_SCHEMA = "mdpf-category-views-history/v1"
HISTORY_SOURCE_TYPE = "category-views"
CLIENT_SUPERVISED = "Client - Opal Supervised"
CLIENT_UNSUPERVISED = "Client - Opal Unsupervised"
def assemble_history_leaf(scope, dated) -> (content, omitted)    # dated: iterable of (YYYY-MM-DD, body bytes)
def _content_sha(content) -> hex sha256 of json.dumps(content, sort_keys=True, separators=(",", ":"))
```

Behaviour, exactly:

1. **Pure and deterministic.** Sort the input ascending by date; the same dated objects in any order give an equal `content` and an equal `_content_sha`.
2. **Per dated object**, read `body["nodes"]["Client"]["children"][<name>]["aum"]` for the two names. A missing node, a missing `aum`, a `None`, a bool or any
   non-number gives `None` (ABSENT IS NOT ZERO: a missing node is never read as `0.0`). A measured `0.0` stays `0.0`. The date is KEPT in `dates` with the null.
3. **Omit and name, never fill.** A body that is not valid JSON (`reason` "unparseable"), is not a JSON object ("not_an_object"), or carries an `as_of`
   whose first ten characters differ from its key date ("as_of_differs_from_key") is left out of every array and appended to `omitted` as
   `{"date": <date>, "reason": <reason>}`.
4. **The content** is exactly `{schema, leaf, scope, n_dates, dates, client_supervised, client_unsupervised, omitted}` -- no other key, three arrays of equal
   length, `n_dates == len(dates)`. No model name, firm id, account figure, or any other node of the dated object is copied.

### Step 2 -- `_publish_history_one` and the handler hook

For each scope that appears in the derived publish set with type `category-views` (so the scope set comes from the gold listing, never a literal list):
list the dated keys under `{GOLD_ROOT}/{scope}/category-views/` (the existing `_KEY_RE` grammar), read each, call `assemble_history_leaf`, hash the content, and
write `{SERVE_ROOT}/{scope}/category-views-history.json` with the SAME `put_object` call shape and an additive `_provenance` the other leaves carry
(`written_by`, `written_at`, `source_keys` = [first dated key, last dated key] as `s3://` URIs, `source_count`, `source_vintages` = {"<scope>/category-views-history":
<last date>}). Build the key from `SERVE_ROOT` exactly as `_publish_one` does; type no `platinum/mdpf` literal and add no bucket, prefix or name (the publisher's
serve keys are existing-pipeline f-strings; the naming gate's non-application for an existing pipeline applies).

- **D5 for the leaf.** If the previous pointer's `history_rows["<scope>/category-views-history"].content_sha256` equals this run's and the served key is listed,
  the status is `unchanged` and there is NO `put_object`. Add a `load_latest_pointer_doc(s3)` that returns `(pointer_doc, error)` from ONE read of `latest.json` and
  use it in the handler for both `rows` and `history_rows` (so the handler still makes exactly one served-plane read). Keep `load_latest_pointer` working.
  Measured fact you do not fix: the publisher's role CANNOT read `latest.json` in production (`AccessDenied`, manifest `20261013T135047Z-4fca44fb` carries it
  in `prior_pointer_note`), so every production run reads an empty pointer and republishes all 18 pairs; the history leaves will do the same. That is existing
  behaviour; the tests (which stub S3) are where `unchanged` is exercised. Do not add a read of the platinum plane to get around it.
- **Isolation.** A failure on one scope's leaf sets that row's `status` to `error` with the message and never sinks the run or another scope's leaf. The rows
  live under a NEW manifest key `history_rows` ("<scope>/category-views-history" -> `{serve_key, status, content_sha256, n_dates, n_source_objects, omitted, ...}`)
  and under `history_rows` in the pointer; they are NOT added to `results`, `expected`, `derived_pairs`, `failed` or `all_present`, and they do not change
  `published` / `unchanged` / `missing_pairs` / `unexpected_pairs` (those keep meaning "the gold-projected pairs"). A scope with no `category-views` gold writes no
  leaf and is reported by the existing `missing_pairs` exactly as today.
- Nothing in the 18 gold-projected leaves changes by a byte.

### Step 3 -- tests

(a) `tests/test_history_leaf.py` (new; the idiom and `StubS3` of `tests/test_completeness.py`; copy the stub, do not import across test modules), at least SIX tests:
the leaf is written for each of the four scopes with the dated nodes' values; ascending order whatever the listing order; a missing node is `None` not `0.0` and a
measured `0.0` survives; a malformed dated object is omitted and named while the other scopes' leaves are written and `all_present` is unaffected; a second run
makes zero serve-key writes and the pointer carries four `history_rows`; a scope without `category-views` gold writes no leaf and `missing_pairs` still names it.
(b) `tests/test_completeness.py`: its three comprehensions that collect the serve-key writes
(`if not k.startswith("platinum/mdpf/_manifests/")` and the `k2` form) gain `and not k.endswith("category-views-history.json")` (and the `k2` equivalent), so
the 18 gold pairs are still asserted as 18 and the history leaves are asserted in their own file. **Change nothing else in that file; delete, loosen or skip
no assertion.**

### Step 4 -- the docstring

Add to the module docstring a short paragraph: the one derived leaf, why (FWD-9, the ruling msgs), that it is read-only over existing dated gold, that it
adds no field to any gold-projected leaf, and that "NEVER ... synthesizes fields" in the header continues to hold for every gold-projected leaf.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke of the publisher, no `s3 cp`/`put`/`rm`, no `build_package`, no `safe-deploy`. Read-only
   `get`/`list`/`describe` is allowed (Step 0; criterion AC3 reads 91 dated gold objects). No install, no push. REFUSE, do not rescue. The deploy of this code is
   CloudOps's, in its own window, after a never-widen pair; none of it is yours.
2. Only the files in section 3 change. The gold tier, the consolidator, every other publisher function, the Terraform, the edge (router, CloudFront, WAF), the portal
   and the category registry are read-only. `a4_expected`, `ARTIFACT_TYPE_SCOPE_SET` and the artifact-type axis are NOT touched (the leaf is not a gold type).
3. **Never** loosen, wrap or skip an existing assertion; never widen an IAM statement; never read the platinum plane to make `unchanged` work in production.
4. The leaf carries ONLY the date axis and the two Client aum arrays: no model, firm, account or node name beyond the two fixed Client child names the field
   names echo, and no other number.
5. **CLIENT DATA:** never print an account id. No non-ASCII. Keep each file's line endings as you find them (read them first; both publisher files are LF). Use the Edit tool.
6. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py
infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/tests/test_completeness.py
infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/tests/test_history_leaf.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-j-1.category-views-history-leaf.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~23/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/build_package.py`,
`infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf`, `infra/aws/lambda-edge/public-data-router/index.mjs` and the issuer's checks under
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/` (`r7_cn_j_1.py`, `ref/make_reference_publisher_j1.py`; never edit them, read what each
arm asserts). The reference file shows the shape the issuer's arms accept; your code is yours and must be your own reading of the order.

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_j_1.py" unit; echo "exit=$?"</invocation><expect>ROUND 7 CN-J-1 UNIT: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_j_1.py" seam; echo "exit=$?"</invocation><expect>ROUND 7 CN-J-1 SEAM: 8 of 8 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_j_1.py" real; echo "exit=$?"</invocation><expect>ROUND 7 CN-J-1 REAL: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-j-1" judgment="true"/>
</proof_of_spec>

AC4 is JUDGMENT, graded at the round-7 close (never self-graded): `/seams` on the leaf-to-chip seam, grounded on the served objects after the deploy and the first
scheduled publisher run that carries the code -- MECHANICAL (the four `platinum/mdpf/{scope}/category-views-history.json` keys exist, reachable through
`/api/general/mdpf/{scope}/category-views-history.json`, each leaf's arrays equal that scope's dated category-views nodes, every existing served leaf byte-equal
apart from `_provenance.written_at`), DECLARATIVE (the leaf names its schema, its omitted dates and its source vintage), SEMANTIC (the Trend's Client chips draw
on the leaf's dates and are absent, never zero, on every other date).

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~23/MDPF_CANON.TO-CN-j-1.category-views-history-leaf.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for), with AC4 UNVERIFIABLE-BY-INSTRUMENT and status_reason
"graded at the round-7 close". **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your
paths), and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W17-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the Step 0 result (what you read and what it showed), the diff (one line per file), the output line of every criterion, the lines you read for the
single-pointer-read claim, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7, from the CTO's round-6 analysis (FWD-9 enters beside CN-h-1, msgs 5067, 5071, 5086-5088; PRD v2.15-v2.16). Design:
`round7/HISTORY_ROUTE_DESIGN_READ.md` @add7fc4481 (option B, recommended and ruled "its own cell and pair"); the consumer is `TO-CN-i-1`.
- **Three corrections to the design read, all measured 2026-10-13 by the drafting fork:**
  (1) The design read said the publisher "keeps only the latest dated key per scope and type" and so assembles a leaf; it also said the leaf rows join "the manifest's
  results map". They do not: the leaf is NOT a gold pair, so it stays out of `results`, `expected`, `failed` and `all_present` (a new `history_rows` carries it). Folding it
  into `results` would have made `all_present` and the existing tests assert over a set that is not the gold-derived set.
  (2) The design read's idempotence ("recomputed each run from the listing") is kept, but the D5 comparator is dead in production: the publisher's role has NO
  GetObject on `platinum/mdpf/_manifests/latest.json` (simulation: implicitDeny; manifest `20261013T135047Z-4fca44fb` `prior_pointer_note` AccessDenied; today's run
  published 18 of 18). So the leaf is rewritten every production run like the 18 pairs; its content is deterministic, so only `_provenance.written_at` differs.
  The order does NOT widen IAM to repair that; it is a separate finding (surprise row to be filed by the issuer) for its own pair.
  (3) The earlier "N = 1 writer" stands, but the publisher's header says it "NEVER patches shape, renames, or synthesizes fields; it projects an already-canonical gold".
  A derived leaf departs from that. The precedent for a deliberate extension is `taxsma_extend` (TX-u-1, contract 0.6.0, behind a rollout switch). The PRD's CONTRACTS
  row for the served platinum JSON enumerates four leaves (`aggregate-aua-timeseries`, `account-distribution`, `aum-metrics`, `account-units`) and does not name
  `category-views` or this leaf: the CTO/CVO ratified-text half needs a CONTRACTS addendum naming `category-views-history` before the pair is signed (asked in the issuer's message).
- **Row to the CTO:** D1-S21 (the category-views snapshot and the NEWEST time series differ by up to 301,207.84 on the same date; they agree to 0.00 against each date's OWN dated
  ts object). The leaf serves the snapshot's own Client numbers; the cent-exact sum for a chip date is read against that date's own dated ts object, and the grade says so.
- **The pair (CTO + COO, written at the drain by the issuer, never by the worker):** `NEVER_WIDEN_PAIR_R7_CN_J_1.md` (draft beside this file).
- **Deploy order (CloudOps ~DELL1, a WORLD order the issuer cuts after the drain; never a worker):** publisher package only: `build_package.py --pin <the merge commit>`,
  upload, a targeted `safe-apply` on the publisher function that moves the code AND `MDPF_PUBLISHER_COMMIT` in `infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf`
  (line 163, the D1-S18 class of stamp: set it from the pin actually built), read the deployed package's manifest back, and a read of the four served leaves after the
  first scheduled publisher run (13:50Z) -- an on-demand publisher invoke writes real served keys, so the order authorizes none; the edge read of Step 0 repeats as a
  precondition. No consolidator or gold-lambda deploy: nothing here touches `mdpf-gold-lambda`.
- **Risk and class:** WORLD (once deployed the cell adds four served keys and a manifest field). `worker`, not light: about 110 product lines, a new test file, and an edit to
  an existing test file.
- **Fanout:** one cell, one chain, slot ~23; no shared file with CN-h-1 (`dim_mdpf_aggregate_aua_timeseries.py` and tests) or CN-i-1 (portal files); a deploy-order edge
  only: CN-i-1's Client chips draw the history from this leaf once it is served (CN-i-1 ships as-of first without it), and FWD-9's grade waits for it. Base box/dell1.
- **Checks at base (dry-run before the cut):** `r7_cn_j_1.py unit` 0 of 6, `seam` 3 of 8 (S2, S7, S8 controls), `real` 2 of 6 (R0, R2 controls). Scratch reference: 6/6, 8/8, 6/6;
  `selftest` OK (two mutants RED).
- **Not provable offline, graded after deploy (AC4 and the pair's read-back):** the edge reaching the new leaf (CloudFront behaviours and WAF were not read), the served bytes
  of the four leaves, the deployed publisher's `CodeSha256` and manifest, and the portal fetch (CN-i-1's).

<status>complete</status>
<round>7</round>
<to_id>MDPF_CANON.TO-CN-j-1</to_id>
<slot>~23</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
