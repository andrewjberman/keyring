# /self-drive dell2-box -- ticks 163-164 (2026-10-20 ~08:57Z-09:56Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 163 and 164, since the tick 162 log (@186e3f0daa). state: ARMED.

## The v0.24 Ticket Center form is LIVE on PROD

- **LIVE** as portal-v2.1.247, f48e09dd, at 09:28:44Z; run 39400700239 (`~Y2` msg 11294, DT msg 11296).
- **Read here:** origin/PROD is f48e09dd; the site's Last-Modified is 09:28:38Z.
- **The DT's staff read** is ABSENT: no sanctioned staff login.
- **Fold f10f** (PROD into DEV): APPROVED. Read here: 0 files differ from DEV, and origin/PROD and origin/DEV are both ancestors.

## The packager blockers (run 6 P4)

- **Blocker A**, the 403 (IB2 msg 11291, `A_PACKAGER_403.txt`): the gateway authorizer refuses with `ORIGIN_VERIFICATION_FAILED`, because
  the packager calls the direct execute-api host. The token is valid to 2027-01-09.
  - **Ruled:** route through CloudFront. The authorizer is NOT changed and the origin secret is NOT given to the resident.
  - `~Y2` msg 11298: it is a binding (`--packager api_base`). r34n = r34m v2 with only `api_base` set to `https://opalinvest.dev` (2 members),
    as AR-y-450.
  - AR-y-449 reads whether the edge function and authorizer admit a service Bearer.
  - AR-y-451 is an alias probe, run before any install.
- **Blocker B**, the IAM gap: the grant's CTO half is SIGNED @c72cacf853 (blob 4322982199). Read here: +21/-0, one statement, GetObject and
  GetObjectVersion, prefixes registry-derived. The GO went to IB2 at 09:31Z.

## Rulings

| item | ruling |
|---|---|
| A live staff read (`~Y2` msg 11294) | No agent uses a real person's login. Run 7 files through the PROD page as the pair's synthetic staff user. |
| ADDENDUM 9 (run 7 through the portal page; blob 8e355eb836, sha256 17f32c72) | CTO half SIGNED @663ddfd135. It grades FWD-1, FWD-2 and FWD-8 live. It starts after the IAM grant and r34n close green; a real name or figure in a screenshot is a STOP. |
| The order | IAM grant, then the alias probe, then r34n, then run 7. Outside 11:30Z-14:15Z. Never two at once. |

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"):
  - `C:\dev\wk-irpt-dashbd-503`;
  - row 544d;
  - row 65a1;
  - row a392.
- **S3 deletes:**
  - row 6e7c;
  - row 128f;
  - the synthetic leftovers of runs 5 to 6.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
