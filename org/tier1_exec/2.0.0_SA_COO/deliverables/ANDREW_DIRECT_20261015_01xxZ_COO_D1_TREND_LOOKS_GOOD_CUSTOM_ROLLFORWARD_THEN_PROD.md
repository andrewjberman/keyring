# Andrew-direct 2026-10-15 ~01:1xZ (dell1, `2.0.0_SA_COO~D1` terminal) -- the Global Trend smoke: "It looks good", Custom Models needs roll-forwards, then PROD now

## VERBATIM

> "It looks good! [a screenshot of the Global Trend as served on http://localhost:5174/, signed in as an internal user: the full-history Trend, Nov 2024 to Oct 13, with the Composition footnote and the Carried forward legend entry]. Only thing is need rollforwards for the the Custom Models. This is good though, let's get that sorted for PROD now"

Said at this seat's terminal after smoking the build on 5174 (portal `wk-MDPF_CANON-27-portal` @d0390f1ac1, plain `dev:live` reading the real served Global object published 2026-10-14 23:10Z to 23:11Z).

## The seat's reading (the verbatim governs; this is not adjudicated wider or narrower)

- **The build is accepted as the Trend he wants**, with ONE change: the Custom Models series rolls forward (carries the last known value) where it has no value, as the other groups already do on the carried dates. The seat cuts that change as an amendment of cell `CN-p-2` and does not widen it to any other series.
- **"Sorted for PROD now"** is read as his word to take the Trend, with that change, to PROD. It is the client-facing exception in CLAUDE.md (Agent Autonomy: a portal PROD push that changes a client-facing page waits on his word): this record is that word for the page `/portfolios` (Model Portfolios) and for the candidate that carries the Custom Models roll-forward. The held approval row `dell1-20261014T230556Z-a196` (head `9f5bbbca`, before the roll-forward) is superseded by a row on the new head; no PROD push happens on the old head. The route is the law's: DEV only by `portal-merge-forward.sh` on an approved row, PROD only by a chosen-set promote (the box CTO and the Tier-2 deployer); the data the page reads is already served (gold and served plane, 2026-10-14 23:11Z).
- **Not decided by this record, put to the CTO:** none; the CTO runs the approval row and the promote.
