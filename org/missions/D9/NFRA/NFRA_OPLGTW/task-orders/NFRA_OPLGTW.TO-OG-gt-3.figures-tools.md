# NFRA_OPLGTW task order -- `OG-gt-3` -- `harvest_get_fundamentals` and `harvest_query_columns`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~74</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-3` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

`harvest_get_fundamentals` and `harvest_query_columns` (model_block, bestdata, refdata, histdata, segments, price; the tabular allow-list).

### The base you build on (cell OG-gt-0, ALREADY ON YOUR HEAD): `app/harvest_typed.py`, exactly this surface

- `admit_typed(tool, ref, *extra) -> Optional[dict]`: the refusal dict, else `None`. It wraps `harvest_read.admit` (principal
  present, Opal user, served prefix; one audited refusal). Call it FIRST, before any S3 call.
- `audit_ok(tool, ref, nbytes) -> None`: the one audit row of a served call.
- `refusal(message, code) -> dict`: `{"error", "code", "guard_denied": True}`.
- `envelope(body, *, as_of, source_keys, denominator, absent_reason=None) -> dict`: returns
  `{"as_of", "source_keys", "denominator", "absent_reason", **body}`, projected to 50 KB.
- `project(out, limit=51200) -> dict`: when the JSON size exceeds `limit`, pops items off the end of the largest list
  field until it fits, sets `"truncated": True` and `"projected_to_bytes"`.
- `list_keys(prefix) -> list[{"key", "size", "last_modified"}]`: every page, no Delimiter, auto-paginated.
- `newest_part(prefix) -> Optional[str]`: for a prefix laid out `<prefix>date=YYYY-MM-DD/part-<stamp>.parquet`, the key
  with the greatest `(date partition, part file name)`; `None` when there is no `.parquet`.
