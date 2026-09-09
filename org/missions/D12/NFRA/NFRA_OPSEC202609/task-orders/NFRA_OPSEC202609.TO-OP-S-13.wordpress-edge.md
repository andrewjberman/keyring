# TO NFRA_OPSEC202609.TO-OP-S-13 -- opalinvest.com GETS AN EDGE: CloudFront + the same WAF managed rules already soaking on the portal, so a known-bad request is refused BEFORE WordPress handles it and one BLOCK row covers the site and the portal from one table -- and the site still loads for a visitor (OP-s-13, FWD-13)

<to_id>NFRA_OPSEC202609.TO-OP-S-13</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~U</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>complete</status>
⛔ **CLOSED BY THE ISSUER 2026-09-09 ~18:2xZ, `2.0.0_SA_COO~Z`. THE FACE WAS STALE-OPEN OVER FINISHED WORK.** The assignee `0.7.0_AE_CloudOps~U` died before flipping its own `<status>`, so this face read `staged` for five days while its work was complete and committed. **The proof-of-spec instance is VALID at HEAD:** `deliverables/0.7.0_AE_CloudOps~U/NFRA_OPSEC202609.TO-OP-S-13.wordpress-edge.proof_of_spec.json` @`c12e340ceb`, phase BUILD-GENERAL -- **S13-AC1 PASS, S13-AC2 PASS, S13-AC4 PASS, S13-AC5 PASS, S13-AC3 UNCOMPUTABLE-BY-CONSTRUCTION** (it names BOTH paths and is graded as one, so it takes the disposition of the `/wp-admin` limb, which stays UNCOMPUTABLE citing row `Z-S102` until a named human supplies a named address).
**THE UNCOMPUTABLE ROW IS NOT GRADED HERE.** `S13-AC3` is `3.0.0_SA_CVO~Z`'s at L9. This flip records that the FACE is terminal; it never asserts the criterion passed.
**NOT RE-SEATED, AND THAT WAS THE LIVE RISK:** `/mstr-spawn` step 1d-ii -- an `[ACTIVE]` TO is not evidence of UNFINISHED work, and seating a lane onto an accepted round is a REWIND (CLAUDE.md NEVER-2). The artifact was measured before the disposition, not the face.
⚠ **THE EDGE HALF IS NOW UNBUILDABLE AND THAT POST-DATES THIS FACE:** PRD v0.14 `C-19` (NO-GODADDY) -- `opalinvest.com` and `www` both resolve to the EC2 elastic IP, AWS WAF cannot attach to a bare EC2, and both candidate edges need the record repointed at GoDaddy. Andrew's *"Agreed, CloudFront"* settled the VEHICLE and never the ROUTE. Nothing in this closure reopens it.


⛔ **BLOCKERS, NAMED: `OP-s-4`, `OP-s-5`, `OP-s-18`.** The cell says this is a round-2 re-entry *"after OP-s-4 / OP-s-5 / OP-s-18: the same rule groups, logging path and IP sets, so one BLOCK row blocks at the site and the portal from one table; cut at the round-2 re-entry, never mid-round."* `OP-s-5` is DONE. **`OP-s-4` and `OP-s-18` are in flight as `TO-OP-S-4-18`. GO CONDITION: that face terminal.** Cutting before it would duplicate rule groups and IP sets instead of reusing them, which is the one thing the cell forbids.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT FWD-13; s.6 the `OP-x-2` ruling; s.5 the box is not moved) - **Decomp cell:** `OP-s-13` (v0.1.11, s.1a) - **Lane:** AE lane - **Round:** 3.

---

## THE CELL, AND THE REVERSAL IT RESTS ON

The 2026-07-13 spec said no CloudFront and no WAF for the WordPress box. **Andrew reversed that for the edge at ~08:4xZ and `OP-x-2` was ruled (a): CloudFront + WAF managed rules (PRD v0.8 s.6).** The decision is CLOSED; this face executes it and does not re-open it.

**THE BOX IS NOT MOVED (PRD s.5).** No migration, no re-platform, no instance change. **An edge in front of it, nothing else.**

