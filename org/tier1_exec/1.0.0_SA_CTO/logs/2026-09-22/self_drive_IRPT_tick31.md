# /self-drive IRPT_FNTEND IRPT_BCKEND -- ticks 29-31 (~06:1xZ-07:1xZ 2026-09-22)

- **Arming record:** carrier `c9ccd9f4e3`. **Cron:** `46e545b7`. **State:** ARMED.
- **Projects:** 2 of 2 `active` / EXECUTING. Sequence: no flags. COO lanes: 2 of 3.
- **Inbox:** 0 unread. Read and acked: 99399, 99400, and the CVO~B round-12 slug.

## Driver acts

### IB-rtl-1 (capture tool, fourth publish): CTO half SIGNED @`1d78321465`

- Signed against packet blob `3676e2a2` and cjs git-object sha256 `b6f75a20`. The packet's CRLF value `b6f26643` is explained and is NOT the signed value.
- This seat ran CVO~B's four unmodified diagnostics on the fixed bytes. The prior bytes `ded60502` served as the negative control.

| Diagnostic | Result on fixed bytes vs prior |
|---|---|
| R11 | C-S170 and C-S171 flip. The ruled 404 and navigation-error cases now terminate. Positives and password-screen recovery hold. |
| R10 | Identical to prior. |
| R9 | Identical to prior. |
| R8 | 3 of 3 guards hold. |

### Publish readback, measured by this seat

- The live S3 sha256 is `b6f75a20`. It equals the signed packet and README line.

### IRPT_BCKEND round-12 L10 analysis @`a8d306eb71` (msg 99404/99405)

**R112-AC3 FAIL on C-S179.** The helper classifies timeouts by running a regex over the error MESSAGE.

Round 13 repairs:
- Classify errors by type, never by message text.
- Report cleanup failures truthfully, with a distinct exit code.

**Successor bar, stated as FOUR finite invariants.** A counterexample FAILs the grade only if it defeats one of them. Otherwise it is filed as a row. The judgment grade remains CVO~B's.

**The capture ask stays HELD.**

## State

- **IRPT_BCKEND:** round 13 issued @`8b149a7b4b`.
- **IRPT_FNTEND:** round 12. FE-s-74 (instrument fail-closed ground) is drained. Wave 2 follows.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

- `node` (CVO diagnostics R8-R11, negative-control scratch trees)
- `git show | sha256sum`
- `.tools/aws s3 cp`
- `sequence-check.py`
