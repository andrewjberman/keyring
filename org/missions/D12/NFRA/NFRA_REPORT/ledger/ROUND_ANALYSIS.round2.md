# NFRA_REPORT — ROUND 2 ANALYSIS (L10 answered)

**archetype:** VALIDATE

| | |
|---|---|
| **Written by** | `1.0.0_SA_CTO~Z` |
| **Written** | 2026-09-10 ~08:5xZ |
| **Answers** | the round-2 slug, `surprise-channel/remediations/REMEDIATION_v1.Z.md` @`4fe64b8cac`, cut by `3.0.0_SA_CVO~Z` (msg 20856) |
| **Reads** | `ledger/COMPLETION_REPORT.round2.json` (`2.0.0_SA_COO~ZZ`), the PRD at v0.7, the channel's 24 items |
| **Verdict** | **ROUND 2 DOES NOT CLOSE. It RECUTS.** One outcome cannot grade REALIZED. |
| **Recut owner** | `2.0.0_SA_COO~ZZ`, one issuance |

> **This artifact is placed in the project's own `ledger/`, not in this seat's `deliverables/`.** Round 1's
> analysis went to `org/tier1_exec/1.0.0_SA_CTO/deliverables/` instead, which is half of what row
> `NFRA_REPORT-Z-S9` records. That limb is discharged here; the other half is stated in §5.

---

## 1. COVERAGE READ, PER OUTCOME

**Denominator: 12 FWD outcomes in the PRD header at v0.7.** Source: `COMPLETION_REPORT.round2.json`
`outcomes[]`, cross-read against the PRD. Cells are cumulative across rounds 1–2 by the COO's stated
convention, which is correct — an outcome served only in round 1 would otherwise read UNCOVERED and
that would be false.

| FWD | DONE-WHEN state | cells | COVERED | grade |
|---|---|---|---|---|
| FWD-1 | EXERCISED | RP-s-2, 3, 4, 16, 17 | yes | REALIZED |
| FWD-2 | APPLIED | RP-s-1, 14 | yes | REALIZED |
| FWD-3 | EXERCISED | RP-s-2, 15 | yes | REALIZED |
| **FWD-4** | EXERCISED | RP-s-1, 13 | yes | ⛔ **NOT REALIZED** |
| FWD-5 | EXERCISED | RP-s-6 | yes | REALIZED |
| FWD-6 | EXERCISED | RP-s-7 | yes | REALIZED |
| FWD-7 | EXERCISED | RP-s-8, 18 | yes | REALIZED |
| FWD-8 | EXERCISED | RP-s-9 | yes | REALIZED (SEGMENT limb); BOX-GRAIN limb OUT OF SCOPE |
| FWD-9 | APPLIED | RP-s-5 | yes | REALIZED |
| FWD-10 | APPLIED | RP-s-10 | yes | REALIZED |
| FWD-11 | EXERCISED | RP-s-11 | yes | REALIZED |
| FWD-12 | EXERCISED | RP-s-12, 19 | yes | REALIZED |

**UNCOVERED partition: EMPTY — 0 of 12.** Every outcome has at least one cell serving it, so **no PRD
addendum is owed and none is written.** The two routes rule 27 gives this seat at L10 are a PRD addendum
(for an outcome no cell served) or a round-N analysis; the UNCOVERED set being empty selects the second.

⛔ **COVERED IS NOT A GRADE, AND THE TWO MUST NOT BE READ AS ONE.** `COVERED` says a cell served the
outcome. The grade says the served artifact is right at the PRD's current version. FWD-4 is the case
where they diverge, and the COO's own note says so explicitly rather than letting COVERED carry the
weight. That distinction is the reason this round recuts instead of closing.

---

## 2. THE ONE OUTCOME THAT CANNOT GRADE REALIZED

### FWD-4 — NOT REALIZED. Row `NFRA_REPORT-Z-S10`, the only row still ARMED in the slug.

**DONE-WHEN:** *"a real failure has been read and attributed by a person to one part and one owner."*

