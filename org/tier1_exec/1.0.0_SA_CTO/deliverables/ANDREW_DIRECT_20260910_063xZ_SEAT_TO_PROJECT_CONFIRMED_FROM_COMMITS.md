# SEAT-TO-PROJECT, CONFIRMED FROM COMMITS

**archetype:** VALIDATE

**Seat:** `1.0.0_SA_CTO~Z` · **Written:** 2026-09-10 ~06:4xZ · **Fabric:** SITEZ @ `c72d7277a2` (on origin, ls-remote read by `0.0.0_AB_MSTR~Z`)

## The instruction

Andrew-direct, relayed VERBATIM by `0.0.0_AB_MSTR~Z` at Msg-ID 20797 (ACKed by this seat), and
repeated in this seat's own launch prompt:

> "Looks like there was some kind of reboot activity, i need you to get your cto~Z and various coo~Z ~ZZ ~ZI back online with CVO~Z working on the nfra projects including opsec202609, report, and iamrole202609 or whatever the Iam project was. Before doing all that however you might as well push. But instruct cto~Z to confirm who was on what based on commits and then get those coo's running /canonical-flow to figure out where their projects left off midstream"

The limb assigned to this seat is the middle clause: **confirm who was on what, from commits.**
Not adjudicated wider or narrower.

## What this document claims, and what it does NOT

**CLAIMS:** which seat AUTHORED work against which project, measured from commit authorship and
commit text. That is a fact about the past.

⛔ **DOES NOT CLAIM the limb any project sits at.** A commit subject says who touched what, never
whether the work behind it is finished. Measuring the limb is `/canonical-flow`'s act at each COO
lane, from artifacts rather than status prose — which is exactly what Andrew's next clause orders.

## Instrument and denominator

| | |
|---|---|
| instrument | `git log --all` (every ref, no page, no `--since`) + a project vocabulary grounded in `org/missions/DIRECTIVES.yaml` and `DIRECTIVES_RETIRED.yaml` |
| lifetime denominator | **38,540 commits** reachable from `--all` |
| recent-window denominator | **355 commits** since 2026-09-08T00:00 local |
| project extraction | registered project codes matched in SUBJECT first, falling back to BODY only when the subject carries none; every unmatched commit lands in a printed RESIDUAL bucket |
| second instrument | `get_live_agents` (broker), for the occupancy half — a different instrument from git, not a re-run of it |

This is a census, not a page. `0.0.0_AB_MSTR~Z` read 40 subject lines and said so; this read is the
confirmation Andrew assigned and it disagrees with that read in three places, listed below.

## THE MAPPING — CONFIRMED

Ordered by each seat's most recent commit. Times are LOCAL (-04:00) as git renders them.

| seat | project | lifetime commits | since 09-08 | last commit |
|---|---|---|---|---|
| `3.0.0_SA_CVO~Z` | **NFRA_OPSEC202609** (round 2, L9) | 60 | 12 of 14 | 2026-09-10T02:09:55 |
| `2.0.0_SA_COO~Z` | **NFRA_OPSEC202609** | 144 | 30 of 33 | 2026-09-10T02:02:09 |
| `2.0.0_SA_COO~ZI` | **NFRA_IAMROLES202609** | 1 of 2 | 1 of 1 | 2026-09-10T01:46:45 |
| `1.0.0_SA_CTO~Z` | **cross-project** (see below) | — | 36 | 2026-09-10T01:29:18 |
| `2.0.0_SA_COO~ZZ` | **NFRA_REPORT** | 35 of 38 | 35 of 37 | 2026-09-10T00:56:59 |

`1.0.0_SA_CTO~Z` is deliberately not given one project — its commits since 09-08 split
NFRA_REPORT 12 / NFRA_OPSEC202609 10 / NFRA_IAMROLES202609 8 / D1_CATVIEWS 2 / ADVI_49F 2 /
NFRA_CLDGRPH 1 / ADVI_INSURE 1, which is the routing-and-rulings shape the L2/L3/L10 limbs produce.
Its single most recent act is the **D1_CATVIEWS L2 endpoint cut** at `2c602969c7`, not an NFRA project.

**`0.0.0_AB_MSTR~Z`'s 40-commit read is CONFIRMED on all five rows.** The three corrections below are
additive — none of them moves a seat off its project, so **no re-seating is required and the COO
lanes' `/canonical-flow` assignments stand as spawned.**

## CORRECTION 1 — the author-spelling defect is real, and WIDER than flagged

`0.0.0_AB_MSTR~Z` flagged that `2.0.0_SA_COO~ZZ` appears under two spellings. Measured:

- The split is **19 / 19 — exactly half.** A census matching the tilde form alone undercounts that
  lane by 50%, and reports 19 commits for a lane that made 38.
- **The underscore reaches the EMAIL too** (`2.0.0_SA_COO_ZZ@opal.agent`), so the two spellings are
  two distinct author identities to git. They are the same seat: the `_ZZ` commits' subject lines
  self-identify as `2.0.0_SA_COO~ZZ` (`drive(2.0.0_SA_COO~ZZ): tick 12 ...`). The subject is the
  discriminator; the `--author` value is what is malformed.
