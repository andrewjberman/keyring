# NFRA_OPSEC202609 — ROUND 2 ANALYSIS (L10 answered)

**archetype:** VALIDATE

| | |
|---|---|
| **Written by** | `1.0.0_SA_CTO~Z` |
| **Written** | 2026-09-10 ~10:4xZ |
| **Answers** | the round-2 slug, `surprise-channel/remediations/REMEDIATION_v2.Z.md` @`8aace78993`, cut by `3.0.0_SA_CVO~Z` (msg 20895) |
| **Reads** | the PRD at v0.14 (19 declared outcomes), all 31 task orders unscoped, the channel's 168 items, `ledger/L8_PACKET.round2.final.md` |
| **Verdict** | **ROUND 2 DOES NOT CLOSE. IT RECUTS** — and it carries a second, independent blocker the sibling project does not have |
| **Recut owner** | `2.0.0_SA_COO~Z`, one issuance |

---

## 1. COVERAGE READ, PER OUTCOME

**Denominator: 19 outcomes declared in the PRD header at v0.14.** Derived by reading all 31 task
orders UNSCOPED for their outcome references — **not** from a completion report, because none exists
(§6). Status per order is its own `<status>` line.

| | |
|---|---|
| **COVERED** | **18 of 19** — every one has at least one terminal cell |
| **UNCOVERED** | **1 — `FWD-19`** |

Cells per covered outcome ranged 1 to 7; two outcomes (`FWD-14`, `FWD-17`) carry one cancelled cell
each alongside their complete ones, and the cancellations carry the re-entry pointers this seat's
earlier ruling supplied.

### ⛔ `FWD-19` IS UNCOVERED — NO CELL REFERENCES IT

> *"Automated submissions and scraping against the marketing site are refused or challenged, and a
> real visitor is never stopped."*
> **DONE WHEN (EXERCISED):** a scripted submission to the contact form refused or challenged without
> a human acting; a real submission by a person in a browser succeeding unchanged in the same window;
> and the volume of automated submissions reaching the entry store measured before and after.

**This is not drift and nobody dropped it.** `FWD-19` was ratified by Andrew at the PRD's **v0.14**
(2026-09-09 ~16:2xZ) — *after* round 2's decomposition was frozen. A frozen decomposition cannot
grow a cell mid-round; that is the rule working. The outcome has simply never had a round.

⭐ **AND IT IS THE ONLY OUTCOME ON THIS PROJECT SOURCED FROM A USER-VISIBLE COMPLAINT** — Andrew's
own words at this seat's terminal: *"We get a lot of bullshit form fillouts that are surely
programmatic from bots."* Its bar was deliberately calibrated down in the same session (*"Naive
majority is fine for now"*), so it is a small, bounded, high-salience piece of work rather than a
research problem. **It is the first thing round 3 should cut.**

**ROUTE:** rule 27 gives this seat a PRD addendum for an outcome no cell served, or a round-N
analysis. `FWD-19` needs no PRD change — it is already ratified, bounded and calibrated at v0.14, so
an addendum would restate a settled spec. It is carried into the recut instead, in §3.

---

## 2. WHAT THE ROUND ACTUALLY PRODUCED

| | |
|---|---|
| task orders | **31 terminal** — 29 complete, 2 cancelled with re-entry pointers |
| investigation items | **168**, **0 undispositioned** — 104 GRADUATED, 64 DISMISSED_WITH_REASON |
| judgment criteria | **2 of 2 graded, both PASS** |
| slug rows | **99** — 94 round-2 graduations + 5 carried from round 1 |
| **of those, ARMED** | **65** |
| **REMEDIATED or DISARMED** | **ZERO** — the CVO verified no remedy landed this round |

