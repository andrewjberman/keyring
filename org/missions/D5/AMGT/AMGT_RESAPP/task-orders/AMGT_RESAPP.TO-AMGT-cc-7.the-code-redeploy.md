# AMGT_RESAPP task order -- `AMGT-cc-7` -- THE ROUND-79 REDEPLOY: ONE READ GRANT, THEN THE CODE THAT SERVES THREE NAMED HOOKUPS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-cc-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no new cron, alarm, monitor or cadence; one redeploy by hand. The daily snapshot schedule is unchanged.
comp-iam: RUN by the issuer's drafting read at the cut (round79/GROUP_E_NOTES.md) -- the role opal-amgt-scoped-api-role holds one inline policy, opal-amgt-scoped-api-grants: 33 object-read resources and 33 list prefixes, 0 naming job_record; this act adds ONE read-only prefix to both limbs and nothing else. The plan STOPs on any IAM change the pair does not list.
comp-iam coverage: BLIND to an IAM change outside the plan; no simulate-principal-policy call was made at the cut.
comp-adversary: RUN by the issuer at the cut -- the deployed function +s6R0/rc reads last round's list YES (R78 DEPLOYED: YES 3 of 3, the issuer's one real run 2026-10-08 09:02Z) and serves none of segment_table, dossier_sections or a Seeking Alpha state, so this round's deployed line FAILS until this act. At CLOUD HEAD the build's own gate (gen_harvest_prefixes.py --check) exits 1; cell cc-5 repairs it before the commit the GO names.
EGRESS CLASS, declared: NONE. The build fetches nothing from the internet: its wheels are files on this box and two packages come from the deployed zip.
</preflight>

## 1. THE ACT -- `AMGT-cc-7` (round 79, decomposition s.87)

Under ONE NEVER-2 entry and ONE never-widen pair, with THREE legs recorded apart:

1. **Grant leg (IAM).** Before anything else, read the role's inline policy and save it whole: role `opal-amgt-scoped-api-role`, policy `opal-amgt-scoped-api-grants`. It is the BEFORE of this leg.
2. **Code leg.** Build from a DETACHED worktree at EXACTLY the commit the GO names, never "at or after" it. `memory_size` stays 1769.
   - **The build fetches nothing.** In its environment: `AMGT_DEPLOYED_ZIP` naming the zip of the package that is live NOW (the GO gives the path; its sha256 in base64 must equal the live CodeSha256, and the build stops if it does not), `PIP_NO_INDEX=1`, `PIP_FIND_LINKS` naming the folder of six wheel files the GO gives, and `PIP_LOG` naming a file you attach. If either pip step cannot resolve from that folder the build STOPS; no variable is unset to get past it. Before you run the script, read its lines in `org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/SITEZ_INSTALL_DOWNLOAD_LINE_CENSUS_20261007.md`.
   - Build `--build-only <a kept path>` and upload THAT file, not a rebuild.
   - Before the upload: (a) `r78_bb23.py --compare-zip <the kept zip>` with `R78_BB23_DEPLOYED_ZIP` set to the live package's zip reads EQUAL: YES, 147 of 147; (b) the CONTENT-DIFF the pair lists is what the build prints, measured against the live package. A file not on the list is a STOP. A vendored file reading CHANGED is a STOP, except any the pair names with its reason.
   - ONE `safe-apply` on `infra/aws/terraform/harvest/`, the plan graded UNTARGETED. It may move exactly TWO resources: the function's code (`module.scoped_amgt_api.aws_lambda_function.this`: its artifact object and hash) and the role's inline policy (`aws_iam_role_policy.scoped_amgt_api_grants`: ONE added read-only prefix in the object-read resources and the same ONE in the list condition). No route, no memory, no schedule, no other IAM line. Any other resource, or any other change inside the policy, is a STOP before the apply.
   - The new CodeSha256 differs from the live one AND equals the kept zip's. An unchanged hash is a 0-diff deploy: STOP.
   - After the apply, read the role's inline policy again and save it whole: the AFTER of the grant leg. It reads the BEFORE plus one line in each of the two limbs and nothing else changed (the pair gives the counts).
   - Then run `round71/checks/leadpanel_cold_warm.py --label after` and read the cold invokes' `AMGT_PHASE` lines. Reported, not graded.
