# AMGT_HARVST task order -- `HVST-ag-2` -- ROUND 34: ft AND sa -- MEET EACH PUBLISHER'S CHALLENGE AND PASS IT UNDER THE INPUT-SOURCE MONITOR, WITH AN ft SOLVER IF ITS SECURITY VERIFICATION NEEDS ONE (FWD-11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ag-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- phase A LOCAL (a solver + tests); phase B ft and sa traffic from the box's own egress / sa's existing route (R7), in FRESH profiles under a separate root, no Secrets write, no gold write.
comp-adversary: RUN at L5 -- the adversary is a pass with no challenge met, or one passed by a human hand (an RDP session is connected to the box). AC2 requires a met-and-passed challenge inside a monitor window that reads hardware input 0.
</preflight>

## 0. THE CELL (decomposition section 47, `HVST-ag-2`; PRD v0.13 FWD-11; round-33 analysis item 2)

FWD-11 names ft's Security Verification and sa's checks. **ft:** its stored session passes in-tab today (the issuer's
backfill runs); FT shows a "Security Verification" interstitial (signature `ft_security_verification`, `<title>security
verification</title>`) to browsers it does not trust -- `verification.CHALLENGE_PUBLISHERS` is ("bbg", "wsj",
"barrons"), so NO ft solver exists. **sa:** the collector reaches sa over REST (curl_cffi via its residential route,
R7), where a check is a refusal, not a page; the sa web origin in a browser can show its own bot check (PerimeterX
press-and-hold, the same family as bbg).

## 1. PHASE A (LOCAL)

1. Find what each challenge IS by meeting it read-only: a FRESH anonymous TabSession (profile under
   `<your deliverables>/r34-profiles/<pub>`) opening ft's and sa's web origin and one content page each, at most 5
   requests per publisher, under `InputSourceMonitor`. Save the challenge page's DOM text (no cookies, no values) as
   `ag2_<pub>_challenge.html` when met.
2. If ft's Security Verification is met: add an ft solver to `lib/opal_data_harvest/verification.py` `solve()` that
   completes it LOCALLY from the page's own DOM (a checkbox/button/slider, as the existing solvers do) -- NEVER a
   vision/AI API, never a third-party solving service -- and add `"ft"` to `CHALLENGE_PUBLISHERS`. sa's PerimeterX
   press-and-hold reuses the bbg press-and-hold solver (`_solve_press_and_hold`); wire `"sa"` only if its challenge is
   that control.
3. Plants in `lib/opal_data_harvest/test_ag2_ft_sa_solvers.py` with fake pages built from the saved DOM.

## 2. PHASE B (WORLD) -- the challenged passes

Under `InputSourceMonitor` for the whole act: for ft and for sa, in FRESH profiles under your separate root, meet the
challenge (up to THREE fresh profiles per publisher, at most 15 requests per publisher) and pass it through `solve()`.
Write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/ag2_challenged_pass.json` in the shape
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round34/checks/ag-2.AC2.py` reads (open it). A challenge
not met is recorded `"none"`; one met and not passed is `passed: false` with the signature -- never a final state.

**Bounds:** ft and sa ONLY; the issuer's ft and sa backfills use the main-tree and `~92` runtimes and profiles --
NEVER touch those profiles or runtimes. No residential arm beyond sa's existing route.

<paths>
lib/opal_data_harvest/verification.py
lib/opal_data_harvest/test_ag2_ft_sa_solvers.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ag-2"><invocation>python -m pytest lib/opal_data_harvest/test_ag2_ft_sa_solvers.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ag-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round34/checks/ag-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-ag-2.ft-sa-challenged-pass.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ag-2.ft-sa-challenged-pass`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-33 analysis @`b25abce8d4` item 2. Authority R-21; R7. No pair. CTO ruling 27782: no vision/AI
solving API without Andrew's per-use word.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>34</round>
<slot>~90</slot>
<fabric>site-z</fabric>
