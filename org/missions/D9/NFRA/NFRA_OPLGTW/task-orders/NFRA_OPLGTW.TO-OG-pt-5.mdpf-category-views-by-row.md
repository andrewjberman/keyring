# NFRA_OPLGTW task order -- `OG-pt-5` -- G3: mdpf_get_category_views, firm-scoped through the existing portal_index gate

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pt-5</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pt-5</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~92</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-pt-5` (decomposition addendum R3-T.60, workstream G3-CATVIEWS, FWD-22 G3; replaces the superseded OG-pt-3)

G3 tool `mdpf_get_category_views` (firm-scoped: one scope per call, reusing the `portal_index` firm gate).

Build one firm-scoped G3 tool, `mdpf_get_category_views`. Module `infra/aws/ec2/opal-gateway/app/portal_mdpf.py`.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` (OG-gt-6) over `app/harvest_typed.py` (OG-gt-0):
- `Scope(name, bucket, served_prefixes, client, max_bytes=64 MiB)`; `admit_scope(scope, tool, ref, *extra)` (principal present, else `principal_required`; Opal user, else
  `typed_opal_only`; `ref` and every `extra` under a served prefix with no `..`, else `typed_prefix_not_served`; one audited refusal each; call it FIRST, before any S3 call);
  `list_keys(scope, prefix)`, `newest_part(scope, prefix)`, `read_parquet(scope, key, columns, filters)`, `read_json(scope, key)` (`.json` and `.json.gz`, capped; raises
  `TypedOverCap`); re-exports `envelope`, `project`, `refusal`, `audit_ok`, `TypedOverCap` (`envelope(body, *, as_of, source_keys, denominator, absent_reason=None)`;
  an empty body must carry an `absent_reason`; the answer is projected to 50 KB with `truncated` set when it is).
- You construct your OWN scope in your module: `Scope("portal", <the bucket>, <your served prefixes>, <client>)`. The bucket is `opal-data-portal-v2`. The client is
  `app.internal_role.s3_client` when it returns a client (the gateway's assumed internal reader role: it already reads `json/*` and `platinum/*`), else a module-scope boto3
  client created lazily INSIDE a function (the `harvest_read._client` pattern; copy it; do not import it from another cell). A tool module never imports
  `get_current_principal` (reach the principal only through `typed_scope`/`harvest_typed`).
- Each tool is a TOP-LEVEL function in your module with exactly the tool's name and inputs below, returns a dict, and answers with `as_of` (THE OBJECT'S OWN as-of field, read
  from the object and named by its contract, never the read time), `source_keys` (the exact keys read), a `denominator` and `absent_reason`. A requested item that is absent
  (an unknown ticker, slug or universe) returns an empty body with `absent_reason`, never an error.

### KEYS COME FROM THE CATALOG (CTO ruling msg 34173; `NFRA_MCPINDEX` msg 34293)

The gateway CODE types NO S3 key, prefix or bucket literal for this table (the commit-time naming limb refuses the legacy `platinum/mdpf/` layout, and there is no override). The key template and the bucket are read at call time from the table's DATA_CATALOG row, owned by `NFRA_MCPINDEX` (v0.5, on your HEAD):
entity `opal_data_portal_v2_platinum_mdpf_category_views` (row id c-5902fd256409; key template `platinum/mdpf/{scope}/category-views.json`; firm-scoped). Do NOT write `app/refs/DATA_CATALOG.yaml`.
The loader is `app/integrations/portal_index/integration.py` `runtime_catalog()` (it returns the loaded catalog `query_v0._catalog()`, built by `app/catalog_gate.py` `load_catalog`); read both to find how a table row is reached by its `entity` name. If the loaded catalog has no accessor by entity, write a SMALL helper in YOUR module that scans the loaded catalog's entries for
`entity == <name>` and returns `bucket`, `prefix` and `key_template`; do not edit `catalog_gate.py`, `query_v0.py` or `portal_index/integration.py`. A row not found, a retired row, or a scope that does not fill the template is `absent_reason` (zero reads). Your module's served prefix is COMPUTED from the row. Tests use a SYNTHETIC catalog fixture of the same shape
(synthetic names, no real key text); the issuer's AC2 probe runs against the real catalog and the real bucket.

### Shape of the reads (the portal's served JSON; contracts at the lines below in `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md`)

Each served object is one JSON document (some gzip-encoded, which `read_json` handles). One whole object per call, projected to 50 KB. The answer's body names the sections you
return (`models`, `series`, ...) as the contract names them; a call that selects one item of a family (`ticker`, `slug`, `universe`, `index`) reads that item's object only.

### The tool (G3 section 3.4, line 252 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md`)

- **`mdpf_get_category_views(scope: str)`**: firm AUA by category (Models, SMA, Client, Alternatives, Insurance) from `platinum/mdpf/<scope>/category-views.json` (contract line 884),
  for ONE scope per call: `global`, `49financial`, `cottonwood` or `inflection`. `global` is the enterprise aggregate, never the sum of the three. Any other scope, or none, is
  refused `harvest_bad_argument` before any S3 call.
