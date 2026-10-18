# /self-drive dell1 box -- ticks 130-131 (`1.0.0_SA_CTO~DELL1`, 2026-10-18 18:14Z-18:48Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec.
Covers everything since the tick-129 log (@ad524d91ab). Tick 130 (18:18Z) was quiet. **state: ARMED.**

## Inbox (0.8)

0 unread at 18:48Z. Read and acked: 8201, 8206, 8212, 8213.

## Acts taken

| project | act | hash |
|---|---|---|
| AMGT_HARVST r99 | cn-3 COO half ca850150 read. **One edit named** (msg 8204): the half's 6000-request budget had no enforcing instrument, while the driver stops at 14000 read requests and 1.8 GiB (`dossier_refresh.py:61-62`). W1 edited it (f4bff167 @184cfe4b73); the diff changes the budget line only | msg 8204 |
| AMGT_HARVST r99 | **cn-3 CTO half SIGNED**, binding f4bff167. 93 dossiers are added, add-only; N=1 writer (`dossier.py:1651`); the guard reads through `_model_block_read`. Conditions: pin 56bacbc853, A-3 block-key STOP, site Z CLEAR first, window closes 12:30Z 10-19, step-2 wall time to the cn-4 host rule (over 600 s means Fargate), committed NEVER-2 close | 98c304e18f |
| NONE | **Act row e5fe added for Andrew:** dell1's session 1 is Disconnected and locked (quser 18:42Z, re-read at 18:48Z: Disc, idle 1:47). `/unstick` cannot focus a window, so SC1 has not picked up the cn-3 GO (8209). MSTR withdrew its unmeasured line that seats with watchers still get mail (8213). One measured case: this seat received 8212 and 8213 through its watcher while the session was Disconnected | open-calls e5fe |

## Open calls (Step 1)

The list has 149 rows, 5 open:
- 4 are acts only Andrew can do;
- 1 is escalated: 48ae under XA-cbaa, at the laptop CTO, asked again at 17:20Z.

## ACTS ONLY ANDREW CAN DO

- **e5fe (new):** reconnect and unlock dell1's desktop session at the machine. Citation: physical presence; MSTR will not unlock it.
- **0cf5:** confirm ADVI_COTBOOKS's 6 DONE WHEN lines. Citation: L2, rule 27.
- **89c9:** the SOC2_MSLOGS round-2 re-derive. Citation: it needs his MFA session.
- **e1ee:** restart the dell2 box manager. Citation: physical presence at the machine.
- **FWD-10 client-facing PROD push.** Citation: the portal PROD rule.

## Watch

- cn-3: site Z's CLEAR, then SC1's run, which needs the session unlocked.
- RESAPP round 122 issuance.
- XA-cbaa.

## Compiler Tools

None run. The measurements were:
- `git show 56bacbc853:` reads of `dossier.py` and `dossier_refresh.py`;
- sha256 of the COO half at both versions;
- quser.

-- 1.0.0_SA_CTO~DELL1
