# Router review -- comp-which and the comp-rail, as designed vs as used

Fork of 4.0.0_SA_CRO, 2026-10-08 ~22:1xZ, laptop CLOUD tree. READ-ONLY. For Andrew-direct ~21:3xZ (record
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_213xZ_COMP_TOOLS_AUDIT_DELETE_UNUSED_REVIEW_COMP_WHICH_ROUTER.md).
[READ] = read in a file or counted. [INFER] = reasoning. Every count names its log and window.

Sources counted:
- LAPTOP: `org/mcp/comp-which-rail.log`, 116,204 lines, 2026-06-22T12:56Z -> 2026-10-08T21:56Z.
- SITE Z: the newest archived copy, `org/audit/archive/sitez/2026-10-08T170308Z/org_mcp_comp-which-rail.log`, 61,980
  lines, ending 2026-10-08T17:01Z.
- No dell1 or dell2 rail log exists in the archive.
Windows: 30d = since 2026-09-08; 7d = since 2026-10-01 (8 days).

---

## 0. Verdict

**Not dialled in.** The rail works as a fence. The router is barely used as a router.
1. **Usage has collapsed.** In the last 7 days, organic comp-which calls numbered 88 on the laptop and 21 on site Z,
   against 911 and 1,403 rail denials.
2. **The biggest use is a ritual.** 58% of organic questions over 30 days are "read this exact inbox file / known path".
   That needs no router. They misroute: the rank-1 tool is often comp-iam or comp-lambdamap for an inbox read.
3. **No-fit is high:** 41% of organic questions on the laptop over 30 days, 59% on site Z.
4. **comp-which almost never leads to a tool run it started.** Of 7,713 comp-find and comp-read runs over 30 days on the
   laptop, 55 came from comp-which (`src=comp-which`); 7,658 were direct.
5. **The escapes carry the load.** 40,531 searches were ALLOWED as single-file or pipe-receiver shapes over 30 days,
   against 7,713 comp-tool runs. The rail mostly changes command SYNTAX, not behaviour.
6. **Whether a routed tool is then used cannot be measured.** No route row carries the asking seat's serial; the code
   says so itself (`.tools/comp-which:1780`). Curated hits and fuzzy hits are logged under one event name (:2327).
COMPRAIL's own acceptance AC5 ("comp-tool usage UP / raw-bypass DOWN post-enforce", `docs/architecture/NFRA_COMPRAIL_PRD.md`
section 9) is not met on this data.

---

## 1. Design, briefly [READ]

- **Rail hook** `.tools/hooks/comp-tool-hud.sh` (463 lines; PreToolUse on Grep, Glob and Bash):
  - Bash repo `grep`/`find`/`rg` and raw `aws` inspection are DENIED per segment. The enforce switch is
    `org/mcp/comprail-gate1.enforce` (present). A denial aborts the whole Bash call (CLAUDE.md rule 21).
  - Escapes: a `# rail-checked: <why>` marker (audited as RUN-OVERRIDE); `/freeform` (a per-session marker,
    `comp-tool-hud.sh:44-52`); a pipe-receiver grep and a single-file grep pass as ALLOW-SEARCH.
  - Native Grep and Glob are "nudge-and-proceed" by design (COMPRAIL PRD section 3, the 2026-06-22 refinement).
- **comp-which** `.tools/comp-which` (2,764 lines):
  - RULES: 91 curated tuples (:90).
  - `_default_router` (:2213) calls `comp_route.route` (`org/modules/graph/comp_route.py:341`) over capabilities from
    `comp_capability_provider.py`, which reads `comp-coverage-map.yaml`. Only `comp-*` tools are capabilities.
  - A curated hit is credited to the FIRST TOKEN of its call. Below the vetted band it prints "NO CURATED RULE MATCHED".
  - The posterior route and backstop (:2109, :2152) are logged as ROUTE-POSTERIOR or NOFIT-POSTERIOR (:2327). The old
    `ROUTE` event (:2602) has not fired since week 27.
  - The no-fit fallback runs comp-find under a budget, default 90 s (:44-59, `_run_primitive` :1859). 47 log lines
    mention a budget or a kill.
  - `--json` mode exists (:2083).
