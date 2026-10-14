# NFRA_OPLGTW task order -- `OG-gt-1` -- `harvest_resolve_security` and `harvest_security_coverage`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~72</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-1` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

`harvest_resolve_security` and `harvest_security_coverage` (crosswalk, universe, identity; one ListObjectsV2 per keyed prefix); the CUSIP `not_held` correction.

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

### The two tools (G1 section 3, lines 54-74 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`)

Module `infra/aws/ec2/opal-gateway/app/harvest_identity.py`.

- **`harvest_resolve_security(query: str)`**. Input: a ticker, a Bloomberg ticker, a `security_key`, a company or legal name, a
  CIK, an ISIN, a SEDOL. Returns `status` one of `exact` | `candidates` | `none` | `not_held`; `security_key`; `display_ticker`;
  `bloomberg`; `name`; `cik`; `isin` where held; `other_listings[]`; `not_held[]` (the identifier kinds that were asked
  for and are not held). A nine-character CUSIP-shaped query (`^[0-9A-Z]{8}[0-9]$`) answers `status: "not_held"`
  with `not_held: ["cusip"]`, never `none`. Reads: `crosswalk/v1` newest, `universe/v1` newest,
  `bloomberg/harvest/bronze/identity/` newest per key. If `lib/research/api/name_search.resolve_query` can run over those
  parts through `harvest_typed` without a second S3 reader, wrap it; otherwise implement the match over the three datasets
  and file an OBSERVATION row naming why the library could not be wrapped. Several candidates return `candidates` (at most
  25, each with the field that matched); no match returns `none`.
- **`harvest_security_coverage(security_key: str)`**. Returns, per dataset: `dataset`, `present` (bool), `objects`, `newest`
  (the newest stamp or partition), `trading_days_behind_t1` (use `lib/trading_calendar.py` for T-1; never a calendar-day
  difference), and per layer (gold, silver, bronze, derived) totals. Reads: one `list_keys` per KEYED prefix (about 30,
  the datasets whose contract names a `security_key` path segment or a `<key>/` first segment) plus
  `packs/<key>/input_ledger.json` through `read_json`. Reading is by listing only: no object body is read except the ledger.

### Where the contracts are (read each section you need; they are the truth of columns and layout)

Contract sections in `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`: crosswalk 2102-2273; universe 4261-4416; identity 3041-3195; bloomberg bronze identity
8772-8934; packs 3419-3537; the keyed datasets' headings are listed by `grep -n "^### " <file>`.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_gt1.py` (fake client, Opal stand-in principal)

- `test_oggt1_ac01`: an exact ticker resolves `exact` with a `security_key`; a company-name fragment returns `candidates`
  capped at 25; a query matching nothing returns `none`.
- `test_oggt1_ac02`: a CUSIP-shaped query returns `not_held` with `not_held == ["cusip"]` and the envelope's `absent_reason`
  set; an ISIN held for the fixture name is returned in `isin`.
- `test_oggt1_ac03`: coverage lists every keyed dataset of the fixture with `present`, `objects`, `newest` and
  `trading_days_behind_t1` an integer or `None` with `absent_reason`; the packs ledger is read once.
- `test_oggt1_ac04`: a non-Opal principal is refused both tools with zero S3 calls; both tools write exactly one audit
  record per call.

The live probe is the issuer's AC2. Run `harvest_resolve_security("ASML")`, a CUSIP-shaped query and the coverage of ASML's
key yourself first, as `cd infra/aws/ec2/opal-gateway && python -c ...` with `INTERNAL_READER_ROLE_ARN` unset.

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
infra/aws/ec2/opal-gateway/app/harvest_identity.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/tests/test_og_gt1.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.0_BRIEF_20261014.md
lib/research/api/name_search.py
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~72/`. Rows: id `NFRA_OPLGTW-Z-W72-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)resolve ASML: status exact, security_key set; CUSIP query: status not_held; coverage datasets [1-9]\d*, rows well-formed True; packs present (True|False) vs independent head \1; envelope on all three True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both tools are built and answer a CUSIP query `not_held`.
- `AC2`: against the real bucket: ASML resolves exactly, a CUSIP answers `not_held`, and the coverage rows agree with an independent `head_object` on the packs ledger.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-1.identity-tools.proof_of_spec.json`. Validate it after your last commit with
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
<slot>~72</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
