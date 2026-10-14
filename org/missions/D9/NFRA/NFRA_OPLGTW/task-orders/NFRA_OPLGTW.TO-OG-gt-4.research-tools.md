# NFRA_OPLGTW task order -- `OG-gt-4` -- `harvest_get_research`, `harvest_get_filing_analysis`, `harvest_get_peers_and_scores`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-4</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-4</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~75</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-4` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

`harvest_get_research`, `harvest_get_filing_analysis`, `harvest_get_peers_and_scores`.

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

### The three tools (G1 section 3, lines 146-183 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`)

Module `infra/aws/ec2/opal-gateway/app/harvest_research.py`.

- **`harvest_get_research(security_key: str, as_of: str = None, fields: list = None)`**. Returns dossier fields (each a value
  with its citation, or an absent reason); the continuation thesis and pillars; `ai_fill` blocks; the research-report list
  (class, period, fund, author); the management roster. Reads: gold `research_dossier` (underscore; the newest `as_of`),
  `research-continuation`, `ai_fill`; silver `amgt/harvest/silver/research-report/`; `management/v1`; bloomberg bronze
  `exec_officers`. The hyphen `amgt/harvest/gold/research-dossier/` is read ONLY to confirm that `research_dossier` supersedes
  it (G1 marks that inferred): file one OBSERVATION row stating what you measured (the newest stamp of each, and whether
  the underscore table carries every field the hyphen one does); the tool serves the underscore table.
- **`harvest_get_filing_analysis(security_key: str, accession: str = None, include_passages: bool = False)`**. Returns form,
  filing_date, items by category (guidance, segments, risks, commentary, big_bets, big_challenges) with citations;
  denominators; drafted sections; passages only on request. Reads: `filings/v1` (`.analysis` and `.source`), `drafting/v1`,
  `sec/harvest/silver/filing_source/`. With no `accession` the newest filing; an unknown accession returns an empty body
  with `absent_reason`.
- **`harvest_get_peers_and_scores(security_key: str)`**. Returns peer members (name, ticker, country, sector, cap, factors,
  rung); scores (divergence, peers_v, robustness with status and reason); posture (verdict, books, weight_by_book). Reads:
  `peers/v1` newest, `scores/v1`, `posture/v1` newest.

### Where the contracts are (read each section you need; they are the truth of columns and layout)

In `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md`: research_dossier 1949-2101; research-dossier (hyphen) 1802-1948; research-continuation 1660-1801; ai_fill
218-363; silver research-report 4417-4660; management 3196-3418; exec_officers 8238-8367; filings 2819-3040; drafting 2627-2818;
sec filing_source 6737-6974; peers 3538-3755; scores 4110-4260; posture 3756-3973.

**Ruling A1 (issuer, on your row: the naming limb).** The commit-time naming gate (LGIC_ENFORCE; `.tools/naming-gate.py`) REFUSES a NEW out-of-pattern S3 literal and has no override for it. Four live prefixes are spelled with hyphens (`research-continuation`, `research-dossier`, `research-report`, `research-report-extract`); their canonical underscore spellings hold 0 objects, and AMGT_HARVST owns any rename (R19). So: write ONLY the canonical underscore spelling of a prefix in the module (the gate grades it CONFORMANT), and resolve the LIVE spelling at run time with one helper `_live_prefix(canonical)`: list the canonical prefix through `harvest_typed.list_keys`; if it holds no key, list the same prefix with the underscores of its LAST path segment written as hyphens (built with `str.replace`, never typed) and use that if it holds keys; else the dataset is absent (`absent_reason`). Put the prefix actually read in `source_keys`. NEVER type a hyphenated S3 literal, split a string to get past the gate, or override it. The module is then tolerant of the rename. Tests: a fake holding only the hyphen spelling resolves to it; a fake holding both prefers the canonical; one holding neither is absent. Also (your rows S3 and S5): `research_dossier` holds duplicate objects per (key, as_of) and `filing_source` repeats an accession across partitions: keep the NEWEST object per (key, as_of) and per accession, and say how many duplicates were dropped in the denominator. Your rows S1 and S2 (the base's projection nulls a dict-carried body over 50 KB; over-cap reads write no audit row) are accepted as known limits of the base: `truncated` already says so; they go to the enrichment list, not this cell. Your row S4 (the underscore dossier carries all 22 hyphen field names for ASML) CONFIRMS the supersession; the tool serves the underscore table only.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_gt4.py` (fake client)

- `test_oggt4_ac01`: research returns dossier fields with citations, the continuation, ai_fill and the roster; `fields`
  narrows the dossier; an `as_of` picks that stamp; the hyphen table is never read by the tool (zero keys under it).
- `test_oggt4_ac02`: filing analysis returns the six categories with citations; `include_passages` false omits passages;
  an unknown accession returns an empty body with `absent_reason`.
- `test_oggt4_ac03`: peers and scores returns members, the three score kinds with status and reason, and the posture with
  `weight_by_book`; a key with no posture returns that part empty with `absent_reason` naming it, other parts intact.
- `test_oggt4_ac04`: a non-Opal principal is refused all three tools with zero S3 calls; one audit record per call.

The live probe is the issuer's AC2, on ASML: at least two of the three tools return a non-empty body and every empty one
names why. Run all three yourself first, with `INTERNAL_READER_ROLE_ARN` unset.

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
infra/aws/ec2/opal-gateway/app/harvest_research.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/tests/test_og_gt4.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/L4R_REVIEW_NFRA_OPLGTW_v3.0_BRIEF_20261014.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~75/`. Rows: id `NFRA_OPLGTW-Z-W75-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt4.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ASML: research \w+, filing analysis \w+, peers/scores \w+; non-empty [23] of 3 \(want >= 2\); every empty one names why True; envelope on all three True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three tools are built, refuse non-Opal, and never read the superseded hyphen table.
- `AC2`: against the real bucket: ASML returns bodies for at least two of the three tools and every empty answer names why.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-4.research-tools.proof_of_spec.json`. Validate it after your last commit with
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

- A1 (issuer, 2026-10-14 ~15:4xZ, workers' rows on the naming limb): hyphenated live prefixes are resolved at run time from the canonical underscore spelling; no hyphenated literal, no override. The worker is re-seated on its uncommitted module with this amendment. No criterion moves. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>G1-TYPED</workstream>
<slot>~75</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