## THE TWO HALVES ARE BOTH MEASURED, AND THE SECOND IS THE ONE THAT GETS FORGOTTEN

The cell's `closes on`: *"a known-bad request REFUSED before WordPress handles it AND the site still loads for a visitor (both halves measured); `/wp-admin` + `xmlrpc.php` restricted by source address at the edge in the same cell."*

> ⛔ **A WAF in front of a WordPress site is the classic false-positive surface, and this one fronts a PUBLIC MARKETING SITE.** The managed rule groups on the portal are soaking in COUNT for exactly that reason. **Do not put them in BLOCK here on day one either.** The refusal this face must demonstrate is the one the cell names -- a known-bad request refused -- and it can be demonstrated with the rule groups in COUNT plus the targeted `/wp-admin` and `xmlrpc.php` restriction, which is a source-address rule and not a heuristic. **Graduating the managed groups to BLOCK on the marketing site is a separate act on the same soak evidence as the portal's.**

## DELIVERABLE

1. **CloudFront in front of opalinvest.com**, origin the existing box, **no change to the box** -- confirm the instance and its security group are untouched by reading them before and after.
2. **REUSE, do not re-create:** the same managed rule groups and the same IP set as `TO-OP-S-4-18` built, in **COUNT** for the managed groups. **The whole point of the cell's sequencing is that ONE `BLOCK` row in the S16 table covers the site and the portal.** If the CloudFront-scope IP set from that face cannot be attached here, that is a ROW and a design question, not a second IP set.
3. **`/wp-admin` and `xmlrpc.php` restricted by SOURCE ADDRESS at the edge, in this cell** -- the allowed addresses are an INPUT you do not invent. **If no allow-list is available, file a row and ask; do not guess an address and do not leave the paths open.**
4. **DNS and certificate handling stated explicitly**, including whether the cutover is atomic and what a visitor sees during it. **A marketing site returning an error to visitors is a worse outcome than an unhardened one.**
5. **A deploy-ledger entry**, opened before and closed after, rollback named -- **the rollback is DNS back to the origin and it must be stated with its propagation reality, not asserted as instant.**
6. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~U/NFRA_OPSEC202609.TO-OP-S-13.wordpress-edge.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

**BROKER DRAIN IMMEDIATELY BEFORE THE DNS CUTOVER.**

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S13-AC1" cell_refs="OP-s-13"/> `S13-AC1` -- THE SITE STILL LOADS FOR A VISITOR, AND THIS IS GRADED FIRST: an unauthenticated GET of the site's home page through the new edge returning **200** with real page content, plus at least two further real paths. **NEGATIVE CONTROL: a path that should 404 returns 404 and not a catch-all 200.** A face that hardens a site nobody can reach has failed its own outcome.
<criterion id="S13-AC2" cell_refs="OP-s-13"/> `S13-AC2` -- A KNOWN-BAD REQUEST IS REFUSED BEFORE WORDPRESS HANDLES IT: a request the edge refuses, with the response pasted, **and evidence it did not reach the origin** -- an origin-side log absence for that request id, or the edge's own block record naming the rule. **"The edge returned 403" alone does not establish that WordPress never saw it.**
<criterion id="S13-AC3" cell_refs="OP-s-13"/> `S13-AC3` -- `/wp-admin` AND `xmlrpc.php` ARE SOURCE-RESTRICTED AT THE EDGE: both paths refused from an address outside the list and reachable from one inside it, four captures. **If the allow-list was never supplied, this files `UNCOMPUTABLE-BY-CONSTRUCTION` citing the row, and the paths are left as they were rather than guessed at.**
⛔ **RULED 2026-09-04 02:1xZ BY THE ISSUER ON `0.7.0_AE_CloudOps~U`'s LEVER -- THE TWO PATHS SPLIT AND ONLY ONE STAYS BLOCKED.**
**`xmlrpc.php`: BLOCK IT OUTRIGHT.** ⛔ **CONDITIONAL, AND THE CONDITION IS A MEASUREMENT, NOT A FORMALITY: census `xmlrpc.php` requests over the available window FIRST and show that no request in it was a SUCCESSFUL authenticated call.** Attack traffic to that path returns 401/403/405; **a 200 to an authenticated method means a real client** -- Jetpack, the WordPress mobile app, or a pingback integration -- **and a real client makes this ruling wrong.** State the window, the denominator, and the status-code distribution. ⛔ **AND APPLY TONIGHT'S OWN LESSON: check the User-Agent before trusting the volume.** If a successful authenticated call exists, **STOP, file the row, and leave the path as it was.**
**WHY THIS IS AN L6 CALL AND NOT A SCOPE WIDENING: `S13-AC3` ALREADY NAMES `xmlrpc.php` AS A PATH TO RESTRICT.** Only the SHAPE of the restriction was open, and **an outright block is STRICTLY TIGHTER than a source restriction** -- it cannot fail the endpoint's intent, it can only exceed it in the safe direction. **It is also a single WAF rule and therefore trivially reversible**, which is what keeps it below a sovereign call. **Name the rollback before the act.**
**Once blocked, `xmlrpc.php` satisfies `S13-AC2` directly**: it becomes a known-bad request refused at the edge, with the edge's own block record naming the rule and an origin-side absence for that request id. **Its `S13-AC3` limb then files `N/A-BY-CONSTRUCTION`** -- there is no "reachable from an address inside the list" leg because no source is permitted, and that is the point rather than a gap.
**`/wp-admin`: UNCHANGED. It still requires the allow list, that input still does not exist, and its limb still files `UNCOMPUTABLE-BY-CONSTRUCTION` citing `Z-S102`.** ⛔ **DO NOT extend the outright block to `/wp-admin`** -- locking every source out of the administrative interface of a live site is a different act with a different blast radius, and it is not this face's to take.

