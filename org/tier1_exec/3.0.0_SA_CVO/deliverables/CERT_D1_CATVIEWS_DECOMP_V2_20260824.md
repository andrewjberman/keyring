# CERT — D1_CATVIEWS stage-3 decomp **v2** (the view-tree absorption)

**Certifier:** `3.0.0_SA_CVO` · **Requested:** COO 66383 · **Subject:**
`workflows/atom_decomposition/runs/d1-catviews/20260824T195537Z/DECOMP.md` @`469a9e9868`
**Date:** 2026-08-24 ~20:15Z · **Subject is LOCAL at cert time** (rides the integration window; stated
rather than called landed).
**Supersedes:** `CERT_D1_CATVIEWS_DECOMP_20260824.md` (v1 @`d2706b2849`), which the project JSON had
marked SUPERSEDED-PENDING-ABSORPTION. **This run IS the absorption, so that cert's state now closes.**
**Alternate post-invalidation signer:** base `1.0.0_SA_CTO` ONLY (CRO class excluded this session,
Andrew-direct ~19:3xZ).

## VERDICT

**CERTIFIED on the ENUMERATION — 28 of 28, both symmetric differences empty, arithmetic closes.**
**ONE P1 FINDING that COO must correct in the decomp (a SIZING line, not a missing surface), and it
does NOT invalidate the run** — which is my pre-stated discriminator doing exactly the work it was
stated to do: *I certify the enumeration, not the sizing.*

## MECHANICAL — measured at this seat, with the extractor controlled

| | measured by me | COO stated |
|---|---|---|
| cells declared (leading table cell, markup-stripped) | **28** | 28 |
| cells mentioned anywhere in the file | **28** | — |
| **mentioned-but-not-declared** | **EMPTY** | — |
| declared duplicates | **EMPTY** | — |
| arithmetic | **14 carried + 13 new (h) + 1 new invariant = 28** | 14 + 13 + 1 = 28 |
| criterion-bearing | **25** (non-bearing: `D1-g-1`, `D1-g-2` by declaration; `D1-f-1` DARK) | 25 |
| criteria → cells | **0 criteria → NOT-YET-EVALUABLE** | stated as NOT-YET-EVALUABLE, not MISALIGNED |

**THE EXTRACTOR WAS CONTROLLED THIS TIME, BECAUSE IT WAS WRONG TWICE ON v1.** It now strips `**`
and backticks before matching and accepts bare, bold, backticked and bold-backticked declarations.
Controls run: `D1-h-v4` PRESENT ✓ · `D1-h-r1` PRESENT ✓ · `D1-zz-9` ABSENT ✓ · `D1-h-v9` ABSENT ✓ —
**it discriminates, and a fabricated id in the same shape does not fool it.**
*One reading note on my own output: a secondary check listing "declared but appearing only once" is an
artifact of that check's design (a cell mentioned solely in its own declaration row), **not** a finding —
declared ⊆ mentioned holds by construction, so the load-bearing difference is the empty
mentioned-but-not-declared set.*

**COO's s.0.1 pre-empted the exact failure that broke my v1 pass.** They declared the 14 carried cells
in full because their own `grep -o` control read 20 of 28 — *"my own grep-o control read 20/28 before
that table existed, so I added it rather than let you find it."* **A decomp author running the
certifier's instrument against their own file, and repairing what it found, is the process working.**

## RULE 24 — five records, and (iv) applied as a TEST rather than asserted

`R-h0` L0 axis · `R-h1` Client L1 · `R-h2` Models L1+L2 · `R-h3` SMAs L1 · `R-h4` PRESENCE. Present for
every enumeration v2 mints **or adopts** (the 08-20 widening: adoption is an authoring act).

- **`R-h1` DECLARES A CE FAILURE AND REPAIRS IT AS A CELL.** Andrew's Client L1 is two-valued;
  Cottonwood's live flag is three-valued (`unflagged`, `D_05.supervised_split.py:126-137`). COO did not
  paper this over and did not fold it — `D1-h-c3` renders it as a labelled third bucket, on the stated
  ground that folding *"would silently move AUM across a fee line."* **A named CE failure with its
  remedy cut as a cell is postulate (i) being applied, and I certify it as such.**
- **`R-h1` (iv) declares its own non-movers:** PREDICATE {LIVE, LIVE-other-grain, DARK} — cot needs
  nothing, 49F needs a cross-plane join, inf needs a source. **One remedy does not move all three, it
  is named, and `D1-h-v4` is the disclosed non-mover's render.** That is (iv)'s own test passing by
  declaring a failure, which is what the postulate asks for.
- **`R-h0`** CE is evaluated against the DECLARED layer (the stored 5-enum) with the exclusion named
  (Insurance, 4 of 5) rather than against internal consistency. Correct frame.
- **`R-h4`** is declared deliberately trivial. Recording a trivial postulate as trivial is better than
  omitting it; noted, not penalised.

## THE GRAIN FINDING IS THE RUN'S REAL WORK, AND I RE-DERIVED IT

COO's load-bearing catch: Andrew's Client L1 predicate lives on an **account**; the MDPF Client
substrate is a **(firm × date) residual** (`MDPF_ASSETS_WSA_CONTRACT.md:113-116`). **A per-account
predicate cannot partition a firm-level residual** — so the split is not a renderer change, and
`D1-h-c1..c3` exist because of that. **A decomp that had read the word as renderer-only would have
shipped a split with nothing to split.** Verified against the contract at the cited lines.

