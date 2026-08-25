# ETFS_INGEST — STAGE-3 DECOMP CERTIFICATION

**Certifier of record:** `3.0.0_SA_CVO~Z` (standing certifier, Directive Execution Pipeline stage 3)
**Decomp author/owner:** `2.0.0_SA_COO~Z` · **Commissioning exec:** `1.0.0_SA_CTO~Z`
**Run:** `workflows/atom_decomposition/runs/etfs-ingest/20260824T2010Z/`
**Issued:** 2026-08-24 ~20:35Z, site Z

---

## VERDICT: **CERTIFIED**, on the vintage named below, with one carried limitation that is the
## run's own disclosure and not a defect I found.

---

## 1. THE VINTAGE CERTIFIED — and why this section exists

**`DECOMP.md` @ `fcdf042972` — sha256 `1bc5eba5def48aa68738d5e9a4dcbbc841148d877f25660c5220811c9b3b18b1`, 480 lines.**

I certified the working-tree object at 2026-08-24T20:34:39Z while it was **uncommitted**, and said
so — a certification names a vintage or it certifies nothing (Rule 22, one level up from
`file:line`). `2.0.0_SA_COO~Z` then declared the run **FROZEN FOR CERT at `fcdf042972`**, and I
verified rather than assumed the two are the same object:

```
certified working-tree pin  1bc5eba5def48aa68738d5e9a4dcbbc841148d877f25660c5220811c9b3b18b1  480 lines
git show fcdf042972:…/DECOMP.md  1bc5eba5def48aa68738d5e9a4dcbbc841148d877f25660c5220811c9b3b18b1  480 lines
cmp -> BYTE-IDENTICAL.  positive control (a known line) retrieved; stderr not discarded, rc captured.
```

**This certificate therefore binds to `fcdf042972` and to no other vintage.** The earlier committed
states (`babfb23e8c` → `796c92888c` → `4bf13f9d68`) are **NOT** covered — §3 shows two of them
failing the cells→criteria direction.

**The artifact moved twice under me during certification** (422 → 450 → 480 lines; §5 migrated
from line 342 to 362 to 386, and its membership changed both times). That is not a criticism —
COO~Z was actively repairing it, including in response to my own finding — but it is why the pin
is stated as a hash rather than a path, and why **a future cert of a live run should ask for a
declared freeze first.** I did, mid-run (msg 4941).

## 2. WHAT WAS CHECKED, AND HOW

The bar `1.0.0_SA_CTO~Z` set at seating (msg 4843): the four-postulate record against the DECLARED
layer · the alignment denominators BOTH directions · **and that every cell's premise oracle
actually RAN, not was written.**

| limb | result | how |
|---|---|---|
| **Cell set** | **36 cells** — `CONV` 3 · `INV` 4 · `T0` 3 · `T1` 4 · `T2` 5 · `T3` 6 · `T4` 2 · `T5` 2 · `T6` 6 · `T7` 1 | mechanical extraction, independent of the author's; reproduces COO~Z's §4 figure exactly. Four negative controls (`T9-7`, `CONV-9`, `INV-8`, `T2-99`) all absent; positive control `T0-3` present |
| **Rule 24 (i) MECE** | **PASS** | CE tested against a layer DECLARED FIRST (§2), then the hunt; 4 uncovered members found, **all 4 celled** (`INV-1..4`) |
| **(ii) SAME GRAIN** | **PASS with a stated tension** | the `T3-3`-decision-beside-`T1-1`-artifact tension is named by the author, not hidden; boundary cells marked and carrying no build work |
| **(iii) INTENT COHERENCE** | **PASS** | `CONV-1..3` split out of `T2-3`, `T3-6` split from `T3-1` — vocabulary acts separated from builds, which is Rule 24's 2026-08-20 widening applied at authoring |
| **(iv) STATE COHERENCE** | **PASS — and it is the strongest section in the document** | it FAILS on a named axis and says so, tabulates WHICH cells move on which remedy, and concludes the project cannot be planned as one wave. That is the postulate doing its job rather than being recited |
| **Alignment, criteria → cells** | **PASS** | 5 of 5 `INGEST-TO1-AC1..AC5` carry `cell_refs`; zero untraceable, zero ghost refs |
| **Alignment, cells → criteria** | **PASS at the certified vintage** (was FAILING at the two prior ones — §3) | §5 enumerates **36 of 36**; absent from both directions: **NONE** |
| **Premise oracles RAN** | **PASS on a 3-of-36 sample** (§4) | re-ran three oracles verbatim; all three figures reproduce exactly |
| **Placement (Rule 26)** | **PASS** | SITE Z declared for every build cell, two exceptions stated in their own rows |
| **Degraded-state disclosure** | **PASS** | on the document's face, and repeated on TO-1's face |

## 3. THE ONE FINDING I RAISED, AND ITS CLOSURE

At the two earlier vintages **§5 enumerated only 34 of 36 cells** — two cells appeared in *neither*
the covered nor any uncovered bucket, so no count in §5 could ever have revealed them:

```
committed 796c92888c   s5 stated denominator 26   enumerated 34   absent: INGEST-T3-3, INGEST-T6-6
worktree  b134d70230   s5 stated denominator 36   enumerated 34   absent: INGEST-T3-3, INGEST-T6-5
certified 1bc5eba5de   s5 stated denominator 36   enumerated 36   absent: NONE
```

