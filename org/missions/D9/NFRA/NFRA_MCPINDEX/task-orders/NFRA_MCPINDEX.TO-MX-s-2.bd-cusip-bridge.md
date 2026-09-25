# NFRA_MCPINDEX task order -- `MX-s-2` -- ROUND 2 addendum (Andrew's option 4): the Black Diamond cusip bridge on a production schedule, and the one affected served figure corrected

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-2</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DS_ClientPlatform~D</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at the act -- this order CREATES a production schedule (a producer trigger, not an alarm or monitor; ruling R-2 (2) names it so).
comp-iam: DECLARED-NOT-APPLICABLE -- the builder runs under its existing identity; the schedule's invoke grant is the DT/AE apply's (rule 13) and is carded there.
comp-adversary: DECLARED-NOT-APPLICABLE -- a data-completeness repair.
EGRESS CLASS, declared: Opal's own AWS only.
</preflight>

## 1. THE CELL -- `MX-s-2` (decomposition section R2.6)

**Measured, live, read-only:**
- `opal-data-bd` `silver/bd_assets_dim.parquet`, the asset_id-to-cusip bridge, was last written 2026-04-14T20:44:16Z.
- No scheduler runs its builder, `build_bd_assets_dim.py`.
- Since 2026-04-14, 14,367 of 3,185,260 silver transaction rows carry a null cusip.
- Of the 3 served figures that join on cusip, ONE carries nulls: `s3://opal-data-bd/gold/timeseries/holdings_lots/2026-09-18.parquet`,
  22,172 null-cusip rows of 1,264,679. Its producer, `data/black_diamond/scripts/gold/B_01.holdings_lots.py:280-305`,
  also maps cusip 'CASH' to null at `:291`, so some of those nulls are cash by design.

Sources: `deliverables/0.9.0_WK_NFRA_MCPINDEX~4/round2-reads.result.md`, and the CTO's ruling R-2 in
`org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round1.md`. READ BOTH.

Do:
1. **The production schedule** for the bridge builder, placed BEFORE the silver merge it feeds. Its name comes from
   `lib/opal_naming.py name()` and contains `assets-dim`. It is a production schedule, never an alarm.
   - CLAUDE.md rule 13 gives PROD triggers to the DT/AE lanes. If the lane gate refuses your trigger file, write the
     schedule spec into your deliverables and file a BLOCKING row naming the DT/AE apply. Do not work around the gate.
   - Fire the builder ONCE ad hoc as QA. The schedule stays the acceptance.
2. **The served correction**, under a never-widen sign-off, because it rewrites served gold:
   - write the blast radius to `deliverables/0.4.0_DS_ClientPlatform~D/SIGNOFF_REQUEST_bd_cusip.md`: every
     `holdings_lots` partition to be re-run, and the rollback per key (the prior object's version);
   - STOP until BOTH halves are recorded in it, `1.0.0_SA_CTO~O` and `2.0.0_SA_COO~O`;
   - then open the NEVER-2 ledger with slug `nfra-mcpindex-bd-cusip-served-fix`, commit the entry and its sentinel,
     re-run B_01 for exactly those partitions, and close the entry.
3. **The probe** `deliverables/0.4.0_DS_ClientPlatform~D/probes/mx_s_2.py AC3`. It reads the latest `holdings_lots`
   partition and counts null-cusip rows that are NOT cash by B_01's own cash rule, with the denominator printed. It
   prints `VERDICT: PASS-MXS2-AC3` only when that count is 0.

## 2. BOUNDS

1. No served key moves before both sign-off halves are recorded. Rewrites are to the named partitions only, with the
   rollback proven per key.
2. No alarm, monitor or notification is built (the standing moratorium). A schedule is a producer trigger.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
data/black_diamond/scripts/silver/
data/black_diamond/scripts/gold/B_01.holdings_lots.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-bd-cusip-served-fix.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, as a seat row
`NFRA_MCPINDEX-Z-S<k>` (site-Z; take the next free k), fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from the workspace root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-2"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s2.AC1.sh; echo "exit=$?"</invocation><expect>schedules/rules named *assets-dim* ENABLED>=1; bd_assets_dim.parquet LastModified after issue=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-2"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s2.AC2.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-2"><invocation>timeout 300 python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/probes/mx_s_2.py AC3</invocation><expect>(?m)^VERDICT: PASS-MXS2-AC3(?![0-9])</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/NFRA_MCPINDEX.TO-MX-s-2.bd-cusip-bridge.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once to `2.0.0_SA_COO~O`:
- the schedule's name and placement;
- the ad-hoc fire;
- the sign-off file;
- the partitions rewritten;
- the ledger path;
- any row.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary round-2 issuance on Andrew's option 4 (record @bda25438c8; CTO msg 25944): the DS lane 0.4.0_DS_ClientPlatform~D was seated at 22:55:02Z, AFTER round 2's one issuance, for two acts the round-1 analysis PARKED (R-2 (2), R-4); same issuer (2.0.0_SA_COO~O), disjoint write set, nothing on the held branch.

**ISSUER NOTES:** R-2 (2), C-S13. Supplementary issuance on Andrew's option 4 (@bda25438c8; CTO msg 25944). No Black
Diamond tool that answers by cusip is cut until this closes (R-2 (3)).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~D</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
