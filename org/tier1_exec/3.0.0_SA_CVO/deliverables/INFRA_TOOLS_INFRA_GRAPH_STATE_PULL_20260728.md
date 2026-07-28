# INFRA.TOOLS + INFRA.GRAPH — CVO state pull (5 fields per sub-group)

    to:        0.0.0_AB_MSTR (state pull, not a dispatch — routing stays CTO/COO)
    authority: Andrew-direct 2026-07-28, naming CVO: *"CVO separately focused on essentially the
               entire Infrastructure on enumeration aspects in the tools."* Register `604344553f`.
    from:      3.0.0_SA_CVO, grounded on this session's own measurements (anchors throughout)
    date:      2026-07-28T18xxZ

---

# SUB-GROUP 1 — `INFRA.TOOLS`

## 1 · ATTACH — **your list has one critical omission and several demotions**

You said you built it from code prefixes, not from knowing the work. **The omission is the single
most relevant project in the estate to this sub-group.**

**ADD — `NFRA_COMPUNIFY`. This is THE coverage-universe project.** It owns
`org/modules/graph/comp-coverage-map.yaml` (1,081 lines, the per-tool ledger) **and** the enforcing
gate `comp-coverage-check`. **Status: `complete`.** Exercised by me 2026-07-28T155xZ:
```
PASS: every tool one home, every overlap declared, no phantom seam, inventory complete,
      projection current, grain stable.
swept: 88 homed tool(s) (36 tools[] + 52 meta_tools[]) | 12 gate_contract rule(s), 0 unverifiable
```
**A state pull on "the enumerated coverage universe per tool" that omits COMPUNIFY is missing the
answer.** Not a criticism of your method — it is exactly the failure mode a prefix-built list has,
because COMPUNIFY's name says nothing about tools.

**ADD — `NFRA_MSBEFF`** (the empirical corpus: 21,775 rows, 718 findings, 187 override intents,
**129 referenced vs 83 registered tool names ≈ 46 phantoms** — the phantom class IS a coverage
finding). **ADD — `NFRA_COMPLEARN` + `NFRA_COMPDRIFT`**: the coverage map's own header names them as
the "ONE NOUN, TWO VERBS" pair (LD-0227) the ledger exists to serve — they are structurally attached,
not adjacent. **ADD (active, lower weight) — `NFRA_COMPASSURANCE`, `NFRA_COMPSIMILAR`, `NFRA_COMPTEAM`.**

**DEMOTE — `NFRA_TOOLHUD`** (`complete` 2026-06-16; the HUD nudge, not coverage).
**RECLASSIFY — `NFRA_COMPRAIL`** (`complete`, but the **live enforcement rail**): it is not a coverage
project, it is the **enforcement point** where a coverage mismatch becomes catchable. Attach it as
mechanism, not as scope.
**CORRECT — `NFRA_TOOLSEM`**: attached correctly, but **4 commits and ZERO code/infra files.** It is a
charter. Anything routed to it lands nowhere today.

## 2 · HOLES — live work covered by NO project code

- **H1 · The NEGATIVE declaration.** Per tool, *what it cannot see WITHIN its declared surface*. The
  map declares `surface`/`granularity`/`concern`/`store`; **none of that reveals that comp-heat is
  blind to gitignored files, 5 submodules incl. the entire portal, and all S3-resident code**
  (measured today: 24,605 tracked, **21.2% vendored**, 4 structural exclusion classes).
  **COMPUNIFY is `complete` and this is NOT a gap in its charter — it is beyond it.** So the work
  is real and belongs to no code. **Hole, not drift.**
- **H2 · The RUNTIME-PROVENANCE axis.** Rule 12 mandates EC2 code live in S3; every repo-scanning
  tool is therefore blind co-extensively with Rule 12's scope. Anchor: my brief `@d4fee91bc`; the
  measured instance is comp-clobber clean-on-a-thrice-clobbered-key `@cc025f038`. **No project code.**
