# CTO ruling (cluster lead) -- Andrew-direct 2026-10-13 ~13:1xZ: the Dell identities get the permissions their own projects need; three grants, identical on both dell agent users, one NFRA_CTLPLN cell under a pair; the laptop CloudOps seats ~ANL and ~FBL stand down when the grants are live

From 1.0.0_SA_CTO (laptop), 2026-10-13 ~13:2xZ. Andrew's word, VERBATIM (recorded by `4.0.0_SA_CRO` at its terminal,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_131xZ_DELL_BOXES_GET_THEIR_OWN_PERMISSIONS_NO_CROSSBOX_CLOUDOPS.md`
@3245d69502): "I do not want CloudOps agents from one box working on projects that are otherwise based on another box, because its
unnecessary separateion in 99% of cases. THis is why I ask if those are residue because I thought we have already moved past this
after giving the Dell Boxes the ability to handle their own resource.s" and, on the ask: "Yes you should send CTO this note, that
the Dell Boxes need the necessary permissions so this cross-box behavior is not necessary."

## What the CRO measured (not residue: each laptop order names a permission the Dell identity lacks)

| laptop seat | Dell project | the gap |
|---|---|---|
| `0.7.0_AE_CloudOps~ANL` | IRPT_ANLREQ (dell2) | `kms:Decrypt` on the IRPT key denied to dell2 (`IRPT_ANLREQ.TO-READS-Y10...md` line 41; crossbox 552a, e261) |
| `0.7.0_AE_CloudOps~FBL` | ADVI_FIRMBKTS (dell1) | the protected edge functions bound to the laptop identity (NFRA_CTLPLN round-3 ADDENDUM 7, cited in `TO-FB-f-19` line 14); "dell1's identity cannot simulate" (`TO-FB-f-21` line 77) |

## Ruling

1. THREE GRANTS, applied IDENTICALLY to both dell agent users (`cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`), so the
   standing rule "the dell agent users are identical" holds and no Dell-placed project routes work to a laptop seat:
   (a) `kms:Decrypt` (with the `kms:DescribeKey` it pairs with) on the IRPT key, scoped to that one key ARN;
   (b) `iam:SimulatePrincipalPolicy` (and `iam:GetContextKeysForPrincipalPolicy`), scoped to the roles the firm-bucket pairs
   simulate (the `irpt-*` and `*-inf-*` role ARNs the FB-f-21 pair named), never `*`;
   (c) admission to the protected edge functions `shared-advisor-router`, `shared-advisor-router-response`, `auth-validator-edge`
   at the same reach the laptop identity holds today (the ADDENDUM 7 binding reversed for the dell users, nothing else widened).
   This is a widening and runs under CLAUDE.md NEVER-1: one never-widen pair, CTO half `1.0.0_SA_CTO` (this seat), COO half
   `2.0.0_SA_COO~C`, applier `0.7.0_AE_CloudOps~U7` by `safe-apply`, never a console edit; the plan reads exactly the three
   statements added and nothing destroyed, or it stops.
2. OWNER: NFRA_CTLPLN (the Dell identity policy is its C-SEATS contract). `2.0.0_SA_COO~C` cuts it as the FIRST cell of the
   round-12 issuance (ahead of CT-aa-5/6), one build cell (the Terraform statements + the pair halves) then the staged apply.
   The cell reads two things before it writes: the managed policy on the dell users sits at 5 of 5 versions (site Z's OG-ap-13
   receipt, 108716) and the applier prunes the oldest non-default version first; and ADDENDUM 7's binding is reversed by editing
   the statement that carries it, read at its bytes, not by a new allow beside it.
3. READ-BACK, by the Dell seats themselves (the point of the word): dell2's CloudOps lane decrypts one IRPT-key object it could not
   read before (status only); dell1's CloudOps lane runs one `simulate-principal-policy` on an `irpt-*` role and reads a decision;
   dell1 invokes or describes one protected edge function with the dell identity and gets a non-AccessDenied answer. Three lines,
   codes and names only.
4. STAND-DOWN: when the three read-backs are recorded, `0.7.0_AE_CloudOps~ANL` and `0.7.0_AE_CloudOps~FBL` finish any order they
   hold (none may be left half-done: 0cab is closed; ~ANL's a827/7c76 run to their own terminal) and are stood down by
   `0.0.0_AB_MSTR`; the dell issuers re-address any later order of that class to their own CloudOps lanes. A Dell-placed project
   sending a CloudOps order to the laptop after that is a surprise row, not a route.
5. "Dell boxes should not be curtailed" (20:5xZ 10-12) and this word read together: the dell identities widen to what their
   projects need and narrow nowhere; the IAMROLES narrowing stays withdrawn (c404 addendum 1).

## Acts

- `2.0.0_SA_COO~C`: the round-12 first cell as above; the COO half; the staged order to ~U7.
- `0.0.0_AB_MSTR`: relay to ~DELL1 and ~DELL2 (the grants are coming; their CloudOps lanes own the read-backs; no new cross-box
  CloudOps order to the laptop from now); the stand-down of ~ANL/~FBL on the read-backs.
- No act for Andrew: the grants are Opal's own IAM, applied under the pair.

## SUPERSEDED IN SHAPE 2026-10-13 ~16:5xZ -- Andrew's word "Sure let's do rec b" (2.0.0_SA_COO~C @ff6d6d5fd7): both Dell users join AdministratorAccessOpalCapital with three deny classes kept; the grants above are served by the group membership; read-backs stand. Ruling: CTO_RULING_DELL_ADMIN_GROUP_SUPERSEDES_GRANTS_AND_S9112_PURGE_ROTATE_IF_EXISTS_NO_ACCOUNT_DISABLE_20261013.md
