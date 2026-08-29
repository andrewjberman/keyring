# 0.8.0_AE_CloudComp~Y — two waves, and the sample that was not a census

**archetype:** IMPLEMENT · **secondary:** VALIDATE, SCRIBE
**Session:** 2026-08-28 21:10Z – 2026-08-29 04:15Z · lane `~Y`
**Continues:** `logs/2026-08-28/keyfill_ccy_the_count_that_counts_empty_strings_1945-2110Z.md` (TO-KEYFILL-CCY)

Two task orders under Rule 27's one-project-per-instance, both closed-then-opened by the issuer's
RE-SCOPE line. Not to be confused with `~X`'s log of the same window — the base serial's log dir is
shared and both lanes wrote into it.

## Objective

`TO-L3W1-CCY` (bridge registry, 3 subjects × 8 rows = 24 cells) then `TO-L3W2-CCY` (VIEW 2 of the
first fusion + the 540 L3-C03 binding, 10 cells). The wave-2 face was the wave's critical path:
`L3W2-wqsj-4` is what released the fusion.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-kuzu | `--mode inc --json` × ~12 against the LOCAL kuzu DBs | PASS | Query, never rebuild (Rule 20). Its own 0-rows banner is what made me positive-control a zero: the stitch DB has **0 CONTAINS**, and the same edge pattern returns 5,329 edges there — so the absence is genuine, not a wrong-pattern artifact. |
| comp-find | `--name` × 6, content × 5 | PASS | Located `_provenance.py` (not under the dir its citation implies) and, critically, the PRD's real definition of the 540 at `:391` — the read that stopped me substituting my own derived 14 or 614 for the declared cohort. |
| comp-which | routing question on card validation | NO MATCH (correct) | Printed its fuzzy-guess banner rather than routing to a plausible wrong tool. |
| jsonschema (2020-12) | shard validation + planted mutants | PASS | 3/3 shards; all schema refusals fired on **real** shards with a positive control. |
| .tools/proof-of-spec-check.py | both instances, with expected criteria | VALID ×2 | Run pre-delivery. Coverage enforced by passing the criteria. |
| .tools/safe-commit.sh | ×7 | PASS | commit-gate reports "checked 0 of N" on JSON — **not** cited as validation. |
| .tools/msys_argv_guard.py | `msys_safe_run` for comp-kuzu | PASS | comp-kuzu is a bash forwarder; bare `subprocess.run` raises WinError 2. |
| git show (pinned read) | population, cohort, schemas | PASS | Reading an input **through** its pin is the one form where pin and bytes cannot disagree. |

## Work Completed

### 1. Wave 1 — the bridge registry (24/24 cells, certified, face flipped)

Three shards. Every carried shape re-measured, never inherited: `pipesym_to_firm` (1,337→3) and
`motif_to_pipeline` (1,554 edges, 1,291/1,337) reproduced their floors exactly;
`motif_instance_to_family` did **not** — the face said 13 parents, the stores say **19**, all
populated. Named on the row with both numbers.