3. **Snapshot leg.** After the code leg, invoke the snapshot's scheduled event once (`{"amgt_scheduled_action": "refresh_freshness_snapshot"}`), so the /freshness snapshot is written by the new code with the Seeking Alpha states. Read its stamp. If the event answers that the read was not complete and nothing was written, that is NOT a rollback of the code: report it and stop before AC1 (the grant may not have reached the function yet; say what the event printed).

**Begin only when** the GO names the build commit and both halves are committed. Read every live worktree's `.open_deploys/` (`git worktree list --porcelain`, then `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/`), and measure the artifact before acting on any entry you find. `r79_deployed_cells.txt` (beside the round-79 checks) lists the round's deployed checks; the GO states how many lines it holds.

A failing criterion is the ROLLBACK trigger: the prior artifact through the module and the prior policy text, one `safe-apply`. **Pins:** r76 c62 and c63, and r75 c59 with its 40-wide burst. A c59 that reads UNMEASURED (exit 2) is NOT a rollback trigger: report it and stop.

**The three hookups this act serves, by name** (the pair lists the same three; a hookup missing from the built package is a STOP):
- `segment_served.serve_segment_table`, called in `read_thesis_bundle`: `/thesis` gains the key `segment_table`.
- `dossier_sections.dossier_sections`, called in `read_thesis_bundle`: `/thesis` gains the key `dossier_sections`.
- `collector_read.seeking_alpha_by_security`, called in `read_coverage_freshness`: each /freshness row gains `seeking_alpha`.

**Also in your record:** the Lambda source map's note for this function still says the artifact was never uploaded (row AMGT_RESAPP-Z-S370). Correct that note in this deploy's own source-map update, to say what is true after this act.

## 2. BOUNDS

1. The act and nothing else. No memory change, no IAM change the pair does not list, no S3 delete, no vendor or SEC call, no push of shared branches, no portal promote, nothing fetched from the internet.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-cc-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/checks/r79_deployed.py"; echo "exit=$?"</invocation><expect>every listed round-79 deployed check passes; R79 DEPLOYED: YES n of n with n equal to the count the GO states; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-cc-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for c in c62 c63; do PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round76/checks/r76_served.py" --cell $c --where deployed || exit 1; done &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c59 --where deployed; echo "exit=$?"</invocation><expect>R76 C62 and C63 SERVED: YES (unless the pair states a round-79 cell changes what they read, and then as the pair says) and R75 C59 SERVED: YES with one or more cold invokes inside the bar, on the deployed function; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-cc-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round78/checks/r78_deployed.py" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_served_shape.py" --where deployed; echo "exit=$?"</invocation><expect>R78 DEPLOYED: YES 3 of 3 and R77 SERVED SHAPE: YES on the deployed function (no regression, unless the pair names one a round-79 ruling intends); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback and base-vs-new CodeSha256 as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-cc-7.the-code-redeploy.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the prior and new CodeSha256, and the kept zip's path;
- the role policy BEFORE and AFTER: the two counts in each limb and the one added line;
- the CONTENT-DIFF and size, and the pip log's index-request count (expected 0);
- every criterion's output lines;
- the leadpanel AFTER output and the cold `AMGT_PHASE` table;
- the snapshot stamp after the event and what the event printed.

Stamp any row's `surfaced_at` with `date -u`.

## AMENDMENT 1 (2026-10-08 ~14:3xZ, by the issuer on the CTO half's ruling) -- FOUR LEGS, THE GRANT FIRST IN ITS OWN APPLY

