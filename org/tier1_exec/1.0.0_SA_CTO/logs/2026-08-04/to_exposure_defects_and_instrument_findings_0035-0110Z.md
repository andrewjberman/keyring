# TO-exposure defects, instrument findings, and the vocabulary census facts (0035-0110Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE

Window opens where `2026-08-03/served_integrity_findings_c1_dc1_nerves_2225-2340Z.md` addendum 3
closed (@034cbbe32d, the 87% exposure). **Zero commits authored by me this window** -- every ruling
landed as an MCP verdict into another seat's commit, which is the correct shape for a gate-holder and
is why the git-scoped pull is empty. The XXX.md law (@415eef540e) belongs to the prior window.

## What this window produced

**Three new defects from the 59-row staleness cut (`0.7.0_AE_CloudOps~B`):**

1. **LIVE DISPATCH HAZARD -- `NFRA_COMPLEARN.AMD-P3a` exists twice and the copies disagree.** One says
   `STAGED -- DO NOT ISSUE, ANDREW-GATED-ON-SPAWN` and names lane `~A`; the other names `~B`; **both
   read `status=pending`.** RULED: **latest + most-restrictive binds applies ACROSS COPIES of one TO**
   exactly as across instructions -- DO-NOT-ISSUE wins immediately, everywhere. ~B told not to work it;
   hold stands until COO's dedupe adjudicates with that ruling as tiebreak.
   **This is CI-R7R8 INVERTED:** there a real P0 was invisible; here an Andrew-gated item reads
   dispatchable. The first cost ten days; the second could have spent Andrew-reserved authority.
2. **Two `pending` TOs untracked in git** (`0.8.0_AE_CloudComp`) -- existed only on this laptop's disk,
   would evaporate on any clean checkout. Ruled tonight-class. **CLOSED before my ruling arrived** (COO
   preserved @4da7b6d77f); ~B **verified on the primitive** (git history + sentinel re-run, zero still
   untracked) rather than accepting COO's report.
3. **`comp-pipescript deployed` is BLIND to Model-B cross-tree deployment** -- returned "all
   up-to-date" on the exact file whose bd copy was six weeks stale. Scopes by the script's REPO HOME,
   so a shared script deployed into a second firm's bucket is outside coverage. **`0 UNCOVERED` is
   itself cot-scoped.** Routed as a named input to the comp-tool universe audit.

**bd-plane six-week delta review (`~B`, read-only): both changes SAFE-AS-IS, no deploy ruling owed.**
"Six weeks diverged" collapsed to **TWO commits with an exact fork point (`4632383568`) and an EMPTY
residual**. F1 (declarative drift on a schedule anchor) FIXED @f1d6f2294c ahead of the T2.C apply,
comment-only PROVEN not asserted. bd deploy GO'd at DS, hash-pinned, boundary held.

**comp-blast declared-territory residue CLOSED (`~A`, @3a1f36e544).** Population is now a **PREDICATE,
not a roster** -- role-based (>=1 outbound WRITES|PROJECTS_TO|TRIGGERS|...), N=842 of 20,480, printed
every run so a change in N is a coverage FINDING, not noise.

## Laws and rulings issued this window

| ruling | content |
|---|---|
| Most-restrictive-binds ACROSS COPIES | A DO-NOT-ISSUE copy beats a `pending` twin, immediately, regardless of which file a reader opened |
| Risk-reflex disposition (SPLIT) | **KEEP the over-firing** (file-scoped is correct; over-fire beats under-fire on an immune response) / **FIX the wording** -- "before this commit proceeds" is an IMPERATIVE describing a GATE printed by a NUDGE. Same defect Rule 20 was corrected for. **An imperative that does not gate trains agents to read real blocks as noise**, and it sits on the commit path every agent takes |
| F2 -> universe audit | **A COVERAGE COUNTER EVALUATED WITHIN THE SCOPE IT IS MEANT TO AUDIT WILL ALWAYS READ ZERO** -- strictly worse than no counter, because the zero is read as assurance |
| Predicate-not-roster | The audit's test for every (c)-class tool: **IS THE UNIVERSE A PREDICATE OR A LIST?** A type-based population re-encodes the same accident in new names |
| Doctrine-2 extension RATIFIED (`~A`) | **A suite that starts SKIPPING is the VISIBLE half. The INVISIBLE half is a suite whose FIXTURE STOPS SELECTING -- no skip, no failure, full green, zero coverage.** Detector for both: assert the DENOMINATOR the test exercised, and MUTATE to prove it can fail |

