# AMGT_RESAPP task order -- `AMGT-rn-6` -- THE SIDEBAR UNDER THE CONTRACT: App.tsx's navigation brought to C1, C11, C13 on Andrew's word

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rn-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~151</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing reaches AWS.
comp-adversary: RUN by the issuer over the round-38 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: NONE. No server, no fetch, no network.
</preflight>

## 1. THE CELL -- `AMGT-rn-6` (round 39, decomposition s.47, item 10)

The sidebar (`App.tsx`, the `<aside>` at `:270-271` and its menu) was Andrew's reserved card through rounds 37-38 and is released
("Rec approved", CTO msg 25682). Its body-scope reads at the round-38 baseline: weights FAIL [500,600], radii FAIL ["8px"],
shadows FAIL 1, sizes FAIL [10] -- all its own. The class census reads `size=2 weight=5 radius=5 shadow=2`. **Build:** every
weight to {400,700} (`font-medium`/`font-semibold` -> `font-normal`/`font-bold` by role), every radius to {2,3,4,pill}
(`rounded-lg` -> `rounded` or `rounded-[4px]`; the avatar's `rounded-full` is pill and stays), no shadow outside a focus ring
(`shadow-lg` on the aside and `shadow-2xl` on the dropdown go; a 1px border is the separation), no size below 11
(`text-[10px]` at `:369` -> `text-[11px]` or `text-xs`), and C13 on `:403`'s truncated email (a `title` attribute with the full
text is the recovery path, or wrap). Read `portal/DESIGN.md` C1-C13 for the rules; change nothing outside the aside, its menu items
and the user dropdown; no layout, colour or behaviour change.

## 2. BOUNDS

1. **No server.** The body-scope render is the issuer's after the merge; your criteria are the census and the typecheck.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-151-portal` at DEV `5e339ffd`.
3. Standing: no install, no push, no promote. REFUSE, do not rescue.

## 3. SURFACES

<paths>
portal/src/App.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~151/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rn-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-6.AC1.sh; echo "exit=$?"</invocation><expect>src/App.tsx idiom=N size=0 weight=0 radius=0 shadow=0 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rn-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/typecheck.sh; echo "exit=$?"</invocation><expect>tsc -b --noEmit exit=0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~151/AMGT_RESAPP.TO-AMGT-rn-6.the-sidebar-under-the-contract.proof_of_spec.json`.
Report names each token replaced (before -> after, with its line), the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** item 10 (CTO msg 25682 item 3, Andrew "Rec approved"). Render grade: the issuer's real run on 5174 after the
merge, body scope: weights, radii, shadows, sizes PASS 6 of 6.

<status>pending</status>
<round>39</round>
<slot>~151</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
