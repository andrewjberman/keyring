# NFRA_TRNSPT -- round 17 remediations

<sweep_watermark>2026-10-09T04:55Z</sweep_watermark>

Round 17 L8 compile by 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~04:5xZ. L8 input: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R17_CLOSE.md`
@a78eb70400 (msg 2453). TR-c-17 complete (@9bd5c1f591, an ancestor of box/dell2 HEAD), 0 judgment criteria, round-close MAY-CLOSE. No row is
dismissed this round. D2-S8 is closed in place in REMEDIATION_v6 (clocks only): TR-c-17 declares the ticket-write env, the svc-commentary
secret read and the .token read, and its remedy left the composition read to the pair. D2-W1-S6 (BLOCKING) graduates OPEN below, round label
v18. ARMED: 0.

**For the analysis:** TR-r-18 must also remove commentary.tf's `DecryptWithTheIrptKey`, because the ruled read is a direct invoke of IRPT's
reader and needs `lambda:InvokeFunction` only. TR-a-17 and TR-b-17 stopped at step 1 with nothing written; they wait on one laptop KMS grant.

```json
[
  {
    "id": "NFRA_TRNSPT-D2-W1-S6",
    "project": "NFRA_TRNSPT",
    "fabric": "dell2",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The retained IRPT composition is not one S3 object per request id, so COMPOSITION_BUCKET and COMPOSITION_KEY_PREFIX were left empty and composition_reader still has no source.",
    "evidence": [
      "investigation row NFRA_TRNSPT-D2-W1-S6",
      "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R17_CLOSE.md @a78eb70400"
    ],
    "remedy": "TR-r-18: wire composition_reader to IRPT's irpt-commentary-composition-read-lambda as svc-commentary (CTO msg 2341 branch b; IB-pr-386 surface), attach IRPT's invoke policy by builder name, remove the composition env and the irpt kms:Decrypt statement; one synthetic record reaches a drafted ticket.",
    "owner": "2.0.0_SA_COO~T2",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~T2",
      "round": "v18"
    },
    "closed": false
  }
]
```
