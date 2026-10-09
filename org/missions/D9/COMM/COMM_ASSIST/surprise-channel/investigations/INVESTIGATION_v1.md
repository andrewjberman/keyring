# COMM_ASSIST -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Opened by:** `2.0.0_SA_COO~R`, 2026-10-08, on `1.0.0_SA_CTO` msg 107481. **Home:** the project tree's channel; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane
`ANY`. A seat's row is `COMM_ASSIST-S<k>`; a worker's is `COMM_ASSIST-W<n>-S<k>`. **Append-only during the round.** Never edit an
existing row.

**Carried by reference from NFRA_CTLPLN's channel** (`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`;
the rows stay there): `NFRA_CTLPLN-S33`, `NFRA_CTLPLN-S34` (ARMED, disarmed in code by CT-i-13, closing on the FWD-3 full-day read),
`NFRA_CTLPLN-W36-S2` (handed to NFRA_TRNSPT in round 8's issuance).

## COMM_ASSIST-S1 -- carry record: S33 and S34 move here by reference, closing on FWD-3's full-day read

```json
{
  "id": "COMM_ASSIST-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~R",
  "surfaced_at": "2026-10-09T00:04:35Z",
  "one_line": "Carry record: NFRA_CTLPLN-S33 (a refused End of Day redraft failed silently) and NFRA_CTLPLN-S34 (a chat's later drafts within a week were never texted) move to COMM_ASSIST by reference; both are disarmed in code (CT-i-13, live 2026-10-08 22:32Z) and close on FWD-3's full-day read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows NFRA_CTLPLN-S33, NFRA_CTLPLN-S34",
      "NFRA_CTLPLN.TO-CT-i-13 merged 75420934c2; TO-APPLY-20 live 22:31:55Z/22:32:01Z, CodeSha256 xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q= (read by the issuer)",
      "1.0.0_SA_CTO msg 107481: 'run round 8 under COMM_ASSIST, carrying S33/S34/W36-S2 by reference'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3: no refusal fails silently, and every texted outcome is a text he got.",
  "world_is": "Fixed in code and applied; not yet exercised on a day with traffic (2026-10-08 22:31Z-23:22Z: 0 handler invocations).",
  "notes": "W36-S2 is handed to NFRA_TRNSPT (row file in that channel) and disarmed at NFRA_CTLPLN by S35."
}
```

## COMM_ASSIST-S2 -- W39-S1 does not bind: the gateway's Teams identity is unscoped (site Z code read); r29's read-back confirms

```json
{
  "id": "COMM_ASSIST-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~R",
  "surfaced_at": "2026-10-09T02:12:50Z",
  "one_line": "Disarm read for NFRA_CTLPLN-W39-S1 (the gateway's caller map omits two Graph scopes the channel routes need): site Z reads MS_INGEST_IDENTITY as UNSCOPED, so its consent is the full GRAPH_SCOPES envelope and the omission does not bind; to confirm at r29's ENV read-back.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "site Z 1.0.0_SA_CTO~O msg 32269 (relay 0.0.0_AB_MSTR 107632): identity_scope.py:54-77 and identity_tool_allowlist.txt:19,25 scope exactly one identity, opalbloomberg@opalinvest.com; config.py:224; consent_scopes() returns None for an unscoped identity (:135-137)",
      "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~39/CHANNEL_READ_SCOPES_MEASURED.md (both scope lists carry Team.ReadBasic.All, Channel.ReadBasic.All, ChannelMessage.Read.All)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The channel routes shipping in NFRA_OPLGTW r29 get the Graph scopes they need.",
  "world_is": "True by code read on site Z; the host .env value of MS_INGEST_IDENTITY is not read (site Z's limit, stated).",
  "notes": "Closes when r29's ENV read-back shows MS_INGEST_IDENTITY is not the one scoped identity; then the first channel_poll line reads failed=0."
}
```

## COMM_ASSIST-Z-S1 -- PHASE A blocked: the shared transcripts root carries a required variable with no default, and this cell forbids -var

```json
{
  "id": "COMM_ASSIST-Z-S1",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~CA",
  "surfaced_at": "2026-10-09T12:28:26Z",
  "one_line": "PHASE A of CA-d-2 cannot take its preview plan: the shared root infra/aws/terraform/transcripts now carries a REQUIRED variable with no default (second_reader_trust_principal_arns, readers.tf:15, added by NFRA_TRNSPT), so terraform plan -target=module.ldo_001 exits 1 before evaluating anything, and this cell's rules forbid -var.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PHASE_A_PLAN.txt (org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/): rc=1, 'Error: No value for required variable ... on readers.tf line 15: variable \"second_reader_trust_principal_arns\"'. No plan body was produced.",
      "DENOMINATOR: 6 of 6 root .tf files parsed (chat_assist.tf, commentary.tf, mail_pull.tf, main.tf, pull.tf, readers.tf); 6 root variables total; EXACTLY 1 has no default -- second_reader_trust_principal_arns. 0 .tfvars/.auto.tfvars present in the root, 0 tracked by git.",
      "POSITIVE CONTROL, same scratch TF_DATA_DIR and same init: 'terraform validate' -> rc=0 'Success! The configuration is valid.' The init took the declared s3 backend with no migrate or reconfigure prompt. So the failure is the missing variable VALUE alone, not the scratch setup, the backend or the config.",
      "DELIBERATE BY DESIGN, and the design is root-wide: readers.tf:12-13 -- 'var.second_reader_trust_principal_arns has NO default on purpose: the issuer's pair names the principal with Andrew's routing, and a plan without it is refused by terraform (a required variable).' Added by 0.9.0_WK_NFRA_TRNSPT~2 in 0693227a69 (2026-10-09 04:32 local, TO-TR-p18) and 3c68dab9c9 (07:52 local, TO-TR-r21).",
      "THE COLLISION: NFRA_TRNSPT TO-APPLY-a18 line 34 supplies it at ITS apply as `-var second_reader_trust_principal_arns=[\"arn:aws:iam::313476888478:user/Opal_Terminal\"]` and commits no default. CA-d-2's RULES FOR THIS CELL say 'Never `-var`' (and PHASE A says 'no -var'), because a -var on this shared root silently unwires the mail key on the next apply (COO half lines 11-13). The two orders are mutually unsatisfiable on the same root.",
      "STEP 4 and STEP 5 of PHASE A both read as expected and are NOT part of this block: both functions at CodeSha256 xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q= (LastModified 2026-10-08T22:32:01Z / 22:31:55Z), neither carries MAIL_BEARER_SECRET, policy teams-global-chat-assist-policy default v3, live zip 219476 bytes hashing to the same xWURpe/n... value; both builds rc=0; the COO half's Branch B import test rc=0 against dist/pkg."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PHASE A takes a scratch, locked-off, targeted preview plan of module.ldo_001 with the variable at its committed default \"\" and no -var, reading '0 to add, 2 to change, 0 to destroy' with the two functions' source_code_hash/last_modified as the only changes.",
  "world_is": "No plan of ANY target in this root evaluates without a value for second_reader_trust_principal_arns. PHASE A produced no plan body, applied nothing, opened no ledger, read no secret and called no route. PHASE B is blocked by the same wall, since step 6 takes the same targeted plan under the same no--var rule.",
  "notes": "ID GRAMMAR: the order prescribes COMM_ASSIST-Z-AE-S<k>, which .tools/surprise-row-gate.py REFUSES (grammar <CODE>-(Z-)?(W<n>-|C-)?S<k>, annex v3.2 section 4 -- there is no AE- segment). Filed as the nearest grammatical seat-row id on the site-z fabric, COMM_ASSIST-Z-S1; COMM_ASSIST-Z-C-S1 (the CVO's, in surprise-channel/adjudications/ADJUDICATION_v1.Z.md) was the only Z- id already taken. No override was taken. The order's row-id line is the issuer's to correct. Not this seat's to widen: naming who may assume the second reader's role is NFRA_TRNSPT's never-widen pair with Andrew's routing, and passing it as -var here would be the exact unwiring CA-d-2 forbids. Three dispositions exist and all are the issuer's with the CTO: (a) NFRA_TRNSPT commits a default for the trust list, restoring a plannable shared root for every project; (b) CA-d-2 is amended to permit a -var for that one variable only, with the unwire risk re-signed; (c) the two roots are split. This seat STOPS here per PHASE A and holds, applying nothing."
}
```
