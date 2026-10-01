# DSGN_AMGTV1 task order -- `AV-o-2` -- THE RESEARCH TEAM'S DOSSIER ON THE PAGE: PILLARS, MANAGEMENT, FUND OF RECORD, LAST STATED POSITION

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-o-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~36</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut (read-only invokes).
comp-adversary: RUN by the issuer at the cut on portal DEV b6634ba0 -- dossier.cjs 0 of 4 (FAIL as expected: the page has 0 consumers of `dossier_fields`); green arm 4 of 4 (13 pillars over IMB / AZN / TSM in order, each with its report named; IMB and TSM management passages; IMB and AZN fund of record and last stated position on the Posture tab and the header posture line; TSM says none is stated; 6501 shows its reason); bound Q2 8 of 8 at base and on the green arm with the component code INLINE in each file (a first green arm that put it in a new shared module turned drafting / execFallback / execText / execPattern RED -- their loaders resolve only the modules they name, and `../types` for type positions only); portal tsc -b rc=0 on the green arm. Blind spot: static markup with the estate chrome stubbed; the layout is the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-o-2` (round 10, decomposition v10; serves AMGT_CORPUS FWD-10, 11, 15, 16, 18)

The CTO's ruling (round-9 analysis, ruling 2; AMGT_CORPUS round-20 ruling 1): the served `dossier_fields` are rendered -- the
pillars with their citation and terms, the management passage beside the roster, and the fund of record plus the last stated
position on the posture line and the Posture tab. The page has no consumer of them today. `/thesis` serves `dossier_fields` =
{ `thesis_pillars`: [{ `pillar`, `text`, `terms`, `citation` }], `management`: { `status`, `value`, `citation` },
`fund_of_record`: { `status`, `value`, `citation` | `reason` }, `last_stated_position`: { `status`, `value`: { `fund`,
`size_pct`, `text` }, `citation` | `reason` } }, or `{ status, reason }` for a name with no dossier (6501: "no research dossier
for this name"). A citation carries `report_key` (an s3:// key), `extract_key`, `locator`, `passage`. Build:
1. **Types** (`portal/src/pages/SecurityAnalysis/types.ts`): the dossier's shape as TYPES ONLY (interfaces / type aliases) and
   `dossier_fields?: DossierFields | null` on `ThesisBundle`. **No runtime value may be exported from `types.ts` and imported by a
   component** -- the page harnesses load `../types` for type positions only, so a value import from it turns them red.
2. **The pillars on the Thesis tab** (`tabs/ThesisTab.tsx`, beside the identity line): headed "The research team's thesis
   pillars", each served pillar in the served order -- its `pillar` in bold, its `text`, its served `terms` other than the pillar
   name itself (e.g. "Terms: price"; nothing when there are none), and "Source: <report file name>" (the last path segment of
   `citation.report_key`, extension off, e.g. "Imperial Brands Research Pack 2026 07 17_v1"). A `{ status, reason
   }` block reads one sentence with the served reason in words: "The research team's thesis pillars: no research dossier for this
   name."
3. **The management passage on the Exec Management tab** (`tabs/ExecManagementTab.tsx`, beside the identity line and the roster):
   headed "The research team on management", the served `management.value`, and its report file name; an absent passage reads one
   plain sentence.
4. **Fund of record and last stated position on the Posture tab** (`tabs/PostureTab.tsx`) **and on the header posture line**
   (`components/SecurityOverlay.tsx`, beside `PostureHeaderLine`): one plain line, e.g. "Fund of record: IDVZ; last stated
   position: Potential ADD in IDVZ (currently ~2.5%)." with the report file name on the tab; when both are ABSENT the tab says "No
   fund of record is stated in the research team's pack" and prints no fund code. The header reads the /thesis bundle through the
   page's existing `useThesisBundle(securityKey)` hook (the /overlay does not carry `dossier_fields`; the tabs already fetch it).
5. **Put the small components and helpers INLINE in each file that renders them** (no new module): the page harness loaders
   resolve only the modules they already name.
No storage path (`s3://`, `extract.json`, a key) in visible text -- a key may ride a `data-` attribute. No value is converted,
joined or guessed; nothing else on the tabs moves.

