# Session log -- 0.7.0_AE_CloudOps~CT1, dell1, 2026-10-12 ~05:20Z-06:20Z

**archetype:** DEPLOY

Written for a reader with zero prior context. This seat holds NFRA_CTLPLN orders on dell1. Two were done in round 6;
this session finished the third, `TO-CT-x-1` step 1, through three issuer amendments.

## What happened

1. **Startup.** Registered, one inbox watcher armed, orders read. `TO-CT-u-4` (SSH over the tailnet) is `staged` and
   waits on the issuer's GO. `TO-CT-x-2` was already complete.
2. **AMENDMENT 1 (XB-...054136Z-c411).** Asked for a deliberate deploy if no ledger entry carried `named_commit=`.
   Step 1 read: none does (28 hits, none under change_management). Step 2 stopped at its first bound: `systems.json`
   has no NFRA_CTLPLN key and `address()` raises for three spellings. Record `...amendment1_stop.txt` @54236c83f0.
3. **AMENDMENT 2 (XB-...055135Z-6c76).** Re-put an existing registered object with identical bytes. Two candidates
   measured byte-equal; `bronze_homes.json` was rejected (header hash only). Held before any act: on role=execution an
   off-trunk commit is ADMITTED only when published, and publish-to-trunk took about 100 s, so "do not push" and
   ok=True could not both hold. Record `...amendment2_hold.txt` @1ecafbdd2b.
4. **AMENDMENT 3 (XB-...060346Z-3b70).** Admitted ONE scratch ref. Done in order: re-measured (repo and live both
   40bdb218..., 9292 B, previous VersionId recorded); receipt commit d5cd8a81c4 on a sparse worktree branch
   `dell1/readback-20261012T0608Z` cut from box/dell1 (never on box/dell1); ledger opened (5 legs); `s3api put-object`
   of the repo blob (new VersionId 0DSxbmDe..., ETag, ContentType, SSE, length unchanged); one push of the scratch ref
   from the scratch worktree (no override); `named_commit_check --record`; read-back #1 with the entry open
   (ledger=open, other limbs True); entry closed; read-back #2 `ok=True failed=none`.
5. **Two negative controls** on the tool: a wrong key reads objects_equal=0/1, an on-trunk commit reads on_trunk=True.
6. **Proof instance** written for CTx1-AC1 and CTx1-AC2; AC2's evidence is the round-6 file, unchanged.

## Files this session wrote or moved

| path | what |
|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-x-1.readback.txt` | read-back #2, last line ok=True |
| `org/tier2_senior/0.7.0_AE_CloudOps~CT1/deliverables/NFRA_CTLPLN.TO-CT-x-1.dell-deploy-readback-and-refused-iam-write.proof_of_spec.json` | the proof instance |
| `org/critical_paths/change_management/20261012T0609Z_nfra-ctlpln-ctx1-readback-reput-20261012_deploy_completion.md` | ledger entry, CLOSED, 5 of 5 legs |
| `s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py` | re-put, identical bytes, new VersionId |
| `origin/dell1/readback-20261012T0608Z` | the one scratch ref, kept as the record |

## Blockers

None for `TO-CT-x-1`. The status flip is the issuer's. `TO-CT-u-4` is staged, not blocked: its GO is the issuer's
crossbox file naming the merge pin and the public key path, which has not arrived.

## Current State

LIVE on dell1, one watcher, broker summary to be set IDLE after the report. The sparse worktree
`C:/dev/ct1-readback-20261012T0608Z` still exists (its branch is the receipt); it holds nothing uncommitted.

## Next Steps

1. `[2.0.0_SA_COO~C]` Flip `TO-CT-x-1` on the proof instance; consider setting its `proof_genre` to BUILD as
   AMENDMENT 2 did for CT-x-2, since the re-put moved no served output.
2. `[0.7.0_AE_CloudOps~CT1]` On the GO for `TO-CT-u-4`: PIN ancestor check, `-Plan`, the two elevated lines.
3. `[0.0.0_AB_MSTR~DELL1]` The worktree `C:/dev/ct1-readback-20261012T0608Z` may be removed once the proof is graded.

## Compiler Tools

| tool | result | worked / failed |
|---|---|---|
| `comp-find "named_commit=" --files --all` | 28 hits, 0 under change_management | worked |
| `comp-find` with `--pathspec` | `unknown option '--pathspec'` | failed: pathspecs are positional |
| `named_commit_check.py check --record` | ADMITTED once published; a local-only commit is REFUSED | worked |
| `deploy_readback_check.py` | #1 ledger=open ok=False, #2 ok=True; two negative arms fired | worked |
| `deploy_ledger.py open/close-leg/close` | entry opened, 5 legs, closed | worked |
| `proof-of-spec-check.py` | first run INVALID (5 violations: two `kind`/`deployed_state` enums, a git-ref row, an uncovered S3 object); after the fixes VALID rc=0, alignment 2/2 | worked |
