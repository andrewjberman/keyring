# NFRA_OPLGTW task order -- `OG-cc-1` -- the 13-month closure census: which silver dates have no qualified completion record (PRD v2.0 item 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~41</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE the reads run under the operator's IAM user: list and GET of s3://opal-data-assets/schwab/{08242234,08335338}/meta/complete/ (completion records) and delimiter listings of the four served silver prefixes; no role or policy is read for a decision or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is round-31 analysis items 4-5 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round31.md @e43ee663be) and PRD v2.0 item 4 (@e43ee663be, signed @5924aaedbe).
EGRESS CLASS, declared: NONE beyond Opal's own S3.
</preflight>

## 1. THE CELL -- `OG-cc-1` (decomposition addendum R3-T.30, round 32 items 5 and 4's marker clause)

The gateway serves a date only when that master's completion record for it QUALIFIES (PRD C3). Master 08335338 holds 27
records, 2026-08-31 to 2026-10-07 (read 2026-10-08), so most of a 13-month window has silver partitions but no
qualified record. This cell sizes that gap exactly, per master. It changes nothing; `OG-bf-1` (your next order) fills it.

**"Qualified" is the gateway's own record-level rule, imported, never re-implemented.** From the repo root, with
`infra/aws/ec2/opal-gateway` on `sys.path`: `from app.integrations.schwab import catalog as cat`;
`contract = cat.parse_contract(<json of org/standards/NFRA_OPLGTW_CONTRACT.json>)`. A record at
`schwab/<m>/meta/complete/date=<D>.json` is:
- `LEGACY` when it carries no `closure` object;
- `QUALIFIED` when `cat.membership_findings(marker, closure, m, D, contract)` holds no finding whose class is one of
  `cat.F_REJECTED_BUCKET`, `F_REJECTED_MASTER`, `F_REJECTED_DATASET`, `F_REJECTED_DATE`, `F_REJECTED_KEY`, and
  `cat.validate_closure(closure, contract.masters)["status"] == cat.RESULT_QUALIFIED`;
- `NONQUALIFYING` otherwise.
Object heads are NOT re-checked here (the gateway also HEADs each object at serve time); say so in the record.

Do, per master `08242234` and `08335338`:
1. Class every completion record (paginate the listing). `oldest_qualified` and `newest_qualified` are the first and
   last QUALIFIED dates overall (this is round 32 item 4's marker clause).
2. The window: `to` = `newest_qualified`; `from` = the same calendar day 13 months earlier, clamped to that month's
   last day (2026-10-07 gives 2025-09-07; 2026-03-31 would give 2025-02-28).
3. Silver dates in the window: the union of `date=YYYY-MM-DD/` partitions of `dim_position`, `dim_balance`,
   `dim_asset` and `dim_transaction` under `schwab/<m>/silver/` (delimiter listings), with the per-dataset counts.
4. `missing`: every silver date in the window whose record is not QUALIFIED (absent, LEGACY or NONQUALIFYING), sorted.
5. Write `W/closure_census_record.json`:
   `{"qualification": "record-level: catalog.membership_findings + catalog.validate_closure; object heads NOT re-checked",
     "measured_utc": "...",
     "masters": {"<m>": {"window": {"from": "...", "to": "..."}, "silver_dates": <int>,
                        "silver_dates_by_dataset": {"dim_position": <int>, ...}, "markers_total": <int>,
                        "markers_in_window": {"qualified": <int>, "legacy": <int>, "nonqualifying": <int>},
                        "oldest_qualified": "...", "newest_qualified": "...", "missing_count": <int>,
                        "missing": [...]}}}`
   and `W/closure_census.result.md`: per master the window, the counts, the missing dates as ranges, the NONQUALIFYING
   records with their finding classes, and the dates where datasets disagree (a date in one served dataset and not
   another).

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~41/`.

## 2. BOUNDS

- Read only. No write, copy or delete anywhere in S3. Only the two masters' prefixes; no other firm's data.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~41/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W41-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/cc1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)08242234: window .*08335338: window .*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the issuer's reader recomputes every count, both qualified bounds and the exact missing list from live S3 with
  the gateway's own code, and your record equals it.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cc-1.closure-census-13m.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: the literal AC output; per master the window, the counts and the missing ranges; commits and rows.
   Your next order (`OG-bf-1`) reads your record; you will be handed it by continuation.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), item 5 plus item 4's marker clause; chain `OG-cc-1` -> `OG-bf-1` (section 4a item 8b) in slot ~41.
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>32</round>
<slot>~41</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
