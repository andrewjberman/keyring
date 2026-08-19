# D0–D9 PRD package review pass (10/10) + ontology-lockdown record + adversarial round 1

**archetype:** VALIDATE

**Agent:** `3.0.0_SA_CVO` (base) · **Window:** 2026-08-19 18:34Z → 19:45Z · **Mandate:** Andrew-direct
at this terminal ("write CTO base and say that you are ready and waiting to review PRDs as they are
ready for completeness and coherence of strategy") + the ontology-lockdown ruling ~18:52Z.

## What this session was

A cold start (`/watcher` + `org/XXX.md`), then a single high-density review pass: **ten PRD packages
authored by `1.0.0_SA_CTO` in one evening, reviewed and verdicted in one evening, every finding
absorbed same-turn.** Plus one sovereign ruling recorded + broadcast, and the opening round of an
Andrew-ordered adversarial exchange with CRO.

## 1. Startup

Registered (PID 9260), persistent inbox Monitor armed (task `baxfb7udi`, `TaskOutput` → running),
zero crons per LD-0175. No orphan under my serial; the four live `inbox-watch.sh` processes belonged
to CTO/COO/CRO/CRO~A and were left alone. PATH probe 97/97 resolving **and exercised** (a forwarder
produced its own banner — resolution is not execution). `/estate-pull status` per the base-lane
charter: 16/16 manifest days present since the 08-04 epoch, **producer healthy**, 14 days PENDING.

## 2. Andrew-direct: ontology lock-down (recorded + broadcast, same turn)

Record `@1044c49f2e`, verbatim, with channel + time; broadcast to COO/CTO/MSTR/CRO in four separate
sends (an in-body cc copies nobody). **The estate-report backlog is re-parked on his reason** — no
point adjudicating semantics against an unlocked ontology — which **closed the sovereign call I had
raised at load.**

The operational half: **I retired the elapsed-time backstop.** The old trip (any 08-11+ day PENDING
>24h from emission) had fired eight times over and would now fire *daily* on a hold he deliberately
chose. The gate is a **STATE** (lock-down complete), never a duration. ⛔ The three PRODUCER classes
— ABSENT day / stale RUNNING / FAILED — stay instant-fire, untouched: **a park on the REVIEW step is
not a park on the PRODUCER.**

## 3. The review pass — 10 packages, 8 P0, 0 rejected

| Pkg | Verdict | Commit | The finding that mattered |
|---|---|---|---|
| D2 | 2 P0 | `@cc223ee3b6` | Undeclared 4th verdict class on 47% of rows **disabled CTO's own illegal-derivation gate**; C4's three-way compare needed a leg §4a did not carry |
| D7 | 1 P0 2 P1 | `@11f472a7bb` | The §6 existence check for the one build **could not see its target** (gateway not repo-resident — measured); intake trigger is an agent loop, not a schedule |
| D1 | 2 P0 | `@d476339293` | Rule-24: "one remedy moves all values" false for Residual (**a registry cannot deliver its own complement**); the five views did not sum to total AUA while §3 asserted partition |
| D0 | 2 P0 | `@c7e4d16f6c` | TO-5 pre-committed "16+3" from an INFERRED row; **source-confirmed at `broker.py:474`** the ACK primitive would inherit the conflation it exists to retire, plus a real message-loss window |
| D3 | 0 P0 | `@3e5038ebd3` | Strongest package; carries the overlap invariant D1 asserted away |
| D5 | 0 P0 | `@715fe724d8` | Event-gated queue had no freshness contract; collided with Rule 25 at ~2026-10-29 |
| D6 | 1 P0 1 P1 | `@7ea13aa4ed` | The addendum made the **run FALSE**; and D6 pressured the premise D7's authz deferral rests on |
| D4 | 0 P0 | `@12f90b44d6` | The estate **already held** DIVZ/IDVZ holdings — a contemplated sovereign egress ask may be unnecessary |
| D8 | 0 P0 | `@a9a173e7fa` | Content-store PK was a **display name** in the week display names are being re-legislated |
| D9 | 0 P0 | `@3ae19879fb` | The trade-execution guardrail's DONE bar **named no test that could fail** |

**Five protocol rulings came out of the pass and outlive it:** §6 gains a fourth existence-check form
(on-box SSM read, required for S3-deployed EC2 services); a canonical verdict vocabulary stated
in-artifact; **records name their reader** (my four-instance pattern); run-pointer integrity; and
amended-PRD-gains-a-run-row.

**Three findings changed what gets built:** D1's views now partition by construction; D8's PK is ruled
a stable id **before the table exists**; D6's resolver floor excludes the ticket surface **by
construction**, making D7's deferral premise durable rather than incidental.

**The cross-package half was the part no single-PRD read could reach** — D6-vs-D7's authz premise,
D4/D5's shared unowned CSV source, and the four-instance no-named-reader pattern. That is the whole
argument for one reviewer holding all ten.

## 4. MY OWN ERROR, recorded beside the hits

**D9's should-have-asked (five packages conditioning device-split on an unmeasured sitez envelope,
"nobody owns it") was ALREADY FALSE WHEN I FILED IT.** `MSTR~Z` measured every cell at 184400Z; the
split session allocated against the measurement and Andrew ruled the item map.

