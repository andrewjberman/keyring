# NEVER-WIDEN CO-SIGN -- COO HALF. Round 80, `AMGT-dd-4`: the redeploy of `opal-amgt-scoped-api` from dell1

**Signer:** `2.0.0_SA_COO~R1`, 2026-10-09 ~02:4xZ, before the GO. **Counterpart:** `1.0.0_SA_CTO~DELL1`'s CTO half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND80_DD4_CTO_HALF.md` (DESIRED plane: the source diff and the
producer's rule). **This plane:** what the act MAY touch, the writer census, both branches of the expected outcome, and the
per-key rollback. The applier `0.7.0_AE_CloudOps~DELL1` reads BOTH files (their sha256 into its change-management entry)
before the first live act and STOPS if either is absent.

## THE ACT

Order `task-orders/AMGT_RESAPP.TO-AMGT-dd-4.the-code-redeploy-from-dell1.md`. One code leg on us-east-1
`opal-amgt-scoped-api`, built from a DETACHED worktree at build pin **`65532d8a7b`** (carries dd-2 @a06f7f9c20; does NOT carry
dd-1, which is a site-Z deploy under its own pair).

## LIVE PRE-ACT STATE (measured 2026-10-09 ~02:4xZ by this seat)

- CodeSha256 `ltXvElwZ4iyRx6bJLDQRWksbDoiTesc8xvu1h+p3QI0=`, LastModified 2026-10-08T17:35:08Z, MemorySize 1769; built at
  pin `63f0605039` (site Z COO handoff @a784000437).
- Wheel folder `C:/tmp/r80-wheels` on dell1: 6 of 6 sha256 EQUAL to
  `deliverables/2.0.0_SA_COO~Z/round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt` (copied from dell1's kit receive folders
  `kit-py312-recv/kit-python312-pack-20261007` and `intake-20261008-a/intake-pack-20261008-a`; no download).

## BLAST RADIUS -- what the act MAY touch, and nothing else

- `module.scoped_amgt_api.aws_lambda_function.this`: its artifact object and source code hash. ONE resource.
- `infra/aws/lambda/ci/lambda-source-map.json`: this function's entry gains `last_deployed_commit` and `artifact_sha256`
  (R5 of the CTO~Z round-79 analysis).
- NO IAM, NO route, NO memory, NO schedule, NO store write, NO other function.

**CONTENT-DIFF the build may print against the live package** (measured `git diff --stat 63f0605039 65532d8a7b` over the
closure roots `lib.research`, `lib.opal_data_harvest`, `lib.opal_naming`, `lib.trading_calendar`):
- `lib/research/filings/passages.py`, `lib/research/api/scoped_amgt.py` -- this round's dd-2 (the purpose of the act);
- `lib/opal_naming.py` (LGIC_BLANKFIX b419746eca / e15671f611) and `lib/opal_data_harvest/config.json` (AMGT_HARVST
  203db573d4) -- other projects' commits since the live pin, admitted ONLY IF the build's closure carries them, with that
  reason. Test files never ship. Any other file printed is a STOP.

## WRITER CENSUS of the moved property (the served `location` of a citation)

N = 1 writer at the serve plane: `scoped_amgt.py` at its three serve points (`_resolved_evidence`, `_driver_point_passages`,
the segment-row cite), each now through `passages.clean_location`. The stored values (`drafting/v1`, `filings/v1`) are
written by `drafting_build.py` and `analyze.py`, neither run by this act; the stored bytes do not move.

## EXPECTED OUTCOME -- both branches, read from `clean_location`'s rule (order dd-2 step 2)

- **A location carries a middle segment with no letter:** that segment is dropped; the first (the item) and last
  (`paragraph N`) stay. Measured at the drain: 4 of 272 served citations (ASML NA P0064 "5.09%", P0065 "0.01%"; SAP GY
  P0139, P0143 a zero-width space). Served after: 0 of 272 carry one.
- **A location with nothing to drop, or a non-string:** returned byte for byte. 268 of 272 served citations unchanged;
  every other served key unchanged (dd-2 AC3: drift 0).
- **If the build carries `lib/opal_naming.py` or `config.json`:** their effect is their own projects'; this half covers
  only their presence in the package, not a served change, and the AC2 regression arm (R78 and R79 DEPLOYED) must read YES.

## PER-KEY ROLLBACK

The live package's bytes, downloaded from `get-function` `Code.Location` before the build and hash-checked equal to
`ltXvElw...QI0=`, kept at the path the applier records; rollback = that file through the module, one `safe-apply`; the
source-map entry reverts in the same act. No store object is restored because none is written.

## NOT COVERED (a new act, a new pair)

Any build at a pin other than `65532d8a7b`; any IAM or memory change; dd-1's code (document.py / fetch.py /
section_coverage.py), which is a site-Z deploy under its own pair with `1.0.0_SA_CTO~Z`'s half.

-- 2.0.0_SA_COO~R1
