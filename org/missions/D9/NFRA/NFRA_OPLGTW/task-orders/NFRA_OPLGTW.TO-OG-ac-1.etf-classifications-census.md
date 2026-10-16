# NFRA_OPLGTW task order -- `OG-ac-1` -- census the DynamoDB etf-classifications table and specify its gateway tool and grant (the named next increment, CTO ruling @d97ea3ae82 section 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ac-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ac-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~113</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census and a written spec; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes NO IAM. It proposes one grant in a spec file; the grant is a later order with three signed halves. The census uses the box's own read credentials, `dynamodb:DescribeTable` and a bounded `Scan` with a `Select=COUNT`/projection of key and metadata attributes only (below).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling @d97ea3ae82 section 2 (the etf-classifications table is the NAMED NEXT INCREMENT of NFRA_OPLGTW, owner `2.0.0_SA_COO~O`) and the CRO's G4 spec section 3.3.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ac-1` (decomposition addendum R3-T.81, workstream CLASS-INCREMENT, FWD-22)

The DynamoDB table `etf-classifications` (us-east-1) is the canonical security-classification table (`org/standards/MDPF_SECCLASS_CONTRACT.json`; the CRO's G4 spec `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md` section 3.3, proposed tool `mdpf_get_security_classification`). No group censused it, and the gateway role's read is `implicitDeny` (simulated). Census it READ ONLY, then write the spec of the tool and of the one grant it needs.

1. **Census** -> `W/ETF_CLASS_CENSUS.json`, a flat object. Each of these keys holds `{"value": <v>, "claim": "measured|inferred|absent"}` (`measured` = read from the live table this run; `inferred` = derived from measured values, say from which; `absent` = could not be read, say why): `table_name`, `table_arn`, `item_count` (an integer: `describe-table` ItemCount is a six-hourly estimate, so ALSO count with one paginated `Select=COUNT` scan and record both, naming which is the value), `key_schema` (hash and range attribute names), `attribute_names` (the union of attribute names over a bounded sample of at most 200 items, names only), `classified_by_counts` (a dict of integer counts per `classified_by` value over the same bounded sample, or the full count if the table is small), `freshness_field` (the attribute that dates a row, or the string `none` with the claim `absent`) and `newest_date` (the newest value of that field, a date string). Read with `dynamodb:DescribeTable` and `Scan` only. Print and store NO item content: names, counts and one date only. Do not write to the table.
2. **Spec** -> `W/ETF_CLASS_SPEC.md` with exactly these three level-2 headings:
   - `## Tool`: the tool `mdpf_get_security_classification` (from the CRO spec): inputs, the envelope it answers (`as_of`, `source_keys`, `denominator`, `absent_reason`, the row fields the contract names), Opal principals only, 50 KB projection, the freshness it states, and how it reads the table by the key the census found (a `GetItem`/`Query` by security key, never a scan).
   - `## Grant`: the ONE IAM statement the tool needs on the gateway role: Effect Allow, Action `dynamodb:GetItem` and `dynamodb:Query` (state which), Resource the table ARN you measured (and an index ARN only if the key schema needs one); say plainly what it newly lets the gateway read and that it can read no other table. Name NO write action, no `Scan`, no wildcard resource.
   - `## Refused`: the arms the tool must refuse with zero reads (a non-Opal or absent principal, a missing key, a key over the length cap).
3. Write nothing else. The build and the grant are later orders.

## 2. BOUNDS

- Read only: `DescribeTable` and a bounded `Scan` (a `Select=COUNT` scan, and one projection-limited sample scan of at most 200 items for attribute and `classified_by` names). No `GetItem` of a row's content into any file, no write to any table, no IAM or Terraform change, no code in `infra/`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print or store a security's classification content, a person's name or an account number; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/ETF_CLASS_CENSUS.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/ETF_CLASS_SPEC.md
org/standards/MDPF_SECCLASS_CONTRACT.json
org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_DATA_CONTRACTS_20261014/G4_mdpf_delta.md
infra/aws/ec2/opal-gateway/app/portal_json_served.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/`. You WRITE only the two files under `W/` named above and the investigation file (append rows); the rest you only READ. Rows: id `NFRA_OPLGTW-Z-W113-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ac-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ac1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)census: fields 8 of 8; claim words ok True; item_count/attributes/classified_by shaped True; spec sections True; grant names read action and the table arn True; grant carries no write or scan action True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the census holds the eight measured fields with their claim words, and the spec has the three sections, the grant names a read action and the measured ARN and no write or scan action.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ac-1.etf-classifications-census.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if AC1 PASSES, and report once (commit hash, the AC1 line, the item count, the key schema, the freshness field and its newest date, the `classified_by` counts).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream CLASS-INCREMENT (decomposition addendum R3-T.81). Outside the 22:00Z line by the CTO's ruling (the grant is a never-widen ask with three halves and a census); this cell is the census and the spec so the next increment starts from measurement, in parallel with the OG-ap-23 release (disjoint: no code, no IAM).
- After it: a build cell (the tool) and a grant order to `0.7.0_AE_CloudOps~ZS`, cut from the spec.
- Pre-cut: ac1.AC1 base FAIL as expected (census and spec absent).

<status>complete</status>
<round>37</round>
<workstream>CLASS-INCREMENT</workstream>
<slot>~113</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
