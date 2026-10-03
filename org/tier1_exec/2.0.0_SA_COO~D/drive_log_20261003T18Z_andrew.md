# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 18Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 18:0xZ | IRPT_DASHBD B1 (~P B1 GO 104674) | the P-2 window, B1 | P-3 + P-6 LANDED portal `19796bc0` (DEV e862b0c4 merged in; tests 11 of 11; typecheck rc=0) | DRIVE FORWARD |
| 18:0xZ-18:3xZ | DSGN_IRPTV1 (FAST) | Andrew-direct change 2 | the Securities map's chips say "Sleeve:", plus a "Sleeve: Client" sleeve; LANDED portal `2f326afc`; B2's DEV head sent to 0.0.0_AB_MSTR + ~P | DRIVE FORWARD |

## Change 2

- Words (~18:0xZ, with a screenshot of the Securities map): "I think we should use the term 'Sleeve' not 'Model' for
  these various bubble segments. Additionally, there should be a sleeve called 'Client' which is just the Client
  residual that is not attached to a Model or SMA Strategy."
- Before: one chip per model ancestor; a security with no model above it had no chip. The residual read a bare
  "Client", and only when an entire model's securities were residual.
- After:
  - every chip reads "Sleeve: <name>";
  - each account has one "Sleeve: Client", last. It covers the residual sleeve, plus securities with no model or
    strategy above them that are not under a Models or SMAs category;
  - chips filter by their own securities.
- Pin holdings-sleeve-chips; the DEV file fails it exactly as the screenshot showed. iv-e-114 arm D and iv-e-44 pinned
  the old words and are re-worded; every other assertion in them is unchanged.
- Live walk `20261003T182601Z` (local): the chips read "Sleeve: ...", and there is no Client chip on a client that is
  all Models. A client with a residual was not walked: the screenshot's account was not identified to this seat.
  Andrew can see it on 5174.

## Landing mechanics

- The main checkout's fast-forward to B1 stopped on two uncommitted wire files. All 20 such files equalled DEV head
  ignoring line endings. Their 15:53Z mtime matches this seat's own suite run in the main tree (the gen-wire
  idempotence test regenerates them). The two blocking files were reset (lossless; the fast-forward wrote the same
  content back); 18 CR-only files remain as they were.
- Lease reads of FULL at 17:4xZ and 18:1xZ were taken from inside the portal worktree, where drive-mode.py cannot see
  the main worktree's lease file and fails closed. The lease was FAST throughout (re-armed 17:48Z to 19:48Z). The DEV
  push at 18:1xZ was admitted by the gate. Read the lease from the workspace root.

## Open

- 0.0.0_AB_MSTR is promoting DEV 2f326afc to PROD (B2) and froze DEV pushes (104683) until PROMOTED.
- The held branch `coo-d-regime-readings` (four commits) lands after the freeze lifts. Andrew has not said whether he
  wanted it in this push; it is not in it.
- ~Y's Aproxy live run waits on ~Y's re-confirmation against Andrew's data-collection review.
- 0.0.0_AB_MSTR 104675 relays an NFRA_TRNSPT ask (the meeting allowlist values) because the owner, ~T, is not live.
  Parked: this seat answers after the promote. The meetings may need Andrew's choice.
