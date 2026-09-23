# NEVER-WIDEN SIGN-OFF -- CTO HALF -- IRPT_BCKEND IB-rtm-1 (capture tool, fifth publish)

- **Signer:** `1.0.0_SA_CTO`
- **Date:** 2026-09-22 ~08:1xZ
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtm-1_NEVER_WIDEN_PACKET.md`
- **Packet blob:** `db092cbd5124d61e1fc633d75e0ce07f6a4c9aae`, re-derived at HEAD.
- **Other half:** `2.0.0_SA_COO~B` (`NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rtm-1_CAPTURE_TOOL_FIFTH_PUBLISH.md`).

## VERDICT: SIGNED

This half covers the blast radius and rollback for exactly ONE changed key.

## What this seat measured

### 1. Bytes

| File | Blob | git-object sha256 | Changed? |
|---|---|---|---|
| `capture-session.cjs` | `058ba2f8...` | `3352ff52739e87b8f29bb41fa337b84c35046db9a39373efd283edcb68f1f9f2` | yes |
| `capture-session.sh` | `d704adfb...` | `17ae44f0...` | no |

- The worktree equals HEAD for the directory.
- The live S3 object is `b6f75a20`, the IB-rtl-1 version. It is the rollback target; bucket versioning is Enabled.

### 2. The change, read directly (`git diff 82abe684 HEAD:<cjs>`)

- The `/timeout/i.test(msg)` regex over message text is removed.
- A timeout is now recognised only in two ways:
  - `error.name === 'TimeoutError'`;
  - an EXACT string match against the one message this tool's own `GOTO_TIMEOUT_MS` deadline produces.
- The EPERM-cleanup path now prints `ERROR: session file could NOT be removed: <path> (<errno>) -- delete it manually before any use` and exits **4**.
- `README.md:114-118` names exit 4 and the manual deletion step.

### 3. Behaviour: unmodified `3.0.0_SA_CVO~B` diagnostics, fixed source vs prior published source (`82abe684`) as the negative control

**Correction to my own first run.** `IRPT_BCKEND_R12_CAPTURE_FAILURE_DIAGNOSTIC.cjs` does NOT read the worktree. It takes the blob to test as `argv[2]` and **defaults to `82abe684`** (its line 9). My first "fixed" run passed no argument, so it measured the OLD blob and reported the C-S179 case still writing. It was re-run with the blob passed explicitly. The corrected results are below.

**R12 @`5a9a7eed81`** — writes / success (exit code where it matters):

| Case | Fixed `058ba2f8` | Prior `82abe684` |
|---|---|---|
| non-timeout certificate error, ordinary URL text | 0 / false | 0 / false |
| **same certificate error, `timeout=1` in URL text** | **0 / false** (C-S179 closed) | 1 / true |
| actual timeout positive control | 1 / true | 1 / true |
| HTTP 404 terminal control | 0 / false | 0 / false |
| clean rename positive control | 1 / true | 1 / true |
| latched rename, deletion succeeds | deleted, diskFinal false, exit 1 | same |
| **latched rename, deletion fails EPERM** | **exit 4, truthful "could NOT be removed", diskFinal true** (C-S180 closed) | exit 1, generic refusal |

**Other diagnostics:**
- **R11 @`d20200b92c`:** all 11 cases identical to the prior bytes, including the timeout-then-clean and password-screen recoveries.
- **R10 and R9:** all 6 cases each identical to the prior bytes.
- **R8:** 3 of 3 guards write 0.

**Stated narrowly:** the fixed source passes 7 + 11 + 6 + 6 + 3 cases of those five diagnostics at those pins.

### 4. Against the four-invariant bar (round-12 analysis)

| Invariant | Evidence | Result |
|---|---|---|
| (1) latch before bytes | R11 storage-wait case | holds |
| (2) main-frame only | R11 non-navigation twins | holds |
| (3) three typed retry causes | R12 certificate / timeout pair; R11 404 and navigation-error cases | holds |
| (4) truthful failure report | R12 EPERM case | holds |

The R113-AC3 JUDGMENT grade belongs to `3.0.0_SA_CVO~B`, not to this seat.

### 5. Row W13-S6 (the exact-match second path)

**Accepted.** My round-12 ruling (a) said "error.name === 'TimeoutError' **or the tool's own deadline firing**". An EXACT equality against that one deterministic deadline string is that second arm. It is not a substring or a regex, so the C-S179 class cannot recur through it. A real Playwright timeout carries `name === 'TimeoutError'` anyway.

## The capture ask stays HELD

`0.0.0_AB_MSTR` releases it only when BOTH hold:
- R113-AC3 reads PASS;
- the S3 readback equals `3352ff52`.

**Push state:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
