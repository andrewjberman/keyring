# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- UIR-07: an exact full-name match ranks first (v2, search AND browse(q))

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UIR07_SEARCH_RANK_20260926.md`
blob `a96d2ee0bebd6fe63ad9ccbd61827ed50b3d04b2` @`3a780322d8`. The blob is the same at HEAD and on disk (read
2026-09-26 ~22:3xZ).
**First half:** 1.0.0_SA_CTO (msg 101546, on v2). **Asked by:** 2.0.0_SA_COO~P msg 101543. This seat is not in the act.

## VERDICT: SIGNED on blob a96d2ee0, with one condition on the served arms

- **Order only, the same sets.** One predicate (`full_name_match`: the display name's sorted tokens equal the query's)
  becomes the first sort key in `search` and in `browse(q)`. The any-token filter runs first and is untouched, so
  the same query returns the same SET before and after. Writers of the ranking: 2 call sites of 1 predicate. Nothing
  a viewer may see is widened.
- **v2's catch is right:** the page's header search calls `/directory/browse?q=` (portal `ClientSearch.tsx:95`), not
  `/directory/search`.
- **Rollback** is the live `o9Qu0Jm7`. Any arm FAIL means a same-turn rollback, as the packet says.

## CONDITION: run the reported case the way it was reported -- GLOBAL mode, as typed

- Andrew's screenshots were taken with the firm menu at **"Global (All)"** (UIR-07; screenshot 165438).
- This seat's `/ui-walk` run at 22:12Z, also Global, typed `anna thiessen` into the page's search. The exact match
  "Thiessen, Anna" was **#17 of 17** options (`tmp/ui-walk/20260926T221206Z/findings.json`, check `search:ranking`),
  the Cottonwood entry listed after sixteen 49F "ANNA ..." entries.
- The packet's before-run measured the same case at rank **2** in `browse(q)`, which reads as a single-firm (Cottonwood)
  query. That arm cannot see the Global list.
- **So the served before/after arms also run the page's GLOBAL request, exactly as the page issues it** (the Global
  tenant or context, `q` = "anna thiessen" in lower case and in the reversed order), and report the exact match's rank
  in the list the page renders. Pass: after-rank 1.
- **If Global merges per-firm answers without re-ranking** (in the backend's global browse or in the portal), the fix
  does not reach the case Andrew reported. That is NOT a rollback (order only, no widening), but UIR-07 stays OPEN,
  and the merge point is named for the next cell. A `/ui-walk --client "anna thiessen"` after the apply is the
  page-level check.

Not measured by this seat: the handler and entry diffs (the offline arms are the packet's).
