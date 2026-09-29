# AMGT_RESAPP task order -- `AMGT-vv-5` -- FWD-30'S HARNESS READS THE REDESIGNED PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-vv-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~168</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the checks read committed fixtures; nothing reaches AWS.
comp-adversary: RUN by the issuer at the cut -- AC1 demands EXACT parity (missing=0 AND extra=0) on all four sets with the page's FIGURES count equal to the export's 182, so a reader that drops the export's extra figures instead of finding them on the page FAILS; AC2 keeps the dropped-absence control firing by TOKEN, so a loader fix that blinds the verdict FAILS.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-vv-5` (round 47, decomposition s.55) -- THREAD-BREAKING, FIRST

`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs` is FWD-30's instrument: it renders the Security Analysis
page in node and compares the page's figures, cites, absences and cases with the rich export. AMGT's page redesign project
(DSGN_AMGTV1) merged three page cells into portal DEV (`abcec1b2`..`5fac7a37`), and the harness no longer reads the page:

1. **It does not load.** `components/ThesisCards.tsx:29` imports `{ HeroDialog, DialogStamp } from '@/ui/components/graphic/HeroGraphic'`,
   which the harness's loader cannot resolve (`Error: Cannot find module ...`, rc=1). The harness already stubs page-only
   components it does not compare (read `STUBS` / `SOURCE_STUBS`, and the round-46 `TimelinePanel` entry, as the precedent).
2. **It does not see the header's figures.** `components/HeaderCards.tsx` ("four header cards replace the seven Stat tiles") shows
   each header figure under `data-card-figure-mnemonic="<MNEMONIC>"` with `data-card-figure-state="SERVED"` (`:107-109`); the
   harness's `pageFigures()` reads only `data-stat-tile="<MNEMONIC>" data-stat-state="SERVED"`. So, with (1) stubbed, the one served
   fixture reads `FIGURES page=176 rich=182 extra=6` -- `header|PX_LAST, CUR_MKT_CAP, NET_DEBT, CURR_ENTP_VAL, VOLUME_AVG_30D,
   EQY_BETA` -- figures the page DOES show, in the cards. The export is right; the instrument is blind.

**Build:** make the harness load the redesigned page (stub what it does not compare, one-line comment why) and make `pageFigures()`
also read a SERVED header card's figure by its mnemonic, as `header|<MNEMONIC>`. Keep reading `data-stat-tile` too (other
surfaces may still render tiles). The OK predicate, the three other sets and the page parser's existing reads stay as they are.

## 2. BOUNDS

1. **The harness file only.** No page file, no export file, no Python, no fixture edit. Never make the instrument blind to fit the
   product: nothing the page shows may drop out of a compared set, and no export figure may be dropped to make parity.
2. **No server; no vite; no deploy; no write to AWS.** Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~168/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; the fixtures `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/fixtures/`
and the controls `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/controls/`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-vv-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-5.AC1.sh; echo "exit=$?"</invocation><expect>FWD-30 HARNESS READS THE REDESIGNED PAGE: YES (harness rc=0; sets exact (missing=0 extra=0): 4 of 4; FIGURES page=182) -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-vv-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-2.AC2.sh; echo "exit=$?"</invocation><expect>THE VERDICT COUNTS A DROPPED ABSENCE (tokens, not rc): 2 of 2 -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the build (exact parity on the served fixture against the redesigned page); AC2 its difference control (the pre-fix exports
still read "missing=1" and "EXPORT-COMPARE NOT OK").

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~168/AMGT_RESAPP.TO-AMGT-vv-5.fwd30s-harness-reads-the-redesigned-page.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the portal and outer commit hashes, and any row. The issuer may continue you with a second order on this worktree.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** found AT the cut, not on the analysis's list: DSGN_AMGTV1's merges into portal DEV (5fac7a37) broke FWD-30's
instrument twice. Measured in a scratch portal worktree (`C:/tmp/r47probe`, HeroGraphic stubbed THERE only): FIGURES 176/182, extra =
the six header mnemonics above; ABSENCES 17/17 and CASES 3/3 unaffected; EXPORT-COMPARE NOT OK. HeaderCards.tsx still SHOWS all six
-> an instrument gap in RESAPP's own harness, not a page drop and not an export change. Thread-breaking -> first on slot ~168; vv-1
(which also edits this file's CASES parser) follows on the same worker. Base: AC1 FAIL (the load error), AC2 FAIL (the load error;
the old rc-only control would pass).

<status>pending</status>
**ISSUER CLOSE (`2.0.0_SA_COO~Z`, 2026-09-29):** drained @a6c17f4bcf (portal ed109ced). AC1 re-run by the issuer: "FWD-30 HARNESS READS THE
REDESIGNED PAGE: YES", 4 of 4 sets exact, FIGURES 182/182; instance VALID rc=0. BOUND for L9: the six header figures sit in each card's
click-open window (`HeaderCardDetail`), which the harness now renders per card; the static first view shows only each card's lead.
<status>complete</status>
<round>47</round>
<slot>~168</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
