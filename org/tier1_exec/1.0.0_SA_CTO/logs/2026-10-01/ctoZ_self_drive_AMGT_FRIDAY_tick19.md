# /self-drive AMGT_FRIDAY -- tick 19, `1.0.0_SA_CTO~Z`, 2026-10-01 20:46Z-21:47Z (freeze at 22:00Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_040xZ_SELF_DRIVE_60M_AMGT_FOUR_PLUS_ETFS_RIVALS_ARM_ON_CRO_BRIEF.md`. **state: ARMED.**

## Scope state (measured at 21:45Z)

- **Projects:** 5 of 5 `active`, 0 `complete`.
- **THE FREEZE CANDIDATE (22:00Z): portal DEV `3c37a01c`** (DSGN round 21, walked clean).
  - The backend it reads is live: RESAPP aj-2 since 13:59Z, and HARVST gold #3 since 20:12Z (served, 54 of 95 names with a
    collected month).
  - CORPUS's face is complete.
- **ETFS_RIVALS:**
  - d-5 landed: AC2 and AC3 PASS; AC1 FAILs on the GQGU clause only.
  - Addendum 1 (the G2 own-capture fix) is signed by both halves (COO @ad07f847d2, CTO @1ef54f4ff8), and A1-A3 are issued (84384fc1f7).
- **AMGT_HARVST:** round 36 is in flight. Overnight unattended collection runs 03:00-11:00Z.
- **Inbox:** 0 unread. Acked: 28060, 28066.
- **Push state (ls-remote), MEASURED:**
  - **Origin CLOUD MOVED to `25f4ac5418`** (a `1.0.0_SA_CTO~O` log commit, 21:27Z), so this fabric's AMGT records are now on origin
    (`6cbef26707` is an ancestor). I did not push it; whoever pushed did so outside this seat.
  - Origin CLOUD's portal gitlink is still `b336b141`.
  - Origin portal DEV is `d79b9934`; local DEV is `3c37a01c`, not on origin. `merge-tree` returns rc=0.
- **Completion test:** NOT DONE. 0 of 5 are complete, and all 5 are REACHABLE.

## Acts taken

| act | hash |
|---|---|
| RIV-d-5 addendum 1, CTO half SIGNED (q-1 fix in the pin; G2 delta GQGU +307 and the other 12 unchanged; 0 cross-fund rows; control 4,094 of 4,094; live base = d-5 17:46Z) | `1ef54f4ff8` |

## Acts only Andrew can do

1. **PROD for the demo** (CLAUDE.md Git: `0.0.0_AB_MSTR` pushes trunks on Andrew's word).
   - The act: pull-merge origin portal DEV `d79b9934` into `3c37a01c` (never a rebase), push DEV, then promote DEV to PROD.
   - The promote also carries 14 commits from other seats: 13 DSGN_IRPTV1 and 1 MDPF_TAXSMA.
   - The CLOUD side is already on origin.
2. **A HARVST residential arm, if wanted** (vendor per-use word; R7).
3. **Web search for the rivalfunds AI, if wanted** (vendor per-use word; FWD-17).

## Compiler Tools

`git ls-remote`, `git fetch` + `merge-base --is-ancestor`, `git ls-tree` (gitlink), `lambda list-functions`, broker `send_message`/`ack_messages`.
