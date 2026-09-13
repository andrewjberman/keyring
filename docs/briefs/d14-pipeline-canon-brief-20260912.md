# D14 "PLATFORM LOGIC" — THE PIPELINE CANON — STEP-1 BRIEF (v2)

**Author:** `4.0.0_SA_CRO~D` · **UTC:** v1 2026-09-12 ~17:5xZ (`@2659d45788`) · **v2 ~18:4xZ**
**Mode:** NEW (greenfield). No project exists under D14 yet; no Part 0.
**What changed v1 → v2:** the reference set now EXISTS. v1 described six outcomes and pointed at a
census; v2 points at seven landed artifacts in `infra/logic/` and cites each by hash.
⛔ **v2.1 CORRECTION (2026-09-13 ~00:5xZ): v2's headline "Part I is UNCHANGED — a finding" was FALSE**, and
`1.0.0_SA_CTO` measured it (96279: `git show` at both vintages, sections sliced, sha256 + unified diff, with a
control slice that differs). The SET is unchanged — six outcomes, same order, nothing added, retired or
renumbered. **The CONTENT is not: two outcomes each gained a value in an enumeration, which under Rule 24
is a schema change:** O3 CONFORMS / CONTRADICTS / OUT OF PLANE → **+ DERIVED FROM another project's row**;
O6 CONFORMANT / MIGRATE / RETIRE / DECLARED EXCEPTION → **+ AWAITING a named word**. Both values are already
USED by the artifacts (IRPT_FNTEND's four surfaces grade DERIVED; the ledger carries 10 AWAITING rows), so the
artifacts are right and the claim was wrong. The endpoint was re-cut on this at `ddf93b2165` (FWD-3 and FWD-6
ACCEPT lines re-tested; no id renumbered). Parts IV, V, VI, VII and REFS re-issued at v2; v2.1 joins the
row-state column and adds the routing re-derivation.
**Directive:** D14 "Platform Logic", minted `@ff4dfaf23e`, LAPTOP, members empty by design.
**Commissioned by:** Andrew-direct, this session — *"let's start with the census let's start breaking
this down"* → *"a brief that effectively becomes the principal priority project"* → *"Persist this
group of artifacts in a folder in ajb_workspace/infra/logic … a /loop that cycles every 10m to drive
the full creation of the necessary analysis, artifacts, and ultimately, /create-brief with tight
flow and structured refs to said artifacts"* (`845abef6c9` s.1).
**Consumer:** STEP 2, `1.0.0_SA_CTO` `/endpoint --forward`.
**Method authority for the rulings this brief carries:** key tensions settled with the CRO before the
brief, each as a rule or a range (`b65a7225a2` s.3 → `3fd386598f`).

⛔ **This brief authorizes no migration.** Every ruling it carries classifies; none moves a byte.
NEVER#3 stands. The ~16:1xZ pause on projects actively building data pipelines (`697a457a6d`)
stands until Andrew lifts it by name.

---

# PART I — THE OUTCOME TERRITORY (set unchanged from v1; O3 and O6 enumerations widened — see header)

Written as what a named kind of person can DO that they cannot do today. Each is qualitative and
disputable; no number is invented in this part. Step 2 cuts from here and nowhere else.

### O1 — A seat handed any pipeline tree answers "is this conformant, and against which rule" from one document

A seat — a worker, a COO lane, the CVO at L8 — is given a pipeline tree it has never seen. It opens
ONE document and can say for each of the five axes whether the tree conforms, departs, or is a
declared exception, **and cite the numbered rule**, without asking another seat. Every term in that
document carries the PLANE it binds on, so a rule about the storage-path segment `{scope}` cannot be
scored against an entitlement object's `scope_kind` (finding IV.7). `1.0.0_SA_CTO` named the failure
this ends: *"a canon whose correct reading requires three other documents is not yet a canon."*

### O2 — Andrew ticks product-vs-firm for every scope in the estate from one table, in one sitting

Every scope, enumerated by subtraction from the measured plane list — never from recall — sits in one
table with its evidence and the ruled default. Andrew reads one column and ticks. It is the mechanism
he approved for the residual of D10-1 (`e29a895ce3` card 3) and the per-instance form of his A-1 word
(*"I specify them on a per instance basis"*). The five scopes he already named arrive pre-ticked.

### O3 — A paused project's owner reads, row by row, what in their PRD the canon contradicts and what it does not — and resumes on that read

The owner of a paused project opens a contradiction report and sees, per planned data structure:
CONFORMS · CONTRADICTS rule N (the rule quoted) · OUT OF PLANE · DERIVED FROM another project's row.
The report is produced with a plane-aware instrument whose positive control is built from the real
shape (findings IV.7, IV.11). An empty CONTRADICTS column is the project's lift evidence; a non-empty
one is its amendment list. Either ends that project's pause — Andrew's stated reason for pausing.

### O4 — Anyone naming a firm anywhere reads the name from one registry rather than spelling it

A seat writing a route, a bucket name, an IAM condition, a key prefix or a Terraform module reads the
firm's key from ONE registry and references it. Today 49 Financial is `bd`, `49f`, `49financial` and
`opal-data-bd` across three planes (IV.4); SmartX put entity ids where a scope belongs (IV.3). Both
are the absence of this registry.

### O5 — An engineer onboards firm N+1 by executing one checklist end to end and reaches a served dashboard with no one-off

Andrew: *"we're going to have the same pattern over and over again as we take on more and more
firms."* One ordered checklist — mint the identity (O4), the buckets, the IAM, the pipelines in the
canonical grammar, the routes — and at the end a user of that firm sees their dashboard. Anything
requiring a judgment the canon has not made is a defect in the canon, not a step in the onboarding.
**This is the outcome the other five exist to make possible.**

### O6 — Every plane in the estate carries a disposition someone can act on

Every tier plane carries exactly one of CONFORMANT · MIGRATE (to where, under which rule) · RETIRE ·
DECLARED EXCEPTION (with the D10 PRD §6 schema) · AWAITING a named word. A migration project starts
from these rows rather than re-censusing. The register's failure mode is in its schema: an exception
list that only grows is how the pattern dies, so every conditional entry is auditable for expiry.

---

# PART II — WHERE THE BOUNDARY SITS (unchanged from v1, siblings re-verified)

**This project OWNS:** the canon (O1), the tick-list (O2), the contradiction reports (O3), the
identity registry as a contract (O4), the onboarding contract (O5), the ledger and register (O6).
All are documents, contracts and classifications. **It moves no data, repoints no trigger, edits no
bucket policy.**

**It RELIES ON, and does not own:** Rule 17/17a/17b (`docs/doctrine/CLAUDE_ANNEX.md`, 17b at
`dd9b33de65` — amendments are Andrew's, landed by `1.0.0_SA_CTO`); the census (`d35653da5e`);
Andrew's per-scope ticks.

| sibling | relationship |
|---|---|
| **The migration projects**, one per pipeline family (not yet minted; first = D10-2's *"first worked pipeline-family case"*) | CONSUMERS of O1/O4/O6. They move data; this project never does. Method: MAP → CLASSIFY → RULE → PORT → REPOINT → PROVE (D10 PRD §5). |
| `IRPT_BCKEND`, `IRPT_FNTEND` (D9, paused) | CONSUMERS of O3; their reports exist (REFS). |
| `MDPF_GLOBAL`, `MDPF_CANON` | MDPF_CANON's A-1..A-3 and B2 INHERITED as law; MDPF_GLOBAL's absorption question sits at `1.0.0_SA_CTO`. |
| `ETFS_CANON`, `ETFS_INGESTION`, `ETFS_POSITIONING` | the general-data case; conformant under T2 once X3 is declared. |
| `OPAL_CONSOLIDATION` (closed 08-25 on membership), `OPAL_ASSETS` | PRIOR ART; their §2b end-state is what O6 finishes. Not reopened. |
| `NFRA_OPSEC202609`, `NFRA_IAMROLES202609` (D12) | ADJACENT; O4 supplies the identifiers their IAM conditions scope on. |
| `ADVI_APISCP` | INHERITED for the serving route; storage clause FALSIFIED (IV.2); routing clause UNVERIFIED (VII). |
| **D10 "Partner Implementations"** | its 08-25 stance is THIS work under an older title; whether its canon content folds into D14 or D10 keeps the structural PRD is an open sovereign question MSTR wrote into D14's stance (96239). |

**Not this project's:** vendor egress; any apply; the Rule 17b text; the D14 register row; the pause lift.

---

# PART III — THE QUALITATIVE BAR (unchanged from v1)

- **O1** passes when a worker who has never seen the estate and the CVO at L8 reach the same rule
  citations from the same document — where today two seats reach different answers from different
  documents.
- **O2** passes when Andrew answers the D10-1 residual in one sitting from the table — where today the
  call has sat since 2026-08-25 because nobody put the cases in front of him.
- **O3** passes when a paused project's owner can point at the row that ended their pause — where
  today the pause has no per-project lift condition.
- **O4** passes when a seat asked "what is this firm called" reads the answer instead of choosing it.
- **O5** passes when onboarding a firm produces zero surprise rows naming a judgment the canon should
  have made — where today every firm has been a one-off, which is the sentence Andrew opened with.
- **O6** passes when a migration project starts from the ledger's rows rather than a fresh census —
  where today the July consolidation's disposition column was specified and never built.

---

# PART IV — THE SUBSTRATE: FINDINGS, EACH WITH WHAT WAS MEASURED

IV.1–IV.10 carry from v1 unchanged (`@2659d45788`); their short forms are kept so this part is
self-contained. IV.11–IV.13 are new.

**IV.1** The canon was already law, homeless and unenforceable by design (17b's own "not a warrant to
move anything"); the gap was an owner, a registered project and a ledger that can reach zero.
**IV.2** `ADVI_APISCP` §2's "never in a shared bucket" is false as current state: 34 of 4,361
firm-identifiable objects in `opal-data-portal-v2`, 13 written 2026-09-12; exposure not claimed.
**IV.3** SmartX minted 12,432 planes with entity UUIDs in the scope segment — ruled a VIOLATION.
**IV.4** 49 Financial: four spellings, tiers split across two buckets.
**IV.5** The "legacy" buckets are the live estate; platinum lives in six buckets; the 16:0xZ ruling
ratified the majority.
**IV.6** Format law violated both ways, live; a transition started and not finished.
**IV.7** `scope` is two words on two planes; a term join false-positives (COO~F 96202).
**IV.8** Two census instruments disagreed; a capped sweep truncates the alphabet.
**IV.9** Prior rulings inherited as law, not re-derived (list unchanged; now cited from `02_DOCTRINE.md`).
**IV.10** A stale ACTIVE HOLD names a key that 404s; the artifact moved, the record did not.

### IV.11 — A positive control built from a chosen string passed for the wrong reason, twice in one day
`2.0.0_SA_COO~F` retracted its S51 measurement (96267): the detector was `\b`-anchored, `_` is a word
character, so `\bbucket\b` cannot match `storage_bucket` — and its positive control fired on a bucket
NAME in a comment, never on a field. True figure: **4 surfaces in 3 of 14 files**, not 0. Earlier the
same afternoon `0.0.0_AB_MSTR`'s owned-paths control returned rc=0 on all three cases because the file
list was passed in a variable the hook does not read (96265). **Finding:** an O3 instrument's positive
control must be built from the file's own naming convention, never from a string the author chose;
and a `\b`-anchored census over snake_case is blind to compound names and must say so. Carried into
`02_DOCTRINE.md` §0 for v0.2.

### IV.12 — The contradiction reports exist, and the paused projects' distance from the canon is short
`IRPT_BCKEND` (13 planned surfaces): **3 CONTRADICTS**, each with a one-sentence fix or an exception
path — a missing `platinum/` prefix (R1); no gold parquet artifact between silver and the served JSON
for derived client data (R11+R14 — the design already exists in `1.0.0_SA_CTO`'s accrual spec, home
ruled by T1); vendor PDFs in a new bucket rather than assets bronze (R4-partial). 3 CONFORMS, 4 OUT OF
PLANE, 2 UNDETERMINED, 2 doctrine GAPS surfaced (transactional state; Lambda artifacts vs R16).
`IRPT_FNTEND` (v0.2): 4 surfaces whose grade is DERIVED from BCKEND's rows; one serving-route question
routed. **Finding:** nothing either project planned is *architecturally* against the canon.

### IV.13 — The ledger's shape: where the estate's debt actually sits
`06_CONFORMANCE_LEDGER.md` §7: 27 CONFORMANT · 14 MIGRATE-home (every one LIVE and daily) · 6
MIGRATE-format · 3 MIGRATE-grammar · 13 RETIRE · 2 exceptions granted + 3 owed · 9 AWAITING a word.
**Finding:** the largest item by consequence is D10-2 (the three legacy buckets carry the live serving
load; five rows cannot close until Andrew names the surviving bucket per firm); the largest by count is
SmartX (12,432 planes, one design decision). The debt is concentrated, not diffuse.

---

# PART V — WHAT MUST BE TRUE (named, NOT sequenced — sequencing is step 5)

- O2, O3 and O6 read the canon (O1); it exists at v0.1 and is prior art the PRD absorbs or re-cuts.
- O5 reads O4; the registry seed exists; its RUNTIME (table, YAML, TF data source) is an L4/L7 choice.
- O3's instrument is plane-aware AND its positive control is built from the real shape (IV.7, IV.11).
- Every exception entry states PERMANENT or CONDITIONAL; three are OWED (X2, X3, X5) and the ledger
  says so rather than granting them.
- The D10-1 ticks are Andrew's (16 rows); the ledger's 9 AWAITING rows close on his words (D10-2 ×5,
  demo ×2, imo, MDPF gold home). Nothing here derives them.
- Two doctrine GAPS need a ruling before O1 is v1.0: GAP-1 transactional/workflow state (no tier, no
  rule); GAP-2 Lambda artifacts vs R16.
- The D10 (a)/(b) register question is Andrew's; it decides which file Rule 17b's dead citation names.
- The Rule 17b text stays `1.0.0_SA_CTO`'s to land and Andrew's to amend; the canon cites it.
- Andrew's word, by name, lifts the pause; O3 produces the evidence, not the lift. **The row-state
  column of both O3 reports waits on `3.0.0_SA_CVO`'s compile** (accepted 96257); until it lands the
  reports read "as the PRD reads," not "as the project decided."

---

# PART VI — STATUS · ⛔ NOT OUTCOME-BEARING · measured 2026-09-12, clocks per line

- Pause: IN EFFECT since ~16:1xZ; every live seat HELD or on a declared read; IRPT_FNTEND round 4 cut
  with four orders at pending and zero workers; IRPT_BCKEND 10 of 12, frozen.
- `infra/logic/` exists in HEAD (9 files); lane `PLATFORM_LOGIC_DOCS` granted `@df27878bfe` (~18:32Z);
  the override Andrew authorized at ~18:1xZ was used for five commits (one audit line each) and is
  retired from `45160b1525` on.
- The 10-minute loop is ARMED (job `ccae4f94`); this brief is its row #14; it stops itself on this
  commit. A successor re-arms only off `ANDREW_DIRECT_20260912_180xZ_…_LOOP_ARMED.md`.
- Rule 17b amended `dd9b33de65`; its dead citation deliberately left for the D10 (a)/(b) answer.
- All CRO commits this session LOCAL; origin/CLOUD `6ced337f86` at the last ls-remote (~18:4xZ).

---

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

- ~~The O3 row-state column is empty.~~ **JOINED at v2.1** from `3.0.0_SA_CVO`'s compile `@ac907356c8`
  (re-derived exact by `1.0.0_SA_CTO`): IRPT_BCKEND 188 rows / **71** dispositioned (not 188 — the CVO
  corrected its own offer), 28 storage-plane rows of which **15 are undispositioned**; IRPT_FNTEND 138 rows /
  41 dispositioned, **2** touch the four surfaces, both undispositioned. Denominators are perishable
  (shared append-only channels).
- ~~The ADVI routing clause is unverified~~ **RE-DERIVED at v2.1 on the applied plane**
  (`infra/logic/07_ROUTING_REDERIVATION.md`): TRUE for every scoped S3 path class but `platinum/advi/{firm}/`,
  which the deployed router routes to the shared bucket **by ruled design** (LD-0442) — a collision with R6/R7
  that Andrew's ruling resolves in the security-positive direction. Not exercised through CloudFront; read from
  associations and bytes.
- **No producer was traced to any plane;** liveness is `LastModified`. No RETIRE was checked for a live
  reader (`comp-blast` not run).
- **The two SmartX subtrees are characterized, not counted per plane.**
- **`platinum/advi/49financial/*` residue is INFERRED dead;** its producer was not traced.
- **The stale hold's successor key is INFERRED** from basename; contents not diffed.
- **Whether a SITEZ-placed row can be worked from this fabric is UNRESOLVED** — moot for D14.
- **Code-level firm spellings** (`FIRM_BUCKET_MAP`, roles.ts, IAM conditions) were not censused; the
  identity spine will gain aliases.
- **No D10-1 tick is assumed** beyond the five Andrew named on 2026-08-25.
- **The IRPT_FNTEND measurement has been wrong once;** its corrected figure carries controls a third
  party can re-run, and that is the only claim made for it.

---

## REFS TO CARRY — structured, one line per artifact, cited by hash

```
  BRIEF PATH        docs/briefs/d14-pipeline-canon-brief-20260912.md   (this file; v1 @2659d45788)
  DIRECTIVE         D14 "Platform Logic"  @ff4dfaf23e (+@b0bc31483c verbatim repair)  LAPTOP
  PROJECT           NONE-YET  (D14 members empty by design; L3 is 1.0.0_SA_CTO's)
  EXISTING PRD      NONE for this project

  THE REFERENCE SET  infra/logic/   lane PLATFORM_LOGIC_DOCS @df27878bfe
    README.md                        what/why, rulings by hash, how driven         @845abef6c9
    ORDER_OF_OPERATIONS.md           compile sequence, status column, loop §F      @845abef6c9 .. @5288666762
    01_CENSUS.md            (Part 1)  36 buckets, every plane, two instruments      @d35653da5e (moved @845abef6c9)
    02_DOCTRINE.md          (O1)      20 rules R1-R20, five axes, plane-tagged §1,  @e729fd6f30
                                      register schema §4, not-ruled §6
    03_CONTRADICTION_REPORTS/IRPT_BCKEND.md  (O3)  13 surfaces, 3 CONTRADICTS      @51cbf75cca
    03_CONTRADICTION_REPORTS/IRPT_FNTEND.md  (O3)  v0.2 regraded, 4 surfaces        @5288666762
    04_SCOPE_TICKLIST.md    (O2)      19 rows by subtraction, 16 to tick            @54a764cb28
    05_IDENTITY_SPINE.md    (O4 seed) 4 firms / 3 products / 8 vendors / 2 masters  @45160b1525
    06_CONFORMANCE_LEDGER.md (O6)     every plane's disposition + register X1-X6    @4faf061126 (+ v2.1 platinum/advi correction)
    07_ROUTING_REDERIVATION.md        the ADVI routing clause on the APPLIED plane  (v2.1)
  ROW-STATE INPUT   org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ROW_STATE_COMPILE_FOR_LOGIC_ROW8_20260912.md @ac907356c8
  ENDPOINT          ENDPOINT_FWD_D14_PIPELINE_CANON_20260912.md @ddf93b2165 (re-cut on the Part I correction)

  RULINGS CARRIED   e29a895ce3 (client platinum per-firm; gold parquet; D10-1 default; D10-2 deferred)
                    697a457a6d (the pause)  ·  ed3f6b32e4 + 392052b751 (scope law; 2x2 grid; A-1 supersession)
                    b65a7225a2 + a359f4df03 (D14; tensions-first; naming corrections)
                    3fd386598f (five tensions + grid restatement)  ·  6b7f491747 ("Platform Logic")
                    845abef6c9 (the folder + loop authority; override s.2a; override's end s.2b)
                    dd9b33de65 (Rule 17b amended, 1.0.0_SA_CTO)
                    ANDREW_DIRECT_20260825_1755Z · ANDREW_DIRECT_20260826_1810Z (D10-2 folded, D10-3 deferred)
  INHERITED LAW     docs/architecture/D10_GLOBAL_PIPELINE_STRUCTURE_PRD.md §2 §5 §6
                    docs/architecture/MDPF_CANON_PRD.md §1 (A-1..A-3), row B2
                    docs/architecture/OPAL_ASSETS_CONSOLIDATION_PRD.md §2, §2b
                    docs/doctrine/CLAUDE_ANNEX.md Rules 17 / 17a / 17b
  SIBLING PROJECTS  the migration projects (one per pipeline family, not yet minted) · IRPT_BCKEND ·
                    IRPT_FNTEND · MDPF_GLOBAL · MDPF_CANON · ETFS_CANON · ETFS_INGESTION ·
                    ETFS_POSITIONING · OPAL_CONSOLIDATION (closed) · NFRA_OPSEC202609 ·
                    NFRA_IAMROLES202609 · ADVI_APISCP · D10 "Partner Implementations" (the (a)/(b) question)
  WAITING-ON        3.0.0_SA_CVO row-state compile (96257, since 18:2xZ) -> O3 reports v2.1
                    Andrew: 16 ticks (04_SCOPE_TICKLIST.md); 9 ledger words; GAP-1, GAP-2; D10 (a)/(b)
  MEASURED AT       census 2026-09-12 ~16:3xZ UTC; Part VI clocks per line
```

**Author:** 4.0.0_SA_CRO (Chief Research Officer) · **Home:** org/tier1_exec/4.0.0_SA_CRO/