- **H3 · `INFRA.TOOLS.O2` (output contract).** Your new objective. **No project code.** §O2 below.
- **H4 · Cross-tool coverage diffing at suite scale.** `comp-toolgraph` does declared-vs-actual for
  *coupling*; nothing does it for *coverage*. Sits between TOOLGRAPH and COMPUNIFY, owned by neither.

## 3 · STANCE — with anchors

| | verdict | anchor |
|---|---|---|
| **DECIDED** | **YES** | COMPUNIFY S0 contract + 4 locked CTO rulings + a 12-rule `gate_contract`, `comp-coverage-map.yaml:87-153` |
| **BUILT** (positive enumeration) | **YES** | 88 homed tools, gate PASS, **exercised** 2026-07-28T155xZ (not read — run) |
| **BUILT** (negative declaration) | **NO** | H1; no `excludes:` field exists in the schema |
| **SERVING** | **UNASSESSED** | I have not established whether `comp-coverage-check` is wired into a commit/CI path or is invoke-only. `routable: false, role: enforcement-gate` in the ledger tells me its *class*, not its *wiring*. **Not guessing.** |

**A correction I owe this report, because I made it three times today:** I claimed COMPUNIFY's gate
was "not built," its population was 36, and its exclusions vocabulary was absent. **All three false**,
each from reading a document instead of exercising the thing — the S0 header's forward-looking
*"the gate itself → S2"* read as current state. **`UNASSESSED` above is me not repeating that.**

## 4 · FRONTIER — the single next thing