⛔ **THAT LAST ROW IS THE STATE OF THE PROJECT, AND IT SHOULD NOT BE READ AS A FAILURE OF THE ROUND.**
Round 2 was a *finding* round: it was cut to look, and it looked well enough to graduate 99 items.
Remediation is the next round's work by design. But it means **the security posture on the ground is
substantially unchanged by round 2** — 65 live hazards are now precisely described and none is fixed.
A reader who sees "168 items, 0 undispositioned" and infers the estate is safer has read the wrong
quantity: that number measures *adjudication completeness*, never *remediation*.

**The four shapes the round found**, recorded because they are worth more than the item list:
- an instrument answering confidently about the wrong object — a liveness oracle returning a clean
  zero for the estate's most-used verifier, and a false belief that propagated through four carriers;
- a control perfectly configured and without effect — five instances, including two login-abuse
  alarms publishing to a topic with **zero subscribers**, every check on the alarm's own side passing;
- a constraint true of the intent and false of the mechanism — a reservation of the blocked-IP sets
  that Terraform declares empty and re-enforces on every apply;
- an artifact that outlived its truth and kept directing — a deploy ledger closed 5/5 on a control a
  later deploy removed, every health signal green throughout.

---

## 3. WHAT THE RECUT MUST CARRY — `2.0.0_SA_COO~Z`, ONE ISSUANCE

**R3-A — `FWD-19`, the uncovered outcome. Cut it first.** The bot/scraper defence for the marketing
site's contact form. Bounded by the v0.14 calibration: the naive majority stopping is success, a
sophisticated bot still getting through is explicitly **not** a failure of this outcome. Its bar is
EXERCISED and its three limbs are testable in one window — a scripted submission refused, a human
submission succeeding unchanged, and the arrival volume measured before and after. ⚠ **The
before-measurement has to be taken BEFORE the defence goes up**; if the cell is cut without that,
the outcome becomes ungradeable and the round is wasted on it.

**R3-B — remediation of the ARMED set.** 65 armed rows carry the live hazards. Sequencing them is
the COO's L5 call, not this seat's; the only constraint from here is that the two login-abuse alarms
with zero subscribers and the blocked-IP-set contradiction are the ones whose *stated* purpose is
currently not being served at all.

**CARRIED, NOT CUT — the five round-1 graduations that had never reached any slug** (`Z-S1`, `Z-S2`,
`Z-S11`, `Z-S13`, `Z-S17`; four of them ARMED). They are in this slug now. They need no new cell —
they need to not be lost again, which §5b addresses.

**OUT OF SCOPE, and not to be re-raised:** the rotation stop (`Z-S157/159/160`) graduated with its
remedies **already applied on the deployed plane**, measured on artifacts that postdate the rows.
APPLIED, not EXERCISED — so it is not a recut item, but it is also not yet a REALIZED grade.

---

## 4. THE JUDGMENT GRADES, AND ONE RULING INSIDE THEM

Both judgment criteria PASS, and one carries a ruling worth restating because it changes a remedy
rather than a grade:

**S10E-AC6 passed ON CONDUCT with the fork RULED: the seal key must be BOUNDED IN CODE.** A runbook
cannot add an expiry to a compiled cache, so a procedural remedy was refused. **The durable fix is to
stop deriving a symmetric seal key from the signing key at all** — that is the shape the recut should
take if it touches this, not a documentation change.

**S10D-AC2 PASS** on one secret id and one expiry literal in the shipped bytes, verified at a digest
the assignee never cited — the grader went to the artifact rather than the report.

---

## 5. TWO STRUCTURAL FINDINGS ROUTED OUT OF THIS PROJECT

Both are this seat's surface. Neither is remediable by any cell of this project.

### 5a. The row gate's per-row L10 check is O(rows × full-census) — a large slug wedges the whole device

Measured by `3.0.0_SA_CVO~Z` from its own commit: the pre-commit hook re-runs the **full L10
precondition once per row**. On a 99-row, 543 KB slug that is 99 task-order censuses over both roots,
and it **held the repository lock for every seat on the device for ~23 minutes**. Ninety-nine
"L10 precondition for" lines in the run log; the lock file frozen throughout.

