# AMGT_HARVST task order -- `HVST-ag-1` -- ROUND 34: wsj AND barrons -- A FRESH IN-PROFILE SIGN-IN THAT MEETS THE DOW JONES DATADOME CHALLENGE AND PASSES IT, UNDER THE INPUT-SOURCE MONITOR (FWD-11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ag-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- WORLD: wsj/barrons traffic from the box's own egress (no residential arm), sign-ins inside FRESH profiles under a separate profile root, credentials read only for the sign-in and never printed; no Secrets write; no gold write.
comp-adversary: RUN at L5 -- the adversary is a "pass" with no challenge met, or a challenge passed by a human hand (an RDP session is now connected to the box). AC2 requires a met-and-passed challenge inside a monitor window that reads hardware input 0.
</preflight>

## 0. THE CELL (decomposition section 47, `HVST-ag-1`; PRD v0.13 FWD-11; round-33 analysis item 1)

FWD-11 needs each publisher's live challenge met and passed with no human hand. Round 33 proved it for bbg
(`deliverables/0.9.0_WK_AMGT_HARVST~91/af2_challenged_pass.json`: press-and-hold, hardware input 0). wsj and barrons:
round 32 re-minted their sessions in clean profiles and those sign-ins met NO challenge, so no wsj/barrons challenged
pass exists. Round 32 also measured that an UNSOLVED DataDome slider at the Dow Jones sign-in left a profile blocked
("Access is temporarily restricted") until a fresh profile solved it -- the sign-in route is where DataDome meets a new
browser.

**What exists on CLOUD:** `lib/opal_data_harvest/input_source.py` `InputSourceMonitor` (hardware vs injected input);
`lib/opal_data_harvest/verification.py` `solve()` (the barrons/wsj DataDome slider located by its instruction text in
the DataDome frame, re-locate once on a detached frame), `renew()` (the Dow Jones sign-in inside a profile, solve once on
a sign-in challenge), `lib/opal_data_harvest/tab_transport.py` `TabSession`.

## 1. THE ACT (WORLD)

1. Under `InputSourceMonitor` for the whole act, for wsj then barrons: open a TabSession on a FRESH profile under a
   SEPARATE root (`<your deliverables>/r34-profiles/<pub>`, NOT the main-tree profiles, which hold the working
   sessions) and run `renew()` (it signs in when the account check reads logged out, which a fresh profile does). A
   DataDome slider met on the sign-in route goes to `solve()` once.
2. Up to THREE fresh-profile attempts per publisher (a new profile folder each time) to MEET a challenge; at most 15
   requests per publisher in total. If none is met, record `challenge_met: "none"` honestly -- never force one.
3. Write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/ag1_challenged_pass.json` in the shape
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round34/checks/ag-1.AC2.py` reads (open it): the
   instrument, window, hardware/injected counts, and per publisher `challenge_met`, `path`, `passed`, `solved_at`.
4. Do NOT edit `verification.py` (another cell owns it this round): a solver defect is a row.

**Sequencing:** wsj is yours FIRST (the issuer's wsj driver run starts after you report); barrons is yours alone. Never
bbg, ft or sa.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ag-1"><invocation>python -m pytest lib/opal_data_harvest/test_af2_input_source.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ag-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round34/checks/ag-1.AC2-auth.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC1 re-runs the monitor's plants (the instrument the record rests on).
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-ag-1.wsj-barrons-challenged-pass.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ag-1.wsj-barrons-challenged-pass`.

## AMENDMENT 1 (issuer `2.0.0_SA_COO~H`, 2026-10-01 ~14:1xZ) -- AC2 RE-POINTED TO THE ROBUST-AUTH LIMB

CTO ruling msg 27860 splits FWD-11 per publisher into (1) ROBUST AUTH -- MET on 3 or more fresh unattended sign-ins and
renewals under the monitor -- and (2) CAPTCHA (a full driver day under the monitor, plus a planted fixture), graded
elsewhere. "ag-1 may close on this limb." Your record reads barrons 3 of 3, wsj 2 of 3 (attempt a2 timed out on
`Page.goto` before sign-in).

1. ONE more wsj fresh-profile sign-in (`r34-profiles/wsj/a4`), `renew()` under `InputSourceMonitor`, at most 5 requests.
   The issuer's wsj driver run is live in another profile: it kept collecting after your two earlier wsj sign-ins, so
   this one act may run beside it. Append the attempt to `publishers.wsj.attempts` in `ag1_challenged_pass.json` (same
   fields: `profile`, `error`, `signin_renewed`, `challenge_solves`) and widen the record's window/counts to cover it.
2. AC2 is now
   `python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round34/checks/ag-1.AC2-auth.py`, expect
   `AC2 RESULT: PASS`. Re-write the proof instance with this invocation and flip `<status>` to complete if both pass.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-33 analysis @`b25abce8d4` item 1. Authority R-21; R7. No pair: no served gold moves.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>34</round>
<slot>~91</slot>
<fabric>site-z</fabric>
