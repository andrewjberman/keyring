# TO POSN_AGGFIX.TO-A2-1 -- THE PRODUCER CHANGE, PROVED LOCALLY: the weights and each book's `aum` come from Opal's current assets-by-model file, the aggregate counts the primary models and their blends, and it leaves the shared file for the Opal-only key -- proved by running the handler before and after on the SAME inputs with every S3 write captured and nothing served (AF1-s-6, AF1-s-7, AF1-s-8; FWD-4, FWD-6, FWD-7, FWD-8)

<to_id>POSN_AGGFIX.TO-A2-1</to_id>
<project>POSN_AGGFIX</project>
<issued_to>0.9.0_WK_POSN_AGGFIX~1</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2**
@`cbd85e5cff` (C-CURRENT-SOURCE, C-MEMBERS, C-NO-SILENT-EMPTY, C-OPAL-ONLY-DATA, C-FIVE-BOOKS-UNCHANGED) - **Decomp cells:** `AF1-s-6`,
`AF1-s-7`, `AF1-s-8` - **Issuance:** round 1, slot `~1`, SECOND in this slot's queue. **Handed to you only after TO-A1-1 drained.**
**NO DEPLOY AND NO SERVED WRITE IN THIS ORDER: every S3 write the handler attempts is captured to your scratch.**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_AGGFIX~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_AGGFIX~1;`. Your worktree is
`/c/tmp/wk-aggfix-1-1` (branch `wk-posn_aggfix-1-1`). First act: `git rev-parse --abbrev-ref HEAD` and
`test -d org && test -d .tools && echo TREE-OK`, then bring SITEZ's drain of your previous order into your branch if it is not already an
ancestor (`git merge-base --is-ancestor SITEZ HEAD || git merge --no-edit SITEZ`; never a rebase). Commit ONLY via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_AGGFIX~1 <0.9.0_WK_POSN_AGGFIX~1@opal.agent>" -F <msgfile> -- <paths>` (msgfile by
the Write tool, PURE ASCII). Every `.py` edit passes `.tools/commit-gate.sh`. Never push, rebase, `checkout --`, `clean`. Scratch in
`/c/tmp/wk-aggfix-1-1/.scratch/` only.

**THE BEFORE-ARM ANCHOR IS A FIXED COMMIT, `605c03f81f`** (the decomposition commit). Read the producer's before-bytes with
`git show 605c03f81f:infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`, never from a
drain ref or a merge-base, which move.

## THE CELLS (verbatim from the decomposition @`605c03f81f`)

**`AF1-s-6` -- the weights and each book's `aum` come from the current file (S6, C-CURRENT-SOURCE, C-MEMBERS, C-NO-SILENT-EMPTY).** In
`lambda_function.py`, the Lambda branch of `load_aum_data` (:1421-1476) reads `platinum/mdpf/global/aum-metrics.json` and records its
VersionId and `period`; the legacy key `json/portfolios/aum-metrics.json` has ZERO occurrences in the file afterwards. A module constant
carries the standard's membership (primary `served_name` -> code; blend `served_name` -> constituents and shares) and is proved equal to
`org/standards/POSN_AGGREGATE_MODEL_SET.json`. The result separates (a) `book_aum`: each primary model's OWN row, no blend share, for the
five books (:1798 keeps `.get(code, 0)`, so a failed read still writes 0 into each book, unchanged); (b) `member_aum`: each primary row
plus each blend's constituent shares; (c) `left_out`: every row that is neither. A failed read, or a file missing any of the five
primary rows, makes the aggregate UNAVAILABLE (never an empty aggregate that reads as current). The local (non-Lambda) branch :1478-1522
is not the legacy key and is untouched.

