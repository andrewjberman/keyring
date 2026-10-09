# MDPF_CANON PRD v2.9 -- ratified-text half review (L4-R re-sign)

**Reviewer:** `3.0.0_SA_CVO` (dell1). **Object:** `org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md` @12adb87963 (msg 2996).
**Diff read:** `git diff 12adb87963~1 12adb87963` on the PRD. It changes the header, adds one CONTRACTS row ("the firm gold writer"),
adds one SURFACE MANIFEST row and adds the v2.9 note. No ENDPOINT line changed. **Verdict: SIGN.**

## Checks

| Check | Result | Evidence |
|---|---|---|
| ENDPOINT untouched | PASS | the diff has no ENDPOINT line; `prd-signoff status` reads current by ENDPOINT hash. |
| Least privilege, one firm per principal | PASS | the row grants each principal only its own firm's gold prefix: never platinum, never another firm. M10's runner stays platinum-only. |
| Address is builder output (CLAUDE.md rule 30) | PASS | `address('mdpf','49financial','gold','holdings',...)` = `s3://opal-data-49financial/mdpf/49financial/gold/...`; for cottonwood it is `s3://opal-data-cottonwood/mdpf/cottonwood/gold/...`. Both match the row's `opal-data-{firm}/mdpf/{firm}/gold/*`. |
| Names resolve in the builder | PASS | `name('mdpf','49financial','gold-writer','role')` = `mdpf-49f-gold-writer-role`; for cottonwood it is `mdpf-cot-gold-writer-role`. The firm sits in the scope slot, as the row says. |
| Cross-firm law (CLAUDE.md hard stop) | PASS | one principal per firm, so each one's write set stays inside its own firm bucket. |

## Note for the L6 order (not a refusal)

- The row names the principal as "`name()` output" without printing it. The order that builds M2's roles should print each role name and
  grant prefix from the builders, for example `mdpf-49f-gold-writer-role` on `opal-data-49financial/mdpf/49financial/gold/*`. It should
  also read the live LGIC_ENFORCE Deny that is claimed to admit these roles unchanged (FWD-6), rather than assume it.

-- 3.0.0_SA_CVO
