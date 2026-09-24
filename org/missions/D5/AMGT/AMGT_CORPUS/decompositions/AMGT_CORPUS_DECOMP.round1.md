# AMGT_CORPUS -- L5 decomposition (COO) -- v1.0 (round 1)

**Seat:** `2.0.0_SA_COO~X`, seated on the operator's word at this terminal 2026-09-23 ~01:4xZ, on `1.0.0_SA_CTO~Z`'s L4->L5
handoff (msg 24518; acknowledged 24530/24531). **Directive:** D5. **Fabric:** site-z, branch `SITEZ`.
**Consumes:** PRD s. SURFACE MANIFEST R1-R11 at `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` **v0.4
@8fbb066b62** (landed by `1.0.0_SA_CTO~Z`, msg 24539). v0.3 @c94a6bb2ef was read first, when both halves were SIGNED.
v0.4 changes FWD-4 only, and the manifest rows are byte-identical to v0.3. `prd-signoff.py status` read WITHHELD at
v0.4's landing, then ADMITTED once `3.0.0_SA_CVO~Z` re-signed the ratified half @ca6b233108 (brief half current,
`2.0.0_SA_COO~Z`). v0.4's terms, as ruled in 24532:
- **FWD-4 ends at the EXECUTABLE REQUEST.** For one backlog name, one command produces the exact induction request
  (what it will add, an ambiguous identity refused), executable by the seat holding the universe. The induction act
  itself is `AMGT_RESAPP`'s: it writes that project's surfaces and spends its vendor budget.
- **`C-NO-VENDOR-CALL` stands untouched.**
- **FWD-4's population is re-pointed** at "a backlog folder the universe carries UNRESOLVED", conditional on `CRPS-c-5`
  measuring the resolved-and-absent set. If that set is non-empty, the original population stands.

**The issuance is cut only when `prd-signoff.py status AMGT_CORPUS` reads ADMITTED at v0.4.** Section 9 says why that
is a gate and not a wait.

**The rectangle is RECEIVED, not derived here.** L4 wrote the manifest. This file mirrors it, re-grounds what it can at
its own vintage, and adds the dependency edges, the placement axis and the battery. It does not re-open the manifest's
MECE. It makes the rulings section 8 states and defends.

---

## 1. The rectangle -- eleven cells over eleven manifest rows, `CRPS-c-<n>` mirroring `R<n>`

**THE INVARIANT:** every cell mirrors exactly one manifest row, and every row has exactly one cell. Measured at this cut:
11 cells over 11 rows, a bijection.

**CELL-ID CONFORMANCE, MEASURED** (`org/standards/DECOMP_CELL_ID_CONVENTION.md` SHAPE 1): the ids were loaded into the
enforcer object itself (`.tools/proof-of-spec-check.py` `CELL_ID_RE`, `fullmatch`):
- 11 of 11 ids match.
- Malformed controls: a lowercase prefix is refused and underscores are refused. A two-letter axis (`CRPS-cc-1`) is
  admitted, because the regex admits 1-4 letters. No cell here uses one.

No cell id from another project's decomposition is written in this file. Siblings are cited by path only.

**CELL STATUS VOCABULARY, ADOPTED** from `AMGT_RESAPP`'s decomposition s.2a (by path):
`NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`. Every cell at this cut is `OPEN`. That is measured
(11 of 11 evaluated), not a missing value.

**CODE HOME:** a new package `lib/research/corpus/`. It does not exist at this cut (measured). Every cell owns its own
module and its own test file, so no two cells edit one file. `CRPS-c-4` creates the package, the shared library-root
module and the test poison, and every later cell reads them and does not change them.

