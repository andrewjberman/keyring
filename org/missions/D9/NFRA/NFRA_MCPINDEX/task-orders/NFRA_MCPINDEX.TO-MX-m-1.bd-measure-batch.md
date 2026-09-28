# NFRA_MCPINDEX task order -- `MX-m-1` -- the read-only measure batch: BD SSM exit honesty, the 42 cusip deltas in silver, the CASH share of null cusips, and the lots consumers

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-m-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~11</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- read-only measurements; nothing is scheduled, fired or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads with the seat's existing Opal AWS credentials; no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- measurements, graded at L9.
EGRESS CLASS, declared: NONE beyond Opal's own AWS reads (S3 get/list, SSM list-commands/get-command-invocation/get-document). No vendor call.
</preflight>

## 1. THE CELL -- `MX-m-1` (round 3, enrichment item 4)

Four measurements. Nothing is fixed here: each finding routes through a row or the issuer. For EVERY number you
report, print the denominator beside it and name the command that produced it. A zero must name what would have made it
non-zero.

**(a) Exit honesty of the BD SSM documents other than `opal-bd-asset-dim-download`.**
- Enumerate the Black Diamond SSM documents (`aws ssm list-documents` with Owner Self, then filter by name); print the
  denominator.
- For each document, read its content (`aws ssm get-document`). Name the failure branch and whether it ends in a
  non-zero `exit`.
- Then take its last N runs, N stated (`aws ssm list-commands --filters key=DocumentName,value=<doc>`). Compare each
  run's SSM Status against the outcome its own uploaded log records.
- Report the count of runs where SSM says Success while the log records failure.
- Row Z-S47 measured the fees document at 69 of 121. Re-measure it in the same table.

**(b) Did MX-s-6's 42 cusip deltas reach silver transactions?**
- `data/black_diamond/scripts/silver/merge-daily-incremental.py:57` joins `silver/bd_assets_dim.parquet` for cusip
  enrichment on every daily run.
- The dim was rewritten 2026-09-28 ~06:22Z with 42 changed cusips (VersionId `pdoQY5Waj63_...` vs its predecessor;
  list the versions to find both).
- Measure how many silver transaction rows written AFTER that version now carry a cusip that differs from the value
  the PREDECESSOR dim would have given them.
- Count them by the 42 asset_ids, never listing rows.

**(c) The CASH share of `holdings_lots`' null cusips.** Gold `holdings_lots` reads 22,172 of 1,264,679 null (R-11).
`B_01` maps 'CASH' to null. Of the null-cusip rows at the latest partition, how many are cash rows? State the
predicate you used for "cash" and cite its file:line.

**(d) A live-consumer census for gold `canonical/lots_unrealized` and `canonical/lots_realized`.** Both have been
silent since 2026-07-23 (row Z-W4-S2). Find every reader in the repo with `comp-find`, and print the denominator.
Name the LIVE ones: a scheduled job, a Lambda or a served page that reads them. Say whether anything reads them today.

Write `MEASURE_BATCH_ROUND3.md` in your deliverables dir. It has four sections headed exactly `## (a)`, `## (b)`,
`## (c)`, `## (d)`. Each section has a line starting `DENOMINATOR:` and a line starting `FINDING:`. Commit it.

## 2. BOUNDS

1. READ-ONLY: no S3 write, no SSM send-command, no Lambda invoke, no schedule change.
2. Firm line: Black Diamond reads stay in the bd plane (`opal-data-bd`). Nothing under `data/cot/` or cot's bucket.
3. No private data in the repo: no account ids, no asset rows, no names. Counts, ids-as-counts and hashes only.
4. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~11/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W11-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-m-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/m1.AC1.sh; echo "exit=$?"</invocation><expect>sections complete 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-m-1" judgment="true"><!-- graded at L9 by 3.0.0_SA_CVO~O: does each of (a)-(d) answer its question on the right population, with its denominator and its instrument named, and is a zero's cause named? R-11's REMEDIATION_v1 flip and item 5's census read (c) and (a). The worker records, never grades. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~11/NFRA_MCPINDEX.TO-MX-m-1.bd-measure-batch.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once: the four FINDING lines, the commit hash, and any rows.
Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-2 analysis s.5 item 4 (a)-(d) @e4445020f5; R-11.
- Dry-run at base: m1.AC1 FAIL (the record is absent).
- Result routing:
  - (a) decides whether Z-S47's class extends past the fees leg, which MX-s-12 retires;
  - (b) grades the CTO's own caveat (carry-list draft item 4);
  - (c) feeds R-11's REMEDIATION_v1 flip;
  - (d) closes Z-W4-S2's open question.

<status>pending</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
