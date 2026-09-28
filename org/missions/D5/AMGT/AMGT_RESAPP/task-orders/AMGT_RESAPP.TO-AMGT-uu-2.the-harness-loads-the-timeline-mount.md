# AMGT_RESAPP task order -- `AMGT-uu-2` -- THE EXPORT-COMPARE HARNESS LOADS A HEADER THAT MOUNTS THE TIMELINE PANEL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-uu-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~166</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks read committed fixtures; nothing reaches AWS.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is a control that passes on a blind instrument (row Z-S294): AC2 requires the dropped-absence TOKENS on both pinned pre-fix exports, so a harness that crashes FAILS it instead of reading as the control firing. Base-run on the shared tree: AC1 FAIL, AC2 FAIL (both on the crash).
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-uu-2` (round 46, decomposition s.54)

`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs` renders the Security Analysis page in node (it
transpiles each page source itself) and compares the page's figures, cites, absences and cases with the rich export -- the
instrument of FWD-30 ("the export equals the page"). AMGT_HARVST's portal commit `92a25762` mounts a new
`TimelinePanel` in `portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx` (imported at `:41`, rendered at `:166`).
`TimelinePanel.tsx` imports `@/api/api-client` (`:35`), `@/ui/components/states` (`:36`), `@tanstack/react-query`, `recharts`
and `lucide-react`. The harness's `load()` (`:144-152`) resolves only an exact `STUBS` key (`:69-108`), a relative path (through
`SOURCE_STUBS`, `:110-125`, or a transpile), or a plain `require` from the portal root; it has no `@/` mapping (the app maps
`@` to `./src`: `portal/vite.config.ts:17`, `portal/tsconfig.json:9`). So every run on a tree carrying the mount crashes:
`Error: Cannot find module '@/api/api-client'`, rc=1, no FIGURES line (row Z-S292). `portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs`
already received its two stubs in `92a25762` (`:128-131`); this harness did not.

**Build:** make the harness load the page WITH the mount and keep comparing. The timeline is not part of the export, so the
panel must contribute nothing to the three compared sets or the CASES set: stub `TimelinePanel` (a `SOURCE_STUBS` entry that
renders nothing) and/or resolve `@/`-prefixed names to `src/`; state in a one-line comment which you chose and why. The
harness's page parser keeps reading the page as it is; the OK predicate keeps `absDiff.missing.length === 0` (round 45).

Your portal worktree is cut from local portal `DEV` (`92a25762`), which carries the mount.

## 2. BOUNDS

1. **The harness file only.** No page file, no Python, no data, no fixture edit. Never make the instrument blind to fit the
   product: nothing the page renders outside the timeline may drop out of a compared set.
2. **No server; no vite; no deploy; no write to AWS.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~166/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; the fixtures `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/fixtures/`
and the controls `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/controls/`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-uu-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-2.AC1.sh; echo "exit=$?"</invocation><expect>LOADS AND COMPARES WITH THE MOUNT: YES (harness rc=0; sets with missing=0: 4 of 4) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-uu-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-2.AC2.sh; echo "exit=$?"</invocation><expect>THE VERDICT COUNTS A DROPPED ABSENCE (tokens, not rc): 2 of 2 -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 is the build (the one served fixture reads 4 of 4 sets with missing=0 WITH the mount present); AC2 is its difference
control (the two pre-fix exports still read "missing=1" and "EXPORT-COMPARE NOT OK" -- the fix did not blind the verdict).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~166/AMGT_RESAPP.TO-AMGT-uu-2.the-harness-loads-the-timeline-mount.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the portal and outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-45 analysis s.4 item 2 (row Z-S292). Base on the shared tree (portal DEV @92a25762): AC1 FAIL (harness
rc=1, 0 of 4), AC2 FAIL (0 of 2, the crash). On the published tree @c3dd9ca9 (no mount) AC1 reads NOT_EXERCISED and the AC2 loop
reads 2 of 2 by token -- so AC2 discriminates a crash from a verdict. Precedes uu-3 on slot ~166 (uu-3's AC2 runs this harness).

<status>pending</status>
<round>46</round>
<slot>~166</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
