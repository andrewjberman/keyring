# ANDREW-DIRECT 2026-10-02 ~16:4xZ -- open-calls recs approved: ft solver A+B; Ocilar key not rotated until funded; re-check Ocilar in 30 days

- Channel: site-Z terminal of `2.0.0_SA_COO~H` (session d9ce3a44-2d1e-4745-8265-458874d2c772), typed by Andrew.
- Time: 2026-10-02 ~16:47Z (12:47 ET).
- Recorded by: `2.0.0_SA_COO~H`, same turn.

## Verbatim

Andrew: "recs approved. plus keep a note in wherever the comp-schedule routes that we should check on oscilar being
funtional in 30 days."

## What "recs approved" approved (the /open-calls cards at this lane, ~16:5xZ)

- **CALL 1 -> REC (A+B):**
  - (A) the ft sign-in hCaptcha is solved by the NopeCHA BROWSER EXTENSION (VEW-1; CTO 28484 already YES), for
    unattended sign-in and renewal;
  - (B) Andrew hand-solves ONE ft sign-in NOW, so the aj-4 2-hour keep-alive test runs today while A is built.
- **CALL 2 -> REC (no rotation now):** the Ocilar API key is NOT rotated now. It is rotated when the Ocilar account is
  first funded.

## The note (as said)

"check on oscilar being funtional in 30 days" -- due on or after **2026-11-01**. Read
`api.ocilar.com/api/v1/services` (key from Secrets `ocilar/credentials`; VEW-4). If `hcaptcha` is live, the Ocilar
route (aj-6 code, merged @67cc4ecbcc) becomes usable, and per CALL 2 the key is rotated when the account is funded.
Carried in AMGT_HARVST's project file as a dated `scheduled_checks` row.

`comp-schedule` has NO carrier for dated checks today. Its five carriers are deploy sentinels, open deploy ledgers,
CLAUDE.md moratoria, task-order scope guards, and `org/projects/*.json` `blocking` prose. The HARVST
`org/projects` stub is generated without `blocking`. So the carrier gap is put to comp-schedule's owner
(`1.0.0_SA_CTO~Z`), and this record does not edit the tool.

## Relay

One line to `1.0.0_SA_CTO~Z` naming this path (the solver choice, and the comp-schedule carrier gap).
