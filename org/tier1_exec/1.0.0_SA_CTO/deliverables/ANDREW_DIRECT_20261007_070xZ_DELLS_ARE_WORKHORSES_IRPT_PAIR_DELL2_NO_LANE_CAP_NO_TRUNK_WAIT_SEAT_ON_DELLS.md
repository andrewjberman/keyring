# ANDREW-DIRECT 2026-10-07 ~07:0xZ -- the Dells are workhorses: IRPT pair to dell2, no lane cap, no shared-branch wait, seat on the Dells

**Channel:** typed at the `1.0.0_SA_CTO` terminal (laptop). **Recorded by:** `1.0.0_SA_CTO`.

## His words, VERBATIM

"THe entire point of the Dells is that they are workhorses, they should be flying. I am ok with your move of the IRPT pair back to Dell2.
Definitely drop one lane cap and shared-branch wait for the dells. Yes i recommend seating the three lanes successors directly on the
dells."

## The three questions it answers, as this seat put them to him

1. "Move IRPT_BCKEND and IRPT_YCDGEN back to dell2, or keep both on dell1?"
2. "Drop the one-lane cap and the shared-branch wait for the Dells?" The table above that question described the wait as: "Deploy only
   from the shared branch, which site Z alone merges and pushes".
3. "Seat the three lanes' successors directly on the Dells rather than relaunching them on the laptop?" The three lanes are
   `2.0.0_SA_COO~P`, `~Y` and `~M`.

## What this seat does on it

- IRPT_BCKEND and IRPT_YCDGEN: `placement: DELL2` on both tree rows; `org/missions/SEQUENCE.yaml` rows and change_log. This reverses his
  ~06:1xZ word of the same night ("should both be on dell1"), on his own later word.
- The lane cap: `capacity.coo_sessions` loses its `dell1` and `dell2` entries, and the stage names lose the one-lane-at-a-time gating.
  He named no replacement number; none is written.
- The shared-branch wait: NFRA_CTLPLN PRD v0.9 amends FWD-5 and FWD-10 in place and C-IDENTITY, C-TRUNK-DEPLOY and C-ROLES. A Dell
  deploys its own committed, named candidate without waiting for another box. This is an ENDPOINT change: the ratified-text half
  re-opens for `3.0.0_SA_CVO`.
- Seating: one ask to `0.0.0_AB_MSTR` to relay the seating to each Dell's fabric manager.

## The layout after this word

| Box | Projects |
|---|---|
| dell1 | MDPF_SECHIST, MDPF_SECCLASS |
| dell2 | IRPT_BCKEND (three workstreams), IRPT_YCDGEN, IRPT_DASHBD, IRPT_CUSTDY, ADVI_COTBKF; ADVI_BILLING and NFRA_OPSWKF behind his inputs |

## Not decided by these words (surfaced, not adjudicated)

- HOW the wait is dropped. "Deploy from its own named candidate" is this seat's contract for it; he approved dropping the wait, not a
  mechanism. Who merges a Dell's round into the trunk afterwards is unchanged by this word.
- A Dell's lane limit, if any. He removed the cap of one and named no other.
- The serial a lane's successor takes on a Dell.
- `2.0.0_SA_COO~M` is live on the laptop for the MDPF_SECCLASS-S39 disarm (seated ~06:3xZ on this seat's ask, before this word). It
  finishes that act where it is.

-- 1.0.0_SA_CTO
