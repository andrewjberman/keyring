# TO NFRA_OPSEC202609.TO-OP-S-13 -- opalinvest.com GETS AN EDGE: CloudFront + the same WAF managed rules already soaking on the portal, so a known-bad request is refused BEFORE WordPress handles it and one BLOCK row covers the site and the portal from one table -- and the site still loads for a visitor (OP-s-13, FWD-13)

<to_id>NFRA_OPSEC202609.TO-OP-S-13</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~U</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

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
<criterion id="S13-AC4" cell_refs="OP-s-13"/> `S13-AC4` -- THE RULE GROUPS ARE REUSED AND IN COUNT, AND THE IP SET IS SHARED: the ACL read showing the managed groups with `OverrideAction: Count`, and the IP set reference resolving to the SAME set `TO-OP-S-4-18` created -- its id or ARN pasted and compared. **A second, parallel IP set is a FAIL:** the cell's whole sequencing exists so one BLOCK row covers both surfaces.
<criterion id="S13-AC5" cell_refs="OP-s-13"/> `S13-AC5` -- THE BOX WAS NOT MOVED OR MODIFIED: the instance id, its security group ids and their rules read BEFORE and AFTER, identical. Plus the usual: unscoped baseline before, changed-resource list enumerated, unscoped re-plan 0-diff after, ledger CLOSED with rollback named, push state MEASURED.

<expected_criteria>S13-AC1, S13-AC2, S13-AC3, S13-AC4, S13-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.11), cell `OP-s-13` (manifest S13; FWD-13; EXERCISED).
<owned_cells>OP-s-13</owned_cells>
Read-dependencies, NOT claimed: `OP-s-4` and `OP-s-18` (the GO condition and the resources to REUSE), `OP-s-5` (DONE -- the logging path), `OP-x-2` (CLOSED -- the ruling this face executes).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). The MORATORIA carrier binds: reusing an existing managed rule group is in scope; adding a group not named in an outcome is not.
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
