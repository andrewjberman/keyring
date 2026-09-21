# ANDREW-DIRECT 2026-09-21 ~00:5xZ -- **/self-drive RE-SCOPED: LGIC and NFRA_OPLGTW OUT; MDPF_TAXSMA and NFRA_MCPINDEX IN** -- and this seat spawns the two COO lanes

**Seat:** `1.0.0_SA_CTO` · **Device:** laptop · **Branch:** CLOUD · **Terminal:** `1.0.0_SA_CTO`

---

## 1. HIS WORDS, VERBATIM

> *"adjust drive loop, LGIC is going to be taken out of the loop, NFRA_OPLGTW is to be taken out of the loop,
> instead we will be proceeding with TAXSMA and MCPINDEX. I have already closed out COO~O and will be closing
> out COO~G now. You must spawn the new COOs and adjust your drive loop accordingly."*

Typos and casing are his. **This record is the ARMING RECORD for the new scope** (`/self-drive` §5: a re-arm on
a new word is a NEW record) and is **committed before tick 1** (§0.5).

## 2. THE CODES, RESOLVED RATHER THAN GUESSED

He named *"TAXSMA"* and *"MCPINDEX"*. A wrong code must never read as a clean pass, so both were resolved
against the register and `sequence-check`:

| he said | resolved | evidence |
|---|---|---|
| TAXSMA | **`MDPF_TAXSMA`** | `org/missions/D8/MDPF/MDPF_TAXSMA/project.json` -- laptop, `dep_stage EXECUTING`, `status scoping`, `coo_lane 2.0.0_SA_COO~T`, **sequence flag `LANE-DARK`** |
| MCPINDEX | **`NFRA_MCPINDEX`** | `org/missions/D9/NFRA/NFRA_MCPINDEX/project.json` -- laptop, `dep_stage PRD`, `status active`, `coo_lane null`, **sequence flag `NEEDS-SLOT`** |

⚠ **ONE AMBIGUITY, NAMED NOT ABSORBED:** three legacy flat stubs also carry the token --
`org/projects/OPAL_TAXSMA.json`, `OPAL_TAXSMA_PT2.json`, `OPAL_TAXSMA_REGISTRY.json`. **I have taken
`MDPF_TAXSMA`**, because `SEQUENCE.yaml` names `MDPF_TAXSMA` and `NFRA_MCPINDEX` **in the same sentence** as
his seat priority. If he meant an `OPAL_TAXSMA*` stub, one word re-points it.

⭐ **BOTH ARE ALREADY PLACED AT SEQUENCE STAGE 0 -- literally titled *"Andrew's seat priority -- MDPF_CANON,
then IRPT_BCKEND, then MDPF_TAXSMA, then NFRA_MCPINDEX"*** -- and **both PRDs read v0.5 ADMITTED with the
brief AND ratified-text halves SIGNED.** The instruction moves the loop onto work the sequence already ordered
and the L4-R gate already cleared; it is not a new fork.

## 3. ARM TERMS

| term | value |
|---|---|
| **scope** | `MDPF_TAXSMA, NFRA_MCPINDEX` |
| **replaces** | `LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM` (his word: *"taken out of the loop"*) and `NFRA_OPLGTW` |
| **cadence** | 30m, unchanged |
| **device** | laptop |
| **adjudication** | unchanged -- this seat adjudicates every adjudicable call itself; a call pending at another seat is never a reason to idle |
| **paired_with** | the two COO lanes below (his word institutes them) |
| **STOP-CONDITION** | §4 completion test read from the register, or his stand-down |

## 4. THE TWO LANES

| project | lane | why this serial |
|---|---|---|
| `MDPF_TAXSMA` | **`2.0.0_SA_COO~T`** | **the register ALREADY names `~T`** and the sequence flags it `LANE-DARK`. Seating `~T` makes the register TRUE; inventing a new letter would create a second truth beside it. |
| `NFRA_MCPINDEX` | **`2.0.0_SA_COO~M`** | free (in use: `~A ~B ~C ~D ~E ~F ~G ~O ~T ~X ~Y ~Z`), mnemonic, and the project's `coo_lane` is `null` so nothing is contradicted. |

**CAPACITY, checked against his own 2026-09-14 cap of three concurrent COO lanes:** live now are `2.0.0_SA_COO~B`
(IRPT_BCKEND round 7, mid-flight) and `2.0.0_SA_COO~G` (closing on his word). `~O` is already gone. After `~G`
closes: **`~B` + `~T` + `~M` = 3. At the cap, not over it.**

Model/effort are **not hand-passed**: `spawn-agent.ps1` derives Opus 5 / extra-high for Tier 2 on the spawn
path, and the derived form exists precisely so a successor cannot lose the instruction silently.

## 5. WHAT I AM HANDING OFF, NOT ABANDONING

LGIC leaves my loop with work **measured and owed**, and it is stated here so it is not lost with the scope:

- ⛔ **17 LGIC task orders read `<status> complete` while their own proof-of-spec records a FAILING
  criterion** (`CANON` 2, `ENFORCE` 6, `LGCTFM` 4, `NAMING` 5). **Corrected figure:** I broadcast **19** an
  hour ago; 19 counted TERMINAL, and **2 of those read `superseded`, where a failing criterion is legitimate.**
  `2.0.0_SA_COO~G`'s `LGIC_ENFORCE-S103` named six; the measured population is **17**.
- **One open disarm clock**, `LGIC_CANON-S22` (ARMED, residual sized at 278 raises in six unowned families).
- **Seven clock-less rows decided by this seat and awaiting carriers `3.0.0_SA_CVO` must MINT** -- four
  DISARMED, two staying ARMED, `LGIC_LGCTFM-S66` ARMED with a narrowed remedy.
- **`LGIC_LGCTFM-S66` touches Andrew directly:** the `ANDREW_CARD.md` he holds contradicts itself, and `FWD-4`
  closes on his read of it. **One line needs correcting before that read counts.**
- **`LGIC_ENFORCE-S149`**, the slug-proxy gate defect, carded ARMED and deliberately unfixed.

## 6. ORDER OF EXECUTION

1. **This record, committed** (§0.5 -- no carrier, no tick).
2. **Spawn `2.0.0_SA_COO~T` and `2.0.0_SA_COO~M`.**
3. **Broadcast to every live seat same turn**, naming the scope change and the LGIC hand-off.
4. Tick 1 on the new scope.
