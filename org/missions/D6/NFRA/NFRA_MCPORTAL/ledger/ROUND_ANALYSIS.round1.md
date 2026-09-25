# NFRA_MCPORTAL -- ROUND 1 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-09-25 ~05:0xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 25866, `REMEDIATION_v1.Z.md` @5336862b71, `ADJUDICATION_v1.Z.md` same commit),
and on `2.0.0_SA_COO~O`'s drain-end read (msg 25860) and real run (`deliverables/2.0.0_SA_COO~O/round1/real_run/RESULT.md`
@c24f9788e9). All three were read to the end. The grade tokens are `REALIZED | NOT_REALIZED | DEFERRED | HELD`. The
recut is `2.0.0_SA_COO~O`'s, in ONE issuance.

---

## 1. L7, L8 and L9 accepted

- **L7:** 7 of 7 orders are terminal. MP-w-1, t-1, t-2, t-4 and t-5 are complete; MP-t-3 and t-6 were superseded under
  ruling R-1. The CVO re-ran 6 of 6 instances VALID.
- **L8:** 9 of 9 investigation rows are dispositioned (5 graduated, 4 dismissed with reason), and the CVO added two
  findings, C-S10 and C-S11. The slug carries 7 rows: 1 REMEDIATED and 6 OPEN.
- **L9:** this round had no judgment criteria, and none were self-graded.
- **Adopted as the round's most useful act:** the CVO's C-S10. It found a premise under round 2's first cell that
  nobody had measured. C4's owner check keys on the ALB header's `oid` claim, with a replay window on `iat`, and every
  test planted both claims itself. The CVO refused the premise instead of refusing the cell, which is the right grain.

## 2. Outcome grades

| FWD | grade | why |
|---|---|---|
| FWD-1 | NOT_REALIZED | The thread's local half is built: the shell, the owner gate, the grant writer's code and the Entitlements tab. The served half is not: the writer cannot run as packaged (W3-S3), and nothing is deployed. |
| FWD-2 | NOT_REALIZED | The owner gate is built and merged (MP-t-1). It is not deployed, so no signed-in colleague has been refused LIVE. |
| FWD-4 | DEFERRED | Audit rows exist per principal. The dashboard-wide history needs a cross-principal feed (W2-S1, s.3 R-4). |
| FWD-3, 5, 6, 7, 8, 9, 11, 12, 13 | DEFERRED | These are enrichment rounds, in Andrew's page order, after FWD-1 is REALIZED. |
| FWD-10 | DEFERRED | The call log and the person and server stop use the kill switch, blocklist and revocation FILES (C6 keeps those files). It does not wait on G-OPLGTW. |

## 3. Rulings on the open rows

**R-2, on C-S10 (ARMED): measure first, and both branches are ruled now, so the measurement picks and nobody waits.**

Background: the ALB fills `x-amzn-oidc-data` from its configured userinfo endpoint
(`graph.microsoft.com/oidc/userinfo`, scope `openid profile email`). Microsoft's userinfo response is documented to
carry `sub`, `name`, `family_name`, `given_name`, `picture` and `email`, and not `oid`. The ALB adds its own `exp`, `iss`
and `signer`. So both claims C4 leans on may be absent. This is not a finding: the cell measures it.

- **The measurement, round 2's first cell:** one real `x-amzn-oidc-data` header from Andrew's own ALB-authenticated
  request. Record its claim KEYS, with values redacted except the owner key, which becomes the writer's configuration.
- **If `oid` is present:** no change.
- **If `oid` is absent:**
  - The owner key is `sub`. It is pairwise, meaning stable for this app and this user and not derivable by another
    app, and the ALB signs it.
  - The writer's owner configuration is Andrew's measured `sub`. W3-S2's oid is not used by the writer.
  - C4's words "Andrew's Entra object id" become "Andrew's subject identifier as the ALB-signed header carries it". That
    is a CONTRACTS wording addendum, and the ENDPOINT is unchanged. `3.0.0_SA_CVO~O` signs the reworded half once.
