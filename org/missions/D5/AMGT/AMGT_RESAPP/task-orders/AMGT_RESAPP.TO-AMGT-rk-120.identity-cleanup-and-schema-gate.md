# AMGT_RESAPP task order -- `AMGT-rk-120` -- the identity cleanup: (a) Z-S225, rk-114's byte-identity arm must build the PINNED side from ENRICH-free registrations so it tests the PROPERTY and not the repo's state; (b) the CTO's carried WRITE-TIME schema check, so a crosswalk that fails `crosswalk.schema.json` is REFUSED at build; CODE ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-120</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~120</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one library module and its tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; no AWS write. Any crosswalk read is
  READ-ONLY.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification; the declaration applies to the worker's
  deliverable at drain.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~120`.** Work ONLY in the worktree named in your spawn prompt. First act: print
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and test that `org/`, `.tools/`,
`lib/research/identity/crosswalk.py` and `lib/research/identity/crosswalk.schema.json` exist; if any is absent, STOP
with a BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~120;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL -- `AMGT-rk-120` (round 30, code only)

**The governing text, verbatim:**
- CTO msg 24314, carried: *"the crosswalk build does not validate at write, and only a test does. A write-time schema
  check belongs in the next identity code cell, so the next nonconforming document is refused at build and not caught
  at review."*
- CTO msg 24328: *"Identity cleanup, code only: Z-S225's pinned-module arm plus the WRITE-TIME schema check I carried
  at round 29."*
- Row `AMGT_RESAPP-Z-S225` (filed by `2.0.0_SA_COO~Z` @`24d95ac157`), which records the defect and names it an
  ISSUER-TEXT defect of the issuer's, not the worker's.

**THE MEASURED STATE (issuer, on the merged tree after rk-113's drain @`74128f4c8b`; re-measure in AC0):**
- `python -m pytest lib/research/identity/tests` reads **1 failed, 66 passed** on the MERGED tree. Each worker read
  67 passed in its own worktree, because only the merged tree carries BOTH rk-114's arm and rk-113's ENRICH row.
- The failure is `test_crosswalk_enrich_coverage.py::NoEnrichRowsByteIdentical::test_no_enrich_rows_byte_identical`,
  raising `ValueError: REFUSED: 1 security_key collision(s) ['992_HK_Equity']` from the PINNED module's `:676`, called
  at `test_crosswalk_enrich_coverage.py:265`.
- **The cause:** the arm builds the pinned (pre-rk-114) crosswalk with the **LIVE** `registrations.json`, which now
  carries rk-113's ENRICH row for `992_HK_Equity`. The pinned module has no ENRICH mode, so it refuses the duplicate
  before it can build. The arm therefore tests the repo's current state, not the property it names.
- **Production is unaffected:** at HEAD, `load_registrations()` reads 8 rows with 1 ENRICH row, and
  `build_crosswalk("2026-09-22")` returns 96 records with `denominators.enriched` 1 and Lenovo's identity present.

**RULED, LIMB (a) -- Z-S225:**
- `test_no_enrich_rows_byte_identical` builds the PINNED side from a registrations set with **ENRICH rows filtered
  out** (or from a fixture), so the arm proves "with no ENRICH row, the output is byte-identical to the pinned
  module's" regardless of what `registrations.json` carries today.
- The CURRENT-module side of the comparison is built from the SAME filtered set, so the two sides differ only by the
  module under test.
- Add an arm `test_enrich_row_present_does_not_break_the_property`: with the LIVE registrations (ENRICH row and all),
  the CURRENT module builds successfully and the PINNED module refuses -- **assert that refusal explicitly**, so the
  reason the old arm broke is itself pinned as expected behaviour rather than a surprise.
- Do NOT edit `registrations.json`, and do not remove any assertion.

**RULED, LIMB (b) -- the write-time schema check:**
- `lib/research/identity/crosswalk.py`'s pool write validates the document against
  `lib/research/identity/crosswalk.schema.json` BEFORE the put, and RAISES on a violation so nothing nonconforming is
  published. Put the check in the one place every pool write passes through (read the module and name it in your
  report); the validator is the same one `test_add_security.py` already uses.
- The refusal message names the FIRST violation (path and message), so an operator can act on it without re-running a
  validator by hand.
- A conforming document is written exactly as today -- **byte-identical**, no reordering, no added field.
- Tests, in a NEW file `lib/research/identity/tests/test_crosswalk_write_validates.py`:
  - `test_conforming_document_writes_unchanged` -- the bytes put are byte-equal to today's for a conforming document
    (stub the S3 client; capture the body);
  - `test_nonconforming_document_raises_before_put` -- inject a document with an unknown `denominators` key (the
    exact class rk-114's amendment 1 fixed) and assert the raise AND **0 puts** on the stub;
  - `test_refusal_names_the_first_violation` -- the message carries the offending path;
  - `test_live_served_document_validates` -- READ-ONLY: the current served crosswalk validates (skip with a NAMED
    reason if S3 is unreachable, never a silent pass).

**What this cell does NOT change:** `add_security.py`, the schema file itself, `registrations.json`, `battery.py`,
every S3 object, and the served crosswalk. **No live write of any kind.**

## 2. WHERE THIS CAME FROM

ROUND 30, decomposition s.38 (cut by `2.0.0_SA_COO~Z`), on the CTO's msgs 24314 and 24328 and row Z-S225.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/add_security.py
lib/research/identity/build_universe.py
lib/research/identity/tests/test_crosswalk_enrich_coverage.py
lib/research/identity/tests/test_crosswalk_write_validates.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~120/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-120.identity-cleanup-and-schema-gate.md
</paths>

- A surface not named here is a WALL, including `crosswalk.schema.json` and `registrations.json`. Scratch is
  `<worktree>/.scratch/r120/`.
- **ISSUER AMENDMENT 1 (2026-09-22, 2.0.0_SA_COO~Z, on your row W120-S1; committed by the issuer before the rebuild):**
  the write-time check as built fires ONLY from `crosswalk.py`'s `main()`. I measured the call sites myself:
  `crosswalk.py:1094` passes `document=`, but `add_security.py:180` and `build_universe.py:918` do NOT. **`add_security`
  is the path rk-113 actually published through**, so the gate misses the very route that would have written a
  nonconforming served document -- the defect it exists to refuse. So:
  - `add_security.py` and `build_universe.py` join `<paths>`, and BOTH call sites pass `document=<the document they are
    about to write>`. Change nothing else in either file;
  - add ONE arm to `test_crosswalk_write_validates.py` proving a NONCONFORMING document raises through the
    `add_security` path with 0 S3 writes (stub the client; never a live write), and ONE proving the conforming path
    still writes;
  - AC2 becomes "6 passed" (4 + 2), AC3's identity total becomes I0 + 7, and AC4's file list gains the two modules;
  - W120-S1 is then resolved; file a row that says so and cite this amendment.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~120 <0.9.0_WK_AMGT_RESAPP~120@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY.** No S3 write, no crosswalk publish, no vendor or model call. The live reads in AC0 and the two live
  arms are READ-ONLY.
- **The validator must not change what a conforming document looks like.** If making the check pass would require
  editing the schema OR the document shape, STOP with a BLOCKING row: that is a scope change for the CTO, not a
  repair.
- **One pytest call per test directory.** **Bars are AC0-measured + N**, never typed zeros.
- **THE REFUSAL CLAUSE** applies. **SURPRISE ROWS:** `AMGT_RESAPP-Z-W120-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (literal; timeout 600)

