# ADVI gold, redesigned to the LGIC canon — L1 BRIEF

generated: 2026-09-15
author: 4.0.0_SA_CRO (Chief Research Officer), home org/tier1_exec/4.0.0_SA_CRO/
proposed_project: NONE-YET. The code is assigned by `1.0.0_SA_CTO` at L3; `ADVI_GLDLGIC` is offered as a candidate only.
placement: proposed D8 / ADVI / laptop, where the ADVI macro and ADVI_FIRMBKTS already live. The directive and the
SEQUENCE placement are `1.0.0_SA_CTO`'s calls and are NOT made here.
status: L1 BRIEF (new). No endpoint, no PRD, no task order.

**Commission, as relayed to this seat.** `0.0.0_AB_MSTR` msg 97110 relays `1.0.0_SA_CTO`'s disposition (msg 97097,
/open-calls card 3) of Andrew's word at the CTO terminal, ~14:2xZ 2026-09-15:

> "recs approved aand all future pipelines must abide by lgic structures patterns"

What that approval covers:
- An ADVI GOLD REDESIGN as **its own project, not folded into ADVI_FIRMBKTS**.
- ADVI's gold, redesigned under the LGIC doctrine (`infra/logic/02_DOCTRINE.md` R1–R21) and addressed by
  `lib/opal_naming.py`'s `key()`, `address()` and `name()`.
- It is Andrew's named use case, *"a decent amount of gold work/redesign for ADVI"* (quoted as relayed in 97110; see
  Part VII).
- The standing rule behind it is CLAUDE.md **Rule 30**: every new pipeline gets its homes, tenancy and names from the
  canon and its builders, never from a seat's judgment.

---

## PART I — THE OUTCOME TERRITORY

Each outcome is one thing a named kind of person can do once this is done.

### O1 — An engineer changes an ADVI gold table once, and every firm's gold carries the change

An engineer who adds or corrects an ADVI gold table does it in one place, and every firm that runs ADVI picks it up.
Today the same job exists as a separate copy per firm (Part IV.1). A fix to one firm's copy leaves the others as they
were, and nothing says so.

### O2 — An engineer brings a new firm's ADVI gold online from registry rows and configuration, with no hand-typed path or name

Adding firm N+1 to ADVI gold means:
- adding its identity-registry rows (`infra/logic/registry/`);
- giving it configuration.

Every storage address comes from `address()`, every key from `key()` and every resource name from `name()`. When a
builder refuses, the fix is the missing registry row, never a typed workaround (Rule 30). No firm-specific copy of the
code is made.

### O3 — An analyst reads any ADVI gold table as typed parquet with its full dated history, in the firm's own bucket

Anyone answering a question from ADVI gold opens a parquet table, typed at its boundary, that holds the full history
available, with one row added per day. This is the form Andrew ruled (R11). They find it in that firm's bucket (R5,
R7) and never have to reconstruct it from a served JSON file.

### O4 — An operator names the one producer of any served ADVI file, and it reads gold, never writes gold

For any file a portal page reads from ADVI, an operator can say which single publisher writes it. That publisher reads
gold parquet and writes the served JSON. Gold never doubles as the served file, and no second writer exists (R12).
Per-page shaping, display names and route shapes live in the publisher, not in gold.

### O5 — An operator can say where any ADVI gold job runs and why, and find its code in one place beside its gold

For each ADVI gold job, an operator can say:
- whether it runs as a Lambda pulled from silver or on EC2;
- what makes it heavy enough for EC2, where it does (R13);
- where its one deployed code home is, in the same bucket as the gold it writes (R16).

### O6 — An operator opens an ADVI gold plane and finds only gold

Run state is not in the gold plane: watermarks, manifests, parity records, leases and intake all live under `state/`
for the tenancy they belong to (R21). Backups and scratch are outside the tier grammar, dated, with an expiry (R17).

### O7 — An advisor notices nothing on their pages unless a change was announced

After each part of the redesign lands, every figure an advisor or firm user reads on an ADVI surface is what it was
before, unless a difference was authorized and announced. There is no side-by-side old and new pipeline and no
double-write (R18). Every served file that moves carries a never-widen sign-off.

### O8 — Andrew can see every place ADVI gold departs from the canon, and why

Any deliberate departure from R1–R21 in ADVI gold is an exception-register entry he acknowledged, marked PERMANENT or
CONDITIONAL (R20). An undeclared departure is a finding someone can act on, not a quiet habit.

---

