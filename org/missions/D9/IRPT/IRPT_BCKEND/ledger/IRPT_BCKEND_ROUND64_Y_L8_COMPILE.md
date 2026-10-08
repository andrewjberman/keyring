# IRPT_BCKEND round 64, workstream ~Y -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~Y2` (issuer, dell2) **for** `3.0.0_SA_CVO`, 2026-10-08 ~17:2xZ. The round is WORLD by the L6 gate's
floor (on `lambda-source-map.json`). Decomposition: `decompositions/IRPT_BCKEND_DECOMP_R64_Y.md`. Issuance: @6c7fd403f0.
The cell is the release-2 repin ruled by `1.0.0_SA_CTO~DELL2` msg 1089 (release 2 = this repin plus the smoke test).

## Terminality

**1 of 1** order is terminal: `IRPT_BCKEND.TO-IB-yr-641`, status complete. Its proof instance is VALID, as read by the
worktree's own checker. Drained @f7a9d0b34f (3 paths needed, 0 dropped, 0 foreign; the index check shows 0 of 3 differ).
`python .tools/round-close-check.py --project IRPT_BCKEND --round 64`: `orders=2 judgment=0 ungraded=0 verdict=MAY-CLOSE`.

**Reboot note.** The first worker instance committed the repin @bfe123b5d1 at 15:07Z, and then dell2 rebooted at 16:38Z
before the proof and the status flip. A fresh `worker-light` on the same worktree checked the commit without changing it,
re-ran both criteria, wrote the proof and flipped the status @17b5bd4bc2.

## The cell and what it delivered

In `infra/aws/lambda/ci/lambda-source-map.json`, row `irpt-ycharts-generate`, three `staged_from` rows moved from pin
`3f29017cfc` to `f09b802cdc9b5b96a8da9aefe864107327a43cb0`. No other row or field changed.

| packaged_as | new sha256 (= sha256 of the blob at the pin) |
|---|---|
| `uploads.py` | `47f89e0b46609c5b70fc944acae33454e2da433cc3bdd3c1974d8ee984c9337d` |
| `interactive_access.py` | `c28d9a74c9af2c5d5014ae54ffda388c2666d24e9c98ac42df3ace457e59e684` |
| `generate_installed.py` | `d878d10731f4e0d76a2b58b26fd7e0dd43e5d4febfbb87c626eabacd07a05e62` |

| criterion | issuer run | worker run |
|---|---|---|
| Y64-1-AC1 (`release-census.py --pin HEAD`) | `changed_members=3` at bfe123b5d1 and again at f7a9d0b34f; the same three names, built vs live hashes printed | `changed_members=3`, 3 of 100 members |
| Y64-1-AC2 (`BUILD_ONLY=1 build-and-upload.sh`) | base control at f09b802cdc: OK, 63 .py | `OK: import-closure -- 63 packaged .py file(s)`, nothing uploaded |

**No judgment criteria. No rows filed.**

**Not exercised:** nothing is served. The live function is still `ZspX0qD2..` (release 1). Release 2 is a later act: it
needs its own never-widen pair, and per the issuance it waits on Andrew naming a real filer entitlement.
`2.0.0_SA_COO~V2` (TCKT_VNEXT TV-r-1) waits on X-1 being live.
