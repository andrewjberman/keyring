# AMGT_RESAPP task order -- `AMGT-ar-3` -- THE CODE REDEPLOY CARRYING ar-1 AND ar-2 (FWD-39 CENSUS REPAIR, PLAIN REASON WORDS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one code-only redeploy by hand.
comp-iam: RUN by the issuer at the cut -- ar-1 and ar-2 declare no new read or write. The halves list every S3 read path the content diff adds, and each one carries a simulate-principal-policy arm reading allowed on opal-amgt-scoped-api-role before the code leg is called LANDED (CTO round-67 ruling 4).
comp-adversary: RUN by the issuer at the cut -- on deployed 2rFeF57l, r68_served c27 and c28 FAIL (6 own-name, 82 boilerplate; 18/3/12 jargon reasons).
EGRESS CLASS, declared: NONE for the act; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ar-3` (round 68, decomposition s.76)

Under ONE NEVER-2 entry and ONE never-widen pair, redeploy `opal-amgt-scoped-api` at the build commit the GO names, carrying ar-1 and
ar-2. Build and upload ONE artifact, then ONE code-only `safe-apply`. `memory_size` stays 1769.

**Begin only when** the GO names the build commit and both halves are committed. Then:
- **Re-read the base CodeSha256 live.** It is the one the halves name, `2rFeF57lMh8MkU6WRgZyImZt7RMlW14BdxmUjIBvSSQ=` (the AMGT_CORPUS
  al-5 build), unless another project's closed NEVER-2 entry since then records a newer one. Any other value is a STOP.
- **Two projects deploy this function.** Read `org/critical_paths/.open_deploys/` first. If another entry on this function is open,
  wait for it to close.
- **Build from a detached checkout at the build commit.** The CONTENT-DIFF runs against the DEPLOYED build, never an older pin. Any
  CHANGED/ADDED/REMOVED file not on the halves' list is a STOP.
- **For every new S3 read path the halves list,** a `simulate-principal-policy` on the function's role must read `allowed`. If one does
  not, it is a STOP: no grant rides this act.
- **Any destroy, IAM, route or gateway change in the plan is a STOP.**
- **The package is near its ceiling:** print the build's size. A build over 262,144,000 B is a STOP.

A failing criterion is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change, no store write, no S3 delete, no vendor call, no push of shared
   branches, no portal promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 2400)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ar-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell c27 --where deployed; echo "exit=$?"</invocation><expect>run from a checkout at the build commit: population 0 non-200; C1 and C2 PASS over every cloud-serving name; R68 C27 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell c28 --where deployed; echo "exit=$?"</invocation><expect>C1, C2 and C3 PASS; R68 C28 SERVED: YES on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ar-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c23 c25 c26; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py" --cell $c --where deployed || exit 1; done; echo "exit=$?"</invocation><expect>R67 C23, C25 and C26 SERVED: YES on the deployed function (no regression); and exit=0</expect></criterion>
</proof_of_spec>

The following are run with them and reported (no regression), and the issuer re-reads them:
- `r67_served.py --cell c24 --where deployed`: mismatches 0, unreadable 0, and no-table-row unchanged from the base read;
- `r64_served.py --cell c9 / c10 (30-day clauses) / c11 / c12 / c13 / c14`, `r65_served.py --cell c17`, and
  `r66_served.py --cell c18 / c19 / c22`, all `--where deployed`;
- `r64_served.py --cell c15 --where deployed`, cold, on the day route.

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control. It goes at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ar-3.the-code-redeploy.proof_of_spec.json`, and
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256 and the artifact VersionId;
- the CONTENT-DIFF summary and the package size;
- every criterion's output lines;
- the regression reads.

Stamp any row's `surfaced_at` with `date -u`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.76; staged until ar-1 and ar-2 drain and the pair is signed. CTO round-67 rulings 4 and 5.

<status>staged</status>
<round>68</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-05 ~01:5xZ):** both halves are committed and the build commit is `7158bc9d4d`.
- COO: `round68/NEVER_WIDEN_HALF_COO_AR3.md` @f20719a16c.
- CTO: `ledger/NEVER_WIDEN_ROUND68_AR3_CTO_HALF.md` @090ba579d3, SIGNED under three conditions:
  1. at build time, re-read the deployed code; the CONTENT-DIFF must be exactly the 2 files;
  2. grade c27 and c28 on the DEPLOYED function, over 233 names / 199 serving;
  3. one NEVER-2 entry opened before the upload, and the proof in the DEPLOY genre with base-vs-new CodeSha256.
- Base: `2rFeF57l...`, VersionId `O1WGPxfTK9vszvvZqzzuOfjQAGMOIZiM`. New S3 read paths: none.

<status>pending</status>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~03:1xZ):** CLOSED.
- AE~A instance @0beac8cabc is VALID (rc=0), genre DEPLOY.
- `2rFeF57l` -> `6wwEU3Sw`; VersionId `O1WGPxfT` -> `3eIFUS9k`; 1769. CONTENT-DIFF exactly the 2 files.
- AC1 c27 YES (233/199): own-name 6 -> 0, boilerplate 82 -> 0. AC2 c28 YES: 18/3/12 -> 0. AC3 YES. 13 of 13 reported reads YES;
  c15 cold 1.84-1.95 s. The NEVER-2 entry is closed.
- Issuer real run @ `round68/REAL_RUN_r68_deployed_20261005.txt`: c27, c28, c23, c24, c25 and c26 all YES on `6wwEU3Sw`.

<status>complete</status>
