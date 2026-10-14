# MDPF_CANON task order -- `CN-m-1` -- THE READER CENSUS OF THE STAGED GLOBAL AGGREGATE (row D1-W16-S5; FWD-3 / FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~20</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell reads schedules and writes a record.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell adds no AWS call to any deployed code; the worker's own reads are get/describe/simulate on named resources.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r7_cn_m_1.py record 0 of 1 (no record at base), verify 1 of 5 (V1 key-exists is a control), selftest 6 of 6; a scratch reference record reads record 7 of 7 and verify 5 of 5 (the arms can pass).
EGRESS CLASS, declared: NONE (the worker writes no AWS; every AWS call is a read).
</preflight>

## 1. THE CELL -- `CN-m-1` (round 7, decomposition v7)

**What is asked.** One object is written every day by the gold consolidator and read by nobody the project has named:
`s3://opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json` (below, **the staged key**). It is the Global time series before the tax and SMA overlays and
before the min-firms fold, so it is UNFOLDED: it can still carry model lines held by a single firm. Find every reader of it and write the census as ONE record. You write no
product code and change no AWS resource.

A **reader** is anything that can fetch the staged key's bytes: a script or lambda whose code reads it (by its literal key, or by a template such as
`gold/mdpf_revamp/{scope}/aggregate_aua_timeseries.json` or a prefix plus the file name, where `global` is among the scopes it reads); a schedule or trigger that runs such a
reader; and an IAM role whose granted `s3:GetObject` (or `s3:*`) covers the key. A WRITER of the key is not a reader; list it as an excluded file with the reason
`PRODUCER-WRITE-ONLY`.

### Step 1 -- the five classes, each with its own instrument and its own denominator

Run every command from the repository root of your worktree. Every AWS command is a read.

1. **`code`** -- consumers in the repository. Run `python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_m_1.py universe`: it prints, as JSON,
   the denominator (`scanned` files under `data/`, `infra/`, `lib/`, `.tools/` with a code or config suffix) and the files that name BOTH `gold/mdpf_revamp` and
   `aggregate_aua_timeseries`. Read each listed file (use `comp-read <file> --for "does it read the global staged aggregate key, and what does it do with the bytes?"`, or the Read
   tool) and place it in exactly one of two lists: `readers` (it reads the staged key; `kind` is `reads`) or `excluded` (give `path` and one `reason` from `PRODUCER-WRITE-ONLY`,
   `TEST`, `DECLARATIVE-ONLY`, `COMMENT-ONLY`, `OTHER-KEY`, `SELF`). `comp-pipescript io <script>` helps for the gold scripts but reports a dynamic prefix as UNRESOLVED-PREFIX
   and cannot name the key: when it does, read the code. `evidence` is `path:line` of the line that reads the key. For each reader write where its bytes go (`output_key`) and
   its `surface` (section 2). The `denominator` is `{"scanned": <the universe's scanned>, "unit": "files"}`.
2. **`scheduled`** -- what runs a code reader on a clock. For each reader in `code`, find its trigger (`infra/aws/lambda/ci/trigger-map.json`, `infra/aws/terraform/**` schedules,
   the daily dispatch `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`). For each EventBridge Scheduler schedule you name, read its live state with
   `.tools/aws scheduler get-schedule --name <name> --output json` and record `State` and the cron expression as `state` and `expression`; for an EventBridge rule use
   `.tools/aws events describe-rule --name <name> --output json`. A reader with no schedule is not an entry. The `denominator` is `{"scanned": <number of triggers or schedules you examined>, "unit": "triggers"}`; `count` is the number of `readers` entries (a trigger that runs a code reader).
3. **`iam_static`** -- roles whose Terraform grant covers the key. Read the grants in `infra/aws/terraform/` (use the Grep tool with `path` set to your worktree's
   `infra/aws/terraform`): a statement counts when its actions include `s3:GetObject` or `s3:*` and a Resource pattern matches
   `arn:aws:s3:::opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json` by wildcard (`gold/mdpf_revamp/*`, `gold/mdpf_revamp/global/*`, `opal-data-assets/*`,
   `*`). One entry per ROLE with `evidence` `file:line` of the Resource that matches. The `denominator` is `{"scanned": <number of .tf files you read>, "unit": "tf files"}`.