- **If `iat` is present:** no change.
- **If `iat` is absent:**
  - The freshness bound is the ALB-signed `exp`. The writer refuses an expired header.
  - The named residual in C4 widens from "a short window" to "the header's own lifetime". It remains visible through
    the writer's own audit record, and it is stated in the addendum. The replay route still needs a compromised gateway.
- **Fails closed either way:** if neither `oid` nor `sub` is present, the writer refuses every write, and the dashboard
  says why. No owner key is invented.

**R-3, on W3-S3 (ARMED): the staged build, R-1 as written, plus the CVO's added requirement.** The in-zip proof also
RUNS the handler on one refusal (a write with no owner header) from inside the built package. The refusal arm is the
one that must work before any grant is written.

**R-4, on W2-S1 (FWD-4's feed): the writer's OWN record is the feed.**
- The dashboard's history reads a record that only the grant writer writes: its own table, named by
  `lib/opal_naming.py name()` (Rule 30), append-only, one item per write or refusal. The writer's IAM grants
  PutItem-only on it, and the gateway's grants read-only.
- It is the same record C4's residual already relies on. One record serves both, so there is no second audit.
- **Why not an index on `operator_audit`:** that table and its record types are NFRA_OPLGTW's contract, and adding
  an index meets G-OPLGTW. **Why not the writer's log group:** a history page that queries logs is slow and
  unstructured.

**R-5, on C-S11:** accepted as the COO wrote it. The typed client refuses a non-JSON response by content type and shows
a plain reason. Its test plants an HTML 200.

**R-6, on W1-S1 (ARMED, disarm owner `1.0.0_SA_CTO`): not the recut's.** It is a fabric-tool gap:
`owned-paths-validate` refuses a worker's task-order-granted brand-new path as UNDEFINED before it reads the grant.
NFRA_OPALAI's row Z-W1-S1 is the same defect. The fix is this seat's own act, outside the round. It touches
`.tools/owned-paths-validate.py` and carries the row's two-arm control. It is recorded separately, and it binds no
cell.

**W3-S2 (INERT):** it follows R-2. The oid carries into the writer's configuration only if the header proves to carry
`oid`.

## 4. THE ENRICHMENT LIST ROUND 2 CUTS

It is cut in order, with dependencies stated. A build order carries at most three mechanical criteria.

1. **E1, measure the header** (R-2). WORLD read-only. It produces the claim-key record and the owner key. **E3's
   configuration waits on it.**
2. **E2, the staged build** (R-1, R-3). The in-zip import and the in-zip refusal run.
3. **E3, MP-t-3 re-cut: the writer's apply.** It covers the one `lambda:InvokeFunction` grant, the writer's own table
   (R-4), the owner configuration from E1, and a change-ledger entry naming the blast radius (C10). If E1 lands on a
   "claim absent" branch, the C4 wording addendum is signed before E3's apply.
4. **E4, MP-t-6 re-cut: the gateway serves the dashboard and handlers.** It is a NARROW gateway release, the same shape
   as NFRA_OPALAI's ruling @592e319a06: cut at the deployed `f1f0fc6780`, plus ONLY NFRA_MCPORTAL's gateway commits.
   The five foreign commits stay out.
5. **E5, the non-JSON refusal** (R-5).
6. **E6, the cross-principal history** (R-4), which reads the writer's table.
7. **Close run: FWD-1 LIVE.** Andrew narrows one colleague's data grant from the dashboard; the colleague's next MCP
   call is answered within the new limit; it is widened back; both writes show in the history. Plus A1n's negative
   arms, run LIVE.

**Subtracted from round 2, with the reason for each:**
- the remaining pages (FWD-3, 5-9, 11-13): they follow FWD-1 in Andrew's order;
- S6 (tiers and tool lists into the table): G-OPLGTW, Andrew's word;
- W1-S1: this seat's own act (R-6).

## 5. What this analysis does not do

- It does not measure the header. E1 does, and every C4 sentence above that depends on it is conditional.
- It does not change the ENDPOINT. A C4 wording addendum, if E1 triggers one, is CONTRACTS only.
- It does not touch NFRA_OPLGTW's store, contract or record types.
