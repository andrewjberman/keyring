# NEVER-WIDEN SIGN-OFF -- CTO HALF -- IRPT_BCKEND IB-rtl-1 (capture tool, fourth publish)

- **Signer:** `1.0.0_SA_CTO`
- **Date:** 2026-09-22 ~06:0xZ
- **Packet:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IB-rtl-1_NEVER_WIDEN_PACKET.md`
- **Packet blob:** `3676e2a26e8018c3ba91627f3df8fdd0b4a96cc7`, re-derived at HEAD by this seat.
- **Other half:** `2.0.0_SA_COO~B` (`NEVER_WIDEN_SIGNOFF_COO_HALF_IRPT_BCKEND_IB-rtl-1_CAPTURE_TOOL_FOURTH_PUBLISH.md`).

## VERDICT: SIGNED

This covers the blast radius and the rollback for exactly ONE key.

## What this seat measured

### 1. The new bytes

| File | Blob | sha256 |
|---|---|---|
| `capture-session.cjs` | `82abe684...` | `b6f75a20150c170687ef2c1974b0a219a4ba56fc11a457b03b1fa688c68f353c` |
| `capture-session.sh` | `d704adfb...` | `17ae44f0...` |

- The cjs values are computed from the git object. They match the packet's table row (`:25`) and the README target (`:46`).
- The sh is unchanged.
- The packet also carries a second value, `b6f26643...`. It explains that this is the CRLF working-tree hash of the same file (`:19-20`, the S113 class). **The signed value is the git-object sha256, `b6f75a20`.**

### 2. The served bytes, which are the rollback target

- The live cjs sha256 is `f03666ef...`, the IB-rtk-1 version.
- Bucket versioning is Enabled.
- Rollback is either a republish of blob `ded60502` or a restore of the prior version.

### 3. Behaviour

I ran `3.0.0_SA_CVO~B`'s unmodified diagnostics on the fixed source (`82abe684`, with the worktree equal to HEAD). As a negative control I ran the same diagnostics on the prior published source (`ded60502`).

**R11 lifecycle @`d20200b92c`** (11 cases; each cell is writes/success):

| Case | Fixed | Prior | Row |
|---|---|---|---|
| storage-wait foreign hop, then portal | **0/false** | 1/true | C-S170 closed |
| non-navigation foreign response | **1/true** | 0/false | C-S171 over-refusal closed |
| storage-wait same-origin positive | 1/true | 1/true | control |
| non-navigation same-origin positive | 1/true | 1/true | control |
| interactive foreign navigation refusal | 0 | 0 | unchanged |
| same-origin 500 / timeout / missing-marker, then clean | 1/true each | 1/true each | the three retryable causes still recover |
| same-origin 404, then clean | **0/false** | 1/true | now terminal (see below) |
| same-origin non-timeout navigation error, then clean | **0/false** | 1/true | now terminal (see below) |
| same-origin password screen, then clean | 1/true | 1/true | the ordinary sign-in flow still works (W13-S1) |

- The two rows marked "now terminal" apply the one retry taxonomy from this seat's round-11 analysis (c): only timeout, 5xx and marker-absent retry. That is the ruled behaviour, not a regression.
- **R10 @`33c5b593ef`:** 6 of 6 cases identical to the prior source. 1 positive; 5 refusals, including both earlier residuals.
- **R9 @`a62b69f6d3`:** 6 of 6 cases identical. 1 positive, 5 refusals.
- **R8:** 3 of 3 guard cases write 0.

**Stated narrowly:** the fixed source passes the 11 + 6 + 6 + 3 cases of those four diagnostics at those pins. The R112 JUDGMENT grade is `3.0.0_SA_CVO~B`'s to give.

### 4. Consumer

- The only consumer is the human host step. The host is STOPPED, and this act does not start it.
- The README hash line is updated inside the publish act, to `b6f75a20`. The publish arm must confirm that line equals the S3 readback in the same act.

## The capture ask stays HELD

`0.0.0_AB_MSTR` releases the ask only when BOTH of these hold:
- `3.0.0_SA_CVO~B`'s R112-AC3 reads PASS;
- the S3 readback equals `b6f75a20`.

**Push state:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
