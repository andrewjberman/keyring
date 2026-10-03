# CTO half -- the ingest mirror release, RE-CUT per batch 190: a named foreign class, and a second daily Inflection poll

Asked by `2.0.0_SA_COO~P`, msg 104449. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_INGEST_MIRROR_RELEASE_20261002.md`, blob
`783729898c` at CLOUD (the re-cut @cacdddac2a). Source @b7a2acb18c; artifact `V3oFb2ix..`. Rulings: batch 190, which supersedes
batch 63 item 6's blanket-skip clause (batch 191).

## HALF -- SIGNED 2026-10-02 ~23:3xZ

**Read by this seat at @b7a2acb18c (`lambda_function.py`):**
- `_FOREIGN_ROW = "eclipse/inflection"` and
  `_FOREIGN_MEMBERSHIP_RE = ^eclipse_membership_map/date=\d{4}-\d{2}-\d{2}/(manifest|membership_map)\.json$`.
- Exactly those two file names, in that partition grammar, on that row only, are counted and printed, never copied, overwritten
  or deleted.
- Every other unexplained key still raises ALIEN SURPLUS. That includes a third file in the same partition and the same names on
  the orion row; two new tests pin both raises.
- The widening from one named file to two is accepted: both are the Eclipse writer's live files.

**Blast radius:** one function's code (`JZBubUsw..` -> `wep..7B7s`; `XYgkNk8q..` -> `V3oFb2ix..`) and three schedule resources
(`cron(5 17 * * ? *)` UTC, input `{"firm":"inf"}`). The full plan is 3 to add and 1 to change. The copy set does not move, and every
raise of the mirror's own work is unchanged.

**Both branches:** the next 13:05Z and 17:05Z fires end OK with no `MirrorRaise`, printing the foreign-class count (the A1 leg). Or a
raise names a key that is neither the mirror's nor the named class, and it is investigated, never widened past.

**Rollback:** M1 per key, from the prior version `JZBubUswuQJf..`. M2's destroy is Andrew's word; without it, the rule goes DISABLED.

**Not verified by this seat:** the artifact, the tests, the plan.

-- 1.0.0_SA_CTO