**The defect:** `RP-s-13`'s merged `ATTRIBUTION.md` renders `opal-gateway` and `opal-globgrph` as
**UNGROUPED**, and its line 30 still reads *"third member (`Gateway`, `Graph`, or both) | OPEN CALL AT
ANDREW."* PRD **v0.7** ratifies a **FOUR-member** axis — Dashboard | Website | Gateway | Graph — naming
those two surfaces as the referents of the two new members, and records the call **RULED AND CLOSED**.
The artifact and its governing spec disagree, measured on both sides by `2.0.0_SA_COO~ZZ` and again by
`3.0.0_SA_CVO~Z`.

An attribution surface that renders the two newest axis members as UNGROUPED cannot satisfy *"attributed
to one part and one owner"* for a failure in either of them.

⭐ **THE CELL IS NOT DEFICIENT AND IS NOT GRADED AS ONE.** Both the COO and the CVO asked for this
explicitly and this seat agrees on the evidence: `RP-s-13` was cut, built and merged **inside the window
in which FWD-4 was under active Andrew adjudication**, and was overtaken **twice** — v0.6's si2 amendment
overtook its issued BOUNDS while the worker was still building (caught by that worker re-grounding on the
live PRD rather than on its own order, row `W2-S5`), and v0.7's axis ruling overtook the finished
deliverable. **The worker was right at every vintage it read.** The grade attaches to the ARTIFACT'S
CURRENCY, not to the cell's execution, and the remedy is a round-3 cell rather than a finding against
`0.9.0_WK_NFRA_REPORT~1`.

**Z-S10's disarm is fixed to the recut** and it is correctly still ARMED until then.

### FWD-8 — REALIZED on the served limb; the other limb is OUT OF SCOPE and stays there.

The BOX-GRAIN limb is blocked on resource-level Cost Explorer being **opt-in DISABLED at the payer
account** — Andrew's billing decision, not this project's work. Row `Z-S4`, disarmed INERT. The SEGMENT
limb is served and graded REALIZED. **This is not carried into the recut** and must not be re-raised as
an open item: it is out of scope by a prior round-N analysis and nothing has changed it.

---

## 3. WHAT THE RECUT MUST CARRY — `2.0.0_SA_COO~ZZ`, ONE ISSUANCE

Two cells. Both derive from rows the slug names; neither is new scope.

**R3-1 — FWD-4's attribution surface, from `Z-S10`.** Bring `ATTRIBUTION.md` to PRD v0.7: the axis has
four members, `opal-gateway` and `opal-globgrph` are the referents of the two new ones and must not
render UNGROUPED, and line 30's "OPEN CALL AT ANDREW" is stale prose that v0.7 closed. ⚠ **The
acceptance criterion must score the RENDERED OUTPUT, not the source** — a criterion that greps the
composer for a four-member list would pass while the rendered artifact still shows UNGROUPED, which is
the exact shape of this round's own measured criterion weakness (§4).

**R3-2 — deliverable folder derived from `<issued_to>`, from `Z-S8`.** All seven round-2 orders name ONE
worker's folder, so the tree cannot say who authored what. Round 3's cut derives the folder from
`<issued_to>`. This is an L6 mechanic and is cheap at the cut; it is expensive to retrofit.

**CARRIED, NOT CUT — the round-3 worker-face constraint** already recorded in `project.json` `blocking`
@`cf3e8fa7f6`: any census or absence claim is run from the MAIN checkout, never from the worker's own
worktree, and a comp-find zero obtained inside a worktree is not evidence of absence. Ruled at msg 20822,
carried by the COO to a durable carrier after its first home (a session-only cron prompt) would have lost
it. See `org/modules/graph/INSTRUMENT_LIMITS.md` LIMIT 4 / 4a.

**NOT IN THE RECUT AND NOT THIS PROJECT'S WORK:** the two structural findings in §4. They are named here
so the recut does not absorb them, and routed in §5.

---

## 4. THE ROUND'S OWN CRAFT — one measured weakness, accepted

`2.0.0_SA_COO~ZZ` measured against itself that **18 of 24 round-2 criteria (75%) are `grep -c` word or
line counts**, and that the recut which fixed two round-1 criterion defects carried this one forward *at
a higher rate than the round it was correcting*. Recorded rather than adjudicated — criterion design is
the COO's L5/L6 craft, not this seat's to rule.

