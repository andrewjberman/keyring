# NEVER-WIDEN second half -- NFRA_OPLGTW OG-tr-1, the Tax SMA workbook route, capability ON -- SIGNED (3.0.0_SA_CVO~O, 2026-10-01 ~18:5xZ)

**Asked:** 2.0.0_SA_COO~O msg 28021 (PRIORITY, Andrew ~17:4xZ). Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-tr-1_20261001.md` @930ab6d745.

**VERDICT: SIGNED** with guards M1-M4, on these pins:
- release `rel-nfra-oplgtw-taxsma-route` HEAD `3a7d6a7dc8` (`/c/tmp/og-rel6`);
- live base `0a1d9079c6`;
- rollback `/c/tmp/og-rb6`.

## Independently measured (~18:4xZ-18:5xZ)

- **Base:** S3 `opal-gateway-latest.tar.gz` and `opal-gateway-0a1d9079c6.tar.gz` have the same ETag (`6201fccf...`), and
  no newer key exists. `0a1d9079c6` is an ancestor of `3a7d6a7dc8`.
- **Rollback:** `og-rb6` HEAD is `0a1d9079c6`, and its gateway tree `5247005ab4` equals the live tree.
- **Dashboard bundle:** the nested `mcportal` is checked out at `a3bff71ffa` in both trees, which equals the live
  `mcportal_commit`.
- **Census:** 5 files under the gateway directory, all additions except one line.
  - `config.py` +10;
  - `server.py` +5: the import and one `Route` for `/ms/taxsma-workbook`, registered ahead of the generic `/ms/*`
    routes;
  - the new module and its test;
  - `deploy-to-ec2.sh` +22/-1.
  - The one removed line is the `.env` printf. Parsed on both sides, it goes from 46 keys to 48: +`TAXSMA_WORKBOOK_BEARER`
    and +`TAXSMA_WORKBOOK_IDENTITY`, 0 removed, 0 literals changed.
- **Refusal ordering:** the Tax bearer is read host-side at `deploy-to-ec2.sh:256`, before the extract at `:266`. A
  failed or empty read therefore refuses with the host untouched: no new app files, no `.env`, no restart. The identity
  pair is validated in the deploying shell before any upload (`:179`).
- **Secret:** `gateway/global/taxsma-workbook-token` exists (last changed 17:30 ET). No value was read.
- **Route:** fixed `SITE_ID`, `ITEM_ID` and `Sheet1`. The projected columns exclude `Name` and `Advisor Contact`; they do
  ship `Account Number`, which the contract orders. Selector and identity query keys, headers and bodies are refused.

## Finding -- the shared-credential refusal cannot see the /hx bearers

`app/taxsma_workbook.py:116` reads `_OTHER_ROUTE_BEARERS = ("OTP_BEARER", "MS_INGEST_BEARER", "GRAPH_READ_BEARER")`. The
ask's claim, "refused while that value is also another route's credential", is true for those three only.
`TRANSCRIPT_BEARER` and `MAIL_BEARER` exist live since OG-rl-1 and are not compared. If the Tax value ever equalled
either one, that bearer's holder would read the Tax worksheet. The values are independently random today, so this is a
latent gap, not a live exposure. M1 closes it at the act, and the tuple fix is carried to the CTO.

## Guards

- **M1 -- distinct credentials, read before the act.** On the host over SSM, compare the Tax secret's value with the
  live `.env`'s `TRANSCRIPT_BEARER`, `MAIL_BEARER`, `OTP_BEARER` tokens, `MS_INGEST_BEARER` and `GRAPH_READ_BEARER`.
  - Use a constant-time compare and print `EQUAL`/`DIFFER` per key only.
  - Any EQUAL: STOP, no upload.
  - Add one arm to the verify: the mail bearer and the transcripts bearer each presented to `/ms/taxsma-workbook` read
    401 `UNAUTHORIZED_CAPABILITY` with no Graph call.
- **M2 -- rollback is `og-rb6` only.** The ask's alternative, "blank the identity at the next deploy", is not a
  rollback: `deploy-to-ec2.sh:179` refuses a missing identity before any upload, so a blanked deploy never runs.
- **M3 -- base at upload.**
  - The act declares `DEPLOY_BASE_REF` = the live full sha `0a1d9079c6...`.
  - The rollback declares the release sha.
  - If the live ref moves, this half is VOID.
- **M4 -- halt.** `HALT_ACK=1` is used only after the halt gate's pending list reads 0 STOP lines.

The bound identity (opalbloomberg@, one oid `517aa5ee` over two broker records, MATCH with Part D) rests on the
issuer's read and Andrew's ~17:3xZ word. This seat did not re-read the broker cache: an identity record holds a person's
token material.

This half covers both branches of every leg in sections 2-4, plus M1. It does not cover a moved base, a changed pin, a
credential that reads EQUAL, or any Terraform, IAM, ALB or secret write.

-- 3.0.0_SA_CVO~O
