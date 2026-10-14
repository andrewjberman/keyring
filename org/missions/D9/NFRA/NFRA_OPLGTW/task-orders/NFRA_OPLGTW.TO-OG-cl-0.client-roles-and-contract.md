# NFRA_OPLGTW task order -- `OG-cl-0` -- G2 design, read only: the existing firm- and vendor-scoped reader roles, the five core client_* tool contracts, the 08403355 registry proposal

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cl-0</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cl-0</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~83</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-cl-0` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

G2 design cell, read only: the reader-role inventory per vendor, the `client_*` core tool contract, and the registry proposal for master 08403355. No code, no IAM, nothing applied.

READ-ONLY design cell for the client-data tools (FWD-22, G2). It builds no code and changes no IAM. Its output tells the issuer which
reader roles already exist for each vendor, which are missing, and the shape of the `client_*` tools, so the adapter cells and the G2
never-widen ask are cut against measured roles.

**The rule it serves (PRD v3.2, the CVO's condition):** G2 client data NEVER reads through `gateway-global-internal-reader-role`. Key-segment
vendors (Black Diamond, Orion, Eclipse, Schwab, Commonwealth) read through a firm- or vendor-scoped reader role whose S3 grant is
prefix-conditioned to ONE firm; existing roles are used first (build ladder step 2); a missing role is a new role named by
`lib/opal_naming.py`. Only the mixed-firm objects (SmartX, four firms per object; Tax SMA's RIA column) rely on a code row filter,
proved by a two-firm negative arm.

1. **Role inventory.** Enumerate the IAM roles that can read the client-data buckets (`opal-data-assets` silver prefixes for
   `blackdiamond/`, `orion/`, `eclipse/`, `smartx/`, `schwab/`, `commonwealth/`, and `opal-data-bd/silver/`) using the served cloud graph
   (`comp-find --corpus aws '<pattern>' IamRole`, read first; then one live `iam get-role` / `list-role-policies` / `get-role-policy` per
   candidate, read only). For each candidate role record: its trust principals, every S3 read grant (bucket, prefixes, conditions), whether the
   grant is conditioned to ONE firm, and which vendor and firm it serves. Write `W/G2_ROLES.json` =
   `{"read_at", "denominator": {"roles_scanned": N, "roles_with_s3_read_on_client_buckets": M}, "roles": [{"role", "trust_principals": [...],
   "s3_reads": [{"bucket", "prefixes": [...], "conditioned": true|false}], "one_firm": true|false|"unknown", "firm", "vendor"}],
   "vendors": {"<vendor>": {"status": "EXISTING-FIT"|"NEEDS-NARROWING"|"MISSING", "role": "<name>"|null, "why": "<one sentence>"}}}` for the six vendors
   `blackdiamond`, `orion`, `eclipse`, `schwab`, `commonwealth`, `smartx` (and one row `taxsma`). Never print a credential or an account id.
2. **The tool contract.** Write `W/G2_CLIENT_TOOLS_CONTRACT.md` from the PRD addendum v3.1 rulings 1-5 and v3.2
   (`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`, the sections "v3.1 addendum" and "v3.2 addendum") and from the G2 census
   (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G2_assets_silver.md`: sections 1 and 2, lines 1-54, then the per-vendor contracts you need). It has ONE section per core tool, each headed by
   the tool's exact name: `client_resolve_account`, `client_get_holdings`, `client_get_transactions`, `client_get_allocation`,
   `client_get_fees`. Each section states: the inputs; the answer shape and its envelope (`as_of`, `source_keys`, denominator,
   `absent_reason`, `platform_label`, `platform_label_source`); which vendor adapter reads which G2 table (by contract id) and the freshness it
   reads, in trading days (`lib/trading_calendar.py`); the firm fence kind per vendor (`key-segment` or `row-filter`); the refusal arms; and the
   decisions the adapter cell must not re-open (last-4 never unique; Schwab masters 08242234, 08335338 and 08403355 overlap and are deduped by
   account, never summed; snapshot-in-every-partition tables read from the newest partition only; live 49F Black Diamond silver is
   `opal-data-bd/silver/`; unregistered SmartX firms Titleist, Canopy and Parable are never returned; the `49-schwab-conv` tables that stopped on
   2026-07-23 are not served).
   **Andrew-direct ~15:0xZ (CTO msg 34134, record @9a314c1e98; it SUPERSEDES the CTO's 15:03Z "freshest store wins" ruling, msg 34130):**
   "opal-data-bd is not a bucket we want to use for this at all, the only client-data we want to be using explicitly at this time is the
   silver vendor folders in opal-data-assets". So every `client_*` adapter reads ONLY `opal-data-assets/<vendor>/<firm>/silver/`: no
   `opal-data-bd`, no `opal-data-mdpf` feeds, no per-firm Tax SMA gold. The Black Diamond adapter reads `blackdiamond/<firm>/silver/` and states
   its trading-day lag on every answer (49F is behind on row Z-S110; `assets` is 80 trading days behind and `transactions_enriched` 122, so
   neither may answer as current). Increment versus snapshot is UNMEASURED: the adapter cell measures it per table before any tool sums or spans
   dates; name that grain as an open item. In `W/G2_ROLES.json` a vendor with no opal-data-assets vendor-silver prefix to read (Tax SMA today)
   takes status `MISSING` with a `why` that says so; do not inventory roles for the excluded stores, except to name them as NOT USED.
   G2's `ask_inputs` name `opal-data-assets` vendor silver prefixes only.
3. **The registry additions, as a proposal only.** Write `W/G2_SCOPES_PROPOSAL.md`: the exact additions that put master `08403355` into
   `NFRA_OPLGTW_CONTRACT.json` and `infra/logic/registry/scopes.json` (read both files; show the current rows and the added rows). Apply NOTHING.
4. **The ask inputs.** In `W/G2_ROLES.json` under `"ask_inputs"`, list for the G2 never-widen ask: every prefix the core tools read, the role that
   reads it, and the rollback per key for any role that would be NEW or NARROWED.
5. Report once: the vendors by status, and the single biggest gap.

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
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G2_assets_silver.md
org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md
lib/trading_calendar.py
lib/opal_naming.py
org/standards/NFRA_OPLGTW_CONTRACT.json
infra/logic/registry/scopes.json
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/parts/G2f_bd_live_prefixes.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~83/`. Rows: id `NFRA_OPLGTW-Z-W83-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cl-0"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl0.AC1.sh; echo "exit=$?"</invocation><expect>(?s)roles: scanned [1-9]\d*, with S3 read on client buckets \d+, rows \d+, well-formed yes; vendors with a status and a reason 7 of 7; credentials in file 0; ask_inputs present yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cl-0"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl0.AC2.sh; echo "exit=$?"</invocation><expect>(?s)contract: tool sections 5 of 5, each with inputs, freshness, fence and refusal clauses 5 of 5; decisions carried 5 of 5.*scopes proposal: names 08403355 yes.*registry files changed by this cell: 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the role inventory carries its denominator, a status and a reason for all seven vendors, and no credential.
- `AC2`: the contract has one section per core tool with its required clauses and carries the five binding decisions, and the registry files are unchanged.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cl-0.client-roles-and-contract.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- Decomposition addendum R3-T.52: the design the G2 adapter cells (g2-1..n) and the G2 ask are cut against.
- READ ONLY: no write outside `W/` and the investigation file.
- Pre-cut: g20.AC1 and g20.AC2 base FAIL as expected (the records are absent).

- A1 (issuer, 2026-10-14 ~15:1xZ, CTO msg 34130): two Black Diamond rulings added to step 2 and the G2f census added to `<paths>`; ruling (1) is superseded by A2. The worker was
  already running; it is continued with this amendment when it reports. No criterion moves. Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-14 ~15:2xZ, CTO msg 34134, Andrew-direct): client data reads ONLY `opal-data-assets/<vendor>/<firm>/silver/`; step 2 rewritten
  (no opal-data-bd, no mdpf feeds, no per-firm Tax SMA gold); the role inventory keeps its seven vendor rows (Tax SMA may read MISSING). The worker is
  continued with A1+A2 when it reports. No criterion moves. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>FWD22-W3</workstream>
<slot>~83</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
