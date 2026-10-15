# ANDREW-DIRECT 2026-10-15 ~16:3xZ -- move all HARVST operations to dell1

**Channel:** relayed by `2.0.0_SA_COO~O` (site Z), its msg 34494, to `0.0.0_AB_MSTR~Z`, which carried it to
`0.0.0_AB_MSTR~DELL1` over agentbus (bus id `db26b668-4857-4058-86f6-f6a6e4674e80`, 2026-10-15T16:37:02Z). The
original terminal and exact time are not in the relay; "~16:3xZ" is the relay's own stamp.

**VERBATIM (as relayed):**

> "Yeah we can move all HARVST operations to Dell1, including Seeking Alpha + Bloomberg as well. I will also handle FT for them soon enough. Dell1 has more capacity to run these kind of ops so better to just move all that to them as a function of moving all AMGT work over to that box. Let CTO and MSTR know that so they can communicate this and update the repo as needed."

**Relay note (site Z MSTR, not Andrew):** this widens `1.0.0_SA_CTO~Z`'s 16:2xZ ruling (drop wsj and barrons,
`CTO_RULING_SITEZ_HARVEST_RUNNER_DROP_WSJ_BARRONS_20261015_Z.md` @86581c31be) to all publishers, sa and bbg
included, FT to follow. Site Z has made NO change to its runner yet. The handover order (when site Z stops each
publisher vs when dell1 starts it, so no publisher has zero writers) is for `1.0.0_SA_CTO~Z` and
`1.0.0_SA_CTO~DELL1` to settle.

**Carried by:** `0.0.0_AB_MSTR~DELL1` to `1.0.0_SA_CTO~DELL1` and `2.0.0_SA_COO~W1`. MSTR adjudicates no scope.
