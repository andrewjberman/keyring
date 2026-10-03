# CRO FAST pin grades (3.0.0_SA_CVO), 2026-10-03

## LDO-001 End of Day weekend runs (ledger `ldo-001-eod-weekend-runs-20261003`, closed f84b96d1d4), read 21:5xZ 2026-10-03

Andrew-direct ~20:5xZ ("yes i want weekend runs"). Pin 0c326e8f86. The CRO's V1 compares `tenant.py` only; this seat
compared every member.

| read | result |
|---|---|
| `teams-global-chat-assist-handler-lambda` and `-ingress-lambda`: CodeSha256 `c8s2XI7ooGJG..` on both = the downloaded zip's sha256; LastModified 21:00:58Z and 21:01:08Z | deployed bytes as recorded |
| 18 members: 12 byte-equal to `git show 0c326e8f86:<path>`, including every `.py`; `handlers.py` = `infra/aws/lambda/teams-chat-assist/handlers.py`, `ldo.py` = `infra/aws/terraform/modules/ldo/runtime/ldo.py`, `tenant.py` = the pin | PASS on the code |
| 6 members differ by CRLF only: the six `infra/logic/registry/*.json` files equal the working-tree copies, and their content equals the pin modulo line endings | PASS modulo EOL |

**Note.** The build read an autocrlf working tree, the class of row IRPT_BCKEND-S286 in another builder (LDO's
`build.sh`). JSON readers ignore CRLF, so it has no effect on behaviour. The same fix applies: stage members from `git show`
or build from a `core.autocrlf=false` checkout. No row is filed: no behaviour is affected and the class is on record.

**Limits.** The EOD run itself (poll_eod queued 2026-10-03 at 21:01:20Z and the draft texted) was not read from the logs.

-- 3.0.0_SA_CVO
