# CTO~X SESSION LOG -- SPRING CLEAN + DIRECTIVES-CHECK TIGHTENING -- 2026-08-25 16:40Z

**Seat:** `1.0.0_SA_CTO~X` (lane X, PID 2164). **archetype:** MIXED. **secondary_archetypes:** DIAGNOSE, BUILD, COORDINATE.
**Window:** 2026-08-25 ~16:03Z -> 16:55Z. **Commits THIS SESSION: 2 -- `c06bb5a819` (LINKAGE partition) and
`9cdef47ebd` (this log). Both are ON `origin/CLOUD`** (ls-remote read, not a cached ref; MSTR's push carried them).

⛔ **SESSION-vs-SERIAL, stated here because this log is the only durable place it survives:** `1.0.0_SA_CTO~X`
carries earlier work from a **PREDECESSOR SESSION** -- `00004eac8b` (2026-08-25T00:19Z, the "Agg" positioning
trace + `usePersistentToggle` + portal `d53049a0`). **That is NOT this session's work.** A future census keyed on
`--author` will attribute it to "CTO~X" and be **right about the serial and wrong about the session**; `--author`
matching cannot separate a predecessor from a successor, and the audit line has one identity field. Any defect
rate derived from "CTO~X's commits" must state which session -- notably a `safe-commit` verify-helper SyntaxError
reported as "2 of 4 commits", whose denominator belongs to the predecessor: **this session saw zero.**

**MANDATE (Andrew-direct, ~15:47Z issued to base CTO, REASSIGNED to this lane ~16:0xZ):** handle spring
cleaning + directives/directives-check tightening so base CTO can hold the fabric. His scope: assess
`/directives-check` state, correspond it with the underlying projects, tie them in harder, judge whether
PRDs/registrations need adjusting, sequence the work, and **relay to COO who issues spawn requests to MSTR.**
Plus the ~15:5xZ addition: *"systematically start closing out old projects/TOs with some kind of tag that
signifies that it was closed for dormancy/potentially superseded but regardless irrelevant now."*

---

## 1. THE FINDING THAT REFRAMED THE WHOLE TASK

**Andrew asked us to close "old" things. By the estate's own ratified definition, NOTHING IS OLD.**
`0 of 124` open projects clear Rule 25's 90-day dormancy bar; oldest is `YALP_MACROS` at **80.9d**.

I did not take that at face value, because a zero is exactly the shape a broken instrument produces:
- **Two independent age signals** -- last commit touching `org/projects/<CODE>.json`, and last commit
  *naming* the code -- **agree at zero.**
- **No bulk clock-reset** manufacturing it: zero commits in the last 400 name >=8 project codes; the only
  >=15-JSON commit is `44c6925b35` (2026-05-22), itself a dormancy close-out.
- Conservative signal-A-only measure: **still zero.**

So a Rule-25 sweep run today selects nothing. **That is an answer, not a blocker** -- and it forced the
real question: if not age, then what?

**THE REFRAME: THE DEBT IS CONSISTENCY, NOT AGE.** Open TOs partition MECE and sum exactly to `to-check`'s
own denominator:

| Class | TOs | Projects | Basis |
|---|---:|---:|---|
| **A** | 75 | 32 | open TO on an **already-terminal** project |
| **B** | 114 | 65 | open TO whose project has **no registration JSON** |
| **C** | 13 | 3 | open TO on a hold/dormant project |
| LIVE | 183 | -- | genuinely open work on open projects |
| | **385** | | **sums to 385 of 385** |

**202 of 385 (53%) need NO age bar and therefore NO sovereign threshold.** A TO left open on a project
already marked complete is stale by construction. That is the executable spring clean.

## 2. AN INSTRUMENT ERROR I MADE AND CAUGHT

My first TO census read **438 open**. `to-check --all` reads **385**. I did not publish either number --
I replicated to-check's own classifier and found **my** error: I read only the `<status>` XML tag and
missed the `**Status:**` markdown fallback that to-check also reads. Corrected replication: **385, delta 0.**
*A number that disagrees with the estate tool is my bug until proven otherwise.*

## 3. THE TRAP I DID NOT WALK INTO

MSTR taught this class an hour earlier on `PFMG_TAXSMA` -- a **superseded code** that read as an
unregistered project, where the obvious remedy ("mint the missing JSON") would have created a second
file for a live project under a dead code. I applied that lesson to Class B3 before handing it over:

- `MDPF_REMED` (11 TOs) -- referenced by `MDPF_PIPELINE_TRUTH` + `MDPF_PROVCANON`. **`MDPF_PROVCANON` is 1 DAY OLD.**
- `ADVI_BDPARITY` (4) -- referenced by `ADVI_49FSRC` + `ADVI_PERFRP`, both **live D2 members**
- `COT_SUPERVISED`, `ADVI_49F` -- likewise referenced by live projects

**THE DISCRIMINATOR IS REACHABILITY, NOT AGE.** A naive orphan sweep would have closed TOs that live
projects still point at. Base CTO independently found the mirror trap on the project side (47 "closable"
projects, 8 of them <=5d old and pre-decomp).

## 4. WHAT I BUILT -- the LINKAGE partition (`c06bb5a819`, LOCAL)

**The defect: membership was ONE-DIRECTIONAL.** The engine read `DIRECTIVES.yaml -> members.projects`
and nothing read back, so the board could not see a project belonging to no directive.

```
COVERAGE      15 of 124 open projects are on a live directive (12.1%)
UNAFFILIATED  109 open projects belong to NO directive -- invisible to the board
BACK-POINTERS 1 of 333 JSONs carry a `directive` field (0.3%) -- the migration denominator
```

**The board displayed an eighth of the open population while its rows read as though they covered the
estate** -- the exact retrieval-control class CLAUDE.md names: a count with no frame. Per-row TO counts
now carry the estate denominator (`19 of 385 open estate-wide`). Added `GHOST MEMBERS`, `DISAGREEMENT`
(a project claiming a directive that does not claim it back), and `STATUS RESIDUE` (projects in neither
the declared open nor terminal set -- printed, excluded from every count, **assumed in neither direction**).

**Verified by exercise, not assertion:** 9/9 planted-mutant controls pass on **both arms** -- every
detector fires on a synthetic defect **and** an agreeing project stays silent, so they are not
undiscriminating. `--json` contract intact and additive (renderer reads via `.get()` throughout);
`--code`/`--retired` correctly suppress the partition; `ruff --target-version py39` clean; `py_compile`
clean; **0 non-ASCII lines introduced** (SKILL.md's 4 are pre-existing, verified against HEAD).
Its own denominator reconciles exactly with the estate tool: `open_tos=385 == to-check --all`.

**Still status, never action.** Both files are lane `ANY`; **nothing touched `org/missions` or `org/projects`.**

## 5. THE TAG DESIGN -- PROPOSED, NOT MINTED

Build-ladder rung 2 first: `superseded_by` already exists (9 projects) and precedent `44c6925b35` already
ran CLOSE-COMPLETE / CLOSE-SUPERSEDED / ON-HOLD. **Extend that, do not mint a parallel vocabulary.**

Two-field split (RCG-charters-v2 remedy pattern): `status` = lifecycle state; `closure_reason` = termination
cause, required iff closed. Four-postulate record in the COO relay. **Rule 24(iv) declared asymmetry:
`superseded` requires a companion `superseded_by`; the other three values do not -- named because the
postulate requires naming which values do not move together.**

**Token hygiene (word-boundary, canon + all 333 JSONs):** `closure_reason` = **0, free**. `disposition` =
**65 in project JSONs -- OCCUPIED, that name is OUT.** And **`Lifecycle_Stage` is PRIOR ART** (CLAUDE.md
Rule 24 names it the compliant enum specimen from 08-20) -- **this must reconcile against it, not be coined
beside it. I have NOT done that reconciliation.**

**Migration cost, measured: 317 of 333 map mechanically (95%); 16 need a human read (5%).**

## 6. ROUTED TO ME BY MSTR, GROUNDED AT SOURCE, DELIBERATELY NOT FIXED

`comp-directives check` returns **rc=2 on a CORRECT register** (`PARTITION: D8 in BOTH views`). Read at
source: `comp_directives.py:251` does `set(live_ids) & set(ret_ids)` -- **the schema treats a directive id
as a permanent unique key while Andrew uses the number as a refillable SLOT** and re-minted D8. Rule 24(ii)
same-grain: **his usage is not the error, the schema is.**

I did **not** fix it in the same breath as everything else: it is a live gate with a 10/10 self-test on a
hand-edit-sealed file, and changing partition semantics means changing the gate's own control. **Urgency
flagged: an rc=2 that is EXPECTED on a correct register trains people to ignore the gate**, which is how a
real breach gets waved through.

## 7. COMPILER TOOLS

- **`/directives-check`** (the subject of the work) -- run bare pre-change for the baseline board, and again
  post-change to exercise the new partition; `--json`, `--code D7`, `--retired` run as scope controls.
- **`.tools/to-check.py --all`** -- the TO denominator of record (385). Used as the **oracle against which I
  falsified my own 438**, not as a second opinion.
- **`comp-directives check`** -- surfaced the partition violation MSTR routed; true `rc=2` measured by running
  it **unpiped** (my first read showed `rc=0` because `$?` after a pipe reports `tail`, not the tool).
- **`.tools/owned-paths-validate.py`** (read) -- resolved my own lane's write surface at source rather than
  assuming it.
- Raw `git log`/`grep` used for the age census: no comp-tool covers "last commit naming a project code" as a
  per-project age signal. `comp-heat freshness` was surfaced by the HUD and is the nearest neighbour, but it
  ranks **cold subtrees by write-history**, not project-code mentions -- a different grain, so it would not
  have answered the dormancy question. **Possible coverage gap; flagged, not claimed.**

## 8. STATE AT CLOSE

- **Delivered:** COO relay `70754` (+ base CTO `70755`, MSTR `70756`), 3/3 DELIVERED, bodies verified
  non-empty at ~10.3KB each (an empty body and a real one return identical receipts).
- **`@c06bb5a819` + `@9cdef47ebd` are ON `origin/CLOUD`** -- verified by `git ls-remote` and `branch -r --contains`.
  (Stated as "landed LOCAL" in msgs 70754-70756, which was TRUE WHEN WRITTEN and went stale when MSTR pushed;
  corrected to the three recipients in 70768-70770. **MSTR has pushed twice more since -- re-read the tip rather
  than pinning a hash.**)
- **At Andrew, and NOT to be inferred:** (a) **the bar** -- Rule 25's 90d selects zero; 60d would select 12,
  30d would select 45. Picking it is a Rule 24 act and it is his. (b) **retro-tagging volume was already
  carded 08-24 and is unanswered**; his 08-24 ~14:12Z ruling was DIRECTION RATIFIED / MIGRATION NOT
  AUTHORIZED, and **my LINKAGE partition does not authorize it -- it only makes the population countable.**
- **Owned-paths:** `1.0.0_SA_CTO~X` is **not** enumerated in `ANY_EXEC_OR_AE` (`~C` is) or `ANY_CTO` (`~B` is)
  -- the documented recurring tilde-lane gap. I hold `logs/` + `task_orders/` by the home-folder convention
  and **cannot commit project JSONs or deliverables.** Not blocking this session's scope; **it would block S4
  if that lands here.** Raise as `[OWNED-PATHS AMEND ASK]` via COO at that point, not pre-emptively.
- **No gate created, nobody spawned, no approval step invented.** Sequencing S1-S5 is a recommendation to COO.

**Blockers:** none at this seat.

---

## 9. A MIS-SOURCING I MADE, AND THE CLASS IT BELONGS TO

In msgs 70768-70770 I corrected an attribution and **routed the correction at the wrong author.** I wrote
*"MSTR's push message credits CTO~X with the AGG removal..."*. **The substance was right -- that work is a
predecessor session's, and MSTR agrees -- but the SOURCE was wrong.** The message is **msg-id 67347, dated
2026-08-25T00:20:46Z**: a *predecessor MSTR session*, sixteen hours before this seat existed. The current MSTR
grepped its own sent traffic before replying and found no such claim, and correctly noted that `d53049a0` does
not even resolve in this tree.

**HOW I GOT IT WRONG:** a `heartbeat()` returned five queued messages in one block, and **I read the block as
current traffic.** The oldest was 16 hours old. The envelope says `0.0.0_AB_MSTR` -- which is TRUE OF THE SERIAL
and says nothing about the session.

⛔ **THE CLASS IS THE ONE I WAS CORRECTING: I READ A SERIAL AS A SESSION, INSIDE THE ACT OF TELLING SOMEONE ELSE
NOT TO.** Knowing a failure mode by name does not immunize you against writing it.

**AND A CORRECTION DELIVERED TO THE WRONG AUTHOR IS WORSE THAN NONE** -- it reads as discharged while the real
record stays uncorrected, and it puts a false claim about the *current* author into three inboxes.
**MECHANISM, not care: a queued-message dump carries no recency frame. Read the `Msg-ID` and `Date` header on
every message you act on -- the delivery order is not the authoring order.**
