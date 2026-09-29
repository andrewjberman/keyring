# CTO read -- TO-IB-m21-212 Part 1: the deployable cot login script (rows S165, S199)

**Diff:** `org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_R21_S165_PORT_DIFF_20260929.md` at CLOUD
`8b20b75d63` (commits 6a0ce7fe65, fdf12eadb1; .gitattributes 626033ace0, 2a4c589512); candidate md5
`7d37465ba68e8ddf44a66c008179d080`, built from the capture 28dd27a0. **Read by:** 1.0.0_SA_CTO, 2026-09-29 ~09:1xZ
(ruling S198's "diff read by this seat before it lands"). **Verdict: READ, fit for Part 2 on the conditions below.**

## Read

- **Group A (S165):** a bounded retry (`BD_MAX_LOGIN_ATTEMPTS` default 3, exponential backoff from
  `BD_LOGIN_BACKOFF_MS`); the terminal exit moves to `main()`, terminal behaviour unchanged.
- **Group B (S199):** the session `smPut` failure sets rc 1 and logs "session NOT advanced" instead of passing silently.
- **Group C (naming):** the firm id becomes a required env read with a fail-closed exit 3; the two Black Diamond cookie
  names and the debug prefix move to `secret-ids.env`. Those three are VENDOR configuration and an existing path whose
  value is unchanged, not canon names; the registry itself refuses to route the vendor spelling through a firm, so
  this is the right carrier. Naming limb WARN 7, 0 REFUSE, no waiver.
- **The CRLF hazard (5a)** is real and fixed for the cot env (`*.env text eol=lf`); the working copy is byte-equal to
  the blob.
- Not ported, deliberately: `classifyByDom` and the other 49F-only divergences.

## Conditions for Part 2

1. **Two artifacts, one act:** the `.js` and `secret-ids.env` deploy together under one ledger; the rollback restores
   BOTH (the running `.js` md5 28dd27a0 and the box's env md5 9b55e03c as captured).
2. **The first real run is the proof:** a login that advances the session, or a named failure (exit 2/3, or retries
   exhausted), read from the box's own log; never a silent pass.
3. The sibling 49F and inf env files under `infra/aws/ec2/` carry the same CRLF hazard; file it as a row with an owner
   (outside this order's grant).
