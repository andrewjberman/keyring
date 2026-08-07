# 4.0.0_SA_CRO -- session close: four sovereign calls ruled and executed, and the C3.ii join was rebuilt on the PRD corpus after Andrew called the registry-only approach too thin (2026-08-07 17:10Z -> 21:20Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE, VALIDATE

## Window

17:10Z -> 21:20Z. Prior log: `c3ii_join_shipped_and_three_defects_in_my_own_instrument_1600-1710Z.md`
@bdac197ce3. **4 commits mine**; 20 by `4.0.0_SA_CRO~A` (coordinated, not authored by me).

## What happened

**1. ANDREW RULED ALL FOUR OPEN CALLS. VERBATIM: "Approved acrtoss the board"** (~1940Z, my
terminal, answering `/open-calls`). Recorded durably @784e17bb66 **transcribed exactly as typed,
keystroke included** -- a verbatim record that has been tidied is not a verbatim record -- and
broadcast to CTO + COO + MSTR + `~A` the same turn.

**2. CALL 1 -- THE PROCEED-CONDITION IS RATIFIED AND IS NO LONGER INFERRED.** Every log at this seat
since 0500Z declared the ATOM_DECOMP work as resting on an authorization I had inferred and he had
not answered. **The unwind contingency is DISCHARGED, not exercised.** It closed the same call for
`~A`, who had deliberately rendered it in their own `/open-calls` as NOT-MINE with no rec attached so
it could not ride along on his earlier ruling -- **their refusal to widen was vindicated: it took a
separate sovereign act 25 minutes later to close it.**

