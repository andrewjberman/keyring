# Control-plane brief for the dell1 and dell2 CTOs -- 2026-10-07 ~07:1xZ

**From:** `1.0.0_SA_CTO` (laptop, the control plane). **For:** the CTO seat Andrew brings online on each Dell. Read at load, after
`org/XXX.md`. State below is as measured on the laptop at the time above; re-measure anything before acting on it.

## 1. What each box holds (the authority is `org/missions/SEQUENCE.yaml` v6 and each project row's `placement`)

| Box | Project | Stage read 07:1xZ | First act there | Predecessor lane on the laptop |
|---|---|---|---|---|
| dell1 | MDPF_SECCLASS | EXECUTING, PRD v0.12 ADMITTED | issue the round from the decomposition | `2.0.0_SA_COO~M` (live on the laptop: runs the signed rule-B remap and writes the v0.12 decomposition; issues nothing) |
| dell1 | MDPF_SECHIST | PRD v0.1 ADMITTED | decomposition (L5) | none: new |
| dell2 | IRPT_CUSTDY | PRD v0.1 ADMITTED | decomposition (L5) | none: new |
| dell2 | IRPT_BCKEND | EXECUTING, PRD v0.28 ADMITTED, three workstreams | each successor reads its `STATUS~P.md`, `STATUS~M.md`, `STATUS~Y.md` | `~P` (log @0d44093fe1), `~M`, `~Y` |
| dell2 | IRPT_YCDGEN | EXECUTING, round 6 | drain branch `wk-IRPT_YCDGEN-82`, then Andrew's report retry | `~Y` (handoff @217963b67d) |
| dell2 | IRPT_DASHBD | EXECUTING, PRD v0.7 ADMITTED | `/canonical-flow IRPT_DASHBD` | `~P` |
| dell2 | ADVI_COTBKF | EXECUTING, PRD v0.4 ADMITTED | read worker branches `wk-ADVI_COTBKF-13` to `-16` (left mid-round at the laptop's reboot) | `~C`, taken off it by Andrew |
| dell2 | ADVI_BILLING, NFRA_OPSWKF | PRD v0.1 ADMITTED, WAITING | nothing: each waits on an input only Andrew brings | none |

MDPF_TAXSMA is closed on Andrew's word; its six open order faces are owed terminal flips by the first D8 COO lane on dell1.

## 2. What a Dell may do in AWS (NFRA_CTLPLN PRD v0.11, `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md`)

- APPLIED today: update existing Lambda code, register ECS tasks, write EventBridge rules, read and write S3 objects and DynamoDB items.
- BUILT, NOT APPLIED: the create grant (create, update and tag on non-IAM resources), merge `7091ecaecc`; CTO half signed in
  `CTO_HALF_NFRA_CTLPLN_CT_c_1_DELL_CREATE_GRANT_20261007.md`. Until it applies, a Dell creates nothing. Its read side is short for ten
  services (row NFRA_CTLPLN-W4-S4), so a Terraform apply from a Dell fails at refresh until that fix lands.
- NEVER, refused by the cloud: any IAM write, CloudTrail stop, update or delete, deletes on `opal-data-*`, table or database deletes.
- A ROLE: the laptop creates it. Write in (C-ROLE-REQUEST): the project, the resource the role is for, the service that assumes it, and
  each permission tied to the code line that needs it. Send it to `1.0.0_SA_CTO` through your fabric manager's bus relay. The same
  write-in carries a bucket policy, a key policy or a Lambda permission. Andrew called this arrangement interim.
- A DEPLOY: your own committed work, named by full commit hash in your box's own ledger entry, with no wait on another box (FWD-10 as
  amended). The deploy tools' acceptance of a commit off the trunk is a cell not yet built; where a tool refuses, report its line.
- A served move still needs both never-widen halves.

## 3. What is not ready for a fourth fabric (do not work around these; report what you hit)

- A project row's `fabric` stays `laptop` for now. Two readers still know only two fabrics: `.tools/surprise-row-gate.py:2042-2051`
  refuses a row filed from a Dell-fabric project, and `org/standards/PRD_HEADER.schema.json:20` (row NFRA_CTLPLN-S5). The box is carried
  by `placement`.
- Per-box append files: a surprise row written on a Dell goes in that box's own suffixed file, never the laptop's (FWD-8;
  `.tools/git-hooks/one-writer-check.py`).
- Trunk: a Dell never pushes `CLOUD`. Publish your round branch; the merge into the trunk is another box's act and never a precondition
  for your deploy.

## 4. Rulings of tonight a Dell seat will meet

- Six asset classes only: cash, fixed income, equity, structured, alternatives, commodities (Andrew, MDPF_SECCLASS records). No seed
  run until `_shared/etf_classification.py` carries six-class values (CTO condition on the rule-B remap).
- The Cottonwood `B_01b` classifier is rolled back in S3 and in the repo; its deploy is unsigned
  (`CTO_RULING_MDPF_SECCLASS_S39_ROLL_BACK_COT_B01B_20261007.md`).
- No lane cap on a Dell. No vendor call without Andrew's per-use word.

## 5. Open between the laptop CTO and a Dell CTO

Who rules what is not yet said by Andrew: whether a Dell CTO writes the PRD addenda, round analyses and never-widen halves for the
projects on its box, or sends them to the laptop. Until he says, send a question that needs a ruling to `1.0.0_SA_CTO` with your REC;
it is answered the same tick under the laptop's `/self-drive`.

-- 1.0.0_SA_CTO
