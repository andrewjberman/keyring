# DELL1 self-drive box -- tick 202, 2026-10-20 ~19:48Z (delta: FIDUPL device-trust cause settled, XA-72a8 ruled, 49F xref restored)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 19:48Z. Acked since tick 201: 8769, 8772, 8774, 8776.
- open_calls.json: 163 rows, 5 OPEN.
  - Acts only Andrew can do: 89c9, ea86, 5013 (withdrawn in substance) and 3bc7 (new).
  - Fork 3d0c: ruled at cross-adjudication, close pending.

## Acts and rulings
- **NFRA_FIDUPL attempt 10** (P1 8769):
  - In headful real Chrome the username step passed, and the password POST was SENT. It answered 403 "Not Authorized".
  - ATT was absent at the POST. The Akamai and ThreatMetrix cookies were present.
  - The one-attempt rule binds, and there is no retry.
  - Act row 3bc7 for Andrew: a hand sign-in on the box through `tmp/fidupl` 02, 03 and 05.
- **CRO 8772** (`RESEARCH_20261020_NFRA_FIDUPL_ATT_IS_PERSISTED.md` @cbd22974b6):
  - ATT is persisted from an earlier session and is never minted at login. It is set only by the post-login virtual-assistant calls on
    `digital.advisorchannel.com`, so a fresh profile is refused regardless of the browser mode.
  - Andrew's hand sign-in is both the fix and the test. If it is also refused by hand, the next capture is the Certified Browser
    enrollment.
  - P1 confirmed that nothing blocks `digital.*` (8774), and its cookie-name reader is ready.
- **XA-20261020T184817Z-72a8 RULED** by the laptop CTO at 19:36:57Z: (a) Fargate, with four conditions.
  - The conditions: LGIC names; the schedule on its own clock; the task definition pinned by digest; the co-7 apply under its pair.
    W1 was told.
  - `open-calls.py close --xadj` refused because the laptop's record file has not synced to dell1. I retry after box-sync.
- **The 49F `dim_account_xref`** (laptop COO~C via MSTR 8776): RESTORED. dim-convert now has 3008 MB, and one run wrote
  `date=2026-10-19`.

## Scope state
- **NFRA_FIDUPL:** FU-x-1 and FU-s-11 are pending; everything else is complete. 0 objects under `fidelity/`. The 3 fetch rules are
  DISABLED. All runs wait on 3bc7.
- **AMGT_HARVST:** round 100. co-6 is building on Fargate.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **3bc7:** the Fidelity hand sign-in on the box (his login).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `xadj.py show`.
- `open-calls.py add` and `close` (refused).
- `ssm list-commands`.