**The rules every cell keeps (PRD CONTRACTS, binding):** C-PRESENTATION-ONLY -- the page derives nothing: no figure is computed,
converted or guessed, no name is looked up or joined, and a value the payload does not carry reads as a designed empty state
naming, in plain words, what is missing and which team fills it -- never a project code, serial or storage path.
C-ESTATE-FIXTURES -- windows are the estate's HeroDialog + DialogStamp, panels and states are the estate's; nothing forked.
**Design law (portal `DESIGN.md`):** white panels with navy ink (C3); ONE dark band per page; no translucent white (C5.8); no
shadow (C11). A code, field name or path may sit in a data attribute or in code, never in visible text -- and text inside a
collapsed `<details>` is still visible text.

**If a bound harness check is anchored on the raw text this cell changes,** re-anchor that ONE check onto the same fact as the
page now states it (the words, or a data attribute), keep its claim, never drop it; the harness keeps at least its base
check count (the floor in the bound criterion). Only a harness named in `<paths>` may be edited. Record each re-anchor
(old anchor -> new) in the instance. Measured on the green arm (inline components, types-only `types.ts`), no bound harness needs a
change, so none is granted -- a red bound means a new module or a value import from `types.ts` crept in.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; every other page, component, tab and harness is unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~36/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `portal/src/pages/SecurityAnalysis/hooks/useLeadPanelApi.ts` (`useThesisBundle`),
`portal/DESIGN.md`, and the issuer's checks and fixtures under `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/`
(never edit them; the fixtures are the served payloads the checks render: IMB LN and AZN LN every field SERVED, TSM US fund of
record and last stated position ABSENT, 6501 JP the `{ status, reason }` block).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-o-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/dossier.cjs"; echo "exit=$?"</invocation><expect>DOSSIER FIELDS ON THE PAGE: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-o-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round10/checks/bound.cjs" Q2 drafting.harness.cjs:8 execFallback.harness.cjs execText.harness.cjs execPattern.harness.cjs:9 posture.harness.cjs:32 posturePattern.harness.cjs:13 shell.harness.cjs:10 tabs.harness.cjs:20; echo "exit=$?"</invocation><expect>Q2 BOUND: 8 of 8 harnesses green -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-o-2" judgment="true"/>
</proof_of_spec>

AC1 is the built dossier on the SERVED /thesis of IMB, AZN, TSM and 6501 (pillars in order with their report; the management
passage; fund of record and last stated position on the Posture tab and the header posture line; the empty block's reason; no
storage path on the face); AC2 the bound on every harness that loads the four tabs and the header. AC3 is JUDGMENT, graded by
`3.0.0_SA_CVO~Z` at L9 on the issuer's signed-in walk (IMB's Thesis, Exec Management and Posture tabs and header; 6501's Thesis
tab), never self-graded: the research team's pillars, management view and position read as the team's, each traceable to its
report, and a name with no dossier says so (CORPUS FWD-10, 11, 15, 16, 18). Portal typecheck, if you run one:
`node_modules/.bin/tsc -b --noEmit` inside `portal/` (`tsc -p .` lists no files and checks nothing).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~36/DSGN_AMGTV1.TO-AV-o-2.the-dossier-on-the-page.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY; the
grant admits it -- it is not outside your write surface).
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 10 = the round-9 analysis s.4 item 2 with ruling 2. Base b6634ba0: dossier.cjs 0 of 4; green 4 of 4; Q2 8 of 8
at base and on the green arm (the green arm carried o-2, o-3 and o-4 together).

<status>complete</status>
<round>10</round>
<slot>~36</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