The scoring vintage explains it — I scored `@375c874a9e`/`@8d662d5f1f`, both predating 184400Z — **but
a vintage is an explanation, not a defence.** The correct form was *"no PRD names an owner AT THIS
VINTAGE; check whether one has been established since."* **A no-owner claim is an absence claim, and I
did not name the tree I searched** — the exact class I had filed against D4 two packages earlier, and
I committed it while filing it. *Knowing a failure mode by name does not immunise you against writing
it.* Residue that survives: MSTR's ownership was discoverable only by asking until the split decision
recorded it; that line is now recorded, which closes it.

## 5. Adversarial round 1 (Andrew-ordered, CRO)

Fired 194246Z. Attacked all four options including the two I agreed with; **three explicit refusals**
(mutants+negative-controls grade the CHECKER not the DECLARATION — pre-registration is the
discriminating control; O2 tool-keyed cannot express a zero-tool substrate, which is the one instance
Andrew called screaming; "mechanize therefore skip" trades away the unknown-unknown). Moved CRO's
rank-4 to 2 on a **decay-rate** axis they had not argued.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-find` | `--name PRD_AUTHORING_PROTOCOL*`; `union-find` over ontology; `--name *m365*gateway*`; `--name *divz*`; group/shared-mailbox over `infra/aws/ec2` | denominators printed on every call (1/26,821 · 10/86 · 4/26,859 · 9/26,876 · **MEASURED ZERO**/347). The zero and the 4-hits-all-docs are what grounded D7 P0-1 and D4 P1-2 |
| `comp-estate` / `comp-cache` / `comp-transform` | read **in** the packages under review, not re-run | scored the packages' own tool evidence; re-ran nothing that would duplicate their runs |
| `.tools/prd-evidence-check.sh` | positive control + **3 mutants** + a source read | **4 defects found**: blind to the atom_decomp gate (grep=0), multibyte-regex false-WARN (proved with a bare `\xc2` probe), numbered-heading false-WARN (2/153 live PRDs), stale tool list. Routed to AE 0.7 via CTO; **never cited in any verdict** |
| `aws` (operational) | manifest census (16 days, materialised not `--query`-paginated); `silver/holdings/` census (67 objects, size spread) | the 67-object series check upgraded a D4 claim from n=1 to n=67 |
| `to-check.py` | `--all --assignee` (self, and `0.5.0_AE_OpalETL`) | found my 8 base TOs; independently confirmed TO #42's sovereign issuer + 36-day age for D9 P1-2 |
| `safe-commit.sh` | 12 commits under the CVO author line | risk-reflex clean each time (1 file vs 1,817 danger nodes, denominator printed) |

**Gap found:** `prd-evidence-check.sh` cannot see the ground-truth chain it is supposed to lint —
a WARN-mode instrument whose domain predates the rule by 3.5 months. Routed, not fixed (not my lane).

---

# CONTINUATION 19:45Z → 20:20Z — the ontology lock-down assist

**archetype:** VALIDATE

## 6. Adversarial exchange — CLOSED at full convergence (3 rounds)

Round 1: attacked all four options, **three explicit refusals**. Round 2: CRO conceded all three; I
conceded their full-matrix beat my substrate-keying, then attacked their counters. Round 3: five more,
all conceded. **The decisive catch — their chase-audit policed only ONE LEG of a two-leg comparison**:
it stopped editing a *declaration* to match a failing resolver but left open editing the *resolver* to
match the declaration — *the identical rationalization, and the easier one to commit innocently,
because "I fixed the resolver" reads as engineering.*

**I also attacked my own round-1 fix:** I had killed a frozen tool-count denominator; the fix hardened
one axis and left the **substrate** axis unguarded. My own instrument, same defect, one axis over.

**Yield beyond the ranking:** my self-caveat — that catches landing where my context is deepest is a
*selection effect*, predicting blindness where context is thin — was taken into T11 as the
**BLINDNESS MAP**: multi-validator coverage composes as the union of deltas, uncovered region stated
as residual.

## 7. §4 exit-bar census — 3 passes

**Pass 1 (deprecated axis, recalled terms):** 89 files, 6 terms, **96 raw occurrences → 3 findings.**
Two outside the tranche's target list. Sharpest: `L0B_CHANGE_TYPE_VOCABULARY.md` **defines two live
change-type terms by the behavior of `comp-surface-check`, retired 08-06** — a definitional anchor to
a nonexistent instrument. Also: `10_census/` had **no in-tree vintage**, and the 08-19 fold gave a
07-31 seed a same-day git date — *a staleness signal that now read FRESH*, which **invalidated the
confident half of my own census** (80 occurrences classified on a date I knew from memory, not from
the artifact). CRO landed the README between passes.

**Pass 2 (derived list — the fix applied to my own instrument):** term list derived from the registry
changelog. **136 occurrences, ZERO new defects** — all AWS physical names, retirement records, or a
different live sense. **The yield was the falsification:** every retired term has a live homonym;
`territory` alone would fire ~30 false positives against a load-bearing concept. **Killed the naive
term-lint before it was built** — reshaped to a diff-time advisory on added lines only.

**Conflicting-half pass 1:** denominator by *parsing* — 68 terms, all 68 with file-citing authority,
6 commit-pinned; **63 ratified / 3 deprecated / 2 contested.** **The bar was UNFALSIFIABLE** (the
canon self-declares five cells in the two states the bar forbids) → rewritten to *no UNDECLARED*
conflict, with the five cells listed in-bar. My addition: **a disposition path scoped to LESS than the
actual defect is the same failure as no path — it just looks complete.**

## 8. My two cells — one worked, one corrected

**`Unreconciled_Aua`:** claiming it is what surfaced the defect. **One field name, two computations,
both served** — `INF_D_02` accumulates (`+=` AUA of accounts with no billing record), `INF_D_04`
subtracts (`total_aua − holdings_total`). Read both served keys live: `book.json` ships
`unreconciled_aua: 0.0` **beside `unreconciled_account_count: 4`**; `header_metrics.json` ships
`-0.0` (the negative zero is the subtraction's tell). CTO's 08-12 finding **re-scoped** from a field
rename to a three-bucket vocabulary unification riding the INF bind.

⚠ **`Lifecycle_Value` — I OVER-CLAIMED IT.** Its `resolution_owner` names `3.0.0_SA_CVO~Z`, not base
me. **Second ownership over-claim of the night** (the sitez envelope was the first) — both in areas
where my context was thin, both with the correct form sitting in a record I had not read. Banked as a
T11 specimen: **"who owns X" claims cost more scrutiny precisely because they read as cheap to make.**
Positive result: ran the cell's own `do_not` test — the C3 walk's subjects are contract records,
matching `lifecycle_class`'s declared grain, so **the conflation is NOT being ratified by usage. Open,
not decaying** — a distinction now in the bar.

**Near-miss recorded:** I nearly took the cell's counterexample as settling the contest — it is one
side's argument against a live opposing MSTR ruling, both carrying an Andrew verbatim. Taking my own
side as settled, in a cell I had just claimed, would have been the self-grading error I attacked in O1.

## 9. Scope — asked rather than assumed

T4/T5 are canon edits outside my chartered commit scope. I had a plausible grant and **asked anyway**,
on separation-of-duties grounds: *the seat that audits scope deciding its own scope is the
self-grading pattern.* CRO ruled **option (c)** — CRO executes T2–T5, **my role converts to exit-bar
certification of their edits.**

## 10. Prereg re-read (owed, not a re-score)

A2 closed my C4 P0-2 verbatim. **New finding one convention over:** A3's harness basis rule said the
residual *"IS the accrual component alone"* — **defining the residual to be accrual instead of testing
it against accrual**, making C5's classifier collapse to zero by construction. *A permanent
classification class whose test cannot fail is the smoothing, wearing a mechanism's name.* **The sound
form was already in their own evidence** (BD publishes accrual separately; the qt1 identity holds on
120,215 rows) — one-clause fix, adopted as A5: residual compared **against** the published field,
non-matching residuals stay in the census.

## Compiler Tools (continuation)

| tool | invocation | result |
|---|---|---|
| `comp-find` | `unreconciled_aua` (62/26,920, banded); `lifecycle_class` (276/26,920) | located the two-producer collision and the C3 walk; bands separated source from doc |
| `python` (parsing, not reading) | registry changelog → naming-act term list; term/authority/status triples | **derived** denominators for passes 2 and 3 — the house method CRO ratified |
| `aws s3 cp` (operational) | both served keys read live | the `0.0` beside `count: 4` trap, and the `-0.0` subtraction tell |
| `grep`/`sed` (scoped reads) | both computations, walk subject grain, prereg addenda | grain match that cleared the `do_not` |

**Gap:** none new. Pass 2's finding is that a *proposed* instrument would have been defective.

## Blockers

NONE self-blocking; every remaining item is event-anchored with a named owner. **63 prose-vs-authority
comparisons** → O1 seam (CRO building tonight). **Certification of CRO's T2–T5** → when they land.
**`Unreconciled_Aua` first act** (the D_02 deployed-bytes read) → rides the INF bind. **`Lifecycle_Value`**
→ not mine; ~Z's fence, routed via MSTR per LD-0325 confinement. Estate-pull stays parked by sovereign
word. Prereg is closed pre-probe and does not move before Thursday absent a new Andrew word.

— 3.0.0_SA_CVO
