# NEVER-WIDEN CO-SIGN -- CTO HALVES. Round 14, chain E. One section per co-signed cell.

**Signer:** `1.0.0_SA_CTO~Z` (DRAFT -- unsigned, uncommitted). **Counterpart:**
`2.0.0_SA_COO~Z`'s COO halves at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND14_CHAIN_E_COO_HALVES.md`
@`9a6aa12da2` (APPLIED/EXERCISED plane). **This plane: DESIRED -- the SOURCE DIFF and THE PRODUCER'S OWN
RULE.** Neither half stands alone.

**VINTAGE.** Every `path:line` below is read at `HEAD = c8989376008b7e84ccd34a92acee6cbfcb5d730c` (branch
`SITEZ`). `git diff --stat 9a6aa12da2 HEAD -- lib/research` is EMPTY and `git status --porcelain lib/research`
is EMPTY, so the COO half's citations and mine read the same bytes; no vintage split exists between the halves
on the producer sources. Governing contract: `C-EXEC-MANAGEMENT`, PRD v0.13
(`org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md:723-757`).

**READ THIS FIRST -- THE STANDING GRAIN CAVEAT FOR ALL FOUR CELLS.** Chain E's task orders
(`AMGT-rk-43/45/47/48`) are NOT committed at `9a6aa12da2` (`git ls-tree 9a6aa12da2 .../task-orders/` returns no
`rk-4x` file; highest present is `rk-30`). So for each cell I can read the PRODUCER'S RULE AT HEAD exactly, and
I can read the PRD clause exactly, but the DIFF ITSELF is not yet a file I can cite. Where a claim depends on
code the cell has yet to write, I mark it **UNVERIFIED (diff not yet authored)** and state what the order must
contain for the COO half's outcome to hold. That is the honest boundary of this plane tonight, and it is the
single largest qualifier on every section below.

Measured with `comp-find <token> lib/` (CLAUDE.md Rule 21; denominator 182 files scanned, corpus=all), all at
HEAD: `roster_source` **0**, `COMPANY_EXEC_OFFICERS` **0**, `skip-pool` **0**, `absent_because` **0**,
`exec_officers` **0**. `NOT_SEARCHED` over the whole corpus: **5 hits / 66,309 files, ALL band DOC**, none in
first-party source. **So every named surface of chain E is ABSENT from the code at HEAD.** Chain E is
net-new code on four served properties, not an edit to an existing one.

---

## `AMGT-rk-43` -- honest management states in the adapter; redeploy (R14-E1)

### 1. THE ACT
ONE redeploy of `opal-amgt-scoped-api` from the worker's worktree bytes (build script -> artifact VersionId ->
ONE targeted `safe-apply`, 0 destroy); portal edits committed, not promoted; no producer run, no pool write, no
IAM. **This agrees with the COO half exactly.**

### 2. THE SOURCE DIFF
The cell changes `lib/research/api/scoped_amgt.py`, in two functions the COO half names correctly by line:

- `ceo_profile_reading()` -- `scoped_amgt.py:2275-2302`. Confirmed at HEAD: `def ceo_profile_reading` is at
  `:2275`; the function ends at `:2302`.
- `read_management()` -- `scoped_amgt.py:2305-2371`. Confirmed at HEAD: `def read_management` is at `:2305`;
  `return block` is at `:2371`, `def read_scores` at `:2374`.

What the change must make the code do, against what it does now:

**(a) the zero-officer arm.** At HEAD there is none. `read_management()` sets the served status
UNCONDITIONALLY once a document parses -- `scoped_amgt.py:2347`, `"management_status": POOL_SERVED`, inside a
`block.update({...})` that no officer-count branch guards; `officers` is computed one line earlier at `:2344`
and is used only for counts. So a name whose Item-6 cut is EMPTY reads `SERVED` with `officer_count 0`. The
COO half's characterisation of the round-13 defect (ASML) is **CORRECT and I confirm it at source.** The PRD is
explicit that this is wrong: *"A roster with ZERO officers is NOT SERVED. It is ABSENT with its reason."*
(`AMGT_RESAPP_PRD.md:733-735`). The cell must add the arm and the `absent_because` field; `absent_because`
is **0 hits in `lib/`**, so it is new.

**(b) the CEO arm.** The COO half says `ceo_profile_reading` *"reads fields"*. **At HEAD it does not read a
field -- it PARSES PROSE**, and this is the sharpest source finding in chain E. The decisive lines:

```
scoped_amgt.py:2273   _SERP_URL_COUNT_RE = re.compile(r"returned (\d+) url")
scoped_amgt.py:2294       found = _SERP_URL_COUNT_RE.search(str(profile.get("basis") or ""))
```

and the comment above it, printed verbatim at `scoped_amgt.py:2264-2266 @c8989376008b`:

> `# SENTENCE; it carries no field separating "the instrument answered and found`
> `# nothing" from "the instrument returned links whose host it cannot read" (row`
> `# AMGT_RESAPP-Z-W22-S1). The url count is therefore PARSED from the object's own`

**That comment is FALSE at HEAD.** The object DOES carry exactly that field. It is `absence_class`, it is in
the ratified schema as an enum -- `lib/research/management/management.schema.json`,
`definitions.ceo_profile.properties.absence_class`, `{"enum": ["NOTHING_FOUND", "CANNOT_SAY", null]}`, under
`additionalProperties: false` -- and the producer sets it at `enrich.py:416` (default), `:437`, `:441` and
`:448`. `comp-find 'absence_class'`: 10 SURFACED hits, 8 of them in `lib/research/management/enrich.py`, 1 in
`integrations/bloomberg/research/management_posture_batch.py:179` (a second CONSUMER that reads the field
correctly). The adapter is the only consumer that re-derives it from a sentence.

This matters to the co-sign because the PRD ratifies the field, not the sentence
(`AMGT_RESAPP_PRD.md:750-752`): *"The page renders the object's own `absence_class`, never a reason it infers,
in FIVE states: CONFIRMED; NOT SEARCHED, with the reason; SEARCHED, NOTHING FOUND; SEARCHED, NOTHING KEPT
...; SEARCH FAILED, with its cause."* HEAD's `ceo_profile_reading` returns THREE values
(`scoped_amgt.py:2270-2272`: `CONFIRMED`, `NOT_CONFIRMED_NOTHING_FOUND`, `NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY`)
and derives them by inference. **If rk-43's diff does not replace the parse with a read of `absence_class` and
widen the enum to five, the redeploy ships a served plane that does not conform to the clause it is cut under.**
UNVERIFIED (diff not yet authored) whether it does.

### 3. THE PRODUCER'S RULE, BRANCH BY BRANCH
The producer here is the ADAPTER at request time (no batch runs). Reading `read_management()` at HEAD:

