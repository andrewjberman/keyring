# NFRA_OPLGTW task order -- `OG-et-1` -- G5 wave A: etfs_get_partner_ownership, etfs_get_ownership_rollup, etfs_get_monthly_report

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-et-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-et-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~84</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-et-1` (decomposition addendum R3-T.52, workstream FWD22-W7, FWD-22 G5)

G5 wave A ownership tools `etfs_get_partner_ownership` (firm REQUIRED), `etfs_get_ownership_rollup` (the dashboard's own totals) and `etfs_get_monthly_report` (coverage from each partner's csv, never the verdict).

Build three G5 ownership tools over `opal-data-etfs` (wave A). Module `infra/aws/ec2/opal-gateway/app/etfs_ownership.py`.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py` (OG-gt-0): `Scope(name, bucket, served_prefixes, client, max_bytes)`, `admit_scope(scope, tool, ref, *extra)` (principal present; Opal user, else `typed_opal_only`; `ref` and every
`extra` under a served prefix with no `..`; one audited refusal; call it FIRST, before any S3 call), `list_keys(scope, prefix)`, `newest_part(scope, prefix)`, `read_parquet(scope, key, columns, filters)`, `read_json(scope, key)`
(it decides gzip by the key's suffix: a `.json` object that is gzip-encoded raises; sniff the first two bytes `1f 8b` yourself over `typed_scope._load_capped` in that case), and the re-exports `envelope(body, *, as_of, source_keys, denominator,
absent_reason=None)` (projected to 50 KB; an empty body must carry an `absent_reason`), `project`, `refusal`, `audit_ok`, `TypedOverCap`. A tool module NEVER imports `get_current_principal` or holds a boto3 client at module scope.

Build your OWN scope: `Scope("etfs", <the bucket opal-data-etfs>, SERVED_PREFIXES, <app.internal_role.s3_client when it returns a client, else a lazily created boto3 S3 client inside a function>)`, where `SERVED_PREFIXES` is a MODULE CONSTANT
tuple of the exact top-level prefixes your tools read (each ending `/` or naming the one object): the release's IAM grant is generated from it by AST, so it must hold exactly what you read and nothing else.

Each tool is a TOP-LEVEL function with exactly the tool's name and inputs, returns a dict, and answers with `as_of` (the object's own as-of or its file date, never the read time), `source_keys` (the exact keys read), a `denominator`
dict (which carries `trading_days_behind_t1` from `lib/trading_calendar.py`) and `absent_reason`. An item that is absent returns an empty body with `absent_reason`, never an error.

### FIRST ACT (the naming limb stopped five G1 workers)

Before you build, stage every S3 key or prefix literal your module will hold (as a scratch `.py` file) and run `python .tools/naming-gate.py --diff <the staged diff> --enforce`. A refused literal: STOP, file ONE BLOCKING row naming it and the gate's
suggestion, report. Never split a string or override. (The gate grades the bucket literal and `s3://` URIs, not bare keys.)

### Binding reading rules (G5 census section (c), lines 112-121 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md`)

1. **Re-run parts supersede, never add.** Where a prefix keeps several parts per date, the newest part (max `revision`) is the complete snapshot; never sum parts.
2. **Three dates in one row:** the file key (run date), `data_as_of` (the issuer date, usually the day before) and `_ingested_at`. Weekend files carry Friday's data and are NOT staleness. Report all that the row carries.
3. **Units differ by layer:** weights are percentage points in Opal silver and gold/holding; say the unit in the answer.
4. **Claims are in the data** (`claim` MEASURED/INFERRED per row where present): pass them through.
5. **Never sum across firms.** A partner-firm slice is read for ONE firm per call; no tool returns a total that adds firm slices.

### The three tools (G5 section (c), lines 130-134; contracts: daily partner ownership 161-220, ownership dashboard 221-276, monthly report 277-332)

- **`etfs_get_partner_ownership(firm: str, as_of: str = None, etf_ticker: str = None)`**: how much of each Opal ETF one partner firm holds. `firm` is REQUIRED and is ONE of the partner key segments (`49financial`, `cottonwood`, `inflection`; read
  the list of partner segments from a listing of `daily/`, never typed more than once); none, an empty one, a comma list or an unknown firm is refused `harvest_bad_argument` with ZERO reads. Reads `daily/<firm>/<YYYY-MM-DD>.json` (one
  file per partner per date, 4 rows: DIVZ, IDVZ, PFDE, PFOE): with `as_of` that date's file, else the NEWEST file of that firm (the file name is the date); `etf_ticker` narrows the rows. Returns `rows` (list) and the three dates it carries.
  `daily/_archive/` is not served. The partners' latest dates differ (49financial and inflection 2026-10-13, cottonwood 2026-10-12): state each answer's own `as_of` and lag.