- `read_parquet(key, columns=None, filters=None) -> (rows, total_rows, nbytes)`: columns projected at read; `filters` is
  a list of `(column, op, value)` with op in `=`, `<`, `>`, `in` (a string value is coerced to the column's date type).
- `read_json(key) -> (obj, nbytes)`: `.json` and `.json.gz`, capped.
- `TYPED_MAX_BYTES` (64 MiB): the cap on one object read; over it, `harvest_over_cap`.

**Rules of the seam.** A tool module NEVER imports `get_current_principal` or boto3: it reaches S3 and the principal only
through `harvest_typed`, so one probe patch point (`app.harvest_read.get_current_principal`) governs every tool. Each tool
is a TOP-LEVEL function in your module with exactly the tool's name and the inputs below, returns a dict, and every success
carries `as_of`, `source_keys`, `denominator` and `absent_reason` through `envelope(...)`. A key you were asked about that is
absent returns an empty body with `absent_reason` set (a string naming WHY), never an error and never silence.

### Two corrections from the CRO's L4-R review (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.0_BRIEF_20261014.md` section "Corrections"), binding on this cell

1. `chatter_daily`, `article_security_mention` and `chatter_window` are read from the NEWEST part file of the newest date
   partition ONLY (`newest_part`). Every part is a full snapshot: the newest chatter_daily part holds 68,002 rows against
   1,338,296 across all parts; the newest mention part 52,424 against 459,334. Reading the prefix multiplies counts about 9x
   and 20x with no error. This is the one guard whose absence returns a plausible wrong number.
2. `harvest_get_chatter` returns `data_status` for every day and never presents 0 articles as "no chatter" (on the newest
   day 174 of 242 names read DENIED and 68 PARTIAL). `harvest_resolve_security` answers a CUSIP query `not_held`, never
   `none` (CUSIP is held in 0 of 18 Parquet tables; ISIN only for 65 names).

### The two tools (G1 section 3, lines 130-145 and 195-212 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`)

Module `infra/aws/ec2/opal-gateway/app/harvest_figures.py`.

- **`harvest_get_fundamentals(security_key: str, kind: str, mnemonics: list = None, fiscal_years: list = None)`**. `kind` is one of
  `model | consensus | reference | valuation_history | segments | price` (else `harvest_bad_argument`). Returns, by kind:
  `model`: figures (mnemonic, fiscal_year, value, unit, vintage, source) and cases, with `model_block` versions; `consensus`:
  the `BEST_*` fields for FY1-FY3 from bestdata; `reference`: refdata fields; `valuation_history`: histdata rows; `segments`;
  `price`: the price series (`price_history_px_last`, newest date). Reads: `derived/model_block` and `derived/model_block_fye`
  newest per key; `bloomberg/harvest/bronze/` bestdata, refdata, histdata, segments newest per key; price_history newest
  date. `mnemonics` and `fiscal_years` filter the rows. These are Bloomberg bronze tables read FROM THE BUCKET ONLY: no tool
  here, and nothing you write, calls Bloomberg.
- **`harvest_query_columns(dataset, columns, security_keys=None, filters=None, order_by=None, limit=50)`**. Tabular datasets
  ONLY, from this allow-list: `chatter_daily`, `chatter_window`, `article_security_mention`, `article_sentiment`,
  `candidate_universe`, `model_block` (figures), `bestdata`. Anything else is refused `harvest_bad_argument` with the allow-list.
  `columns` must be declared columns of the dataset's contract (an unknown column is refused `harvest_bad_argument` naming it);
  `filters` is `[{column, op, value}]` with op in `=`, `<`, `>`, `in` (any other op refused); `order_by` is `"<column>"` or
  `"<column> desc"`; `limit` 50 default, 200 max (clamped, `limit_applied` says so). Returns projected rows (declared columns
  only) plus the denominator scanned (`{"rows_in_object": N, "rows_after_filter": M}`) and the part or object read in
  `source_keys`. The newest-part rule (correction 1) applies to chatter_daily, chatter_window and article_security_mention;
  every other dataset reads "the newest part or object of the dataset" per its contract.

### Where the contracts are (read each section you need; they are the truth of columns and layout)

In `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`: model_block 2274-2475; model_block_fye 2476-2626; bestdata 8101-8237; refdata 9231-9471; histdata 8368-8640;
histdata_daily_px 8641-8771; segments 9472-9602; price_history_px_last 8935-9080; price_history_tot_return 9081-9230;
candidate_universe 831-1021; chatter_daily 1022-1280; chatter_window 1466-1659; article_security_mention 364-640;
article_sentiment 641-830.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_gt3.py` (fake client with in-memory Parquet)

- `test_oggt3_ac01`: fundamentals `model` returns figures with mnemonic, fiscal_year, value, unit and vintage; `consensus`
  returns BEST_* for FY1-FY3; `mnemonics` and `fiscal_years` filters narrow the rows; an unknown `kind` is refused.
- `test_oggt3_ac02`: `harvest_query_columns` returns only the declared columns, orders `desc`, applies `=`, `<`, `>`, `in`
  filters, clamps `limit=500` to 200 with `limit_applied`, and prints the scanned denominator.
- `test_oggt3_ac03`: a dataset outside the allow-list, an unknown column and an op of `like` are each refused
  `harvest_bad_argument` with ZERO S3 calls.
- `test_oggt3_ac04`: `chatter_daily` through `harvest_query_columns` reads the newest part of the newest partition only
  (the fake holds an older part with different values; the result equals the newest part).
- `test_oggt3_ac05`: a non-Opal principal is refused both tools with zero S3 calls; one audit record per call.

The live probe is the issuer's AC2: the 20 highest `articles_total` of the newest chatter_daily day must equal an independent
read of the same part; fundamentals for ASML `consensus` returns BEST_* rows. Run both yourself first, with
`INTERNAL_READER_ROLE_ARN` unset.

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
infra/aws/ec2/opal-gateway/app/harvest_figures.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/tests/test_og_gt3.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.0_BRIEF_20261014.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~74/`. Rows: id `NFRA_OPLGTW-Z-W74-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)query top-20 on \d{4}-\d{2}-\d{2}: tool True vs independent equal; unknown column refused True; limit 500 clamped to 200; consensus rows for ASML [1-9]\d*; source key is the newest part True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both tools are built, the allow-list and column refusals fire before any S3 call, and chatter reads the newest part only.
- `AC2`: against the real bucket: the top-20 equals an independent read of the same part, bad arguments are refused, and consensus returns rows.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-3.figures-tools.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- The release this cell rides: `NFRA_OPLGTW.TO-OG-ap-18`; its grant is `NFRA_OPLGTW.TO-OG-hv-2` (A5).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).
- Queue: staged until OG-gt-0 merges; the spawn is the GO.

<status>staged</status>
<round>37</round>
<workstream>G1-TYPED</workstream>
<slot>~74</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