`.scratch/r120/ac0.py`:
```
import json, sys
sys.path.insert(0, ".")
from lib.research.identity import crosswalk as cw
regs, src = cw.load_registrations()
print("registrations", len(regs), "enrich_rows", [r.get("security_key") for r in regs if r.get("mode") == "ENRICH"])
doc = cw.build_crosswalk("2026-09-22")
print("HEAD build records", len(doc["records"]), "denominators", json.dumps(doc["denominators"], default=str))
r = [x for x in doc["records"] if x.get("security_key") == "992_HK_Equity"][0]
print("992 identity present", bool(r.get("identity")))
print("validator_used_by_tests", "jsonschema")
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-120"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python .scratch/r120/ac0.py &amp;&amp; python -m pytest lib/research/identity/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -1</invocation><expect>BEFORE any edit: registrations 8 with the ENRICH row for 992_HK_Equity; the HEAD build reading 96 records with denominators carrying enriched 1, and 992's identity present -- production is healthy; then the suite line reading "1 failed, 66 passed" (I0 = 67 collected), which is Z-S225. Record every value; a drifted count is RECORDED, not a fail</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-120"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/identity/tests/test_crosswalk_enrich_coverage.py -v -p no:cacheprovider 2&gt;&amp;1 | tail -12</invocation><expect>LIMB (a): "8 passed" and 0 failed -- the 7 existing arms plus test_enrich_row_present_does_not_break_the_property -- with test_no_enrich_rows_byte_identical now PASSING against the LIVE registrations, because the pinned side is built from an ENRICH-free set</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-120"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/identity/tests/test_crosswalk_write_validates.py -v -p no:cacheprovider 2&gt;&amp;1 | tail -10</invocation><expect>LIMB (b): "4 passed" and 0 failed, with the four named arms PASSED -- including test_nonconforming_document_raises_before_put asserting 0 puts on the stub, and test_live_served_document_validates (or a NAMED skip, never a silent pass)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-120"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python -m pytest lib/research/identity/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -1 &amp;&amp; python -m pytest lib/research/filings/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -1</invocation><expect>the identity suite reads "N passed" with 0 FAILED, N = 67 (AC0's collected count) + 1 new enrich arm + 4 new validator arms = 72 at the cut's baseline -- state the arithmetic from AC0's own measured numbers, not from this sentence; and the filings suite is UNCHANGED from its own pre-edit count</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-120"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git diff --name-only HEAD~1 HEAD -- lib integrations infra .tools portal &amp;&amp; git diff --stat HEAD~1 HEAD -- lib/research/identity/crosswalk.schema.json lib/research/identity/registrations.json</invocation><expect>the changed code files are EXACTLY lib/research/identity/crosswalk.py, lib/research/identity/tests/test_crosswalk_enrich_coverage.py and lib/research/identity/tests/test_crosswalk_write_validates.py; and the second diff is EMPTY -- neither the schema nor registrations.json was touched</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~120/AMGT_RESAPP.TO-AMGT-rk-120.identity-cleanup-and-schema-gate.proof_of_spec.json`,
grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4` (rc 0), flip the record face's
status to complete only if every criterion passes, commit, and report once, naming where the write-time check sits and
the before/after suite counts.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
1. **Z-S225 is the issuer's own defect**, named as such in the row: the arm was specified without stating which
   registrations it reads. Limb (a) makes the arm state its own input.
2. **Limb (b) is the control that would have caught BOTH of rk-114's amendments at the first build** rather than at
   review -- the `enriched` denominator key and the `identity` sub-schema's five missing keys.
3. The two limbs share `crosswalk.py` only through limb (b); limb (a) touches tests only.

<status>pending</status>
<round>30</round>
<slot>~120</slot>
<fabric>site-z</fabric>