- **`etfs_get_ownership_rollup()`**: the platinum dashboard's OWN cross-partner totals, read from `platinum/etf_ownership_dashboard.json` (one object, `internal_only`, overwritten daily; `run_as_of` and a per-partner `as_of`). The tool SUMS
  NOTHING: it returns the object's own figures with their as-of fields (`as_of` = `run_as_of`, and the per-partner as-ofs in the body).
- **`etfs_get_monthly_report(month: str = None)`**: did the monthly report go out and was it complete. `month` is `YYYY-MM` (default: the newest folder under `platinum/reports/`; an unknown month returns an empty body with `absent_reason`;
  a malformed one is refused `harvest_bad_argument`). Reads the folder's listing and each partner's `opaletfs_<partner>_<YYYYMM>.csv` (rows = a date + one row per ETF). **Coverage comes from each partner's OWN csv, from its
  `# coverage:` comment line, NEVER from `coverage_verdict.json`** (for September the verdict says 21/21 while the CSVs say Cottonwood 20/21 and Inflection 18/21: row Z-S113, a correctness defect, not a freshness one). Returns `files` (the
  folder's object names with sizes), `coverage` = a DICT `{"<partner>": "<the text after '# coverage:', stripped>"}` taken from each csv, and the csv rows per partner (50 KB projection applies). `coverage_verdict.json` is not read at all.
  The `.pdf` and `.html` are listed, never returned.

Served prefixes of your scope (the `SERVED_PREFIXES` constant, exactly): `daily/`, `platinum/etf_ownership_dashboard.json`, `platinum/reports/`.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_et1.py` (a recording fake client; Opal stand-in principal patched at `harvest_read.get_current_principal`)

- `test_oget1_ac01`: partner ownership reads the NEWEST file of the requested firm only (the fake holds three dates for two firms), returns its 4 rows with `as_of` equal to the file date, honours `as_of` and `etf_ticker`, and never reads another firm's key.
- `test_oget1_ac02`: no firm, an empty firm, `"49financial,cottonwood"` and an unknown firm are each refused `harvest_bad_argument` with ZERO S3 calls.
- `test_oget1_ac03`: the rollup returns the dashboard object's own figures with `as_of` equal to its `run_as_of`, sums nothing (a fake with three per-partner figures: no key in the answer equals their sum unless the object carries it), and reads exactly one key.
- `test_oget1_ac04`: the monthly report's `coverage` equals each csv's own `# coverage:` line even when a fake `coverage_verdict.json` says otherwise (the verdict key is never fetched: assert it is absent from the recorded calls); an unknown month is empty with `absent_reason`; a malformed month is refused.
- `test_oget1_ac05`: a non-Opal and an absent principal are refused all three tools with ZERO S3 calls; an over-cap object is refused `harvest_over_cap`.

The live probe is the issuer's AC2. Run the same calls first, with `INTERNAL_READER_ROLE_ARN` unset. NOTE: today the box credentials read the bucket; the gateway's internal reader role does NOT yet (the release carries a grant).

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer
  registers every tool and re-pins the counts at the merge, in one commit. Do not edit them; name the registration you
  expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/etfs_ownership.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/tests/test_og_et1.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G5_etfs.md
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~84/`. Rows: id `NFRA_OPLGTW-Z-W84-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-et-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/et1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-et-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/et1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)etf ownership: partner file newest rows (\d+) vs independent \1; firm-required refusals True; rollup own as-of True; monthly coverage from each csv True, verdict not read True; non-Opal refused True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three ownership tools are built, require one firm, sum nothing, take coverage from each partner's own csv and refuse non-Opal before any read.
- `AC2`: against the real bucket the newest partner file matches an independent read, the firm-required refusals fire, the rollup's as-of sits in its object, the coverage equals each csv's own line and the verdict file is not read.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-et-1.etfs-ownership-tools.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.52; PRD v3.5 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- Decomposition addendum R3-T.52 (G5 wave A). Rides release `OG-ap-20` with the G5 never-widen ask and the read grant on `opal-data-etfs` (cell OG-et-3, cut when this cell's served prefixes exist). Today neither the gateway role nor the internal reader reads this bucket.
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).

<status>pending</status>
<round>37</round>
<workstream>FWD22-W7</workstream>
<slot>~84</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
