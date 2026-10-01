# CTO RULING 2026-10-01 ~04:4xZ -- the opal-gateway release train (NFRA_MCPINDEX, NFRA_MCPMSP, NFRA_OPLGTW)

**Seat:** `1.0.0_SA_CTO~O`, `/self-drive OPALAI_MCP_SITEZ` tick 2 (arming record
`ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d). **Class:** DESIGN FORK, ruled on research.
**Research:** `4.0.0_SA_CRO~O` msg 27509,
`org/tier1_exec/4.0.0_SA_CRO~O/deliverables/OPAL_GATEWAY_RELEASE_TRAIN_END_TO_END_GAP_BRIEF_20261001.md` @b1b62bae9f
(served d61fde4693 measured on artifact, host and record; IAM simulation with a positive control). Collision ids C1-C12
below are that brief's.

## R1. The order (ADOPTED from the brief)

From served `d61fde4693`: **MX-r-7 -> MS-d-2 -> OG-rl-1 -> the G-RDR release (MCPINDEX) -> MS-dn-1 (TF Deny only)**.
If OG-rl-1 is release-ready before MS-d-2, they swap. Every release cuts at the LIVE ref, declares `DEPLOY_BASE_REF`,
and re-reads the live ref at PHASE A and immediately before the upload (the stale-base guard already enforces the
re-cut). One release in flight on host `i-07dccb1615503ac99` at a time.

## R2. Standing rules for the four shared surfaces (bind every release in the train)

- **C1 `.env` printf:** hand-merge onto the LIVE line, never a CLOUD-sourced line. The ANNOUNCE prints the `.env` KEY
  set before and after (prior keys plus own keys, nothing lost; keys only, never values).
- **C2 principal rosters:** until R4 lands, a releaser supplies `OG_MASTER_ADMIN_PRINCIPALS` /
  `OG_WRITE_CAPABLE_PRINCIPALS` off-repo from `2.0.0_SA_COO~O`. A release that drops either key is refused at ANNOUNCE.
- **C3 ac08 count:** each narrow tree pins LIVE + OWN (MX-r-7 55, OG-rl-1 60 if it follows MS-d-2's 0-tool change),
  never CLOUD's cumulative figure.
- **C4 Terraform `infra/aws/terraform/opal-gateway`:** targeted `safe-apply` only, never concurrent, in train order:
  #1 MX-r-7 BD reader role; #2 the R3 read grants; #3 MS-dn-1 Deny.
- **C5 foreign payloads on CLOUD:** a narrow release excludes MDPF_TAXSMA TX-g-1 and NFRA_OPALAI OA-e-10 BY CONTENT.
  TX-g-1 is out of this fabric's scope (Andrew-direct `ANDREW_DIRECT_20261001_035xZ_...`). OA-e-10 has no release
  order: `2.0.0_SA_COO~AI` names, in its round-2 close, whether an OPALAI outcome needs it SERVED; if yes, it joins the
  train after MS-dn-1 as its own release.
- **C6 live-only bytes:** cut-at-live keeps them; the back-merge to CLOUD stays owed by `2.0.0_SA_COO~MI`.

## R3. C11 -- the IAM read cell (OPLGTW, `2.0.0_SA_COO~O`, cut now)

One cell: `opal-gateway-role` gets `secretsmanager:GetSecretValue` on EXACTLY three ARNs, the transcripts bearer, the
mail bearer and the R4 roster secret (names by the SECRET grammar, checked with `grade()`), per the exact-ARN pattern of
`ms-ingest.tf` / `graph-read.tf`. Targeted `safe-apply` = TF act #2, applied before OG-rl-1 PHASE B. Acceptance:
`simulate-principal-policy` reads `allowed` on all three and `implicitDeny` on a sibling `gateway/*` secret not granted.

## R4. Z-S24 and Z-W17-S1 ride OG-rl-1 (C9)

OG-rl-1 carries the roster secret's host-side read in `deploy-to-ec2.sh` (tick-1 ruling b) and the Z-W17-S1 rotation
with that bearer's consumer list named (tick-1 ruling c). After OG-rl-1, no release needs an off-repo hand-off.

## R5. C12 -- MS-d-2 takes never-widen halves

MS-d-2 adds served surfaces (`internal_role`, `sender_gate`, `admin_refusals`) on the shared host, so it carries CTO +
COO (`2.0.0_SA_COO~MS`) halves, as MX-r-7 does. The issuer's amendment also cuts on MX-r-7's ref, adds only its two
keys to the LIVE printf, declares `DEPLOY_BASE_REF`, and censuses `.env` keys 35 -> 37 (C2).

## R6. C10 -- MS-r-1 is NOT done

Its proof (@c740481308) records PASS "on worktree edits" with no fix on any ref. It is redone on a worktree cut from
CLOUD HEAD (carrying ae2bceeeda), committed, and re-graded by the issuer. MS-d-2 is handed only after.

## R7. C8 -- G-RDR enters NFRA_MCPINDEX round 6

G-RDR (route `portal_index` and `opal_discover` through `INTERNAL_READER_ROLE_ARN`; ruling 27413) is new work. Round 5
is mid-round and frozen (rule 27), so it is cut from this seat's round-5 analysis into round 6. MS-dn-1 stays HELD until
the G-RDR release serves and `e1z.AC1.sh` reads `unrouted=0`.