It is repeated here for one reason: **it is the direct cause of R3-1's warning.** A word-presence grep is
exactly the instrument that would score FWD-4's remedy as done while the rendered surface is still wrong.
The self-measurement and the recut risk are the same fact.

Separately accepted from the CVO's `C-S8`: **neither judgment criterion was named in the L8 packet**,
which reported "19 of 19 with a valid proof" and reserved nothing. A proof tally and a gradeable set are
two different quantities. Both judgment criteria were subsequently graded at `C-S8` and **both PASS**, so
nothing shipped wrong; the packet's shape is corrected for round 3 by the COO's own carried fact.

---

## 5. TWO STRUCTURAL FINDINGS ROUTED OUT OF THIS PROJECT

Both are this seat's surface, both verified here on this seat's own instrument rather than on the slug's
word, and **neither is remediable by any cell of NFRA_REPORT.**

### 5a. The slug CANNOT structurally carry a worker-surfaced row — `surprise-row-gate.py`

`_coordinate_violations` refuses any NEW row carrying a `W<n>` coordinate when the committer is not that
worker (the allocator discipline). Protocol §5 requires a remediation row's `id` to EQUAL the graduated
investigation row's id. **A slug by construction only ever CARRIES ids minted elsewhere — every id in it
was minted by someone else, by definition — and the gate cannot tell MINTING an id from CARRYING one.**

Graded as an allocation, every worker-surfaced graduation is refused. **So the CVO cannot cut a slug for
any worker-surfaced row.** 7 of this round's 13 graduated rows carry `W1`/`W2`, so the slug required an
audited `# surprise-row-override:`.

**Why it has never surfaced, measured by the CVO across the estate's 7 existing remediation documents
(NFRA_CLDGRPH v1/v2/v3, NFRA_COMPEFFICACY v1, NFRA_OUTSET v1, NFRA_OPSEC202609 v1.Z, ETFS_GUARDRAIL v1):
49 rows, ZERO carrying a W coordinate.** NFRA_REPORT is the first round whose graduated set is majority
worker rows, which is the only reason there is an instance now. **This will recur on every v3 round from
here**, because v3 makes workers the L7 executors and therefore the majority surfacers.

⛔ **NO GATE EDIT IS AUTHORIZED BY THIS ANALYSIS.** The override was correct — the alternative was
dropping 7 of 13 rows from the round's only forward carrier. The finding is NAMED, NOT DESIGNED, and the
CVO explicitly declined to treat this seat's earlier "do not edit the gate" ruling as cover for opening
one, which was the right call.

### 5b. The disposition resolver collapses two clocks — `surprise-row-gate.py::_resolve_latest`

**VERIFIED BY THIS SEAT AT SOURCE, not taken on the slug's word.** The application loop is:

```
for _p, rows in investigation_files:          # investigation AND adjudication docs, as ONE union
    for r in rows:
        for target in (r.get("adjudicates") or []):
            ...
            latest[target] = r.get("disposition")   # no test of the DOCUMENT, no test of the SEAT
```

So **any** row carrying `adjudicates` stamps its own `disposition` onto its target — including an
investigation-lane row filed by a peer seat or a worker. A DISARM row therefore sets a REMEDIATION-track
verdict, collapsing the two clocks protocol §5 says must never collapse. **The L10 precondition enforces
that a disposition EXISTS and never who set it.**

**MEASURED INDEPENDENTLY BY THIS SEAT** (classifying each item by who set its terminal disposition):

| population | CVO adjudication row | peer row, investigation lane | self-set, never adjudicated |
|---|---|---|---|
| NFRA_REPORT, reconstructed pre-`C-S10`/`C-S11` | 8 | 8 | 8 |
| NFRA_REPORT, now | **24** | 0 | 0 |
| ~~NFRA_OPSEC202609, as it stands~~ ⛔ **RETRACTED — see the box below** | ~~82~~ | ~~18~~ | ~~67~~ |

The 8/8/8 reproduces the CVO's account exactly. **The CVO both found and repaired this inside its own
round** — `C-S10`/`C-S11` swept all 24 to CVO-set, which is why NFRA_REPORT's L10 precondition is sound.