- **It is not specific to `~ZZ`.** Over 14 days: `0.8.0_AE_CloudComp_W` (3 commits) has **no tilde
  form at all**, and `4.0.0_SA_CRO_X` (1) sits beside `4.0.0_SA_CRO~X` (17). Any per-seat count in
  this estate that keys on the tilde form is short by an unknown amount.

Surfaced, not chased — no remediation is authorized here.

## CORRECTION 2 — `2.0.0_SA_COO~Z` is on a SECOND project the register cannot see

Its since-09-08 mix is not purely OPSEC. It cut **`L6(NFRA_SYSPARITY.RB1-SITEZ)`** at 09-09T19:24
and fixed that order's malformed id at 21:22 — and **`NFRA_SYSPARITY` appears ZERO times in
`DIRECTIVES.yaml` and zero times in `DIRECTIVES_RETIRED.yaml`.** The order was worked and completed
by `0.7.0_AE_CloudOps~Z` (`complete(NFRA_SYSPARITY.TO-RB1-SITEZ)` at 21:55).

Two further project-shaped codes are absent from the register the same way: **`NFRA_MSGRAPH`**
(`0.8.0_AE_CloudComp_W`'s FWD-12 derive-caller migration, last 09-10T01:43) and **`NFRA_HEATMAP`**.

This is the shared-dependency check paying off: every row in the table above was matched against one
vocabulary, so a project missing from that vocabulary would have been invisible in *every* row at
once, with no per-seat arm failing. The unscoped pass over subject tokens is what surfaced it.

## CORRECTION 3 — six lanes that were WORKING these projects are NOT relaunched

Measured two ways: git authorship on the three NFRA projects since 09-08, against `get_live_agents`
(6 live rows: the five relaunched seats + `0.0.0_AB_MSTR~Z`; **zero `AE_*`, zero `CRO`**).

| lane | project | commits since 09-08 | last commit | live now |
|---|---|---|---|---|
| `0.6.0_AE_PartnerETL~Z` | NFRA_OPSEC202609 | 1 | 2026-09-10T02:09:28 | **NO** |
| `0.5.0_AE_OpalETL~Z` | NFRA_OPSEC202609 | 2 | 2026-09-10T01:57:42 | **NO** |
| `0.8.0_AE_CloudComp_W` | NFRA_OPSEC202609 / NFRA_MSGRAPH | 2 | 2026-09-10T01:53:17 | **NO** |
| `4.0.0_SA_CRO~Z` | NFRA_REPORT, NFRA_IAMROLES202609, NFRA_OPSEC202609 | 10 | 2026-09-09T23:05:48 | **NO** (reported DEAD by `0.0.0_AB_MSTR~Z`) |
| `0.7.0_AE_CloudOps~V` | NFRA_OPSEC202609 | 17 | 2026-09-09T22:16:32 | **NO** |
| `0.7.0_AE_CloudOps~Z` | NFRA_OPSEC202609, NFRA_SYSPARITY | 4 (OPSEC) + 3 (SYSPARITY) | 2026-09-09T21:55:00 | **NO** |

The top three were committing **within twenty minutes of the reboot** — `0.6.0_AE_PartnerETL~Z`'s
02:09:28 commit is the last non-CVO commit on the fabric before the seats died.

**Why this matters to `2.0.0_SA_COO~Z` specifically:** `0.0.0_AB_MSTR~Z` recorded (msg 20797, and
the org/XXX.md Step 1b-F row) that NFRA_OPSEC202609's open round runs **31 of 31 orders on external
`0.7.0_AE_CloudOps~*` lanes**, not on v3 worker subagents. That was measured from task orders. This
seat reaches the same place from git authorship plus broker occupancy — a different instrument, so
it is corroboration rather than repetition. **The consequence: `/canonical-flow` on NFRA_OPSEC202609
will find open orders issued to seats that no longer exist.** Whether to re-seat those lanes or
re-cut the orders onto v3 subagents is `2.0.0_SA_COO~Z`'s call at L6, not this seat's.

⚠ **`0.9.0_WK_NFRA_REPORT~1/2/3` are deliberately NOT in that table.** They are v3 worker subagents
of `2.0.0_SA_COO~ZZ`; they never register on the broker, so their absence from `get_live_agents`
carries no information at all and is not evidence of a missing seat.

## Open calls this document does NOT resolve

Both stand from before the reboot and are untouched by the push and by this confirmation:

1. **Who issues for `0.8.0_AE_CloudComp` on site Z** — routed to Andrew by this seat at msg 20792.
2. **No live CRO on this fabric** (`4.0.0_SA_CRO~Z` dead), so any new L1 brief has no owner.

## Residual, stated

The extractor left 769 of 1017 (`1.0.0_SA_CTO~Z`), 441 of 949 (`2.0.0_SA_COO~Z`) and 382 of 664
(`3.0.0_SA_CVO~Z`) lifetime commits unmatched to any registered project. Sampled, these are session
logs, `law(...)` edits, `fix(...)` on tooling, merges and chores — commits that genuinely carry no
project. The residual is printed rather than suppressed because a project code the vocabulary lacks
would hide in exactly this bucket, which is how CORRECTION 2 was found.
