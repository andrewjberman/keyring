# AMGT_CORPUS task order -- `CRPS-e-3` -- ROUND 3: the sector template's body becomes a function of its key (the corpus-wide total leaves the body; the disclosure stays in the printed line) so the producer re-runs on a grown corpus

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-e-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 (round-1 read, not re-run); this cell's one S3 write is gold sector-template objects through gold_put (write-once, new names only), measured by its own put.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 3. Serves **FWD-6** (the sector template is a measurement re-producible as the
corpus grows), row `AMGT_CORPUS-Z-S17`, CTO R-68.

## 1. THE CELL -- `CRPS-e-3`

**Where this came from.** `lib/research/corpus/sector_template.py` `build()` (:407-413) puts `total` (the corpus-wide report count) in
the artifact body while `_object_name()` (:431-435) hashes only `{method_version, inputs}` -- so on a grown corpus an unchanged type
gets the same name for a different body and `gold.gold_put` refuses (correctly: gold never overwrites). No consumer reads `total`
(census 2026-09-24: 0 of 30 files; the only read is this module's own `--show-first-graded` print).

**RULED -- what you build (`sector_template.py`, its tests):**
- `total` leaves `fields` and the artifact body; the denominator stays disclosed in the printed lines (`business_type %s reports %d
  of %d` at `--write` and `--show-first-graded`, computed at print time from the run's `total`); `_assemble_artifact`/`_object_name`
  unchanged otherwise, so a type whose inputs did not change mints the SAME name with the SAME body (`existed`, no refusal).
- `METHOD_VERSION` IS bumped by one (ISSUER AMENDMENT 1): removing `total` changes the body for unchanged inputs, so the
  object name must change ONCE or gold refuses the new body under the old name (row AMGT_CORPUS-Z-W3-S3). Old objects keep
  their names; after this one re-mint a grown corpus with unchanged type inputs mints nothing new.
- Tests: `body_without_total` (the artifact carries no `total`, the print line still does); `grown_corpus` (a fixture: the same
  type inputs under total 124 and total 218 produce byte-identical bodies and one name); the existing tests stay green.

## 3. SURFACES

<paths>
lib/research/corpus/sector_template.py
lib/research/corpus/tests/test_sector_template.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-3.sector-template-write-once.md
</paths>

READ-ONLY: `lib/research/corpus/gold.py`, `typed.py`, `extract.py`, `substrate.py`, `dossier.py`. Scratch `.scratch/e3/`.
Your deliverables dir: `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. No vendor call, no library write, no S3 delete; the one S3 write is `--write`'s
  write-once gold puts (new names for types whose inputs changed; `existed` for the rest).
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W3-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-e-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e3_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ deselected)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-e-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e3_AC2.sh</invocation><expect>(?s)types [1-9]\d* reports_typed \d+ unmapped_reports \d+ other_excluded \d+.*securities_typed \d+ of \d+ unmapped_securities \d+ conflicts \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-e-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e3_AC3.sh</invocation><expect>business_type \S+ reports \d+ of \d+</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: `--write` completes on the live 218-report corpus (rc 0, every type reached);
  AC3 the bound: the denominator is still disclosed where it was.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-e-3.sector-template-write-once.proof_of_spec.json`
   (keep the shape of your d-6 instance in that dir).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's `types ...` and `securities_typed ...` lines and the per-type `put_performed` counts (new vs existed).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 1 (2026-09-24 ~19:4xZ):** the RULED bullet on `METHOD_VERSION` is reversed -- the issuer's ruling not to bump it was wrong (removing a body field for unchanged inputs requires a new name once; row Z-W3-S3). And AC1's expect admits pytest's `-k`-filtered summary (`N passed, M deselected in`), which the as-cut pattern could never match (row AMGT_CORPUS-Z-W3-S4, found by `0.9.0_WK_AMGT_CORPUS~3`); at the base the check still FAILS (0 passed). Graded by: GATE (viii) (the order declares `<placeholders>`); no other limb grades a modification.

**ISSUER NOTES:** R-68's fork settled by the issuer's census (0 consumers of `total`); the intuitive fix (total into the key) is
refused there because it would mint a new object per type on every corpus growth. Checks dry-run at the base: AC1 FAIL (no such
tests), AC2 FAIL (GoldImmutableError on the first type), AC3 PASS (the print line) -- recorded in the issuance commit.

<risk>LOCAL</risk>
<status>pending</status>
<round>3</round>
<slot>~3</slot>
<fabric>site-z</fabric>