| cell | row | outcome | act (the engine, and what binds it) | state | chain | touches |
|---|---|---|---|---|---|---|
| `CRPS-c-4` | R4 | FWD-3 | **THE BACKLOG: folder census and resolution. FIRST CELL.** `library.py` derives the library root (never hardcoded; `C-LOCAL-AND-DEVICE-DERIVED`) and refuses loudly, naming the path, when it is absent. It enumerates folders and files by LISTING ONLY (no open) and records each file's OneDrive placeholder state. `backlog.py` reads the folder list FRESH and resolves each folder through the identity layer's own functions (`crosswalk.harvester_key` then `crosswalk.resolve`), never a local string match (`C-IDENTITY-VIA-THE-LAYER`). It prints three counts summing to the folder count (resolved, unresolved-with-reason, ambiguous-with-candidates) and writes ONE gold object per scan vintage (R4). It also answers K1. Plus the package's `__init__.py` and the test `conftest.py` poison. | OPEN | A1 | code + S3 (gold) |
| `CRPS-c-1` | R1 | FWD-1 | **REPORT BYTES AS FILED.** For every file in a RESOLVED folder: read the bytes (`rb`, never any other mode), sha256 them, and land them through the ONE bronze writer, `lib/research/harvest/store.py` `bronze_put`, at the builder's `research-report` address, partitioned by security key. Metadata carries the source path relative to the library root, the file mtime and the scan vintage. The key includes the content hash, so a changed file lands as a NEW object and the prior one stays (`C-CORPUS-AS-RECEIVED`). Then every stored object is RE-OPENED and matched byte for byte against the file on the drive. Printed: objects == files, both counted. A file in an unresolved folder is NOT stored and is printed with its folder and reason. | OPEN | A2 | this box -> S3 (bronze) |
| `CRPS-c-2` | R2 | FWD-1, FWD-5, FWD-6, FWD-7 | **EXTRACTION, a separate object naming its bronze parent.** Reads each bronze object FROM THE STORE, never the library again, and writes an extraction at `research-report-extract` in the same partition. Per type: DOCX text and headings by paragraph style (zipfile + lxml; python-docx is NOT installed and nothing is installed); PDF text per page and heading candidates (PyMuPDF); XLSX sheet names, row labels and mnemonic cells (openpyxl `read_only`, `data_only`, and the vendor cache sheets are NOT opened); PNG and HTML recorded as not-extracted, with the reason. Answers K3 (PDF extractability) and K4 (workbooks without Excel; FactSet codes). | OPEN | A3 | S3 -> S3 (bronze) |
| `CRPS-c-3` | R3 | FWD-2 | **THE TYPED PER-REPORT RECORD** in silver through the ONE silver writer (`store.silver_append`): security key, report id, bronze key, class (A research pack / B earnings update / C short form / D stock move / OTHER, measured from the scan's four skeletons), fund as written, sector as written, period, author, size. A field the report does not state is null with an `absent` reason. Answers K5: how the PERIOD is determined (filename date, header, or content) and how many of the files carry one. Plus `reports_for(security_key)`, which returns that name's reports in period order. | OPEN | A4 | S3 -> S3 (silver) |
| `CRPS-c-6` | R6 | FWD-5 | **THE PER-NAME CONTINUATION ARTIFACT (gold).** Per resolved name: thesis pillars, the name's own KPI set, fund of record, last stated position. EVERY field cites the report and the passage or sheet it came from; a field the reports do not state is null with an `absent` reason, never inferred or defaulted (`C-CITED-OR-ABSENT`). Graded on one covered name, built for every resolved name, denominator printed. | OPEN | A5 | S3 -> S3 (gold) |
| `CRPS-c-10` | R10 | FWD-8 | **THE ONE-CALL SUBSTRATE READ.** One call by security key returns the prior reports, the continuation artifact, the sector template, the fund form and the typecast, each with its content hash and `{key, sha256}` for every input (`C-INPUT-HASHED`). A second call after a new report lands returns a changed hash for exactly the artifact that changed and unchanged hashes for the rest. No new store. | OPEN | A6 | code (reads S3) |
| `CRPS-c-11` | R11 | FWD-9 | **THE READ-ONLY PROOF.** Two arms. The NEGATIVE CONTROL runs `CRPS-c-1`'s ingestion against a COPY of the library made write-denied, and the run completes. The CODE CENSUS is an AST census of every `.py` under `lib/research/corpus/` for write, move, rename, delete or open-for-write calls reaching a library-root path. It prints zero and its denominator, and a planted-write POSITIVE CONTROL proves the census can find one. A ledger record, no store. LAST CELL: the census must see the whole package. | OPEN | A7 | this box (scratch copy) |
| `CRPS-c-5` | R5 | FWD-4 (v0.4) | **THE INDUCTION REQUEST, NO VENDOR CALL.** Measures and prints BOTH populations: resolved-and-absent from the universe, and backlog folders the universe carries UNRESOLVED. Picks ONE name by a stated deterministic rule. A single command prints the exact request that `lib/research/identity/add_security.py` would execute, and what it would add, BEFORE anything else; an ambiguous identity is REFUSED. It EXECUTES NOTHING: no Bloomberg call, no `registrations.json` write, no pool write. The poison is positive-controlled. | OPEN | B1 | code |
| `CRPS-c-9` | R9 | FWD-7 | **THE GENERIC MODEL TYPECAST (gold, one object).** From R2's workbook extractions: the shared mnemonic core, the extended ratio set and the Opal Case Assumptions block, each with the count of workbooks carrying it out of the workbooks read. The FactSet-coded variants are typed onto the same lines where a mapping is MEASURED, and printed as unmapped where it is not. | OPEN | C1 | S3 -> S3 (gold) |
| `CRPS-c-7` | R7 | FWD-6 | **THE SECTOR TEMPLATE, one per business type (gold).** Section names, KPI set and chart pages per business type, each measured with its denominator (that type's reports of the total) and the per-term counts behind each KPI. Both sector vocabularies are bridged through the engine's own map (`lib/research/peers/taxonomy.py` `GICS11_TO_SCANNER13_v1`), never a new mapping. Graded on one business type; built for every type with a denominator. | OPEN | D1 | S3 -> S3 (gold) |
| `CRPS-c-8` | R8 | FWD-6 | **THE FUND FORM, one per fund of record (gold).** The report skeleton each fund's reports keep (IDVZ, PFOE, DIVZ as the corpus writes them), each section with its count of that fund's reports. Where two funds' skeletons differ, BOTH are kept and labelled (`C-TEMPLATE-IS-MEASURED`). | OPEN | E1 | S3 -> S3 (gold) |

---

### 1a. Re-groundings performed at L5 (SITEZ HEAD @3ab14b967a, 2026-09-23 ~01:4xZ-01:5xZ)

Every figure is this seat's own read. None of them spends a cell's work.

**K1, the library on THIS device.**
```
root  C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research
folders 93     files 351 = .pdf 184 + .xlsx 78 + .docx 71 + .png 17 + .html 1     305.7 MB
stat attributes: local 248, RECALL_ON_DATA_ACCESS (OneDrive cloud placeholder) 103
```
Equal to the brief's scan on every count. **103 of 351 files are cloud placeholders, so READING THEM HYDRATES them**
through OneDrive (the firm's own Microsoft 365 tenant; not a vendor API, and no write to the library's content). The
ingestion cell records each file's placeholder state BEFORE its read. What this does NOT settle is how a PARTIAL sync
would read. That is `CRPS-c-4`'s question.

**K2, the identity layer.** The crosswalk the layer loads is `s3://opal-data-harvest/crosswalk/v1/2026-09-22.json`
(96 records, 237 index forms, 0 ambiguous; 93 records carry a `source_row.folder`, and 0 of those folders are outside
the library).
```
crosswalk.resolve(<raw folder name>)                          resolved 2 of 93
crosswalk.resolve(crosswalk.harvester_key(<folder>, pilots))  MEASURED 33 of 93 | record with security_key None 60 | ambiguous 0
```
**So the layer ALREADY holds every library folder, and resolves 33 of them.** The other 60 are records the universe
carries UNRESOLVED (the ticker was not measurable from the folder's one-pager). **K2 RULING (carried to L5 by the PRD,
`:386-387`, and made here):** FWD-3 stays a PRINTED DENOMINATOR this round, with NO human pass. Its three counts are
satisfiable on these numbers. The 60 are a question of INDUCTION (FWD-4's path, v0.4), not of resolution. Reported to
`1.0.0_SA_CTO~Z` in msg 24530 and adopted in 24532.

**FWD-4's induction path.** `lib/research/identity/add_security.py` (an `AMGT_RESAPP` cell's build) is the estate's only add-a-security
act. It makes ONE Bloomberg `reference_data` call per name, including under `--dry-run`, and writes the layer's
`registrations.json` and the crosswalk pool. It already accepts `--folder "<library folder>"`. That fact produced the
v0.4 ruling above.

**Rule 30, the builder.** `lib/opal_naming.py address()` with source `amgt`, scope `harvest` (`naming.lookup`):
```
R1 bronze/research-report                s3://opal-data-harvest/amgt/harvest/bronze/research-report/<partition>
R2 bronze/research-report-extract        s3://opal-data-harvest/amgt/harvest/bronze/research-report-extract/<partition>
R3 silver/research-report                s3://opal-data-harvest/amgt/harvest/silver/research-report/<partition>
R4 gold/research-backlog                 s3://opal-data-harvest/amgt/harvest/gold/research-backlog/<partition>
R6 gold/research-continuation            s3://opal-data-harvest/amgt/harvest/gold/research-continuation/<partition>
R7 gold/research-sector-template         s3://opal-data-harvest/amgt/harvest/gold/research-sector-template/<partition>
R8 gold/research-fund-form               s3://opal-data-harvest/amgt/harvest/gold/research-fund-form/<partition>
R9 gold/research-model-typecast          s3://opal-data-harvest/amgt/harvest/gold/research-model-typecast/<partition>
8 of 8 print, 0 refuse
```
The partition values above are the builder's probe arguments. Each cell prints the address it actually wrote.

**The ONE writer.** `lib/research/harvest/store.py` (an `AMGT_RESAPP` cell's build) is the shared bronze and silver writer:
- `bronze_put(source, request, partition, object_name, body, ...)` is a conditional, never-overwrite put. The same
  sha256 is a no-op; different bytes raise `BronzeImmutableError`.
- `silver_append(source, table, rows, record_key_fields, run_stamp)` writes parquet partitioned `date=` BY FETCH DATE.
- `entity_partition("security_key", key)` mints the slash-safe partition through the crosswalk.

Gold has no shared writer. Each gold cell writes with a conditional put (`IfNoneMatch='*'`) at `address()` output and
never overwrites.

**Parsers on this box** (a worker installs NOTHING): openpyxl 3.1.5, PyMuPDF (fitz) 1.28.2, pypdf 6.16.2, pyarrow 24.0.0,
boto3 1.43.46, lxml 6.1.1. **NOT installed:** python-docx, pdfplumber, xlrd. So DOCX is read with zipfile + lxml.

**The two-vocabulary bridge exists:** `lib/research/peers/taxonomy.py:38` `SECTOR_MAP_ID = "GICS11_TO_SCANNER13_v1"`.

---

## 2. Rule 24 four-postulate record, for what this file ADDS

**(i) MECE over a declared domain, by subtraction.** The domain is the manifest's printed rows R1-R11: 11 rows.
Cells = 11 rows minus 0 excluded = 11. No row is split and none is merged. The one value set this file authors is the
report-class enum `A | B | C | D | OTHER`. Its domain is every file ingested. A-D are the scan's four measured skeletons
(`RESEARCH_CORPUS_SCAN_20260922.md` s.1). `OTHER` is the subtraction's remainder: company source PDFs, PNG charts, the
HTML file and the blank templates. **Token census:** `research-report` and its siblings appear only in the PRD manifest.
The class letters are the scan's own.

**(ii) Same grain.** Every cell is one ENGINE, one row of the manifest.

**(iii) Intent coherence.** The chain axis orders by DATA dependency (what a cell reads that another writes), and by
nothing else.

**(iv) State coherence -- what each remedy does NOT move.**
- `CRPS-c-1` moves bronze for RESOLVED folders only. The 60 unresolved folders' files stay unstored and are printed.
  FWD-1's "every file the folder list resolves to" is graded on that resolved set.
- `CRPS-c-5` moves NOTHING in the world: no pool, no registration, no universe row. Its output is a request.
- `CRPS-c-11`'s negative control writes nothing to the library, by construction (a write-denied copy).
- No cell moves anything SERVED. The platinum report object, the page and the adapter are the `AMGT_RESAPP` addendum's
  (`C-NO-RAW-BRONZE-AT-SERVE`).

---

## 2b. BATTERY DISPOSITION PER LENS

### `comp-schedule --drift` -- RUN
```
REACHED-DENOMINATORS: C1=23; C2=7; C3=12; C4=21; C5=334
GATES ARMED: 2 [--drift]   G-3 (owner CTO)   G-7 (owner POD4, data/black_diamond/scripts/gold/gold_dispatch.sh:59)
```
Neither armed gate names a harvest, research or corpus surface. The open-deploy census reads 7 entries in the shared
tree's `org/critical_paths/.open_deploys/`, 0 naming harvest, corpus or research. **BLINDNESS, STATED:** 31 other live
worktrees (`git worktree list`: 32 rows) were NOT read (CLAUDE.md NEVER-2 worktree clause). **No cell here is a deploy**:
the S3 writes are data objects at new prefixes, so no act depends on that read.

### `comp-iam` -- RUN (`roles`: 214 found)
Three harvest-sourced roles are listed: the chatter-axis pair and `opal-research-pull-enqueue-role`. **None of them is
the credential these cells write with.** **BLINDNESS:** this is the DESIRED plane (Terraform) only, and `comp-iam roles`
prints no vintage. **This box's own credential is NOT read by this lens.** Each writing cell measures it with its first
real conditional PUT to its own new prefix and records the outcome. A refusal is a BLOCKING row, never a workaround.

### `comp-adversary` -- RUN on this file; declaration at section 7.

### `comp-blast` -- DECLARED-NOT-APPLICABLE
No cell moves a served object or an existing prefix. Every write is a new prefix under `amgt/harvest/`.

---

## 2c. BOUNDS THE BATTERY ADDED TO CELLS -- carried into the L6 cut
- **Every cell:** no vendor API, no Claude API (`C-NO-VENDOR-CALL`); no install; no notifier (`C-NO-NOTIFIER`).
- **Every writing cell:** S3 writes ONLY under `opal-data-harvest`, ONLY at `address()` output, NEVER overwriting. A
  refused PUT is a BLOCKING row, never a hand-typed key.
- **Every reader of the library** (`c-4` lists, `c-1` reads, `c-11` copies): opens `rb` or lists only. No write, move,
  rename or delete under the library root (`C-CORPUS-READ-ONLY`). The root is derived, never typed.
- **Every test file:** offline, under `CRPS-c-4`'s `conftest.py` poison (boto3 client construction, `subprocess.run`,
  `socket.create_connection` all RAISE), with a positive control proving it bites. **A no-network PASS with no poison
  proven is an ABSENCE** (the CVO's standard, adopted estate-wide at AMGT_HARVST round 2).
- **`CRPS-c-5`:** the add-security module is imported, never executed. Its Bloomberg transport, `boto3` and
  `subprocess.run` are poisoned, and the poison is positive-controlled.

---

## 3. Placement axis

Every cell executes on **site Z** (this desktop, branch `SITEZ`). The library is synced to THIS device's OneDrive, and
the identity layer and the harvest writer live in this fabric's tree. No cell executes on the laptop fabric.

---

## 4. Dependency edges, keyed to OBSERVED completion (a drained, VALID proof-of-spec instance), never a status word

```
  chain A:  CRPS-c-4 -> CRPS-c-1 -> CRPS-c-2 -> CRPS-c-3 -> CRPS-c-6 -> CRPS-c-10 -> CRPS-c-11
  chain B:  CRPS-c-2 -> CRPS-c-5
  chain C:  CRPS-c-2 -> CRPS-c-9 -> CRPS-c-10
  chain D:  CRPS-c-3 -> CRPS-c-7 -> CRPS-c-10
  chain E:  CRPS-c-3 -> CRPS-c-8 -> CRPS-c-10
```
- **c-1 after c-4:** bronze is partitioned by security key, which only the backlog's resolution supplies. c-1 also
  reads c-4's `library.py`.
- **c-5 after c-2 (amended at the cut, v1.0 before issuance; it read "after c-4" at @3c09ae6ce8):** its population is
  c-4's unresolved set. But `add_security --folder` alone cannot induct an UNRESOLVED folder, because `_discover` reads
  the same one-pager whose ticker already failed and returns UNRESOLVED ("the identifier is NOT guessed from the folder
  name"). So the request must carry an EVIDENCED `--bloomberg` candidate, read from the `Ticker:` header of the team's
  own report for that name. Those folders' files are not ingested (ruling 4), so c-5 reads them `"rb"` and parses them
  with c-2's extractor, which puts it after c-2.
- **c-2 after c-1:** an extraction names its bronze parent.
- **c-3 after c-2:** the typed record's class, fund, sector and period are read from the extraction.
- **c-9 after c-2:** the typecast reads the workbook extractions only. It needs no typed record.
- **c-6, c-7, c-8 after c-3:** each groups reports by name, business type or fund, which the typed record carries.
- **c-10 after c-6, c-7, c-8 and c-9:** the one call returns every gold artifact.
- **c-11 LAST:** its census must see the whole package, and its negative control runs c-1's ingestion.

**M = 5**, the widest antichain of the edge set (`c-5, c-6, c-7, c-8, c-9` can all be in flight at once after c-3).

---

## 5. The round -- one issuance, fan-out as data

- **Round 1 covers all 11 cells in ONE issuance.** Five worker slots:
  - `~1` drains chain A in order (c-4, c-1, c-2, c-3, c-6, c-10, c-11). It is continued, not respawned, so the
    ingestion context carries into the derivations and the proof.
  - `~2` c-5 and `~3` c-9, both spawned on c-2's valid drain.
  - `~4` c-7 and `~5` c-8, spawned on c-3's valid drain.
- Fan-out line for the issuance commit:
  `fanout: 5 of 5 chains, cap 8, reason: M is the widest antichain after c-3; chain A is one continued worker; c-5 and c-9 spawn on c-2's valid drain, c-7 and c-8 on c-3's.`
- **Drain duty owed by this seat, not by a worker:** before continuing `~1` onto `CRPS-c-10`, merge the drained c-7, c-8
  and c-9 branches into `~1`'s worktree branch, since c-10 reads their modules. When `CRPS-c-5` drains VALID, hand its
  `induction_request.json` to `AMGT_RESAPP`'s COO by file and message. When `CRPS-c-11` drains, name the write-denied
  copy's path to the operator for cleanup (recursive deletion is an operator act).
- The surprise channel is `org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md`. It is
  already open, with seat rows `Z-S1..Z-S3`. Workers mint `AMGT_CORPUS-Z-W<n>-S<k>`.

---

## 6. `<preflight>` -- what this decomposition actually ran
```
prd-signoff.py status AMGT_CORPUS        v0.3 @c94a6bb2ef ADMITTED, 2 of 2 halves SIGNED current (v0.4 pending, s.9)
receiving-check.py <PRD>                 ACCEPT (prd-manifest: manifest, ENDPOINT, header, outcome cards, agreement)
sequence-check.py --project AMGT_CORPUS  not in SEQUENCE.yaml (not sequenced); 3 live COO lanes on this box (~X ~Y ~Z)
to-check.py --all --assignee 2.0.0_SA_COO~X   0 held (2 hits are DS~V orders naming ~X in prose), 3146 scanned
comp-schedule --drift                    2 armed, 0 on these surfaces (C1=23 C2=7 C3=12 C4=21 C5=334)
comp-iam roles                           214 found; 3 harvest-sourced, none the writing credential (DESIRED plane)
address() x 8 store rows                 8 of 8 print, 0 refuse
library stat census                      93 folders, 351 files, 103 placeholders
crosswalk.resolve via harvester_key      33 MEASURED / 60 record-unresolved / 0 ambiguous, of 93
proof-of-spec-check.py CELL_ID_RE        11 of 11 ids match; 2 of 3 malformed controls refused
```

---

## 7. comp-adversary declaration

Recorded at the issuance commit (the tool reads committed citations). The declared blindness this file accepts in
advance: the tool's neighbourhood is filesystem adjacency, not the cells' real neighbours. Those neighbours are the
identity layer (`lib/research/identity/`), the harvest writer (`lib/research/harvest/store.py`), the taxonomy bridge,
and the library outside the repo, and they were read directly in s.1a.

---

## 8. Rulings this decomposition makes, and what it REFUSES to assume

**Rulings (L5's own, each stated so a reader can dispute it):**
1. **K2:** FWD-3 is a printed denominator this round, with no human pass (s.1a).
2. **R3's "by security key" is a COLUMN, and the partition is the ONE silver writer's fetch-date partition.**
   `store.silver_append` partitions `date=` by fetch date under `AMGT_RESAPP`'s `C-SILVER-PARQUET`. This project adds
   no second silver writer, and FWD-2's query by security key is a filter over the column. Reported to the CTO in the
   drain-end read as a manifest-argument reconciliation, not a defect.
3. **K5 is carried by `CRPS-c-3`, not `CRPS-c-1`.** The PRD's K-card table names "the ingestion cell" for K5.
   The period is a field of the TYPED RECORD (R3), and the ingestion chain's typed-record cell is where it is read.
4. **FWD-1's population is the files of RESOLVED folders.** That is the DONE WHEN's own phrase, "every file the
   library's own folder list resolves to". Unresolved folders' files are printed, never stored under a guessed key.

**What this decomposition REFUSES to assume:**
- **That every file hydrates.** A placeholder that fails to hydrate is printed with its error and counted, never
  skipped silently.
- **That a report's period, fund, class or sector is inferable.** Each is `absent` with a reason when the report does not
  state it.
- **That the PDF-only reports carry the Word skeleton.** K3 is measured, not assumed.
- **That this box can write the new prefixes.** Each writing cell measures it with a real conditional PUT.
- **That resolved-and-absent is empty.** `CRPS-c-5` measures it and prints both denominators.

---

## 9. Holds, and whose they are

| hold | on | owner | what lifts it |
|---|---|---|---|
| the ISSUANCE | PRD v0.4 (the FWD-4 amendment, ruled 24532) re-opens the RATIFIED-TEXT half; `to-pipeline-gate.py` LIMB 6 refuses a new order against a stale half | `3.0.0_SA_CVO~Z` (re-sign), after `1.0.0_SA_CTO~Z` lands v0.4 | `prd-signoff.py status AMGT_CORPUS` reads ADMITTED at v0.4. **This is a GATE, not a wait:** both acts are on-demand acts by live seats, and the orders are cut in the meantime |
| the live induction (a Bloomberg `reference_data` call plus a layer write) | `AMGT_RESAPP`'s surfaces and vendor budget | `AMGT_RESAPP`'s COO, on Andrew's per-use word, carried by `1.0.0_SA_CTO~Z` when it arises (24532) | NOT this project's. `CRPS-c-5` ends at the executable request |
| any served move of these artifacts | the `AMGT_RESAPP` addendum | `1.0.0_SA_CTO~Z` | the addendum's own L2 |

-- `2.0.0_SA_COO~X`