4. **`iam_live`** -- what AWS decides today. For each role in `iam_static` plus these three, run
   `comp-iam simulate <role> s3:GetObject arn:aws:s3:::opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json --no-control`: `mdpf-daily-runner-ec2-role`,
   `mdpf-gold-lambda-role`, `opal-assets-mdpf-egress-publisher-role`. Record the printed `STATE` of each as `ALLOWED`, `DENIED` or `NOT-DECIDABLE` (a conditioned statement
   evaluated without context prints NOT-DECIDABLE; that is NOT a deny, record it as is and do not retry with invented context). Write `principals_checked` and
   `states` (counts that sum to `principals_checked`), and list each role and its state in `per_principal`. The `denominator` is `{"scanned": <roles simulated>, "unit": "roles"}`.
5. **`trail`** -- can the world tell you who read it? Run `.tools/aws cloudtrail describe-trails --output json`, then for each trail
   `.tools/aws cloudtrail get-event-selectors --trail-name <name> --output json`, and `.tools/aws s3api get-bucket-logging --bucket opal-data-assets --output json`.
   `covered` is true only if some data-event selector covers `arn:aws:s3:::opal-data-assets/` objects for reads. `server_access_logging` is true only if the logging call
   returns a `LoggingEnabled` block (an empty object means none). `trails` lists the trail names read, `evidence` quotes the deciding selector lines. Where `covered` is false
   the record SAYS that no read evidence exists for this bucket; the absence of read events there is NOT a count of zero readers. The `denominator` is
   `{"scanned": <trails read>, "unit": "trails"}`.

### Step 2 -- the record

Write `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~20/CN-m-1_READER_CENSUS.json` (ASCII only), and beside it `CN-m-1_READER_CENSUS.md`: one page in
plain English, a table per class, then the partner-facing readers and what each writes where. The JSON has this shape (fields not listed are allowed):

```
{ "key": "s3://opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json",
  "census_at": "<date -u +%FT%TZ>", "head": {"etag": "...", "last_modified": "...", "content_length": 0},
  "verdict": "READERS-FOUND" | "ZERO-READERS-PROVEN" | "ZERO-STATIC-READERS-RUNTIME-UNOBSERVED",
  "total_readers": <readers in code + scheduled + iam_static>, "zero_readers": <total_readers == 0>,
  "partner_facing": [<ids of readers whose surface starts PARTNER-FACING>],
  "classes": {
    "code":       {"denominator": {"scanned": N, "unit": "files"}, "count": n, "readers": [R, ...], "excluded": [{"path": "...", "reason": "..."}, ...]},
    "scheduled":  {"denominator": {"scanned": N, "unit": "triggers"}, "count": n, "readers": [S, ...]},
    "iam_static": {"denominator": {"scanned": N, "unit": "tf files"}, "count": n, "readers": [R, ...]},
    "iam_live":   {"denominator": {"scanned": N, "unit": "roles"}, "principals_checked": N, "states": {"ALLOWED": a, "DENIED": d, "NOT-DECIDABLE": u}, "per_principal": [...]},
    "trail":      {"denominator": {"scanned": N, "unit": "trails"}, "covered": bool, "server_access_logging": bool, "trails": [...], "evidence": ["...", ...]} } }
R = {"id": "<the path or role name>", "evidence": "<path:line>", "kind": "reads", "surface": "<section 2>", "output_key": "<key or prefix, or null>"}
S = {"id": "<schedule name>", "evidence": "<name>", "state": "<live State>", "expression": "<cron>", "runs": "<the reader id it runs>", "surface": "<section 2>", "output_key": ...}
```

Verdict rule: `READERS-FOUND` when `total_readers` is above 0. At 0, `ZERO-READERS-PROVEN` only if `trail.covered` is true; otherwise
`ZERO-STATIC-READERS-RUNTIME-UNOBSERVED`. A zero is recorded as `count: 0` with its denominator, never left out.

## 2. THE SURFACE OF A READER (what you classify; one value per reader)

- `NONE` -- its output stays in a log, a test or memory.
- `INTERNAL` -- its output is another internal producer's input or a staging key under `gold/` that no page fetches.
- `PARTNER-FACING-CANDIDATE` -- it writes a key under the `portal/` prefix of `opal-data-assets` (the prefix a partner firm or client page is served from) and you have NOT shown that
  the staged bytes themselves land there. Name the `output_key` (a template with `<as_of>` or `{scope}` is fine) and state in the .md what stops or allows the staged bytes
  from landing (for example a refuse-to-overwrite rule and which job writes first).
