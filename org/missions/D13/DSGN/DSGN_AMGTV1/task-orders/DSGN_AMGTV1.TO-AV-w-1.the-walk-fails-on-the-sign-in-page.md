# DSGN_AMGTV1 task order -- `AV-w-1` -- THE WALK HARNESS FAILS WHEN A STEP LANDS ON THE SIGN-IN PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-w-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~13</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks read fixtures the issuer captured at the cut.
comp-adversary: RUN by the issuer at the cut on portal DEV a93071b8 -- walkvoid.sh NO (walker rc=1 on the unknown flag, 0 WALK VOID lines); detect.mjs 0 of 6 (module absent). Blind spot: static markup with the estate chrome stubbed; bands, contrast and layout are the walk's.
EGRESS CLASS, declared: NONE. No fetch off this machine.
</preflight>

## 1. THE CELL -- `AV-w-1` (round 4, decomposition v4; serves the round's instrument, row Z-S3)

.claude/skills/ui-walk/walk.mjs walks the local portal build (http://localhost:5174) signed in as the walker account and
prints "STEP <label>: N finding(s)" per step. On the round-3 close walk it lost its session after the first name, landed on
the sign-in page, ran its page checks there and printed "0 finding(s)" -- and the run still exited 0. The CVO's ruling
(round-3 analysis, decision 1): the walk harness must FAIL when any step lands on the sign-in page, and its positive control
is a deliberately signed-out run that fails. Until then a walk's zero is an unproven reading.

Build:
1. `.claude/skills/ui-walk/signin_detect.mjs` (new, ES module, no imports) exporting
   `isSignInPage({ path, hasEmail, hasPassword })` -> boolean: true on the portal's sign-in route (`/login`, or a path
   under `/login/`), or when BOTH the email and the password inputs are visible on the page; false otherwise. An email field
   alone is not the sign-in page, and a route that merely starts with the letters "login" (e.g. `/login-history`) is not.
2. In `walk.mjs`: after every step's navigation/settle -- every `checks(page, label)` call, the login step itself excepted --
   read the page's path and whether `#email` and `#password` are visible, and call `isSignInPage`. When it is true: record a
   finding `walker:signed-out` (claim `measured`) for that step, print
   `WALK VOID: step <label> landed on the sign-in page`, stop walking, write the outputs as today, and exit NON-ZERO
   (`process.exitCode = 3` after the `finally` block's writes). The SUMMARY line gains `walk void: yes|no`.
3. A `--no-login` flag: skip arming the account, reading the secret and the sign-in step entirely (no `ui_walker_account.py`
   call of any kind), then walk the routes as given. It exists to run the signed-out control; with it every protected route
   lands on the sign-in page, so a correct walker prints WALK VOID and exits non-zero.
4. `SKILL.md`: one line documenting `--no-login` and the WALK VOID exit.
A normal signed-in walk behaves exactly as today (same steps, findings, outputs) and still exits 0 when no step is void.

The walker's network guard, DO_NOT_CLICK list, account handling and outputs are unchanged apart from the above.
The http://localhost:5174 portal build is served by another seat; never start, stop or restart a server on that port. If it
does not answer 200, AC1 prints "not runnable": file a BLOCKING row naming that, and report.

## 2. BOUNDS

1. No push, no deploy, no install. The only network your checks touch is http://localhost:5174 (the local dev build). REFUSE, do not rescue.
2. Never arm, disarm, read the secret of, or otherwise touch the walker account (`ui_walker_account.py`); the checks never sign in.
3. Only the files in `<paths>` change.

## 3. SURFACES

<paths>
.claude/skills/ui-walk/walk.mjs
.claude/skills/ui-walk/signin_detect.mjs
.claude/skills/ui-walk/SKILL.md
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~13/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular `.claude/skills/ui-walk/ui_walker_account.py` and the issuer's checks under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-w-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/walkvoid.sh"; echo "exit=$?"</invocation><expect>SIGNED-OUT CONTROL: the walk FAILS on the sign-in page: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-w-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round4/checks/detect.mjs"; echo "exit=$?"</invocation><expect>SIGN-IN DETECTOR: 6 of 6 cases -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 is the built behaviour against its real neighbour (the served 5174 build, signed out); AC2 the detector's arms, negatives included. No judgment criterion: an instrument cell. 

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~13/DSGN_AMGTV1.TO-AV-w-1.the-walk-fails-on-the-sign-in-page.proof_of_spec.json`.
Report once: what changed and where, each re-anchor (old -> new) if any, the output line of every criterion, the portal (if any) and
outer commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = the round-3 analysis's enrichment list @46d28c6c4c section 4 (CTO msg 26587). Decomposition v4.
Base a93071b8: walkvoid.sh NO (walker rc=1 on the unknown flag, 0 WALK VOID lines); detect.mjs 0 of 6 (module absent).

<status>complete</status>
<round>4</round>
<slot>~13</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