| branch | condition | what it writes into the block | what it does NOT |
|---|---|---|---|
| no identity | `:2331` `if not key` | `management_status ABSENT`, reason "identity UNRESOLVED" | never reads S3 |
| ABSENT | `:2336` document None and record ABSENT | status ABSENT + "no M-1 management object has landed" | never sets pool fields |
| READ_FAILED | same guard, other reason (`:2339`) | status READ_FAILED + "not evidence that no roster exists" | never sets pool fields |
| SERVED | document parsed | status SERVED + every figure, incl. `pool_*` from a SECOND read at `:2343` | **no zero-officer test at all** |
| foreign object | `_foreign()` `:1228-1240` | READ_FAILED, "a foreign object is never served" | never serves it |

The COO half's three expected outcomes rest on these branches as follows, and I confirm the mapping except at
one point:

- SAP_GY_Equity `SERVED` / `ceo CONFIRMED`: rests on the SERVED branch plus `ceo_profile_reading`'s first arm
  (`:2288-2289`, `status == "RESOLVED" and profile.get("url")`). **Covered on both branches** -- the negative
  arm is the `ABSENT` branch, also stated.
- ASML `ABSENT` / `absent_because ZERO_OFFICERS`: rests on a branch **THAT DOES NOT EXIST AT HEAD** and that
  this cell creates. The half is right about the target state; it is an outcome of the diff, not of the rule.