**`AF1-s-7` -- the aggregate computed over the members (S7, C-MEMBERS, C-NO-SILENT-EMPTY).** `calculate_aggregated_holdings` (:1525)
weights each model by `member_aum[code] / members_sum`; `model_breakdown` keeps today's meaning (each model's own weight in that ticker);
`total_aum` = `members_sum` (1.1). A zero or UNAVAILABLE total returns the UNAVAILABLE payload rather than `[]` (:1538-1541 today). The
exercise re-derives the aggregate weight of three named holdings by hand from the model books and the member AUM and matches the
producer's output to 6 decimals.

**`AF1-s-8` -- the aggregate leaves the shared file for the Opal-only key (S8, C-OPAL-ONLY-DATA, C-FIVE-BOOKS-UNCHANGED).**
`extract_current_holdings` stops writing `current_holdings['AGG']` (:1811-1814); the handler writes the 1.1 payload to
`json/positioning/opal_aggregate.json` beside `OUTPUT_KEY` with the same put shape (:2627-2634), on EVERY run (OK or UNAVAILABLE). The
exercise runs the handler at the base commit and at the branch HEAD against the SAME inputs with S3 writes captured (never served) and
proves: the shared file's five books byte-identical in every field except `aum`; each book's `aum` equals its own current `by_model` row;
`current_holdings` carries exactly the five books; every other top-level key byte-identical apart from `generated_at`; the new key's
payload matches 1.1 with `status OK`; and the failure arm (the current file unreadable) yields `status UNAVAILABLE`, books `aum` 0.

**THE 1.1 CONTRACT (decomposition s.1.1 -- the three chains share it; do not change a key):**
```
{ "status": "OK" | "UNAVAILABLE", "reason": null | "<one line>",
  "generated_at": "<ISO Z>", "data_as_of": "<YYYY-MM-DD>",
  "current_holdings": { "AGG": { "holdings": [ <exactly today's AGG holding shape> ], "total_aum": <float> } },
  "weights": { "UST": w, "ST": w, "INT": w, "LT": w, "ULT": w },
  "weights_source": { "key": "platinum/mdpf/global/aum-metrics.json", "version_id": "<VersionId read>", "period": "<file period>" },
  "members": { "UST": aum, "ST": aum, "INT": aum, "LT": aum, "ULT": aum,
               "blends": [ { "model_name": "...", "aum": x, "constituents": { "<code>": share, "<code>": share } } ] },
  "left_out": [ { "model_name": "...", "aum": x } ],
  "reconciliation": { "five_primary_sum": x, "members_sum": y, "file_total_model_aum": z, "gap": z - y,
                      "gap_explanation_ref": "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/AF1_S1_GAP_EXPLANATION.md" } }
```
`current_holdings.AGG.total_aum` is `members_sum`. `status UNAVAILABLE` carries `holdings: []`, a non-null `reason`, and whatever of
`weights_source` / `members` / `reconciliation` was readable (nulls otherwise).

**ONE PRECISION THE ISSUER ADDS, MEASURED at `lambda_function.py` @`605c03f81f` (it refines AF1-s-6's parenthesis, it does not change the
cell):** "today's failure fallback" has TWO arms and you keep BOTH exactly. (i) A WHOLLY failed weight read returns `{}` (:1475-1477),
and `generate_positioning_data`'s gate `if aum_data:` (:2374-2381, the function defined at :2117) sets `current_holdings = None`, so
:2392-2395 writes NO `current_holdings` key and no `data_date` into the shared file at all. (ii) A PARTIAL read (a code absent from the
dict) writes `aum: 0` into that book only (:1798). Row `POSN_AGGFIX-Z-S1` records the PRD sentence that describes only arm (ii). Your change keeps (i) keyed on `book_aum` being empty and (ii) on
`.get(code, 0)`, and in both arms the Opal-only key is written with `status UNAVAILABLE`.

**Your inputs from TO-A1-1 (read them at SITEZ, never re-derive):** `AF1_S1_GAP_EXPLANATION.md` (cited by `gap_explanation_ref`); the blend
verdicts (a CONTRADICTED blend STOPS this order with a BLOCKING row; NO-DEFINITION-FOUND proceeds on the standard as written).

## YOUR ACT

