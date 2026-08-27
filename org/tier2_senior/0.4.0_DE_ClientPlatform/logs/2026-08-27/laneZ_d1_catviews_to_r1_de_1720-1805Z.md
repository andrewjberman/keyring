# Seated on a TO that was already done -- and the one cell nobody had exercised was the one that mattered

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (primary), BUILD, DIAGNOSE, COORDINATE

**Date:** 2026-08-27
**Task Order:** D1_CATVIEWS.TO-R1-DE (successor seat to `0.4.0_DE_ClientPlatform~C`)
**Status:** TO-R1-DE **complete** -- flipped, evidenced, CVO-ruled. Holding nothing.
**Portal commits:** `7ed51b9e` (DEV) -- **LOCAL**
**Workspace commits:** `91706ed0b1`, `ede6a45212` -- **LOCAL** (`0.0.0_AB_MSTR~Z` is the integrator)
**Window:** 2026-08-27T17:20Z -> 18:05Z

---

## Objective

Seated by MSTR~Z 9329 / COO~Z 9336 on `D1_CATVIEWS.TO-R1-DE`, portal frontend, D1_CATVIEWS ONLY.
The brief said explicitly: *successors to seats that FINISHED, not revivals* -- read the TO and the
artifacts, what is open is open.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `to-check.py` | `--all --project D1_CATVIEWS` (x2) | PASS | The discriminating call for a lane seat -- `--assignee` is the broken one (DE~C's banked finding). Re-run AFTER my own edit: 4 ACTIVE -> 3. |
| `to-check.py` | `--all`, filtered to DE class | PASS | Rule 27 self-check: **zero** open TOs addressed to `~Z` besides this one. COO~Z's 9336 reflex, run on my own serial. |
| `proof-of-spec-check` | not run | N/A -- **stated, not blank** | The instance was already VALID and CVO-CERTIFIED; re-running the author's own passing check is repetition, not corroboration (Rule 22). I re-derived the RENDER instead, which is the plane the checker cannot see. |
| `bun run typecheck` | `tsc -b --noEmit` (x2) | PASS rc=0 | 11,675ms then 12,193ms. **The DURATION is the oracle** -- discriminates the build-mode form from the 277ms zero-file no-op at `ci.yml:56`. |
| `bun run lint` | `eslint .` | PASS rc=0 | 0 errors / 7 warnings -- **the same 7** DE~C measured at `fce757cb`, so my change added none. |
| `ui-smoke.mjs` | 9 runs: 2 fixtures + mutant, `--click` x4 | PASS (after a trap) | Every L0/L1/L2 state + both `D1-inv-4` directions. Screenshots **READ**, not merely captured. |
| `git` (ls-remote / merge-base / reflog / rev-list) | push state, ancestry, divergence, overlap set | PASS | Every commit claim carries a **negative control** (a bogus hash that failed as required). |
| `comp-*` | not run | N/A -- **stated, not blank** | Rail advisory fired on the portal search; the questions I actually had were *git ancestry* and *a rendered pixel*, which no comp-tool answers. Named rather than skipped silently. |

**Gap found:** `portal/scripts/ui-smoke.mjs` `--click` matches on the **accessible name**; its
CLICK-FAIL diagnostic prints `aria-label || textContent`. For any control whose label spans block
children -- every tile in this panel -- those differ by whitespace, so **the failure handler hands
you a string guaranteed not to match**. Cost 4 runs. Worse: a zero-match locator and a genuinely
unactionable element produce the *identical* message, so I only separated them with a DOM probe.
Surfaced to CVO~Z, not chased (not in my cells).

---

## Work Completed

### 1. Measured the TO before touching it -- and it was already done

`<status>` read ACTIVE. In the **same file** `<cell_status>` read 8/8 COMPLETE; a CVO cert sat on
disk; DE~C's close-out read DELIVERED + DISARMED; all 5 portal commits were ancestors of
`origin/DEV` **and** `origin/PROD`. **Four carriers of one obligation, and the stale one is the one
`to-check.py` classifies on** -- which is why `D1_CATVIEWS.json` kept telling coordinators
"TO-R1-DE ACTIVE, do not idle it", and why a lane got seated on finished work.

### 2. Re-derived all 8 cells rather than inheriting the record

Per-cell table appended to the TO, **evidence class labelled PER ROW**. `D1-c-2` is marked CARRIED,
not re-derived, because my fixture matched on every run so the no-block branches never rendered here.

### 3. Closed the limb DE~C declared NOT-YET-EVALUABLE

They refused to upgrade the Alternatives inert limb without exercising it -- correct. But the TO
already carried the instrument: the issuer's own AC5 resizing ruled a **synthetic fixture** the right
exercise when zero firms hit a path. Nobody had carried that argument one row down. Now exercised:
tile renders, carries its label, reads `disabled=True` in a probe where the other three read
`disabled=False` -- **positive control inside the same measurement**.

### 4. The finding, and the order that made it actionable

DE~C's `D1-inv-4` row read "closes on both firms" -- a pass with no evidence the indicator could read
anything else. Built the negative control **first**: mutant fixture, `total_aua` 100M -> 110M,
rendered *"$95.00M vs $105.00M -- DOES NOT CLOSE"*. The control is real.

⛔ **Which is exactly what made the next thing worth acting on: the BREACH rendered in
`text-xs text-slate-400`, styling byte-identical to the PASS.** A money invariant whose failure
looked like its success. Fixed in-cell using the file's own amber idiom (`:101`). Both directions
re-exercised **after** the edit -- including the PASS branch, the direction that announces nothing
if it breaks.

### 5. CVO ruling, and the label fixed ON THE LINE

CVO~Z 9431: **NO CERT DELTA owed** -- but the answer ran against their own office. The cert's
*"D1-inv-4 discharged, 8 of 8"* established COVERAGE, not exercised breach-legibility, and all four
of its instruments are structurally blind to a rendered pixel. They also corrected my label:
`AC7` does not appear in that cert; the id is `D1R1DE-AC7`. **Landed on the normative line, not only
in the reply** -- MSTR~Z's seating brief named that exact failure mode this session.

### 6. The eye COO asked for on my 3 BARRED hazard items

Parsed (49 items, census printed): **Z-S45 INERT, needs nothing. Z-S23 carrier-lag** -- but flipping
it retires the *general* bucket-wide-14-day-expiry hazard along with my instance, which nothing else
carries. **Z-S49 is the live one**, and it routes itself to "only a human can close this" on the
claim that `ui-smoke.mjs` has never touched a deployed surface. **Measured: `--origin` landed
2026-07-23; `--token` (real bearer) landed 2026-08-20 by THIS SERIAL -- five days before the item was
written.** Not closed by me: Z-S49 is D4 and Rule 27 bars it. Surfaced with what I could not
establish named.

---

## Decisions Made

- **Flipped the TO myself** rather than routing the flip. `complete` is self-marked by the assignee
  per `org/XXX.md`, and manufacturing a COO approval step would have been a gate Andrew never asked
  for.
- **Fixed `D1-inv-4`'s legibility rather than filing it.** The cell is in my `<decomp_ref>`; that is
  scope, not scope creep. Filing it would have been the safer-looking wrong call.
- **Did NOT decide the cert question on the certifier's behalf.** Cost one message; it caught a
  defect in the cert.
- **Did NOT close Z-S49** despite owning its `disarm_owner` field -- owning a field is not holding
  the project.
- **Stopped after two probes** on the `send_message` body item, and declined CVO's correctly-designed
  third: my own extra data row already excluded the hypothesis it would test.

---

## Files Modified

`portal/src/components/CategoryViewTree.tsx` (`7ed51b9e`);
`org/tier2_senior/0.4.0_DE_ClientPlatform~C/task_orders/D1_CATVIEWS.TO-R1-DE.portal-view-tree-l0-l1-l2.md`
(`91706ed0b1`, `ede6a45212`).

---

## Blockers

**None.** D1_CATVIEWS remains NO-SHIP and `category_views` unpublished -- that gate is not this
lane's, was not touched, and `complete != shipped` is stated on the TO's face.

---

## Current State

TO-R1-DE **complete**, CVO-ruled no-delta, 8/8 re-derived at this seat. All three commits **LOCAL**;
`0.0.0_AB_MSTR~Z` pushes. Portal `7ed51b9e`'s parent **is** the `origin/DEV` tip, so it is a clean
fast-forward: 1 ahead, 0 behind. Zero crons, zero gates created.

---

## Postmortem -- three, and the second one nearly reached another seat

**1. I probed for my own prior work by folder path and got a false absence.** No
`org/tier2_senior/0.4.0_DE_ClientPlatform~Z/` exists -- this serial's logs live in the **base** folder
under `laneZ_*` names. I read "no such directory" as "this serial has never worked here."

**2. And I had a denial drafted on the strength of it.** DS~P credited a measurement to my serial;
I had no session memory of it and my folder probe said absent, so I nearly replied that I never made
it. **It was mine** -- 21 commits under this serial, the finding at `laneZ_etfs_ingest_to5:68`.
Caught by asking git for commits by my own author line. Had it gone, a real finding of theirs would
have lost a corroborating source to a confident denial *from the seat best placed to be believed
about it*. **Absence of my own memory is not evidence of absence of my own work**, and the folder
probe was the wrong instrument for the question.

**3. I asserted LENGTH as the `send_message` discriminator's likely cause in my own head and ran a
probe on it.** CVO falsified it from traffic they had already generated. I could have asked a seat
that sends long messages all day before spending two probes. **The cheapest instrument was another
seat's existing output, and I reached for a new experiment.**

**The property they share:** all three were *retrieval* errors, not reasoning errors -- I picked an
instrument that could not see the thing, and in two of three the clean negative it returned was
indistinguishable from a true absence. The one that did not reach anybody was stopped by a positive
control, not by care.
