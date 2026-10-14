# NFRA_OPLGTW task order -- `OG-pt-2` -- G3: portal_get_macro, portal_get_valuation, portal_get_security_scan, portal_get_pipeline_freshness

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pt-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pt-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~80</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-pt-2` (decomposition addendum R3-T.52, workstream FWD22-W5, FWD-22 G3)

G3 tools `portal_get_macro`, `portal_get_valuation`, `portal_get_security_scan` and `portal_get_pipeline_freshness`.

Build four G3 portal tools over the macro, valuation, security-scanner and pipeline objects. Module `infra/aws/ec2/opal-gateway/app/portal_macro.py`.

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

### FIRST ACT (the naming limb stopped five G1 workers last round)

The commit-time naming gate (`.tools/naming-gate.py`, LGIC_ENFORCE) REFUSES a NEW out-of-pattern S3 key literal and has no override. Before you build anything: write the list of every
S3 key or prefix literal your module will hold into a scratch file under your `W/` directory, stage it as a `.py` file with one assignment per literal, and run
`python .tools/naming-gate.py --diff <the staged diff> --enforce`. If ANY literal is refused, do not type it: STOP at once, file ONE BLOCKING row naming the refused literals and the gate's
canonical suggestion, and report (the issuer rules the resolution). If all are CONFORMANT, build. Never split a string, build a key from pieces to hide it from the gate, or override it.

### Shape of the reads (the portal's served JSON; contracts at the lines below in `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md`)

Each served object is one JSON document (some gzip-encoded, which `read_json` handles). One whole object per call, projected to 50 KB. The answer's body names the sections you
return (`models`, `series`, ...) as the contract names them; a call that selects one item of a family (`ticker`, `slug`, `universe`, `index`) reads that item's object only.

### The four tools (G3 section 3.4, lines 257-260 of `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md`)

- **`portal_get_macro(slug: str = None)`**: with no slug, the macro indicators from `json/macro/macro_data.json`, the volatility objects `json/macro/volatility_data.json`
  and the yield curve `json/macro/yield_curve_fred.json` (lines 534-608); with a `slug`, that indicator's series from `json/macro/timeseries/<slug>.json` (79 members; an unknown
  slug returns an empty body with `absent_reason`; a slug with `/` or `..` is refused `harvest_bad_argument`).
- **`portal_get_valuation(index: str = None)`**: from `json/valuation/valuation_data.json` and `json/valuation/risk_premium_data.json` (lines 609-645); with `index`, only that
  index's block of each (the contract names the key); an unknown index returns an empty body with `absent_reason`.
- **`portal_get_security_scan(universe: str, factor: str = None, top: int = 20)`**: the top and bottom names of one universe by factor percentile, from
  `json/security_scanner/latest/universes/<universe>/scanner_data.json` and `json/security_scanner/latest/factor_metadata.json` (lines 755-773). `top` is clamped to 100
  (`limit_applied` says so); an unknown universe returns an empty body with `absent_reason`; a universe with `/` or `..` is refused `harvest_bad_argument`. It never returns a
  client or firm figure (this is a manual FactSet upload of public securities).
- **`portal_get_pipeline_freshness()`**: each source's `data_as_of` and last run from `json/latest/manifest.json` (lines 774-792), with `trading_days_behind_t1` per source.

Served prefixes of your scope (exactly these): `json/macro/`, `json/valuation/`, `json/security_scanner/`, `json/latest/`.

### Binding corrections and rules

1. **The object's own as-of.** `as_of` is the as-of field INSIDE the object (the contract names it, for example `data_as_of`), and `source_keys` names the object read. A tool never
   answers a stale object as current: when the object's as-of is more than one trading day behind T-1 (`lib/trading_calendar.py`; never a calendar-day difference), the answer says so in
   its denominator (`trading_days_behind_t1`).
2. **`json-tiered/` is market data only** (375 keys under `market-overview/`). It is read by `portal_get_market_returns` only, and it is a widening named in the G3 never-widen ask.
   A tool NEVER treats `json-tiered/` as an authenticated store.
3. **Never served:** `platinum/advi/` (client PII, catalog hold), `perfrp_*`, tickets, trade submissions, anything under `json/portfolios/<firm>/`. They are not in any served prefix of yours.
4. **A firm-scoped object takes ONE scope per call** (`global`, `49financial`, `cottonwood`, `inflection`); `global` is the enterprise aggregate and is never the sum of the three
   firm scopes. A call naming no scope or an unknown scope is refused `harvest_bad_argument` before any read.

### Tests, `infra/aws/ec2/opal-gateway/tests/test_og_pt2.py` (a recording fake client; Opal stand-in principal)

- `test_ogpt2_ac01`: each tool reads exactly its objects, answers with the four envelope keys, and `as_of` equals the as-of field inside the fixture object.
- `test_ogpt2_ac02`: an unknown slug, index and universe each return an empty body with `absent_reason`; a slug or universe with `/` or `..` is refused `harvest_bad_argument` with ZERO S3 calls.
- `test_ogpt2_ac03`: `portal_get_security_scan` clamps `top=500` to 100 with `limit_applied`, orders by the factor percentile, and returns top and bottom names.
- `test_ogpt2_ac04`: a non-Opal principal and an absent principal are refused every tool with ZERO S3 calls; an over-cap object is refused `harvest_over_cap`.
- `test_ogpt2_ac05`: `portal_get_pipeline_freshness` reports `trading_days_behind_t1` per source and marks a frozen source (a source more than five trading days behind) as stale in the body.

The live probe is the issuer's AC2. Run the same calls yourself first, with `INTERNAL_READER_ROLE_ARN` unset.

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
infra/aws/ec2/opal-gateway/app/portal_macro.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/tests/test_og_pt2.py
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G3_portal_v2.md
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~80/`. Rows: id `NFRA_OPLGTW-Z-W80-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pt-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/pt2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pt-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/pt2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)portal tools: 5 of 5 answered from their keys with the object's own as-of \(.*\); non-Opal principal refused True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the four tools are built, read exactly their objects, clamp and refuse before any S3 call, and report freshness in trading days.
- `AC2`: against the real portal bucket all four answer from their keys with an as-of that sits inside the object, and a non-Opal principal is refused.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pt-2.portal-macro-tools.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.52; PRD v3.4 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- Decomposition addendum R3-T.52 (G3). Rides the release `OG-ap-19` with the G3 never-widen ask (`json-tiered/`); the grant needs no new IAM (the internal reader already reads json/* and platinum/*).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).

<status>pending</status>
<round>37</round>
<workstream>FWD22-W5</workstream>
<slot>~80</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
