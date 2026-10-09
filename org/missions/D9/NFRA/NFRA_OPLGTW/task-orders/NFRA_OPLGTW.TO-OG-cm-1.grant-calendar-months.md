# NFRA_OPLGTW task order -- `OG-cm-1` -- a grant may reach 13 months: the `calendar_months` window (PRD v2.0 item 4, FWD-12)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cm-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cm-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~42</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and contract change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; S3 and the state store are faked in the tests.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is PRD v2.0 item 4 (org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @e43ee663be, both halves signed @5924aaedbe) and section 4a of org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round31.md @8ca3947b86.
EGRESS CLASS, declared: NONE. No network request of any kind.
</preflight>

## 1. THE CELL -- `OG-cm-1` (decomposition addendum R3-T.30, round 32 item 8a)

Andrew-direct 2026-10-08 ~21:2xZ: Alyssa's gateway access with 13 months of history, "asap". Today the gateway serves a
ROLLING window of the latest qualified complete business date and the previous 29 calendar days, fixed contract-wide
(`window_days` in `infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py`, `availability()` near line 871), or
a FIXED enumerated date set (`date_mode` `fixed_dates`). PRD v2.0 item 4, verbatim:

> "A grant may set `calendar_months` (1 to 13) in place of `calendar_days`; exactly one is set. The window is the latest
> qualified complete business date and every business date on or after the same calendar day 13 months earlier
> (month-end clamped). A date with no qualified completion record is reported unavailable (C3 unchanged). ... The query
> and export caps (A14) are not raised by this addendum; a measured run over 13 months decides whether any cap moves,
> as its own ruling."

READ first: `catalog.py` `availability()` and `_enumerated()`, `app/integrations/schwab/integration.py` (how a grant's
date mode reaches `availability`), `app/data_entitlement.py` and `app/admin_grants.py` (the grant record and its
validation), `ops/schwab_entitlement_admin.py` (the operator's grant writer), and the contract
`org/standards/NFRA_OPLGTW_CONTRACT.json` (`grant_date_modes`, `proposed_initial_profile`, `limits`).

Do:
1. **The grant field.** A rolling grant may carry `calendar_months` (an integer 1 to 13) OR `calendar_days` (as today),
   never both. A grant with neither keeps today's contract window exactly. Validate at the grant WRITE (admin path and
   the ops writer) and again at the READ (a stored grant that violates it is refused, never coerced).
2. **The window.** With `calendar_months = n`: anchor on the latest qualified date for that master and dataset (as
   today), and the first date is the same calendar day n months earlier, clamped to that month's last day
   (2026-03-31 with n=13 gives 2025-02-28). Every listed completion date in [first, latest] is evaluated as today;
   unqualified dates go to `not_available`. The response's `window` names `calendar_months` and the first and last
   dates. Nothing is filled from another date, dataset or master.
3. **The contract.** Record the new field in `org/standards/NFRA_OPLGTW_CONTRACT.json` in the contract's own style
   (where the rolling window and grant modes are declared), with its bounds 1 to 13 and the rule "exactly one of
   calendar_days or calendar_months". Do NOT change `limits`, `masters`, `datasets`, `data_prefixes` or
   `forbidden_field_classes`. Copy the file byte-for-byte to `infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json`
   (the release suite refuses a differing copy). If the contract carries a version field, bump its minor.
4. **Performance, measured not assumed.** A 13-month window evaluates up to ~280 dates per master and dataset. In a
   test, time `availability()` over 280 faked qualified dates and state the figure in your report. Do not raise any cap
   and do not add a cache; if the figure threatens the 30-second deadline, file a row with the number.
5. **Tests**, offline, in a new file `infra/aws/ec2/opal-gateway/tests/test_grant_calendar_months.py`, named EXACTLY
   `test_ogcm1_ac01` .. `test_ogcm1_ac05`, as the header of
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/cm1.AC1.sh` lists them. Reuse the fakes of
   `tests/test_schwab_catalog.py`.
6. Run, each in its own process, and state totals: `tests/test_grant_calendar_months.py`, `tests/test_schwab_catalog.py`,
   `tests/test_schwab_query.py`, `tests/test_admin_grants.py`, and any test that reads the contract file.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~42/`.

## 2. BOUNDS

- No release, no deploy, no grant written to any live store, no AWS call. This cell is BUILT and HELD on your branch;
  Alyssa's and Andrew's grants are set to 13 months at the release, not here.
- No cap in `limits` moves. Delete or rename no existing test; change no existing assertion.
- Fetch nothing from the internet. Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/catalog.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/admin_grants.py
infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py
infra/aws/ec2/opal-gateway/ops/schwab_status.py
infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json
infra/aws/ec2/opal-gateway/tests/test_grant_calendar_months.py
org/standards/NFRA_OPLGTW_CONTRACT.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~42/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W42-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/cm1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cm-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/cm1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_schwab_catalog\.py: pytest rc=0 .*removed or renamed 0.*test_schwab_query\.py: pytest rc=0 .*removed or renamed 0.*test_admin_grants\.py: pytest rc=0 .*removed or renamed 0.*contract copies: identical.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the 13-month window, its refusals, the unavailable-date rule, the unchanged default and the unchanged caps.
- `AC2`: the catalog, query and grant suites pass whole, and the two contract copies are identical.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cm-1.grant-calendar-months.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the diff of every app file and the contract; the measured 280-date timing; every
   test file run with its totals; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), item 8a: the gateway half of FWD-12, split by the issuer from section 4a's item 8 because the
  13-month reach needs a grant mode the gateway does not have. The marker backfill (item 8b) is `OG-bf-1`.
- This cell OWNS the contract file this round. `OG-tm-1`'s contract lines for master 08403355 (`masters`, four
  `data_prefixes`, one `completion_prefixes`) are a merge hookup the issuer adds at the drain, never a second writer.
- Ships in the r29 release (`OG-rl-15`), which the issuer proposes to the CTO to carry this cell beside R55's three;
  the grants are set to 13 months at that release (Andrew's and Alyssa's principals only, his 17:4xZ answer 2).
- Pre-cut: see the issuance commit.

<status>complete</status>
<round>32</round>
<slot>~42</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
