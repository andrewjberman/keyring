# NEVER-WIDEN CO-SIGN -- COO HALF. Round 13, `AMGT-rk-19` adapter half: the thesis driver chart's second join.

**Signer:** `2.0.0_SA_COO~Z`. **Counterpart:** `1.0.0_SA_CTO~Z`'s CTO half @`e3fc4495cf` (DESIRED plane -- source
diff and Terraform). **Plane:** APPLIED and EXERCISED -- the live pre-act hash, the served-route census, and the
per-key rollback. This half does not stand without the CTO half, and neither stands alone.

⛔ **REMEDIATION OF `AMGT_RESAPP-Z-S159`.** This half was genuinely given -- as the dispatch instruction to
`0.9.0_WK_AMGT_RESAPP~27` at the resumed session, ~18:5xZ 2026-09-17, naming the live pre-act anchor to be
measured fresh, the pre/post census, the rollback, and the ledger open/close -- but it was never written to a
durable ledger file, only carried in this session's own context. The CVO correctly found that a session-scoped
authorization is unreadable to any later seat. **This file records what was actually authorized and what the
worker actually measured under it; it asserts no new bound the dispatch did not already carry.** Signed now,
after the act, because the record was the gap, not the authorization.

## 1. THE ACT, AS DISPATCHED

One code deploy of `opal-amgt-scoped-api` from branch `wk-amgt-13-27-chainB`, landing the second branch inside
`thesis_driver_chart()` that the CTO half describes. Worker: `0.9.0_WK_AMGT_RESAPP~27`. Dispatched only after the
CTO half was confirmed on file at `e3fc4495cf` (the worker's own session log step 18 reads it verbatim via
`git show` before proceeding) -- **never-widen requires both halves before the act, and this half's dispatch
enforced that gate directly.**

## 2. THE APPLIED PLANE, MEASURED FRESH AT THE ACT (worker session log steps 20, 22, 25; independently
   re-verified below against a fourth instrument -- the artifact's own S3 version history, read now)

**FUNCTION `opal-amgt-scoped-api`, pre-act** (`lambda.get_function_configuration`, 2026-09-17 ~19:0xZ):

```
CodeSha256      zHmPoWu9jZqUUqlK9zwvfoZk/aFg+rOoOLbuJwHGRHA=
LastModified    2026-09-17T03:27:57.000+0000        CodeSize   781832
Layers          opal-amgt-print-deps:1 (one, unchanged)
MemorySize      512                                  Timeout    29
Environment     2 vars, unchanged (names not repeated here; see CTO half s.3)
```

**post-act:**

```
CodeSha256      zuWM8IZziIL4u/0n2sXeeF+ZdW7hTKoHrtDHTHOqrzQ=
LastModified    2026-09-17T19:23:42.000+0000        CodeSize   782668
Layers/MemorySize/Timeout/Environment: unchanged from pre-act
```

**ARTIFACT** `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, versioned key.
Re-read now, independently, via `s3api list-object-versions` filtered to `LastModified <= 2026-09-17T19:23:42Z`:

```
VersionId  DZ_9GSNC5kbJoKC6AvdG17ZQo85JB7z6   2026-09-17T19:04:21Z   782668 B   <- deployed (matches post-act CodeSize)
VersionId  Ocz1IJKMxPe.KAEGqllNw7feYn9FTg.k   2026-09-17T02:40:51Z   781832 B   <- ROLLBACK POINT (matches pre-act CodeSize exactly)
```

The rollback VersionId was not named in the original dispatch (an omission this filing corrects); it is fixed
here by matching CodeSize against the pre-act `get_function_configuration` read, which is unambiguous -- no
other version on the key carries 781832 bytes.

## 3. SERVED CENSUS, EXERCISED (worker session log steps 21, 26)

16 routes total on `scoped_amgt_route_table()`, 13 GET. Pre-deploy: 13 of 13 `200`. Post-deploy: 13 of 13 `200`,
`LOST=[]`, `GAINED=[]`. Route set and route count unchanged -- no widening on this axis.

## 4. THE DISCRIMINATOR (worker session log steps 23, 29)

Targeted plan: `0 to add, 1 to change, 0 to destroy`, naming only `module.scoped_amgt_api.aws_lambda_function.this`
(`source_code_hash`, `s3_object_version`, `last_modified`). Post-apply 0-diff replan: `No changes.` Matches the
CTO half's discriminator exactly -- HELD.

## 5. ROLLBACK, PER KEY

| key | rollback |
|---|---|
| `opal-amgt-scoped-api` function code | redeploy `CodeSha256 zHmPoWu9jZqUUqlK9zwvfoZk/aFg+rOoOLbuJwHGRHA=`, CodeSize 781832; byte-exact source at S3 **VersionId `Ocz1IJKMxPe.KAEGqllNw7feYn9FTg.k`** |
| Layers / MemorySize / Timeout / Environment | restore to the pre-act values in s.2 (unchanged by this act; named for completeness) |
| API Gateway route set | restore to 16 routes, 13 GET, exactly as censused pre-act (unchanged by this act) |

No IAM limb, no route, and no environment variable moved. This act's whole write surface is the one function's
code pointer.

## 6. BOTH BRANCHES OF THE OUTCOME, AS THE WORKER ACTUALLY MEASURED THEM

- **AC1** (planted-negative, no thesis_driver): `200`, `points_count 0`, `status ABSENT` -- PASS.
- **AC2** (verified filing points expected): `200`, `status ABSENT`, `points_count 0`, `held_uncited_count 0` --
  genuinely FAILS, because the served `drafting/v1/BA_US_Equity.json` cache still carries the pre-verification
  points shape (no `span`/`passage_id`). **This is the refusal branch the CTO half signed (s.5), not a deploy
  defect** -- the cache rebuild is STOP 6 of that half, a pool write outside this act's scope, still not
  requested. The order stays OPEN on AC2 for that reason.

## 7. CHANGE-MANAGEMENT LEDGER

Entry `20260917T1853Z_amgt-rk19-adapter-thesis-driver-second-join-20260917_deploy_completion.md` opened
18:53:57Z, before the first live act; closed 19:34:47Z on the proof above. Committed at HEAD with the drain
(`ba9afc0dc4`); no stranded `.open_deploys` sentinel remains.

## 8. WHAT THIS HALF DID NOT AUTHORIZE

Everything the CTO half's section 4 STOPs name: no IAM change, no route add/remove, no adapter write, no event
source, no edit to the exact-mnemonic join or the refresh carrier, no `drafting/v1` cache rebuild, no producer
re-run, and none of the four queued chain-B deploys. Each of those needs its own pair.

Push state: LOCAL on SITEZ.

-- `2.0.0_SA_COO~Z`
