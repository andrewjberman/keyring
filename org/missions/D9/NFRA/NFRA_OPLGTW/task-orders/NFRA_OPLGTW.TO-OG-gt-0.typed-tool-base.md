# NFRA_OPLGTW task order -- `OG-gt-0` -- the typed-tool base (envelope, projection, newest-part read, one admit wrapper)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-0</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-0</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~71</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: RUN-BY-ISSUER at the cut: the new code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant (A5: the policy on gateway-global-internal-reader-role, which `harvest_read._client()` assumes); this cell changes no IAM and adds no AWS call beyond those two. Live probes run with the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z msg 34077 and msg 34083 on PRD v3.0 (FWD-22; Andrew-direct ~12:4xZ), the CRO's G1 census @0d7c29b3c5 section 3, and the two corrections of the CRO's L4-R review @e47fafb709.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-0` (decomposition addendum R3-T.50, workstream G1-TYPED, FWD-22)

The typed-tool base: the envelope (`as_of`, `source_keys`, denominator, `absent_reason`), the 50 KB projection, the newest-part read over `harvest_read`'s capped client, one admit-and-audit wrapper; offline tests with a fake client.

Build the typed-tool base the other five cells import. Today `app/harvest_read.py` (OG-hv-1, already on your HEAD) serves
`harvest_list` and `harvest_read` over `s3://opal-data-harvest`: admission by `admit()`, a capped client, one audit row. Its
Parquet reader returns at most 1000 rows of every column; a typed tool needs column projection, filters and the newest-part
rule, so the base is a NEW module that reuses `harvest_read` (`admit`, `_client`, `_audit`, `_refusal`, `BUCKET`,
`CODE_*`) and changes none of it.

1. **Module `infra/aws/ec2/opal-gateway/app/harvest_typed.py`** with exactly the surface below. It imports `harvest_read` as
   a module and calls `harvest_read.get_current_principal()` through that module attribute (never `from ... import`), so a
   probe that replaces `harvest_read.get_current_principal` governs it.


- `admit_typed(tool, ref, *extra) -> Optional[dict]`: the refusal dict, else `None`. It wraps `harvest_read.admit` (principal
  present, Opal user, served prefix; one audited refusal). Call it FIRST, before any S3 call.
- `audit_ok(tool, ref, nbytes) -> None`: the one audit row of a served call.
- `refusal(message, code) -> dict`: `{"error", "code", "guard_denied": True}`.
- `envelope(body, *, as_of, source_keys, denominator, absent_reason=None) -> dict`: returns
  `{"as_of", "source_keys", "denominator", "absent_reason", **body}`, projected to 50 KB.
- `project(out, limit=51200) -> dict`: when the JSON size exceeds `limit`, pops items off the end of the largest list
  field until it fits, sets `"truncated": True` and `"projected_to_bytes"`.
- `list_keys(prefix) -> list[{"key", "size", "last_modified"}]`: every page, no Delimiter, auto-paginated.
- `newest_part(prefix) -> Optional[str]`: for a prefix laid out `<prefix>date=YYYY-MM-DD/part-<stamp>.parquet`, the key
  with the greatest `(date partition, part file name)`; `None` when there is no `.parquet`.
