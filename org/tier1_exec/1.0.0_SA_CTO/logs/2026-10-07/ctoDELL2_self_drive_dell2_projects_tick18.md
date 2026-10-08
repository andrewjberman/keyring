# /self-drive dell2 projects -- tick 18 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 17 (@edc6618b42), plus tick 18 (23:47Z). **state: ARMED**

## Scope state (23:47Z)

7 of 7 are active / EXECUTING. Sequence flags are unchanged (the known NEEDS-SLOT tracker gap on IRPT_CUSTDY and ADVI_COTBKF). Inbox:
0 unread after acks.

## Calls closed and acts

| input | ruling or act | carrier |
|---|---|---|
| Live read at 23:43Z | `irpt-ycharts-generate` still served `uFTONal...` about 70 minutes after release 1's half. A status ask was sent | msg 23:44Z |
| `~G2` 1147 and `~Y2` hold | The after-read 5 method was already ruled at 22:35Z (Andrew's F1 retry, plus CloudWatch in the meantime). Restated: deploy | msg 1149 |
| `~Y2` 1151 (L3 refused: dell2 has no `ssm:GetParameter` for the AL2023 AMI parameter that safe-apply's untargeted tag-authz plan reads) | Rec (a): the laptop applies by hash (artifact uploaded, S3 version `4Pvl.mN3tY9...`), under the same pair. No TAGAUTHZ_OVERRIDE. (b) The Dell read grant is a lasting fix at laptop `~C` | msgs 1155-1156 |
| MSTR 1145/1146 (laptop ruling 106630: the BD split pull's halves are dell2's) | -- | -- |
| `~D2` 1152 (DB-b-45 pair) | CTO half SIGNED. Andrew's word was read at @5ef6d33141. Rollback deletes go to Andrew; this is the one use of the word | @5a223f2a26 |

## Acts only Andrew can do

As at tick 16, plus:
- **His F1 retry**, once release 1 is applied by the laptop and after-read 4 passes.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `get-function-configuration` (CodeSha256, LastModified) caught a signed release that had not moved. That is the measured state, not
  the status the seat summarised.