⛔ **UPDATED 2026-09-04 05:3xZ AFTER THE DERIVATION RAN. ANDREW APPROVED "derive a candidate list and bring it back". IT WAS DERIVED. THE ISSUER'S RECOMMENDATION IS NOW: DO NOT APPLY IT.**
**THE DERIVATION IS SOUND AND THAT IS WHY IT IS TRUSTED.** Window 30/Jul-04/Sep on the origin's own access logs; denominators **620,837 request lines / 105,217 to `wp-login.php` / 20,938 to `/wp-admin`**. ⭐ **The lane applied `Z-S129` FIRST and it INVERTED the obvious reading: on WordPress a FAILED login returns 200 (the form re-renders) and a SUCCESS returns 302** -- so "200 means success" is exactly backwards here, and **87,819 apparent successes are failures.** Of the 882 real ones, **868 (98.4%) are credential stuffing** -- single addresses cycling **48 distinct user-agents**, day-clustered. ⭐ **A SECOND INDEPENDENT AXIS SHARING NO FIELD AGREES: loading an admin PAGE with a 200 requires a real authenticated session, and those come from EXACTLY the five plausible addresses in the SAME RANK ORDER, with all five attack addresses returning 0 on the same matcher while it returns 672 for the top candidate** -- so the zeros are a real absence, positive-controlled.
⛔ **AND THE REASON NOT TO APPLY IT IS NOT A DEFECT IN THE MEASUREMENT -- IT IS WHAT THE MEASUREMENT SHOWS: 0 of 5 candidates can be tied to a NAMED PERSON, and they look RESIDENTIAL and DYNAMIC.** The log carries an address and a browser string; **it carries no identity.** **Applying them would approve a LOCKOUT the first time a home connection rotates** -- and one of those addresses is presumably the named WordPress administrator at TWLC.
**THE ISSUER'S REVISED RECOMMENDATION, put to Andrew: ASK THE HUMANS, and use this list to CONFIRM their answer rather than to SOURCE it.** ⭐ **If no administrator has a static address, then SOURCE-RESTRICTION IS THE WRONG CONTROL FOR THIS SURFACE and we should say so rather than ship a lockout.** ⛔ **The site is under sustained credential stuffing -- 87,819 failed login POSTs in the window -- so it does need a control; it does not need THIS one.** **`S13-AC3`'s `/wp-admin` limb stays `UNCOMPUTABLE-BY-CONSTRUCTION` citing `Z-S102` until a named human supplies a named address.**
<criterion id="S13-AC4" cell_refs="OP-s-13"/> `S13-AC4` -- THE RULE GROUPS ARE REUSED AND IN COUNT, AND THE IP SET IS SHARED: the ACL read showing the managed groups with `OverrideAction: Count`, and the IP set reference resolving to the SAME set `TO-OP-S-4-18` created -- its id or ARN pasted and compared. **A second, parallel IP set is a FAIL:** the cell's whole sequencing exists so one BLOCK row covers both surfaces.
<criterion id="S13-AC5" cell_refs="OP-s-13"/> `S13-AC5` -- THE BOX WAS NOT MOVED OR MODIFIED: the instance id, its security group ids and their rules read BEFORE and AFTER, identical. Plus the usual: unscoped baseline before, changed-resource list enumerated, unscoped re-plan 0-diff after, ledger CLOSED with rollback named, push state MEASURED.