## Three corrections OF ME, all accepted (running total this session: 8)

1. **"Third folder family / structural defect" -- WRONG, and I AMPLIFIED it.** It is COO~A's deliberate
   07-10 spec-home convention with lane pointer copies. ~B narrowed their own finding after COO supplied
   provenance; I had already endorsed and broadened the wider version. **The narrower true finding
   survives: a pointer that drifts from its spec is worse than no pointer.**
2. **"The schedule-anchor premise is INVERTED" -- WRONG; it is HALF-inverted.** The lag is
   table-family-scoped, so PERIOD tables are unchanged and my 16:30 ET anchor argument still holds for
   them; only SNAPSHOT tables shift. **~B's formulation, which is the better finding: "it was not simply
   stale; it was HALF-RIGHT IN A WAY THAT READS FULLY-RIGHT, which is worse."** A wholly-false paragraph
   is caught by the first reader who checks a claim; a half-true one survives every spot-check.
3. **A parity check would close the pointer drift -- IMPOSSIBLE.** 6 of 7 pairs have the spec copy
   carrying ONLY `issued_to` and the lane copy ONLY `assigned_to`: **no shared field exists to drift
   against**, so no diff/lint could EVER have detected the disagreement. Structurally unobservable, not
   missed. Disposition narrows to: unify the field name first, or path-only pointers (the only option
   that cannot regress -- **a path-only pointer has nothing to drift**).

## The vocabulary census (MINE, for a calm board) -- scope now set by evidence

- **`status` is UNANIMOUS `pending` across all 14 pair files. A FIELD WHOSE VALUE NEVER VARIES CONVEYS
  ZERO BITS** -- `status` is decoration; all real state migrated into fields never designed for it (the
  gate in prose inside my own `OPLMCP.06` status text; the dispatch-hold in prose PAST THE SERIAL inside
  the ASSIGNEE field, 5 of 7).
- **The question is therefore NOT "which states are missing" but "WHERE DID THE STATE GO, AND WHY DID IT
  LEAVE."** State migrates into prose because the vocabulary could not express what the author needed,
  and prose is the only field that never rejects a value.
- **Method (COO, binding): ENUMERATE FROM THE WILD SET, not the states we remember.** Documented
  vocabulary is `staged`/`pending`/`complete`; tonight surfaced three more in the wild
  (blocked-on-dependency, Andrew-gated-on-spawn, held-for-disclosure). **First deliverable is a census of
  what `status`/assignee/body free-text ACTUALLY say across all 1,856 TO files** -- not a design meeting.
- **Control worth keeping:** `AMD-P3d`, the ONE pair where both copies use `assigned_to`, is the LEAST
  divergent. **The pair that COULD be compared is the pair that stayed closest.**

## Compiler Tools

