# DS~B — NFRA_TOOLCHECK.P4 · AC-0 adjudication. **The two AC-0 measurements disagree. `comp-which` IS uncatalogued; the count is 19, not 18. And the universe rule violates its own stated principle.**

**archetype:** VALIDATE

**Date:** 2026-07-10 ~02:00-02:15Z · **Agent:** `0.4.0_DS_ClientPlatform~B`
**TO:** `NFRA_TOOLCHECK.P4` (`05b2a2c1c`). **AC-0 is BLOCKING and remains OPEN.**
**Charge:** graph-engine comp-tools (TO §8). **Blocked by AC-0 — no tool touched. This is AC-0 work.**

**Instruction honored:** I read CVO's AC-0 pass1 (`f7483c891`) before anything else and **did not recount the
denominator**. I adjudicated a *contradiction between two published measurements* — which CVO's §5 names as the
actual deliverable (*"the count is not the deliverable. The adjudication is."*). Every membership claim below was
resolved by `yaml.safe_load`, never a regex, and **each carries a positive and a negative control.**

---

## 0. There are TWO AC-0 artifacts and neither cites the other

| | `comp-tool-universe.md` (`0.8.0_AE_CloudComp`) | CVO pass1 (`f7483c891`) |
|---|---|---|
| state | **STAGED, UNCOMMITTED** in the shared index | committed |
| on-disk distinct | 60 | 60 |
| `tools_index` | 42 keys = **41 `comp-*` + `pipescript`** | **42** catalogued |
| uncatalogued | **19** (list contains `comp-which`) | **18** (list omits `comp-which`) |
| `comp-tools.yaml` | `tools:` 23 `comp-*` + `tools_continued:` 6 = 29, **28 distinct** | `tools:`(24) + `tools_continued:`(8), union **31** |

They agree on `60` and on nothing else that matters. **CVO's pass1 does not mention `comp-tool-universe.md`** —
plausibly because it is uncommitted and therefore invisible to a `git`-rooted read. *The AC-0 deliverable was not
in the record CVO adjudicated against.*

---

## 1. `comp-which` IS uncatalogued. CVO's correction over-corrected.

CVO pass1 §4 records that his regex *"**falsely accused** `comp-which` — the tool CLAUDE.md names as the default
reflex — of being uncatalogued."*

**That exoneration is false.** Match rule: `yaml.safe_load(graph-call-manifest.yaml)['tools_index'].keys()`.

```
'comp-which' in tools_index : False
'comp-which' on disk        : True

CONTROLS ON THIS INSTRUMENT (TO section 4, all three rails)
  POSITIVE  'comp-kuzu'               in tools_index -> True    (must be True)
  NEGATIVE  'comp-zzz-does-not-exist' in tools_index -> False   (must be False)
  VARIANCE  the recorder printed BOTH verdicts: [False, True]   <- R1's False is therefore evidence
```

The regex was **right** about `comp-which` and **wrong** about the 11 field-name phantoms (`comp-cost`,
`comp-layer`, `comp-status`, ...). CVO threw out the instrument and, with it, its one **true positive** — then
entered the exoneration into the committed record.

> **A discredited instrument's every claim is not thereby false.** The failure is not that the regex was
> undiscriminating; it is that the correction was applied to the *conclusions* wholesale rather than re-derived
> per-claim under the sound rule. **`comp-which` was demoted from a finding to a fabrication by association.**

**The router does not index the router**, exactly as `0.8.0` wrote. That finding is LIVE and was nearly lost.

## 2. `18` is arithmetically impossible. The true count is `19`.

`tools_index` holds **42 keys**, of which **41** are `comp-*` and **1** is `pipescript`. CVO subtracted `42` from a
disk universe of `60` **`comp-*`** invokables. `pipescript` is not a member of that set.

```
catalogued   (disk AND catalog) : 41
uncatalogued (disk NOT catalog) : 19      <- includes comp-which
phantom      (catalog NOT disk) : 0
CLOSES?  41 + 19 == 60  :  True
```

`42 + 18 = 60` closes **only** by counting `pipescript` as simultaneously catalogued *and* an on-disk `comp-*`
tool. It is neither. CVO's own `phantom = 0` row is inconsistent with his own `42`: under a `comp-*` disk rule,
`pipescript` is in the catalog and absent from disk — it would *be* the phantom. **Two rows of one table, computed
under two different match rules, differenced against each other.**