## PART II — WHERE THE BOUNDARY SITS

**This project OWNS how ADVI gold is PRODUCED from now on:**
- the per-firm gold jobs and their shared implementation;
- the gold table set, its grain and its format;
- the split between gold and the publisher for ADVI's served files;
- compute placement and code homes;
- removing run state from ADVI gold planes;
- builder-derived names and addresses for everything it creates.

**It RELIES ON, and does not own:**

| Sibling | What it owns | The seam |
|---|---|---|
| `ADVI_FIRMBKTS` (D8, PRD v1.2 RATIFIED) | Moving the EXISTING bytes out of the three legacy buckets (`opal-data-bd`, `-inf`, `-cot`) into the spelled-out firm buckets. That includes the source-first re-fold of existing keys and the JSON-to-parquet conversion on the way ("Analytical files become gold parquet", `ADVI_FIRMBKTS_PRD.md:175`). It also owns minting `opal-data-inflection` and `-cottonwood`, their serving grants and fence, the tenant assertion, and retiring the legacy buckets on proof. | FIRMBKTS decides where the bytes that exist today go. This project decides what writes gold from now on. Where both touch one served file, the move and the reshape are one act (R18). Part V names that dependency; sequencing it is step 5's job. |
| `LGIC_CANON` (D14) | The canon and doctrine: it classifies and never moves anything (R19). | This project is one of the per-family conformance projects R19 calls for. |
| `LGIC_NAMING` (D14) | The naming schema (`org/standards/NAMING_SCHEMA.json`) and the grading rule. | Names come from the schema. This project mints no naming rule. |
| `LGIC_ENFORCE` (D14) | The identity registry rows, the builders and `grade()`, and the fence. | A missing ADVI row is added through LGIC_ENFORCE's registry, not invented here. |
| `MDPF_CANON`, `MDPF_TAXSMA` (D8) | MDPF's product-shaped gold, and Tax SMA's use of 49F's canonical valuation (`b00_canonical_valuation`) as the basis for Tax SMA values. | The b00 canonical valuation contract that MDPF_TAXSMA consumes must survive this project unchanged, or change only through its owner. |
| The portal's ADVI pages and their route owners | The URLs callers use. | Served URLs are preserved (the CANON DEC-5 precedent). The publisher changes behind the route, not the route itself. |

**EXCLUDED:**
- Bronze and silver. They have their own homes and laws (R4, R9, R10) and their own projects.
- Gold for MDPF, ETFs, Tax SMA, Find, IMO and Investor Reporting.
- Conformance of any non-ADVI pipeline. Each gets its own migration project (R19); none rides on this one.
- The legacy buckets' retirement, which stays with ADVI_FIRMBKTS.
- Any change to what a figure means, as opposed to where and how it is produced.

---

## PART III — THE QUALITATIVE BAR

- An engineer asked to add one gold table for every ADVI firm edits one place, and each firm's gold carries the new
  table after its next run, with no per-firm copy to remember.
- A firm added to ADVI gets its gold from registry rows and configuration. A reviewer looking for a hand-typed bucket,
  key or resource name finds none.
- An analyst answering "what was this account worth on a past date" reads it from a gold parquet history, not from a
  served JSON file or a backup copy.
- Anyone asking "who writes this served ADVI file" gets exactly one producer, and that producer reads parquet.
- An advisor using their pages across the redesign cannot tell it happened, except where a change was announced to
  them.
- Andrew, asked to acknowledge an ADVI departure from the canon, is shown it as a register entry with its reason and
  expiry. It is never discovered after the fact.

---

## PART IV — THE SUBSTRATE: WHAT EXISTS, MEASURED

1. **ADVI gold is several parallel per-firm implementations of one job.** A filename census of the repository,
   2026-09-15 ~14:5xZ, excluding tests, `__init__.py` and `__pycache__`:
   - **The runner families.**
     - `data/assets/scripts/gold/runners_49f` has 73 files, `data/inf/scripts/gold/runners_inf` 21 and
       `data/cot/scripts/gold/runners_cot` 25.
     - **15 filenames are identical in all three**: the canonical `a00`–`c01` series, from `a00_dim_account.py`
       through `b00_canonical_valuation.py` and `c00_flow_ledger.py`.
     - 56 of 49F's 73 appear in neither of the other two.
   - **The per-firm series.**
     - `data/black_diamond/scripts/gold` has 68 files, `data/cot/scripts/gold` 43 and `data/inf/scripts/gold` 54.
     - **39 filenames are shared between the BD and COT series** (`A_00.accounts_dimension.py`,
       `B_00.canonical_holdings.py`, and more).
     - The INF series uses its own naming, with 0 stem overlap with BD.
   - **The gold census as a whole:** 384 non-test gold scripts across 17 subtrees. The ADVI families above, plus
     their `lib`/`_lib` folders (21 inf, 15 bd, 13 cot, and 3 each of bd `_lib` and cot `_lib`), make up most of it.
