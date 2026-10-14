# NFRA_OPLGTW task order -- `OG-gt-6` -- the scope seam: harvest_typed's helpers generalised by a Scope (bucket, served prefixes, client), HARVEST byte-equivalent

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-6</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-6</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~77</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-6` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

The scope seam the other FWD-22 groups import: `typed_scope.py` with `Scope`, `HARVEST`, `admit_scope` and the four S3 helpers taking a scope; `harvest_typed.py` and `harvest_read.py` untouched.

Build the scope seam. `app/harvest_typed.py` (OG-gt-0, merged, on your HEAD) reaches ONE bucket: its helpers call
`harvest_read._client()` and `harvest_read.BUCKET`. The other FWD-22 groups read other buckets (portal-v2, etfs) with their own
served prefixes. Do NOT edit `harvest_typed.py` or `harvest_read.py` (the five G1 tool cells import them in parallel): add a NEW
module that generalises them by a `Scope`, and prove the HARVEST scope behaves exactly as `harvest_typed` does.

1. **Module `infra/aws/ec2/opal-gateway/app/typed_scope.py`**, importing `harvest_read` and `harvest_typed` as MODULES (never
   `from ... import` of the principal; never boto3):
   - `Scope`: a frozen dataclass `Scope(name: str, bucket: str, served_prefixes: tuple, client: Callable[[], Any], max_bytes: int = harvest_typed.TYPED_MAX_BYTES)`.
   - `HARVEST = Scope("harvest", harvest_read.BUCKET, harvest_read.SERVED_PREFIXES, harvest_read._client)`.
   - `admit_scope(scope, tool, ref, *extra) -> Optional[dict]`: for `HARVEST` it IS `harvest_typed.admit_typed` (same codes). For any
     other scope: a principal must be present (else `principal_required`), must pass `tools._is_opal_user` (else `typed_opal_only`), and
     `ref` and every `extra` must start with a member of `scope.served_prefixes` and contain no `..` (else `typed_prefix_not_served`).
     Each refusal is `harvest_read._refusal(message, code)` and one audited record through `harvest_read._audit`. Import `tools` lazily
     inside the function (as `harvest_read.admit` does).
   - `list_keys(scope, prefix)`, `newest_part(scope, prefix)`, `read_parquet(scope, key, columns=None, filters=None)`, `read_json(scope, key)`:
     the same semantics, signatures and return shapes as the `harvest_typed` functions of the same names, with `Bucket=scope.bucket`, the
     client from `scope.client()`, and the cap `scope.max_bytes` (over it raises `harvest_typed.TypedOverCap`). Reuse the pure parts
     (the filter application, the `_layout_key` ordering, the date coercion) by calling `harvest_typed` helpers; copy only what must
     take the scope. Re-export `envelope`, `project`, `refusal`, `audit_ok`, `TypedOverCap` from `harvest_typed` unchanged.
2. **Tests,** `infra/aws/ec2/opal-gateway/tests/test_og_gt6.py`, S3 replaced by a recording fake client, a principal stand-in patched at
   `harvest_read.get_current_principal`:
   - `test_oggt6_ac01`: over the same fake listing and the same in-memory Parquet, `newest_part(HARVEST, p)`, `list_keys(HARVEST, p)`,
     `read_parquet(HARVEST, k, cols, filters)` and `read_json(HARVEST, k)` return EXACTLY what the `harvest_typed` functions return.
   - `test_oggt6_ac02`: a scope `Scope("t", "other-bucket", ("a/", "b/"), fake_client)` sends every call to `Bucket="other-bucket"` (the fake
     records the argument), and `newest_part` and `read_parquet` work on a `date=` layout under it.
   - `test_oggt6_ac03`: on that scope a non-Opal principal is refused `typed_opal_only`, an absent principal `principal_required`, an off-list
     prefix and a `..` key `typed_prefix_not_served`: each with ZERO recorded S3 calls and one audit record; an Opal principal on `a/x` is admitted.
   - `test_oggt6_ac04`: a scope with `max_bytes=100` refuses (raises `TypedOverCap`) a 500-byte object, in `read_parquet` and in `read_json`.
3. **Your AC2 is a bound and a regression:** `app/harvest_typed.py` and `app/harvest_read.py` are byte-unchanged against the base you
   branched from, and the five `test_og_gt0.py` tests still pass.

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
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/tests/test_og_gt6.py
infra/aws/ec2/opal-gateway/tests/test_og_gt0.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~77/`. Rows: id `NFRA_OPLGTW-Z-W77-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt6.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt6.AC2.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*harvest_typed\.py and harvest_read\.py unchanged vs the base: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the scope seam's four named tests pass: HARVEST is equivalent to harvest_typed, another scope reads its own bucket, refuses before any S3 call, and caps its reads.
- `AC2`: a bound and a regression: the two modules the G1 cells import are byte-unchanged, and gt-0's five tests still pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-6.scope-seam.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- The seam for G3, G6, G5 and G2 (decomposition addendum R3-T.52). Rides the release of the first group that imports it (OG-ap-19).
- No tool is registered by this cell.
- Pre-cut: gt6.AC1 base FAIL as expected (module and tests absent); gt6.AC2 base PASS as expected (a bound and a regression: nothing differs at the base).

<status>pending</status>
<round>37</round>
<workstream>FWD22-W3</workstream>
<slot>~77</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
