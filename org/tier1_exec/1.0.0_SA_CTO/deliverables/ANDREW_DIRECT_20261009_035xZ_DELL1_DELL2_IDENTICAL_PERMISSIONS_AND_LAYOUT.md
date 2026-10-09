# ANDREW_DIRECT 2026-10-09 ~03:5xZ -- DELL1 and DELL2 carry the exact same permissions and layout; each deploys for itself

**Channel:** laptop terminal, to 1.0.0_SA_CTO. **Recorded by:** 1.0.0_SA_CTO, same turn.

## Andrew's words, verbatim

> "DELL1 and DELL2 should have the exact same permissions and layout. If DELL2 can deploy on its own and work with access and permissions
> on its own, then DELL1 should be able to do so as well. i bring this up because I see DELL1 is making requests to MSTR~Z to have CloudOps
> agents set up on sitez to handle DELL1 deploys which is needless; DELL1 should be able to handle its own needs on its own box."

## The CTO's ruling

1. **One permission set for both Dells.** Every grant that tonight reached one Dell user alone moves to the `dell_agents` group, or is
   mirrored, so `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` hold the same effective permissions. Known per-user grants:
   - dell2's `dell2_ssm` policy (the resident-host documents, and the standing shell-script document of AMENDMENT 24);
   - the transcripts-key `kms:GenerateDataKey` of AMENDMENT 25, which was ruled dell2-only at ~03:4xZ and is now **both Dells**;
   - any other per-user statement the census finds.
   The amendment cell **measures** this, never lists it by hand: one simulation of both users over the same action and resource census
   must print identical results. That equality is the cell's acceptance; a difference is a defect to fix, or a named exception Andrew
   gives.
2. **Each Dell deploys through its own `0.7.0_AE_CloudOps~<box>`, on its own box** (his ~22:0xZ word, re-stated tonight). No Dell's
   deploy is routed to site Z or to the laptop. dell1's request to 0.0.0_AB_MSTR~Z for a site-Z CloudOps seat is withdrawn. Where
   dell1 met a refusal that sent it there, that refusal is the input to item 1, named by dell1.
3. **Same layout:** each Dell runs the same seat set, a fabric manager (`0.0.0_AB_MSTR~DELL<n>`), a CTO, its COO lanes, and its own
   CloudOps seat. Where one Dell lacks a seat the other has, its MSTR seats it.
4. **What stays the same:** the step-C before-rule (tell the laptop before changing shared resources: firm buckets, the state bucket,
   shared keys, protected functions), after-the-fact send and IAM reports, and the denies on IAM users, access keys, login and MFA.

## Blast radius (the CTO half), in plain words

dell1 gains what dell2 has: shell scripts on the resident host and the route hosts, the resident-host documents, and writing encrypted
transcript files. Trail: every send and IAM change is reported after the fact by bus. Both branches: A, the plan changes only the policies
and attachments named, and the two-user simulation is equal, so apply. B, anything else, or any inequality, means apply nothing and
report. Rollback: re-apply at the amendment's parent commit.

**SIGNED (CTO half)** -- `1.0.0_SA_CTO`

## Addendum ~05:3xZ -- AMENDMENT 27, shell on mdpf-daily-runner (row NFRA_CTLPLN-W14-S48, 2.0.0_SA_COO~C msg 107749)

Measured by the issuer: parity reads 1532/1532 equal; A26-A28 built and VALID, nothing applied. A27 gives both Dells standing
`AWS-RunShellScript` on `mdpf-daily-runner` (`i-02448edb624a7a7cf`) for dell2's IB-pr-383. A shell there runs as
`mdpf-daily-runner-ec2-role`, which the directory runner uses to assume the 49 Financial source principal
(`principal_49f.tf:1-12`), so the blast radius is wider than this half named.

**RULED: YES, A27 applies with A26 and A28,** on Andrew's word that the Dells run their own scripts inside Opal's AWS without waiting on the
laptop. Plain words: a Dell seat on that host can act with 49 Financial's source credentials, as the daily runner does.
**Conditions:**
1. The step-C before-rule is restated in the apply order. A send that writes a firm data bucket, or assumes the 49F principal for anything
   other than the runner's own documented job, tells the laptop first.
2. Every send to that host is reported after the fact by bus (command id, purpose).
3. CLAUDE.md's cross-firm rule binds the scripts run there: never write 49 Financial data into another firm's tree.

**SIGNED (addendum)** -- `1.0.0_SA_CTO`


## Condition (4) answer 2026-10-09 ~14:3xZ -- MDPF_STRATID.TO-APPLY-W2-a read grant (dell1)

On `0.0.0_AB_MSTR` msg 107994 (relay of dell1 `0.7.0_AE_CloudOps~DELL1` msgs 2542/2543, before the act): **OK.** One statement on each of
two roles, the MDPF daily runner's role and `mdpf-gold-lambda`'s execution role: `s3:GetObject` on
`arn:aws:s3:::opal-data-etfs/config/etf_universe.json` and nothing else (no wildcard, no List, no Put). The object is Opal's own ETF list,
not a firm's data, so the cross-firm rule is untouched. Applied through Terraform (`safe-apply`), read back live with a positive control
(the key reads allowed) and a negative control (a sibling key still reads implicitDeny), reported after the fact by bus.

**SIGNED (condition 4)** -- `1.0.0_SA_CTO`
