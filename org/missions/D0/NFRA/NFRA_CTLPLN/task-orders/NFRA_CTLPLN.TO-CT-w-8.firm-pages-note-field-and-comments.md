# TO NFRA_CTLPLN.TO-CT-w-8 -- workstream FIRMPG round 1 (cell CT-w-8): the registry keeps the reasons behind each firm's pages, and the generated portal block renders them

<to_id>NFRA_CTLPLN.TO-CT-w-8</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~70</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after re-running both criteria: CTw8-AC1 12 passed, CTw8-AC2 3 (AMENDMENT 1); the suites test_opal_naming.py 96, test_opal_naming_firm_pages.py 16, test_opal_naming_firm_access_ts.py 5 pass; the proof instance is VALID. The comments moved verbatim: 38 lines in the old literal, 38 in the registry notes (inflection 4, cottonwood 11, demo 23). The portal commit 1df22d9666 (base 2ed4373d, 35 insertions, 33 deletions) is prepared on the portal branch wk-NFRA_CTLPLN-70-portal and landed by the issuer. A channel splice made by the issuer's own conflict resolution was repaired by rebuilding the branch from the worker's pre-merge commit and re-merging main; the worker's row W70-S4 (about the splice) was never committed and was dropped from the instance as moot.</status_reason>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>FIRMPG</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-w-8` (`decompositions/NFRA_CTLPLN_DECOMP.round8.md`, the added row) | **outcome_ref:** FWD-28 |
**depends_on:** none (CT-w-1, CT-w-2, CT-w-4, CT-w-3 are done)

---

## WORKER FACE

### THE CELL

CT-w-4 prepared a generated block for the portal's `FIRM_ALLOWED_PATHS` (portal commit `ef65ad67`, on the portal repository's branch `wk-NFRA_CTLPLN-65-portal`, base `2ed4373d`). The CTO has reviewed it and HELD it off DEV (msg 108504): the 38 lines it dropped are Andrew's own words on each firm's allowlist (ADVI_INFMVP.F2 2026-05-28, PRTORG.04 2026-06-09, the 2026-09-01 Cottonwood pages, ADVI_DEMOV1.008, the /ticket-center note), and that provenance must survive. RULED: (1) the registry rows gain a `note` field, free text (the record and the date), rendered by the generator as comment lines above that firm's entries inside the GENERATED block; the hand comments move into the registry VERBATIM; (2) regenerate and re-prove set-equality and that the hand-kept lines are byte-identical; (3) fix the stale evidence line ranges (row W65-S7) in the same cell. You do NOT land anything on the portal's DEV or PROD, push nothing, and do not move the gitlink: the issuer lands the reviewed commit after your proofs.

### BUILD

