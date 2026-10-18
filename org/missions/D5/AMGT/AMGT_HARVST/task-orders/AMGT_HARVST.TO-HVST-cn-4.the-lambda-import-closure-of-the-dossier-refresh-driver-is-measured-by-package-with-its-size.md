# AMGT_HARVST task order -- `HVST-cn-4` -- ROUND 99, workstream REFRESH-HOST: THE IMPORT CLOSURE OF THE DOSSIER-REFRESH DRIVER IS MEASURED PER PACKAGE, WITH ITS SIZE AND THE MODULE THAT PULLS EACH THIRD-PARTY PACKAGE IN (READ-ONLY; it decides how the scheduled Lambda can be packaged)

<!-- ===================== WORKER FACE -- the worker's whole context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cn-4.the-lambda-import-closure-of-the-dossier-refresh-driver-is-measured-by-package-with-its-size</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cn-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~181</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL and READ-ONLY: Python imports and file-size reads on this box only. NO S3 call, NO AWS call, NO Bloomberg, NO network, NO `pip install`, NO write outside `<paths>`, NO edit of any source file (the cell reports; it does not fix).
comp-adversary: RUN at L5 -- the adversary is a closure read from the SOURCE TEXT of imports instead of from what a real import loads (a lazy import inside a function is not in the closure of an import, and a conditional top-level import is), a size taken from a package's folder name instead of from its distribution's file list, a package credited to the wrong importer (the importer is the module whose own import statement first loaded the package, recorded by a hook, never guessed), a finder that cannot see a planted import (it has a negative and a positive control), and a verdict edited to match a hope.
</preflight>

## 0. THE CELL

