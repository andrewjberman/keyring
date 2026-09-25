# NFRA_MCPINDEX task order -- `MX-s-1` -- ROUND 2 addendum (Andrew's option 4): TrueShares holdings reach silver, and the guard counts them

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-1</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DS_ClientPlatform~D</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a conversion fix and a one-time backfill; the existing daily conversion runs unchanged.
comp-iam: DECLARED-NOT-APPLICABLE -- the converter's existing role writes the same bucket; no grant changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- a data-completeness repair.
EGRESS CLASS, declared: Opal's own AWS only.
</preflight>

## 1. THE CELL -- `MX-s-1` (decomposition section R2.6)

**Measured at this order's cut, live, read-only:** `opal-data-assets` `trueshares/{DIVZ,IDVZ}/bronze/holdings/` hold 33
delivered dates each. `trueshares/{DIVZ,IDVZ}/silver/fact_holdings/` holds 0 objects. Each fund's
`trueshares/<fund>/meta/backfill-status.json` reads silver `backfill_complete: true`, guard "expected 72 ... missing 0",
because its expected set never counts the holdings feed. The converter for exactly this path exists:
`data/assets/scripts/silver/etf_conversion.py:279-347` (`_convert_trueshares_holdings`), wired at `:231-232`. Source
row: `NFRA_MCPINDEX-W3-S2` (read it in the project channel).

Do, as the DS lane (CLAUDE.md rule 13: DS owns these silver scripts and their QA deploy):
1. **Find why** the holdings feed never converts. Print the evidence: the call path, a dry run on one bronze date, and
   the log line.
2. **Fix the converter** so a delivered holdings file lands in `fact_holdings`, Rule 17 STRICT, as the converter's own
   docstring states. Deploy through `.tools/safe-deploy.sh` as rule 13 requires.
3. **Backfill** every missed date since 2026-08-24 for both funds, idempotent and re-runnable, with each date's result
   printed.
4. **Make the completeness guard count the holdings feed**, so a holdings gap can never again read "missing 0".
   Include a test that plants a missing holdings date and sees the guard report it.

## 2. BOUNDS

1. Silver only. No gold or platinum object, and no served key, is written by this order. The ETF tools that will read
   this data are a later round's.
2. Every live write is idempotent and names the exact keys it wrote. There is no deletion of any object.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
data/assets/scripts/silver/
data/assets/tests/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, as a seat row
`NFRA_MCPINDEX-Z-S<k>` (site-Z; take the next free k), fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from the workspace root after your deploy and backfill)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-1"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s1.AC1.sh; echo "exit=$?"</invocation><expect>for DIVZ and IDVZ, silver fact_holdings dates >= bronze dates > 0; funds converted 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-1"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s1.AC2.sh; echo "exit=$?"</invocation><expect>for DIVZ and IDVZ, guard missing=0, fact_holdings>0, guard expected within 2 of the live silver total; funds whose guard counts the holdings feed 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/NFRA_MCPINDEX.TO-MX-s-1.trueshares-holdings-silver.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once to `2.0.0_SA_COO~O`:
- the cause;
- the fix commit and its deploy;
- the backfilled dates per fund;
- the guard change;
- any row.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary round-2 issuance on Andrew's option 4 (record @bda25438c8; CTO msg 25944): the DS lane 0.4.0_DS_ClientPlatform~D was seated at 22:55:02Z, AFTER round 2's one issuance, for two acts the round-1 analysis PARKED (R-2 (2), R-4); same issuer (2.0.0_SA_COO~O), disjoint write set, nothing on the held branch.

**ISSUER NOTES:** R-4, W3-S2. Supplementary issuance on Andrew's option 4 (@bda25438c8; CTO msg 25944; MSTR seated the
lane at 22:55:02Z). While TrueShares stays unfixed, the ETF tools must exclude it and say so (R-4).

<status>pending</status>
<direct_act>true</direct_act>
<slot>~D</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