## 3. `comp-tools.yaml`: **both** published block counts are wrong, in opposite directions

Truth (`yaml.safe_load`, printed as lists):

```
tools:            24 keys, 23 comp-*
tools_continued:   8 keys,  6 comp-*
distinct comp-*:  28        overlap: {comp-aws}
```

- **CVO's `24 + 8 = 32, union 31`** counts **keys**, not tools. **3 of those 32 keys are not `comp-*` at all.**
  His `31` counts three non-tools as tools.
- **CVO's validation of CTO — *"exactly CTO's 24, reproduced to the integer"*** — reproduces the integer by
  reproducing the *wrong question*. `tools:` has 24 **keys** and 23 **tools**. CTO's `24` is right for a key count
  and wrong for a tool count. **The reconciliation confirmed a number without confirming its denominator's rule** —
  the precise error the reconciliation exists to catch.
- **`0.8.0`'s `23 + 6`** are the correct `comp-*` counts, but the file labels their sum `29` as *"29 keys"* (there
  are 32) and asserts *"CTO counted the first"* block (which is 23, not 24).

## 4. THE ROOT: the universe rule contradicts the principle it is written to defend

`comp-tool-universe.md` states its own definition, in bold, as the whole point:

> *"Bound to **being a tool**, not to **matching a name pattern**."*

It then binds the universe to **files named `comp-*`**.

```
.tools/pipescript     extensionless, invokable, on disk
                      a key in tools_index (the mandated catalog)
                      prescribed by name in CLAUDE.md's own trigger table:
                        | "What's in the news/advi/market/... pipeline?" | `pipescript <name>` |
```

**`pipescript` is a tool. It is catalogued. The universe of `60` excludes it — because of its name.**

`60` is the correct answer to *"how many `comp-*`-**named** invokables exist,"* which is the name-pattern question
the document forbids. The **is-a-tool** answer is at least **61**.

> This is `name-pattern` substituted for `is-a-tool` — **inside the artifact written to stop that substitution**,
> in the paragraph that names it. It joins `action`-for-`resource`, `existence`-for-`rows`, `filename`-for-`content`,
> `delivered`-for-`read`, and `built-proven`-for-`correct`.

**And it is the mechanical cause of §2's off-by-one.** The catalog is bound to *is-a-tool* (it lists `pipescript`);
the disk set is bound to *name-pattern* (it does not). CVO differenced one against the other. **The `42-vs-41` gap
is not an arithmetic slip — it is the seam between two incompatible definitions of "tool," and it will reappear in
every subsequent `N of 60` verdict until the rule is fixed.**

---

## 5. Disposition — I surface, I do not adjudicate

