# NFRA_MCPINDEX task order -- `MX-q-2` -- ROUND 2, E5: two read-only live reads (Black Diamond null cusips; Eclipse tenancy)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-q-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~4</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two one-shot reads; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only reads under the operator's existing AWS access, through the .tools/aws shim; no grant is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a measurement cell.
EGRESS CLASS, declared: Opal's own AWS only (S3 / Athena reads).
</preflight>

## 1. THE CELL -- `MX-q-2` (round 2, decomposition section R2.1)

Two rulings of the CTO's round-1 analysis (`org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round1.md` R-2 (1)
and R-3, READ THEM) each need one read before any tool over that data is cut. Both are READ-ONLY.

1. **Black Diamond (row C-S13).**
   - Background: `opal-data-bd` `silver/bd_assets_dim.parquet`, the asset-to-cusip bridge, was last written
     2026-04-14T20:44:16Z, and no scheduler builds it. So an asset first seen after that date enters silver transactions
     with a null cusip.
   - Measure, over the silver transactions dated on or after 2026-04-14, the row count and the count with a null cusip.
     Find the table through the round-1 analysis `deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-blackdiamond.result.md`.
   - Measure, for every SERVED figure that joins on cusip (name each, with its producer and key), whether it carries a
     null-cusip row today.
   - Record in `deliverables/0.9.0_WK_NFRA_MCPINDEX~4/round2-reads.result.md` the two lines, with the instrument and
     denominator above each:
     - `BD-NULL-CUSIP rows=<n> null_cusip=<k> since=2026-04-14 source=<s3 prefix> read_at=<UTC>`
     - `BD-SERVED-CUSIP-JOINS served_figures_checked=<m> carrying_null=<j>`
2. **Eclipse (row C-S12).**
   - Background: the Eclipse silver converter calls `filter_to_inflection()` 0 times, so its firm scope is an unverified
     single-tenant assumption (`deliverables/0.9.0_WK_NFRA_MCPINDEX~4/analysis-eclipse.result.md`).
   - Measure the distinct firm or rep identifiers across live Eclipse silver rows, and how many fall outside the
     Inflection allowlist the Orion tables use (find it through `_orion_api_silver_lib.py`'s `filter_to_inflection`).
   - Record the line `ECLIPSE-SCOPE rows=<n> distinct_ids=<d> outside_allowlist=<k> allowlist=<repo path> read_at=<UTC>`.

Aggregate counts only: no client name, account number or balance enters the file.

## 2. BOUNDS

1. READ ONLY. No write to any bucket, table or pipeline. Scheduling the BD builder and adding the Eclipse filter are DS
   acts, PARKED by the rulings (R-2 (2), R-3) and not yours.
2. Every read terminates (`timeout 120`, or the tool's own budget), and states its vintage.
3. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~4/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_MCPINDEX-Z-W4-S<k>`, fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-q-2"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/q2.AC1.sh; echo "exit=$?"</invocation><expect>BD read: rows>0 null_cusip<=rows since=2026-04-14 read_at present=1; served figures checked>=1 carrying null<=checked -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-q-2"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/q2.AC2.sh; echo "exit=$?"</invocation><expect>Eclipse read: rows>0 distinct_ids>=1 outside_allowlist<=distinct_ids allowlist at HEAD=yes read_at present=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~4/NFRA_MCPINDEX.TO-MX-q-2.two-reads.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once:
- both measurements, with their instruments;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E5, R-2 (1) and R-3. Chain B, independent of the held branch; cut from CLOUD. Its numbers decide
whether Black Diamond and Eclipse tools are cut in round 3.

<status>pending</status>
<round>2</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
