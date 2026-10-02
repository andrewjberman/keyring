# /self-drive AMGT_FRIDAY -- relaunch tick 1, `1.0.0_SA_CTO~Z`, 2026-10-02 05:1xZ

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_045xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RELAUNCH.md` @1e3216c005.
**state: ARMED.** Cron `81c504f6` runs hourly at :43 and is session-only.

## Startup (relaunch after the site-Z reboot)

- `/watcher`: re-registered, Monitor task `bh5auhogc`, script pid 4864. The census regex has to allow the quoted path
  (`inbox-watch\.sh"?`), because the SKILL.md form reads 0 rows on this device.
- Mail: 3 messages, all acked (28192, 28194 and 28199); delivery ledger 5/5 READ.
- LIVE_ARMS: landed the RELAUNCH sub-block @983e7540cb (MSTR~Z ask 28199), reported in msg to MSTR~Z.
- Audit-archive: 14 findings, all MANIFEST-ENTRY-MISSING-LIVE, UNCOVERED and baseline-missing. These are pre-existing
  classes. They are owned by the audit-archive tool and are not re-filed here.

## Scope (denominators printed)

| project | status | dep_stage | directive | COO loop |
|---|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | D5 SITEZ | ~X `/canonical-drive` 30m (cron 21a4937a) |
| AMGT_HARVST | active | EXECUTING | D5 SITEZ | ~H `/canonical-drive` 30m (cron b91f32c6, msg 28205) |
| AMGT_RESAPP | active | EXECUTING | D5 SITEZ | ~Z (confirmed by MSTR~Z summary) |
| DSGN_AMGTV1 | active | EXECUTING | D13 LAPTOP (register finding) | ~D (confirmed by MSTR~Z summary) |
| ETFS_RIVALS | active | EXECUTING | D5 SITEZ | ~RV `/closer-drive`, FAST lease 05:08Z-17:08Z, surface `data/etfs/scripts/rivalfunds` |

- Register: 15 live directives. D5 holds 94 open TOs.
- Sequence: none of the 5 is placed (`sequence-check --project`, rc 0, 0 flags each).
- Inbox: 0 unread.

## Calls this tick

- **COO~H item (5), "env-var credentials change offered to Andrew, unanswered": RULED WITHDRAW** (05:14Z). COO~H sent
  its card in msg 28215. The offer was to let the ft sign-in read credentials from an environment variable instead of
  Secrets; COO~H infers this from context and has not measured it. COO~H's rec was WITHDRAW, and the ruling follows
  it. Secrets-by-name is the ratified contract (`lib/opal_data_harvest/credentials.py`, HVST-ab-1 C-HV-TRUST-TOKEN).
  The rotated value is already in `astn/ft/credentials` v e7cace73. A second credential source would need a contract
  change that serves no outcome. The ruling went to ~H by message, and the item is closed.
- **ETFS_RIVALS:** routed to `4.0.0_SA_CRO~RV`, whose summary reads 0 open calls at HEAD 983e7540cb.
- **Tick 26's open item 1 is CLOSED:** the CLOUD commit `8b4ad05c38` (portal gitlink 24646bca) is an ancestor of
  origin/CLOUD (`merge-base --is-ancestor`).
- **Standing ruling 28084, unchanged:** AMGT_HARVST gold #4 runs after the bbg drain (323 pending at wind-down), or
  without it from 10:00Z, and before 13:00Z in either case. Owner: COO~H.

### Calls after the tick (05:15-05:25Z)

- **AMGT_HARVST, ai-5 repair cell (COO~H msg 28221, row Z-S58 @18ee3ffbd5): RULED YES.** The bbg drain is O(n^2):
  every row's silver_append re-reads 576 parts. The cell batches to one silver_append per source per pass, with a
  per-row fallback on SilverRowError. Paths are `uploads.py` and its test; risk class SERVED.
  - Condition: plant 1 proves that the batched pass writes the same row set (keys plus values) as the per-row path. A
    difference there is a served-output change and needs never-widen sign-off.
  - The real run is the live drain reaching 0 pending.
  - Gold #4 stays on ruling 28084.
- **DSGN_AMGTV1, Z-S10 (auth refresh 500): DISARMED by this seat as disarm_owner,** row Z-S13 @092047f79f.
  - Walks 20261001T151253Z and 164049Z: 8 of 8 post-login refreshes answered 200, and neither netlog holds a 5xx.
  - The evidence is the 5174 dev build proxying the shared auth backend, not a PROD read.
- **DSGN_AMGTV1 next limb (COO~D msg 28220): RULED HOLD, no round 22.**
  - Round 21's freeze, 3c37a01c, is live in PROD b3a1d8a6, and DEV takes no DSGN product change before Andrew's 09:00 ET
    read.
  - The next limb is L9 grading of the FWDs toward CLOSED.
- **CVO~Z is dark: spawn asked of MSTR~Z.** It is needed for the HARVST round 36 L8 compile, DSGN L9, and governance
  forks.
- **ETFS_RIVALS, rk-1 (CRO~RV msg 28218):** CRO~RV ruled it under its own authority. The carrier is the issuer's
  decomposition amendment, and nothing is owed by this seat.

## Acts only Andrew can do

1. The ETFS_RIVALS FWD-1 signed-in read, which needs his login (CLAUDE.md "his login or MFA code").
2. The CLOUD push of the 7 local commits ahead of origin 1f2346734b. MSTR pushes trunks on his word (LD-0367/0368).

## Completion test

NOT DONE: 0 of 5 projects read `complete`. Reachable: 5 of 5.

## Compiler Tools

- `directives-check.py --json`: scope resolved.
- `sequence-check.py --project` x5: 0 flags.
- `active-commitments.py`: 5 lines in 3 of 27 ledgers, none in scope.
- `fabric-check.py --agents`: 9 site-Z seats live. The `~D` row maps to NFRA_TRNSPT, which may be a project-mapping
  artifact, because MSTR~Z confirms `~D` on DSGN_AMGTV1. Left unverified.
- `audit-archive-invoker.py`: 14 findings.
- Gaps: `/watcher` census regex vs a quoted path, as above.