- **NU_US_Equity `SERVED` / `ceo NOT_SEARCHED` -- THE ONE I CANNOT CONFIRM.** `NOT_SEARCHED` is **0 hits in
  first-party source** (`comp-find 'NOT_SEARCHED'`: 5 hits / 66,309 files, band DOC=5, all five in
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CEO_STEP_IMPLEMENTATION_DESIGN_20260918.md`). At HEAD, a name with
  no declared IR domain produces a basis string written at `enrich.py:424` -- *"no declared IR domain for this
  name: a SERP not scoped to the company's own domain is not the contract's search"* -- which contains no
  `returned N url`, so `scoped_amgt.py:2294-2299` returns `NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY` with
  `reading_basis "ceo_public_profile.basis names no url count"`. **So the COO half's expected value for NU is
  a NEW ENUM MEMBER, and an outcome enum is a schema under CLAUDE.md Rule 24** (four postulates + a
  word-boundary token census before the value lands). Neither half names that obligation. I name it here.

**A producer defect the cell must not paper over.** `absence_class` is initialised to `NOTHING_FOUND` at
`enrich.py:416` and the two early returns at `:421` (no CEO on the roster) and `:425` (no IR domain) return
WITHOUT changing it. So every object where NO SEARCH HAPPENED carries `absence_class NOTHING_FOUND` -- the
field says "searched, found nothing" about a name that was never searched. The same conflation is hard-coded
for an empty roster at `enrich.py:536`. **Reading `absence_class` naively in the adapter would therefore
propagate a wrong state**, which is presumably why the adapter parses the sentence. The correct diff fixes the
PRODUCER's field and then reads it; reading the field alone is not enough, and parsing the sentence forever is
not the contract. I state this as a DESIGN CONSTRAINT on rk-43, not as an objection to the act.

### 4. WRITER CENSUS CROSS-CHECK
The COO half prints **N = 1** writer of the Lambda's bytes (`build-and-upload-scoped-amgt.sh` + the targeted
apply), with an adapter single-writer queue behind it. **I did not re-derive N on the deploy plane** -- that is
the APPLIED plane and the COO half measured it there; re-running the COO's own instrument would be REPETITION,
not corroboration (Rule 22). On MY plane the relevant census is the CONSUMERS of the property this cell moves:
`comp-find 'absence_class'` gives **2 first-party consumers** (`scoped_amgt.py` and
`integrations/bloomberg/research/management_posture_batch.py:179`), and the second one reads the field
directly. **A change to `ceo_profile_reading`'s value set therefore does not reach that second consumer, and
the two consumers will disagree on the same object.** Neither half names the second consumer. NOT a blocker
for the act; named so it is not discovered later.

### 5. WHAT THIS HALF DOES NOT COVER
Any producer run; any S3 write of any kind; the portal push or PROD promote; a second redeploy; any change to
`enrich.py`'s `absence_class` assignment (a producer edit is a DIFFERENT act on a DIFFERENT plane and needs its
own pair); the `NOT_SEARCHED` enum widening as a schema act under Rule 24; and any reconciliation of
`management_posture_batch.py` with the new value set.

---

## `AMGT-rk-45` -- one pool: the newest pool object for every reader (R14-E3)

### 1. THE ACT
(i) ONE write of `management/v1/_pool/<today>.json` in `opal-data-harvest`, overwriting today's null-valued
object; (ii) the one-line adapter change at `scoped_amgt.py:2343` plus its own redeploy, sequenced after
rk-43 drains. **This agrees with the COO half on the WHAT. It does NOT agree on the HOW of (i)** -- see 3.

### 2. THE SOURCE DIFF
**The adapter line is exactly right.** Printed at HEAD, `scoped_amgt.py:2343`:

```
    pool_document, pool_record = read_pool_object(MANAGEMENT_PREFIX, MANAGEMENT_POOL_NAME, as_of=document.get("as_of"))
```

Dropping `as_of=` changes which object is read, and the semantics are documented in the callee's own docstring
at `scoped_amgt.py:1153-1156`: *"With `as_of`, the object `<as_of>.json`; without, the LATEST: the last `.json`
key directly under the prefix in key order, which for ISO-dated names is the newest date."* The mechanism is
`:1183-1194` -- paginate `list_objects_v2`, keep `.json` keys with no further `/`, `sorted(...)[-1]`. So the
change makes every name's pool comparison read ONE object, the newest, regardless of the name's own `as_of`.
That is the E3 endpoint and the diff is one keyword argument.

**Property-name note.** The COO half's outcome names `pool_object_key`. `read_management()` publishes no such
key. The carrier at HEAD is `pool_read.object_key`, set at `scoped_amgt.py:1225`, surfaced into the block at
`:2360` as `"pool_read": pool_record`. Same fact, different name; the worker's criterion must read
`pool_read.object_key` or it will read `None` and grade a true success as a failure. Likewise the half's
`pool_avg` is `pool_avg_tenure_years` (`:2358`). Cosmetic, but a criterion is a literal.

### 3. THE PRODUCER'S RULE -- AND THE FIRST DISAGREEMENT WITH THE COO HALF
The COO half states the act's (i) as *"ONE `put_object` ... through `crosswalk.write_pool` (put + head
read-back)"* and later reasons about *"the pool object's rebuild"* yielding `pool_avg null`. **Those are two
different producers and the half treats them as one.**

- `crosswalk.write_pool(key, payload)` (`lib/research/identity/crosswalk.py:609-655`) is a BYTE MOVER. It
  takes a payload someone else built. It applies NO schema.
- The only in-repo code that BUILDS a pool document is `enrich.compute_pool()` (`enrich.py:582-618`), and the
  only code that writes one WITH VALIDATION is `enrich.write_pool_object()` (`enrich.py:625-630`), which calls
  `validate_pool()` first and **raises** `"the pool object does not validate, nothing written"` (`:627-628`).
- `write_pool_object` is reachable at HEAD from exactly one place: `enrich.main` at `:690`, guarded by
  `--write-pool` at `:680`. **`comp-find 'write_pool_object' lib/`: it is defined at `:625` and called at
  `:690`. There is no standalone pool-rebuild entry point.**

**Consequence: "a put through `crosswalk.write_pool`" bypasses `pool.schema.json`** (which is
`additionalProperties: false` and requires `as_of`, `pool_avg_tenure_years`, `pool_denominator`). The producer's
own refusal branch -- "nothing written" on an invalid pool document -- **does not exist on the path the act
names.** If instead the worker reaches the pool through `enrich.main --write-pool`, then `:685`
`receipt = write_document(...)` fires FIRST and a PER-NAME dated key lands -- **a key rk-45's blast radius does
not name.** Either reading widens something the half did not intend. The order must pick one and say which.

**The second disagreement: `write_pool` does not always write.** Printed at HEAD,
`crosswalk.py:626-628`:

```
    written = False
    if head is None or head.get("Metadata", {}).get("document-sha256") != digest:
        condition = {"IfMatch": head["ETag"]} if head else {"IfNoneMatch": "*"}
```

and the docstring at `:612-614`: *"An object already carrying the same document-sha256 is NOT rewritten
(re-running mints nothing)."* The COO half's null branch says *"the object is still written"*. **Source says:
if the recomputed pool document serialises to the same bytes as the null-valued object already at
`_pool/2026-09-18.json`, NOTHING is put, `put_performed` is `False`, and the ETag does not move.** This is
NARROWER than what was signed, never wider, so the act stays covered -- but a criterion asserting "the object
was written" or "the ETag changed" would FAIL on a correct run. Flagging it as a criterion hazard, not a
radius breach.

**Branches of `crosswalk.write_pool`, complete:**

| branch | source | writes | does not write |
|---|---|---|---|
| key absent | `:628` `IfNoneMatch: "*"` | put-if-absent, `put_performed True` | -- |
| key present, bytes differ | `:628` `IfMatch: head["ETag"]` | conditional overwrite | -- |
| key present, bytes identical | `:627` predicate false | **nothing**, `put_performed False` | no put, no ETag move |
| head raises non-404 | `:624-625` `raise` | nothing | propagates, uncaught by `main` |
| concurrent writer between head and put | `IfMatch` 412 | nothing | **uncaught** -> traceback |
| read-back mismatch | `:637-648` `raise ValueError` | the put ALREADY HAPPENED | the raise does not undo it |

The last row is worth the co-sign's attention: a READ-BACK MISMATCH raises AFTER the put, so "the command
failed" and "the object did not move" are not the same statement. The per-key rollback in the COO half (pre-act
bytes to `.scratch/` with sha256, re-put) **covers this correctly** -- I confirm the rollback is sound for
every branch above.

**The third disagreement, and the one I would not sign around: `compute_pool` contradicts the ratified
contract.** PRD `AMGT_RESAPP_PRD.md:753-755`: *"the average tenure is the mean over OFFICERS across EVERY
current FILING roster -- **the newest object per name across all dates**, within the union universe -- **never
over one run's objects**."* The producer at HEAD, `enrich.py:594`:

```
    mine = [k for k in keys if k.endswith("/%s.json" % as_of) and "/%s/" % POOL_NAME not in k]
```

**That is a SAME-DATE filter.** It selects only per-name objects whose key ends in today's date -- which is
precisely "one run's objects", the construction the clause forbids. The null-value state the COO half observed
on `_pool/2026-09-18.json` is the DIRECT OUTPUT of this rule (`tenures` empty -> `:610`
`round(...) if tenures else None`), not a fact about the data. So:

- The COO half's expected outcome *"BA and NU BOTH serve the SAME non-null `pool_avg`"* requires enough
  per-name objects dated TODAY. Under `compute_pool` at HEAD, that requires a same-day run over the covered
  names -- **which Andrew has forbidden** (*"I dont care about rerunning until the process is completely
  validated end to end"*, quoted in the chain I half).
- The half's stated `names_with_roster` 7 is therefore **UNVERIFIED on my plane** and, read against `:594`,
  looks like a figure from a date on which a run happened, not a figure today's rebuild will reproduce.
- **So the non-null branch is, on the code as written, structurally unreachable tonight**, and the null branch
  is the one that will fire. The half covers that branch -- it says so, and the rollback holds -- so the ACT
  is covered. What is NOT covered is the fix: making the pool conform to `:753-755` is a change to
  `enrich.compute_pool()`, a file the rk-45 blast radius does not name.

I therefore record, loudly: **rk-45 as cut delivers a CONSISTENT pool read (E3) and does NOT deliver a
CONFORMANT pool value (C-EXEC-MANAGEMENT's newest-object-per-name rule).** Those are different outcomes and
the round should not read the first as the second.

**A fourth branch neither half names.** With `as_of` dropped, `read_pool_object` gains a listing step
(`:1183-1189`) that can fail: `POOL_READ_FAILED` (`:1197-1206`). On that branch `pool_document` is `None`,
`read_management` still returns `management_status SERVED` (`:2347`) with `pool_avg_tenure_years` null via
`(pool_document or {}).get(...)` at `:2358-2359`. So "SERVED with a null pool" has TWO causes after this cell
-- a genuinely null pool and a failed pool read -- and they are distinguishable only in `pool_read.status`.
The criterion must read that field or it cannot tell the two apart.

### 4. WRITER CENSUS CROSS-CHECK
The COO half prints **N = 2** writers of `_pool/<date>`: `enrich.main --write-pool` (`enrich.py:689-699`) and a
direct `crosswalk.write_pool` for this act. **I measure the same N = 2 and I confirm the cited region**:
`compute_pool` is called at `:689` and `write_pool_object` at `:690`, so `:689-699` is correct as a span
(the print block runs to `:699`). Instrument: `comp-find 'write_pool' lib/` plus a line-numbered
`git cat-file -p HEAD:lib/research/management/enrich.py | sed -n '676,695p'` -- a DIFFERENT instrument from the
COO's live-key inspection. **One refinement:** the true single writer of the KEY is
`crosswalk.write_pool` in both cases; the two entries differ in what BUILDS the payload
(`compute_pool` + `validate_pool`, versus nothing). Naming the payload-builder is what makes the census
decision-relevant here, and that is the distinction section 3 turns on.

The half's claim that no SCHEDULE writes this prefix (`OpalResearch-ExecManagement` DISABLED, chain F's census,
re-measured at spawn) is an APPLIED-plane measurement and I do not re-derive it. I note only that the
in-repo trigger surface is consistent with it: `comp-find 'raw/bloomberg' lib/` returns 11 hits, all readers
or docstrings, **no writer**.

### 5. WHAT THIS HALF DOES NOT COVER
Any change to `enrich.compute_pool()` (including the newest-object-per-name fix the PRD requires); any run of
`enrich.main --write-pool` over the covered population; any per-name `management/v1/<key>/<as_of>` write; a
second redeploy; any pool object other than `<today>`; and the criterion-literal corrections named in 2 and 3
(`pool_read.object_key`, `pool_avg_tenure_years`, `put_performed`).

---

## `AMGT-rk-47` -- Bloomberg officer fallback on the three validation names (R14-E5)

### 1. THE ACT
ONE Bloomberg `ReferenceDataRequest` (`NAME`, `COMPANY_EXEC_OFFICERS`) on CAT US / CSL AU / 6861 JP, landing
three fresh `raw/bloomberg/<key>/<stamp>/exec_officers.json` stamps put-if-absent; then `enrich` on the three
with `--skip-pool`, landing three NEW dated `management/v1/<key>/<as_of>.json` keys; `_pool/` untouched; no
Lambda, no Terraform. **This agrees with the COO half.**

### 2. THE SOURCE DIFF
**Everything this cell calls is net-new.** Measured with `comp-find <token> lib/` (182 files scanned):
`COMPANY_EXEC_OFFICERS` **0 hits**, `exec_officers` **0 hits**, `roster_source` **0 hits**, `skip-pool`
**0 hits**. The corpus-wide `COMPANY_EXEC_OFFICERS` census returns 59 hits across 66,307 files, and every
SURFACED hit is in ONE CRO deliverable
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_TAB_SCORE_REVIEW_20260915_W/{analyze,measure}.py`) --
a review script, not a producer. **There is no Bloomberg-officer fallback module in `lib/` at HEAD.**

