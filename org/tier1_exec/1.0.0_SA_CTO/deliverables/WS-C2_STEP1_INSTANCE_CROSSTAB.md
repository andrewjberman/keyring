# WS-C2 STEP 1 -- THE INSTANCE CROSS-TAB, with forced and measured cells separated

**Program:** NFRA_VELOCITY / CORE, WS-C2. **Author:** `1.0.0_SA_CTO~Z`. **2026-07-31.**
**Predecessor:** `WS-C2_STEP0_AXIS_COMMENSURABILITY.md` rev 3 `@ee3673d89`.
**Corpus:** `org/tier0_exec/0.0.0_AB_MSTR/deliverables/INCIDENT_TAXONOMY/` (files 01-11).
**Extractor:** a strict 9-axis table-row parser, then a permissive one. Both re-runnable.

**Fence:** `ADVI_PERFORMANCE` / `MDPF_GLOBAL` not drawn on, not opened.

---

## S.1 THE DENOMINATOR, RESOLVED FIRST -- AND ONE GAP I CANNOT CLOSE

| count | source |
|---|---|
| **218** | naive `grep` for a table row containing an M-token |
| **208** | permissive 9-axis parse -- **the working denominator** |
| **204** | rows carrying an ASSIGNED mechanism (`M\d+`) |
| **4** | rows where the MECHANISM COLUMN IS AN EM-DASH -- **the taxonomy's OWN residual** |
| **210** | `00_SUMMARY.md`'s claim |
| **+2** | **UNRESOLVED GAP vs the summary. Stated, not reconciled away.** |

**THE 218 IS WRONG AND THE WAY IT IS WRONG MATTERS.** The 14 excess rows are *disposition* rows --
`| **PROMOTE M1** | 9 instances... |`, `| **COLLAPSE §7a-§7d into instance rows under M6/M9** | ... |`.
They MENTION mechanisms; they are not incidents. **A mention counted as an instance is M8
(TEXT vs SEMANTICS) committed against the very corpus that defines M8.**

**AND MY FIRST PARSE WAS ITSELF DEFECTIVE, IN THE MECHANISM I HAD JUST NAMED HOMELESS.** The strict
regex required `M\d+`, so **every incident whose mechanism column is an em-dash was silently dropped**
-- 204 returned as if it were the whole set. Those 4 rows are precisely the incidents *the taxonomy
itself could not mechanism-classify*, i.e. the most interesting rows for an expressiveness question.
**A well-formed query returning a well-formed wrong answer: M2, mine, on the third attempt of a night
spent naming it.** Caught only by reconciling against a denominator I did not control.

**File 11 (`COMPILER_TOOLS_LOG`) contributes ZERO incident rows** -- it is telemetry aggregate
(22,911 PASS / 2,006 FAIL), consistent with the summary's separate *"26,235 parsed telemetry rows"*.
Not a gap.

**The +2 remains open.** I am not adjusting a denominator to match a headline.

---

## S.2 MEASURED PER-MECHANISM DISTRIBUTION (denominator 204 assigned)

| M | n | % | M | n | % |
|---|---|---|---|---|---|
| **M6** | 41 | 20.1 | M11 | 12 | 5.9 |
| **M1** | 25 | 12.3 | M9 | 10 | 4.9 |
| **M5** | 22 | 10.8 | M3 | 9 | 4.4 |
| **M2** | 19 | 9.3 | M10 | 7 | 3.4 |
| **M14** | 17 | 8.3 | M4 | 6 | 2.9 |
| M8 | 16 | 7.8 | M12 | 5 | 2.5 |
| M7 | 13 | 6.4 | M13 | 2 | 1.0 |

**MSTR's concentrated four (M6+M1+M2+M5) = 107/204 = 52.5%**, against the summary's *115/210 = 55%*.
**Consistent within the denominator discrepancy -- the concentration REPRODUCES.** That is a genuine
independent re-derivation of MSTR's headline from the raw rows.

**M14 at 17 is FIFTH, two incidents behind M2.** The "four mechanisms" boundary is not a natural
cleavage; it is a top-N cut with a near-tie at the edge. **Worth stating because "four mechanisms carry
55%" reads as a discovered structure and is partly a choice of N.**

---

## S.3 THE CROSS-TAB (denominator 208, all rows)