- **Routing test** `.tools/comp-which-routing-test.py`: gibberish abstention, an anti-control, and a positive probe. It
  passed today (this seat's run, 18:5xZ). It grades abstention and pollution, not whether real questions route well.
- **Projects:**
  - **COMPRAIL** set out to make "comp-which-first" the reflex and to build tools for uncovered intents (AC1-AC5).
  - **COMPEFFICACY** (`org/missions/D11/NFRA/NFRA_COMPEFFICACY`, ROUND_CLOSE since 2026-09-04, round 8: 8 REALIZED,
    2 NOT_EVALUATED) graded tool ACCOUNTS: one list, written accounts, what each counts and cannot see, a cleared /
    retired / short-list state per tool (FWD-4), and a ratified short list that a seat starts from (FWD-8). It did not
    measure USE. FWD-8's short list waits on Andrew's "estate sitting" ruled "after the roadmap".
  - **COMPTOOL_USEPATHS** (2026-06-25) proposed a 4-layer use-path model; its open CTO decisions were not re-read here.

## 2. As used -- weekly, laptop [READ]

Organic = comp-which rows outside minutes holding 8 or more rows (bursts are harnesses such as the routing test).

| ISO week | organic comp-which | burst rows | organic NOFIT | DENY | RUN-OVERRIDE | ALLOW-SEARCH | RUN-FIND | RUN-READ |
|---|---|---|---|---|---|---|---|---|
| W33 (Aug 10) | 20 | 74 | 5 | 59 | 47 | 0 | 564 | 75 |
| W35 | 95 | 928 | 54 | 254 | 53 | 1,725 | 1,789 | 225 |
| W36 | 1,828 | 913 | 1,047 | 460 | 88 | 3,369 | 1,790 | 2,744 |
| W37 | 1,796 | 94 | 323 | 456 | 130 | 4,179 | 990 | 2,281 |
| W38 | 432 | 75 | 193 | 678 | 123 | 6,577 | 775 | 315 |
| W39 | 2,462 | 107 | 1,397 | 888 | 418 | 10,622 | 739 | 1,752 |
| W40 (Sep 28) | 55 | 0 | 29 | 930 | 371 | 12,678 | 360 | 289 |
| W41 (Oct 5-8) | 78 | 609 | 50 | 502 | 137 | 6,490 | 107 | 95 |

Read across: denials rose about 9x and escapes 7x, while comp-find runs fell to a sixth and comp-read to a thirtieth of
their peak.

**30-day totals, laptop:**
- Organic comp-which 4,793 (ROUTE-POSTERIOR 2,821, NOFIT-POSTERIOR 1,972 = **41% no-fit**).
- DENY 3,452 and RUN-OVERRIDE 1,177.
- ALLOW-SEARCH 40,528: single-file 20,743, pipe-receiver 19,788.
- CENSUS-PIPE 1,335: DENY 1,104, ALLOW 232.

**Site Z:**
- 30 days: comp-which 1,059 (ROUTE 432, NOFIT 627 = **59% no-fit**); DENY 4,145; OVERRIDE 930; ALLOW 45,287;
  RUN-FIND 2,350; RUN-READ 1,042.
- 7 days: comp-which **21**; DENY 1,403; OVERRIDE 342.

**What organic questions are (laptop, 30d, n = 4,793, keyword classes, [INFER] on the class edges):**
- read a known file or inbox message: 2,758 (58%);
- other: 1,767;
- verify or check: 215;
- which or who: 53.

A typical row: "Read exact inbox file 20260922T...md" routed to comp-iam+comp-lambdamap+comp-trigger.

**Rank-1 routed tool (organic ROUTE-POSTERIOR, 30d):** comp-read 1,606; comp-estate 363; comp-iam 312; comp-freshness 174;
then comp-blast, comp-axes, comp-pipescript, comp-kuzu, comp-diff and comp-xray at 22-28 each.

**Who runs comp-find and comp-read (30d, laptop, by serial base):** CTO 2,330; COO 2,022; CVO 1,560; CRO 872; MSTR 290;
KRN 181; AE CloudOps 165; workers fewer than 100 each. `src=comp-which` 55 vs `src=direct` 7,658.

**NOFIT vocabulary (top words):** exact, read, inbox, irpt, file, inspect, review, source, message, canonical, find,
unread, path, commit, notice, contents, holdings, pinned, handoff, locate, evidence, contract.

## 3. Friction [READ, attribution INFER]

**Denials by class (laptop, 30d, n = 3,455):**

| Class | Denials | Overrides |
|---|---|---|
| repo_search | 1,790 | 692 |
| CENSUS-FILTERED | 1,097 | 126 |
| infra_grep | 394 | 113 |
| aws_iam_inspect | 88 | 139 |
| aws_freshness | 52 | 72 |
| aws_route | 21 | 29 |
| aws_deploy_verify | 13 | 9 |

Overrides EXCEED denials for the aws classes: agents pre-mark the override before any denial.

**What follows a denial within 10 minutes (laptop, 30d, 3,456 denials).** Many seats share one log, so this is an upper
bound on cause:
- a comp-tool run: 1,555 (45%);
- nothing logged: 1,284 (37%), most plausibly the native Grep/Read tools, which the rail does not log;
- any override: 804 (23%); an override of the same command: 439 (13%);
- a comp-which call: 710 (21%).

**Top override reasons (keyword hits, n = 1,177):** census 110, aws 105, comp-find 102, outside 82, worktree 67, line 66,
exact 62, single-file 61, scratch 58, pipe 44, log 32, "no comp-tool" 30.

**This session as one data point.** The rail denied `grep -n ... infra/aws/globgrph/*.py` and a `.tf` grep, aborting a
compound Bash call that also held a `git checkout` and a revert, which therefore did not run. The agent re-ran the read
with the native Grep tool (allowed, unlogged) and repeated the revert in its own call. The deny cost two round-trips and
moved the search off the log. It did not move it onto a comp-tool.

## 4. Recommendations, highest value first

1. **End the "comp-which before reading a known file" ritual.** It is 58% of organic questions, it misroutes, and it
   adds a call per read. Two changes:
   - Make comp-which short-circuit a question naming an existing path straight to `comp-read <path>`.
   - Say plainly in the seat prompts (Codex especially) and in CLAUDE.md rule 21 that a known path needs no router.
2. **Make routes measurable.** Log the asking serial and `route_id` on every ROUTE-POSTERIOR and NOFIT row, and on the
   comp-tool run that follows (comp-find and comp-read already log `src=`). Then "is the routed tool used?" is a join,
   not a guess. Today 0 of the 17,687 route rows that comp-which's own comment measured carry a serial (:1780).
3. **Separate curated hits from fuzzy ones and mark synthetic rows.** Log a vetted flag (a curated rule fired vs the
   posterior guess). Tag rows written by the routing test and other harnesses (W28-W32 are about 95% burst rows), so
   usage telemetry stops counting tests.
4. **Curate rules for the top no-fit clusters** before any new tool: inbox and handoff reads, commit and evidence
   verification, holdings/custody (IRPT), the "canonical source of X" lookup. The no-fit share (41% and 59%) is the
   coverage-gap list COMPRAIL AC4 asked for.
5. **Re-tune the deny to the overridden shapes.** Paths outside the repo, worktree and scratch paths, an exact one-file
   line read, and census pipes account for most overrides and of the 1,097 CENSUS-FILTERED denials. Let those pass as
   ALLOW-SEARCH (they are already allowed for the native tools). Keep the deny on blind recursive repo grep, the case
   COMPRAIL was built for.
6. **Decide comp-which's place in the reflex.** On current use (88 and 21 organic calls in 7 days against 911 and 1,403
   denials) it is a fence plus a ritual, not a router. Either invest (1-4) and re-measure AC5 in two weeks, or demote
   rule 21 from "comp-which is the reflex" to "use comp-which when you do not know the tool".
7. **Retire the dead `ROUTE` event path** (:2602, silent since W27) and finish COMPEFFICACY FWD-8 (the ratified short
   list) as the starting set agents actually see. The router can then rank those tools first.

## Not read

- dell1 and dell2 rail logs (none archived here). Site Z only to 17:01Z today.
- The bodies of `comp_route.py`, `comp_capability_provider.py`, `_default_router` beyond their entry points; the
  posterior's affinity provider.
- `NFRA_COMPTOOL_USEPATHS.md` beyond its headings; COMPEFFICACY round analyses 6-7; its tool list and per-tool states.
- Native Grep/Glob/Read usage (the rail does not log the native tools; "nothing logged" in section 3 is their likely
  home, not measured).
- Per-tool health (which tools run at all): the parallel tool-usage census owns that.