The cell must therefore add, at minimum: the fallback module; a `--skip-pool` flag in `enrich.main` guarding
`:689-690`; `roster_source` on the document; and the fallback's own labelling.

### 3. THE PRODUCER'S RULE -- AND A REFUSAL BRANCH NEITHER HALF NAMES
`enrich.main`'s branches at HEAD, in order:

| # | branch | source | writes |
|---|---|---|---|
| 1 | document fails schema validation | `:677-679` prints `BLOCKED: the document did not validate, nothing was written`, `return 1` | **NOTHING** |
| 2 | `--write-pool` not given | `:680-684` prints `DRY: ...`, `return 0` | **NOTHING** |
| 3 | `--write-pool` given | `:685` per-name key, then `:689-690` pool | **BOTH** |
| 4 | exception in `write_document` | uncaught | nothing landed |
| 5 | exception in `compute_pool`/`write_pool_object` | uncaught | **PARTIAL: per-name key landed, pool did not** |

**Branch 1 is the one that breaks the COO half's "either branch: 3 dated keys".** `validate()` (`:460`) runs
`lib/research/management/management.schema.json`, whose top-level is `additionalProperties: false` with
properties `['absence_reason_class', 'absence_reason_evidence', 'as_of', 'avg_tenure_years',
'ceo_public_profile', 'generated', 'generated_at', 'lusha_enrichment', 'officers', 'parse_strategy',
'parser_version', 'roster_reason', 'roster_status', 'security_key', 'source_accession', 'source_item',
'source_key', 'text_normalization']` -- **`roster_source` is not among them.** The PRD requires it on every
object (`AMGT_RESAPP_PRD.md:727`: *"Every management object carries `roster_source` = FILING |
BLOOMBERG_FALLBACK."*). **So writing `roster_source` without editing the schema takes branch 1 and lands ZERO
keys with `rc=1`.** The COO half's REFUSED branch -- *"the object is written with `roster_source ABSENT` and
the reason"* -- is unreachable at HEAD's schema in EITHER direction: with the field, validation fails; without
it, the PRD clause fails. The schema edit is a repo file, not a served key, so it is arguably outside the
never-widen plane; but the OUTCOME the half signed rests on it, so I name it here rather than let a worker
discover it at `rc=1`.

**Branch 3 also writes the pool.** There is no way at HEAD to land a per-name key WITHOUT landing the pool
object: `:685` and `:690` sit under the same `--write-pool` guard and nothing between them can be skipped.
**`--skip-pool` is the entire mechanism by which rk-47's blast radius excludes `_pool/`, and rk-47 is the cell
that writes it.** The half's AC3 (pool ETag equal before and after) DETECTS a breach; it does not prevent one,
and **rk-47's half records no pre-act snapshot of `_pool/<today>.json` and no rollback for it** (it is in NOT
COVERED). Since rk-45 has already rewritten that object by the time rk-47 runs, the bytes rk-45 saved are the
PRE-rk-45 state, so nothing in chain E can restore the post-rk-45 pool if `--skip-pool` mis-fires. **THE GAP:
one branch of rk-47 (the `--skip-pool` guard not taken) writes a key no half in this chain can roll back.**
Remedy that costs nothing: rk-47's worker saves `_pool/<today>.json` bytes + sha256 + VersionId to `.scratch/`
before the first `enrich` run, exactly as rk-45 does.

