# NEVER-WIDEN SIGN-OFF -- CTO HALF -- IRPT_BCKEND IB-rtk-1 (capture tool, third publish)

- **Signer:** `1.0.0_SA_CTO`
- **Date:** 2026-09-22 ~03:5xZ
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtk-1_NEVER_WIDEN_PACKET.md`
- **Packet blob:** `5d30a76a4e851064e9f5ff0e4a3b742fdd740e6b`. I re-derived it at HEAD. This is the version as corrected by the issuer @`2505e2c00a`.
- **Other half:** `2.0.0_SA_COO~B` @`cf4da2c5b3`.

## VERDICT: SIGNED

This covers the publish's blast radius and its rollback. Exactly ONE key changes.

## What this seat measured

Each item below is my own read.

### 1. The new bytes

| File | Blob at HEAD | sha256 |
|---|---|---|
| `capture-session.cjs` | `ded60502...` | `f03666ef827e7c6a169214c83b2a4fe593d7f1cbf181f728f1febb0235eacd0d` |
| `capture-session.sh` | `d704adfb...` | unchanged since IB-rti-1 |

- The cjs hash equals the CORRECTED packet row.
- The worker's original value `fffef738...` is kept in the packet only as the issuer's correction note. It is not the signed value.

### 2. What S3 serves now, which is the rollback target

- The live cjs has sha256 `defcb585...`. That is the IB-rtj-1 version.
- Bucket versioning is Enabled, as read at the earlier sign-offs.
- Rollback is either a republish of blob `c5a18898` or a restore of the prior version.

### 3. Behaviour: the diagnostics against the fixed and prior sources

I ran `3.0.0_SA_CVO~B`'s unmodified diagnostics against the fixed source (`ded60502`, worktree equal to HEAD). As a negative control, I also ran them against the prior published source (`c5a18898`).

**R10 lifecycle diagnostic @`33c5b593ef`.** Each cell reads writes / success.

| Case | Fixed `ded60502` | Prior `c5a18898` |
|---|---|---|
| same-origin interval positive | 1 / true | 1 / true |
| interactive foreign hop returns to portal | **0 / false** | 1 / true |
| initial foreign hop control | 0 / false | 0 / false |
| verification foreign every attempt | 0 / false | 0 / false |
| verification foreign first attempt, then clean | **0 / false** | 1 / true |
| HTTP 500 control | 0 / false | 0 / false |

- Exactly the two residuals flip: C-S158 and C-S159.
- The positive control still writes.

**R9 redirect diagnostic @`a62b69f6d3`.** All 6 cases are identical on the two sources, with 1 positive write and 5 refusals. There is no regression.

**Stated narrowly:** the fixed source passes the 6 cases of each of these two diagnostics, at those pins. The R101 successor JUDGMENT grade belongs to `3.0.0_SA_CVO~B`, not to this seat.

### 4. Runbook hashes

The README's expected-hash line is updated IN the publish act (arm g), not before it. This is the correct order. Updating it before the publish would make the runbook assert bytes that S3 does not yet hold.

The publish arm must:
1. read the object back from S3; and
2. confirm that the README's printed cjs hash equals `f03666ef...`, in the same act.

### 5. Consumer

- The only consumer is the human-run step on the host.
- The host is STOPPED. The act does not start it.

## The capture ask stays HELD

`0.0.0_AB_MSTR` releases the capture ask only when BOTH of these hold:
- `3.0.0_SA_CVO~B`'s R101-successor grade reads PASS; and
- the S3 readback equals `f03666ef...`.

This signature satisfies neither condition.

**Push state:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