This amendment REPLACES the order of acts in section 1 wherever they differ. The pair is:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round79/NEVER_WIDEN_HALF_COO_CC7.md` (read it whole: its tables are
your STOP lists, its section THE NEGATIVE ARM holds the eight literal commands, and its section THE ISSUER'S CALLS holds eleven
terms) and `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_RESAPP_R79_CC7_REDEPLOY_20261008.md` (read it whole: GRANT
FIRST, and conditions C1 to C3). ONE NEVER-2 entry, FOUR legs recorded apart:

- **LEG 1, the grant, in its OWN apply, BEFORE any build or upload.** Save the role's inline policy whole (BEFORE). Run the
  eight arms (BEFORE). Then ONE `safe-apply` on `infra/aws/terraform/harvest/` from a DETACHED worktree at EXACTLY the pin the GO
  names, the plan graded UNTARGETED: it shows `aws_iam_role_policy.scoped_amgt_api_grants` ALONE, gaining one resource and one
  prefix value. Any other resource in that plan is a STOP before the apply. Save the policy whole again (AFTER: 34 and 34, the
  two added lines, nothing else changed) and run the eight arms again: P1 and P2 read `allowed`, N1 to N4 read `implicitDeny`,
  C0 and C1 read `allowed`. An `allowed` on N1, N2 or N3: roll the grant back and STOP; nothing else has moved.
- **LEG 2, the build**, as section 1's code leg says (the gate, the two compares, the CONTENT-DIFF: CHANGED 12, ADDED 4, REMOVED 0,
  exactly the two tables of the COO half; 0 vendored lines). No apply in this leg.
- **LEG 3, the code, in its OWN apply.** Upload the kept zip, then ONE `safe-apply`, the plan graded UNTARGETED: it shows
  `module.scoped_amgt_api.aws_lambda_function.this` ALONE. Then the hash rule and the leadpanel run of section 1.
- **LEG 4, the snapshot event.** Read `head-object` on the snapshot object immediately before the event and record THAT
  VersionId as the rollback key. Send the event once. Branch A (200, a new VersionId, 302 rows): wait 65 seconds, then AC1; AC1
  prints the stamp of the view that answered, and an old stamp means wait 65 seconds more and run again. Branch B (500, nothing
  written): report its body, run P1 and P2, and stop before AC1; ONE more event is allowed only when P1 and P2 read `allowed`,
  each event's body and both VersionIds recorded; never a third.
- **Windows (CTO C3):** not while a Bloomberg pull is writing; not inside the 12:30Z scheduled snapshot write.
- **From the snapshot event's log line, report the duration of the one view build inside the function** (CTO C1).
- **c59 (AC2):** run it within minutes of the event with nothing else running on the box. A C1 difference confined to rows
  whose store object is newer than the snapshot's `generated_at` is NOT a rollback trigger: print the differing rows and their
  stamps and stop for the issuer. Any other C1 difference, or C2 or C3 reading NO, is the rollback trigger.
- **Rollback:** the code and the snapshot roll back TOGETHER (the prior artifact through the module, then copy-object of the
  snapshot's prior VersionId; never a delete); the grant by removing the one list entry and applying.
- The source-map note takes the text of the COO half's section SOURCE MAP, with no hash in it.
- This amendment supersedes the preflight line that says no simulation was made: the COO half made ten.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.87; staged until the adapter cell (cc-6) and the repairs cell (cc-5) drain and the pair is signed. CTO round-78 analysis R1: the pair LISTS the three hookups by name. CTO msg 31672: the grant is its own leg with its own before and after. At the GO the issuer names: the build commit; `AMGT_DEPLOYED_ZIP` (`C:/tmp/bb18-r78-fbb643923e.zip`, the package live since 2026-10-08T07:19:32Z, kept by round 78); the wheel folder (`C:/tmp/bb18-wheels`, six files, hashes in `round78/BB18_WHEEL_FOLDER_SHA256_20261008.txt`); and the list count. Checks dry-run at the base: cc-7 AC1 base NO CELLS LISTED exit 2 (FAIL as expected); AC2's pins as round 78's bb-18 read them on +s6R0/rc; AC3 base YES (the issuer's one real run of round 78).

<status>staged</status>
<round>79</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<status>staged -- AMENDMENT 1: four legs, the grant first in its own apply (CTO half, msg 31782); the pair is signed by both seats at the pin 63f0605039; no GO yet</status>
<status>pending -- GO given 2026-10-08T15:14Z (msg to 0.7.0_AE_CloudOps~A): pin 63f0605039, both halves on origin @2d0d4296bf, four legs, the grant first; call 11 read at HEAD 2d0d4296bf (opal_naming.py +12 and exemptions.json only differ from the pin)</status>
<status>complete -- landed @42700562a4 by 0.7.0_AE_CloudOps~A (msg 31985): four legs, grant 33->34, code ltXvElw = the kept zip, snapshot ar7KPWgP 18:08Z; proof VALID; ledger CLOSED. Re-run by the issuer on the shared tree 2026-10-08T21:4xZ: AC1 R79 DEPLOYED YES 1 of 1; AC3 R78 DEPLOYED YES 3 of 3 and R77 SERVED SHAPE YES; AC2 c62 YES, c63 YES, c59 C2 and C3 PASS, C1 301 of 302 at 3.2 h after the event: the one row NG/_LN differs only by a Seeking Alpha record written 20:41Z, newer than the snapshot's generated_at 18:08Z -- the class the order names as NOT a rollback trigger; the seat's run within minutes of the event read 302 of 302. Graded YES by the issuer</status>
