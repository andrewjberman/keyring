# NFRA_OPLGTW task order -- `OG-ac-2` -- build `mdpf_get_security_classification`, the typed read of the DynamoDB etf-classifications table (the named next increment, from OG-ac-1's spec)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ac-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ac-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~113</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code, offline tests and one read-only probe; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes NO IAM. The gateway role's read of the table is the later grant order (`dynamodb:GetItem` on the table ARN); your probe reads with the box's own credentials, `GetItem` only, two keys.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @d97ea3ae82 section 2 (the named next increment) built from the census and spec of OG-ac-1 (`W/ETF_CLASS_SPEC.md`, merged `a69cf430b1`).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ac-2` (decomposition addendum R3-T.83, workstream CLASS-INCREMENT-2, FWD-22)

Build ONE tool in a NEW module `infra/aws/ec2/opal-gateway/app/mdpf_classification.py`: `mdpf_get_security_classification(ticker: str, as_of: str = "latest") -> dict`. Its whole specification is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/ETF_CLASS_SPEC.md` section `## Tool` and section `## Refused` (read both, and `ETF_CLASS_CENSUS.json` beside it, and the contract `org/standards/MDPF_SECCLASS_CONTRACT.json` for the row fields and the key forms). In short:
1. Read path: ONE `get_item` by `Key = {"ticker": <ticker>}` on the table `etf-classifications` (us-east-1). NEVER `scan`, `query`, `batch_get_item` or any write call (the issuer's AC2 greps the module for them). The table NAME is read at call time from a DATA_CATALOG row if one names it (`app/refs/DATA_CATALOG.yaml`, entity `opal_data_mdpf_gold_ai_classified_securities` and its `canonical_table` or `notes` fields; read the row); if the catalog row carries no table name, define it as ONE module constant `TABLE = "etf-classifications"` with a comment citing the contract file, and file an OBSERVATION row saying the catalog lacks it (a DynamoDB table name is a resource name the code may hold; it is not an S3 key).
2. Refusals BEFORE any DynamoDB call, zero calls, each audited as one denied row, with the codes of the spec: `principal_required` (no principal), `typed_opal_only` (not an Opal user), `harvest_bad_argument` for a missing, non-string, empty, over-96-character, whitespace-or-`/`-bearing `ticker` and for an `as_of` other than `latest`. Admit the principal through the seam below (`admit_scope`), not by importing `get_current_principal`.
3. The answer is the common envelope (`as_of` = the row's own `last_updated` date, `source_keys`, `denominator` `{"rows": 1}` or `{"rows": 0}`, `absent_reason` when the ticker has no row) and the body fields the spec names: `asset_class`, `sub_asset_class`, `classified_by` (absent reads `legacy`), `classification_confidence` and `low_confidence` (present only on `model` rows, null otherwise), `identifier_namespace` (absent reads `TICKER`), `last_updated`. It states the row's lag in trading days behind T-1 with `lib/trading_calendar.py` as the OG-sv-1 tools do. Print and store nothing else of the row.
4. Opal principals only; the 50 KB projection applies.

### The seam you build on (ALREADY ON YOUR HEAD)

`app/typed_scope.py` over `app/harvest_typed.py` (`admit_scope`, `envelope`, `refusal`, `audit_ok`, the principal read through the `harvest_read` module attribute) and `app/internal_role.py` for the client. Your own OG-sv-1 module `app/portal_json_served.py` is the closest model of the envelope, the freshness line and the audit; mirror it. A DynamoDB client is created lazily (never at module scope); use `internal_role` for the assumed role when it has a DynamoDB client helper, else a lazily created `boto3.client("dynamodb", region_name="us-east-1")`; do not edit `internal_role.py`.

### Tests, named, in `tests/test_og_ac2.py` (a recording fake DynamoDB client: it records every call name and key; an Opal stand-in principal)

- `test_ogac2_ac01`: a found row returns the envelope with `as_of` from `last_updated`, the named body fields, and the fake saw exactly ONE `get_item` with `Key == {"ticker": <ticker>}`.
- `test_ogac2_ac02`: defaults: a row with no `classified_by` reads `legacy`, no `identifier_namespace` reads `TICKER`, a non-`model` row reads `classification_confidence` and `low_confidence` null.
- `test_ogac2_ac03`: a ticker with no row answers `absent_reason` and `denominator` rows 0 (one read).
- `test_ogac2_ac04`: every refusal arm of the spec (no principal, non-Opal, empty/missing/non-string/over-96/whitespace/slash ticker, `as_of` other than `latest`) is refused with the right code and the fake saw ZERO calls.
- `test_ogac2_ac05`: the module source holds no `scan`, `query`, `batch_get_item` or write call (a source check), and no table-wide read happens in any test.
- `test_ogac2_ac06`: no tool name ends in `_group` or `_role`; the answer for a row over the cap is `harvest_over_cap`.

### Probe (`W/probe_ac2.py`, you write and run it; the issuer re-runs it as AC2)

Against the REAL table with the box's credentials (`INTERNAL_READER_ROLE_ARN` unset), an Opal stand-in principal: (a) pick ONE ticker that has a row WITHOUT reading any other row (ask for the key of a well-known ETF ticker such as `SPY` first; if absent try `AGG`, then `QQQ`; at most three `get_item` calls in all); call the tool and print ONE line `probe cls: mdpf_get_security_classification answered True as_of <YYYY-MM-DD> non_opal_refused True reads_on_refusal 0` after also calling it as a non-Opal principal and asserting the refusal with zero reads; (b) call the tool on the ticker `ZZNOSUCHKEY9` and print ONE line `probe cls: absent_ticker answered True absent_reason set True`. Print no row content.

## 2. BOUNDS

- A new module, its tests and the probe, and the record files. No release, no deploy, no IAM or Terraform change, no write to any table, no catalog edit.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer registers the tool and re-pins at the merge. Name the registration you expect.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a security's classification content, a person's name or an account number; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/mdpf_classification.py
infra/aws/ec2/opal-gateway/tests/test_og_ac2.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/probe_ac2.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/ETF_CLASS_SPEC.md
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/ETF_CLASS_CENSUS.json
org/standards/MDPF_SECCLASS_CONTRACT.json
infra/aws/ec2/opal-gateway/app/portal_json_served.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/app/internal_role.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE only the first three paths, the proof instance under `W` and the investigation file (append rows); the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/`. Rows: id `NFRA_OPLGTW-Z-W113-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ac-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ac2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 6 of 6; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ac-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ac2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)module: tool defined 1 of 1; get_item calls [1-9]\d* \(want 1 or more\); scan/query/batch/write calls 0 \(want 0\).*probe: real row answered 1 of 1; absent ticker answered with absent_reason 1 of 1.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the six named offline tests pass. `AC2`: the module reads by `get_item` only, and the probe answered a real row and an absent ticker against the real table and refused a non-Opal principal with zero reads.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ac-2.security-classification-tool.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the registration and the pinned-count move you expect).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream CLASS-INCREMENT-2 (decomposition addendum R3-T.83). Outside the 22:00Z line (CTO ruling @d97ea3ae82 section 2): the tool needs the gateway role's one `dynamodb:GetItem` grant (`OG-ap-25`, three halves, `0.7.0_AE_CloudOps~ZS`) before it can serve, then a code release after `OG-ap-23`. The probe uses the box's own credentials, so the build does not wait on the grant.
- Census facts to know: 11,362 items, hash key `ticker`, `last_updated` (newest 2026-10-08 in a 200-item sample); the contract's 3,507-row figure (2026-10-07) is stale (row Z-W113-S5).
- Pre-cut: ac2.AC1 and ac2.AC2 base FAIL as expected (module, tests and probe absent).

<status>complete</status>
<round>37</round>
<workstream>CLASS-INCREMENT-2</workstream>
<slot>~113</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
