# NFRA_OPALAI task order -- `OA-g-3` -- ADDENDUM A2: Alyssa Keith's portal-only grant, written through the operator path

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-g-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~9</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot grant write; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface is written or changed; the act runs under the EXISTING operator role opal-gateway-access-admin, which the command itself verifies by sts:GetCallerIdentity (it refuses any other caller); an identity you cannot assume is a BLOCKING row.
comp-adversary: DECLARED-NOT-APPLICABLE -- a narrow, named grant on Andrew's word.
EGRESS CLASS, declared: Opal's own AWS (one POLICY transaction) plus ONE read-only Microsoft directory lookup in Opal's own tenant, ledgered (Andrew-direct 2026-09-26: API egress permitted this session, every call ledgered by the seat that makes it).
</preflight>

## 1. THE CELL -- `OA-g-3` (decomposition ADDENDUM A2)

Spawned only after `OA-g-2` closed: the live gateway then parses a portal-only grant.

**The word (Andrew-direct 2026-09-26 ~02:2xZ, call 2):** "Alyssa Keith, scoped to portal figures only". The record is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_022xZ_CTO_O_OPEN_CALLS_1_TO_6_ANSWERED.md`. The CTO's
ruling (B) (msg 25996) adds: resolve her Entra oid from the directory by the operator path, without waiting for her to
sign in.

In order:
1. **Her identity.**
   - Do ONE read-only lookup of the user "Alyssa Keith" in Opal's Entra tenant (tid `6810043e-d171-4adc-9975-068b35e179da`),
     with an Opal operator credential you already hold.
   - It must match exactly ONE user. Zero or several matches: STOP, a BLOCKING row naming the count.
   - Ledger the call in `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/EGRESS_LEDGER.md`: the
     time, endpoint, purpose and match count.
   - Her oid goes ONLY into the candidate you pass to the operator command, never into a committed file, row or log line.
2. **The candidate.**
   - `portal_channels` = every channel of `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` that
     `catalog_gate` indexes and whose verdict is not `deny`. List the channel ids in your result;
   - `operations` = `["query"]`;
   - zero Schwab masters, accounts, datasets and columns;
   - a date mode the amended contract accepts.
   - Build it in a temp file outside the repo, and delete it after the act.
3. **The act.** Run `python infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py activate --candidate <tmp>
   --approver andrew@opalinvest.com --source-authorization <the record path above> --summary "Alyssa Keith: portal figures only (OA-g-3)"`
   under the operator AWS identity `opal-gateway-access-admin`.
   - Before activating, the command prints the scope diff. Record it in your result with the oid masked.
   - If you cannot assume that role: STOP, a BLOCKING row. Never use another identity.

## 2. BOUNDS

1. ONE principal's grant is written, through the operator command only. No other POLICY record changes, and no direct
   table write happens.
2. No identifier (tid, oid, email) goes into the repository or a row. The criteria print counts only.
3. Standing rule: no push. REFUSE a criterion you cannot meet as written, and report the refusal with its measurement.
   Never repair, widen or route around a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_OPALAI-Z-W9-S<k>`.

## 4. PROOF OF SPEC (literal; run from the workspace root after the act, with OA-g-1 drained to CLOUD)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-g-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g3.AC1.sh; echo "exit=$?"</invocation><expect>portal_only_active=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-g-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/g3.AC2.sh; echo "exit=$?"</invocation><expect>portal_only_active=1 operations=[['query']] -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~9/NFRA_OPALAI.TO-OA-g-3.alyssa-portal-grant.proof_of_spec.json`.
Report once, with:
- the match count;
- the egress ledger line;
- the channel ids;
- the masked scope diff;
- the revision written;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a direct act on Andrew's call 2 and the CTO's ruling (B). Dry-run at base: g3.AC1 and g3.AC2 FAIL
(134 items, 7 POLICY, 0 active profiles, 0 portal-only). Runbook step 6 (the colleague's live question) follows this
act.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~9</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
