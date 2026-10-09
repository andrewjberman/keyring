# NFRA_MCPINDEX task order -- `MX-g-3` -- G-RDR: portal_index and opal_discover read portal-v2 through the Opal-internal reader role

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-g-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-g-3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~22</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change; the role gateway-global-internal-reader-role is live (NFRA_MCPMSP drain e719b4e6ad; trust opal-gateway-role only; GetObject on json/* and platinum/*).
comp-adversary: DECLARED-NOT-APPLICABLE -- the query_v0 routing pattern (app/query_v0.py:98-104) applied to two more readers.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (STS assume + S3 reads, unchanged in kind).
</preflight>

## 1. THE CELL -- `MX-g-3` (round 6; `ROUND_ANALYSIS.round5.md` @1edec80f63 section 5 item 2; CTO ruling msg 27413/27414; release-train ruling R7)

**Start after MX-d-6 is complete and drained. The issuer continues you with this order.**

**Today, measured at the round-6 base:**
- `app/internal_role.py` `s3_client()` (:51-71) reads env `INTERNAL_READER_ROLE_ARN`.
  - Unset: it returns `None`.
  - Set: it assumes the role (session `gw-internal-reader`), caches the client, and raises `InternalRoleUnavailable`
    on failure with NO fallback.
- Its only caller is `app/query_v0.py:98-104`, which falls back to `boto3.client("s3")` when it returns `None`.
- Two portal-v2 readers bypass it:
  - `app/integrations/portal_index/integration.py:266-273` `s3_getter()` builds `boto3.client("s3")` at :273;
  - `app/integrations/opal_discover/integration.py:220-231` `_s3_head()` builds `boto3.client("s3", config=...)` at
    :228.
- NFRA_MCPMSP's reader census (`e1z.AC1.sh`) reads `unrouted=2` (those two files).

**The act:**
1. Route both readers through `internal_role.s3_client()` on the query_v0 pattern:
   - when it returns a client, use it;
   - when it returns `None` (ARN unset), keep today's default client;
   - when it raises `InternalRoleUnavailable`, fail CLOSED with the integration's own error shape. Never silently fall
     back to the instance role.
   - Keep `_s3_head()`'s `Config` (timeouts) when building or wrapping the client.
2. New test file `infra/aws/ec2/opal-gateway/tests/test_internal_role_routing.py` with exactly these named tests:
   - `test_portal_index_reads_through_internal_role`;
   - `test_opal_discover_heads_through_internal_role`;
   - `test_unset_arn_keeps_default_client`.
   Monkeypatch `internal_role.s3_client` and `boto3.client`; make no network call.
3. Do NOT edit `app/internal_role.py` (NFRA_MCPMSP's) or `query_v0.py`.

## 2. BOUNDS

1. No role, policy, grant or `.env` change. The ARN reaches the host `.env` through NFRA_MCPMSP's MS-d-2 (train slot 2),
   never through this cell.
2. Behaviour with the ARN unset is byte-equal in effect to today's. Prove it with the third test.
3. Nothing under `data/cot/`. No push. No deploy (MX-r-8 releases this). REFUSE a criterion you cannot meet as written,
   and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/portal_index/integration.py
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/tests/test_internal_role_routing.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W22-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-g-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/g3.AC1.sh; echo "exit=$?"</invocation><expect>s3 call sites scanned>=1; portal-v2 reader files>=1; unrouted=0; verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-g-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round6/checks/g3.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 3 of 3; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~22/NFRA_MCPINDEX.TO-MX-g-3.rdr-internal-reader-routing.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order
beyond your status flip.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-6 item 2. G-RDR enters here from the CTO's round-5 analysis (train R7), not
mid-round. MS-dn-1 (NFRA_MCPMSP's Deny) stays HELD until the slot-4 release serves this and `e1z.AC1.sh` reads
`unrouted=0` on the served tree. Battery dry-run at base:
- g3.AC1 FAIL as expected (`unrouted=2`: opal_discover, portal_index);
- g3.AC2 FAIL as expected (test file absent).

<status>complete</status>
<round>6</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
