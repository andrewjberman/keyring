# TO NFRA_CTLPLN.TO-CT-i-8 -- workstream INBOUND round 5 CT-i-8: the Teams agent's package is byte-identical whatever line endings its inputs have in the working tree

<to_id>NFRA_CTLPLN.TO-CT-i-8</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~36</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>INBOUND</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-i-8` (`decompositions/NFRA_CTLPLN_DECOMP.inbound5.md`) | **outcome_ref:** FWD-20 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-i-8`. The Teams agent's function package is built by `infra/aws/lambda/teams-chat-assist/build.sh`: it copies files from the
repository into `dist/pkg` (the agent's own folder, two End of Day files, `lib/opal_naming.py`,
`org/standards/NAMING_SCHEMA.json`, every `infra/logic/registry/*.json`) and zips them with fixed timestamps "so identical
inputs give an identical zip". Its header says the package's hash is stable.

It is not, on this machine. Measured by the seat that deployed it on 2026-10-08 (row NFRA_CTLPLN-S27): a rebuild from a fresh
checkout of the LAST deployed commit `55cb79f93c` gave a different hash from the deployed one, because "two packaged registry
files sit CRLF in the shared tree and LF from a fresh checkout". So the package's bytes depend on the line endings of the
working tree it was built in, and a rollback cannot be rebuilt to a known hash. The ruling: "The package's dependence on line
endings is a build defect: a cell, naming the two registry files."

**You deploy nothing, apply nothing and upload nothing.** `dist/` is a build product and is never committed.

### BUILD, IN THIS ORDER

1. **Measure first**, in your deliverables folder, `PACKAGE_LINE_ENDINGS_MEASURED.md`:
   - for every file `build.sh` copies, its line endings in the index and in THIS worktree (`git ls-files --eol <path>`), and
     the same read made in the shared tree with `git -C <the main worktree, from git worktree list> ls-files --eol <path>`
     (a read; change nothing there);
   - the files that differ between the two trees: name them (the row says two registry files), and say what makes them
     differ (an attribute, a setting, an editor's write), from `git check-attr -a <path>` and `git config --get core.autocrlf`
     read in both trees;
   - the package SHA-256 from one build in this worktree as it is.
2. `infra/aws/lambda/teams-chat-assist/build.sh`: make the package independent of the working tree's line endings, by the
   smallest change. The intended shape, unless your measurement shows it cannot work: every TEXT file copied into `dist/pkg`
   (`.py`, `.json`, `.md`, `.txt`) is written with LF line endings whatever it has on disk; any other file is copied as it
   is. Do it inside the packaging step, not by changing any file in the repository, any git attribute or any git setting.
   Keep the fixed timestamps, the sorted order and the header's claim, and add one comment line saying the package's bytes
   do not depend on the working tree's line endings and how.
3. NEW `infra/aws/lambda/teams-chat-assist/tests/test_build_reproducible.py` (a plain script, no network): it runs the real
   `build.sh` twice against two temporary copies of the build's INPUTS (found by reading `build.sh`, not by a typed list
   where a glob is used), one copy with every text input converted to CRLF and one with LF, each into its own temporary
   output, and compares the two zips' SHA-256; then a third build of the unmodified worktree. If `build.sh` cannot be pointed
   at another input root and output folder, add the two environment overrides it needs (`OPAL_BUILD_REPO`,
   `OPAL_BUILD_DIST`), defaulting to today's paths. LAST line
   `PACKAGE-REPRODUCIBLE ok=<True|False> crlf_sha=<12 hex> lf_sha=<12 hex> worktree_sha=<12 hex> files=<n>`; `ok=True` needs
   all three equal.
4. Finish `PACKAGE_LINE_ENDINGS_MEASURED.md`: the package's SHA-256 before and after your change in this worktree; and one
   paragraph on what the change means for the deployed function: the next deploy's package hash will differ from the live
   one even with no source change, if the live one was built with CRLF inputs; say whether your measurement shows that.

### RULES FOR THIS CELL

- **Deploy nothing.** No `terraform`, no `safe-apply`, no `aws` call of any kind, no upload. Nothing leaves this machine.
- Change no file in the shared tree, no git attribute and no git setting, in any tree. Reads there are allowed.
- Edit nothing but the two files in `<paths>`. `dist/` and every temporary build are never committed.
- No non-ASCII in any file you write. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTi8-AC1" cell_refs="CT-i-8"><invocation>python infra/aws/lambda/teams-chat-assist/tests/test_build_reproducible.py</invocation><expect>PACKAGE-REPRODUCIBLE ok=True</expect></criterion>
`CTi8-AC1` -- the built behaviour and its difference control in one run: the real build script on CRLF inputs and on LF inputs gives one package.

<criterion id="CTi8-AC2" cell_refs="CT-i-8" judgment="true"/>
`CTi8-AC2` -- JUDGMENT, never self-graded: `PACKAGE_LINE_ENDINGS_MEASURED.md` names the files that differed and their cause from reads, and states what the change does to the next deploy's hash.
</proof_of_spec>

<expected_criteria>CTi8-AC1,CTi8-AC2</expected_criteria>

The invocation runs under `timeout 120`. Record `CTi8-AC2` in the instance with NO verdict (status
`UNVERIFIABLE-BY-INSTRUMENT`, the reason naming `3.0.0_SA_CVO` as its grader). Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~36/NFRA_CTLPLN.TO-CT-i-8.package-independent-of-line-endings.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CTi8-AC1,CTi8-AC2`, and flip `<status>` to `complete` only when
the mechanical criterion passes and the instance is VALID. Your surprise rows are `NFRA_CTLPLN-W36-S<k>`; append lines only to
the investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.inbound5.md</decomp_doc>
<owned_cells>CT-i-8</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/teams-chat-assist/build.sh
infra/aws/lambda/teams-chat-assist/tests/test_build_reproducible.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- denominator: 0 policies and 0 AWS calls in this cell; the face forbids every AWS call. BLIND: none claimed; this lens reads nothing here.
comp-adversary: RUN -- a deploy made by a build cell (every terraform and aws call forbidden); a normalisation that corrupts a binary file (text suffixes only, all others copied as they are); a fix made by changing a git attribute or setting under other seats (forbidden; the fix is inside the packaging step); a test that proves two LF builds equal (it converts one copy to CRLF: the difference control is the build itself); a silent hash change at the next deploy (the measured file states it). BLIND: the transcripts-pull package, built by another script, may carry the same defect; it is not this cell's and is named in the report if seen.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.20 @ce40c9292d (ADMITTED), FWD-20; row NFRA_CTLPLN-S27; CTO ruling msg 106855.
