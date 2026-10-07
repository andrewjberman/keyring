# dell2 CTO -- first-day friction brief (2026-10-07)

Author `1.0.0_SA_CTO~DELL2`. This answers Andrew's question at dell1 ~18:4xZ, relayed by `0.0.0_AB_MSTR~DELL2` msg 991: "How is your
first day coming thus far since session start? I want to know where there are fumbles/delays/process debt, so we can streamline."

**Scope:** this seat's own record since launch (~07:2xZ): ticks 1-12, about 30 round analyses, 12 never-widen halves, 2 PRDs, 1 L2 and
L3. This brief proposes; it changes no gate or rule (msg 991: nothing changes before Andrew talks with the laptop CTO).

## 1. My own fumbles (each caught, most by another seat)

| # | what I got wrong | who caught it | the pattern |
|---|---|---|---|
| 1 | IRPT_CUSTDY round 6: "hop 5's server half is served". I checked that the code shipped, not that a request could travel the path. Five breaks, then a sixth | `~K2` (S14), `~P2` (W162-S1) | **"deployed" read as "served"** |
| 2 | The SC-e-62/e56 bundle half left out the ENABLED Holdings schedule, a second writer of the served output | `~M2` (msg 827) | the scheduled-producer writer not counted |
| 3 | The first bundle comparison read a shared `FETCH_HEAD` another seat had just moved | my own re-read | a shared ref is not a pin |
| 4 | ADVI_COTBKF round 11 parked all of FWD-3 on prices; step 1 needed none | `~C2` (msg 674) | over-wide parking |
| 5 | Earlier: the C-SILVER count, the module vs the table, cross-firm stores, a withdrawn stop, an L10 31 minutes late | the COOs | reading the wrong object |

Of these, items 1 and 2 cost the most: each one moved a decision to another seat.

## 2. Delays, measured or counted

- **Merge windows on the shared tree.** MSTR's pull-merges hold every shared-tree commit (~5 today; one retry loop kept a window open
  by mistake). Commits waited, and one of my commits was refused mid-stage by a window opening.
- **Two commits that silently did not land.** `safe-commit`'s tail output read like success and the repository was unchanged. I now ask
  the repository each time.
- **Relay hops.** Every laptop-only act (applies, reads, placement carriers, rulings) goes dell2 seat -> MSTR~DELL2 -> bus -> laptop and
  back. Most items today took 2-4 messages before any work.
- **Fenced reads.** The transcripts store (KMS), `AWS-RunShellScript` and `iam:SimulatePrincipalPolicy` were refused to dell2. Each one
  became a FILE round trip or a workaround (the invalid-parameter read-back). Andrew's ~16:1xZ word opens the store once its policy
  applies.
- **The inbox watcher dies every 30 minutes:** re-armed about 20 times today, and mail is deaf in each gap.
- **Slow tools:**
  - `sequence-check.py` takes ~30 s per project, so ~3.5 minutes per tick for 7 projects;
  - it reads NEEDS-SLOT on IRPT_CUSTDY and ADVI_COTBKF all day although their COOs are live, a known reader gap;
  - `directives-check.py` printed D7 as UNRULED.

## 3. Process debt

1. **A half is bound to a branch hash, not to the deploy scope.** One two-file bundle change took four re-points (r1 to r4) as dell1
   republished for row-id and CHANGELOG collisions. The relayed scope was wrong twice ("one member", "+3 tests"). The deploy content
   never changed. *Proposal:* bind a half to the deploy scope's content (bundle member md5 set, or package sha256), and let any branch
   that produces it carry.
2. **"Served" has no mechanical test.** *Proposal:* an outcome or half that claims "served" names the one request that travels the path,
   and its read.
3. **Cross-project contracts surface late.** CUSTDY's hop 5 depended on four IRPT_BCKEND surfaces that nobody listed at L4. *Proposal:*
   the PRD's surface manifest lists each CONSUME's exact route or field, read at HEAD.
4. **The PRD header schema refuses extra fields** (`placement`, `renamed_from`, `endpoint_ref`) that the body then has to carry. It costs
   one refused commit each time.
5. **The act list for Andrew is spread across many logs.** *Proposal:* one current file per box, overwritten each tick.

## 4. What worked

- **The COOs' surprise rows caught my errors fast:** S14, the schedule writer, the cash-in-lieu sign.
- **Reads on named refs plus three-dot diffs** graded four bundle candidates correctly against a moving origin.
- **Andrew's "Proceed with recs" and the CVO's same-hour reviews:** TCKT_VNEXT went from placement to an ADMITTED PRD in about three
  hours.

-- 1.0.0_SA_CTO~DELL2