- `PARTNER-FACING` -- you HAVE shown that the staged bytes land under `portal/`: two reads, one of the served object and one of the staged key, with their sizes or hashes
  printed side by side in the .md (read-only `get-object`/`head-object`; no write).

You judge reach; you do not decide what to do about it. A reader that reaches `portal/` is named; its re-pointing is a different order.

## 3. BOUNDS

1. **No AWS write of any kind**: no `s3 cp`/`put`/`rm`, no invoke, no apply, no deploy, no `start`/`enable`/`disable` of any schedule, no IAM change. Only `get`, `list`,
   `describe`, `head` and `comp-iam simulate`. No install, no push. REFUSE, do not rescue.
2. You write only the files in section 4. You change no product file, no Terraform file, no script. A reader you find is recorded, never edited.
3. **Never** put an account id, a client level or a dollar figure from a served object into the record. Sizes, hashes, dates, keys and role names only.
4. No non-ASCII anywhere in the JSON or the .md. Use the Edit and Write tools. Keep each file's line endings as you find them (read them first).
5. The check cross-examines your record against the repository and against live AWS using a list of readers you are NOT shown; a record that missed a reader fails and
   is yours to extend. Do not trim the census to make it pass.
6. If an instrument will not run (a missing role, an AccessDenied, a timeout), record the call, its exit code and its output in the .md and set that class's entries to what
   you could read; file a surprise row naming the call. Never guess a state.

## 4. SURFACES

<paths>
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-m-1.staged-global-aggregate-reader-census.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~20/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/`, `infra/aws/terraform/`, `infra/aws/lambda/`, `infra/aws/ec2/mdpf-daily-runner/` and the issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_m_1.py` (never edit it; its `universe` mode is your denominator and its `record` mode shows the
field rules).

## 5. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-m-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_m_1.py" record; echo "exit=$?"</invocation><expect>CN-M-1 RECORD: 7 of 7 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-m-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round7/checks/r7_cn_m_1.py" verify; echo "exit=$?"</invocation><expect>CN-M-1 VERIFY: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-m-1" judgment="true"/>
</proof_of_spec>

AC3 is JUDGMENT, graded at the round-7 close (never self-graded): is each reader's `surface` right, and does a PARTNER-FACING-CANDIDATE or PARTNER-FACING reader's
`output_key` and the stated reason (what allows or stops the staged bytes landing under `portal/`) stand on the evidence the .md prints?

## 6. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~20/MDPF_CANON.TO-CN-m-1.staged-global-aggregate-reader-census.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for), with AC3 UNVERIFIABLE-BY-INSTRUMENT and status_reason "graded at the round-7 close".
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your paths), and only when AC1 and AC2 pass.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W20-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the record's `verdict`, `total_readers`, the partner-facing list, the five denominators, the output line of AC1 and AC2, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 7, issuer 2.0.0_SA_COO~D1, on the CTO's round-6 analysis @65bf603a7a section 3 item 2: "the unfolded staged copy has unidentified readers. Cell: a READER CENSUS of
the staged key: comp-pipescript consumers, the IAM grants on the prefix, and the S3 GetObject data events if the trail covers that bucket. The denominator is printed. Any reader that
reaches a partner-facing surface is re-pointed to the folded object under a pair. A census of zero readers is recorded, and the row disarms on it." Row D1-W16-S5 (INVESTIGATION_v1.md,
surfaced 2026-10-12T18:40:21Z, ARMED, disarm_owner `2.0.0_SA_COO~D1`).