**The vendor-egress branch, measured.** `build_document` calls Lusha at `enrich.py:513`
(`prospecting_page(...)`) under `if officers and company_domain:` (`:512`), and Bright Data SERP at `:532` via
`ceo_public_profile(...)` under `if officers` -- **both unconditional on any per-use-word check, and both
inside the `enrich` run rk-47 performs.** I measured whether they can fire on the three names:
`lib/research/management/domains.json` declares **5** domains -- `['BABA_US_Equity', 'BA_US_Equity',
'COST_US_Equity', 'HD_US_Equity', 'SAP_GY_Equity']` -- and **none of CAT / CSL / 6861 is among them**.
`domain_for()` (`:138-146`) returns `(None, None, reason)` for an undeclared name. Therefore at HEAD:
**no Lusha call** (the `:512` guard fails on `company_domain`), and **no Bright Data call** (`ceo_public_profile`
returns at `:425` on `if not ir_domain`, before `:430`'s `serp_brightdata`). **So rk-47 as cut makes NO vendor
call beyond the Bloomberg request it names, and the half's silence on Lusha and Bright Data is CORRECT --
by the domains table, not by a guard.** That is a load-bearing distinction: **the guard is a DATA ROW, and
adding three rows to `domains.json` would silently turn rk-47 into a cell that makes six Lusha credits' and
three SERP requests' worth of vendor egress under a half that names neither.** The order must state that
`domains.json` is NOT edited by this cell.

### 4. WRITER CENSUS CROSS-CHECK
The COO half prints **N = 1** for `management/v1/<key>/<as_of>` (`crosswalk.write_pool`, dated key) and
**N = 1** for `raw/bloomberg/<key>/<stamp>/exec_officers.json` ("the fallback module, put-if-absent").

- **Per-name key: I measure N = 1 and confirm it, with a grain correction.** The single writer at HEAD is
  `enrich.write_document()` (`:619-622`), which is the ONLY caller of `management_key()` (`:553-554`) and the
  only route to that key shape; it delegates the byte move to `crosswalk.write_pool`. Naming
  `crosswalk.write_pool` names the primitive shared with `_pool/`, one grain too coarse to discriminate; naming
  `write_document` is the property's actual writer. Same N, better grain. Instrument: `comp-find
  'management_key' lib/` + line-numbered read of `enrich.py:553-630`.
- **Raw key: I measure N = 0 at HEAD, not 1.** `comp-find 'exec_officers' lib/` = **0 hits / 182 files**;
  `comp-find 'raw/bloomberg' lib/` = 11 hits, 5 SURFACED (all docstrings in `freshness/build_view.py` and
  `identity/crosswalk.py`) and 6 TEST -- **no writer of that prefix exists in `lib/`.** The half's "N = 1
  (the fallback module, put-if-absent)" describes a module that is not in the repo. That is not an error in
  the half -- the cell builds it -- but it means **"put-if-absent" is a REQUIREMENT ON THE DIFF, not a measured
  property**, and it must be stated as such. If the new module reaches S3 through `crosswalk.write_pool`, it
  gets put-if-absent for a fresh key automatically (`crosswalk.py:628`, `IfNoneMatch: "*"`), and gets a
  CONDITIONAL OVERWRITE for a key that already exists -- not a refusal. A same-stamp collision is
  vanishingly unlikely with a fresh timestamp, but "put-if-absent" is the wrong word for what that function
  does to an existing key, and the criterion should say `put_performed True` rather than assert absence.

### 5. WHAT THIS HALF DOES NOT COVER
A fourth name; any write to `_pool/` (and note the rollback gap named in 3); any write on a covered name; the
CEO search (rk-48's); the `management.schema.json` edit that `roster_source` requires; any edit to
`domains.json` (which would open vendor egress this half does not name); and the Bloomberg terminal session
itself.

---

## `AMGT-rk-48` -- the CEO search: organizing agent over SERP records, validation names (R14-E6)

### 1. THE ACT
AC1-AC3 offline (a primitive fix in `data/find/dualbiz/scripts/serp.py`, a mutant pair, a namesake anchor, a
verbatim control) -- no live act. AC4-AC6 live ONLY under Andrew's Bright Data per-use word: at most 9 SERP
requests and an Anthropic call capped at US$2.00 on the three validation CEOs, then an in-place rewrite of the
three dated management keys rk-47 wrote. **This agrees with the COO half.** On the authorization: Andrew's
2026-09-18 ~19:4xZ word covers **Lusha** inside the three-name validation with no credit ceiling, and his
~20:4xZ answers cover the CEO-step shape (labelled links for found-but-not-read, LinkedIn link-only and never
fetched, an unlocker for 403/429 **for the CEO step alone**, a residence line permitted, contact data still
forbidden). **Neither of those is a Bright Data per-use word**, and the COO half is right to gate on the
spawn prompt naming the record. I concur with the gate as written and add nothing to it.

### 2. THE SOURCE DIFF
The existing CEO step is `enrich.ceo_public_profile()` (`enrich.py:404-453`), consuming
`data/find/dualbiz/scripts/serp.py` through `_serp_module()` (`:370-381`), which side-loads the estate module
and injects `BRIGHT_DATA_API_KEY` / `BD_SERP_ZONE` from the environment (`:373-379`) so the module makes no
secret-store call of its own. The primitive's limitation is stated in the producer's own basis string at
`:449-451`: *"title and snippet are null: that primitive returns urls only."*

That limitation is exactly what the ratified clause forbids -- `AMGT_RESAPP_PRD.md:747`: *"Each organic result
keeps its title and snippet, not the url alone."* **So AC1's "primitive fix in `serp.py`" is the change the
contract requires, and I confirm the defect at source.** The consequential edits: `ceo_public_profile` must
stop hard-coding `title`/`snippet` null (`:414`), and `management.schema.json`'s `definitions.ceo_profile`
already carries `title` and `snippet` as properties, so the SCHEMA does not block it (unlike `roster_source`
in rk-47). Verified: `ceo_profile` properties are `['absence_class', 'basis', 'ceo_name', 'ir_domain',
'query', 'snippet', 'status', 'title', 'url']`, `additionalProperties: False`. **A `ceo_profile` BLOCK with
new fields (the half's word) WILL hit `additionalProperties: False` and take `main`'s branch 1 -- nothing
written, `rc=1` -- unless the schema is extended.** Same shape as rk-47's finding, same remedy.

### 3. THE PRODUCER'S RULE, BRANCH BY BRANCH
`ceo_public_profile()` at HEAD, complete (this is the rule the rewrite must preserve or deliberately replace):

| # | branch | source | `status` | `absence_class` | vendor call |
|---|---|---|---|---|---|
| 1 | no CEO on the roster | `:418-421` | ABSENT | **NOTHING_FOUND (the `:416` default -- WRONG, nothing was searched)** | none |
| 2 | no declared IR domain | `:423-425` | ABSENT | **NOTHING_FOUND (same defect)** | **none** |
| 3 | the SERP primitive raised | `:429-433` | ABSENT | **NOTHING_FOUND (same defect)** | attempted |
| 4 | urls returned, none on the IR host | `:440-444` | ABSENT | CANNOT_SAY | yes |
| 5 | zero urls returned | `:436-439` | ABSENT | NOTHING_FOUND (correct here) | yes |
| 6 | a url on the IR host | `:446-452` | RESOLVED | null | yes |
| 7 | empty roster (built elsewhere) | `:532-536` | ABSENT | NOTHING_FOUND | none |

Branch 3 is the PRD's *"A FAILED search (a request error or an unparseable body) is recorded as FAILED, with
its cause -- never as an EMPTY search"* (`:745-746`) -- **and HEAD records it as NOTHING_FOUND, i.e. exactly
as an empty search.** Branches 1, 2, 3 and 7 all collapse into NOTHING_FOUND. **That is four of the five
ratified states missing and the wrong one asserted**, and it is the producer-side twin of the rk-43 adapter
finding. rk-48 is the cell that touches this function; if the rewrite does not fix `:416`'s default, the new
`ceo_profile` block inherits a field that lies on four branches.

**Which branch the COO half's outcomes rest on, and the gap.** The half's positive outcome (a CEO whose SERP
records anchor to the namesake control) rests on branch 6; its negative (no anchoring record, or the vendor
word absent -> `ceo_profile` ABSENT with the reason, `ceo_public_profile` unchanged, nothing rewritten) rests
on branches 4/5 and on the offline refusal. **Both are covered.** But **branch 2 fires FIRST on all three
names and neither half names it**: as measured in rk-47 section 3, CAT / CSL / 6861 are absent from
`domains.json` (5 declared), so `ir_domain` is `None` and `ceo_public_profile` returns at `:425`
**before reaching `serp_brightdata` at `:430`**. **So on the code and data at HEAD, rk-48's AC4-AC6 cannot
issue a single SERP request for the three validation CEOs.** The cell is blocked on a declared IR domain, and
the contract says where that domain may come from -- `AMGT_RESAPP_PRD.md:741-743`: *"The company domain comes
ONLY from the site the filings battery VERIFIED as the right entity -- never a hand list, never Bloomberg's
raw web address."* **Hand-adding three rows to `domains.json` is the forbidden hand list.** So rk-48's live
arm has an unstated upstream dependency on the filings battery having verified a domain for each of the three,
and neither half names it. **This is the finding I would put in front of the issuer before the spawn.**
I have NOT verified whether any other chain's cell supplies those domains -- **UNVERIFIED (the round-14
issuance is not committed; only chains I, M, F, E, P COO halves exist at `9a6aa12da2`).**

**The rewrite's own write rule.** The rewrite goes through `crosswalk.write_pool` (via `write_document`), so
every branch in the rk-45 table applies here too. Two consequences for this cell specifically: (a) if the
rewritten document is byte-identical to rk-47's, **no put happens** (`crosswalk.py:627`) and `put_performed`
is `False` -- a correct outcome that a naive "the key was rewritten" criterion grades as failure; (b) the
overwrite is `IfMatch`-conditional on the ETag read moments earlier (`:628`), so a concurrent writer yields an
uncaught 412 and **nothing is written** -- consistent with the half's radius, and the half's rollback
(saved bytes + VersionId, `copy_object` from the pre-act version) covers every branch. I confirm the rollback
is sound.

### 4. WRITER CENSUS CROSS-CHECK
The COO half prints **N = 1 active writer this round** of the three dated keys (`crosswalk.write_pool` via
`enrich`), two cells in sequence. **I measure the same N = 1** and I confirm the sequencing claim at source:
`write_document` (`enrich.py:619-622`) is the only caller of `management_key` (`:553`), and `enrich.main` is
its only caller (`:685`). Instrument: `comp-find 'management_key' lib/` plus line-numbered reads -- different
from the COO's live-key/VersionId instrument. **One addition the half does not make:** the same three keys are
also READ by `compute_pool` (`enrich.py:594-605`) whenever ANY name is enriched with `--write-pool` on the
same date, so rk-48's rewrite CHANGES A POOL INPUT even though it writes no pool object. Under `--skip-pool`
that is inert this round; it stops being inert the moment any cell runs `enrich` without the flag.

### 5. WHAT THIS HALF DOES NOT COVER
Any SERP request beyond 9; any spend beyond US$2.00; any name outside the three; any `_pool/` write; a run
without the Bright Data per-use word on file; **any edit to `domains.json`** (required for the live arm to
fire, and forbidden by `:741-743` unless the domain comes from the verified filings battery); the
`management.schema.json` extension the new `ceo_profile` block needs; the `absence_class` producer fix at
`enrich.py:416`; the five-state enum the PRD ratifies at `:750-752`; and any fetch of a LinkedIn page (Andrew:
link-only, never fetched) or any unlocker use outside the CEO step.

---

## SUMMARY OF DISAGREEMENTS AND GAPS (the finding, not smoothed over)

1. **rk-45, the act's producer is ambiguous.** "A put through `crosswalk.write_pool`" has no schema and no
   pool-building rule; the only validating path (`enrich.write_pool_object`, `enrich.py:625-630`) is reachable
   solely from `enrich.main --write-pool` (`:690`), which also writes a per-name key at `:685` -- a key the
   blast radius does not name. The order must pick one path explicitly.
2. **rk-45, `compute_pool` contradicts the ratified pool rule.** `enrich.py:594` filters per-name objects to a
   SINGLE DATE; `AMGT_RESAPP_PRD.md:753-755` requires the newest object per name across all dates and says
   "never over one run's objects". The null pool is the rule's output, not the data's. The non-null outcome the
   half expects is unreachable without either a forbidden fleet re-run or a change to a file outside the radius.
3. **rk-45/rk-48, "the object is written" is not always true.** `crosswalk.py:612-614` and `:627`: identical
   bytes are NOT rewritten, `put_performed False`, ETag unmoved. Narrower than signed, but a criterion hazard.
4. **rk-47, a schema refusal branch the half does not admit.** `roster_source` is absent from
   `management.schema.json` under `additionalProperties: false`, so `enrich.main:677-679` lands ZERO keys with
   `rc=1` -- not the "3 dated keys in either branch" the half states.
5. **rk-47, a rollback gap.** `--skip-pool` does not exist at HEAD (0 hits in `lib/`) and rk-47 is the cell that
   builds it; the branch where it mis-fires writes `_pool/<today>.json`, for which rk-47 holds no snapshot and
   rk-45's snapshot is the wrong vintage. One `.scratch/` save closes it.
6. **rk-43, the CEO reading contradicts the contract and its own comment.** `scoped_amgt.py:2264-2266` asserts
   the object carries no distinguishing field; `management.schema.json` `definitions.ceo_profile.absence_class`
   IS that field, written at `enrich.py:437/441/448`. The PRD (`:750-752`) requires rendering it in FIVE
   states; HEAD infers THREE from prose. `NOT_SEARCHED`, the value the half expects for NU, is 0 hits in
   first-party source -- an enum widening that owes a Rule 24 record.
7. **rk-48, the live arm is blocked upstream and unremarked.** CAT / CSL / 6861 are absent from
   `domains.json` (5 declared), so `ceo_public_profile` returns at `enrich.py:425` before any SERP call; the
   PRD forbids supplying the domain by hand (`:741-743`). UNVERIFIED whether another chain supplies it.
8. **Producer-side, both cells:** `absence_class` defaults to `NOTHING_FOUND` at `enrich.py:416` and four
   branches (`:421`, `:425`, `:433`, `:536`) return without changing it -- the field asserts "searched, found
   nothing" about names never searched, and about a FAILED search the PRD says must never be recorded as empty.

**RESERVED WORDS.** Nothing above is claimed as proof, root cause or definitively. Every causal statement is a
source read at `HEAD = c8989376008b7e84ccd34a92acee6cbfcb5d730c`; nothing was EXERCISED by this seat -- no
producer was run, no vendor called, no AWS read or write performed, no file in the repo edited.

Drafted `1.0.0_SA_CTO~Z`, 2026-09-18. **UNSIGNED -- this is a draft for the signer, not a co-signature.**

---

## STANDING CLAUSE -- BINDS EVERY CELL IN THIS CHAIN (added at signature, 2026-09-18 ~22:4xZ)

**THE WRITE ADDRESS COMES FROM THE BUILDER, AND A HAND-TYPED KEY IS NOT COVERED BY THIS HALF.** Every S3 address a cell in
this chain writes is `lib/opal_naming.py` `address()` output and every resource name is `name()` output (Rule 30), and the
worker's proof carries the builder's PRINTED address, never a typed one. - **The commit gate cannot catch the violation:**
measured by `4.0.0_SA_CRO~Z`, relayed by `0.0.0_AB_MSTR~Z`, the naming gate is ENFORCING (`org/mcp/naming-gate.enforce`
@`d181e0ac5a`, read at `safe-commit.sh:691` -- CLAUDE.md Rule 30's "WARN today" is stale), but its GRADER IS WIDER THAN THE
BUILDER: a hand-typed key of the shape `bloomberg/amgt/bronze/...` PASSES the commit gate while `address()` REFUSES the same
key. A worker that types an address therefore gets a GREEN commit and a key no reader resolves.
**Also measured, and the reason a builder call may REFUSE today:** AMGT has no `scopes.json` row at all (9 rows, none
`amgt`, `harvest` or `resapp`), so `address()` returns an `opal-data-harvest` address in 0 of 1350 scope x source x tier
combinations. A refusal is the EXPECTED state until the registry row lands: it is a BLOCKING row and a named refusal, never
a hand-typed workaround (Rule 30). Andrew-direct ~21:45Z: *"opal-data-assets is solely for client data ... the whole
pipeline will exist within opal-data-harvest"*.


## CTO SIGNATURE -- chain E

**Drafted by a reviewing subagent of this seat; the two items this signature turns on were RE-VERIFIED at source by
`1.0.0_SA_CTO~Z`.** (1) `roster_source` -- which ratified `C-EXEC-MANAGEMENT` requires on every management object -- is
ABSENT from `lib/research/management/management.schema.json`'s properties, and that schema sets `additionalProperties:
false`; measured with `comp-find 'roster_source' lib/research/management` -> **0 hits across 10 files scanned**. (2)
`lib/research/management/domains.json` carries **5 declared domains** (BA, COST, HD, SAP, BABA) and none of the three
validation names, so the CEO step returns before any search for CAT, CSL and 6861 -- and that table is a HAND LIST, which
`C-EXEC-MANAGEMENT` forbids as the domain source (the domain comes only from the site the filings battery VERIFIED).

- `AMGT-rk-43`: **SIGNED.** The adapter-comment defect and the five-state rendering sit inside the act's own surface, and
  the blast radius is covered on both branches.
- `AMGT-rk-45`: **WITHHELD.** The signed non-null pool outcome is unreachable: `enrich.py:594` filters the pool to a SINGLE
  date while PRD `:753-755` requires the newest object per name across all dates and says "never over one run's objects", so
  the producer's rule as written yields the null pool. **TO SIGN:** the cell changes `compute_pool` to the newest-object-
  per-name read (the same reader Posture's packs need), and the half states the outcome against the CHANGED producer.
- `AMGT-rk-47`: **WITHHELD.** With `roster_source` absent from the schema under `additionalProperties: false`, the write
  path lands ZERO keys and returns non-zero -- not the "3 keys on either branch" the COO half signs. **TO SIGN:** the cell
  adds `roster_source` and its enum to the schema in the same act, and the half covers the refusal branch explicitly.
- `AMGT-rk-48`: **WITHHELD.** The live arm cannot reach a search for any validation name (the domain table above), so the
  signed live outcome is unreachable and the cell would prove nothing on the three names. **TO SIGN:** either the cell takes
  its domain from the filings battery's verified site as the ratified clause requires, or the order re-cuts the arm as a
  declared NOT-ATTEMPTED with its reason and this half covers that instead.

Signed `1.0.0_SA_CTO~Z`, 2026-09-18, against the COO halves at `9a6aa12da2`.

---

## RE-SIGNATURE -- 2026-09-18 ~23:3xZ, against the COO halves at `541d395e0d` (msg 23855's re-cut)

`2.0.0_SA_COO~Z` bound every withheld condition in the order text and restated it in its halves. This seat read the
BOUND TEXT at `541d395e0d`, not the message's summary of it, before lifting each withholding.

- **`AMGT-rk-45`: WITHHOLDING LIFTED -- SIGNED.** The order's step 1 changes `compute_pool` to read the newest object per
  name across dates (PRD `:752-755`), and the COO half now states the non-null pool outcome against that CHANGED producer,
  with no live act before it is built and its test passes.
- **`AMGT-rk-47`: WITHHOLDING LIFTED -- SIGNED.** Step 3 adds `roster_source` and its enum to
  `management.schema.json` in the SAME act, and the half now covers the refusal branch explicitly (`541d395e0d` chain E
  `:96-102`): a write carrying the field before the schema lands writes ZERO keys with a non-zero rc, the criterion is
  recorded REFUSED naming the schema, and the rollback is a no-op. That is the branch my half said was uncovered.
- **`AMGT-rk-48`: WITHHOLDING LIFTED -- SIGNED.** The live CEO search now runs only for a name whose filings source object
  carries `rk-38`'s `verified_site`; `domains.json` is NOT a source for a validation name, and a name without a verified
  site is `NOT_ATTEMPTED / NO_VERIFIED_SITE` and counted (`541d395e0d` chain E `:127-128`). This also brings the cell onto
  the ratified rule -- `C-EXEC-MANAGEMENT` takes the domain from the battery's verified site, never a hand list -- rather
  than merely making the arm reachable.

Re-signed `1.0.0_SA_CTO~Z`, 2026-09-18 ~23:3xZ.

---

## `AMGT-rk-49` -- Lusha enrichment keyed off the battery's verified site, validation names (R14-F1; FWD-17)

**ADDED MID-ROUND, 2026-09-19 ~14:1xZ, before the cell's first live act.** Counterpart: `2.0.0_SA_COO~Z`'s re-cut
COO half section at `e29ad94617` (APPLIED/EXERCISED). **This plane: DESIRED** -- the source diff and the producer's
own rule. Neither half stands alone; the worker reads BOTH before its first live act.

⚠ **THE VINTAGE ERROR WAS MINE, AND IT IS RECORDED HERE RATHER THAN QUIETLY DROPPED.** This seat refused the first
cut (msg 23886) on five findings. **Three of them were artifacts of reading the WRONG PLANE.** I measured
`lib/research/management/enrich.py` at SITEZ HEAD `7d4e261a11` and reported that `apply_lusha_enrichment` does not
exist, that the gate reads `domains.json`, and that today's run makes ZERO billable calls. **The act does not run at
HEAD. It runs on `wk-amgt-14-50` (`311aa07b43`), where `rk-49` is the cell that RETIRES the `domains.json` gate** --
so I cited the very defect the cell exists to fix as though it were the cell's own behaviour.

⛔ **AND THIS FILE'S OWN HEADER ALREADY STATED THE RULE I BROKE:** *"Where a claim depends on code the cell has yet
to write, I mark it UNVERIFIED (diff not yet authored)."* I wrote that discipline for chain E and then, one cell
later, read HEAD as if it were the act's plane. Rule 22's GRAIN axis -- the object read IS the object claimed, **at
the vintage claimed** -- and a refusal is exactly where a wrong vintage does the most damage, because it reads as
rigour. `2.0.0_SA_COO~Z` corrected it with the branch bytes and this seat accepts the correction without reservation.

### 1. THE SOURCE DIFF, read at `wk-amgt-14-50` = `311aa07b43`
| what | state on the branch | measured |
|---|---|---|
| `apply_lusha_enrichment(document, source_object, lusha_client, dry_run)` | **EXISTS** -- factored out of `build_document` so the full pipeline and `--enrich-only` share ONE instrument, not two copies of the decision | `enrich.py:613-666` |
| `domain_for(security_key, source_object)` | signature CHANGED; reads **only** `source_object["verified_site"]["host"]`, and its docstring RETIRES `domains.json` as a Lusha input by name | `:143-172` |
| `domains.json` as a Lusha gate | **RETIRED BY THIS CELL** -- not consulted at all on this path | `:143-151` docstring |
| `basis` block on the meta | NEW: `{domain_source, verified_site, verified_host, rule}`, the derivation DECLARED and printed rather than an eTLD+1 guess | `:153-159`, `:631-633` |

So the cell moves the Lusha gate from a hand-maintained table onto the battery's own measurement, which is the rule
`C-EXEC-MANAGEMENT` already ratifies. That is the same correction chain E's `rk-48` made for the CEO search, applied
one cell later to the billable call.

### 2. THE PRODUCER'S RULE, per branch, read at source -- FOUR branches, and the ORDER of the first two is load-bearing
1. `officers and company_domain and dry_run` (`:642-643`) -> **no client constructed, nothing charged**, `status`
   stays SKIPPED, reason `"WOULD-CALL (dry run: ...)"`. ⭐ **This branch is tested FIRST, ahead of the billable one.
   That ordering is the whole guard: swap the two and a dry run charges.** The docstring states the intent and the
   code's order is what enforces it -- I checked the order, not the docstring.
2. `officers and company_domain` (`:644-657`) -> ONE `prospecting_page` call; `status CALLED`; `credits_used` is the
   **MEASURED** charge, never clipped to `CREDIT_BOUND_PER_NAME = 2` (`:53`), with a `WARN:` suffix appended when it
   exceeds the bound -- so an over-charge stays readable in the field that polices it.
3. `officers` alone (`:658-660`) -> SKIPPED, and **every officer is stamped `enrichment = "NOT-ATTEMPTED"`.**
4. `reason is None` with no officers (`:661-664`) -> SKIPPED, reason `"no officers to enrich"`, distinct from (3).

**THERE IS NO `FAILED` BRANCH.** An exception from `prospecting_page` propagates; that key is NOT rewritten and the
run exits on the traceback. The re-cut states this deliberately and I concur -- it is the one branch where "the key
is still rewritten" would have been wrong in the direction that loses data.

### 3. ⭐ THE FLAG PAIR -- the one thing neither half's prose had yet named, and it decides whether the act writes at all
The order names the act as `enrich.main --enrich-only --skip-pool`. **Run exactly that, and NOTHING IS WRITTEN.**
On the `--enrich-only` path the write sequence is `:1000-1017`: dry-run returns; `validate()` failing returns
**BLOCKED** with nothing written; then **`if not args.write_pool: print("DRY: --write-pool not given, nothing
uploaded"); return 0`** -- and only past that does `write_document` land the dated key. `--skip-pool` (`:1017-1019`)
acts AFTERWARDS and governs only whether `_pool` is recomputed.

⛔ **So on this path `--write-pool` gates the DATED KEY, not the pool, and the flag's name says the opposite.** The
act needs **both** `--write-pool` (or the three keys are never written) **and** `--skip-pool` (or `_pool` is
recomputed and rewritten, which the blast radius excludes). Named here so that a worker running the order's literal
command does not report a completed act with zero writes, and so that a reader seeing `--write-pool` on the command
line does not read it as authorization for a `_pool` write. **`--skip-pool` is what protects `_pool`; `--write-pool`
is what makes the act happen at all.**

### 4. WHAT THIS HALF CONCURS WITH, on the COO's plane
Blast radius exactly the three dated keys `management/v1/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/<as_of>.json`,
in place, the SECOND in-place rewrite in this chain; `_pool` untouched with ETag compared; no Lambda; no covered
name; writer census **N = 1** (`enrich` through the one carrier), three cells in sequence on the same keys with
`rk-49` reading `rk-48`'s object as its pre-act state; rollback per key from the pre-act VersionId with a read-back.
Which branch each of the three names takes is a DATA fact measured at run time from the battery's `verified_site`,
and it belongs to the APPLIED plane -- the COO half carries it (today: Keyence CALLED, CAT and CSL SKIPPED). This
plane certifies the RULE that maps a verified site to a branch, not today's roster of which names have one.

### 5. WHAT THIS HALF DOES NOT COVER
Any Lusha call on a name outside the three; any `_pool` write; any run without `--skip-pool`; any run lacking the
order's quoted Andrew word (*"2.) Yes full egress."*, record @`4de34f0d95`); a Lambda; a schedule; a second rewrite
of these keys by a LATER cell; and the exception path's aftermath beyond "that key is not rewritten" -- a partial
run that wrote key 1 and threw on key 2 is half-landed BY COUNT, and the entry closes only when all three keys carry
a read-back, which the COO half requires.

Signed `1.0.0_SA_CTO~Z`, 2026-09-19 ~14:1xZ, against the COO half at `e29ad94617`
(file sha256 `53050aea5df82cac98de364e3b103eb1a605b4a1b639f9935f5c60a6a062a960`, measured by this seat, matching the
prefix `2.0.0_SA_COO~Z` stated in msg 23888).
