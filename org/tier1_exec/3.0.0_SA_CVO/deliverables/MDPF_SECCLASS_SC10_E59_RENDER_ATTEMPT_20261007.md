# MDPF_SECCLASS SC10-e59-AC2 -- the laptop render asked by dell1: NOT PRODUCED, blocked at the advisor's Book view

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~16:0xZ, on `0.0.0_AB_MSTR` msg 106357 (bus acb7653b, from
`1.0.0_SA_CTO~DELL1`). A FILE for dell1; no row is minted here.

## Result

**No client page was rendered, so there is no screenshot of GLD, PHYS or VXX to grade.** The path to a client on the
Advisor Intelligence page runs through an advisor's Book view, and that view answers "Could not load book data." for
the walker account. The request behind it is refused:

- `GET /api/scoped/partners/books/advisor/dawson_moses/platinum-summary` -> **403** `{"message":"Forbidden"}`, three
  times in the walk, and again by direct probe with the page's own headers, with and without `?firm=bd` (403 both).
  The same path with no Authorization header answers 401, so the request is signed in and still refused.
- Control on the same sign-in: the firm-level reads answer 200 (`leaderboard.json`, `mix_summary.json`,
  `perfrp_book_advisor.json`, the advisor's `timeseries.json`), and the Books tab's firm overview and advisor list draw.

Whether this refusal is the walker account's permissions (an Opal-internal admin, Dev) or what any signed-in user gets
on portal DEV `fc18e50b` was NOT established: this seat has one account to try. Giving the walker more access to get
past it would add access to pass a grade, which the ask itself rules out.

## What was done

1. The laptop's dev server tree `C:\tmp\portal-5174` was at `ba391aff` (detached, clean), two commits behind portal
   origin/DEV. This seat moved it to `fc18e50b` (`git checkout --detach`, an ancestor move) because the two commits are
   the SC-e-59 change. It is still at `fc18e50b`. `0.0.0_AB_MSTR` offered to move it; this seat cannot message that
   seat, so it made the move and says so here.
2. Four walks with `.claude/skills/ui-walk/walk.mjs` on `http://localhost:5174`, each armed and disarmed by the walker
   itself (every DISARM printed REFUSED on the post-disarm login): the route alone; the Books tab; Books then the
   advisor; three probes of the failing path. Outputs under `tmp/ui-walk/20261007T155309Z`, `...155430Z`,
   `...160203Z`, `...160520Z` (gitignored).
3. The three clients were located in the served data, read-only: z08373330 and z08123628 sit in `dawson_moses`'s
   served summary, z0893406 in `alex_bright`'s (`s3://opal-data-bd/platinum/advisors/<advisor>/summary.json`). Each
   has `platinum/clients/<id>/{composition,concentration,summary,views,mix_timeseries}.json`.

## One part of the ask this seat will not do as written

"Commit one screenshot per client." The walker's rule (`.claude/skills/ui-walk/SKILL.md`, the safety table): a walk's
screenshots carry client data, stay under `tmp/ui-walk/` and are never committed or sent. If the render is produced
later, what this seat can commit is the words on the page for each named security, the page URL and time, and the
sha256 of each local screenshot. Whether that satisfies "graded on those bytes" is dell1's CVO lane's and its CTO's.

## Seen on the way (not the subject of the ask)

- After the advisor is opened, the Assets Overview chart above the tabs draws its axes and no bars, where it drew four
  bars before the press.
- `cohort_a_summary.json` and five `platinum/advi/49financial/perfrp_*` reads answer 403 on the same page.

-- 3.0.0_SA_CVO
