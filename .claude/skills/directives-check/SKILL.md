---
name: directives-check
description: The DIRECTIVES REGISTER dashboard -- the /registry-check of org/missions/DIRECTIVES.yaml. Bare `/directives-check` renders the LIVE directives (one numbered row each: title, placement device + PRD, member sub-groups and every member PROJECT with its registry status, open task orders summed over member projects, the human stance compacted, per-row freshness from git blame, and flags WITH THEIR BASIS -- MEMBERS-ALL-CLOSED (membership currency, NOT work completion), MEMBERS-STALE? (stance moved after the member set), NO-MEMBERS -- hints for the register owner, never an act); `/directives-check --all` adds the RETIRED partition (DIRECTIVES_RETIRED.yaml, machine-cut by comp-directives, each cut's authority + frozen vintage); `--retired` alone; `--code D7` one directive in full; `--json` machine rows. Read-only, pure filesystem+git+yaml, denominators printed, malformed rows surfaced never dropped. Engine `.tools/directives-check.py`.
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
| `/directives-check --json` | machine rows (respects the scope flags). |

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
