# Andrew-direct, 2026-10-16 ~15:3xZ (11:3x AM ET), the `2.0.0_SA_COO~S1` terminal on dell1 -- TCKT_MTADTA

Two messages, sent while the issuer was relaying fire 2. VERBATIM:

1. "It should have a globgrph iam group that can read/write/do ops in there, and if we want to know things about it, we drive/query that lambda."
2. "Also Yang's phone on my IAM has already been dealt with"

## What the issuer did with them (record, not adjudication)

- **Message 2** agrees with `1.0.0_SA_CTO~DELL1` msg 6795: `mfa/Yang_Phone` was deactivated on `Andrew_Berman` on Andrew's word ~12:4xZ and read back (only `mfa/Andrew_Phone`
  remains); call `dell1-20261016T090600Z-6601` is CLOSED. The issuer's earlier replies in this session called it open; that was wrong, and is struck.
- **Message 1** restates the access design. The issuer does not widen or narrow it (CLAUDE.md: surface, never adjudicate scope). It is relayed to the CTO as a question, because the
  built door differs from a literal reading of "read/write/do ops":
  - What is built and live: the IAM group `globgrph-trino-access-group` holds `Andrew_Berman` alone (MFA-gated). Its members invoke the Lambda's `member` alias, which serves
    `get_day`, `get_state`, `list_state` and `derive_silver`, and refuses `put` and every other op. The `collector` alias (the collector role only) serves `put`, `derive_silver` and the
    cursor read. The bucket and key admit the Lambda's role alone, so the group reads and writes ONLY by driving the Lambda.
  - Not built: a member `put`/write op, any maintenance op, and the analyst question op (`query`, FWD-6, a later round).
- Carried to: the CTO (PRD C-ACCESS and the next recut). Nothing is changed by this record.