**3. CALL 3 LANDED @0f5515683c + guard @76ae332de0.** Resource-prefix column in `MACRO_CODES.md`:
**3 rows filled from measurement** (`BDPL->bd-` 28 resources, `YALP->yang` 22, `SXPL->smartx` 5),
**~32 deliberately empty** because only three are derivable and the observed dominant tokens for the
rest are misleading (`ADVI` reads `shared`, `MDPF`/`MKPF`/`TAXX` read `inf`, `SXIN` reads `fred`).
Filling from those would be a hand-drawn roster wearing a predicate's clothing -- the defect the
column exists to remove, re-introduced inside the artifact meant to fix it. Plus a **retired-macro
guard** (CTO's catch): give `CENG` a matching prefix and it flips to APPLIED, the negative control
silently dies, and recall appears to improve at the moment the instrument goes blind.

**4. THE ACTOR QUESTION -- my caution was right and my premise was the wrong rule.** I read the
`ANY_EXEC_OR_AE` membership note (scoped to project registration, "must NOT be read as blanket") and
correctly concluded it does not cover `MACRO_CODES.md`. It does not -- and it is not the governing
rule. The file falls through to `org/projects/**` -> `ANY_EXEC`, which I have held unscoped since
07-22. Resolved independently three ways (mine, COO's, CTO's). **CTO's transferable form: WHICH LANE
APPLIES IS DECIDED BY THE PATH RULE, NOT BY YOUR MEMBERSHIP LIST.**

**5. >> ANDREW CALLED THE C3.ii APPROACH TOO THIN AND HE WAS RIGHT. << ** Verbatim: *"you should
actually scan the associated PRDs with some kind of rare token search or bm25, some kind of
structured discovery... it should make it very very obvious what the relevant semantic verticals
are."* The registry-only join derived 3-5 tokens per macro from ONE TABLE ROW, left five codes with
no usable key, and emitted 31% false candidates. **A 35-row table is not a corpus. The PRDs are: 895
documents, ~9.7MB, never read.** Built `c3ii_prd_vertical_discovery.py` @951c8834f4 -- **engine
REUSED, not reimplemented**: `dup_scan.BM25` is estate-canonical and comp-state already reuses it,
so this is the third consumer (Build Ladder rung 2).

**6. THE SCORER FAILED IN BOTH DIRECTIONS FIRST, and the fix was one I had already justified.** A
">=30% of the macro's own docs" bar admitted **nothing** for 120-doc macros (ADVI, OPAL) and admitted
**any identifier appearing twice** for small ones (SXIN returned `getflag`, `wt_iwr`, `tsla` at
conc=1.0). Both are a SUPPORT problem: concentration as a point estimate treats 2-of-2 as identical
to 25-of-27. Replaced with the **Wilson lower bound** + a `sqrt(n)` support floor -- the same
correction applied to the TO-0 denominator, for the same reason, **not a threshold tuned until the
output looked right**.

**7. THE RESULT SORTS THE 35 MACROS ON EVIDENCE, which is what he asked for:**
- **COHERENT VERTICALS** (real domain vocabulary): `ADVI` (allowedfirmids, pseudonymization,
  advisorid, rel_id) · `MDPF` (non_model_assets, methodology_version, enterprise_total) ·
  `COMP` (query_pass_rate, primary_metric, unaided) · `ETFS` (source_artifact, ownership_value).
- **UMBRELLAS** (vocabulary is their own SUB-PROJECT CODES, not domain terms): `NFRA` (graphuni,
  compproof, compdrift, comproute) · `YALP` (positn, valuat, correl). A registry OF verticals.
- **BUCKETS** (no distinctive vocabulary): `OPAL` 108 docs -> one weak term · `YANG` 41 -> none ·
  `AUTH` 38 -> none · MDLP, MKOV, TAXX -> none.
**Vocabulary coherence is a test of whether a macro is ONE THING**, and classes 2/3 land on exactly
the rows the Rule-24 grain finding flagged this afternoon from a different direction. Two independent
lines of evidence -- a taxonomy reading and a corpus measurement -- converging on the same rows.

**8. `~A` executed everything Andrew approved** (20 commits, coordinated by me): F-1 charter YAML now
parses, F-12 package map, F-4 ledger templates @3211dcd9b3; F-3 strike @5b18011518 and F-2 delta table
@96ed908f2f, both under the METHOD OWNER's ruling; and the CALL-2 case_study read @a99103cb0f, whose
headline is sharp -- **the corpus PROVES law 3 rigorously and then DROPS it from the list an agent
executes.**

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `bm25` across .tools/org/modules | **7 hits / 857 files** | **rung-2 hit**: found the estate's canonical BM25, so none was written |
| `dup_scan.BM25` | reused as a library over 895 docs | PASS | 3rd consumer after debtscan + comp-state; carries the discriminative-token cutoff already |
| `comp-find` | `def _read_s3`-class lookups, owned-paths reads | PASS | on-rails throughout; no raw repo grep |
| `commit-gate.sh` | discovery script | PASS | clean first pass |
| `safe-commit.sh` | 4 commits, all `-F` | PASS | risk-reflex CLEAN with its denominator printed (1,659 danger nodes) |
| discovery `--self-test` | 8 assertions | **8/8** | incl. a **negative control** (an unrelated doc is NOT forced into a bucket) and an idf-ordering check |
| `python` (import probe) | sklearn/numpy/model2vec/ST/tiktoken | PRESENT | `model2vec` (potion family) is installed but **NOT used** -- loading a model is egress and that needs his per-use word |

**What worked:** running rung 2 *before* writing a BM25 -- the estate had one, and comp-state's own
import line says it reused rather than reimplemented, so the precedent was already set. And treating
his "too thin" as correct rather than defending the prior approach.
**What failed:** my first scorer, in both directions at once, on the corpus it was built for.
**Gap found:** none new. The `comp-which` routing half remains open from this morning (low severity,
already routed).

## Blockers

**None.** All four calls ruled; nothing is waiting on a person.

## Current State (zero-context handoff)

- **NFRA_PYFIELD TO-0 CLOSED** (2,744/4,406 = 62.3%); **TO-1 CLOSED** by `0.8.0_AE_CloudComp`
  @50ff3747bf -- recognizer resolves 2,295 of 4,413, and `format_coverage()` RAISES rather than print
  a figure without its pins. **C3.ii TO CLOSED** @c4d354d714.
- **ATOM_DECOMP**: proceed-condition RATIFIED; mechanical fixes LANDED; audit closed at 14 findings +
  the case_study read; F-2/F-3 discharged by the method owner.
- **`MACRO_CODES.md`** carries the resource-prefix column, 3 of ~35 filled, retired-macro guard in.
- **PRD discovery** committed @951c8834f4 with `prd_discovery.json` (per-macro profiles + 133
  unlabelled PRDs + candidate terms).
- **5 commits unpushed** at write time; MSTR pushed a 31-commit backlog earlier this window and takes
  these on the next pass. Lanes commit, integrators push.
- **`4.0.0_SA_CRO~A`** is IDLE, its authorized scope complete.

## Next Steps

1. **[4.0.0_SA_CRO] RE-RUN THE C3.ii JOIN AGAINST THE PRD-DERIVED TERM PROFILES.** This is the
   highest-value next action and it is unblocked. The 187-candidate figure and its 31% false rate were
   produced by the thin registry matcher; the profiles from @951c8834f4 replace it. **Republish with a
   FRESH VINTAGE -- do not edit 187 in place**, or the record carries two numbers under one vintage.
2. **[4.0.0_SA_CRO] CALL 2 residue -- my six own-file findings** (F-8/9/10/11/13/14): the v0.4-vs-v0.3
   changelog, the sec3/sec4 blanks contradiction, the missing fillable template, the decayed prose
   beside a correct pin, the "four laws" count that is three, the conflated citation. Authorized and
   not yet done.
3. **[4.0.0_SA_CRO] CALL 4 -- carrier enumeration**, narrowed: ~10 missing carrier extractors
   (`.loc`/`.iloc`, `groupby`, `on=`, `subset=`, `columns=`, `rename`, `set_index`, `sort_values`,
   `drop_duplicates`, `assign`) + shape-test across all 386 files. **Do NOT hand-measure the attribute
   axis** -- unbounded, resolver-gated, and TO-1 now reaches it.
4. **[4.0.0_SA_CRO -> 1.0.0_SA_CTO~A]** The three-way macro classification (verticals / umbrellas /
   buckets) is method-owner material and converges with the Rule-24 grain finding. Surface, not
   dispatch.
5. **[Andrew, no rush]** The ~32 empty prefix rows need DECLARING by surface owners, not inferring by
   me. And `model2vec`/potion is installed but unused -- if you want embedding-based discovery rather
   than BM25, that needs a model download, which is egress and therefore your word.
