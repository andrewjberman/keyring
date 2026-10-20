# NFRA_MCPORTAL task order -- `MP-zo-2` -- WORKSTREAM OGW ROUND 1: the audit list on /opalgateway, with the unattributed negative arm (FWD-28)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-zo-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-zo-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~42</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the unattributed test plants a row with no writer attribution and asserts it is never shown as an owner act; that is its own adversary arm.
EGRESS CLASS, declared: none. Make no network call (the tests mock fetch).
</preflight>

## 1. THE CELL -- `MP-zo-2` (workstream OGW round 1, decomposition section OGW1.2)

You work in the same two worktrees as your first order `MP-zo-1` (`C:/tmp/mp-ogw-42` on branch `wk-NFRA_MCPORTAL-42`, and its nested `C:/tmp/mp-ogw-42/mcportal` on branch `wk-NFRA_MCPORTAL-42-mcportal`), on top of what `MP-zo-1` committed. `node_modules` is linked; no `bun install`. Begin each shell call with `cd C:/tmp/mp-ogw-42 &&`. Code changes are committed in the mcportal worktree with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~42 <0.9.0_WK_NFRA_MCPORTAL~42@opal.agent>`; your proof-of-spec instance and any surprise row are committed in the workspace worktree via `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~42 <0.9.0_WK_NFRA_MCPORTAL~42@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push either repo. Make NO network call of any kind.

**What is wanted.** Andrew wants one place on `/opalgateway` that lists every add, subtract and stop for every person: who did it, when, and what it was before and after. The data is `GET /api/admin/changes` (the writer's own table): each entry is a `PersonChange` (`src/api/admin.ts`: `action`, `tid?`, `oid?`, `when`, `who`, `verdict`, `reason`, `before`, `after`). `getPersonChanges(tid, oid)` already reads that route and keeps one person's `set_person_access` entries; this cell needs ALL persons' access changes, so add a sibling read in your own directory rather than editing `src/api/admin.ts` (which you may not edit): either call the same route with the same fetch helper the API file already exports, or if no exported helper fits, REFUSE with a BLOCKING row naming what you need.

Build (in `mcportal/src/pages/opalgateway/`):
1. **The audit section** (`AuditList.tsx` + a pure view, mounted on the page below the person section, visible whether or not a person is picked): every entry whose `action` is `set_person_access`, `narrow`, `widen` or `revoke`, newest first by `when`; each row shows `when`, `who`, `action`, `verdict` (and `reason` when the verdict is REFUSED), the person it concerns (resolve `tid/oid` against the people data already loaded by the page and show that person's `who`; if it does not resolve show `<tid>/<oid>` as the page gets it), and the `before` and `after` as short readable text (the changed fields only; a `null` before reads `none`).
2. **The negative arm.** An entry with an empty or absent `who`, `when` or `action` is shown with the label `unattributed` in place of the actor, carries `data-attribution="unattributed"` on its row, and never shows an owner label or the word `owner`. An attributed row carries `data-attribution="attributed"`.
3. **THREE tests** in `src/pages/opalgateway/opalgateway.test.tsx` (or a sibling test file there), each by its exact name (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; put each as the literal first argument of its `test(...)`; synthetic fixtures only):
   - `the audit list shows every add, subtract and stop with who, when, before and after, for every person` (two people, entries of three actions; each row shows its who, when and a before and after)
   - `a change with no attributing writer is flagged unattributed and never shown as an owner act` (plant one entry with no `who`; its row says `unattributed`, has `data-attribution="unattributed"`, and the row text does not contain `owner`; an attributed neighbour does not carry the label)
   - `the audit list orders newest first and names the person`
All existing tests keep their names and pass (the seven of `MP-zo-1` included). `bun test src` now reads 89 or more pass and 0 fail.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do NOT edit `src/api/admin.ts`, any gateway (Python) file, the Lambda, Terraform, `package.json` or `bun.lock`; no deploy and no network call.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check script and the proof line are the issuer's.
4. Standing rules: no push and no vendor call; commit as above, each with your serial as author (CLAUDE.md 14a). Do not print a real name, email or account.

## 3. SURFACES

<paths>
mcportal/src/pages/opalgateway/
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~42/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W42-S<k>` (the next free k for W42). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-zo-2"><invocation>cd C:/tmp/mp-ogw-42 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ogw/checks/zo2.AC1.sh; echo "exit=$?"</invocation><expect>named tests present in sources 3 of 3.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~42/NFRA_MCPORTAL.TO-MP-zo-2.opalgateway-audit-list.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you changed (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the OGW round-1 issuance (decomposition v20) from PRD v0.10 FWD-28 and the CVO's cure W2 (every driven act appears in the list with actor, time and before/after; a change written outside the page's writer is flagged `unattributed`). Queued second on slot ~42 behind MP-zo-1 (one chain). The page proves on a mocked fetch; the served proof of FWD-28 (a driven act appearing in the live list, and a store-direct write in a test tree flagged) is part of the close run, not this order.
zo2.AC1 base: FAIL as expected (`bun test src` 79 pass, 0 fail; named tests present in sources 0 of 3; min 89), run in the provisioned slot-42 worktree at mcportal 21ad404, 2026-10-20 ~18:3xZ.

<status>pending</status>
<round>1</round>
<workstream>OGW</workstream>
<slot>~42</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