> ⛔ **RETRACTED 2026-09-10 ~09:1xZ — THIS SECTION ORIGINALLY "CORRECTED" A FIGURE THAT WAS RIGHT, AND
> THE RETRACTION IS AGAINST THIS SEAT.**
>
> As committed @`2b44f4a62b` this section read: *"The self-set arm is 67, not 6 — `82 + 18 + 6 = 106`,
> which does not sum to that project's own 167-item denominator... 67 of 167 items (40%) have never been
> adjudicated by anyone,"* and concluded *"85 of its 167 items carry no CVO verdict."* **Both figures are
> wrong and the slug's `6` was correct.**
>
> **THE ARITHMETIC OBJECTION USED THE WRONG DENOMINATOR.** The slug's partition is over the **TERMINAL**
> set, not over all items. At its vintage: 167 items, 61 UNDISPOSITIONED, so terminal = **106** — and
> `82 + 18 + 6 = 106` **exactly**. It summed perfectly against its own denominator; this seat checked it
> against 167, which is terminal *plus* the undispositioned backlog.
>
> **THE 67 CONFLATED TWO POPULATIONS.** It merged items with no verdict *yet* — which is the definition
> of UNDISPOSITIONED, the L9 backlog, not a defect — with items terminally self-set. **THE 18 WAS WRONG
> TOO, IN THE OTHER DIRECTION:** those are CVO-authored rows that live in the *investigation* file,
> exactly where spine §4 puts round 1's CVO rows until the adjudications folder lands. They are real
> adjudications. This seat's classifier keyed on the DOCUMENT, not the AUTHOR, and so read twenty of the
> CVO's own adjudications as peer stamps.
>
> **RE-MEASURED, keyed on the author of the setting row (denominator 168 at ~09:0xZ):**
>
> | | |
> |---|---|
> | CVO-authored row, adjudications doc | 103 |
> | CVO-authored row **in the investigation file** (spine §4 — legitimate) | 18 |
> | `Z-S19` + `Z-S20` themselves — **CVO-authored L9 rows**, items only by spine §4 placement | 2 |
> | UNDISPOSITIONED — no verdict *yet*, the L9 backlog | 41 |
> | DISARM RECORDS, terminal self-set (separate known class) | 3 |
> | non-CVO row (`Z-S168`, the withdrawal below) | 1 |
> | **TERMINAL SELF-SET RESIDUE — the actual defect class** | **0** |
>
> CVO-verdict coverage is **123 of 168**. **The residue is ZERO.** Not 85.
>
> ⛔ **CORRECTED AGAIN ~09:1xZ, AND THIS SECOND PASS REPEATED THE ERROR IT WAS RETRACTING.** As first
> written the retraction said *"the genuine defect class is 5, three of which are disarm records"* —
> implying two real defects. `2.0.0_SA_COO~Z` (msg 20864) named those two exactly: **`Z-S19` and
> `Z-S20`, the CVO's OWN round-1 L9 adjudication rows** — the very rows that resolve the 18 this box
> already credits as legitimate. They self-carry a disposition because **the adjudicator dispositioned
> its own adjudication row, which is L9's owner acting in its own limb.** The gate's own docstring says
> a CVO row's id is *not an item*; they count here only because spine §4 places round 1's CVO rows in
> the investigation file until the adjudications folder lands. Verified at this seat by enumerating the
> bucket and reading `surfaced_by` on each of the five.
>
> **So the same grain error — keying on the DOCUMENT or on the row's own id rather than on the AUTHOR —
> survived into the correction written to fix it.** Three passes, each inflating in the same direction:
> 85, then 5, then 0. `2.0.0_SA_COO~Z` disclosed that this correction FAVOURS its own project before
> making it, which is why it was checked exactly rather than argued.
>
> ⭐ **THE DURABLE READING RULE** (`2.0.0_SA_COO~Z`, offered without a remedy and adopted here): **key on
> `surfaced_by`, never on the document, and treat a CVO row's own id as a non-item wherever it sits.**
> That is a reading rule, not a code change — no gate edit is implied and none is proposed.
>
> ⭐ **THE MECHANISM STANDS AND `2.0.0_SA_COO~Z` FOUND THE REAL INSTANCE** (msg 20860), measuring its own
> project rather than accepting the routed figure: `NFRA_OPSEC202609-Z-S115`, a **self-conferred
> GRADUATED** set by that seat in its own row with nothing adjudicating it. Graduation is L9's act.
> Withdrawn at `Z-S168` @`17ea309ebe` to `UNDER_INVESTIGATION` rather than re-graded, because choosing
> any terminal value would repeat the original error in the opposite direction. **The L10 distance ROSE
> by two** — the correct direction for a count that had been flattered.
>
> **WHAT THIS SEAT GOT WRONG, NAMED PLAINLY:** a real mechanism, verified at source, carried an incidence
> figure that was never measured at the right grain — and the error ran in the direction that made the
> finding look larger, published as a headline correction against a peer whose number was correct. The
> mechanism needed no inflation to be worth routing; §5b's structural claim is unaffected and stands.

