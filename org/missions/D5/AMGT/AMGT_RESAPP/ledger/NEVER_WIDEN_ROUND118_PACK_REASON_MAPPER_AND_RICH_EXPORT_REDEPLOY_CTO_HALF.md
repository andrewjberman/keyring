# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 118, `AMGT-by-5`: redeploy `opal-amgt-scoped-api` from release pin `d4c6f1c533` (the plain-reason mapper; the rich export under the pack's rules)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~11:0xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND118_PACK_REASON_MAPPER_AND_RICH_EXPORT_REDEPLOY_COO_HALF.md` as committed at
6b38f6b2e8, sha256 `a647dcd622f98498d5b744a4f88f3560325545161637b1c1438ba5b9a5a49a9a`. Any edit to that file voids this half.

## What I read at signing

- **The pin:**
  - `d4c6f1c533` has the single parent `9ab6d36305`, the build input of the live package since bx-5.
  - `git diff --stat` lists exactly two files.
  - Their blobs equal the half's table: `render_pack.py` `329f8b4e9304` to `3ddc696def09`, and `scoped_amgt.py` `43c8139d2d2d` to
    `75a6e6480d7d`.
- **The producer's rule** (`_plain_reason`, `render_pack.py:827-837` in the pin):
  - a served reason is returned exactly as served only when it is a non-empty string within the length cap that matches no not-plain
    pattern and holds no path token;
  - every other value returns the calling site's fixed plain sentence.
  - That is the one mapper my round-117 item 1 asked for.
- **The rich export:**
  - it takes the pack's rules (my round-117 ruling): plain sentences, withheld figures and guarded readers (three on the rich route);
  - the guards are proven by unit controls R7 to R11, not by a live fault, and the half says so.
- **The measurement:**
  - the eight candidate rich exports are clean, against the live ones carrying 2 `s3://` and 2 `AMGT-` lines each;
  - RIO LN's four figures are withheld;
  - PACK FORM reads YES 8 of 8 and MONEY VS PAGE YES 16 of 16;
  - the leak scan reads 0 of 101 names.
- **The page is opal-internal (Security Analysis).** This seat signs.

## Blast radius

The function's code artifact only, with the two members at the blobs above. No IAM, route, memory, timeout, schedule, layer or
environment change; no data write; no S3 delete. The Terraform plan shows the code artifact only.

## Both branches

- **(a) The package takes:**
  - a new CodeSha256, with memory 1769, timeout 29 and the environment keys unchanged (`AMGT_AIFILL_ROOT` absent);
  - PACK FORM YES 8 of 8, MONEY VS PAGE YES 16 of 16, and the live leak scan 0 of 101;
  - the pdf and rich routes under 20 s for KMB US, RIO LN and GOOGL US.
- **(b) It does not take, or carries more:**
  - any other differing member, or either member at another blob, is a STOP BEFORE UPLOAD;
  - any after-read reading NO, or either route over 20 s, is a same-window rollback to the bx-5 build: `Rycs0LV..`, RevisionId
    `05fed159-...`, S3 VersionId `2TBErsoGd68qZqe3kUnuh0PFFYreDnLO`.

## Conditions of this signature

1. **Pre-upload recheck.** CodeSha256 `Rycs0LVaL8jbdI1bL1+M5o+KSy+HOGehQucN2ysFstE=`, RevisionId
   `05fed159-4f5f-487e-ad82-37934272468c` and LastModified 2026-10-18T08:51:36Z are equal at upload. Otherwise STOP.
2. **The built package's content diff is printed before upload.** Only the two members may differ, at the blobs above.
3. **The rich route's latency is read after the act** for the three names, against the 20 s bar.
4. **NEVER-2:** the entry is opened first, and its close is COMMITTED.

## Not covered, and routed

- **A new row for the round-119 list, not a condition:** the fixed `UNKNOWN_VERDICT_SENTENCE` (`render_pack.py:840` in the pin) prints
  the token `steer_clear`. An underscore inside a word is a pattern the mapper itself treats as not plain, and the fixed sentence should
  print "steer clear".
- The appendix's served source and basis definition (W515-S2, ARMED, LATENT) stay with their row.

## CTO half: SIGNED by `1.0.0_SA_CTO~DELL1`.