⭐ **IT HAS NEVER SURFACED BECAUSE IT HAS NEVER BEEN PROVOKED: the estate's seven prior slugs hold 49
rows COMBINED, and this one holds 99.** It will recur on every v3 round, because v3 makes workers the
majority surfacers and graduated sets get larger, not smaller.

⛔ **NO GATE EDIT IS AUTHORIZED BY THIS ANALYSIS** and none is proposed. The gate's per-row check is
correct in what it verifies; the defect is its cost curve. Named, not designed.

*This seat felt it directly — three refusals on an unrelated record during that window — and it is
recorded here rather than as a complaint: a slug commit should win a lock, the refusals were correct,
and each cost only a retry.*

### 5b. Nothing joins a GRADUATED item to a remediation row — findings can silently never be carried

`C-S35` found that **five of round 1's ten graduations had never reached any slug.** The
investigation document and the remediation document each validate independently, and **no predicate
joins them**, so an item can graduate and then simply never appear anywhere downstream. Nothing in
the fabric would have reported it.

⚠ **This is the more consequential of the two.** 5a costs wall-clock and a wedged device; 5b loses
security findings silently, and it did — for a full round, on a project whose findings are about
credentials and access. The five are recovered here only because the CVO went looking.

Both are held at this seat, and neither can be opened as its own project while no CRO is live.
⭐ **Neither is a whole project either** — the sibling analysis records the same over-processing
error against this seat, and the correction applies here too: these are surgical fixes wanting an
exercise, not briefs.

---

## 6. WHY ROUND 2 DOES NOT CLOSE — TWO INDEPENDENT REASONS

Rule 27: **CLOSED needs `COMPLETION_REPORT` + `COMPLETION_GRADES`, every grade `REALIZED`.**

**(i) `FWD-19` has no cell**, so not every outcome can be graded at all.

**(ii) ⛔ THERE IS NO `COMPLETION_REPORT` AT ANY ROUND OF THIS PROJECT.** Measured against HEAD's
tree: `ledger/` holds exactly one file, `L8_PACKET.round2.final.md`. No completion report, no grades,
at round 1 or round 2.

**That is why this analysis carries a coverage read derived from the task orders rather than from the
report — and it is also why THE GRADES CANNOT BE WRITTEN.** The completion report is the artifact
that maps each outcome to the cells that served it *with their evidence*; grading 18 outcomes without
it would mean this seat re-deriving the COO's own record and then grading its own derivation. That is
not a grade, it is a guess wearing one.

⭐ **SO THE BLOCKER ON CLOSING THIS PROJECT IS NOT THE WORK — IT IS A MISSING RECORD**, and it is the
COO's limb. `COMPLETION_REPORT.round2.json` is owed by `2.0.0_SA_COO~Z`; `COMPLETION_GRADES` follows
from this seat once it exists and once `FWD-19` has a round. Named plainly because a project can sit
indefinitely at "all work terminal, all findings dispositioned" and still never close, and this one
is exactly there.

---

## 7. WHAT IS OWED, BY WHOM

| owner | act |
|---|---|
| `2.0.0_SA_COO~Z` | the round-3 recut — ONE issuance: `FWD-19` first (**R3-A**), the armed-set remediation (**R3-B**) |
| `2.0.0_SA_COO~Z` | **`COMPLETION_REPORT.round2.json`** — absent at every round; it gates the close and nothing else can substitute |
| `3.0.0_SA_CVO~Z` | nothing for round 2 — its engagement ended at the slug |
| `1.0.0_SA_CTO~Z` | `COMPLETION_GRADES` once the report exists and `FWD-19` has had a round; both §5 findings held here |
| — | **Nothing is owed by Andrew.** No sovereign call is raised. `FWD-19` is already ratified and calibrated by him; it needs building, not deciding. |

**Push state:** LOCAL at write time. Only `0.0.0_AB_MSTR~Z` pushes a shared branch; stated as
ancestry rather than a tip hash.
