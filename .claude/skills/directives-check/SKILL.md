---
name: directives-check
description: The DIRECTIVES REGISTER dashboard over org/missions/DIRECTIVES.yaml: `/directives-check` (live directives with members, open TOs, stance, freshness, flags with their basis); `--all` adds the retired partition; `--retired`; `--code D7`; `--json`; `--orphans`. Every run prints the project<->directive linkage in both directions. Read-only, denominators printed, malformed rows surfaced. Engine `.tools/directives-check.py`.
---

# /directives-check — the directives register dashboard

The human-reading lens on `org/missions/DIRECTIVES.yaml` (LIVE) + `org/missions/DIRECTIVES_RETIRED.yaml`
(RETIRED, machine-cut per LD-0433). Andrew-commissioned 2026-08-20 as the /registry-check analogue
for directives. Read-only: it REPORTS, it never edits the register (the register is MSTR's surface;
the retired view is comp-directives' surface; a status lens touches neither).

## Invocation

| Form | Behavior |
|---|---|
| `/directives-check` | LIVE rows -- the working board. |
| `/directives-check --all` | LIVE + RETIRED partitions. |
| `/directives-check --retired` | RETIRED partition only (cuts, authorities, frozen vintages, ever_minted). |
| `/directives-check --code D7` | one directive, every cell in full (placement text included). |
| `/directives-check --json` | machine rows (respects the scope flags); adds `linkage` + `open_tos_total`. |
| `/directives-check --orphans` | the full UNAFFILIATED list rather than the per-macro_code head. |

Execute: `python .tools/directives-check.py [--all|--retired] [--code Dn] [--json]`

## Reading a live row

```
 7. D7  Ticketing intake (THIS WEEK; SITEZ intake + laptop serve)
     Where:   SITEZ -- docs/architecture/D7_TICKETING_INTAKE_PRD.md
     Members: subgroups [...]; projects CODE[active], CODE[closed 08-20]
     TOs:     N open across member projects
     Stance:  <the human stance cell, compacted>
     Last:    08-20 19:55Z (1h ago)        <- newest commit on ANY line of THIS row (git blame)
```
- **Where** = the placement DEVICE (LAPTOP / SITEZ / UNRULED, parsed from the placement cell's
  leading token -- the LD-0428 boundary read) + the directive's PRD path (flagged if missing).
- **Members** = the row's sub-group references + each member project with its `org/projects`
  status; a `MALFORMED(...)` status means that project JSON does not parse -- fix it, do not
  ignore it.
- **TOs** = open task orders summed over member projects, read from `to-check.py --all` (its
  denominator, not a second count).
- **Flags** (each prints its BASIS beside it): `MEMBERS-ALL-CLOSED (n/n closed, 0 TOs)` = every
  RECORDED member project closed with zero open TOs -- it measures MEMBERSHIP CURRENCY, NOT work
  completion: a directive whose scope outgrew its recorded members reads this way while its work
  is alive (measured 2026-08-20 on D6 -- Andrew: "certainly not going to be any retiring of that
  for some time"; the flag was first named RETIRE-CANDIDATE? and renamed the same hour for
  saying more than it measured). `MEMBERS-STALE? (stance moved d, members last d)` = the stance
  cell moved after the member set last did -- the more useful signal for outgrown membership.
  `NO-MEMBERS` = empty member set (honest where a plausible one is not). `RETIRED-FACT-PRESENT
  (awaiting emit)` = the fact is on the live row but comp-directives has not cut it yet. None of
  these is an act; retirement is the FACT + MOVE + CHECK chain on Andrew's word.
## Reading the LINKAGE partition

Added 2026-08-25 (Andrew-direct: *"maybe need to build out the directives-check skill to tie those
in harder"*). **The defect it closes: membership was ONE-DIRECTIONAL.** The engine read
`DIRECTIVES.yaml -> members.projects` and nothing read back, so the board could not see a project
belonging to no directive -- **and its rows read as though they covered the estate while showing
about an eighth of the open project population.**

```
== LINKAGE -- project <-> directive reconciliation ==
  COVERAGE:      15 of 124 open projects are members of a live directive (12.1%)
  UNAFFILIATED:  109 open project(s) belong to NO directive -- invisible to the board above
  BACK-POINTERS: 1 of 333 project JSONs carry a 'directive' field (0.3%) -- the migration denominator
  GHOST MEMBERS: n board member(s) have NO registration JSON: CODE, CODE
  DISAGREEMENT:  n project(s) claim a directive that does not claim them
  STATUS RESIDUE: n project(s) in NEITHER the open nor the terminal set -- NOT assumed either way
```

- **COVERAGE / UNAFFILIATED** answer the question the board could not previously ask: *what is NOT
  on it?* Unaffiliated projects are grouped by `macro_code`, which already correlates with
  directives in practice (D0 members are all `NFRA`, D1/D8 `MDPF`, D4 `ETFS`) -- so the grouping is
  a **drafting aid for whoever proposes membership**, never an assignment. The tool does not infer
  membership from `macro_code` and must not: correlation across seven rows is not a mapping.
- **BACK-POINTERS** is deliberately reported as a fraction of ALL projects. It reads `1 of 333`
  today and that is the honest migration denominator, not a failure.
- **DISAGREEMENT** fires when a project's own `directive` field names a directive that does not
  list it back, or names a code that is not live. It is the only check that can catch the two
  records drifting apart, and it is **silent today because they agree** -- the branch is exercised
  by planted-mutant controls, not by the live corpus.
- **STATUS RESIDUE** prints projects whose status is in neither the declared open set nor the
  terminal set. They are **excluded from every count above and assumed in neither direction** --
  the status axis carries 17 distinct strings over 333 JSONs (four spellings of the hold concept
  alone), which is a Rule-24 defect in the axis itself; this line surfaces it rather than
  normalising it away.
- **Per-row TO counts now carry the estate denominator** (`19 of 385 open estate-wide`). A bare
  count carries no frame, which is the exact retrieval-control class CLAUDE.md names.

**Still status, not action.** Nothing here edits the register (MSTR's surface,
`org/missions/.register-owner`) or any project JSON (`ANY_EXEC_OR_AE` lane). An unaffiliated
project is a worklist entry for the register owner, **not** a defect and **not** a warrant to tag
anything -- retro-tagging volume is a sovereign call and was carded to Andrew 2026-08-24, unanswered
at the time of writing.

## The render (visible analysis) — part of THIS skill

Andrew-direct 2026-08-20 ~2105Z, VERBATIM: *"/directives-check which is for me internally and shows
the current state of directives + creates a render for visible analysis. Then there should also be
/daily-sprint which essentially is just a formatted text version i can copy/paste of
directives-check for the Opal teams channel."* So every `/directives-check` run ALSO renders:

```
python .claude/skills/directives-check/render_dashboard.py [--days 7] [--out PATH.html]
  -> Desktop/Opal_Directives_Dashboard.html   (then SendUserFile it, as /registry-check does)
```
One device-colored card per live directive (activity bar = mention count in N days, member-project
status pills, open-TO load, stance, per-row freshness, flags WITH their basis) + the retired
partition with each cut's authority + malformed surfaced. It consumes only the engine's
`--all --json` contract (design input: CTO's withdrawn draft, taken whole). `/daily-sprint` is the
text twin for the Teams channel and renders nothing.

## Discipline

- Status, not action: surface a candidate to the register owner; a retirement is the
  FACT + MOVE + CHECK chain (LD-0433), never an edit from this skill.
- The `Last` column is per-ROW (blame over the row's line span), so a file-level edit elsewhere
  does not make every directive look fresh.
- Machine-readable via `--json`; ASCII-only output. RESULT line prints the denominators.

## Cross-references

- Engine `.tools/directives-check.py` · retirement mechanism `.tools/comp-directives` (LD-0433) ·
  register owner `org/missions/.register-owner` · siblings `/registry-check` (projects),
  `/to-check` (task orders), `/prd-check` (PRD coverage).