**Consequence for NFRA_OPSEC202609, stated as a fact and not as a dispatch:** its L10 precondition
counts whether a disposition EXISTS, never who set it, so a self-conferred terminal value is invisible
to it. **The measured exposure on that project is ZERO** — the one real instance (`Z-S115`) was found
and withdrawn by `2.0.0_SA_COO~Z` itself; the remaining terminal self-set rows are 3 disarm records (a
separate known class) and 2 CVO-authored L9 adjudication rows that are items only by spine §4 placement.
Routed to `3.0.0_SA_CVO~Z` and `2.0.0_SA_COO~Z` as information; NOT adjudicated here, and NOT this
project's to fix.

⚠ **THIS SEAT IS INSIDE THE FINDING, NOT OUTSIDE IT.** Row `NFRA_REPORT-Z-S12` — this seat's own
disposition of `W1-S5` — used exactly this mechanism: an investigation-lane row with `adjudicates`,
setting a disposition. It was legitimate (this seat was the named `disarm_owner`, and the CVO ratified it
at `C-S9`), but the mechanism is identical and the resolver could not have told the difference. Stated so
this analysis is not read as one seat's finding against others.

---

## 6. WHY ROUND 2 DOES NOT CLOSE

Rule 27: **CLOSED needs two artifacts — `COMPLETION_REPORT` + `COMPLETION_GRADES`, every grade
`REALIZED`.**

- `COMPLETION_REPORT.round2.json` — **EXISTS** @`9c54d5f523`.
- `COMPLETION_GRADES.round2.json` — **NOT WRITTEN, AND NOT YET OWED.** FWD-4 cannot grade REALIZED
  (§2), so the "every grade REALIZED" condition cannot be met by round 2. A grades artifact recording a
  non-REALIZED grade would assert a close that is not available.

**Round 2 is therefore `L10 answered` and RECUTS.** `COMPLETION_GRADES` becomes owed at the round whose
grades are all REALIZED, and this seat writes it then.

This discharges the ROUND_ANALYSIS limb of row `NFRA_REPORT-Z-S9`. **Z-S9's other limb — that
`COMPLETION_GRADES` exists at no round — is answered but not satisfied:** it is correctly absent, and
naming why is the answer. Round 1's analysis living in this seat's `deliverables/` rather than the
project `ledger/` stands as a real defect of round 1 and is not back-filled; this artifact establishes
the correct home going forward.

---

## 7. WHAT IS OWED, BY WHOM

| owner | act |
|---|---|
| `2.0.0_SA_COO~ZZ` | the round-3 recut — ONE issuance covering **R3-1** and **R3-2** (§3), with the criterion warning in R3-1 honoured |
| `3.0.0_SA_CVO~Z` | nothing for round 2 — its engagement ended at the slug per spine §8 |
| `1.0.0_SA_CTO~Z` | `COMPLETION_GRADES` at the round that closes; the two §5 findings held at this seat, both unownable until a CRO exists to open the comp-tool L1 |
| — | **Nothing is owed by Andrew.** No sovereign call is raised by this analysis. |

**Push state:** LOCAL at write time. Only `0.0.0_AB_MSTR~Z` pushes a shared branch; stated as ancestry
rather than a tip hash, since origin has moved repeatedly this session.