| tool / probe | result | note |
|---|---|---|
| `python .tools/to-check.py --all --assignee <serial>` (x4: mine, ~B's, unfiltered, nonexistent-serial) | PASS | **Exercised BEFORE committing the law that mandates it.** Surfaced two output traps I then wrote into XXX.md: `--assignee` is a SUBSTRING match; the rollup groups by PRIMARY assignee so a JOINT TO hides under another seat's heading. The nonexistent-serial run confirmed NO fallback-to-all (total=0), which was the failure mode I was checking for |
| `git show`/`log`/`cat-file` + file-existence discrimination | PASS | Separated 20 benign nerves losses (LD-0371 deletions) from 2 real ones; verified `a1cab01483`, `14b3a3da7d`, `4da7b6d77f` on disk rather than on report |
| `aws s3api head-object` (cottonwood slice ETag) | PASS | Verified the DC1 serve-hold INDEPENDENTLY -- ETag still `44db6559...`, i.e. the held collapse is NOT in production. A production claim made by the seat that just deployed to production needs a second pair of eyes |
| `grep` with POSITIVE CONTROLS (trigger file) | PASS | `roster`=0 and `cottonwood`=0 against `inflection`=5 -- the control is what makes the zeros real absences rather than a broken pattern |

**What worked:** exercising an instrument before ruling on it caught my own law text mid-draft, and
caught ~B's TO premise before a fix was built for a defect that did not exist.
**What failed:** nothing this window.
**Gap found:** `comp-pipescript deployed` cannot see Model-B cross-tree deployment targets (F2 above);
the `0 UNCOVERED` counter is computed inside the gap it exists to flag.

## Current State (zero prior context assumed)

**THE ONE SOVEREIGN ITEM: Andrew's cottonwood disclosure call.** Complete on inputs, nothing moves on
the served surface without it.
- **Double count** (3 naive summers, collapse to `(AccountID, AssetID)` missing): **July episode
  +$205,070.77/day, window OPENED 07-21, STILL SERVING**; **June episode 06-15..06-18 at
  +$336-339K/day, CLOSED but the served artifact still carries it.** Fix BUILT + exercised tie-exact
  @3accc408f8, **DEPLOY HELD**; deployed slice verified still at the pre-fix ETag `44db6559`.
- **Shell-class partials reaching served values**: 4 serve days (07-28..31) x 12 platinum artifacts;
  **depth = FLOWED** -- ADV attribution degenerated to one bucket carrying the whole firm
  (`views.adv.y1/y2/y3.donut.total` served 463,649,292.59 where 436,654,607.00 / 0 / 0 belongs; CLA geo
  inflows ~70x). **Window CLOSED at the 08-01 publish; forward fix (LAG=1) DEPLOYED** @bf4c0aabbe.
- **Residual, recorded not built:** the guard tests `has_data == 0` (ZERO ROWS) while the real failure
  is a 1-3-row PARTIAL that passes. **LAG=1 is producer-avoidance, NOT a control fix.** Routed to
  OVP WS-5.

**In flight, gated on evidence not people:** T2.C clock v2 authored (ET-anchored, derived 10:45 ET
close, 11:00 ET floor, publisher migrating Rule->ET Scheduler) -- apply waits on the schema chain +
Andrew's word at AE's terminal (their seat under an operator hold since ~2312Z). C1impl two-stage: Leg A
parity+heal ships alone, Leg B rides Andrew with DC1 as ONE serve-correction event I orchestrate.
Participation schema DEPLOYED @85e7eb3922 (DELTA=0 value-verified, all 3 labeling requirements
demonstrated on real data). T5.B gate set = {CANON PROVEN, C1, C2}.

**Mine, carried:** the CHANNEL_INDEPENDENCE closure-row sweep (delivery-state + gate-state per row,
**MISSING stated as MISSING never inferred from delivery**, + a supersession verdict per row); the
vocabulary census scoped above; the comp-blast Part-2 PRD post-audit.

**Held for a calmer window (both durably carried, neither dependent on one record):**
`ANDREW_DIRECT_20260714_TAXSMA` (pending, hidden, 3 weeks, dead seat) and AMD-P3a's final disposition
(its held copy reads ANDREW-GATED-ON-SPAWN).

## Next Steps

- **[Andrew]** the cottonwood disclosure call -- disclose+correct, or correct-forward. Nothing else waits on him.
- **[1.0.0_SA_CTO]** closure-row sweep; vocabulary census (start = free-text census over 1,856 TO files); comp-blast Part-2 PRD after the universe audit.
- **[2.0.0_SA_COO]** dedupe-then-dispatch (AMD-P3a lead adjudication) **with a disposition on the CONVENTION itself**, not just the 7 pairs; 60-pending triage by record-reading; TAXSMA morning triage with MSTR.
- **[0.7.0_AE_CloudOps]** T2.C apply chain on the gates; the risk-reflex wording fix as a small item.
- **[0.7.0_AE_CloudOps~B]** post-change verification of "no partner literal survives" -- greps WITH a positive control, both directions.
- **[0.4.0_DS_ClientPlatform]** T4.A remaining families; OVP WS-5 completeness predicate (the partial-blind guard).
- **[0.2.0_DS_PortfolioAnalytics]** DC1 deploy on Andrew's word; C2b discriminating mutant (absence -> honest-None, corrupt -> raises).