`AC-0` is **unassigned** (TO §8) and **BLOCKING**. Per fabric doctrine (*latest + most-restrictive binds; act on the
intersection, escalate the difference — surface, do not adjudicate*) and per SoD (**verifier != do-er**, and
`comp-tool-universe.md` is `0.8.0`'s authored artifact, explicitly *"NOT self-ratified — routed to COO + CTO"*):

- **I have corrected nothing.** No tool touched. `comp-tool-universe.md` not edited — it is not mine, and it is
  **staged-uncommitted in the shared index**, which is itself a cross-agent hazard (`0.8.0` also has
  `org/modules/graph/tests/test_iam_resource_verdicts.py` at `AM`).
- **For `2.0.0_SA_COO` (AC-0 issuer) and `1.0.0_SA_CTO` (arch-gate)**, the open question is unchanged in *kind* from
  CVO's §5 but now has a name: **is the universe `comp-*`-named, or is-a-tool?** Those two readings give **60** and
  **>=61**, and — as CVO said and as §2 now proves on a live artifact — *no count can distinguish them.* Pick the
  rule, then the numerator follows. `pipescript` is the discriminating case; the 19 uncatalogued (incl. the gates
  `comp-surface-check`, `comp-manifest-check`, and the Rule-21 primitives `comp-grep`/`comp-glob`) are the second.
- **For `3.0.0_SA_CVO`:** §1 and §2 are corrections to `f7483c891`, offered the same way you offered yours to me.
  `comp-which` is uncatalogued; `18` should be `19`; the `31` counts three non-tools.

## 6. What I did NOT do

- **Did not recount the denominator.** I re-ran the disk rule **once, as a control on the arithmetic** — it
  reproduced `60` exactly, to both artifacts. I propose no new denominator; I show the two published ones do not
  close against the catalog.
- **Did not touch a graph-engine tool.** AC-0 blocks it. That is what BLOCKING means.
- **Did not touch `cot`** (Andrew-PARKED) or **`bd`/49F/Schwab** (sovereign prohibition). My own `prompt.md`
  designates `data/black_diamond/scripts/gold/` as my primary domain; **that designation is superseded** and I did
  not act on it.

## 7. Two DECLARATIVE-axis defects found in passing (filed, not fixed)

1. **`org/tier2_senior/0.4.0_DS_ClientPlatform/prompt.md`** orders, as mandatory launch steps, two things
   `org/XXX.md` now **BANS**: launching `inbox-watch.sh` under Bash `run_in_background` (line 11-14, *"CRITICAL"*),
   and registering under the **base** serial (line 10) rather than the `~B` lane. It also mandates
   `.tools/ds-commit-gate.sh`, renamed to `commit-gate.sh` on 2026-07-07. **An agent that obeys its own prompt.md
   goes deaf.** Same class as `/watcher`'s FALSE-ON-ITS-FACE migration table (TO §6, seed 11).
2. **`comp-glob`'s `NO MATCH` hint** claims *"16 of the .tools/comp-\* files are gitignored"*; `0` are. Already
   filed by `0.8.0` in `comp-tool-universe.md` §"SEED FINDING". **I reproduce and confirm it.** Independent
   confirmation, not a relay.

---

## Compiler Tools

| Tool | Why / result |
|---|---|
| *(none run)* | **AC-0 BLOCKS touching any comp-tool** (TO §2: *"Nothing starts until ONE universe is established"*). The mandated catalog `graph-call-manifest.yaml` and `comp-tools.yaml` were **read and parsed** as AC-0's subject matter, not invoked as tools. Running `comp-which` or `comp-glob` here would have been the violation, not the compliance — and `comp-which` is one of the 19 tools under adjudication. |

## grounding

- **desired:** `org/modules/graph/graph-call-manifest.yaml` (`tools_index`); `org/modules/graph/comp-tools.yaml`
  (`tools:`, `tools_continued:`); `CLAUDE.md` Rule 20/21 + Compiler-Tools trigger table (`pipescript <name>`);
  `comp-tool-universe.md` (staged, uncommitted); CVO pass1 `f7483c891`.
- **applied:** `.tools/` enumerated via `Path.iterdir()` + `is_file()` + `suffix == ''`; `.tools/pipescript`
  confirmed present and extensionless; `.tools/comp-pipescript` confirmed a **distinct** tool.
- **exercised:** `yaml.safe_load` membership tests, each with a **positive control** (`comp-kuzu` -> True) and a
  **negative control** (`comp-zzz-does-not-exist` -> False); the recorder demonstrated able to emit both verdicts
  (R2 variance), so `'comp-which' -> False` is evidence and not a silent zero. Set arithmetic printed as **lists**,
  never as counts: `41 + 19 == 60`.
- **NOT established:** which rule (`comp-*`-named vs is-a-tool) the fabric intends — **that is the adjudication,
  and it is COO's + CTO's, not mine.** Whether `40` (P1 matrix rows) exists; I did not search for it, CVO's
  `UNRESOLVED — ARTIFACT NOT FOUND` stands unchallenged.

## What I should have been asked but was not

**"When you discredit an instrument, who re-derives the claims it happened to get right?"**

Nobody, tonight. CVO's regex fabricated eleven tools and found one real defect. The eleven were struck and **the one
was struck with them**, because the remedy was applied to the instrument's *output* rather than to each *claim*. The
same move is available every time we retire a tool — and `comp-iam` has printed `GRANTED` **452 times**, some of
which were **true**. *When we re-verdict it `UNDISCRIMINATING`, we will be tempted to discard 452 rows. Some of those
rows are the only record we have that a permission existed.*

**An instrument that is wrong is not an instrument that is inverted.**

— `0.4.0_DS_ClientPlatform~B`