| bucket | n | % | forced or measured? |
|---|---|---|---|
| `TUPLE: grain` | 72 | 34.6% | **assignment FORCED, magnitude MEASURED** |
| **HOMELESS (untypeable)** | **36** | **17.3%** | **MEASURED** |
| `D3-obligation` | 31 | 14.9% | assignment FORCED, magnitude MEASURED |
| `TUPLE: plane` | 26 | 12.5% | assignment FORCED, magnitude MEASURED |
| `TUPLE: scope` | 25 | 12.0% | assignment FORCED, magnitude MEASURED |
| `PARTIAL` | 14 | 6.7% | MEASURED |
| `NO MECHANISM ASSIGNED` | 4 | 1.9% | MEASURED |
| **`TUPLE: rail`** | **0** | **0.0%** | **MEASURED** |

**HOW TO READ FORCED-vs-MEASURED, since this is the control CVO~Z holds me to:** the *mapping*
`M6 -> grain` is a **definition** from step 0, so which bucket a code lands in is **forced**. What the
corpus supplies is **how many incidents carry each code.** So `grain = 34.6%` is *a measured count
passed through a forced assignment* -- **it is arithmetic on my own definition and carries no
independent evidential weight.**

---

## S.4 THE MEASURED RESULT -- THE ONLY CELLS THAT ARE EVIDENCE

Three numbers do NOT depend on which typed bucket anything lands in, and are therefore the actual
findings:

> ### **HOMELESS = 36 of 208 = 17.3%**
> **Roughly one incident in six in the estate's own corpus CANNOT BE TYPED BY THE VOCABULARY AT ALL** --
> M2 (shape-match, wrong content) and M14 (prose-as-control). This is the expressiveness measurement
> WS-C2 exists to produce, and it is independent of the forced mapping.
>
> ### **`rail` TYPES 0 of 208 = 0.0%**
> Step 0 derived this from 14 definitions; **it now holds against 208 instances.** One of the four
> tuple fields names no failure dimension in the entire corpus.
>
> ### **UNTYPEABLE BY EITHER SCHEME = 40 of 208 = 19.2%**
> HOMELESS (36) + mechanism-unassigned (4). **Nearly one in five incidents is outside BOTH MSTR's
> mechanism axis and my rails.** Neither vocabulary alone, nor both together, covers the corpus.

**S.4 OF STEP 0 IS NOW PARTIALLY DISCHARGED.** Its collapse claim was marked FORCED. **It stays
forced** -- the collapse toward `grain` is still my definition doing the work. **What is now measured
is the RESIDUAL, and the residual is the honest expressiveness answer.**

---

## S.5 WHAT THIS DOES TO MSTR's V1

The concentration **reproduces** (52.5% vs 55%, within the denominator gap) -- so it is a property of
the corpus, not an artifact of the classifier. **That is a real V1 result and it is MEASURED.**

But it does **NOT** re-bucket into four distinct tuple classes: M6 and M5 both being `grain` is one
fact stated twice, exactly as step 0 warned. **So V1's answer is:**

> **THE CONCENTRATION IS REAL AND INDEPENDENTLY RE-DERIVED FROM THE RAW ROWS. IT DOES NOT SURVIVE AS A
> FOUR-WAY STRUCTURE UNDER A SECOND SCHEME, BECAUSE THE SECOND SCHEME COLLAPSES THREE OF THE FOUR INTO
> TWO FIELDS AND CANNOT TYPE THE FOURTH (M2) AT ALL.**

**The most useful thing the re-bucket produced is not agreement -- it is that M2, the one member of the
concentrated four my vocabulary cannot hold, carries 19 measured incidents.** A high-frequency
mechanism with no home is a stronger argument for building one than any coverage percentage.

---

## S.6 RESIDUAL + NEXT

- **The +2 denominator gap is OPEN** and is not to be closed by adjusting a count.
- **M3's split** (partition-key = grain vs hash = plane) is unresolved; 9 incidents ride on it.
- **The 4 mechanism-unassigned rows** deserve a read -- they are the taxonomy's own honest UNKNOWNs.
- MSBEFF **by class** and the DEBTLOOPS round-trip remain.
- **M2 stays NAMED HOMELESS** with 19 corpus instances plus six live ones from this session -- including
  two of my own extractor defects while producing this document.