2. **Much of ADVI's gold is still JSON.** The R11 census in `02_DOCTRINE.md:217-220`, and the conformance ledger
   `infra/logic/06_CONFORMANCE_LEDGER.md` `:69`, `:79`, `:87` and `:91`, at its v0.3 vintage:

   | Bucket | Gold JSON | Gold parquet |
   |---|---|---|
   | `opal-data-bd/gold/` | 44,782 | 26,809 |
   | `opal-data-cot/gold/` | 2,856 | 789 |
   | `opal-data-49financial/gold/` | 8,859 | 16,067 |
   | `opal-data-inf/gold/` | 221 left to convert | 17,161 of 22,836 objects already parquet |

   The ledger calls the served JSON under `gold/` **"platinum by function"** (R12, `:69`).
3. **The compute is EC2 today.** `infra/aws/ec2/` carries `bd-gold-layer-runner`, `inf-gold-layer-runner`,
   `consolidation-gold-runner`, `canonical-schwab-runner`, `bd-gold-detail-generator`, and gold QA runners for bd and
   inf. R13 leaves the existing EC2 gold runners **UNCLASSIFIED**, because Andrew deferred the "heavy" threshold until
   the first genuinely heavy case (`02_DOCTRINE.md:239-246`).
4. **Run state sits inside gold planes.** R21's census (`02_DOCTRINE.md:328-330`) lists these as VIOLATED-LIVE in
   bd, inf and cot:
   - `gold/_state/`, `gold/_parity/`, `gold/meta/*_watermark.json` and `gold/manifests/`;
   - `otp/state.json` and `blackdiamond/{49f,cot}/session-trigger-mode.json`.
5. **The builders exist and are the addressing contract.** In `lib/opal_naming.py`:
   - `key()` at `:1287` builds exactly `{source}/{scope}/{tier}/{table}/{partition}`;
   - `address()` at `:1303` places the bucket by the scope's tenancy (`tiers.json`);
   - `name()` at `:1334` builds `{system}-{scope}-{function}[-{qualifier}]-{kind}`;
   - `grade()` at `:1236` grades a name.
   The registry is in `infra/logic/registry/`: scopes, systems, tiers, exemptions and remediations.