1. `lambda_function.py` only. Implement AF1-s-6, AF1-s-7 and AF1-s-8 with the smallest diff that meets them: the membership constant; the
   Lambda branch of `load_aum_data` re-pointed and returning the three separated maps plus source VersionId, period, file total and
   status; `calculate_aggregated_holdings` over `member_aum`; `extract_current_holdings` without the AGG write; the handler writing the
   1.1 payload to `json/positioning/opal_aggregate.json` with the put shape at :2627-2634 after the shared file. The CLI `main()` keeps
   working, and its `--upload` branch (:2489-2510) -- the shared key's SECOND write site (row W1-S4) -- writes the 1.1 payload to
   `json/positioning/opal_aggregate.json` beside the shared file with the same put shape, so a manual upload never serves a shared file
   without its aggregate key. Every other function stays byte-identical.
2. `<PRODUCER_HARNESS_A2>`: a script in your deliverables folder. It loads the recorded `GeneratePositioning` event from the state
   machine's LAST execution that ran it (`YangDataPipeline`, `get-execution-history`, read-only; the raw input string, never a
   hand-written event), then runs `lambda_handler` twice in separate subprocesses with `AWS_LAMBDA_FUNCTION_NAME` set: BEFORE = the file
   at `605c03f81f`, AFTER = your working file. A boto3 wrapper passes every READ through to the real service and CAPTURES every
   `put_object` / `upload_*` / `delete_*` / `copy_object` to `.scratch/` without calling the service (any other write call aborts the
   run). It prints the comparisons the criteria name. Modes, one per criterion that invokes it: `--membership-equals-standard`
   (A2-AC2, no handler run), `--compare` (A2-AC3), `--book-aum` (A2-AC4), `--aggregate-payload` (A2-AC5), `--hand-rederive` (A2-AC6),
   `--fail-weights` (A2-AC7: the platinum `get_object` raises in AFTER; the legacy one raises in BEFORE), `--partial-weights` (A2-AC8:
   the platinum `by_model` served to AFTER with the ULT row removed; the legacy `by_model` with the ULT row removed to BEFORE), `--cli-upload` (A2-AC13: `main()` with `--upload` under the same
   capturing wrapper and the same model PKL). The
   normal-run modes may share one cached pair of runs in `.scratch/` as long as each mode prints which run it read.
3. Record every criterion; file rows for anything off-cell; keep working.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, id `POSN_AGGFIX-Z-W1-S<k>` continuing your sequence, in
`org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md` per the investigation schema; keep working.

## CRITERIA -- structured, one clause each

<criterion id="A2-AC1" cell_refs="AF1-s-6"><invocation>timeout 60 python -c "p='infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py'; s=open(p,encoding='utf-8').read(); print('legacy', s.count('json/portfolios/aum-metrics.json')); print('platinum', s.count('platinum/mdpf/global/aum-metrics.json')); print('opal_aggregate', s.count('json/positioning/opal_aggregate.json'))"</invocation><expect>legacy 0; platinum 1 or more; opal_aggregate 1 or more.</expect></criterion> `A2-AC1` -- THE LEGACY READ IS GONE FROM THE BYTES.

<criterion id="A2-AC2" cell_refs="AF1-s-6"><invocation>timeout 120 python <PRODUCER_HARNESS_A2> --membership-equals-standard</invocation><expect>the module constant's primary map (served_name -> code, 5 entries) and blend map (served_name -> constituents with shares, 2 entries) printed beside the same maps read from org/standards/POSN_AGGREGATE_MODEL_SET.json, and `MEMBERSHIP EQUAL` printed; the control arm (one share changed to 0.4 in memory) prints `MEMBERSHIP DIFFERS`.</expect></criterion> `A2-AC2` -- THE PRODUCER'S MEMBERSHIP IS THE STANDARD'S.