`lib/research/corpus/dossier_refresh.py` (merged at `56bacbc853`) will run as an AWS Lambda on a schedule (a decision of the CTO, with ECS Fargate as the fallback if the deliberate run is slow). A Lambda unzipped package, layers included, may not exceed 250 MB. A first look found that importing the driver loads, besides the standard library, these third-party packages: `numpy`, `pyarrow`, `cloudpickle`, `pandas`, `pandas_market_calendars`, `exchange_calendars`, `fitz`/`pymupdf`, `openpyxl`, `PIL`, `lxml`, `defusedxml`, `dateutil`, `pytz`, `tzdata` and a few more. **This cell measures, per package, how large each is installed, WHICH `lib` module (or package) first pulls it in, and whether that import is at module top level or inside a function.** It changes nothing.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`. Run every script from the repo root of YOUR worktree, with `python -u`, in the FOREGROUND.
a. **Write `cn4_closure.py`** in your deliverables folder. It does, in this order:
   1. Runs the real import in a CLEAN subprocess with an import hook: before importing, it installs a wrapper around `builtins.__import__` that records, for each module that is loaded for the first time, the name of the module that executed the import statement (`globals()['__name__']` of the caller). Then it executes `import lib.research.corpus.dossier_refresh` (with `sys.path[0]` = the repo root; suppress warnings with `-W ignore`). It prints `CLOSURE-IMPORTED target=lib.research.corpus.dossier_refresh modules=<n total> lib_modules=<n modules whose name starts with lib.> third_party_tops=<n distinct top-level names that are neither stdlib (sys.stdlib_module_names), nor starting with an underscore, nor lib>`.
   2. For each third-party top-level name: the distribution that owns it (`importlib.metadata.packages_distributions()`), the distribution's installed size in bytes = the sum of the sizes of the files in `importlib.metadata.distribution(<name>).files` that exist on disk (print the file count beside it); and the FIRST IMPORTER = the `lib.` module that is the earliest `lib` module in the recorded chain (walk the hook's importer chain from the package up to the first name that starts with `lib.`; if a third-party package pulled it, print that package and continue the walk to the `lib.` module). Print one line each, sorted by size descending: `PKG <top-level> dist=<dist name> version=<v> mb=<size in MB, 2 decimals> files=<n> first_lib_importer=<module or NONE> via=<the immediate importer>`.
   3. For each `lib.` module in the closure, a STATIC check with `ast`: does it import a third-party package at MODULE TOP LEVEL (an `import`/`from` statement in the module body, including inside a top-level `try:`), or only inside a function? Print `LIBIMPORT <lib module> top=<third-party tops imported at top level, comma-joined or none> lazy=<third-party tops imported only inside functions, comma-joined or none>`.
   4. Sums: `lib_code_mb` = the total size of the `.py` files of the `lib` modules in the closure; `third_party_mb` = the sum over the distributions printed in 2 (count a distribution once, even if two top-level names belong to it); `total_mb = lib_code_mb + third_party_mb`.
   5. **The controls (rule 22):** POSITIVE: run the same measurement for the target `lib.research.harvest.store` and print `CONTROL-POSITIVE target=lib.research.harvest.store pyarrow_in_closure=<yes|no>` (`store` is known to pull `pyarrow` and `numpy`; if the answer is `no`, print it plainly and do not hide it). NEGATIVE: the same measurement for the target `json` (standard library only) prints `CONTROL-NEGATIVE target=json third_party_tops=0` (any other number means the finder is wrong: STOP and file a row).
   6. The last line, exactly: `LAMBDA-CLOSURE lib_modules=<n> third_party_pkgs=<n distinct distributions> third_party_mb=<x.xx> lib_code_mb=<y.yy> total_mb=<z.zz> limit_unzipped_mb=250 verdict=<UNDER|OVER> biggest=<the three biggest distributions by size, name:mb, comma-joined> removable_by_lazy=<the third-party tops whose only importers in the closure import them inside functions, or none>`.
b. Stdout goes to `cn4_closure.out` (open it with `newline="\n"`), made by this one command run once: `python -u org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~181/cn4_closure.py > org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~181/cn4_closure.out`. **The verdict and the sizes are the FINDING: do not change anything to make them read a particular way.** If `verdict` is OVER, that is the answer the issuer needs, not a failure.
c. File ONE surprise row summarising the finding (the verdict, the three biggest packages and which `lib` module pulls each in); do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~181/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cn-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~181/cn4_closure.out</invocation><expect>(?m)^LAMBDA-CLOSURE lib_modules=\d+ third_party_pkgs=\d+ third_party_mb=\d+\.\d\d lib_code_mb=\d+\.\d\d total_mb=\d+\.\d\d limit_unzipped_mb=250 verdict=(UNDER|OVER) biggest=\S+ removable_by_lazy=\S+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cn-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~181/cn4_closure.out</invocation><expect>(?s)CONTROL-POSITIVE target=lib\.research\.harvest\.store pyarrow_in_closure=yes.*CONTROL-NEGATIVE target=json third_party_tops=0</expect></criterion>
</proof_of_spec>

- AC1 is the finding (its numbers and verdict are what they are). AC2 holds both controls (the finder sees `pyarrow` where it is and nothing where there is nothing). **If a line reads otherwise, DO NOT edit the expectation or the finder to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~18:5xZ):** both FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W181-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~181/AMGT_HARVST.TO-HVST-cn-4.the-lambda-import-closure-of-the-dossier-refresh-driver-is-measured-by-package-with-its-size.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cn-4.the-lambda-import-closure-of-the-dossier-refresh-driver-is-measured-by-package-with-its-size` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cn-4.the-lambda-import-closure-of-the-dossier-refresh-driver-is-measured-by-package-with-its-size.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Why this cell now (a WHILE-BLOCKED cell, `/next-calls --drive`, 2026-10-18 ~18:4xZ).** `cn-3` (SC1's deliberate run) is the measurement the schedule's host waits on; this cell is the other fact the host and the packaging wait on and it needs no run: my own check found that importing `dossier_refresh` loads `pandas`, `pyarrow`, `exchange_calendars`, `fitz`, `lxml` and more (two of the pulls traced to `lib.trading_calendar` and `lib.research.harvest.store`; the others are what this cell finds). A Lambda's 250 MB unzipped cap may be breached by that closure alone, which would decide Lambda against Fargate or force a lazy-import change to the product, whichever the CTO rules.
- Authority: the CTO's round-98 addendum 2 (@6135e9a0fb): Lambda unless `cn-3` measures over 600 s; the CRO's research (@25586b74c0, section 4) names packaging as the open item: "the harvest root already builds two Lambdas, so that is the existing path", which this cell tests. Decomposition section 138.
- Dry run at the base: both criteria FAIL as expected (the file does not exist).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>99</round>
<workstream>REFRESH-HOST</workstream>
<slot>181</slot>
<fabric>dell1</fabric>
