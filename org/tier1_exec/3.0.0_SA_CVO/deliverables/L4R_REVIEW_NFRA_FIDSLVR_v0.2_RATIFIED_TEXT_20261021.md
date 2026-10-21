# L4-R re-review -- NFRA_FIDSLVR PRD v0.2 @88ebad1305, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-21 ~16:0xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 9131 and 9132, answering
`L4R_REVIEW_NFRA_FIDSLVR_v0.1_RATIFIED_TEXT_20261021.md` @51518ac061. Half hash `d8eea635282d`.

## Verdict: REFUSE (ground 1 only; grounds 2 and 3 are closed)

- **Ground 2, closed.** A script compared the fenced blocks at 88ebad1305: the PRD's ENDPOINT is IDENTICAL to the L2 record's. The record now
  orders FWD-1 to FWD-7, and FWD-7's SOURCE keeps Andrew's ~15:35Z words.
- **Ground 3, closed.** FWD-2's family list reads "... open lots, realized gain/loss, unrealized gain/loss", Andrew's ~15:20Z words. The diff
  from v0.1 to v0.2 of the L2 record is exactly that line plus the FWD-6 move.
- **Ground 1, stands.** Open call `dell1-20261021T154821Z-cc75` reads `[OPEN]`.
  - **The CTO's position (msg 9132)** is that cc75 is "listed, not waited on, per the proportionate rule", so that this signature and
    Andrew's confirmation are independent.
  - **The spine binds otherwise**, read at HEAD in `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`:
    - :120-121: "Andrew confirms the `DONE WHEN` line of every outcome here [L2]; it is his last touch point, and after L2 no limb waits
      on him." So his confirmation completes L2, ahead of L4.
    - :191: the ratified-text half requires the ENDPOINT "verbatim from the ratified pins". An unconfirmed endpoint has no ratified pin.
  - **The proportionate rule** (CLAUDE.md rule 27, L4-R) governs re-signing, the CRO-written brief half, and the notifier's wait on a
    wording change. It says nothing about the endpoint confirmation. By its own terms it covers a single-round or sub-week project, and
    this PRD plans later rounds (cell candidates, "Later rounds enrich").
  - **This PRD says the same:** "Andrew's confirmation of the DONE WHEN lines is an act on the box's open calls; this PRD goes to L4-R
    after it."
  - **Precedent:** ADVI_COTBOOKS (v0.1, v0.2) and NFRA_FIDUPL (v0.1 to v0.4) were refused on this same ground. NFRA_FIDUPL was signed on
    its re-delivery after his "Confirm as written."

## Re-delivery

Re-deliver after Andrew answers cc75. If he confirms FWD-1 to FWD-7 as they stand at 88ebad1305, this half is signed on that delivery with
no further reading. The v0.1 nit (C-EXT's `fidx_` sidecar names as builder output) carries.

-- 3.0.0_SA_CVO~DELL1
