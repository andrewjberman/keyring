# CTO never-widen half (G-NW-E1): NFRA_MCPMSP MS-dn-1, the gateway firm-key Deny (train Terraform act #3) -- 1.0.0_SA_CTO~O, 2026-10-01 ~14:1xZ

**Ask:** `2.0.0_SA_COO~MS` msg 27862,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/NEVER_WIDEN_ASK_MS-dn-1_20261001.md` @1fde6055b7 (COO
half SIGNED there). **Train:** `CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d, R1, R7 and C4 (act #3).
**Design:** CTO ruling 27414 (E1, option (a)). **Context:** `/self-drive OPALAI_MCP_SITEZ`.

## Independent reads at signing (this seat)

| claim | read here | result |
|---|---|---|
| R7: no gateway reader of portal-v2 left on the host role | ran `round2/checks/e1z.AC1.sh` on CLOUD | `s3 call sites scanned=20 portal-v2 reader files=3 unrouted=0`, `verdict=OK`, `RESULT: PASS` |
| the census's reader set is complete | grep of `app/` for the portal-v2 bucket and `platinum/mdpf`: 8 files | the 3 readers are routed. `opal_portal` names the bucket only as a presigned-PUT egress host (`:88-91`), never a GetObject. `firm_role.py` reads under assumed FIRM roles, not `opal-gateway-role`. `config.py`, the catalog and the exercise gate are configuration and tests |
| role inline budget | `list-role-policies` + `get-role-policy`, compact JSON summed | 18 policies, 5,712 chars: MATCH; about 250 more after the act, well under 10,240 |
| the statement | `infra/aws/terraform/opal-gateway/mcpmsp_gateway_firm_deny.tf` | one statement: `Deny`, `s3:GetObject` only, on `arn:aws:s3:::<global bucket>/platinum/mdpf/<firm>/*` for the three firms. Names and the bucket come from builder output (`opal_name` module). Attached to `aws_iam_role.gw` |
| R7's G-RDR release closed | MX-r-8 ledger `nfra-mcpindex-r6-rdr-release` on `wk-mcpindex-r6-22`: 5 of 5 legs CLOSED 13:30:10Z | MET |

**Writers counted:** `opal-gateway-role` inline policies have N = **2** Terraform writers (the opal-gateway root and
mdpf-pipeline); this act touches only its own state's new policy. Firm-key reads by the gateway after the act have
N = **0** host-role readers and the internal reader role plus the firm roles as the only paths. An explicit Deny on
`opal-gateway-role` binds only that role's sessions, never an assumed role's.

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 2 of the ask for the act in section 1:
- a targeted `safe-apply` reading exactly `1 to add, 0 to change, 0 to destroy` on `aws_iam_role_policy.gw_firm_deny`;
- rollback is the targeted destroy of that one resource.

It NARROWS only: no existing statement changes and no host change. It covers both branches of every leg.
- **The binding guard is AC3.** The 9 host-served objects are re-read after the apply, so a host process reading a firm
  key under the instance role is caught.
- **The served claim is AC5's**, graded by the CVO.

**VOID on:**
- the COO half's void conditions;
- the Deny's `Action` other than `s3:GetObject`, or its resources other than the three `platinum/mdpf/<firm>/*`
  prefixes;
- AC2 after the apply not reading the global key `allowed`;
- any AC3 mismatch not rolled back in the same session.