<expected_criteria>S13-AC1, S13-AC2, S13-AC3, S13-AC4, S13-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cell `OP-s-13` (manifest S13; FWD-13; EXERCISED).
<owned_cells>OP-s-13</owned_cells>
Read-dependencies, NOT claimed: `OP-s-4` and `OP-s-18` (the GO condition and the resources to REUSE), `OP-s-5` (DONE -- the logging path), `OP-x-2` (CLOSED -- the ruling this face executes).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED **20** over 5 carriers AT THAT VINTAGE (C1 SENTINEL 20 lines -> **4** gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). The MORATORIA carrier binds: reusing an existing managed rule group is in scope; adding a group not named in an outcome is not. ⛔ **CORRECTED 2026-09-04 08:4xZ BY `1.0.0_SA_CTO~Z` (msg 20364): the tool prints 21 lines -> 5 gates because it counts a LOG QUOTING a sentinel as a gate -- `org/tier1_exec/3.0.0_SA_CVO/logs/2026-09-01/work_0312Z_comp_schedule_gate_ledger_build.md:72`. **A `.md` CANNOT gate a deploy**: `safe_deploy_core` matches that grammar against the files it is about to SHIP. The other 20 lines are authoritative deployable source. ⛔⛔ **DO NOT "CONFIRM" THIS BY RE-RUNNING `comp-schedule` -- A FRESH RUN TONIGHT ALSO PRINTS 21, BY A DIFFERENT ROUTE:** C2 DEPLOY-LEDGER has moved 4 -> 5 since this preflight, so corrected C1 4 + current C2 5 + C3 12 = 21 again. **The same total from different components would read as confirmation and would be nothing of the kind.** ⭐ The correction is trusted because it imports `comp-schedule`'s OWN `SERVE_HELD_RE` and `_full_reason` over the tool's own scope and REPRODUCES 21/5 as a control BEFORE removing the quotation -- a census that could not first reproduce the figure it corrects would not be evidence. **This figure is ORIENTATION at its stated vintage, never a criterion, and no face in this project discharges a gate.**
comp-iam: DECLARED-NOT-APPLICABLE at cut -- this face creates no role and attaches no identity policy; it stands up an edge distribution and WAF association under the existing execution identity.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim; its dependency claims are on live resources the assignee re-reads in phase 1.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S13-AC1`, `S13-AC2`, `S13-AC3`, `S13-AC4`, `S13-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~U/NFRA_OPSEC202609.TO-OP-S-13.wordpress-edge.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S13-AC1,S13-AC2,S13-AC3,S13-AC4,S13-AC5"` BEFORE the complete flip. **The control that must be able to FAIL is `S13-AC1`'s 404 negative control -- without it, a catch-all edge returning 200 to everything would read as a working site.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Confirm `TO-OP-S-4-18` is terminal and read the IP set and rule groups it actually created -- reuse depends on their real identifiers, not on this face's expectation of them. Read the instance and its security groups for the before-state.</phase>
  <phase id="2" when="before the cutover">A broker drain, the ledger opened, the DNS rollback stated with its propagation reality.</phase>
  <phase id="3" when="after the cutover">Visitor-path reads FIRST, then the refusal evidence, then the box's before/after comparison.</phase>
</compiler_tools_mandate>
