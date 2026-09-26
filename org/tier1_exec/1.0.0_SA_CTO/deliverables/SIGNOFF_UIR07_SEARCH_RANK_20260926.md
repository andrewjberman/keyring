# SIGN-OFF (1.0.0_SA_CTO half) -- UIR-07: the directory search ranks an exact full-name match first

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UIR07_SEARCH_RANK_20260926.md`
blob `b833af43811d4a64a411eaaae9ea0d6339bd7f66` @`728a152e9b` (2.0.0_SA_COO~P msg 101532). **Rule:** CTO 101506, PRD
v0.15 UIR-07. **Signed:** 1.0.0_SA_CTO, 2026-09-26 ~22:0xZ, under the self-drive arm @`ce6aa15a17`.

## SIGNED, with one added condition

**The act:** `irpt-directory-search` = the live `o9Qu0Jm7` plus `directory/handler.py` @`1068a4b5a5`. The census
must show exactly that member.

**What it changes:** a new FIRST sort key puts an exact full-name match (sorted tokens) first.
- `project()` (scope, the cross-firm gate, permitted accounts) runs first and is untouched, so the visible SET is
  unchanged. Only the order moves.
- Search is a pure read.

**Rollback per key:** the function re-points to `o9Qu0Jm7`.

**Added: the served proof covers all three firms and the reported case.**
- Besides the 20 49F entries, the before/after arms include the UIR-07 case itself: the Cottonwood client from
  Andrew's screenshot, queried in both name orders, BY ID with no name printed.
- Add 5 deterministic COT entries and 5 INF entries, chosen the same way.
- The same pass rule applies: sets identical, after-rank 1, and an existing rank 1 is kept.
- Any set difference means STOP and a same-turn rollback.

## Second half

**4.0.0_SA_CRO.**

## SIGNED on v2 -- blob `a96d2ee0bebd6fe63ad9ccbd61827ed50b3d04b2` @`3a780322d8` (2.0.0_SA_COO~P msg 101542)

**A fresh read.** v2 supersedes v1: the served before-run showed that the page's header search is
`/directory/browse?q=` (`ClientSearch.tsx:95`), which ranked the reported case 2nd and some 49F targets as low as
81st.

`git diff b833af43 a96d2ee0` shows the same single predicate (`full_name_match`) as the FIRST sort key in both
`handler.search` and `entry.browse`.
- The census must show exactly those 2 members.
- `project()`, browse's WHOLE-only and any-token filters, and the response shapes are unchanged, so the visible SETS
  are unchanged.
- An empty query, or one with no full match, orders as before.
- A cursor's order is fixed by the query binding.

**My v1 condition carries**, run through BOTH search and browse(q): the reported Cottonwood case in both orders, by
id; 20 49F entries; 5 COT and 5 INF. Pass means identical sets and after-rank 1. Any set difference means STOP and a
same-turn rollback of both members (the function re-points to `o9Qu0Jm7`).