## P1 FINDING — `D1-h-r4`'s sizing rests on a TREE-SCOPED ZERO read as an ESTATE ABSENCE

**COO measured** (I7): `comp-find -i 'fixed income' data/mdpf` → **0 hits / 60 files**, and concluded in
the `r4` cell that Andrew's example *"Opal Fixed Income"* **is not a registry member**, so *"the L2 drill
today would enumerate three unserved blends and omit the one model he named,"* with the remedy being a
registry edit fed by his per-Partner composition rulesets.

**The zero reproduces exactly and is honestly framed by the tool itself** (`comp-find` printed *"a
MEASURED zero over 60 scanned file(s) in scope — not a claim the term is absent from the estate"*).
**I widened the scope, and the estate answers differently:**

| probe | result |
|---|---|
| `comp-find -i 'opal fixed income'` (estate-wide) | **HIT** — `data/assets/scripts/gold/build_dim_model_portfolio.py` |
| what that hit says (`:15-17`) | *"Live effect: `Opal Fixed Income` was wholly ABSENT from the served dimension, and Opal Conservative Growth read 96 accounts against the vendor's 98. That UNDERSTATED a client-facing AUA number."* — diagnosed `0.7.0_AE_CloudOps~Z` @`924c3b669` |
| negative control | `comp-find -i 'opal zzz nonexistent portfolio'` → NO HITS over 28,118 files (and it declared 13 UNREADABLE files, so even my zero is framed) |
| the other `data/` "fixed income" hits | generic asset-class strings (`'fixed_income': 'Fixed Income'`, a `'FIXED INCOME'` name-matching token) — correctly NOT model names |

**SO: `Opal Fixed Income` IS A REAL, LIVE OPAL MODEL** carried on the BD/assets-side model dimension —
the same `dim_model_portfolio` plane D3 names as the 49F/Inflection models source. **Andrew did not cite
a hypothetical; he cited a model whose absence from a served dimension was already a diagnosed,
client-facing AUA defect one tree over.**

**WHAT MUST CHANGE IN THE DECOMP (COO, `r4` only):** the cell's SURFACE is right and stays; its SIZING
and REMEDY line must stop reading as *"the model he named does not exist in our data."* The remedy is not
only *wait for the per-Partner rulesets* — **there is an existing in-estate authority to reconcile the
MDPF registry against**, and that reconciliation is precisely what surface (e) (`D1-e-1..e-3`,
producer-resolution) already owns. Cross-reference the two rather than leaving `r4` waiting on an input.

**WHY THIS IS P1 AND NOT DECOMP-INVALIDATING:** the surface was enumerated, the cell exists, an executor
would have gone to `r4` and looked. What was wrong is what the cell says the executor will find. **A
missing cell is a CE failure; a mis-sized cell is a correction.** My bar said I certify the enumeration,
not the sizing — this is the case that distinguishes them, and it would be dishonest to invalidate a run
for the finding my own bar pre-declared as non-invalidating.

**THE CLASS, stated because it is in CLAUDE.md verbatim and still caught a careful author:** *a 404 in
the wrong bucket is not evidence of absence — it is the wrong question asked cleanly.* The tool framed
its own zero correctly; the frame was lost when the number moved from the instrument into a conclusion.

## P2 — the three asks (`Q-h1`/`Q-h2`/`Q-h3`) are correctly NOT gates

Routed to CTO for Andrew, with executors building on the decomp's decision rules meanwhile. `Q-h3` in
particular — COO flagging that the third bucket's LABEL is theirs while its EXISTENCE is arithmetic — is
the right split: the arithmetic binds, the naming is sovereign.

## WHAT I DID NOT VERIFY (declared, so nobody reads this cert as wider than it is)

- **I did not re-run I5/I6/I8/I9/I10/I11.** I re-derived I7 (the one a conclusion rested on) and read the
  feeder contract at its cited lines. The other instruments' denominators are printed in-file and stand
  as COO's measurements, not as mine.
- **L-4 stands as COO declared it:** I8 is a TOKEN census, so inf's 0 hits is a measured zero over a
  token, not proof that no fee predicate exists there under another name — `D1-h-c2`'s first act is the
  census that discharges it. **This cert does not upgrade that zero.**
- **No render was exercised** (L-5): I11 reads page source. The renderer cells' oracles are exercise-shaped
  and fire at TO time, not here.

## WHAT COO SHOULD HAVE ASKED BUT DID NOT

**Whether the view tree's L0 presence predicate can ever disagree with the gold plane's five-peer
partition in a way a client would see.** `D1-h-p2` + `D1-inv-4` handle the *sum* (view plane =
`total_aua − Insurance`, and Insurance is 0 for every firm today, so the planes coincide **today**). The
unasked question is the **transition**: the day an insurance member is registered, the gold plane and the
view plane diverge by construction, and the only thing standing between that and a client-visible
discrepancy is a renderer that must not present the five-peer total as the L0 sum — stated in `p2` as an
instruction, but **no cell owns detecting the transition itself.** The INSURE program is actively
building the thing that will register that member (`ADVI_INSURE` s.11 #4 mints a Total Assets element at
L3/L4). **Two live projects, one shared trigger, and neither one's decomp names it as an edge to the
other.** Cheap to close now (a cell whose oracle asserts Insurance == 0 at emit and fails loudly the day
it is not); expensive to discover from a client-facing number later.

— `3.0.0_SA_CVO`
