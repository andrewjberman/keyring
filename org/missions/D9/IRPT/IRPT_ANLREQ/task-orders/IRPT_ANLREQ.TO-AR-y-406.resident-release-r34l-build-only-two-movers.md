# TO IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers -- BUILD ONLY: build the resident tarball and its host scripts twice at one pin, with the r34k tool copied to r34l, and diff it against the running r34k tarball: exactly four members move (SHA256SUMS, reports/resident_bindings.json, ycharts/research/opal_producer.py, reports/resident_installed.py); nothing is uploaded, installed, applied or run on a host

<to_id>IRPT_ANLREQ.TO-AR-y-406</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~306</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ66</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a build in a stage folder outside the repository; the only repository writes are the worker's deliverables)
**Decomp cell:** `AR-y-406` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a clean report) | **depends_on:** `AR-y-404` (merged `3676d5836b`), `AR-y-408` (merged `31c3dc1d4f`), CTO msgs 10696 and 10759

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~306`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-306` (branch `wk-IRPT_ANLREQ-306`), provisioned by the issuer from the current branch (sparse: the tool folder, the producer folders and the r34k record are included). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~306 <0.9.0_WK_IRPT_ANLREQ~306@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture: never commit it. A row id has the form `IRPT_ANLREQ-D2-W306-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions). Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (ruff clean: no single-letter names `l`, `O`, `I`; no non-ASCII).
- **BUILD ONLY.** No upload, no install, no AWS call of any kind, no network, no host command, no push. The stage folder is OUTSIDE the repository and must not exist before the build. Never `rm -rf` a folder you did not create.

### THE CELL (AR-y-406, inlined)

*Context.* The resident host runs release `irpt-resident-0485393f3a-r34k` (tarball sha256 `64f5567dddbd7e96a955410e7e12c5fb3f319551fbe9ce1527cdefdfe8f18a0c`, 317 members; stage folder `C:/dev/irpt-release-r34w/` holds `irpt-resident-0485393f3a-r34k.tar.gz`, its `package.SHA256SUMS` and the host `scripts/`). Two code changes must reach the running resident: `AR-y-404` and `AR-y-408` (the producer's report sections skip builder-only and NOT_IN_THIS_VERSION entries and the last disclosure counts them, `ycharts/research/opal_producer.py`, merged `3676d5836b` and `31c3dc1d4f`) and `AR-g-161` (the pricing as-of date follows the trading-calendar frontier, `reports/resident_installed.py`, merged `87c9948811`). The release machinery is `2.0.0_SA_COO~G2`'s r34 set under `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`: `r34k_build.py` (the driver; its docstring is the spec), `build_resident_package.py` (the builder: members are taken AT THE PIN only for the paths in `files_from_r34.txt` (41 files, which names both `reports/resident_installed.py` and `ycharts/research/opal_producer.py`) and at `--base-pin 0485393f3ad0a7e564f4867f5e70003e2e62195b` otherwise), `pack_r34.py`, `run_builder_fixed_clock.py`, `make_scripts_r34k.py`, `smoke_imports_r34.py`. The r34k record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/r34k/RESIDENT_R34K_BUILD.json` shows the result of the last such build. Measured by the issuer: `lib/trading_calendar.py` is a `--member` entry that reads the file at the PIN, and `_authz/served.py` is NOT in the files-from list (so it stays at the base pin); the files-from list is therefore the release's mover filter.

