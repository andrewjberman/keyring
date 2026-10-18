# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 119, `AMGT-bz-5`: redeploy `opal-amgt-scoped-api` from release pin `2771164d0d` (export currency codes, export management parity, appendix through the mapper)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~13:0xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND119_RICH_EXPORT_CODES_MANAGEMENT_AND_APPENDIX_REDEPLOY_COO_HALF.md` as committed
at 2f657c667b, sha256 `2ff43a0a2cd975228c45e46bb3677b1563819a3fdf9b021b596d00a501fb4dba`. Any edit to that file voids this half.

## What I read at signing

- **The pin:**
  - `2771164d0d` has the single parent `d4c6f1c533`, the build input of the live package since by-5.
  - `git diff --stat` lists exactly one file, `render_pack.py`, at blob `3ddc696def09` to `a281246c18c0` (equal to the half's table).
  - `scoped_amgt.py` does not change.
- **My by-5 row is fixed in the pin:** `UNKNOWN_VERDICT_SENTENCE` (`render_pack.py:874`) reads "steer clear".
- **The producer's rule:**
  - export money rows read `_own_currency`, the same reader the PDF uses;
  - a figure the page withholds prints the page's words with no amount (RIO LN);
  - the export's management lines come from the PDF route's reader and input (C-S195).
- **The measurement:**
  - CROSS SURFACE reads YES 8 of 8, against the live base control NO 0 of 8;
  - the export money rows carry GBp, PHP and USD, where the live ones carry none;
  - the leak scan reads 0 of 101;
  - PACK FORM reads 8 of 8 and MONEY 16 of 16;
  - the PDF text is identical on 8 of 8.
- **One weak point, stated by the half itself:** unit control M6 ("both routes hand the builder the same management object") is true by
  construction of its stub, so it proves nothing. The live cross-surface read is the real proof, and it is a condition below.
- **The page is opal-internal (Security Analysis).** This seat signs.

## Blast radius

The function's code artifact only, with the one member at the blob above. No IAM, route, memory, timeout, schedule, layer or environment
change; no data write; no S3 delete.

## Both branches

- **(a) The package takes:**
  - a new CodeSha256, with memory 1769, timeout 29 and the environment keys unchanged (`AMGT_AIFILL_ROOT` absent);
  - PACK FORM 8 of 8, MONEY 16 of 16, the live leak scan 101 of 101 clean;
  - the eight live exports with no `s3://`, `AMGT-` or vendor-error line;
  - CROSS SURFACE YES 8 of 8 on the LIVE function;
  - both routes under 20 s for KMB US, RIO LN and GOOGL US.
- **(b) It does not take, or carries more:**
  - any other differing member is a STOP BEFORE UPLOAD;
  - any after-read NO, or a route over 20 s, is a same-window rollback to the by-5 build: `H3dCSGL..`, RevisionId `caab3655-...`, S3
    VersionId `xr.zAPt5G9_Tjw8D60wN54ZgecD0x9P4`.

## Conditions of this signature

1. **Pre-upload recheck.** CodeSha256 `H3dCSGLEs4abPk0alOWclPZX1U6lYrxEXkhGZOAJ434=`, RevisionId
   `caab3655-4909-4c3d-ba32-76446effe97d` and LastModified 2026-10-18T11:14:20Z are equal at upload. Otherwise STOP.
2. **The built package's content diff is printed before upload.** Only `render_pack.py` may differ, at the blob above.
3. **The cause of C-S195 is NAMED in the round-119 record:** why the live export printed "could not be read" while the PDF printed the
   reading. The live cross-surface read proves the fix, but a fix without a named cause is not a remediation.
4. **NEVER-2:** the entry is opened first, and its close is COMMITTED.

## Not covered, and routed

- **A round-120 row:** the export lacks the thesis-pillars passage the PDF prints for ICT PM, GOOGL US and ICICIBC IN. That is the same
  surface-parity class as C-S195.
- W518-S2 and the other armed rows stay with their rows.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
