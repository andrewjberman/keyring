# drive log 2.0.0_SA_COO~H -- 2026-10-02 13Z-15Z (opal_bloomberg)

## Andrew present; the ft solver route; track C step 1 (headline into gold)

- **Andrew-direct ~13:08Z:** "we need a whitelist for vendor calls. nopeCHA is permanently whitelisted for egress".
  Record @179990b502. CTO~Z placed `org/ref/VENDOR_EGRESS_WHITELIST.yaml` with VEW-1 NopeCHA. aj-4 was amended to a
  NopeCHA sign-in (@dc610be2d3).
- **aj-4 step 2 FAILED:** the NopeCHA Token API is discontinued (error 19; 1 call, 0 Kimi; row Z-W92-S18; merged
  @5d61b62795).
- **aj-6 cut** on the NopeCHA extension route (CTO 28484, @ce1886a63d), then re-pointed on Andrew-direct ~13:3xZ,
  "bETTER IDEA, LETS USE A NEW SOLVER", to Ocilar. The record is @9bc0e127be with the key REDACTED; the key is in
  Secrets `ocilar/credentials` (us-east-1; read-back matched; the scratch file was deleted; 0 repo hits). CTO landed
  VEW-4 Ocilar.
- **The aj-6 Ocilar sign-in FAILED:** HTTP 503, "Service 'hcaptcha' is not available yet" (row Z-W92-S19). Issuer read
  of `/api/v1/services`: hcaptcha `enabled:false status:coming`; only cloudflare and SAT are live; balance payg $0,
  with 1,000 free hcaptcha solves unused. The solver code (16/16 plants) was merged @67cc4ecbcc with no key in any
  diff. Andrew was offered A (NopeCHA extension), B (hand-solve) or C (another vendor); no answer yet.
- **Track C (CTO 28509):** title (VERBATIM) + published_precision go into the gold mention rows, then rebuild #5 under
  a NEW never-widen pair.
  - aj-7 was cut @cedca01272. Its builder is correct (AC1 6/6), and it was merged @385f4a76cc. Its AC2 crashed on 149
    barrons silver rows whose title is `{'text':...}`; the base builder fails identically, so no gold rebuild could
    run.
  - aj-8 was cut @bff0ce863a (CTO 28525, 3 conditions). `_extract_barrons` unwraps through `typed_text` as wsj does;
    merged @2268853761.
  - Re-derivation: the before-manifest listed 149 targets and the 15 others; exactly 149 were re-pended and uploaded
    into part `...113110Z-r1`. aj-8 AC2 PASS (149/149, 0 others moved). aj-7 AC2 PASS (713 rows, 0 mismatches). Both
    closed @757b50b6ad.
  - Rebuild #5 dry run 1: mention clean (+7,997; 22,372 rows titled verbatim). Daily OTHER 6, all coverage-only: today's
    barrons run covered 6 securities with 0 articles, so DENIED -> PARTIAL. The rule gained a COVERAGE-ONLY class
    (@93107a5b80). Dry run 2 is running.
- **Disk:** C: had 90 GB free at 13:5xZ, after the peers' worktree cleanup.