- **The firm gate is the existing one, reused, not re-invented.** `app/integrations/portal_index/integration.py` already serves `mdpf_get_aum_metrics`, `mdpf_get_account_distribution`
  and `mdpf_get_aggregate_aua` for one scope with a firm gate: read its `_principal()`, `resolve()` and the `catalog_gate.gate(loaded, key, pclass, pfirm)` call it makes (lines 126-190)
  and apply THE SAME verdict to this tool: a principal whose firm is not the requested scope (and who is not admitted to `global` by that gate) is refused with the gate's own refusal
  and NOTHING is read. Import the gate through the module that already exposes it; do NOT copy the gate's rules, and do NOT edit `portal_index/integration.py` or `app/refs/DATA_CATALOG.yaml`
  (NFRA_MCPINDEX's alone). If the gate cannot be called without a catalog row for this dataset, call it with the row of `getMdpfAggregateAUATimeSeriesByFirm` (the closest existing
  per-scope row) and say so in a row; do not add a row.
- Served prefix of your scope: the prefix of the catalog row above, computed, and nothing wider. The objects `account-units.json` (Cottonwood), `_manifests/` and `archive/` are NOT served by this tool.

### Binding corrections and rules

1. **The object's own as-of.** `as_of` is the as-of field INSIDE the object (the contract names it, for example `data_as_of`), and `source_keys` names the object read. A tool never
   answers a stale object as current: when the object's as-of is more than one trading day behind T-1 (`lib/trading_calendar.py`; never a calendar-day difference), the answer says so in
   its denominator (`trading_days_behind_t1`).
2. **`json-tiered/` is market data only** (375 keys under `market-overview/`). It is read by `portal_get_market_returns` only, and it is a widening named in the G3 never-widen ask.
   A tool NEVER treats `json-tiered/` as an authenticated store.
3. **Never served:** `platinum/advi/` (client PII, catalog hold), `perfrp_*`, tickets, trade submissions, anything under `json/portfolios/<firm>/`. They are not in any served prefix of yours.
4. **A firm-scoped object takes ONE scope per call** (`global`, `49financial`, `cottonwood`, `inflection`); `global` is the enterprise aggregate and is never the sum of the three
   firm scopes. A call naming no scope or an unknown scope is refused `harvest_bad_argument` before any read.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_pt5.py` (a recording fake client; a fake gate where the real one needs the catalog)

- `test_ogpt5_ac01`: an admitted principal reads exactly `platinum/mdpf/<scope>/category-views.json`, and the answer carries the four envelope keys with `as_of` equal to the object's own.
- `test_ogpt5_ac02`: the firm fence, two-firm negative arm: a principal of firm A asking for firm B's scope is refused by the gate's own verdict with ZERO S3 calls and one audit record; the same
  principal asking for its own scope is served.
- `test_ogpt5_ac03`: an unknown scope, an empty scope and a scope with `/` or `..` are refused `harvest_bad_argument` with ZERO S3 calls; a non-Opal and an absent principal are refused first.
- `test_ogpt5_ac04`: `global` is read as its own object, never as a sum (the fake holds three firm objects and a global one with different totals; the answer equals the global one).

The live probe is the issuer's AC2: with the Opal stand-in principal, an unknown scope and a non-Opal principal are refused with no read, and an admitted read of the object the gate admits
equals an independent read of the same key. Run the same calls first, with `INTERNAL_READER_ROLE_ARN` unset.

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
infra/aws/ec2/opal-gateway/app/portal_mdpf.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/tests/test_og_pt5.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~92/`. Rows: id `NFRA_OPLGTW-Z-W92-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pt-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/pt5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pt-5"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/pt5.AC2.sh; echo "exit=$?"</invocation><expect>(?s)category views: bad scopes refused True; global served (True|False) with its own as-of inside the object (True|False); non-Opal refused True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the tool is built, reuses the existing firm gate, proves the two-firm negative arm, and refuses bad scopes before any read.
- `AC2`: against the real portal bucket a bad scope reads nothing, a non-Opal principal is refused, and an admitted read equals an independent read (or the gate's own refusal is returned).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pt-5.mdpf-category-views-tool.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G3-CATVIEWS (decomposition addendum R3-T.60). `OG-pt-3` was SUPERSEDED when `NFRA_MCPINDEX` offered a portal-channel row; `~MI` withdrew that offer (msg 34293: a new certified entity is a CVO matter) and the table row route needs no one else. The hookup rides the batch hookup cell with `OG-et-1` and `OG-et-2`.
- Pre-cut: pt5.AC1 and pt5.AC2 are the superseded pt3 checks re-pointed at the new module test file.

<status>complete</status>
<round>37</round>
<workstream>G3-CATVIEWS</workstream>
<slot>~92</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
