# NFRA_OPLGTW task order -- `OG-sc-1` -- the exact column lists of seven Schwab silver tables, both masters (PRD v2.0 items 1-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~40</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only measurement; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE the reads run under the operator's IAM user: ListObjectsV2 with a delimiter, HEAD and two ranged GETs per object (the parquet footer only) on s3://opal-data-assets/schwab/{08242234,08335338}/silver/; no role or policy is read for a decision or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is round-31 analysis item 4 (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round31.md @e43ee663be) and PRD v2.0 items 1-2 (@e43ee663be, signed @5924aaedbe).
EGRESS CLASS, declared: NONE beyond Opal's own S3.
</preflight>

## 1. THE CELL -- `OG-sc-1` (decomposition addendum R3-T.30, round 32 item 4)

PRD v2.0 widens the gateway: account identity columns (item 1) and new datasets (item 2: `fact_acc` as `dim_account`,
open lots `fact_uln`/`fact_ult`, closed lots `fact_rld`/`fact_rly`/`fact_rty`, and `fact_trn`'s codes for flow
labels). The contract's `fields` lists are written FROM this cell's record, so the record must be the exact,
measured column list, never typed from memory or from another master.

Do:
1. For each master `08242234` and `08335338`, and each table `fact_acc`, `fact_uln`, `fact_ult`, `fact_rld`,
   `fact_rly`, `fact_rty`, `fact_trn`: find the newest partition under
   `s3://opal-data-assets/schwab/<master>/silver/<table>/date=YYYY-MM-DD/` (a delimiter listing), and read the schema
   of its `data.parquet` from the FOOTER ONLY: HEAD for the size, a ranged GET of the last 8 bytes for the footer
   length, a ranged GET of the footer, then `pyarrow.parquet.read_schema(io.BytesIO(b"PAR1" + footer + last8))`.
   (This exact recipe was measured by the issuer at the cut on `fact_acc` 08335338: 95 columns.)
2. Record, per (master, table): `newest_date`, `key`, `partitions` (the count of `date=` partitions), and `columns` as
   an ordered list of `{"name": <field name>, "type": <str(arrow type)>}`. `num_rows` from the footer is allowed.
3. **No row content.** Read no row group. Do NOT read, print or record column statistics (min, max, null counts,
   distinct counts): parquet statistics ARE row values (account numbers, names). The record must carry no such key.
4. Write `W/silver_schema_record.json` as `{"bucket": "opal-data-assets", "measured_utc": "...", "method": "...",
   "tables": {"<master>": {"<table>": {...}}}}`, and `W/silver_schema.result.md`: per table, the two masters' column
   lists side by side, every column present in one master and not the other, and every type that differs.
   Mark, without deciding anything, each column whose NAME suggests one of: account number, a name or title, tax id,
   mailing address, email, phone (a list for the CTO, who classifies; you classify nothing).

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~40/`.

## 2. BOUNDS

- Read only. No write, copy or delete anywhere in S3. Only the two masters' `silver/` prefixes; no other firm's data.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~40/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W40-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sc-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/sc1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)cells checked: 14 of 14.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the issuer's reader re-lists every newest partition and re-reads every footer live, and your record equals it
  name for name and type for type, with no statistic in it.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sc-1.silver-schema-measurement.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: the literal AC output; per table the column counts for both masters and the differences; the
   name-flag list; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), item 4. Item 4's second clause (the oldest and newest qualified completion record per master) is
  read by `OG-cc-1` with the same instrument as item 5's census, so the two are never measured twice.
- Feeds round 33's G1/G3/G4 build, cut by the CTO from this record (section 4a: identity columns and lots stay round 33's).
- Pre-cut: see the issuance commit.

<status>complete</status>
<round>32</round>
<slot>~40</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