<criterion id="A2-AC3" cell_refs="AF1-s-8"><invocation>timeout 1200 python <PRODUCER_HARNESS_A2> --compare</invocation><expect>the recorded event's execution ARN and model_pkl_key printed; both runs complete; for the captured shared file: `current_holdings` keys BEFORE = UST ST INT LT ULT AGG and AFTER = UST ST INT LT ULT; per book, every field except `aum` byte-identical (a per-book line `BOOK <code> NON-AUM IDENTICAL`, 5 of 5); every top-level key other than `generated_at` and `current_holdings` byte-identical (a line naming the keys compared and `TOP-LEVEL IDENTICAL`); and a CONTROL line where one holding weight mutated in the AFTER copy in memory is reported as a difference.</expect></criterion> `A2-AC3` -- THE SHARED FILE MOVES ONLY WHERE THE PRD SAYS.

<criterion id="A2-AC4" cell_refs="AF1-s-6"><invocation>timeout 1200 python <PRODUCER_HARNESS_A2> --book-aum</invocation><expect>for each of the five books, the AFTER shared file's `aum`, the platinum by_model row read by the run (model name and VersionId), and `EQUAL`, 5 of 5; the BEFORE values printed beside them equal to the legacy file's rows.</expect></criterion> `A2-AC4` -- EACH BOOK'S AUM IS ITS OWN CURRENT ROW.

