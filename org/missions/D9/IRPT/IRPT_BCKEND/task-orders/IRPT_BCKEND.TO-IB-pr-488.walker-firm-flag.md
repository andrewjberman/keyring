# TO IRPT_BCKEND.TO-IB-pr-488 -- the ui-walk engine gains `--firm "<label>"` and `--first-client`

<to_id>IRPT_BCKEND.TO-IB-pr-488</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~341</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>169</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ROUND-169 ANALYSIS section 3 item 1 (msg 6660) | **Decomp cell:** `IB-pr-488` (decomposition section 161) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-488` (inlined):** the `/ui-walk` engine cannot reach an Inflection client: it has no way to choose the portal header's Firm control, and the page ignores a `?firm=` URL parameter for an internal viewer. Add two flags to `.claude/skills/ui-walk/walk.mjs`:

1. `--firm "<label>"`: before the client search, open the header's Firm control and press the option whose VISIBLE LABEL equals `<label>` exactly, then wait for the control to show that label. The control is the custom dropdown in `C:\dev\ajb_workspace\portal\src\pages\InvestorReporting\header\FirmDropdown.tsx` (read it for its role, aria and test-id selectors; the walker's other steps show how it locates controls). If no option has that label, throw an Error whose message starts `FIRM_OPTION_ABSENT:` and lists the option labels the control showed. `--firm` with no value throws `--firm wants a label`. Parse it in the argument loop where `--client` is parsed (about line 38).
2. `--first-client`: when given (with `--firm`, no `--client`), after the firm is selected and the empty search lists clients, walk the FIRST listed client exactly as `--client` walks a named one. A client name must reach no file outside `tmp/ui-walk/` and no log line the walker prints to the terminal.

Then document both flags in the invocation block of `.claude/skills/ui-walk/SKILL.md` (one line each, in the style of the existing lines).

Do not touch the safety model: the network guard, the base-URL refusal, the arming and disarming, the read-only rule. Do not edit anything under `portal/`. You cannot run a live walk in this order (a later order does); the order's proof is the argument handling and the fail-loud token.

**Environment note:** `walk.mjs` loads `playwright-core` from `<root>/portal/node_modules`; a worker worktree has an empty `portal/` directory, so the issuer's check joins the main tree's `node_modules` by a directory junction the first time it runs. Leave that junction in place; the issuer unlinks it at the drain. Never delete anything through it.

**Criteria (run each under `timeout 120`, record the output and exit code verbatim):**

<criterion id="IB169-1-AC1" cell_refs="IB-pr-488"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-1-AC1</invocation><expect>IB169-1-AC1 PASS</expect></criterion>
<criterion id="IB169-1-AC2" cell_refs="IB-pr-488"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-1-AC2</invocation><expect>IB169-1-AC2 PASS</expect></criterion>
<criterion id="IB169-1-AC3" cell_refs="IB-pr-488"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-1-AC3</invocation><expect>IB169-1-AC3 PASS</expect></criterion>

<expected_criteria>IB169-1-AC1, IB169-1-AC2, IB169-1-AC3</expected_criteria>

What the checks grade: AC1 `node --check` on `walk.mjs`; AC2 `node walk.mjs --base http://example.com --firm Inflection --first-client` reaches the localhost refusal instead of `unknown argument`, and `--firm` with no label does not reach it; AC3 SKILL.md names both flags, `walk.mjs` names `FIRM_OPTION_ABSENT`, and no file outside the grant changed.

## BOUNDS

- **Grant:** the `paths` block and nothing else. No live walk, no arming, no AWS call, no network call.
- **Refusal clause:** STOP, file a row, change nothing more, if the Firm control cannot be selected by its visible label from the page's own markup (say what the markup is), or if a flag would need a change under `portal/`.
- **Row ids** are `IRPT_BCKEND-D2-W341-S<k>` (the next free `k`).
- **Commit** on your worktree branch per your definition; ASCII only. Report once, under 150 words.

<paths>
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~341/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-488.walker-firm-flag.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 161 (round 169, workstream ~P), cell `IB-pr-488`.
<owned_cells>IB-pr-488</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB169-1-AC1, IB169-1-AC2, IB169-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~341/IRPT_BCKEND.TO-IB-pr-488.walker-firm-flag.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a developer-tool script under `.claude/skills/ui-walk/`; no cloud resource, served artifact or portal file is touched. `comp-find` over the task orders for `ui-walk/walk.mjs` read 0 hits across 29,390 files (no other live order names it).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the order runs no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p169_cells.py dry-run at base on dell2 2026-10-12 ~23:2xZ: IB169-1 AC1 PASS (a bound), AC2 FAIL (`unknown argument --firm`), AC3 FAIL (SKILL.md names neither flag). AC2 also run on a throwaway worktree with a patched `walk.mjs`: PASS; and on a patch that accepts `--firm` without a label: FAIL. Commit-gate clean.
lane: the <paths> block IS the grant; worker slot ~341 of IRPT_BCKEND. Class LOCAL.
</preflight>
