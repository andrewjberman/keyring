# ANDREW-DIRECT 2026-08-25 ~14:12Z -- ALL WORK SITS UNDER A DIRECTIVE; NEW PROJECTS ARE TAGGED AT CREATION

**Recorded by:** `1.0.0_SA_CTO`, CTO terminal, same turn as receipt.
**Trigger:** he asked how the `/self-drive` tick numbers were computed -- *"I want to make sure that
we are properly tracking active projects/directives."* I measured, put a two-reading fork to him,
and he ruled.

## VERBATIM -- two words, one ruling

> **"We only want to do it from directives.yaml-associated project layers, really all work we do
> should be underneath a directive."**

> **"So that is fine, when you're making new projects in the process of working on directives
> functions, you should be tagging those projects underneath the relevant directive"**

## WHAT HE WAS RULING ON -- the measurement that produced the fork

```
project JSONs on disk ............................ 332
members of ANY live directive ....................  17
status=active on disk ............................ 103
active AND a directive member ....................  12
ACTIVE BUT MEMBER OF NOTHING .....................  91
  (A) of those, with OPEN TOs -- demonstrably live  49
  (B) of those, zero open TOs -- candidate stale     42
```
Derivation: `org/missions/DIRECTIVES.yaml` `members.projects` per row vs `org/projects/*.json`
`status`; TO counts from `to-check.py --all` (ACTIVE+PENDING+BLOCKED+UNKNOWN), the same denominator
`directives-check.py` uses.

**I put two readings to him: (1) the directive layer is DELIBERATELY a strategic subset and 91
orphans are correct by design; (2) the member sets have fallen behind the work. REC was (2), for
bucket (A) only.** **He ruled (2), and wider than my REC: not "bucket A should be tracked" but
ALL WORK SHOULD BE UNDER A DIRECTIVE.**

## THE TWO HALVES, AND THEY BIND DIFFERENTLY

**1. THE PRINCIPLE (standing, binds now): all work sits under a directive.** The directive layer is
not a curated highlight reel of what matters this fortnight -- **it is the frame the work is
supposed to hang from.** A project that is nobody's directive member is, by his word, work we
should not be doing from an untracked layer.

**2. THE MECHANISM (forward, binds at project creation): a project minted while working a directive
function is TAGGED under that directive when it is minted.** Not later, not on next touch, not when
someone notices -- **at creation, by the seat creating it.**

⛔ **THE MECHANISM IS THE HALF THAT ACTUALLY CLOSES THE GAP, AND IT IS THE HALF THAT WOULD BE LOST
IF ONLY THE PRINCIPLE WERE REMEMBERED.** 91 orphans did not appear by anyone deciding to work
outside the frame; **they appeared one at a time, each minted mid-task by a seat that had no step
telling them to tag it.** A principle with no minting-time act regenerates the backlog at exactly
the rate work is created.

## SCOPE -- DIRECTION RATIFIED; A 91-PROJECT MIGRATION IS *NOT* AUTHORIZED BY THIS LINE

**He ruled the DEFAULT and the CREATION-TIME act. He did not order a retro-assignment sweep**, and
the two buckets take opposite remedies (Rule 24(iv)):

| bucket | n | what it is | remedy |
|---|---|---|---|
| **(A)** | 49 | live work (open TOs) with no directive home | a **REGISTER** act -- assign each to its directive |
| **(B)** | 42 | `status: active` with zero TOs | a **CLOSE-OUT** act -- most are probably finished-and-never-flipped |

**Worked as one item they will be done wrong**: sweeping (B) into directives manufactures 42 fake
members, and closing (A) loses live work. **And assigning a project to a directive is a JUDGMENT
about which directive it serves -- not a mechanical join.** That judgment belongs to the register
owner with the directive owners, and the volume question (all 49 now, or as-touched) is Andrew's.

⛔ **NOT DOING, and stating it so nobody infers otherwise:** I am not editing member sets. The
register is `0.0.0_AB_MSTR`'s, and under the `/self-drive` skill the driver may not edit the member
set its own completion test is measured against -- *a stop-condition satisfiable by adjusting its
own denominator is not a stop-condition.*

## WHAT THIS CORRECTS ABOUT MY OWN REPORTING

My tick line **`COMPLETION: 2 of 12`** was never wrong about its declared population -- laptop
directive members -- **and it reads as a statement about project tracking.** It is a statement about
membership. **Under his ruling those two converge**, which is the point: today the denominator is
12 because the register names 12, not because 12 is the work.

**And I had never read how `open_tos` was derived until he asked** -- sixteen ticks of printing a
number without knowing it summed four TO states over member projects only. `CONTROLS_OVER_CARE`
s.11: a correct retrieval, a claim wider than the read.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `sed`/`grep` on `.tools/directives-check.py` | `open_tos()`, `project_status()`, row assembly | the full derivation chain -- read at source, not assumed |
| `yaml.safe_load` on `DIRECTIVES.yaml` | all 9 rows, device + members | 5 LAPTOP / 4 SITEZ; the 17-member union |
| python census over `org/projects/*.json` | 332 files, `status` field | 103 active, 91 orphaned |
| `to-check.py --all` + regex | TO counts per project (144 parsed) | **the (A)/(B) split -- 49 live vs 42 stale-candidate** |

**What failed:** my census script died on a `U+26D4` I typed into it -- non-ASCII in code, a
CLAUDE.md Code Quality rule I enforce on others; the measurement had already printed.
**Gap found:** project creation has no directive-tagging step, which is the mechanism his second
sentence installs.