<criterion id="A2-AC5" cell_refs="AF1-s-7,AF1-s-8"><invocation>timeout 1200 python <PRODUCER_HARNESS_A2> --aggregate-payload</invocation><expect>the captured json/positioning/opal_aggregate.json (put with ContentType application/json, ContentEncoding gzip, CacheControl no-cache, printed) decompresses to the 1.1 contract with every key present; status OK; weights sum to 1 within 1e-9; each weight equals members[code] / reconciliation.members_sum; current_holdings.AGG.total_aum equals reconciliation.members_sum; reconciliation.gap equals file_total_model_aum minus members_sum; members.blends has 2 entries and left_out lists every other row (0 on today's file); weights_source.version_id equals the VersionId the run read.</expect></criterion> `A2-AC5` -- THE OPAL-ONLY PAYLOAD IS THE CONTRACT.

<criterion id="A2-AC6" cell_refs="AF1-s-7"><invocation>timeout 1200 python <PRODUCER_HARNESS_A2> --hand-rederive</invocation><expect>for the three largest AFTER aggregate holdings by weight, the weight re-derived by hand as the sum over the five books of (the book's weight in that ticker x members[code] / members_sum), printed beside the producer's value with `MATCH` at 6 decimals, 3 of 3; the AFTER aggregate's ticker set equals the union of the five books' tickers.</expect></criterion> `A2-AC6` -- THE AGGREGATE ARITHMETIC, BY HAND.

<criterion id="A2-AC7" cell_refs="AF1-s-6,AF1-s-7"><invocation>timeout 1200 python <PRODUCER_HARNESS_A2> --fail-weights</invocation><expect>BEFORE (legacy read raising): the shared file carries no current_holdings key and no aggregate; AFTER (platinum read raising): the shared file carries no current_holdings key, and json/positioning/opal_aggregate.json IS captured with status UNAVAILABLE, holdings [], a non-null reason; both captures printed.</expect></criterion> `A2-AC7` -- A FAILED WEIGHT READ NEVER SERVES AN AGGREGATE AS CURRENT.

<criterion id="A2-AC8" cell_refs="AF1-s-6,AF1-s-7"><invocation>timeout 1200 python <PRODUCER_HARNESS_A2> --partial-weights</invocation><expect>BEFORE: the ULT book's aum is 0 and the other four books carry their rows; AFTER: the ULT book's aum is 0, the other four carry their platinum rows, and json/positioning/opal_aggregate.json is captured with status UNAVAILABLE and a reason naming the missing primary model; both printed.</expect></criterion> `A2-AC8` -- A PARTIAL WEIGHT READ, BOTH FALLBACK ARMS KEPT.

<criterion id="A2-AC9" cell_refs="AF1-s-6,AF1-s-7,AF1-s-8"><invocation>timeout 300 bash .tools/commit-gate.sh infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py</invocation><expect>`OK: pre-commit gate clean for 1 of 1 file(s)`.</expect></criterion> `A2-AC9` -- THE GATE ON THE CHANGED .PY.

<criterion id="A2-AC10" cell_refs="AF1-s-8"><invocation>timeout 60 python -c "p='infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py'; b=open(p,'rb').read(); print(p, len(b)-len(b.decode('utf-8'))); c=open('CLAUDE.md','rb').read(); print('CLAUDE.md', len(c)-len(c.decode('utf-8')))"</invocation><expect>the producer file prints 0 and CLAUDE.md prints a number greater than 0 (the detector's firing control).</expect></criterion> `A2-AC10` -- ASCII, BY AN INSTRUMENT THAT CAN FIRE.

<criterion id="A2-AC11" cell_refs="AF1-s-6,AF1-s-7,AF1-s-8"><invocation>timeout 60 git diff --stat 605c03f81f HEAD -- infra/</invocation><expect>exactly one file under infra/: infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py.</expect></criterion> `A2-AC11` -- ONE FILE CHANGED UNDER INFRA.

<criterion id="A2-AC13" cell_refs="AF1-s-8"><invocation>timeout 1200 python <PRODUCER_HARNESS_A2> --cli-upload</invocation><expect>main() run with --upload under the capturing wrapper on the same model PKL the handler runs used: exactly two puts captured, json/positioning/positioning_data.json and json/positioning/opal_aggregate.json, each with ContentType application/json, ContentEncoding gzip and CacheControl no-cache, and each decompressed payload equal to the handler AFTER run's capture of the same key in every field except generated_at.</expect></criterion> `A2-AC13` -- THE SECOND WRITE SITE WRITES THE SAME TWO KEYS.

<criterion id="A2-AC12" cell_refs="AF1-s-6,AF1-s-7" judgment="true"/> `A2-AC12` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9:** whether serving `status UNAVAILABLE` on a PARTIAL weight read (a primary model missing) is the right reading of C-NO-SILENT-EMPTY, against serving the aggregate over the rows present with the missing model reported. Record the readings and offer NO verdict.

<expected_criteria>A2-AC1, A2-AC2, A2-AC3, A2-AC4, A2-AC5, A2-AC6, A2-AC7, A2-AC8, A2-AC9, A2-AC10, A2-AC11, A2-AC12, A2-AC13</expected_criteria>

<placeholders>PRODUCER_HARNESS_A2</placeholders>

<paths>
org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-A2-1.producer-reads-current-weights-and-writes-the-opal-only-key.md
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/
org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md</decomp_doc> round 1 @`605c03f81f`.
<owned_cells>AF1-s-6 AF1-s-7 AF1-s-8</owned_cells>
Read-dependencies, NOT claimed: `AF1-s-1` (the gap note), `AF1-s-2` (the censuses), `AF1-s-5` (the running bytes), `AF1-s-17` (the blend
verdicts) -- all TO-A1-1, drained before this order is handed. DOWNSTREAM: `AF1-s-10` (TO-A3-1) deploys exactly your committed bytes.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-15 ~18:3xZ) -- 7 armed gates, 0 POSN; 6 open deploy-ledger entries, 0 POSN; this order deploys nothing and serves nothing (every write captured).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy changes; the harness reads under the box credentials and its wrapper refuses every write call.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not read the recorded GeneratePositioning event of the latest execution, so its model_pkl_key and date are unknown to the issuer; (2) the producer imports `_shared` classification modules that read DynamoDB -- whether any of them WRITES during a handler run is unread, and the wrapper's abort is the instrument; (3) the CLI main() path is not exercised by any criterion; (4) the issuer corrected one parenthesis of AF1-s-6 above from a source read, not from a run.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~1/POSN_AGGFIX.TO-A2-1.producer-reads-current-weights-and-writes-the-opal-only-key.proof_of_spec.json
</proof_of_spec>