**THE ISSUER'S PRE-READ (2026-10-14 ~14:0xZ, a fork of the issuer; NOT the worker's result, not a count the order may cite; the worker is not shown it).**
- Staged key now: 512,084 bytes, LastModified 2026-10-14T13:31:35Z, ETag 1113c3c080c4acb0c38d800610ade827 (the fold's first scheduled fire). The dated served object for the same
  as-of, `portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-13.json`, is 646,107 bytes, LastModified 13:31:48Z (written by the gold lambda).
- **Code class, universe 28 of 8,831 files** (files naming both `gold/mdpf_revamp` and `aggregate_aua_timeseries`). Readers identified so far: `data/mdpf/scripts/gold/dim_mdpf_non_model_assets.py`
  (:102-104, the stage-6c reader of the global and inflection staged aggregates), `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py` (:54 `AGG_GLOBAL_KEY`, :73 and :178-180 the firm keys),
  `data/mdpf/scripts/gold/verify_mdpf_revamp_conditions.py` (:34, a verifier), and **`data/mdpf/scripts/gold/build_portal_gold_accrual.py`** (`SOURCE_PREFIX = gold/mdpf_revamp`, type
  `aggregate_aua_timeseries` over every scope including `global`; it writes `portal/gold/mdpf/{scope}/aggregate-aua-timeseries/<as_of>.json`, never overwriting an existing dated key). The
  consolidator (:2838 writes the key; :2968 reads cottonwood files), `stage_mdpf_revamp_trio.py` and `build_mdpf_spine.py` are writers or other-key readers; the pre-read did not
  classify the remaining files. These four are the `ANCHORS` in the check (V2).
- **Scheduled class:** `mdpf-accrual-bridge-daily` (EventBridge Scheduler, `cron(40 13 * * ? *)`, State ENABLED, target lambda `mdpf-accrual-trigger`, which runs the accrual script over SSM
  on the runner). The dispatch's stage 6 (runs `dim_mdpf_non_model_assets.py` as 6c) is a second, whose liveness is the project's own finding (stage 6 reported dead since 2026-08-14).
  Timing: the lambda writes the dated served key about 13:31Z, the accrual fires at 13:40Z, so the accrual's never-overwrite rule is what stops the unfolded bytes landing under
  `portal/` when both name the same as-of; whether the as-of dates always coincide is the worker's evidence to print. This is the one reader the pre-read expects to class
  PARTNER-FACING-CANDIDATE.
- **IAM:** Terraform grants over `gold/mdpf_revamp/*`: `mdpf-daily-runner-ec2-role` (`infra/aws/terraform/mdpf-pipeline/iam.tf` about :428, :455, :482), `mdpf-gold-lambda-role` (about :883, :963),
  and the publisher and egress-publisher roles (`infra/aws/terraform/opal-assets/mdpf_portal_publisher.tf:38` `mdpf_publisher_read_prefix = "gold/mdpf_revamp/*"`, `mdpf_egress_publisher.tf`). Live
  `comp-iam simulate ... s3:GetObject <staged key>`: runner role ALLOWED, gold-lambda role ALLOWED, egress-publisher role NOT-DECIDABLE (conditioned on `s3:prefix`, missing context). The graph holds no policy text
  (a `comp-find --corpus aws 'opal-data-assets' IAM_ROLE` returns 0 over 297 nodes), so the IAM class is Terraform plus simulation, with its limits stated.
- **Trail class:** NOT COVERED. `opal-organization-trail` data selectors cover `opal-data-49financial`, `-bd`, `-cot`, `-inf` only; `opal-served-key-write-trail` covers only `opal-data-inf|bd|cot/platinum/firm/`
  writes; `get-bucket-logging` for `opal-data-assets` returns an empty object (no server access logging). So no GetObject evidence exists for this bucket and a zero static count
  could not be PROVEN a zero; the verdict at zero would be ZERO-STATIC-READERS-RUNTIME-UNOBSERVED. Enabling data events or access logging is a billed infrastructure change and is NOT in this cell
  (the standing moratorium on new monitors; propose it only if Andrew asks).
- **Expected shape of the record:** READERS-FOUND, at least four code readers, one scheduled reader, at least three IAM roles, one PARTNER-FACING-CANDIDATE (the accrual). If the worker reads fewer than
  the anchors, V2 refuses the record and the fault is the record's.

**Why a worker, and why LOCAL.** The census is read-only over code, Terraform and AWS, and its only artifact is a record under the worker's deliverables folder, so the paths imply risk class LOCAL
(no product file, no `infra/` file, no served object). It is not cut on the DIRECT-ACT path: it carries a judgment criterion (AC3) that the CVO grades, and the CTO named it a cell. Because the
pre-read already covers most of the substance, the issuer MAY instead record the census itself (as the W8-S4 served-key read was); the check, the record schema and the decomposition row are the same either way.
`worker` class, not `worker-light`: five instruments and a reachability judgment. One cell, one chain, slot ~20, base box/dell1.

**Not in this cell:** re-pointing any reader (a later cell under a never-widen pair, cut only if the census finds a PARTNER-FACING or PARTNER-FACING-CANDIDATE reader and the CTO rules it a re-point);
moving the staging write behind the fold guard; retiring the staged key; enabling any trail or access log.

<status>pending</status>
<round>7</round>
<to_id>MDPF_CANON.TO-CN-m-1</to_id>
<slot>~20</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
