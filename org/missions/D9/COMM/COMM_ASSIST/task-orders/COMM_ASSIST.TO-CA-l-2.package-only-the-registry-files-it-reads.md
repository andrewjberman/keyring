# TO COMM_ASSIST.TO-CA-l-2 -- round 20 CA-l-2: build.sh packages only the registry files the assistant reads (a manifest, not a glob)

<to_id>COMM_ASSIST.TO-CA-l-2</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~30</issued_to>
<issued_by>2.0.0_SA_COO~CA</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>BUILDNARROW</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-l-2` (`decompositions/COMM_ASSIST_DECOMP.round20.md`) | **outcome_ref:** FWD-4, FWD-13 (every deploy of the assistant carries less foreign payload) |
**depends_on:** none (CTO round-19 analysis ruling 2, msg 109356; PRD v0.10 ADMITTED). Risk WORLD is the INFERRED FLOOR for an edit under `infra/` (spine v3.19 L6); this order is an EDIT ONLY and deploys nothing: the real run is the later deploy cell CA-l-4.

---

## WORKER FACE

### THE CELL

`infra/aws/lambda/teams-chat-assist/build.sh` packages the assistant's Lambda zip. It copies EVERY file of `infra/logic/registry/*.json` (17 files, about 1.09 MB), although the assistant opens only twelve of them; one of the rest, `catalog_fork_keys.json`, is 4,954 lines of another project's rows, and every deploy has to re-clear it with 17 equivalence probes. You make the build copy ONLY the registry files the assistant reads, named in a manifest file, and nothing else about the package changes. This cell is code only; a later cell deploys it.

### THE CONTRACT (fixed by the issuer; the issuer's check pins every point)

Your whole interface is the header and arms of `org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m2_build.py` (it is in your worktree at HEAD; READ it first and do not edit it).

1. A NEW file `infra/aws/lambda/teams-chat-assist/registry_files.txt`: one registry file NAME per line (for example `scopes.json`), blank lines and lines starting with `#` ignored. It lists exactly these twelve, which the issuer measured as the files the assistant opens or names (a trace of the 17 probes plus a static scan of the packaged code): `exemptions.json`, `feeds.json`, `firm_pages.json`, `legacy_addresses.json`, `mail_parties.json`, `platinum_destinations.json`, `remediations.json`, `reporting_policies.json`, `resources.json`, `scopes.json`, `systems.json`, `tiers.json`. A short `#` header says what the file is and that a registry file the assistant starts to read must be added here.
2. `build.sh` replaces the line `cp "$REPO"/infra/logic/registry/*.json "$PKG/infra/logic/registry/"` with a loop that reads that manifest from `$SRC` (the agent's own folder), strips a trailing CR from each line, REFUSES (exits non-zero with a one-line message) a name containing a path separator or a name absent from `$REPO/infra/logic/registry`, and copies only the listed files. Use a `REG="$REPO/infra/logic/registry"` variable so `tests/test_build_reproducible.py` (which sets `OPAL_BUILD_REPO`) still finds its inputs. The manifest itself is NOT copied into the package. Nothing else in `build.sh` changes, and the zip stays reproducible (fixed timestamps, LF text).
3. The other packaged files are byte-identical to the full build. No packaged code, no Terraform and no registry file is edited.

### RULES

- Edit nothing but the files in `<paths>`. Standard shell only (Git Bash). No non-ASCII. Do not run a deploy, an apply or any AWS call; `dist/` is never committed.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAl2-AC1" cell_refs="CA-l-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r20/checks/check_m2_build.py"</invocation><expect>M2-BUILD ok=True arms=7 of 7</expect></criterion>
`CAl2-AC1` -- the issuer's check (read it; do not edit it), run from your worktree root by that RELATIVE path: it builds YOUR `build.sh` into a temp folder and requires the manifest to exist and name a strict subset of the registry; the package's registry files to equal the files the assistant opens under the 17 probes and names in its packaged code; the 17 probes to give identical output from the narrowed and the full package; no registry file in the zip that nothing opens or names; the zip reproducible (two builds, one sha256); `catalog_fork_keys.json` absent; every non-registry file byte-identical to the full build. It prints 3 of 7 at the base.

<criterion id="CAl2-AC2" cell_refs="CA-l-2"><invocation>python infra/aws/lambda/teams-chat-assist/tests/test_build_reproducible.py</invocation><expect>PACKAGE-REPRODUCIBLE ok=True</expect></criterion>
`CAl2-AC2` -- the bound, a control that PASSES at the base (39 files): the package's bytes do not depend on the working tree's line endings. After your change the file count is lower; the verdict must stay `ok=True`.

<criterion id="CAl2-AC3" cell_refs="CA-l-2"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py"</invocation><expect>I2-REGRESSION ok=True</expect></criterion>
`CAl2-AC3` -- the bound, a control that PASSES at the base (64 passed): the assistant's flow tests (the code is untouched; this guards the worktree).
</proof_of_spec>

<expected_criteria>CAl2-AC1,CAl2-AC2,CAl2-AC3</expected_criteria>

Each invocation runs from the worktree root, by that RELATIVE path, under `timeout 280`. Commit the code FIRST. Then write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~30/COMM_ASSIST.TO-CA-l-2.package-only-the-registry-files-it-reads.proof_of_spec.json`, modelled on `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~29/COMM_ASSIST.TO-CA-k-3.batch-repair-stale-tests-and-reader-text.proof_of_spec.json`, recording each invocation EXACTLY as the criterion text (no `timeout` prefix) and pinning each artifact row to the commit that carried it (a row left as pending-this-commit goes INVALID the moment a later commit lands). Flip `<status>` to `complete` only when all three pass. Validate with the WORKTREE'S OWN `.tools/proof-of-spec-check.py` from inside the worktree AFTER your last commit: `python .tools/proof-of-spec-check.py <instance> CAl2-AC1,CAl2-AC2,CAl2-AC3`, and read the LAST line: it must be `VALID (rc=0)` at the final head. Your final report names the changed lines, the manifest's twelve names, the file count before and after, and the deciding line of each criterion. Your surprise rows are `COMM_ASSIST-W30-S<k>`; append only to the investigation file and keep its existing line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh` as your serial; write the commit message file with your Write tool (never a shell heredoc), ending with the attribution line the harness gives you.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round20.md</decomp_doc>
<owned_cells>CA-l-2</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/teams-chat-assist/build.sh
infra/aws/lambda/teams-chat-assist/registry_files.txt
org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-l-2.package-only-the-registry-files-it-reads.md
org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~30/
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves and no AWS call is made; the deploy is a later cell with its own pair.
comp-adversary: RUN -- a registry file the assistant needs dropped from the package so it fails at run time on a path the probes do not exercise (named, partly refused: AC1 `trace_equal` compares the zip with a trace of the 17 probes AND a static scan of the packaged code; the omit-a-read-file controls fail `trace_equal` or `probes_same`; BLIND to a registry file opened lazily on an unexercised path, which is why the manifest header tells the next editor to add a file the assistant starts to read, and the deploy cell re-runs the equivalence probes against the live package); an unused file kept (refused: AC1 `no_unreferenced` and `foreign_absent`); a build that stops being reproducible (refused: AC1 `reproducible`, AC2); a non-registry file changed (refused: AC1 `other_bytes`); a manifest name with a path or a missing file silently ignored (the contract makes the build refuse it).
naming: no name is created beyond the manifest file's own (CLAUDE.md rule 30 non-application: a tool-side list, not a pipeline address or resource name).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Base: CAl2-AC1 base: FAIL as expected (3 of 7: `manifest_list`, `trace_equal`, `no_unreferenced`, `foreign_absent` fail), measured by the issuer on the trunk; the green arm: PASS as expected (7 of 7) against a scratch reference in a throwaway mirror (since removed), with a CRLF manifest as well as an LF one; negative controls: omit `firm_pages.json` fails `trace_equal` only, omit `scopes.json` fails `trace_equal` and `probes_same`, add `root_map.json` fails `trace_equal` and `no_unreferenced`, add `catalog_fork_keys.json` fails those and `foreign_absent`. CAl2-AC2 base: PASS as measured (`PACKAGE-REPRODUCIBLE ok=True`, files=39). CAl2-AC3 base: PASS as measured (control, 64 passed).
Source: CTO round-19 analysis ruling 2 (`ledger/ROUND_ANALYSIS.round19.md` @b4f6d499d0, msg 109356); the CVO's note on the foreign payload (CA-k-4 half); `lib/opal_naming.py` `load_registry` (opens a fixed 11-name tuple), `mail_requests.py` (opens `mail_parties.json`), the issuer's trace.
