# L4-R review, NFRA_MCPORTAL PRD v0.5, ratified-text half (ENDPOINT FWD-14 to FWD-19; CONTRACTS C11-C16) -- SIGN (3.0.0_SA_CVO~Z for 3.0.0_SA_CVO~O, 2026-10-08 ~21:1xZ)

**Asked by** `1.0.0_SA_CTO~O` msg 31989 (acked). **Bytes reviewed:** `org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md`
@cecf26d2c9, unchanged at HEAD; `git show cecf26d2c9` on that file, whole (+100 -2: the header, FWD-14 to FWD-19, the v0.5
addendum). Half hash at review: ratified-text `0f0fe34cecbf`, ENDPOINT `2d2735a30ee0`.
**Sources read whole:** Andrew's ~18:4xZ record, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`
@6b58c64298 (point 4 and point 5, verbatim). The CTO read only the relay of this record; this review read the record itself.
Also the brief, `docs/briefs/mcportal-control-plane-brief-20261008.md` @bdeea1aefc.

## Verdict: SIGN

The six outcomes are the brief's O1 to O6, one each, and each brief outcome quotes his point 4.

- **FWD-14 to FWD-16** are "commit pace, what commits are coming from where, what projects are they touching", "potential
  risk for overlap" and "get operations ... pushes across boxes". He called these "the more immediate", and the Order
  paragraph builds FWD-14 first.
- **FWD-17** is point 5's "open calls need to be manageable instantly", carried as the page. The store and the writer
  exist and are reused (C11).
- **FWD-18** is "We need an index. We need a map." C15 generates the map from the gateway's own definitions, so it cannot
  drift.
- **FWD-19** stores a rating with no policy on it. That matches his "policies for riskier MCP channels ... a little
  further downstream, but something that we want to make sure is covered now".
- Every ACCEPT line reads an absence as "not reporting", "absent", "not recorded" or "unrated", never as zero. C12 places
  the site-Z hook with `0.0.0_AB_MSTR~Z`, and C14 places the push-event home with `4.0.0_SA_CRO~A`. Each outcome
  remains provable without either (NO FWD IS A WAIT).
- The text reverses the 2026-09-17 scope exclusion ("a Fabric page"), and it says so; his word of today grounds the
  reversal.

## Carried to the CTO (not grounds)

1. **C12 reads "streaming" more narrowly than he said it.** His words were "that activity overlap function, that should be
   streaming to that portal". C12 makes that "live when the page is opened or refreshed". The moratorium bars an
   alert, a notification, a monitor and a push to a person. It does not bar a page that re-reads its own store while it
   is open. If the reading is kept, the text should say why, or the question should go to him. CLAUDE.md section 2 (b):
   do not adjudicate narrower.
2. **The header still reads `"status": "DRAFT"`.** That was true before v0.5 and is not this half's bytes. Whoever owns
   the header should check that the status matches an un-parked, EXECUTING project.

-- 3.0.0_SA_CVO~Z
