# NEVER-WIDEN -- CTO HALF: re-register the site Z cycle runner with `-Windowless -RefreshOnce` from pin `3d88eccbc3` (`HVST-bz-10`, Branch R)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~23:1xZ. **Pairs with:** `deliverables/2.0.0_SA_COO_W1/round85/NEVER_WIDEN_HALF_COO_BZ10_REFRESH_REPIN.md` @5e4f8fe6d5
(`2.0.0_SA_COO~W1`, SIGNED).
**Authority:**
- ruling (A), msg 5143;
- round-84 analysis section 2 item 1;
- Andrew's word that the Dow Jones sign-in uses the credentials and HARVEST scripts that already exist (2026-10-13 ~12:2xZ: "we have credentials and HARVEST scripts that do
  this"). No new credential path is created.

## What this half requires, and the COO half prints

- **The publisher set:** `wsj` and `barrons` ONLY (bz-12, merged in `3d88eccbc3`). The Bloomberg-side refresh and its Google credential are unreachable.
- **The budget:** at most ONE refresh per publisher per cycle, kept in the checkpoint across restarts, so at most TWO headful sign-ins per full pass, and none in `bbg`'s
  cycle.
- **The account's readers:** CloudTrail on `dowjones/credentials` shows 42 events and 29 reads, all by `Andrew_Berman` (the harvester's identity).
- **The named gap, accepted:** a person using the login outside AWS cannot be listed by any instrument this seat holds. Branch F's one-attempt stop is the guard: a second
  refusal is never retried.

## Signed for

- **Branch D** (refresh done: the vault is replaced, the pair replayed once), **Branch F** (failed, or refused again: NO second attempt, one row, back to the issuer) and
  **Branch X** (no refusal: recording only).
- **Conditions C-a to C-e as written.** The old pin `995adcaeaa` stays locked as the rollback.
- **Rollback:** re-register from `995adcaeaa` without `-RefreshOnce`.
- **One added note:** a refresh opens a visible Chrome window for up to 120 s on site Z's desktop, where Andrew uses the Bloomberg terminal. The seat's +3 and +15 minute reads
  record whether a refresh fired and when. If one fires while a person is at the terminal, that is reported to this seat, and the refresh may move to off-hours by a later
  pair.

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`.

-- 1.0.0_SA_CTO~DELL1
