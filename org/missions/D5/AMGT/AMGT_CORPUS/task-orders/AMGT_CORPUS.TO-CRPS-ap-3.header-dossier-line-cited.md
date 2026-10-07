# AMGT_CORPUS task order -- `CRPS-ap-3` -- ROUND 40: FWD-15 -- the team's fund of record and last stated position read cited on the header

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ap-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~5</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act; the check renders two components on hand-built payloads.
comp-adversary: RUN by the issuer at the cut on portal origin/DEV ba391aff -- page_check ap3 build 0/1 control 2/2. Blind spot: static markup only; the reading on the page is AC2.
EGRESS CLASS, declared: NONE. Portal source only. NO push of any portal branch: the DEV landing follows the CTO's render review.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~5`**, slot `~5` of round 40.

**Your portal.** The nested `portal/` repository in your worktree, on its own portal branch based on origin/DEV `ba391aff`. Portal files commit INSIDE `portal/` on that branch first, then the outer commit for the outer files. Never commit the portal gitlink. `portal/node_modules` is a LINK to a tree that already holds the dependencies: NEVER run `bun install` (site rule: a registry fetch is egress). If `bun run typecheck` cannot run because the link is missing, say so in your report and go on; the issuer typechecks at the drain. **Colour law** (`portal/CLAUDE.md`): navy ink on the light canvas and white panels; reuse the classes already in the file.

## 1. THE CELL -- `CRPS-ap-3`

Outcome FWD-15: "The fund of record and last stated position read as the TEAM'S stated posture, cited, beside the unchanged
machine judgment ... the machine verdict is byte-unchanged by their presence."

`portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx` renders two lines inside the header's closed
`<details data-header-more>`: `PostureHeaderLine` (about lines 194-246), the machine's verdict, and `DossierPositionLine` (about
251-287), the team's fund of record and last stated position, from the served dossier fields. Each served field carries its
citation (`DossierFieldBlock.citation` and `DossierPositionBlock.citation` in `../types.ts`: `report_key`, `locator`, `passage`).
`DossierPositionLine` prints the fund and the position and no citation at all.

**Build, in `DossierPositionLine` only:**
1. In the SERVED branch, each of the two fields that carries a citation shows it: an element with
   `data-header-dossier-cite="fund_of_record"` (and one with `data-header-dossier-cite="last_stated_position"`) holding the
   report's FILE NAME (the last path segment of `report_key`; never the `s3://` key in visible text), the locator in words, and
   the served passage, exactly as served. Keep it one compact line each, or a native `<details>` per field if the passage makes
   the header heavy; no JS state.
2. A served field with no citation carries `data-header-dossier-cite-absent="<field>"` and says in plain words that the report
   it came from is not named in this security's data.
3. The line marks itself as the research team's, in words, so it cannot be read as the machine's.
4. `data-header-dossier-position` and the existing sentence ("Fund of record: ...; last stated position: ...") stay, as do the two
   not-served branches. `PostureHeaderLine`, `headerPostureSentence` and everything else in the file are byte-unchanged.

## 2. BOUNDS

1. Do NOT arm the walker or run `.claude/skills/ui-walk/walk.mjs`. You MAY render with `portal/scripts/ui-smoke.mjs` (auth-stubbed).
2. No edit to `tabs/PostureTab.tsx`, `postureCites.ts`, `components/LeadPanel.tsx`, `types.ts` or any `__harness__/` file.
3. NO push of any branch, NO deploy, NO AWS call, NO Bloomberg call, NO vendor call.
4. Only the files in `<paths>` change. Never edit the issuer's checks, fixtures or snapshots.
5. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
6. Rows are `AMGT_CORPUS-Z-W5-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner 2.0.0_SA_COO~X` and `surfaced_at` from `date -u +%FT%TZ` at filing.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/AMGT_CORPUS.TO-CRPS-ap-3.header-dossier-line-cited.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ap-3.header-dossier-line-cited.md
</paths>

Read-only: the whole repository, in particular `portal/CLAUDE.md`, `portal/DESIGN.md`, `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx` (`dossierReportName`, the file-name rule) and the issuer's check `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs` with `ap3_base_snapshot.json` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ap-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round40/page_check.cjs" ap3 portal</invocation><expect>(?m)^ap3 build 1/1 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ap-3" judgment="true"/>
</proof_of_spec>

- AC1 (the real `DossierPositionLine` and `PostureHeaderLine`, rendered to static markup): build -- both fields show their report
  file name and passage with no s3 key in the text, and uncited fields are marked; control -- the line still reads the fund and
  the position, and the machine's posture line is byte-equal to the base snapshot.
- AC2 (JUDGMENT, graded by the CVO at L9 on the issuer's real walk): the team's posture reads cited and as the team's, beside the
  machine's unchanged line.

## 5. WHEN YOU ARE DONE

1. Inside `portal/`, run `bun run typecheck` (clean) if the link allows it, and `node src/pages/SecurityAnalysis/__harness__/posture.harness.cjs`;
   report each one's last line. If a harness line that passed before your change now fails, fix your change, not the harness.
2. Write the instance at the proof path, with its mutant control from the start. Record the judgment criterion as
   `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`; no verdict. Then run `python
   .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if AC1 passes, append a new status tag reading complete at the END of this file, in the SAME outer commit as your instance.
4. Report ONCE: the change and why, AC1's output lines, the typecheck and harness lines, your portal and outer commit hashes, the
   portal branch name, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-39 analysis @`5ccdc90368` ruling 7 + s.4 item 2. Base portal origin/DEV `ba391aff`: ap3 build 0/1 control 2/2. The Posture TAB half of FWD-15's DONE WHEN is not in this cell (the CTO's ruling names the header line); it is read on ap-8. Candidate to the CTO's render review.
<risk>LOCAL</risk>
<status>pending</status>
<round>40</round>
<slot>~5</slot>
<fabric>site-z</fabric>