*What to do.*
1. Make a folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/`. The first seat of this order (`0.9.0_WK_IRPT_ANLREQ~297`, merged `b209b28aec`) already wrote and committed the three files this build needs, in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~297/r55/`: `r34l_build.py`, `make_scripts_r34l.py` and `check_r34l_record.py` (read-only for you; `git show HEAD:<path>` if absent). Copy the three into `r56/` unchanged and read `r34l_build.py` once: it must carry the old root (`R32_DIR = "C:/dev/irpt-release-r34w"`, the r34k tarball sha256 `64f5567dddbd7e96a955410e7e12c5fb3f319551fbe9ce1527cdefdfe8f18a0c`), `delta_vs_r34k`, `EXPECT_CHANGED = ["SHA256SUMS", "reports/resident_bindings.json", "ycharts/research/opal_producer.py", "reports/resident_installed.py"]` and `EXPECT_ADDED = []`, and every output name reading r34l. Change only a word that still names an r34k output or a path under `r55`; any other edit is a BLOCKING row. Record the sha256 of each of the three copies in the record. `check_r34l_record.py` is the acceptance script of this order (it prints the two lines in ACCEPTANCE); run it against the base state (record absent) and against a mutated copy of the record with a fifth changed member (BAD) before relying on it.
2. The pin is `e30c79da3ff6e3166f72b7f8757377ae751a1e2c` (the issuer's scratch branch `scratch/r34l-pin`: the trunk HEAD `956b593a20` with ONE edit, `lib/trading_calendar.py` held at the r34k blob `72178007dd`, because the trunk's version is DASHBD's `f25618c0b4`, which rides its own pair and is read by the builder as a `--member` at the pin; it contains `AR-y-404`, `AR-y-408`, `AR-g-161` and the five tools unchanged). Before the real run print the actual member difference the way the driver computes it, and STOP if it differs from the four members above: a fifth mover, a missing mover or an added member is a BLOCKING surprise row naming it (and NOT a loosened expectation).
3. Run `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/r34l_build.py --pin e30c79da3ff6e3166f72b7f8757377ae751a1e2c --out C:/dev/irpt-release-r35b --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/RESIDENT_R34L_BUILD.json` from your worktree (it needs several minutes: give each command up to 600 s). It prints `R34L-BUILD-OK <members> ...` or `R34L-BUILD-BAD <why>`.
4. Print, from the record, the tarball sha256 and member count, the two-build identity line, the delta against r34k (changed, added, removed), the import smoke line, the gate dry-run return codes, and the sha256 of each of the four host scripts. Also print the `git diff --stat` of `opal_producer.py` and `reports/resident_installed.py` between the r34k scratch pin `1ad8bd8c1bb83ecc35d9489014a42c53812f4424` and the build pin (the two movers' own diffs, by number of lines).
5. Commit `r34l_build.py`, `make_scripts_r34l.py` and the record (the stage folder stays outside the repository). Then write the proof instance and flip the order only after the checker prints VALID: copy the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~296/IRPT_ANLREQ.TO-AR-y-404.report-sections-exclude-builder-only-entries.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly `IRPT_ANLREQ.TO-AR-y-406`, real `controls.mutant` (for example the driver run against a copy of the record with one member name changed, or the gate dry-run's one-byte copy refusing, whichever you ran) and `controls.determinism` (build_a equals build_b); commit it, run `python .tools/proof-of-spec-check.py <instance> "AR406-y-AC1,AR406-y-AC2"`, and flip `<status>` to `complete` (commit alone) only on VALID.

---

## ACCEPTANCE

<criterion id="AR406-y-AC1" cell_refs="AR-y-406"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/check_r34l_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/RESIDENT_R34L_BUILD.json</invocation><expect>R34L-RECORD-OK changed=4 added=0 removed=0</expect></criterion>
<criterion id="AR406-y-AC2" cell_refs="AR-y-406"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/check_r34l_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/RESIDENT_R34L_BUILD.json --identity</invocation><expect>R34L-IDENTITY-OK builds_identical=yes smoke_fail=0</expect></criterion>

You also write `check_r34l_record.py` in the same folder (a small script, ruff clean): it reads the record JSON and (no flag) prints `R34L-RECORD-OK changed=<n> added=<n> removed=<n>` only when `delta_vs_r34k.changed` equals exactly the four members above, `added` and `removed` are empty, and the artifact has a 64-hex sha256 and a member count; otherwise `R34L-RECORD-BAD <why>` and a non-zero exit. With `--identity` it prints `R34L-IDENTITY-OK builds_identical=yes smoke_fail=0` only when `two_builds.files_compared == two_builds.identical` and the import smoke line reads `fail=0`. Run both against the base state (the record absent: BAD or an error) and against a mutated copy of the record with a fifth changed member (BAD) before relying on them.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-406`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR406-y-AC1,AR406-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-406</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a build in a stage folder outside the repository and copies of two tool files in the worker's deliverables; nothing is uploaded, installed, applied or run on a host.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- by reading r34k_build.py and files_from_r34.txt against this cell; the lens: a fifth mover riding the files-from list (STOP, a row, no loosened expectation), a rename that leaves an r34k name in an output (the record and the tarball name must read r34l), the base tarball not equal to the one running (the sha256 gate), the clock not fixed (builds differ), the stage folder created inside the repository (refused), the folder `C:/dev/irpt-release-r35a` left by the first seat's failed build (do not use or delete it; the stage folder of this order is `C:/dev/irpt-release-r35b`), a gate dry-run that cannot fail (the one-byte copy must refuse). NOT seen (blind): the live host, the live root and the release key; denominator: two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's TOP PRIORITY ruling (msg 10696): the release pair and IB2's apply follow this build. The issuer writes the never-widen packet from the record and the CTO half signs before IB2 acts. G2 (`2.0.0_SA_COO~G2`) named `AR-g-161` as a mover (msg 10711) and `lib/trading_calendar.py` as pinned on purpose at the r34k scratch pin (msg 10722). Base: the record and the check script are absent, so `AR406-y-AC1` and `AR406-y-AC2` FAIL as expected.