6. **ADVI gold's home has already been ruled twice.** The 2026-08-18 client-gold-bucket supersession
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260818_CLIENT_GOLD_BUCKET_SUPERSESSION.md`) set the
   per-client bucket. The source-first key string then put ADVI gold under `advi/{firm}/gold/…` in the firm bucket
   (LGIC_NAMING S1; ledger `:91`, "re-folds to `advi/49financial/gold/`"). The home is decided. What is produced there
   is this project's question.
7. **A shared contract crosses into another project.** `runners_49f/b00_canonical_valuation.py`, with basis
   `dim_balance.net_mv_plus_cash`, is reused as-is by MDPF_TAXSMA; its admitted PRD's CONTRACTS table says so. Any
   redesign of b00 has a consumer outside ADVI.
8. **Earlier ADVI gold work exists by name.** `ADVI_GLDOPS` had task orders `.004` (a canonical holdings stack) and
   `.005` (bulk-vectorizing gold scripts), and `ADVI_GLDRST` appears in the flat registry. Neither was read for this
   brief; they are carried as places to look, not as findings.

---

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, NOT sequenced. Sequencing belongs to step 5.

- **Registry rows.** The identity registry carries ADVI's system, the ADVI firm scopes and their tier rules, so the
  builders place every ADVI address and name without refusing. The rows are LGIC_ENFORCE's.
- **Destination buckets.** The firm buckets ADVI gold writes into exist with their serving grants, fence and tenant
  assertion. `opal-data-inflection` and `opal-data-cottonwood` are minted by ADVI_FIRMBKTS.
- **One act per served file.** For any served file both projects touch, ADVI_FIRMBKTS's port and this project's new
  producer form a single act, with one never-widen sign-off (R18).
- **The heavy threshold.** Andrew's R13 threshold, if any ADVI gold job is to stay on EC2. It is his to set and is
  deferred today.
- **Caller URLs.** Every portal route that reads ADVI files is known, so their URLs can be preserved.
- **Register entries.** An R20 entry for each departure ADVI gold keeps on purpose.
- **Tax SMA's contract.** The b00 canonical valuation contract MDPF_TAXSMA depends on is preserved or amended by its
  owner.

---

## PART VI — STATUS (NOT OUTCOME-BEARING)

This part is a snapshot and is not to be cut into outcomes.

- 2026-09-15 ~14:5xZ, repository at HEAD: the filename census in IV.1 and the EC2 homes in IV.3.
- Conformance ledger v0.3 (`06_CONFORMANCE_LEDGER.md`) and doctrine R-census (`02_DOCTRINE.md`), read at HEAD
  2026-09-15. Their object counts carry the ledger's own vintage (planes read 2026-09-12/13); they were not re-counted
  here.
- ADVI_FIRMBKTS: PRD v1.2 RATIFIED; in `org/missions/SEQUENCE.yaml` it is stage 2, HELD at DECOMP (its PRD, lines
  24–29).
- Rule 30 was landed in CLAUDE.md by `1.0.0_SA_CTO` on 2026-09-15.
- All the laptop COO seats are occupied (`2.0.0_SA_COO~G` LGIC, `~O` NFRA_OPLGTW, `~T` MDPF_TAXSMA, per 97110). The
  L5 seat is a later capacity question.

---

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

- **Filename overlap is not content equality.** The duplication in IV.1 is measured by filename and stem. It is not a
  diff: two copies with the same name may have diverged, and that divergence is the risk O1 addresses, not a measured
  fact.
- **No table-grain catalog.** There is no per-table grain or schema list, and no count of how many distinct gold
  tables ADVI serves. That is the project's MAP step (R19).
- **No consumer trace.** Which portal pages and routes read which ADVI files, and whether every served file has
  exactly one producer today, were not measured. R12's one-producer census is itself UNMEASURED in the doctrine.
- **No deployed-bytes check.** Which runner copies are deployed and scheduled today was not read; IV.3 lists EC2 homes
  in source only.
- **The commission is relayed.** Andrew's *"a decent amount of gold work/redesign for ADVI"* is quoted as relayed in
  97110. The body of msg 97097 was not available in any inbox copy. Its broker record, subject "ANDREW APPROVED: …
  ADVI gold", confirms it exists and that `0.0.0_AB_MSTR` read it.
- **Earlier ADVI gold projects were not read.** ADVI_GLDOPS and ADVI_GLDRST are named in IV.8 only.
- **Proposals only.** The directive placement, the project code and any SEQUENCE position are proposals.
- **No numbers are invented.** Part III is qualitative by design.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/d8-advi-gold-redesign-lgic-brief-20260915.md
  PROJECT           NONE-YET (candidate ADVI_GLDLGIC; 1.0.0_SA_CTO assigns at L3)
  EXISTING PRD      NONE
  COMMISSION        Andrew-direct ~14:2xZ 2026-09-15 via 1.0.0_SA_CTO 97097 (card 3), relayed by 0.0.0_AB_MSTR 97110;
                    CLAUDE.md Rule 30
  SIBLING PROJECTS  ADVI_FIRMBKTS (org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md v1.2);
                    LGIC_CANON, LGIC_NAMING, LGIC_ENFORCE (D14); MDPF_CANON, MDPF_TAXSMA (D8)
  CANON             infra/logic/02_DOCTRINE.md R1-R21; infra/logic/06_CONFORMANCE_LEDGER.md v0.3;
                    org/standards/NAMING_SCHEMA.json; infra/logic/registry/
  BUILDERS          lib/opal_naming.py key() :1287, address() :1303, name() :1334, grade() :1236
  PRIOR ART         the runner families data/{assets,inf,cot}/scripts/gold/runners_*; the series
                    data/{black_diamond,cot,inf}/scripts/gold; infra/aws/ec2/{bd,inf}-gold-layer-runner,
                    consolidation-gold-runner, canonical-schwab-runner; ANDREW_DIRECT_20260818_CLIENT_GOLD_BUCKET_SUPERSESSION.md;
                    ADVI_GLDOPS / ADVI_GLDRST (not read)
  MEASURED AT       2026-09-15 ~14:5xZ (repository census); the ledger and doctrine counts carry their own vintages
```
