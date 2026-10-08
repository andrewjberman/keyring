# CTO never-widen half -- NFRA_CTLPLN: the Dell group reads THREE named vendor secrets (one apply of the Dell identity root)

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~23:0xZ. **Counterpart read in full:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_VENDOR_SECRETS_20261007.md` @8ea4e0b9cb (92 lines), and
row `NFRA_CTLPLN-W14-S8`. **Not read by this seat:** the plan itself, the census file, the simulator's output, any secret's value.
**Authority:** Andrew-direct ~18:3xZ item 4, "Vendor egress does not count as raw internet access; those are protected channels.
The Dell Boxes have vendor egress as needed."

## What this half signs, and where it differs from the counterpart

The counterpart signs a grant of four secrets. **This half signs three: `astn/kimi/api-key`, `ycharts/login/credentials`,
`astn/brightdata/residential-proxy`. `openai-api-key` is NOT in the grant.** The two halves do not yet name the same act, so
nothing applies until the counterpart is amended to three and the plan is re-measured.

## The three points the counterpart asked this seat to weigh

1. **The OpenAI key stays out.** `org/ref/VENDOR_EGRESS_WHITELIST.yaml` VEW-2 scopes OpenAI to ETFS_RIVALS and says in so many
   words that it does not cover another project's use (as quoted in row W14-S8; this seat did not open the file). His word of
   18:3xZ is newer and says "as needed"; it did not strike that line, and need is not shown: the four MDPF_SECCLASS programs that
   name the key are older classifiers, and the classification run dell1 has on the laptop tonight reads the Kimi key, not this
   one (`0.7.0_AE_CloudOps~SC` msg 106583: one secret read, no model call). A read cannot be undone short of rotating the key,
   so the side that can be reversed is leaving it out. It enters by condition 6 when a Dell order names an OpenAI call, on the
   whitelist line as it then stands.
2. **"A key once read stays read" is accepted for the three.** Each is a vendor the Dells' placed work calls today or is cut to
   call: Kimi (VEW-3, scope any), YCharts (the report generator, dell2), Bright Data (the proxy the custodian and YCharts
   sign-ins use). That is what "as needed" grants. Rotation at the vendor is the only full rollback and is named as such.
3. **Writes are out of this act and are not left as they are by this seat's silence.** Both Dell users may already write any
   secret's value under the create policy. That is wider than his words ("they should be allowed to create resources"; nothing
   said about overwriting a credential). It is not changed here, because this act is a read grant. It is a cell input to
   `2.0.0_SA_COO~C`: narrow `PutSecretValue` for the Dell group to secrets a Dell created, measured first.

## Blast radius

Two IAM objects in root `infra/aws/terraform/nfra-ctlpln-identity/`. Changed: what the two Dell users may read, by three exact
ARNs, one action. Not changed: any other principal; any key policy (the counterpart reads all under the account's default key);
any secret's value; what a pipeline host or function reads under its own role.

## Expected outcome, BOTH branches

- **A:** the plan reads exactly two creations, the statement naming exactly the three ARNs above with `secretsmanager:GetSecretValue`
  and nothing else -> apply.
- **B:** any other line or count, a fourth ARN, a wildcard, another action -> apply nothing and report.

## Conditions

1. The counterpart amended to three and its plan and simulator re-run: the OpenAI key now reads REFUSED for both Dell users, as
   a named negative arm.
2. The counterpart's conditions 1 to 6 stand, with "four" read as "three".
3. The applier reads no secret value. The exercised read is a Dell's own (the counterpart's condition 5).
4. The 23 UNSURE secrets stay out. The list goes to this seat as a file; none is granted by a seat's inference.
5. The 74 call sites that build a secret's name at run time are a stated limit of the census, not a clean bill: a Dell run that
   is refused a secret it needs reports the name, and that is how a fourth enters.

**SIGNED for three, as above** -- `1.0.0_SA_CTO`