- `read_parquet(key, columns=None, filters=None) -> (rows, total_rows, nbytes)`: columns projected at read; `filters` is
  a list of `(column, op, value)` with op in `=`, `<`, `>`, `in` (a string value is coerced to the column's date type).
- `read_json(key) -> (obj, nbytes)`: `.json` and `.json.gz`, capped.
- `TYPED_MAX_BYTES` (64 MiB): the cap on one object read; over it, `harvest_over_cap`.

**Rules of the seam.** A tool module NEVER imports `get_current_principal` or boto3: it reaches S3 and the principal only
through `harvest_typed`, so one probe patch point (`app.harvest_read.get_current_principal`) governs every tool. Each tool
is a TOP-LEVEL function in your module with exactly the tool's name and the inputs below, returns a dict, and every success
carries `as_of`, `source_keys`, `denominator` and `absent_reason` through `envelope(...)`. A key you were asked about that is
absent returns an empty body with `absent_reason` set (a string naming WHY), never an error and never silence.

2. **Behaviour you must get right.**
   - `read_parquet` reads the object once through `harvest_read._client()`, capped at `TYPED_MAX_BYTES` on the read itself
     (`body = obj["Body"].read(TYPED_MAX_BYTES + 1)`; over it raises the module's own over-cap exception that the callers
     turn into `refusal(..., "harvest_over_cap")`), then `pq.read_table(BytesIO(body), columns=columns)`, applies `filters`
     with `pyarrow.compute` (a string value compared to a date column is parsed with `datetime.date.fromisoformat`; `in`
     takes a list), and returns python rows (`json.loads(json.dumps(rows, default=str))`) plus the object's total row count
     before filtering and the byte count. An unknown column name raises `ValueError("unknown column: <name>")`.
   - `newest_part` lists with `list_keys` and compares `(key.split("/")[-2], key.split("/")[-1])` among keys ending
     `.parquet`; it is a pure function of the listing (no cache).
   - `project` never mutates its argument and never drops `as_of`, `source_keys`, `denominator` or `absent_reason`.
   - `admit_typed` is `harvest_read.admit(tool, ref, *extra)` and nothing else.
3. **Tests,** `infra/aws/ec2/opal-gateway/tests/test_og_gt0.py`, S3 replaced by a recording fake client (monkeypatch
   `harvest_read._client`), a principal stand-in patched at `harvest_read.get_current_principal`:
   - `test_oggt0_ac01`: `envelope` returns the four keys beside a non-empty body (`absent_reason` may be `None` then);
     `envelope({}, ...)` with `absent_reason` falsy raises `ValueError` (an empty body must say why), and with a non-empty
     `absent_reason` string it returns the four keys and no more.
   - `test_oggt0_ac02`: a 200 KB list field is projected to at most 51,200 bytes of JSON, `truncated` is True, the four
     envelope keys survive, and the input object is unchanged.
   - `test_oggt0_ac03`: over a fake listing of `p/date=2026-10-07/part-20261008T010000Z.parquet`,
     `p/date=2026-10-08/part-20261009T100000Z.parquet` and `p/date=2026-10-08/part-20261009T103423Z.parquet`, `newest_part("p/")`
     is the last of the three; an empty listing returns `None`; a listing with only `.json` keys returns `None`.
   - `test_oggt0_ac04`: a non-Opal principal and an absent principal are refused by `admit_typed` with the codes of
     `harvest_read` and ZERO recorded S3 calls; an off-list prefix is refused `harvest_prefix_not_served` with zero calls.
   - `test_oggt0_ac05`: `read_parquet` on an in-memory Parquet of three columns returns only the two requested, honours an
     `=` filter, a `>` filter on a date column given as `"2026-10-08"` and an `in` filter, raises `ValueError` on an unknown
     column, and an over-cap body (cap patched to 100 bytes) is refused with `harvest_over_cap`.
4. **The live probe** is the issuer's check (AC2): `newest_part("amgt/harvest/gold/chatter_daily/")` against the real bucket
   must equal the newest part an independent listing finds, and the listing must hold more than one part. Run the same
   call yourself first (`cd infra/aws/ec2/opal-gateway && python -c "from app import harvest_typed as t; print(t.newest_part('amgt/harvest/gold/chatter_daily/'))"`,
   with `INTERNAL_READER_ROLE_ARN` unset so the box's own credentials read). If the import fails outside pytest for lack of an
   environment variable, name the variable in a BLOCKING row; do not stub the import.

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
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/harvest_read.py
infra/aws/ec2/opal-gateway/tests/test_og_gt0.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~71/`. Rows: id `NFRA_OPLGTW-Z-W71-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-0"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt0.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-0"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt0.AC2.sh; echo "exit=$?"</invocation><expect>(?s)newest chatter_daily part: tool \S+; independent \S+; equal=True; parts listed (?:[2-9]|\d{2,}).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the base is built, refuses non-Opal before any S3 call, and the envelope, projection, newest-part and Parquet reads behave as specified.
- `AC2`: the newest-part rule agrees with an independent listing of the real chatter_daily prefix (the seam probe against the real neighbour).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-0.typed-tool-base.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the tool registrations and the pinned-count moves you expect
the issuer to make at the merge.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-TYPED (decomposition addendum R3-T.50 @d9371ffe81; PRD v3.0 ADMITTED: ratified-text SIGNED by
  3.0.0_SA_CVO~Z, brief SIGNED by 4.0.0_SA_CRO~Z, `prd-signoff.py status` read at the cut). CTO msgs 34077 and 34083.
- The release this cell rides: `NFRA_OPLGTW.TO-OG-ap-18`; its grant is `NFRA_OPLGTW.TO-OG-hv-2` (A5).
- The issuer registers the tools and re-pins counts at the merge (CUT BY WRITE SET: hookups belong to no cell).
- Pre-cut: AC1 and AC2 base FAIL as expected (module, tests and probe absent).
- Wave 1: this cell spawns first. gt-1..gt-5 are staged behind its merge (their worktrees branch from the merge).

- A1 (issuer, 2026-10-14 ~13:5xZ, before the spawn): `test_oggt0_ac01` contradicted itself (an empty body both allowed and
  raising). The face now says: a non-empty body may carry `absent_reason=None`; an empty body must carry a reason. No
  criterion moves. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>complete</status>
<round>37</round>
<workstream>G1-TYPED</workstream>
<slot>~71</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