**Wire PATTERN C (cross-derive) at suite scale: diff each tool's DECLARED `surface` against the
surface implied by its ENUMERATION PRIMITIVE; every disagreement is a coverage defect.**
Why this one: **it needs no oracle** — two independent derivations of the same set, differenced,
produce a negative signal without ground truth (Andrew's explicit constraint: *"even if the
negative-control has yet to have a true oracle"*). `comp-toolgraph` already implements this shape for
coupling, so it is an extension, not a build. Anchor: pattern library `@a3dac97be` §3-C.

## 5 · BLOCKED-ON

**Nothing sovereign. Nothing blocked.** The `excludes:` field + Pattern-C diff are additive to a
`complete`, green project; placement/ratification is **CTO + `0.7.0_AE_CloudOps~Z`** (OPAL_STNDRD),
which is routing, not a block. **Do not read this as needing an Andrew call.**

---

# SUB-GROUP 2 — `INFRA.GRAPH`

**Sent without reconciling with CTO, per your instruction.**

## 1 · ATTACH
`OPAL_STNDRD`, `OPAL_TAXONOMY`, `NFRA_TOOLARCH` (its C0-C3 ladder + §3 stability grader IS the
taxonomy engine), `NFRA_SYSPARITY` + `infra/system/` (modelled-vs-live parity, closed 22/22),
`OPAL_CONSOLIDATION_TAXONOMY_STANDARD.md`, `NFRA_GLOBGRPH` (the graph substrate).

## 2 · HOLES
- **The provenance dimension is absent from the ontology.** Token census over
  `NFRA_TOOLARCH_PRD.md` (116 lines): `provenance` 0, `artifact store` 0, `Rule 12` 0, `pulls` 0 —
  **positive control `archetype` = 12.** The C0-C3 ladder models what a thing IS and how it RELATES,
  **not how it comes to be what it is at run time.**
- **No standard for WHICH bucket holds runtime code.** Measured: **5 of 5 data buckets carry `code/`
  prefixes; all 3 dedicated artifact buckets are empty of code.** Rule 12 says S3, never says which
  bucket. Code inherits data's lifecycle, IAM blast radius and guard surface by default.

## 3 · STANCE
| | verdict | anchor |
|---|---|---|
| **DECIDED** | **PARTIAL** | key grammar + naming law + one-capacity-one-service exist; **no provenance taxonomy, no code-location standard** |
| **BUILT** | **PARTIAL** | one LIVE gate: `.parquet`-under-`bronze/` bucket-policy deny — **on ONE bucket** (opal-data-assets, 07-16); other trees open |
| **SERVING** | **PARTIAL** | 121 scheduled Rules vs 10 Scheduler = **92% on the non-standard side** of a standard that exists |

## 4 · FRONTIER
**Add PROVENANCE (P1 repo / P2 S3-resident / P3 image / P4 layer) as a first-class classification
dimension**, then re-grade every tool's universe against it. It is the axis that makes the other
findings computable rather than anecdotal.

## 5 · BLOCKED-ON
**CTO** — this is his lane and you told me we overlap deliberately. **My disagreement, stated as you
asked rather than reconciled:** his DEBTCLEAN framing of the mdpf case as *"`mdpf` is not a
`PIPELINE_MAP` key"* is an INSTANCE fix; mine is that **Rule 12 conformance makes the whole class
invisible**, so adding `mdpf` closes one tree and leaves the class open. **He has already accepted
this reframe in writing** (`20260728T151837Z`), so it may no longer be a disagreement — flagging that
it *was* one, and that the register should record the class version.

---

# `INFRA.TOOLS.O2` — output contract. **Your framing is right; here is the sharper form**

You proposed: *"a per-tool output contract — what it returns by default, how it bounds a large
result, and how it says THERE IS MORE instead of silently stopping."* **Adopt it. One change:**

>> **BOUNDING IS NOT THE PROBLEM. UNDECLARED BOUNDING IS.** A tool that returns 40 of 400 rows and
>> SAYS SO is correct and useful. The defect is a truncation the reader cannot detect — which is the
>> *same property* as an unenumerated coverage universe: **the output is byte-identical to the
>> complete one, so silence is uninterpretable.** O2 is the coverage-universe problem on the OUTPUT
>> side, and it should be stated that way so the two share a doctrine instead of drifting apart. <<

**FOUR MEASURED INSTANCES IN ONE DAY, from two agents — this is not hypothetical:**
1. **Yours:** `head -40` on a manifest inspection → you told Andrew the GitHub Actions runner was NOT
   in `EC2_MANIFEST.json`. **It was.** An absence read out of a truncated retrieval, on a live
   decommission decision.
2. **Mine:** `aws logs ... --query "length(events)"` applies **per page** → printed `2,0,0,0,0`, no total.
3. **Mine, worse — the "fix" was the defect:** `--no-paginate` truncated to page one and reported
   **1 invocation instead of 4**, which would have turned *"1 of 4, and it stopped"* into *"1 of 1,
   still firing every run"* — **the opposite verdict, from the same log, via a flag whose purpose is
   tidier output.** Caught only because 4 daily log streams existed and 1 was implausible.
4. **Mine:** `head -40` on comp-clobber's static scan — I had to re-run unbounded to trust the zero.

**Proposed contract, four clauses:**
- **C1 DECLARE THE DENOMINATOR IN-BAND** — every bounded output states `showing N of M`. M is the
  count *before* bounding. (Generalises Rule 22's retrieval control to tool output.)
- **C2 TRUNCATION IS A VISIBLE TOKEN**, never a silent stop — a trailing `[+K MORE, use --all]`.
- **C3 AN EMPTY RESULT MUST BE DISTINGUISHABLE FROM A FAILED RETRIEVAL** — `0 of 0` vs `RETRIEVAL
  FAILED`. This is the `git show` clean-empty-stdout class and the binary-mode-grep class in one clause.
- **C4 THE CONTRACT IS THE TOOL'S, NOT THE CALLER'S.** Every instance above came from a CALLER's
  bounding (`head`, `--query`, `--no-paginate`). **A tool that emits its own denominator survives a
  careless caller; one that does not, cannot be made safe by discipline.** That is the whole argument
  for putting this in the tool rather than in a habit.

**Frontier for O2:** C1+C3 on the ~12 highest-traffic comp-tools, since they are cheap and catch both
demonstrated failure modes. **Blocked-on: nothing.**

---

## Ground rules honoured
`UNASSESSED` used once and meant (INFRA.TOOLS SERVING). No CTO/COO lane re-derivation. Every stance
carries an anchor; where I ran something I say **exercised**, where I read something I say so. This
does not jump PORTAL_AUTHHARD or smartx without CTO or Andrew.

— 3.0.0_SA_CVO
