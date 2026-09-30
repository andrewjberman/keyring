# AMGT_RESAPP task order -- `AMGT-zz-4` -- THE BUILD PRINTS ITS CONTENT DIFF; `REGISTRY_HASH` IS SCOPED; RESTAMP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-zz-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~183</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no apply, no upload; the content diff READS the deployed artifact (lambda:GetFunction + its code location) with the seat's existing credentials.
comp-adversary: RUN by the issuer at the cut -- AC2 edits an unrelated and a related registry row on a temp copy; AC3 mutates one packaged file and adds one on a copy of the deployed zip.
EGRESS CLASS, declared: NONE. Opal's own AWS, read-only. The full build (which pip-downloads wheels) is NOT run by this order.
</preflight>

## 1. THE CELL -- `AMGT-zz-4` (round 51, decomposition s.59)

`infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` builds the `opal-amgt-scoped-api` artifact. At `:123` it runs
`gen_harvest_prefixes.py --check` under `set -e`, which compares a fresh render of `lib/research/api/_harvest_prefixes.py` byte for
byte -- including `REGISTRY_HASH`, a hash of ALL seven `infra/logic/registry/*.json` files. Any unrelated registry admission turns it
RED while the four prefix constants stay byte-identical (today: stamped `3118e82e...`, fresh `54d1865c...`), four times so far. And a
never-widen half once read packaging from code comments (`lib/opal_naming.py` IS packaged; the generated module's docstring still says
it is not). Build three things:

1. **The content diff.** A new `infra/aws/terraform/harvest/content_diff.py --zip <zip>`: fetch the artifact the live function runs
   (`lambda.get_function(FunctionName="opal-amgt-scoped-api")`, `Code.Location`, read-only) and compare every file of `<zip>` with it,
   printing one line per file `CONTENT-DIFF <IDENTICAL|CHANGED|ADDED|REMOVED> <archive path>` and then ONE line
   `CONTENT-DIFF SUMMARY: files N, IDENTICAL i, CHANGED c, ADDED a, REMOVED r, against <CodeSha256>` (N = files in `<zip>`). Compare
   file CONTENTS, not zip metadata. Exit 0 when it printed (a CHANGED file is a report, not a failure). The build script calls it on
   the zip it builds, after packaging and before any upload, in both `--build-only` and upload modes. It is a report inside the
   existing script, not a new approval gate.
2. **The scoped stamp.** `gen_harvest_prefixes.py` gains `scoped_registry_hash(registry_dir=None) -> str` hashing ONLY what the four
   constants derive from (today: `systems.json` rows `amgt`, `seeking-alpha`, `bright-data`, `bloomberg`, and `scopes.json` row
   `harvest` -- confirm by reading `compute()`), canonicalised (sorted keys) so formatting noise does not move it; `REGISTRY_HASH`
   is that value, and `--check` compares against it.
3. **The restamp** with `--write`; its diff must show the four constants UNCHANGED (only the hash line and the header comment move).
   Correct the generated module's docstring about `lib.opal_naming` (it is packaged transitively). Update
   `lib/research/api/tests/test_harvest_prefixes.py` if it asserts the old hash rule.

## 2. BOUNDS

1. The five files named in SURFACES. NO `safe-apply`, no `terraform`, no upload, no build run with upload; `--build-only` may be run
   for your own curiosity but it is not a criterion (it exceeds the 120 s bound -- the one build in AMGT-zz-8 exercises it). No
   registry JSON is edited. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/content_diff.py
infra/aws/terraform/harvest/gen_harvest_prefixes.py
infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh
lib/research/api/_harvest_prefixes.py
lib/research/api/tests/test_harvest_prefixes.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~183/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-zz-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_4_stamp.py; echo "exit=$?"</invocation><expect>(a) --check rc=0; (b) 4 of 4 byte-equal, moved []; THE STAMP IS GREEN AND THE FOUR CONSTANTS DID NOT MOVE: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-zz-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_4_scope.py; echo "exit=$?"</invocation><expect>(a) unrelated edit UNCHANGED; (b) amgt row edit CHANGED; THE REGISTRY STAMP IS SCOPED TO WHAT THE CONSTANTS READ: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-zz-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_4_diff.py; echo "exit=$?"</invocation><expect>CONTENT-DIFF SUMMARY: files 345, IDENTICAL 343, CHANGED 1, ADDED 1, REMOVED 0 (the deployed file count, whatever it reads, plus one); CHANGED lines ['lib/opal_naming.py']; THE BUILD'S CONTENT DIFF NAMES WHAT CHANGED AGAINST THE DEPLOYED ARTIFACT: YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the restamp with the constants held; AC2 the scope (the unrelated edit is its own difference control); AC3 the printout (the
mutated file is its control).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~183/AMGT_RESAPP.TO-AMGT-zz-4.content-diff-and-scoped-stamp.proof_of_spec.json`. Report once: which registry rows the scoped hash covers and how you confirmed it, where the build script calls the diff, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-50 analysis ruling 4 (rows Z-S306, Z-S307). Base: AC1 FAIL (--check rc=1, constants 4 of 4 equal); AC2 FAIL (no
scoped_registry_hash); AC3 FAIL (no content_diff.py). Control on the deployed zip at the cut: 40.1 MB, 344 files, lib/opal_naming.py
packaged. `<risk>` WORLD is the path floor (infra/); the order applies nothing. Cut to a worker, not AE~A, because every criterion is
bounded under 120 s and the write surface includes lib/**, which no AE lane holds.

<status>complete</status>
<round>51</round>
<slot>~183</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
