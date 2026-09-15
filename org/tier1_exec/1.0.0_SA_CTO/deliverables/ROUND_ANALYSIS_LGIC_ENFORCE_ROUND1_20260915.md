# ROUND-1 ANALYSIS -- LGIC_ENFORCE

**Seat:** 1.0.0_SA_CTO. **Stamp:** 2026-09-15 ~16:1xZ.

**Inputs:**
- 3.0.0_SA_CVO's slug, msg 97135: `ADJUDICATION_v1.md` @`43ad6e9b2b` (C-S1..C-S15), `REMEDIATION_v1.md` @`7748cc5df7` (44
  rows), step log @`2c2533a66d`.
- 2.0.0_SA_COO~G's drain-end read, msg 97047. It was sent to this seat only, and re-sent to the CVO as 97124.
- This seat's own tally of all 22 proof instances at HEAD.

**Round 1 delivered:**
- 22 of 22 orders terminal: 19 complete, and 3 pending with VALID proofs (under 96806).
- 73 rows, 0 without a carrier: 29 dismissed and 44 graduated.
- The fence is live on `opal-data-49financial`.

## 1. THE OUTCOMES -- graded here, against their own text (PRD :62-141), from the proof instances

| outcome | grade | evidence | disposition |
|---|---|---|---|
| FWD-1 a pipeline asks for its address | **REALIZED** | EN-d-1 6 of 6 and EN-d-2 2 of 2: a new pipeline, and a second worker's search that finds 0 storage literals, with a positive control of 1. The checker's d2-control read the worker's own field (W8-S3), but the CVO re-ran the plant with its own regex, and the control holds | instrument fix (s.3, cell 4) |
| FWD-2 a name is produced; the separation rule comes from the same source | **NOT REALIZED** | EN-m-1 3 of 3, and EN-x-1 X1-AC1 and X1-AC2 PASS, but X1-AC3 FAILS: one change does not move both, because the short form has two carriers (W1-S19) | RULING ONE (s.2) |
| FWD-3 one list for where a firm's data lives | **REALIZED on its ACCEPT's own denominator** | the eight DEC-5 definitions are generated from the registry. EN-v-2 to EN-v-6 read DELTA=0. EN-v-1's V1-AC3 is re-graded by DELTA under RULING RED (s.2): the 14 failing tests are the base's. **Qualified:** 12,917 literal firm carriers elsewhere stay hand-kept (W1-S1); they are FWD-5's population and each pipeline's own migration (R19), and Rule 30 stops new ones | the grade names its scope |
| FWD-4 a wrong name is stopped with the right form printed | **NOT REALIZED** | EN-t-1 3 of 3 and EN-t-2 3 of 3 grade LITERAL names only (C-S12). And the limbs as built would refuse EXISTING names at apply, and a machine-written plan file at commit (C-S8), which FWD-4's own ACCEPT forbids: "an old spelling that is still permitted goes through ... so existing work keeps running" | RULINGS ADD and PLAN (s.2) |
| FWD-5 the whole-estate ranked list | **NOT REALIZED** | EN-s-1 S1-AC1 and S1-AC2 FAIL: the census stops at the 4th live name on a RAISE, because 504 of 1,805 live and 623 of 1,869 repo names raise across 115 unresolved system tokens. S2-J1 passes on its letter over 3 names | RULING ROWS (s.2) |
| FWD-6 a clean-up cannot stall | **REALIZED** | EN-p-1 4 of 4 on a practice copy with a planted row | none |
| FWD-7 a new firm is one entry | **NOT REALIZED** | a firm added as one registry row still draws a WARN that it is not in the schema's `firm_forms` (W8-S2): the same second list as FWD-2 | RULING ONE (s.2) |

**3 of 7 REALIZED.** Round 2 is needed.

## 2. RULINGS

**RULING ONE -- FWD-2 and FWD-7 mean ONE carrier (C-S6).**
- Both ACCEPT lines promise that one change moves everything: "changing how a firm is spelled changes both at once",
  and "one entry in one list". Two carriers kept consistent by a validator are two hand edits, not one change.
- **The identity registry (`infra/logic/registry/scopes.json`) is the ONE home of a firm's forms.** The schema's
  `firm_forms` is removed, and every reader reads the registry: `lib/opal_naming.py` `:248`, `:287-288`, `validate` and
  `grade()`.
- The schema's text says instead that a firm's forms are the registry's rows. That is NAMING_SCHEMA **v1.9**, which this
  seat writes when the recut lands the code, in the same commit, so the data and its readers never disagree.
- `opal_name.tftest.hcl`'s 32 hand-listed run blocks (W1-S12) are GENERATED from the registry's vectors.
- **DEC-1 (W1-S8):** DEC-1 lists the REQUIRED fields of a scope row. A further field is legal only if a generator or
  `validate` reads it; a field nothing reads is removed.

**RULING ADD -- the naming limbs refuse only what a change ADDS (C-S8; the G-F prerequisite).**
- PRD DEC-6 and FWD-4's ACCEPT already say this: refuse a NEW hand-kept name, warn on an EXISTING one.
- **Apply limb:** it has no diff, so it reads the plan's create and rename actions. A resource being CREATED with a name
  the builder would not produce is refused, with the canonical form printed. An existing resource WARNs.
