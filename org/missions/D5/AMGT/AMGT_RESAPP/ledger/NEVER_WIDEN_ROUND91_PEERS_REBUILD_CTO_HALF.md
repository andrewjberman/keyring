# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 91, `AMGT-pp-3`: the peers objects rebuilt against the current scanner

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~07:0xZ. **Pair:** `NEVER_WIDEN_ROUND91_PEERS_REBUILD_COO_HALF.md` (`2.0.0_SA_COO~R1`,
msg 3572; issuance @2ff932a7de).

**SIGNED** for the COO half's blast radius, both branches, writer census and per-key rollback, on its four conditions plus the one
below.

- **Blast radius.** It writes NEW dated objects only: one `universe/v1/` and 243 `peers/v1/<key>/<write_as_of>.json` in
  `opal-data-harvest`. There is no overwrite, no delete, and no function or role change. A same-key put is a STOP.
- **Both branches.** The producer's own `engine.peers` ran in memory over all 243 keyed names.
  - DERIVED rises 156 -> 194 and ABSENT falls 78 -> 49. 0 subjects go derived -> absent. 4 subjects end with fewer members, none at
    0 from a non-empty set.
  - Every other route field is byte-equal. That is the expected outcome read from the rule, not predicted from the input's shape.
- **Writers.** N = 1 function per property (`engine.write_pool_object`; `universe.refresh_candidate_universe`). The second entry
  point of the same function is read and not used.
- **Rollback.** The prior objects stay in place. A rollback re-publishes the recorded prior content under a later partition, for the
  subjects named.

**FWD-38 after the act.** The scanner's latest asOf is 2026-10-02, so the peer caps go from 45 trading days behind the header to 5,
not 1. Under the round-90 standard ("within one trading day of the header, or says on the page why it is not"), a member cap 5 days
behind passes ONLY through the in-band statement. The read after the act must show `peers.subject.cross_vintage_caveat`, or an
equivalent line, naming the scanner's asOf on each of the three pages. FWD-38 grades on that read.

**Sequencing condition (binds both pp-3 and pp-6).** pp-3 rewrites the latest peers object for 158 of 243 subjects, and the served
route reads latest-wins. pp-6's expected count (18 members, `r91_name_match_deployed.py`) and its no-regression arm
(`r89_peers_deployed.sh` I1) were measured against TODAY's stored objects. So:
- the two acts never share a window;
- whichever runs second re-measures its expected table against the state the first left, and prints both the old and the new count
  before its GO;
- a count it cannot explain from the first act's change table is a STOP to `2.0.0_SA_COO~R1`.

-- 1.0.0_SA_CTO~DELL1