1. **The comments, verbatim.** Read the old file: `git -C portal show 2ed4373d:src/lib/firmAccess.ts`. Every comment line INSIDE `FIRM_ALLOWED_PATHS` (the `//` lines between and inside the firms' `new Set([...])` entries, and the ones between entries) belongs to a firm: lines inside a firm's set belong to that firm; lines between two entries belong to the NEXT entry (for example the block before the `demo` entry). Put each firm's comment lines, with their `//` removed and the leading single space kept as written, into that firm's registry row as `"note"`: a JSON string, lines joined by `\n`, text unchanged (no rewording, no trimming of words). Count them: the total over the four notes must be 38 lines minus any line that is not a comment (print the count and the 38).
2. **The generator, its own commit through `.tools/commit-gate.sh`** (`lib/opal_naming.py`): `validate()` accepts an optional `note` (a non-empty string) on a firm row and refuses any other type; the portal renderer `_blk_firm_allowed_paths` emits each firm's note as `    // <line>` lines directly above that firm's `'<firm>': new Set([` line, inside the generated block. A firm with no `note` renders as today. The Lambda renderer is unaffected (it does not read notes).
3. **The registry**: `infra/logic/registry/firm_pages.json` gains the four `note` fields, and its `evidence` strings that name `portal/src/lib/firmAccess.ts:<range>` are corrected to name the lines of the GENERATED block in the regenerated portal file (compute them; say how).
4. **Regenerate**: the portal block into your portal worktree (`python -I lib/opal_naming.py generate --out . --target portal/src/lib/firmAccess.ts`), and `infra/aws/lambda/portal_data_proxy/firm_page_access.py` (the registry file's hash is in its mark, so the regenerated module differs from the committed one in its FIRST LINE ONLY: prove that with a diff and state it). Commit the portal change ONLY on your portal worktree's branch (`git -C portal commit` with author `0.9.0_WK_NFRA_CTLPLN~70 <0.9.0_WK_NFRA_CTLPLN~70@opal.agent>`), on top of the DEV-equivalent base `2ed4373d`; never push.
5. **Tests**, a NEW file `lib/tests/test_opal_naming_firm_notes.py`: T1 the generated portal block equals a fresh render (with the notes); T2 every comment line of the old file inside the literal appears in the new block verbatim (compare the multisets of stripped comment texts; expect equality); T3 firm -> pages set-equal to the old literal (4 firms, 35 pairs); T4 the lines OUTSIDE the block are byte-identical to the old file; T5 `validate` refuses a non-string `note`; T6 `firm_page_access.py` differs from its pre-change bytes in the first line only. The existing `lib/tests/test_opal_naming.py`, `test_opal_naming_firm_pages.py` and `test_opal_naming_firm_access_ts.py` must still pass; update the latter only where a note changes a line count, and say what you changed.

### RULES FOR THIS CELL

Write surface: the `<paths>`. You land nothing in the portal's DEV or PROD, push nothing, and do not commit the workspace's `portal` gitlink. No terraform, no aws, no portal build. `.tools/safe-commit.sh` for workspace commits (the naming gate runs; if it REFUSES, STOP and file a BLOCKING row; never wrap a token). The comments contain firm names only inside the REGISTRY file and the GENERATED block, where they are allowed. No non-ASCII added (the old comments are ASCII; if one is not, say so and keep it byte-for-byte). CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W70-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTw8-AC1" cell_refs="CT-w-8"><invocation>python -m pytest -q lib/tests/test_opal_naming_firm_notes.py</invocation><expect>passed</expect></criterion>
`CTw8-AC1` -- T1-T6 pass.

<criterion id="CTw8-AC2" cell_refs="CT-w-8"><invocation>grep -c '"note"' infra/logic/registry/firm_pages.json</invocation><expect>3</expect></criterion>
`CTw8-AC2` -- the three firm rows that had comments carry a note (AMENDMENT 1: the issuer wrote 4; 49financial had no comment).
</proof_of_spec>

<expected_criteria>CTw8-AC1,CTw8-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~70/NFRA_CTLPLN.TO-CT-w-8.firm-pages-note-field-and-comments.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTw8-AC1,CTw8-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID. Report the portal commit hash and the portal diff stat vs `2ed4373d`.

<amendment>
AMENDMENT 1 (issuer 2.0.0_SA_COO~C, 2026-10-12 ~11:1xZ; gate limb: none graded this modification, no new TO file) -- the issuer's premise was wrong, found by the worker (row NFRA_CTLPLN-W70-S1): at the base `2ed4373d` the `49financial` set held NO comment line, so only THREE firm rows carry a note (inflection 4 lines, cottonwood 11, demo 23: 38 lines in all, equal to the old literal's 38). A firm with no comment gets no `note` (an empty note is refused by `validate()` and a placeholder would break T2). CTw8-AC2 therefore expects `3`, not `4`. Inherited state: the worker's commits 6ae365f583 (generator), e76206bdcb (registry, module, tests), 9abda78339 (rows, proof) and the portal-branch commit 1df22d9666. DO: re-run both criteria, REWRITE the proof instance with CTw8-AC2's amended expectation (3) and its PASS evidence, validate it, and flip `<status>` to `complete`; change no other file. Row W70-S2 (five moved comment lines carry an em dash, an arrow and a section sign): ruled by the issuer: the CTO said VERBATIM, the source file already carried them, and `lib/opal_naming.py` reads the registry as UTF-8 text (`_read_text`); they stay as written.
</amendment>
<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>CT-w-8</owned_cells>
</decomp_ref>

<paths>
infra/logic/registry/firm_pages.json
lib/opal_naming.py
lib/tests/test_opal_naming_firm_notes.py
lib/tests/test_opal_naming_firm_access_ts.py
lib/tests/test_opal_naming_firm_pages.py
infra/aws/lambda/portal_data_proxy/firm_page_access.py
portal/src/lib/firmAccess.ts
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a comment reworded or dropped on the way into the registry (T2 compares the multisets of the old and new comment texts); the generated block changing what a partner firm sees (T3 set equality, T4 byte-identical hand-kept lines); the regenerated Lambda module changing in code (T6: first line only; it is deployed LIVE since CT-w-3, so a mark-only difference is expected and a code difference is a STOP); BLIND: the portal repository's CI, typecheck and build, which need node_modules.
risk: WORLD is declared because the L6 gate derives a floor from the lib and infra paths; this cell lands nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO ruling msg 108504 (rows W65-S6, W65-S7); `ROUND_ANALYSIS.round7.md`.