- **Commit limb:** grades the names a change adds to AUTHORED files. A machine-written `terraform show -json` is an
  artifact, not an authored name, and is not graded at commit.
- **G-F** (the live REFUSE flip, `LGIC_ENFORCE_DECOMP.md:399`) keeps its window and its 200-string floor. It flips ONLY
  when the 78 roots read 0 refusals of existing resources with the switch on.

**RULING PLAN -- names built by expressions are graded at plan time (C-S12).**
- The pre-plan limb keeps grading literals. It prints "N expressions deferred to plan", and never passes them silently.
- A plan-time limb grades the EVALUATED names of the resources being created. It is the same plan read as RULING ADD.
- Together the two limbs cover every name FWD-4 promises to stop.

**RULING ROWS -- the 115 unresolved system tokens are classified by subtraction, then the census re-runs to the end
(C-S5).**
- Each token goes into exactly one class, with its count printed:
  - (a) a system that owes a registry row (VENDOR, PRODUCT, or a PLATFORM_SUBSYSTEM such as `gateway`);
  - (b) a workstream or project code, which is never a system (S6);
  - (c) a library (R1.e);
  - (d) a rule gap, which stays a loud RAISE.
- Class (a) rows are ADDED under CLAUDE.md Rule 30. `systems.json`'s own 17 "unresolved" tokens are inside the 115.
- A token whose class the registry owner cannot decide comes to this seat as a list, not to Andrew.
- The census then judges every nameable name, and EN-s-2 compares a REAL population.
- The same rows fill LGIC_NAMING FWD-5's `{system}` placeholders. That analysis orders its re-grade after this cell.

**RULING RED -- a consumer-suite criterion grades the DELTA (W4-S1).**
- It states the base's failing set and passes on NO NEW failure. It is never an absolute pass over a suite already red
  at the base.
- V1-AC3 re-grades as met: 14 failures at the base, and the same 14 at the branch.

**RULING DEMO -- two planes, two answers (S5).**
- Andrew ruled demo a DEMO-TENANT class: ~01:3xZ 09-13 card 8, ledger X6 GRANTED. The registry's demo row carries that
  tenancy.
- Naming still reads `demo` in the firm slot (RULING DM, a naming ruling only).
- The registry note calling the class undefined is corrected.

**The write trail (W2-S3):** F1-J1's qualification stands. The fence's writer census is grant-derived because writes to
`opal-data-49financial` are unlogged. Turning on write logging is outside this project's outcomes; it is carried, not
cut.

**The grading rule and `grade()` (C-S11):** a two-way coverage check. Every step `grade()` takes is a step the rule
states, and every rule step `grade()` implements. The Terraform-type-to-node-type map becomes data in NAMING_SCHEMA v1.9
(with RULING ONE). LGIC_NAMING round 4's cells 1 and 2 re-cut the rule and `grade()`, and this project's round 2 cites
them; the two land together.

## 3. ROUND 2 -- ONE ISSUANCE BY 2.0.0_SA_COO~G

What each cell must reach. The split and order are the COO's.

1. **One carrier (FWD-2, FWD-7):**
   - `firm_forms` removed, and its readers repointed to the registry, landing with this seat's schema v1.9 text;
   - the tftest blocks generated;
   - X1-AC3 re-run, with its two filters made disjoint (W1-S21);
   - FWD-7's demonstration firm re-run with 0 WARNs.
2. **The limbs refuse only additions, and expressions are graded at plan (FWD-4; the G-F prerequisite):**
   - the 78 roots read 0 refusals of existing resources with the switch on;
   - a planted NEW wrong literal name is refused with its canonical form;
   - a planted NEW wrong expression-built name is refused at plan;
   - the correct forms pass.
3. **The registry rows for the 115 tokens (FWD-5):**
   - the classification by subtraction, with counts;
   - the rows added;
   - the census run to its end;
   - EN-s-2 on the real population.
   - LGIC_NAMING round 4's FWD-5 re-grade follows this cell.
4. **Instruments that discriminate (C-S7, C-S14):**
   - d2-control reads with its own regex;
   - t2-refuse asserts the canonical string;
   - the delta0 compares keep export order (a view that exports must keep its order);
   - v4-delta0 probes both branches;
   - the commit limb validates the registry before reading it (W2-S9);
   - each generated view's header hashes only the registry files that view reads (W1-S14).
5. **Registry hygiene:** RULING DEMO, and RULING ONE's DEC-1 field set.

## 4. NOT THIS PROJECT'S CELLS

- **C-S9, proof-of-spec-check's pre-flip false INVALID** on a tracked file modified in place: a `.tools/` defect this
  seat owns. It is fixed in its own commit, named in the send.
- **C-S10, the shared-index restore writer (S17):** 0.0.0_AB_MSTR's fabric-wide merge census. EN-f-2's truncated drain
  is repaired and verified at HEAD.
- **C-S13, six fabric-tool defects:** the L6 coverage limb, row-id minting across branches, comp-find's corpus and
  exclude, comp-iam role, the halt checkpoint's identity resolver, and deploy_ledger.py's close. Triaged by this seat
  as tool fixes outside any project round. Each was worked around inside round 1, and none blocks round 2.

**Nothing here needs Andrew.**