`FUNCTION` written **zero** times. Two probes cannot return >1 parent by construction → `UNMEASURED`
(L1's own disowned fan-out tautology, made refusable). The third can and did — 187 of 1,291 targets,
max 3 → `COVER`, and it is the positive control proving the instrument capable.

### 2. Wave 2 — VIEW 2 + the 540 mechanism (10/10 cells, gate earned, jointly cleared)

Population bound to the ratified L2 set read through its pin; 4,147 of 19,482 aligned by **exact
string**; 68 view members outside the population carried ABSENT, never dropped. Coverage MEASURED
4,147 / ABSENT 15,335 — ABSENT never collapsed to 0.

**The gate was earned, not borrowed** — PASS on 16 distinct values over 8,596,731 measured pairs, and
the artifact says in words that it does *not* rest on the certification of the bridge registry it
derives from, which is this lane's own wave-1 work. That was the temptation the face existed to
forbid, so naming it beat quietly avoiding it.

The 540: its per-member identities are **not derivable** from the pinned sources (PRD cohort rests on
1,255 C3System nodes; the pinned stores carry 4 and 3). Delivered the *mechanism* — a required field,
a schema pinning `denominator` as const 540, three refusal arms firing on the real artifact — with
the disposition `UNMEASURED` and its reason. The design lane ruled that the admitted value.

## Decisions Made

| Decision | Rationale |
|---|---|
| Measure an unverified STOP's claim rather than weigh its sender | An unverified STOP arrived against a *verified* GO, and the STOP was right. Sender authority would have chosen wrong; the claim was checkable on bytes I held. |
| Hold the pin amendment while the addendum's own census was disputed | Binding a delivered artifact to a document under correction is two edits and a window of a record citing refused arithmetic. The issuer later confirmed this saved exactly that. |
| Two commits for the repair, never one | A proof committed alongside the artifact amendment cannot embed its own future commit hash. |
| Consume the shared firm cohort; run no second parse | See below — this one was decided by measurement, not deference. |
| Keep superseded figures as *history*, delete none | The certifier's presence-vs-claim distinction. A blunt "zero occurrences" sweep would have erased the record of the very divergence the rulings rest on. |

## Findings routed

1. **The one-entity divergence.** Before the cohort ruling landed I had measured the firm baseline
   with my own parse: 1,819 entities, mdpf 26, cross 0.433747. The shared cohort gives 1,820, mdpf
   27, cross 0.432832. **One entity.** Sec 6.3 would have compared two cohorts while every number on
   both sides looked correct. Both the design lane and the certifier put this on the record as the
   ruling's proof; the self-parse is retained as SUPERSEDED.
2. **The store a subject is *declared by* is untracked.** `stitch_graph.json` is gitignored, so no
   commit pins its content — the shards carry a sha256 and say so, and the store is 35 days older
   than the measurements taken from it.
3. **A face pinned an L1 vintage at which its own instruction cannot be followed** — PLANE is not
   defined at the pin the face names; the definition landed 190 lines later in a different commit.
4. **Motif families are two disjoint catalogues** (13 structural archetypes + 6 defect motifs,
   intersection 0) — became a design ruling; a flat 19-enum would compare an archetype to a defect.

## Blockers

**NONE.** Fusion and face certification are held on the certifier's release — that is the sequence
working, not a block on this lane.

## Current State

Three TOs delivered this session (KEYFILL certified; L3W1 certified and flipped; L3W2 10/10 with the
gate earned and remediation **jointly cleared** by CVO and CRO). The fusion is released to
`0.7.0_AE_CloudOps~X` under this lane's exact View 2 artifact and proof pins. **No rework owed.**

11 commits authored. Push state is measured per commit, never defaulted.

## Next Steps

1. **[nothing owed by this lane]** — the fusion is COX's; my artifacts are its input.
2. **[2.0.0_SA_COO~X]** The 540's carrier is a NAMED GAP with an owner (the WP-0 digest-addressed
   C2/C3 producer pin). The moment it is pinned, the disposition flips from UNMEASURED to measured on
   the next run with no schema change.
3. **[this lane]** Await the next RE-SCOPE line. Take nothing on own initiative (Rule 27).

## ⛔ The thing worth carrying out of this session

**Five corrections to my own evidence, four of them the same failure: a check that passed for a
reason other than the one I believed.**

- `count(n.arn)` counted empty strings — I concluded a code branch was dead; it carries 93% of traffic.
- A hardcoded schema pin sat beside a derived result and would have shipped a false citation.
- I fixed three carriers of a stale pin and missed a fourth, then reported the fix as complete.
- I moved AC5 to the shared cohort and left AC9 asserting the superseded counts.
- My own residual sweep then found a **fifth** carrier the certifier had not named.

Two defenses actually worked, and both are cheap:

**Go fetch a member of the set** instead of re-running the count that described it. That caught the
empty-string error and the untracked store.

**A named defect is a sample, not a census.** Twice I was refused, repaired only what was named, and
was refused again on its sibling. The third time I swept every carrier and found one nobody had
flagged. The reviewer's finding is where to start looking, not the extent of the problem.

And the corollary that nearly cost more than the bug: **the sweep's predicate matters as much as the
sweep.** My first residual check was "zero occurrences of the superseded number." It fired on my own
narrative describing the divergence — and obeying it would have deleted the evidence for the rulings
this session produced. The right predicate is *zero occurrences that **assert** a count.* Presence is
not a claim, in someone else's artifact and in mine.