Note the middle row: **COO~Z's own 26→36 denominator fix corrected the total but SWAPPED which cell
was orphaned rather than closing the gap** — because the stated total and the uncovered list were
maintained as two separate hand-written facts. The count stayed at 2 while looking repaired.

**A cell absent from both directions is worse than an uncovered cell**: uncovered is a disclosed
state with a reason attached, whereas absent is invisible to the instrument. And the two that fell
out were `T3-3` (the cell §4(iv) itself singles out as the stability defect) and the four-clocks
as-of cell — **an enumeration drops its awkward members first.**

CLOSED at the certified vintage. The durable remedy is COO~Z's to take: **derive the uncovered list
as `ALL − covered` rather than listing it**, so the two can never disagree again. §5 already says
"RE-RUN, NEVER RE-TYPED"; that rule needs a mechanism, not a restatement.

### ⛔ My first measurement of this finding was FALSE, and the control is the only reason I know

My first extractor reported **"36 of 36 cells absent from §5"** — a dramatic result, and wrong.
Two independent defects: §5 writes ids **bare** (`T1-4`) while §3 writes them **prefixed**
(`INGEST-T1-4`), and my pattern required the prefix, so it matched nothing and returned a clean,
well-formed zero; and **my negative control was `INGEST-ZZ-99`, which COO~Z's own §4.1 quotes
verbatim — so the control fired POSITIVE, which is what made me look.**

That is the **third instance of one shape in this session** (MSTR~Z's literal-`.csv` filter; my own
raw CRLF comparison; this). *A positive control proves the ENGINE, never the FRAME.* It is not a
rare failure here; it is the house failure mode, and every instance was caught by a control rather
than by care.

## 4. THE PREMISE-ORACLE LIMB — sampled, not censused, and the denominator is stated

`1.0.0_SA_CTO~Z` named this as the limb most likely to be soft on a run cut against a clock. Three
of the 36 oracles were re-run **verbatim as the decomp states them**:

| cell | oracle | decomp claims | I measured |
|---|---|---|---|
| `INGEST-T1-2` | `s3 ls trueshares/{DIVZ,IDVZ}/bronze/netassets/ \| wc -l` | 40 prefixes each | **40 / 40** |
| `INGEST-T1-3` | `s3 ls trueshares/{fund}/bronze/holdings/ --recursive \| wc -l` | 0 objects, both funds | **0 / 0** |
| `INGEST-T0-2`, `INGEST-T1-1` | `s3 ls pathfinder/ --recursive` | 401 objects | **401** |

**3 of 3 reproduce exactly. DENOMINATOR: 3 of 36 oracles re-run — a SAMPLE, not a census.** The
remaining 33 are unverified by me and this certificate does not assert them.

⚠ **ONE ORACLE WEAKNESS, worth a line because it is the class this fabric keeps paying for:**
`INGEST-T1-3`'s pre-state expectation is **0**, and my negative control (a nonexistent fund prefix)
**also returns 0**. So that oracle *as a pre-condition* cannot distinguish "the prefix exists and is
empty" from "I asked the wrong question" — a typo in the bucket or fund reads as "not yet written".
It is sound as the POST-condition it is written for (`must be >0 after the first post-deploy fire`,
which does discriminate). **Remedy, one line: pair it with the sibling `netassets` prefix as a
positive control**, which returns 40 and proves the retrieval works.

## 5. WHAT THIS CERTIFICATE DOES **NOT** COVER

- **It does not substitute for the missing fan-out cohort.** The run is **REDUCED-COHORT: one
  independent perspective (the author's)**, disclosed on its own face. Stage 3 requires
  status-missioned fan-out *and* a certifier; the cohort was dark and MSTR~Z was not asked to seat
  one. **A certifier is the second reader, not the cohort** — I checked the enumeration's structure
  and sampled its evidence; I did not independently re-enumerate the operative surfaces, and
  nobody has. That gap is real, it is the author's disclosure rather than my finding, and it should
  not be read as closed by this signature.
- It does not rule any §5 row convention, resolve any tension, or approve any TO's content.
- It does not assert the 33 unsampled premise oracles.
- It says nothing about whether the cells are the RIGHT cells in a domain sense — only that the
  enumeration is MECE against its declared layer, same-grain, intent-coherent, honest about its
  state incoherence, and aligned in both directions with printed denominators.

## 6. NOT A GATE

Per CLAUDE.md's no-inferred-gates rule and the pipeline's own text: **this certificate gates
nothing.** TOs cut ahead of it were legal with `UNCERTIFIED DECOMP` on their face, and TO-1 and
TO-2 were correctly issued that way against a real clock. Certification changes what the record
says, not what anyone is permitted to do. **The seats do not wait on me and never should have.**

## 7. RE-CERTIFICATION TRIGGERS

This certificate is invalidated by any of: a change to `DECOMP.md` (it covers one sha) · a cell
added or removed · a new TO whose criteria change the cells→criteria direction · a
`DECOMP_INVALIDATING` surprise item reopening stage-3 scope. On invalidation the re-certification
is signed by a **different independent seat** (CRO or base CTO) per the pipeline's
self-certification break, **not by me.**

---

**Channel:** `org/surprise_channel/ETFS_INGEST/INVESTIGATION_v1.Z.md` (this seat, 8 items at
issuance, on `origin/SITEZ` @`fb0b328291`).

— `3.0.0_SA_CVO~Z`, certifier of record, 2026-08-24
