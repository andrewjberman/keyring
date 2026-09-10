# ETFS_GUARDRAIL -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Opened by:** `2.0.0_SA_COO~B` at the L6 issuance (a seat row; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`,
identity, folder == project, the allocator coordinate). Lane `ANY`.
**Id grammar:** a worker's row is `ETFS_GUARDRAIL-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that
coordinate); a seat's row is `ETFS_GUARDRAIL-S<k>`; the CVO's adjudication rows live in `../adjudications/` as
`ETFS_GUARDRAIL-C-S<k>`. **Append-only during the round.** Never edit an existing row.
**Round 1 task orders:** 14, one per cell of `../../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.1.1, on three worker
slots (`0.9.0_WK_ETFS_GUARDRAIL~1`, `~2`, `~3`).

```json
[
  {
    "id": "ETFS_GUARDRAIL-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-04T19:05:00Z",
    "one_line": "EG-s-4: PRD s.7.4 homes the classifier in the ETFS layer and s.7.2 S4 binds its discriminator as 'read upstream partition + count priced' -- but the ETFS layer holds ZERO firm-bucket grants by explicit NEVER#1 design (reporter role: opal-data-etfs/* + the artifact prefix only; aggregation reader: daily/* + config/* only). L5 delegates the discriminator to the firm-scoped producers as a non-writing PROBE (EG-s-1/EG-s-2) and to the relied-on inf producer's own invoke answer; the classifier stays etfs-only and returns UNKNOWN where no probe answers; the one IAM change is an invoke grant on the reporter role (EG-s-7). No firm prefix is opened. Carried for the CTO's L10 read; not a spec edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/etfs-reports/iam.tf:24-59 @291551ca2f -- the reporter instance role's policy: ReadEtfsAggregation (s3:GetObject opal-data-etfs/*), ListEtfsAggregation, WriteReports (platinum/reports/* only), PullRendererArtifact (opal-313476888478-lambda-artifacts/ec2/etfs-reports/*); no statement names opal-data-assets, opal-data-inf, opal-data-cot or opal-data-bd",
        "infra/aws/terraform/shared-infra/etfs-aggregation-iam.tf:1-60 @291551ca2f -- the AVGCAP reader role scoped to opal-data-etfs/daily/* + config/* with the header comment 'ZERO firm-bucket grants (NEVER#1: the metric layer never reads opal-data-inf / opal-data-cot / opal-data-schwab)'",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/prd/ETFS_GUARDRAIL_PRD.md s.7.2 row S4 and s.7.4 @4e30d6b635 -- the bound 'Discriminator = read upstream partition + count priced' and the home 'data/etfs/scripts/coverage/classifier.py ... importable by the renderer'; s.7.4's own clause 'These are step-4 PROPOSALS ... a decomp finding may overturn any of them'",
        "infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py:98-144 @291551ca2f and infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py:68-95 -- each owned producer already performs the discriminator on its own firm's partition (head_object on the date= partition; priced / rows count) under its own least-privilege role"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD s.7.2 S4 bound: 'Discriminator = read upstream partition + count priced'; s.7.4: 'S4 classifier -> data/etfs/scripts/coverage/classifier.py. One home, importable by the renderer.' Read together: the classifier, running in the ETFS layer on the reporter box, reads the three firms' upstream silver partitions.",
    "world_is": "The ETFS layer's principals (etfs-reports-reporter-role; etfs-avgcap-reader-role) hold no grant on any firm prefix, by a design that names NEVER#1 as its reason. Granting the reporter role s3 reads on blackdiamond/cottonwood/*, schwab/08242234/* and orion/inflection/* in opal-data-assets would mint the cross-firm reader that design refused. The producers already hold exactly the per-firm read the discriminator needs.",
    "notes": "L5/L6 resolution (decomposition v0.1.1 s.6a): probe mode on EG-s-1/EG-s-2; the inf producer's own invoke answer for Inflection; EG-s-4 etfs-only with an injected probe and UNKNOWN as an honest value; EG-s-7 holds the invoke and the one IAM Sid (lambda:InvokeFunction on three producer ARNs, reporter role, ledgered). If the CTO's L10 read prefers a data grant instead, that is a PRD addendum at L4 and the cells re-cut; nothing in this round opens a firm prefix. Disarm needs nothing: INERT, an OBSERVATION for the record."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-04T20:15:45Z",
    "one_line": "EG-s-3 AC1 bound 'the source's own battery is green at HEAD' is FALSE: test_catchup_scan.py crashes at import (KeyError: ASSETS_BUCKET) before it ever calls the real _catchup_missing_dates -- it was landed against the PRE-repoint shape and nobody re-vendored it across the 2026-08-02/03 repoint.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py@5376ecaa8b -- sets os.environ INF_BUCKET/HOLDINGS_PREFIX (not ASSETS_BUCKET/FACT_POSITIONS_PREFIX/META_DEDUP_PREFIX/CONFIG_KEY/OUTPUT_PREFIX/PARTNER) and calls lf._catchup_missing_dates(universe=[...], skip_date=...) with two kwargs against a real signature that takes three positional args (universe, all_dates, skip_date); it also monkeypatches lf._holdings_key_for/_holdings_exists/_compute_and_write_slice(src_key, universe), names lambda_function.py does not define at HEAD",
        "python -m pytest infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py -q run this turn @5376ecaa8b -- rc=2, '1 error during collection', KeyError: 'ASSETS_BUCKET' raised importing lambda_function.py:77, i.e. the module under test never finishes loading and _catchup_missing_dates is never invoked",
        "git log -1 --format=%H\\ %ad --date=iso 288bfe8378 -- (2026-08-01 15:50:34 -0400, test landed) vs 001a73530a -- (2026-08-03 18:01:50 -0400, 'complete the stranded COMMIT leg of the half-landed inf-etf deploy': introduces ASSETS_BUCKET/FACT_POSITIONS_PREFIX/META_DEDUP_PREFIX + dedup_core.py, i.e. the repoint the test predates and was never updated across",
        "infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py:74-84,271-295@5376ecaa8b -- the live env-var names and the live _catchup_missing_dates(universe, all_dates, skip_date) signature, both incompatible with the test's stubs and call"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO EG-s-3 THE CELL: 'Its own battery test_catchup_scan.py drives the REAL _catchup_missing_dates() unmodified with the S3 collaborators stubbed -- both arms (a hole found; nothing found) required.' Acceptance S3-AC1: 'the source's own battery is green at HEAD, both arms (record N passed).'",
    "world_is": "The battery does not run: it fails at module-import collection (rc=2, KeyError: 'ASSETS_BUCKET') before _catchup_missing_dates is ever called, because it stubs env vars and helper names from the PORT SOURCE's pre-2026-08-02/03-repoint shape. It has been dead since 001a73530a (2026-08-03), ~32 days, silently -- a regression in the real catch-up sweep since then would have gone uncaught by this fixture, which is precisely the failure mode INF_ETF_OWNERSHIP_SCHEDULED_FLOOR AC4p2 built it to catch.",
    "disarm_owner": "3.0.0_SA_CVO (routes the re-vendor: this order's bound is READ the port source and run its battery, not edit it -- 'PORT SOURCE. Relied on, NOT owned -- do not modify to suit the port'; fixing test_catchup_scan.py against the repointed shape is outside EG-s-3's write lane and outside this project's ownership of inf-pipeline)",
    "notes": "S3-AC1 is graded FAIL by output this turn (rc=2, not 'passed'); the TO's other four criteria (S3-AC2..AC5) are unaffected -- the port contract in the deliverable is built from a direct read of lambda_function.py's live bytes, not from the broken test's assumptions."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-04T20:11:30Z",
    "one_line": "EG-s-10's suggested default (vendor lib/trading_calendar.py byte-identical as a new in-repo copy) and TO-EG-s-1/TO-EG-s-2's MANDATORY instruction to do exactly that (S1-AC3, S2-AC3 mechanically check for a fifth and sixth byte-identical vendored copy) run against a live CTO ruling, landed 11 days before this round's L6 issuance, that a fifth in-repo copy of this file IS inline vendoring needing explicit approval nobody gave, and that new consumers should get the Lambda layer instead -- scoped by that same ruling to ONE function only, not migrated to the pre-existing three.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/etfs-positioning/producer-lambda.tf:169-183 @1da1e2b73b -- 'CTO~Z ruled (msg 5462): MINT THE LAYER, NOT A FIFTH COPY. Rule 3 is dispositive -- dependencies go in layers and inline vendoring needs explicit approval; a fifth in-repo copy IS inline vendoring and nobody approved one. The estate's four existing byte-identical copies are that exception taken four times without a word.' and '... this authorises the layer for THIS function and nothing else. The three pre-existing Lambda copies are NOT migrated -- a separate cell with its own owner.'",
        "commit 1da1e2b73b @2026-08-24T18:47:25-04:00 (subject: 'a first-party trading_calendar layer that adds NO fifth in-repo copy') -- the ruling's landing date, 11 days before this round's L6 issuance @5376ecaa8b (2026-09-04T15:25:37-04:00)",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-1.cot-catch-up-port-reporting-obligation-window.md:23,36-37 @5376ecaa8b -- 'trading_calendar.py vendored byte-identical from lib/trading_calendar.py into the source dir ... and added to the source map files'; S1-AC3 mechanically checks CAL_VENDORED_IDENTICAL=True for infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/trading_calendar.py (a file that does not exist at HEAD per S10-AC4)",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-2.bd-49f-catch-up-port-the-tail-a-straight-port-misses.md:22,36-37 @5376ecaa8b -- 'Vendor trading_calendar.py byte-identical from lib/'; S2-AC3 mechanically checks the same for infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/trading_calendar.py",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/prd/ETFS_GUARDRAIL_PRD.md:399 @4e30d6b635 and decompositions/ETFS_GUARDRAIL_DECOMP.md:51 @5376ecaa8b -- neither the PRD's S10 row nor the decomp cell mentions the layer mechanism or the 2026-08-24 ruling; both describe only the 4-copies-vendored state"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-10 (this order) names vendoring byte-identical 'the same pattern inf-etf-ownership-daily already uses' as the presumptive answer, asking only for a reason if a different mechanism applies; TO-EG-s-1 and TO-EG-s-2, already issued in this same L6 batch to sibling workers, state vendoring as MANDATORY (not proposed) and grade it mechanically (S1-AC3, S2-AC3).",
    "world_is": "A committed CTO ruling (producer-lambda.tf:169-183 @1da1e2b73b, 2026-08-24) already exists in the tree stating a fifth in-repo copy of trading_calendar.py needs explicit approval nobody has given, that the estate's four existing copies are an unapproved exception 'taken four times without a word', and that the Lambda-layer mechanism it mints is scoped to ONE function only -- not a retroactive fix for the three pre-existing copies, and (by its own terms) not a license for a fifth/sixth either without the same scoped authorization. The PRD (s.7.2 S10, written after the ruling) and this round's decomposition do not cite it; TO-EG-s-1/TO-EG-s-2 direct exactly the act ('mint a fifth copy without approval') the ruling names as the thing to stop doing.",
    "notes": "This TO (EG-s-10) is VERIFY-only and changes no code; the conflict is recorded here for the CVO's L9 read and for whichever of EG-s-1/EG-s-2's workers reaches the vendoring step first. Disarm: the COO either (a) treats this ruling as the 'explicit approval' precondition and lets EG-s-1/EG-s-2 proceed as written (a decision, not a default), or (b) amends the two TOs to the layer mechanism before their vendoring criteria are exercised. Left alone, the round proceeds to mint the fifth and sixth copies exactly as the ruling forbade doing without a word."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S2",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-04T20:51:26Z",
    "one_line": "TO-EG-s-10's <proof_of_spec> block obliges the assignee to flip the TO's own <status> line to complete and commit it, but the TO's <paths> grant (its write surface, and the assignee's write surface generally per canonical workflow L7) does not name org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ -- a cut defect that is systemic across this round's whole 14-TO issuance, not unique to this cell.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-10.the-trading-calendar-each-producer-resolves.md <paths> block @5376ecaa8b -- lists 7 paths (lib/trading_calendar.py, lib/tests/, 3 vendored copies, this worker's own deliverables/ dir, the investigation file); task-orders/ is absent",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-10...md <proof_of_spec> block @5376ecaa8b -- '...validates it with python .tools/proof-of-spec-check.py <instance> ... BEFORE the complete flip (the task order's <status> line set to complete), which you commit yourself together with the instance and the result'",
        "systemic check across the same L6 issuance: TO-EG-s-1, TO-EG-s-2, TO-EG-s-3, TO-EG-s-4, TO-EG-s-11, TO-EG-s-12, TO-EG-s-13 <paths> blocks @5376ecaa8b -- none of the 7 sampled sibling TOs names org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ either, while each carries the identical '<status> flip ... which the assignee commits itself' instruction",
        ".tools/safe-commit.sh:678-698 @HEAD -- the TO-issuance gate (to-pipeline-gate.py) is documented 'PROSPECTIVE ONLY: fires on NEWLY-ADDED task_orders/*.md; never refuses an existing TO', so no live mechanical gate would refuse an edit to an existing TO's status line -- the bound is the L7 identity line's write-surface rule, not a technical block, and this row exists because that rule is followed rather than tested against"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-10's own <proof_of_spec> block: '...which you commit yourself together with the instance and the result', following the harness identity line's general instruction 'flip the task order's <status> to complete and commit instance, deliverables and flip together'.",
    "world_is": "The same TO's own BOUNDS clause: 'Your write surface is the <paths> block below and nothing else... A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.' The <paths> block does not name task-orders/. The two clauses of the same document are in direct tension, and the gap repeats across every sampled TO in this round's issuance -- a shared dependency (the issuance's path-grant template), not a one-off.",
    "notes": "This worker does NOT edit the TO file to perform the flip; all 5 mechanical/judgment criteria (S10-AC1..AC5) are otherwise satisfied and the proof-of-spec instance validates VALID rc=0. The order is left at its issued status (pending) rather than mis-flipped. Disarm: the COO either widens the <paths> grant on this and the sibling TOs to include the task-orders/ file (or the specific TO path), or performs/authorizes the flip itself at L8 compile, or clarifies that the flip is intended to ride a different, unnamed mechanism (e.g., compiled at L8 rather than by the worker). Left alone, no worker in this round can close its own order without either violating its own write-surface bound or leaving it open."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S3",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-04T22:21:13Z",
    "one_line": "TO-EG-s-10's own <proof_of_spec> text names the instance path 'ETFS_GUARDRAIL.TO-EG-s-10.proof_of_spec.json' (the short to_id form), but .tools/to-pipeline-gate.py's check_complete_flip derives the expected filename from the TO markdown's FULL basename stem plus '.proof_of_spec.json' -- so the status flip was REFUSED ('NO proof-of-spec instance was found beside it') against the correctly-named, already-VALID instance until this worker renamed the file (git mv, within its own deliverables/ grant) to match the gate's derivation.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-10.the-trading-calendar-each-producer-resolves.md <proof_of_spec> block @5376ecaa8b -- 'The ASSIGNEE fills a ... instance at org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-10.proof_of_spec.json' (short to_id form, no descriptive suffix)",
        ".tools/to-pipeline-gate.py:1259-1266 @HEAD -- check_complete_flip computes `stem = os.path.basename(rel).rsplit('.md', 1)[0]` (the FULL TO filename minus .md) then globs `deliverables/*/{stem}.proof_of_spec.json` -- for this TO that resolves to 'ETFS_GUARDRAIL.TO-EG-s-10.the-trading-calendar-each-producer-resolves.proof_of_spec.json', not the short form the TO's own text names",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/NFRA_CLDGRPH.TO-CG-V-2.reachability-iam-authkind-verified.proof_of_spec.json @HEAD -- the established convention IS the full-stem form (matches the gate's derivation), so this TO's own <proof_of_spec> text is the outlier, not the gate",
        "safe-commit run this session, first attempt (pre-rename): '[to-pipeline-gate] REFUSED -- ... flips to complete on PIPELINE-REGISTERED project ETFS_GUARDRAIL, and NO proof-of-spec instance was found beside it', rc=1 -- reproduced live, not inferred"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-10's own <proof_of_spec> block names the instance file 'ETFS_GUARDRAIL.TO-EG-s-10.proof_of_spec.json', and this worker filled and validated exactly that file (VALID rc=0 twice, once per worktree).",
    "world_is": "The live mechanical gate that actually decides whether a complete flip is admitted (.tools/to-pipeline-gate.py check_complete_flip) does not read the TO's <proof_of_spec> text at all -- it derives the expected filename purely from the TO markdown's own basename, which includes the descriptive suffix the TO's prose form omits. A worker following the TO's own instructions verbatim produces a file the gate cannot find.",
    "notes": "Disarmed by this worker's own act (git mv to the gate-derived filename, re-validated VALID rc=0, artifact-resolution pins corrected to the commits that actually carry the two co-authored artifacts), which is within this worker's write grant (its own deliverables/<serial>/ folder). Filed as OBSERVATION/ARMED because the SAME short-form naming instruction appears verbatim in every sibling TO's <proof_of_spec> block in this round (S1-AC.., S2-AC.. etc. all name '<PROJECT>.<TO-ID>.proof_of_spec.json' without the descriptive suffix) -- any sibling worker who fills the instance exactly as instructed and then attempts the flip will hit the identical refusal. Disarm: amend the <proof_of_spec> text on the remaining round faces to the full-stem form, or teach the gate to also try the short-id form."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S2",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-04T22:19:59Z",
    "one_line": "TO-EG-s-3's own <proof_of_spec> block names the instance path 'ETFS_GUARDRAIL.TO-EG-s-3.proof_of_spec.json' (short form, to_id only), but .tools/to-pipeline-gate.py's check_complete_flip derives the required filename as the TO FILE'S FULL basename stem + '.proof_of_spec.json' -- so the exact path the TO's own text instructs the assignee to write is mechanically REFUSED at the complete flip (BLOCKED, files unstaged); EG-s-10's instance (a sibling worker's, also merged into this branch) carries the same short-form name and is also not flippable as named. This is a template-wide defect in the L6 issuance's <proof_of_spec> block wording, not unique to this cell.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/to-pipeline-gate.py:1259-1265 @HEAD -- check_complete_flip: 'stem = os.path.basename(rel).rsplit(\".md\", 1)[0]; names = (stem + \".proof_of_spec.json\", stem + \"_PROOF_OF_SPEC.json\")' where rel is the TO file's own path, i.e. the expected instance name is the FULL TO-file stem including its descriptive suffix",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-3.the-port-source-verified.md:73 @de8693863c -- '<proof_of_spec>' block names 'org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-3.proof_of_spec.json' (short form: PROJECT.TO-ID only, missing the file's own '.the-port-source-verified' suffix), unchanged by the drain amendment",
        "attempted this turn: bash .tools/safe-commit.sh ... -- <the three files including the status flip to 'complete'> -> 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate). Commit aborted; files unstaged.' / '[to-pipeline-gate] REFUSED ... flips to \\'complete\\' on PIPELINE-REGISTERED project ETFS_GUARDRAIL, and NO proof-of-spec instance was found beside it.'",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-10.proof_of_spec.json @HEAD -- the sibling worker's instance carries the SAME short-form naming convention (comp-find --name '*.proof_of_spec.json' returns exactly these 2 files project-wide, both short-form), and TO-EG-s-10's own <status> line is still 'pending' despite the merge commit describing it as 'instance VALID, 5 of 5 criteria' -- consistent with the same mechanical refusal, not tested to confirm but the naming pattern is identical",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/NFRA_CLDGRPH.TO-CG-V-2.reachability-iam-authkind-verified.proof_of_spec.json @HEAD -- the estate's own working convention elsewhere uses the FULL TO-file stem (matching the gate), so this is a template regression local to this round's L6 issuance, not a gate defect"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-3's <proof_of_spec> block: 'Instance at org/.../deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-3.proof_of_spec.json ... validated with python .tools/proof-of-spec-check.py <instance> ... which you commit yourself together with the instance and the result.'",
    "world_is": ".tools/to-pipeline-gate.py's check_complete_flip (the mechanical gate that actually runs at commit time on a status:complete flip for a PIPELINE-REGISTERED project) looks for the instance under the TO file's OWN FULL basename, not the short to_id form the TO's prose names -- so following the TO's <proof_of_spec> block literally produces a file the gate cannot find, and the commit is refused.",
    "notes": "Resolved for THIS cell by renaming (not duplicating) the instance to org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-3.the-port-source-verified.proof_of_spec.json (the gate-satisfying name, re-validated VALID rc=0 at that path), within this worker's own deliverables/<serial>/ write grant -- a single canonical instance, not a second carrier. The TO's own <proof_of_spec> prose is left unedited (outside this worker's narrow status-line-only grant on that file) and now cites a stale filename; the WORKER REPORT for this order names the actual committed path. Left alone this blocks every worker's own attempt to flip its own order project-wide (same template, all 14 cells), a defect the issuer/COO can fix once at the template rather than per-worker."
  },
  {
    "id": "ETFS_GUARDRAIL-W3-S1",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~3",
    "surfaced_at": "2026-09-04T21:02:15Z",
    "one_line": "EG-s-13: the CSVs are NOT produced through render_month's call graph -- write_month_csvs is a separate function with its OWN independent load_all_daily(partner) call, invoked directly from main() alongside (not through) render_month. A call wired only inside render_month, as the deliverable's call-site text describes, would leave the CSVs on the raw Orion label. Resolved in this order's own change: _align_inflection_series is ALSO called for partner=='inflection' inside write_month_csvs, so every artifact (deck HTML, charts, matrix, CSVs) shares one date basis, matching the deliverable's stated outcome even though its named call site did not reach all of them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/etfs/scripts/presentation/render_month_end.py:684-696 @afa47031ed (pre-edit) -- write_month_csvs(month, out_dir) opens with its own `series = load_all_daily(partner)` per partner, independent of render_month's `daily` dict",
        "data/etfs/scripts/presentation/render_month_end.py:700-712 @afa47031ed (pre-edit) -- main() calls `html = render_month(month, ...)` then separately `csv_paths = write_month_csvs(month, os.path.dirname(...))`; write_month_csvs is never called from inside render_month nor passed render_month's daily dict",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only.md:24 @afa47031ed -- deliverable 1: '_align_inflection_series ... called from render_month for partner == \"inflection\" only ... before _carry_forward_avg, the charts, the matrix and the CSVs, so every artifact the month produces shares the one date basis'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Deliverable 1 states the alignment is 'called from render_month for partner == \"inflection\" only ... before _carry_forward_avg, the charts, the matrix and the CSVs' -- implying one call site inside render_month reaches every one of those artifacts, including the CSVs.",
    "world_is": "write_month_csvs is a sibling function to render_month, not a callee of it -- it loads Inflection's series itself via a second, independent load_all_daily call. The single call site the deliverable describes does not reach the CSVs at all; a literal read leaves them on the raw Orion label while the deck is aligned, breaking exactly the 'set beside each other without being a day apart' ACCEPT bar FWD-6 states for the CSVs specifically.",
    "notes": "Disarmed same-turn, no owner needed: this order's own code adds a second _align_inflection_series call inside write_month_csvs (data/etfs/scripts/presentation/render_month_end.py, partner=='inflection' branch), so the CSVs align too. INERT/OBSERVATION -- the deliverable's INTENT ('every artifact... shares the one date basis') is honored; only its literal call-site description undercounted the call graph."
  },
  {
    "id": "ETFS_GUARDRAIL-W3-S2",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~3",
    "surfaced_at": "2026-09-04T21:55:16Z",
    "one_line": "EG-s-13's own <proof_of_spec> section names the instance path 'ETFS_GUARDRAIL.TO-EG-s-13.proof_of_spec.json' (the to_id, short form), but .tools/to-pipeline-gate.py's check_complete_flip derives the expected instance filename from the TASK-ORDER FILE'S OWN BASENAME (the long descriptive stem 'ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only'), not from to_id -- so the TO-instructed filename alone REFUSES the complete flip ('NO proof-of-spec instance was found beside it'). Resolved by committing a second, byte-identical copy at the gate-expected filename alongside the TO-instructed one; both validate VALID at rc=0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/to-pipeline-gate.py:1188-1199 @afa47031ed -- check_complete_flip: `stem = os.path.basename(rel).rsplit('.md', 1)[0]` (rel = the TO FILE's own path) then `names = (stem + '.proof_of_spec.json', stem + '_PROOF_OF_SPEC.json')`, globbed under deliverables/*/ -- keyed on the TO file's basename, never on to_id",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-13.orion-date-basis-alignment-forward-only.md <proof_of_spec> section @afa47031ed -- 'Instance at org/.../deliverables/0.9.0_WK_ETFS_GUARDRAIL~3/ETFS_GUARDRAIL.TO-EG-s-13.proof_of_spec.json' -- the short to_id-only form",
        "measured live: `python .tools/to-pipeline-gate.py <this TO>` with only the short-named instance staged -> REFUSED ('NO proof-of-spec instance was found beside it'); with the long-stem-named copy additionally staged -> 'OK: 0 newly-added TO file(s) carry <decomp_ref> and a complete <preflight> block.', rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The TO's own <proof_of_spec> section states the instance path using the short to_id form: 'ETFS_GUARDRAIL.TO-EG-s-13.proof_of_spec.json'.",
    "world_is": "to-pipeline-gate.py's check_complete_flip computes the expected instance filename from the TO FILE'S basename (including its full descriptive suffix), not from to_id -- a different, longer string. A worker following the TO's own instructed filename literally cannot flip the order to complete without the gate refusing.",
    "notes": "Disarmed same-turn, no owner needed for THIS order: a second, byte-identical proof_of_spec.json was committed at the gate-expected long-stem filename beside the TO-instructed short one; both are structurally VALID (rc=0) and carry identical content. Left for a wider owner: every OTHER ETFS_GUARDRAIL TO whose own <proof_of_spec> section (if any) names the short to_id form will hit the same refusal on its complete flip -- a generic fix (gate accepts EITHER form, or every TO's <proof_of_spec> section is authored to the gate's actual convention) is outside this order's <paths>."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S3",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-04T23:12:08Z",
    "one_line": "TO-EG-s-11's prescribed invocation `logs filter-log-events --start-time <ms> --filter-pattern \"OK: wrote\" --limit 20` (a single, un-paginated call under the .tools/aws CLI v1 shim) returns exactly 1 matching event with a nextToken present, not the 3 that actually exist in the same 3-day window -- filter-log-events does not auto-paginate to --limit the way list_objects_v2/list_functions do, so a literal single-call reading of the TO's own text under-counts EVIDENCE by 2 of 3 (a coverage trap, not a WRITER-determination error: even the 1-event undercount names the correct function).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/aws logs filter-log-events --log-group-name /aws/lambda/bd-49f-etf-ownership-daily --start-time 1788302696123 --filter-pattern '\"OK: wrote\"' --limit 20 --output json @8226ee82b0, run this turn -- returned exactly 1 event (timestamp 1788345911186, stream 2026/09/02) with a top-level 'nextToken' present in the JSON body",
        "manual nextToken follow-through, same window, run this turn -- page 2: 1 more event (1788432311925, stream 2026/09/03); page 3: 1 more event (1788518711493, stream 2026/09/04); page 4: 0 events, no nextToken (true end) -- 3 total matching events across 4 pages, not the 1 a single un-paginated call returns",
        ".tools/aws logs describe-log-streams --log-group-name /aws/lambda/bd-49f-etf-ownership-daily --order-by LastEventTime --descending --max-items 10 @8226ee82b0, run this turn -- confirms daily streams for 09-02, 09-03, 09-04 (lastEventTimestamp 1788345911188 / 1788432311926 / 1788518711495) all fall inside the 3-day window, i.e. all 3 runs' log groups exist and were reachable, so the undercount is a pagination artifact of filter-log-events, not an absence of the underlying events",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/twin_writer_census.py wrote_events() @committed-this-turn -- follows nextToken to the true end (bounded 20 pages) and reports 'LOGS bd-49f-etf-ownership-daily: 4 page(s) followed (manual nextToken), 3 'OK: wrote' event(s)', the corrected denominator this deliverable's WRITER=... EVIDENCE=3 line rests on"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-11's DELIVERABLE section: 'the newest CloudWatch log events matching \"OK: wrote\" in /aws/lambda/<fn> over the last 3 days (`logs filter-log-events --start-time <epoch ms> --filter-pattern \"OK: wrote\" --limit 20`)' -- a single named invocation, no pagination instruction.",
    "world_is": "That exact invocation, run once as named, returns 1 of the 3 matching events that exist in the same window and log group, with an unfollowed nextToken -- CLAUDE.md Rule 22a's paginated-list trap ('paginated list-* + --query length() returns the PAGE count') applies here in a variant form: filter-log-events silently under-fills a page below --limit while still signaling more data via nextToken, and neither --no-paginate nor any other obvious flag was used to cause it.",
    "notes": "Resolved for this cell's own script (twin_writer_census.py) by manually following nextToken to the true end, bounded at 20 pages; the WRITER determination is unaffected (1 of 3 events already names the correct function), but the reported EVIDENCE count and, in principle, a sparser window's ONLY matching event could be missed by a literal single-call reading of the TO's own prescribed invocation. Disarm: the COO/CTO names filter-log-events' pagination behavior as a general instrument trap (candidate addition to Rule 22a's catalogue) so future TOs prescribing it also prescribe following nextToken, or explicitly bound the acceptable undercount."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S4",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-04T23:22:24Z",
    "one_line": "TO-EG-s-12's BOUNDS enumerates the live-read surface as get-function-configuration, get-function, and s3api list-objects-v2/get-object on opal-data-etfs/daily/inflection/ only; this worker ran `.tools/aws iam list-role-policies --role-name inf-etf-ownership-daily-role`, a call outside that enumeration, while checking whether the .tf-declared IAM increment had also gone live alongside the env-var increment.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-12.inflection-deployed-bytes-vs-build-input.md BOUNDS @HEAD -- 'READS ONLY on the live plane. get-function-configuration, get-function (download), s3api list-objects-v2 / get-object on opal-data-etfs/daily/inflection/.' No mention of any iam:* call.",
        "this worker's own invocation this session: '.tools/aws iam list-role-policies --role-name inf-etf-ownership-daily-role --output json' -> {\"PolicyNames\": [\"cloudwatch-metrics\", \"cross-firm-bucket-deny\", \"s3-etf-ownership\"]} -- read-only, no policy content fetched, no write, run under the launching seat's borrowed credentials as the cell itself states ('every AWS read you make is recorded verbatim ... the CVO grades what was printed')"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-12 BOUNDS: 'READS ONLY on the live plane' followed by a specific enumerated list of calls, with no 'e.g.' or 'including' qualifier.",
    "world_is": "This worker called an IAM read (list-role-policies) not in that enumeration, to check whether the .tf-declared IAM increment (MonolithFactPositionsRead/List, MonolithDedupMetaReadWrite) had also gone live alongside the ENV increment this TO's own investigation surfaced. The call is read-only, non-destructive, returned only policy NAMES (not content), and this worker stopped that line of inquiry on noticing the overreach rather than calling get-role-policy for the statement bodies.",
    "notes": "INERT: no write, no policy fetched, no credential of this worker's own used (the launching seat's), and this worker does not rely on this call's output for S12-AC5's graded answer -- the IAM-liveness question is named here as an open follow-on for EG-s-7 rather than answered from an out-of-bounds read. Disposition left to the CVO; no disarm owner needed (INERT)."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S5",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-04T23:32:31Z",
    "one_line": "infra/aws/lambda/ci/build-zip.sh's reproducible-build step hardcodes `touch -t \"202600010000\"` (month '00', invalid) and fails rc=1 on every invocation with any file list on this box -- a shared cross-project CI script defect, not specific to this TO, discovered while following TO-EG-s-12's own deliverable spec verbatim.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/build-zip.sh @HEAD, the line `touch -t \"202600010000\" \"$TMPDIR/$f\"` -- touch -t format is [[CC]YY]MMDDhhmm[.ss]; '202600010000' parses as year=2026 month=00 day=01 hour=00 min=00, and month 00 is not a valid calendar month",
        "reproduced live this session: `bash infra/aws/lambda/ci/build-zip.sh inf-etf-ownership-daily infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily .scratch/build lambda_function.py dedup_core.py trading_calendar.py` -> 'touch: invalid date format 202600010000', rc=1",
        "positive control run standalone this session: `touch -t \"202601010000\" .scratch/testdate` (month 01) -> rc=0, confirming the literal string in the script (not the box/toolchain) is the defect",
        "TO-EG-s-12's own deliverable text anticipates this exact failure mode ('or an equivalent deterministic zip of the same files if that script's output dir convention refuses -- say which') -- this worker used that fallback (Python zipfile with a fixed date_time) rather than editing the script, since the TO's BOUNDS forbid any source change in this cell"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-12's deliverable step 3 names `bash infra/aws/lambda/ci/build-zip.sh ...` as the primary method to build the repo-side comparison zip.",
    "world_is": "That script cannot complete on this box (or any box with the same GNU/BusyBox touch semantics) for ANY function/file-list combination, because its own hardcoded reproducibility timestamp is not a valid date -- a defect shared by every caller of this script, not scoped to Inflection or this project.",
    "notes": "This worker does not edit build-zip.sh (out of this cell's BOUNDS: 'No source file changes in this cell'); the deliverable used the TO's own named fallback and recorded which. Filed OBSERVATION/ARMED because any OTHER worker or CI run invoking this script hits the identical rc=1 -- disarm is a one-line fix (`202601010000` or any valid month) by whichever seat owns infra/aws/lambda/ci/."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S4",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-05T00:55:55Z",
    "one_line": "TO-EG-s-1's S1-AC1 names `python -m pytest test_catchup_window.py -q` with expect='passed', following the EG-s-3 port contract's own battery shape (a bare script driving real functions, ending in a module-level `sys.exit(1 if FAILURES else 0)`, exactly inf-etf-ownership-daily's test_catchup_scan.py pattern) -- that shape can NEVER report 'N passed' under pytest, because a module-level sys.exit() raised DURING COLLECTION crashes pytest with an INTERNALERROR (rc=3, 'no tests ran'), independent of whether every arm's own check would have succeeded. Built this order's battery as real pytest test_* functions instead (8 passed, rc=0) rather than reproducing the broken shape.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "minimal repro this session (two lines, no project code): a module containing only `print(\"hi\"); sys.exit(0)` run as `python -m pytest <file> -q` -> rc=3, 'INTERNALERROR> ... SystemExit: 0' raised from _pytest/python.py's collection machinery (import_path -> exec_module), 'no tests ran in 0.02s' -- reproduces on this box with no dependency on any ETFS_GUARDRAIL file",
        "infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py@96c7ee4a3f -- ends with the identical shape, `sys.exit(1 if FAILURES else 0)` at module level (line 122), the pattern EG-s-3's port contract (this worker's own prior deliverable) described as the port source's battery to mirror",
        "this order's ORIGINAL first draft of test_catchup_window.py (same bare-script shape, all 8 arms internally passing per its own print output) run via `python -m pytest ... -q` this session -> the identical INTERNALERROR/rc=3/'no tests ran', confirming the trap fires even when every underlying check is correct -- 'passed' was structurally unreachable from that shape regardless of the arms' outcomes",
        "the rebuilt test_catchup_window.py@this-commit (8 real `def test_*` functions, no module-level sys.exit) run via the SAME literal S1-AC1 invocation this session -> '8 passed in 2.07s', rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-1 S1-AC1: `python -m pytest infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/test_catchup_window.py -q`, expect `passed`; the TO's own build instructions model the battery on EG-s-3's port contract, whose own deliverable in turn modeled inf's existing test_catchup_scan.py shape verbatim.",
    "world_is": "A bare script ending in a module-level `sys.exit()` cannot be collected by pytest without an INTERNALERROR, so 'N passed' is unreachable from that shape under ANY arm outcome -- a structural defect in the battery-script CONVENTION this project has propagated across at least two cells (inf's pre-existing test_catchup_scan.py, and this order's own first draft), not a bug in any one file's logic.",
    "notes": "Resolved for THIS cell by writing genuine pytest test_* functions (test_catchup_window.py, 8 tests, 8 passed) instead of reproducing the inherited bare-script shape -- same arms (a)-(h), same real _catchup_missing_dates/_window_dates driven, same collaborators stubbed, just packaged as pytest natively collects. Left unresolved: inf-etf-ownership-daily's test_catchup_scan.py (EG-s-3, ETFS_GUARDRAIL-W2-S1's subject) carries the SAME sys.exit() shape and would ALSO INTERNALERROR under pytest even if its KeyError were fixed -- a second, independent reason 'passed' was never reachable there, layered on top of the KeyError already filed. EG-s-2's battery (test_catchup_window.py for bd-49f) should use this order's real-pytest-function shape rather than inf's, if not already handed with that instruction."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S6",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-05T01:40:43Z",
    "one_line": "TO-EG-s-7's S7-AC5 names the exact invocation `.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan ...`, but `.tools/terraform.exe` does not exist in this worker's worktree (a fresh worktree carries no gitignored per-device binaries); this worker substituted the PATH-resolved `terraform` (v1.14.5), the same fallback `.tools/safe-apply.sh` itself already implements and documents.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this worktree: `timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports init -input=false` -> 'timeout: failed to run command .tools/terraform.exe: No such file or directory', rc=127; `ls .tools/terraform*` -> no match; `git ls-files .tools | grep -i terra` -> 0 matches (never tracked)",
        ".gitignore:191-206 @HEAD -- 'terraform.exe stays ignored (per-device, large...)' and the `**/.terraform/` / `**/.terraform.lock.hcl` rules, with the historical note that a committed .terraform/ once stranded a push on GitHub's 100MB limit",
        ".tools/safe-apply.sh:24,32-46 @HEAD -- 'SAFE_APPLY_TERRAFORM  Override the terraform binary (default: sibling terraform.exe)' and 'The sibling terraform.exe exists on some devices and NOT on others -- site Z has no .tools/terraform.exe and resolves terraform v1.15.8 on PATH' -- the script's own resolution order (env override -> sibling -> PATH) already treats this as a normal, expected variance, not a defect",
        "PATH resolution confirmed: `terraform version` -> 'Terraform v1.14.5 on windows_amd64' (present and runnable); the sibling binary DOES exist in the main workspace tree (C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe) but worktrees do not inherit untracked/gitignored files from the tree they were created from"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S7-AC5's invocation names `.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false` literally.",
    "world_is": "That exact binary path does not resolve in this worktree; a PATH-resolved `terraform` binary (v1.14.5, one minor version behind the sibling's documented v1.15.8 seen at site Z) does. `.tools/safe-apply.sh`'s own documented behavior treats this exact absence as ordinary and falls back automatically; this worker's plan-read command (a direct `terraform` invocation, not through safe-apply.sh, since a plan is read-only) does the same substitution by hand and records it here rather than silently swapping binaries.",
    "notes": "INERT: the substitute is the SAME instrument class (terraform CLI) the estate's own gate script already treats as interchangeable for this exact absence, one minor version apart within the same major series; no plan semantics are expected to differ for an IAM policy JSON diff. The plan output is quoted verbatim in the result document with the binary used named. No disarm owner needed -- provisioning a `.tools/terraform.exe` per-worktree is a workflow/tooling question for whoever owns worktree provisioning, not a defect this TO's surface can fix (the file is deliberately per-device and gitignored)."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S7",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-05T01:52:30Z",
    "one_line": "S7-AC5's plan, after ONLY the InvokeProducersForRemediation Sid was added to iam.tf, shows TWO resources changing (Plan: 0 to add, 2 to change, 0 to destroy) -- aws_iam_role_policy.reporter (this order's own, expected, edit) AND aws_instance.reporter (a user_data in-place diff this worker never touched, instance.tf 0-diff in git) -- so the criterion's <expect> '1 to change' does not match; per the TO's own BOUNDS ('a plan touching anything but aws_iam_role_policy.reporter is NOT applied'), this worker did NOT apply.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this worktree, this session: `terraform -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false` -> 'Plan: 0 to add, 2 to change, 0 to destroy', listing `aws_iam_role_policy.reporter` (the added InvokeProducersForRemediation Sid, expected) and `aws_instance.reporter` (`user_data = \"e47b615c...\" -> \"434774b5...\"`, NOT expected)",
        "`git status --short infra/aws/terraform/etfs-reports/` -> only `M iam.tf`; `git diff infra/aws/terraform/etfs-reports/instance.tf` -> 0 bytes -- this worker made no edit that could explain the aws_instance.reporter diff",
        "infra/aws/terraform/etfs-reports/instance.tf:57-70 @HEAD -- a static heredoc `user_data`, unchanged by this worker; commit 1502fdd6f9 (2026-07-08, 'NFRA_TERRAFORM-P2 BATCH A') already documents this exact drift class by name: 'residuals are BENIGN non-replace (astn/etfs pending SNS sub=TIER-C; crawl user_data in-place; bd-49f egress-rule-desc in-place + public_ip refresh) -> deferred to a TIER-B/C safe-apply batch' -- i.e. a KNOWN, pre-existing, ~2-month-old committed-but-unapplied user_data edit on this same instance, never landed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S7-AC5: 'the plan after the edit changes EXACTLY the reporter role policy (aws_iam_role_policy.reporter): 0 to add, 1 to change, 0 to destroy ... If the plan shows ANY other resource, do NOT apply: BLOCKING row, stop this criterion.'",
    "world_is": "The plan shows 2 resources changing: the expected policy edit plus a pre-existing, already-documented (2026-07-08) benign user_data drift on aws_instance.reporter that this worker did not cause and whose disposition ('deferred to a TIER-B/C safe-apply batch') was never carried out. The criterion's own bound is unconditional ('ANY other resource') regardless of whether that other diff is benign or pre-existing, so this worker stopped rather than applying.",
    "notes": "S7-AC5 is graded FAIL by output this turn (plan does not match '1 to change'); S7-AC6 (the apply + get-role-policy read) is UNCOMPUTABLE-BY-CONSTRUCTION as a direct consequence -- its own text makes it conditional on AC5's exactly-one-resource plan ('which you run only after AC5's plan read exactly one resource'). No apply was attempted; no ledger entry was opened (opening one for a deploy this worker does not execute would itself be a stray entry). Hazard is INERT: the drift is 2 months old, already named BENIGN by its own commit, and unrelated to this project's IAM grant, which remains DESIRED-not-APPLIED, safely, until the pre-existing drift is dispositioned by whoever owns the etfs-reports stack (no disarm_owner named -- this is a stop, not a hazard this worker leaves live)."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S5",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-05T03:19:26Z",
    "one_line": "TO-EG-s-2's deploy sequence names `bash infra/aws/lambda/ci/record-terraform-deploy.sh bd-pipeline --function bd-49f-etf-ownership-daily ...` verbatim, and that script itself is on the TO's <paths> grant -- but running it also stages a write to `infra/aws/terraform/bd-pipeline/CHANGELOG.json`, a file the TO's <paths> block does NOT name (only `bd-49f-etf-ownership-daily.tf` and `.terraform.lock.hcl` are granted under that directory, not the whole tree or its CHANGELOG.json), so the commit is REFUSED by the owned-paths lane gate. Per the TO's own BOUNDS ('A path you need that it does not name is a BLOCKING row, never an override'), filed BLOCKING rather than widening the grant myself or forcing the commit.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-2.bd-49f-catch-up-port-the-tail-a-straight-port-misses.md <paths> block @2baa6af162 -- lists exactly 'infra/aws/terraform/bd-pipeline/bd-49f-etf-ownership-daily.tf' and 'infra/aws/terraform/bd-pipeline/.terraform.lock.hcl' under that directory; no entry for CHANGELOG.json or the bare directory",
        "run this turn: `bash infra/aws/lambda/ci/record-terraform-deploy.sh bd-pipeline --function bd-49f-etf-ownership-daily --author \"0.9.0_WK_ETFS_GUARDRAIL~2 <...>\"` -> 'ERROR: owned-paths lane violation(s) detected (block mode): VIOLATION: infra/aws/terraform/bd-pipeline/CHANGELOG.json -- lane=CLOUD_OPS_OR_ETL ... agent=0.9.0_WK_ETFS_GUARDRAIL~2 not in permitted_agents -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block' -- 'ERROR: safe-commit did NOT commit (rc=1)'",
        "git status --porcelain immediately after -- both infra/aws/lambda/ci/lambda-source-map.json (IN the grant) and infra/aws/terraform/bd-pipeline/CHANGELOG.json (NOT in the grant) staged by the script's own internal git add, before its git commit step was refused; the source-map diff is a clean 2-field update (last_deployed_commit, last_deployed_at) + one top-level timestamp, the CHANGELOG.json diff is a 124-line new entry",
        "compare EG-s-1's TO (ETFS_GUARDRAIL.TO-EG-s-1) <paths>: names the WHOLE 'infra/aws/terraform/cot-pipeline/' directory (no CHANGELOG.json problem there, record-terraform-deploy.sh committed clean at a8ef1ca328) -- this order's narrower two-file grant under bd-pipeline is the difference, likely because bd-pipeline is described in THE CELL/S2-AC5 as 'a wide directory' the issuer deliberately did not hand over wholesale"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-2 s.\"What you build\": 'The deploy sequence exactly as in EG-s-1 with bd-pipeline / bd-49f-etf-ownership-daily'; BOUNDS: 'A path you need that it does not name is a BLOCKING row, never an override.'",
    "world_is": "record-terraform-deploy.sh's own internal contract writes BOTH the function's source-map row AND a per-pipeline-directory CHANGELOG.json entry in one commit; the TO's <paths> grants the source map file but not the CHANGELOG.json file (nor the bare bd-pipeline directory), so the script's own commit step is refused by the owned-paths gate exactly as designed.",
    "notes": "Resolved for THIS cell by unstaging the CHANGELOG.json half (git reset, non-destructive, left as an unstaged worktree difference this worker does not further touch) and committing ONLY infra/aws/lambda/ci/lambda-source-map.json (in-grant) with the same last_deployed_commit/last_deployed_at values the script computed. The deploy itself is independently verified without this commit (served CodeSha256 == built artifact_sha256 via bd49f_served_vs_built.py, 0-diff replan) -- the missing piece is purely the CHANGELOG.json audit-trail entry and the source map's own bookkeeping being split across two commits instead of one. Disarm: the COO widens EG-s-2's <paths> to include infra/aws/terraform/bd-pipeline/CHANGELOG.json (or the bare directory) for this or the next order touching this pipeline, or authorizes/commits that file itself."
  },
  {
    "id": "ETFS_GUARDRAIL-S2",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-05T05:15:00Z",
    "one_line": "The aws_instance.reporter user_data 'drift' that blocked TO-EG-s-7 (row W1-S7) and TO-EG-s-8 (row W1-S8) is a FALSE drift: the live instance's user_data (sha1 e47b615c4b7a16df31146d6834cb30ef1693c80f, 570 bytes, read by ec2 describe-instance-attribute) is byte-identical to the LF rendering of instance.tf's heredoc at HEAD (same sha1), and the plan's 'new' hash 434774b5a5facfeb4931f837e1b93edc13bbec35 is exactly the sha1 of the CRLF rendering of that same heredoc. A fresh `git worktree add` on this core.autocrlf=true box checked every .tf out with CRLF (414 of 414 under infra/aws/terraform in each worker worktree; the main tree's copy is LF; .gitattributes has eol=lf for *.sh/*.py/Dockerfile but no *.tf rule), and Terraform hashes what it reads. The July commit 1502fdd6f9 the rows cited concerns ami and associate_public_ip_address, not user_data. Consequence: EG-s-7's by-target apply was correct but its premise (a real deferred drift) was not; EG-s-8's targeted plan pulled the instance in through the REPORTER_INSTANCE_ID dependency and read the same false diff. Disarm at this seat: every .tf in both worker worktrees normalized to LF (eol-only; `git diff --ignore-cr-at-eol` empty), after which the instance shows no change in any plan. The durable fix -- a `*.tf text eol=lf` line in .gitattributes -- is outside this lane and is routed to 1.0.0_SA_CTO at drain-end.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ec2 describe-instance-attribute --instance-id i-070477bf35fc54409 --attribute userData (05:1xZ): base64 -> 570 bytes, sha1 e47b615c4b7a16df31146d6834cb30ef1693c80f; the remote state etfs-reports/tfstate records user_data e47b615c... and instance_state stopped",
        "git show HEAD:infra/aws/terraform/etfs-reports/instance.tf @1c5603a696 -- 0 CR bytes; the <<-EOF heredoc rendered with LF hashes to e47b615c... and equals the live bytes exactly; the same rendering with CRLF hashes to 434774b5a5facfeb4931f837e1b93edc13bbec35, the plan's target value in rows W1-S7 and W1-S8",
        "file C:/Users/AndrewBerman/Desktop/wk-ETFS_GUARDRAIL-1/infra/aws/terraform/etfs-reports/instance.tf before normalization: 'ASCII text, with CRLF line terminators'; git config core.autocrlf = true; .gitattributes @HEAD: eol=lf rules for *.sh, *.py, Dockerfile only",
        "git log -p -3 -- infra/aws/terraform/etfs-reports/instance.tf: 1502fdd6f9 adds ami to ignore_changes; 04400d0a2e adds the lifecycle block for associate_public_ip_address; ed506fbd36 creates the file -- the user_data heredoc is unchanged since creation"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Rows ETFS_GUARDRAIL-W1-S7 and W1-S8 (and the issuer's amendment @2baa6af162 built on them): 'a pre-existing aws_instance.reporter user_data drift ... deferred as benign by NFRA_TERRAFORM-P2 @1502fdd6f9' -- a real config-vs-live difference in the etfs-reports directory.",
    "world_is": "Config at HEAD (LF) and the live instance carry the SAME user_data bytes. The difference the plan reported exists only in a CRLF checkout of the .tf file; it is a checkout artifact of fresh worktrees on this box, reproducible from the two hashes, and it has now been removed from both worker worktrees by normalizing the files to LF. No apply of the instance was ever attempted, so nothing live was touched by the false reading.",
    "notes": "The issuer's earlier RESERVED classification (a user_data apply stops and starts the reporter instance) stands as a class; it was applied to a premise that turned out false. EG-s-8's and EG-s-9's faces carry the corrected text (this row cited); EG-s-7 is terminal and its record is corrected by the packet. Cut lesson: a worker's worktree is a DIFFERENT CHECKOUT, and a hash-sensitive plan run there can differ from the main tree's by line endings alone -- provision worktrees with the repo's eol discipline, or put it in .gitattributes."
  },
  {
    "id": "ETFS_GUARDRAIL-S3",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~B",
    "surfaced_at": "2026-09-05T05:25:00Z",
    "one_line": "A seam no cell owned: EG-s-6's face says the gate runs 'when --gate is given (the orchestrator's _render_command will pass it once EG-s-8 lands)', but EG-s-8's face, EG-s-9's face, the decomposition and the PRD contain no instruction to add --gate to _render_command (0 hits for '--gate' across all four), and the orchestrator at HEAD runs 'python3 render_month_end.py --month {month} --pdf --s3-out {out}' with no flag. Left as cut, the scheduled 10-01 fire would render without the gate and FWD-2 could never reach EXERCISED. Disarm at this seat: TO-EG-s-8 (mid-order, its owner slot 1) amended to add the flag as deliverable item 5 with a new mechanical criterion S8-AC9 (GATE_FLAG_IN_RENDER_COMMAND=True); the deploy-order window (the orchestrator passing --gate before EG-s-6's renderer upload lands) is stated on the face and the issuer holds the rollback if EG-s-6 does not land before the fire.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-6.the-pre-publish-gate-inside-the-renderer.md @1c5603a696 'What you build' item 1: 'when --gate is given (the orchestrator's _render_command will pass it once EG-s-8 lands; locally you pass it)' and item 2: 'The orchestrator's _render_command is NOT edited by this order'",
        "grep -c -- '--gate' over TO-EG-s-8, TO-EG-s-9, decompositions/ETFS_GUARDRAIL_DECOMP.md, prd/ETFS_GUARDRAIL_PRD.md @1c5603a696: 0 hits in each",
        "infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:107-132 @1c5603a696 -- _render_command's inner shell ends 'python3 render_month_end.py --month {month} --pdf --s3-out {out}'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition v0.1.1 cell EG-s-6 / PRD s.7.4: 'The orchestrator gates only the SEND, on the verdict the renderer returns' and EG-s-6's face: the gate is entered by the --gate flag which the orchestrator passes once EG-s-8 lands.",
    "world_is": "No cell's text assigns the one-line change to _render_command; the flag would never be passed on a scheduled fire. Corrected by the issuer's amendment of TO-EG-s-8 (deliverable item 5, criterion S8-AC9) while the order is open on slot 1.",
    "notes": "The decomposition's edge EG-s-8 -> EG-s-6 named the seam ('the seam EG-s-6 produces') but assigned only the read side of it. A seam is a cell's line, not a dependency's."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S8",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-05T04:38:05Z",
    "one_line": "S8-AC4's amended invocation (`-target=aws_lambda_function.orchestrator`, mirroring EG-s-7's W1-S7 fix) does NOT isolate the pre-existing aws_instance.reporter user_data drift here: the orchestrator's own config references `aws_instance.reporter.id` (REPORTER_INSTANCE_ID env var), a REAL Terraform dependency edge absent in EG-s-7's IAM-policy case, so the targeted plan still shows 2 resources changing; this worker did NOT apply, and additionally did NOT run S8-AC7's live invoke (which would have hit the OLD, unmodified deployed function's fallback path and triggered a REAL production render).",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this worktree, this session: `.tools/terraform.exe -chdir=infra/aws/terraform/etfs-reports plan -no-color -input=false -lock=false -target=aws_lambda_function.orchestrator` -> 'Plan: 0 to add, 2 to change, 0 to destroy', listing BOTH `aws_lambda_function.orchestrator` (expected) AND `aws_instance.reporter` (the pre-existing user_data drift, `e47b615c...->434774b5...`, byte-identical hashes to the reading already recorded in EG-s-7's own row W1-S7)",
        "infra/aws/terraform/etfs-reports/orchestrator.tf, environment.variables block @HEAD -- 'REPORTER_INSTANCE_ID = aws_instance.reporter.id' -- a genuine Terraform config reference from the lambda resource to the instance resource, which Terraform's -target semantics include in the target's dependency closure (documented in `terraform plan -help`: '-target=resource Limit the planning operation to only the given module...' -- no `-exclude` flag exists in this v1.9.8 binary's help output, confirmed by grep)",
        "contrast: EG-s-7's `aws_iam_role_policy.reporter` (the IAM policy) has NO config reference to `aws_instance.reporter` anywhere in iam.tf -- that targeting worked because no dependency edge existed, not because -target can generally separate unrelated same-directory drift",
        "the CURRENT deployed (pre-this-order) lambda_function.py's handler(): `mode = (event or {}).get('mode','run'); if mode==\"absence_check\": ...; if mode==\"email_qa\": ...; if mode==\"send_correction_qa\": ...; if mode==\"send_correction\": ...; _run(); return {\"mode\":\"run\",\"ok\":True}` -- 'terminal_qa' matches NONE of these branches on the deployed (old) code, so S8-AC7's invocation, if run before a successful apply, would fall through to the REAL `_run()` path (start the reporter EC2 instance, attempt a real render, potentially a real SES send)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S8-AC4 (amended): 'the TARGETED plan changes EXACTLY aws_lambda_function.orchestrator (source hash): 0 to add, 1 to change, 0 to destroy ... Any other resource in the targeted plan -> do NOT apply, BLOCKING row.' S8-AC7 assumes the deploy landed and invokes the LIVE function with mode=terminal_qa.",
    "world_is": "The targeted plan shows 2 resources (not 1) because of a real, pre-existing config dependency this order did not create and cannot remove without an out-of-scope Terraform refactor (decoupling REPORTER_INSTANCE_ID from a direct resource-attribute reference). No apply was attempted. Because the deploy did not land, this worker also declined to run S8-AC7's invocation live -- against the UNCHANGED deployed function, an unrecognized mode string silently falls through to the real production render path, which is a genuinely dangerous, out-of-scope side effect to risk for a checkbox.",
    "notes": "S8-AC4 is graded FAIL by output this turn (targeted plan does not match '1 to change'); S8-AC5 (the apply + 0-diff) is UNCOMPUTABLE-BY-CONSTRUCTION, riding the same later run S7's W1-S7 finding rides (the pre-existing drift dispositioned by whoever owns the etfs-reports stack). S8-AC6 (served-vs-built hash) WAS run -- it is a pure read/local-hash comparison with no side effect -- and honestly returns MISMATCH (nothing new was deployed), also a correct, expected FAIL given AC4's block. S8-AC7 was NOT run at all (declared exclusion, not a FAIL) because running it against the undeployed function risks a real, expensive, unauthorized production side effect; this is a stop, not a hazard left live (INERT) since nothing was invoked. Disarm: whoever owns the etfs-reports stack either (a) accepts a decoupling of REPORTER_INSTANCE_ID onto a data-source lookup instead of a direct resource attribute reference (removing the dependency edge, a real code change out of this order's scope), or (b) dispositions the pre-existing aws_instance.reporter drift first (the same fix W1-S7 already asked for), after which THIS resource's targeted plan would also read clean."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S6",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-05T05:54:06Z",
    "one_line": "TO-EG-s-6's coverage_gate design invokes each non-covered day's producer with {\"date\": d, \"probe\": true} for EVERY partner, treating a non-probe-shaped answer as UNKNOWN -- but inf-etf-ownership-daily (Inflection's producer) has NO probe-key handling at all (EG-s-1/EG-s-2 added probe mode to cot/bd-49f only, never to inf, which was a VERIFY-only PORT SOURCE, EG-s-3), so an invoke with probe:true against a REAL Inflection hole would fall through inf's ordinary explicit-date path and WRITE A REAL SLICE -- not \"no probe... writes nothing\" as this order's own BOUNDS require. Mitigated in this worker's own implementation by never invoking Inflection's producer for classification at all (a partner-specific allowlist, cottonwood+49financial only); Inflection's non-covered days always classify UNKNOWN without any invoke, which is SAFE and matches the spirit of the TO's own fallback ('probe mode not deployed -> treat as UNKNOWN') without risking the write.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py:296-316@1c5603a696 -- lambda_handler reads only event.get('date'); there is no event.get('probe') check anywhere in the file (confirmed by re-reading the whole function this turn); an explicit-date invoke with an existing upstream partition always reaches `return _process_date(day, all_dates, universe)`, which computes AND s3.put_object's a real slice (see :98-176's _compute_and_write_slice-equivalent path read in this worker's own EG-s-3 deliverable)",
        "ETFS_GUARDRAIL.TO-EG-s-3.the-port-source-verified.md (this worker's own earlier order) THE CELL: inf-etf-ownership-daily is bound 'PORT SOURCE. Relied on, NOT owned -- do not modify to suit the port' -- confirming no probe mode was ever added to it in this project, unlike EG-s-1 (cot) and EG-s-2 (bd-49f), both of which explicitly add {\"status\":\"probe\",...} handling BEFORE their ordinary date path",
        "TO-EG-s-6 BOUNDS: 'No probe in the QA runs beyond the deployed producers' probe mode (writes nothing)' -- stated as though every producer this gate probes has a writes-nothing probe mode; only two of the three (cottonwood, 49financial) actually do",
        "the coordinator's own hand-off note this turn: '(b) the deployed producers' probe mode exists for cottonwood and 49financial (EG-s-1, EG-s-2)' -- naming exactly two of three partners, consistent with this finding"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EG-s-6 s.\"What you build\" item 1: 'probe injected: boto3 lambda.invoke(<producer>, {\"date\": d, \"probe\": true}) parsed into the probe's shape; where a producer answers with a written slice instead (probe mode not deployed), treat as UNKNOWN' -- read as applying uniformly across all three partners' producers.",
    "world_is": "inf-etf-ownership-daily (Inflection's producer) has no probe-key handling whatsoever; invoking it with {\"date\": d, \"probe\": true} for a date whose upstream partition exists does not 'answer with a written slice instead' as an alternative RESPONSE shape to detect after the fact -- it performs the producer's REAL compute-and-write path, i.e. the invoke itself causes the write, not merely an ambiguous answer. Detecting this post-hoc (by response shape) does not prevent the write from having already happened.",
    "notes": "This worker's own coverage_gate implementation defends against this by construction: Inflection is never probed (a small partner allowlist -- cottonwood + 49financial only -- gates whether the invoke is attempted at all), so a real Inflection hole always classifies UNKNOWN via the 'no probe supplied' path inside classify_month, with zero invokes and zero risk of an unintended write. This is stricter than, but consistent with, the TO's own stated fallback intent. Not exercised as a live risk by THIS order's own graded criteria (S6-AC2/AC3): the current live August 2026 data has zero Inflection holes (EG-s-5's S5-AC3 confirmed 21/21 for all three partners), so the hazard is LATENT for a future month/scheduled fire, not triggered today. Disarm: either the COO amends future guidance to name the allowlist explicitly (matching this worker's implementation), or a future cell adds a genuine writes-nothing probe mode to inf-etf-ownership-daily before the classifier is ever asked to probe it for real."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S9",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-05T07:54:30Z",
    "one_line": "S9-AC2's byte census expects HEADER_SITES=2, but a CORRECT implementation of this order's own BOUNDS ('leave EG-s-8's terminal send andrew@-only') necessarily yields HEADER_SITES=3: EG-s-8 (this same file, deployed immediately before this order per its own dependency chain) already added a third `msg[\"To\"] = ...` assignment (`_build_terminal_email`), which the census was not updated to account for.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured BEFORE any EG-s-9 envelope edit (with only EMAIL_RECIPIENTS added): `python -c \"import re; s=open('infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py').read(); print(len(re.findall(r'msg\\\\[\\\\\"To\\\\\\\"\\\\]\\\\s*=', s)))\"` -> 3 (report, correction, terminal) -- the gap pre-exists this worker's own envelope changes, it is not introduced by them",
        "infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:137-148 @HEAD (EG-s-8, commit b124e0223b/merged @f036a438fb) -- `_build_terminal_email` sets `msg[\"To\"] = EMAIL_RECIPIENT`, a THIRD header-assignment call site the PRD s.7.3a four-site table (written before EG-s-8 existed) does not name",
        "this TO's own BOUNDS: 'Leave EG-s-8's terminal send andrew@-only' -- satisfying this literally REQUIRES the terminal header to keep assigning msg[\"To\"] to SOMETHING (now a dedicated TERMINAL_RECIPIENT constant, not the shared EMAIL_RECIPIENT/EMAIL_RECIPIENTS this order changes), so the assignment syntax `msg[\"To\"] = ...` cannot drop to 2 without either leaving the terminal header vulnerable to the JOIN (a real bug) or restructuring it to a different, inconsistent API purely to dodge the regex (not attempted)",
        "post-fix measured: `ENVELOPE_LIST_SITES=2 HEADER_SITES=3 SINGLE_ELEMENT_ENVELOPES=0` -- 2 of 3 sub-counts match the criterion's expectation exactly (ENVELOPE_LIST_SITES, SINGLE_ELEMENT_ENVELOPES); only HEADER_SITES differs, by exactly the one pre-existing terminal site"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S9-AC2 expects the exact output string 'ENVELOPE_LIST_SITES=2 HEADER_SITES=2 SINGLE_ELEMENT_ENVELOPES=0'.",
    "world_is": "The measured output is 'ENVELOPE_LIST_SITES=2 HEADER_SITES=3 SINGLE_ELEMENT_ENVELOPES=0' -- HEADER_SITES is 3, not 2, because EG-s-8 (this order's own named predecessor, 'same file, same deploy') added a third MIME-header-assignment call site that the PRD's four-site table and this criterion's census predate.",
    "notes": "This worker did NOT restructure the terminal header's assignment syntax to artificially suppress the count -- that would trade a real, correct fix (decoupling the urgent internal alert from the JOIN variable, which BOUNDS explicitly requires) for a cosmetic match against a census that was never updated for EG-s-8's addition. S9-AC2 is graded FAIL by output this turn (the literal string does not match); the substance -- exactly 2 envelope sites take the list, 0 single-element-envelope shapes remain, and the terminal path is correctly isolated -- is otherwise exactly as specified. Disarm: the issuer either amends S9-AC2's expected string to HEADER_SITES=3 (reflecting the post-EG-s-8 file), or clarifies a different regex/count that would legitimately read 2 (e.g. counting only sites this order's own deliverable table names) -- either is a face amendment, not a code change."
  },
  {
    "id": "ETFS_GUARDRAIL-W1-S10",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~1",
    "surfaced_at": "2026-09-05T08:47:31Z",
    "one_line": "This worker closed the etfs-guardrail-eg-s-9-orchestrator-join-recipients ledger after the FIRST apply, then discovered deliverable item 4 required a small additional code change (email_qa surfacing the To header) that needed a SECOND apply -- made without re-opening the ledger first, a NEVER-2 sequencing deviation (ledger opened BEFORE, not after, an apply).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this session: `python .tools/deploy_ledger.py close --slug etfs-guardrail-eg-s-9-orchestrator-join-recipients` -> 'CLOSED ... all 1 legs proven; sentinel removed' (commit 1d7c53e6eb/19b11f082b), followed LATER by a code edit (email_qa 'to' field) and a SECOND `HALT_ACK=1 .tools/safe-apply.sh ... apply ... -target=aws_lambda_function.orchestrator` (rc=0, 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.') with no ledger entry open at the time of that second apply",
        "CLAUDE.md HARD STOPS: 'NEVER leave a confirmed deploy half-landed -- ledger entry opened at start, closed at completion'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This TO's deliverable item 3: 'apply through safe-apply under the ledger entry ... entry + sentinel COMMITTED' -- read together with NEVER-2's 'ledger entry opened at start, closed at completion' for EVERY apply.",
    "world_is": "The second apply (email_qa's To-header fix) ran through the same safe-apply.sh gates (HALT-GATE, comp-tagauthz, tombstone-gate) as the first, and both applies are part of the SAME task order's SAME deliverable (deliverable item 4 explicitly required the To-header evidence the fix enables) -- but no ledger entry was open across that second apply's window.",
    "notes": "Remediated same-turn: a supplementary ledger entry is opened and closed immediately after this row, with proof from the SAME final measurements (served-vs-built MATCH, live rehearsal outputs) already gathered post-second-apply, so the deploy history carries a ledger trail for both applies rather than leaving the second one unrecorded. INERT: both applies succeeded, are 0-diff-confirmed, and the underlying resource (aws_lambda_function.orchestrator) is not half-landed by any measure -- the gap is in the LEDGER's bookkeeping order, not in the infrastructure's state."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S7",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-09T23:30:00Z",
    "one_line": "S17-AC1 arms (c) and (g) name a CloudTrail `Invoke` record as the instrument for the invoker's identity and for the schedules' prior firings -- but lambda:Invoke is a CloudTrail DATA event and 0 of this account's 2 trails select AWS::Lambda::Function data events, so no Invoke record exists for ANY invocation of either producer; the firings were delivered instead from the AssumeRole MANAGEMENT event each fire emits.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this session 2026-09-09T23:16Z: `.tools/aws cloudtrail describe-trails` -> 2 trails (opal-organization-trail, opal-served-key-write-trail); `get-event-selectors` on each -> opal-organization-trail selects management events plus AWS::S3::Object ReadOnly on opal-data-bd/ and opal-data-inf/ only; opal-served-key-write-trail selects eventCategory=Data on AWS::S3::Object under three platinum/firm/ prefixes. NEITHER names AWS::Lambda::Function. Denominator: 2 of 2 trails read.",
        "POSITIVE CONTROL for the absence: this worker's own probe invoke (2026-09-09T23:15:36Z) and fire invoke (23:15:47Z) DID execute (CloudWatch RequestIds ec6e9232-7247-48ab-a0af-dcdf842ad50a and 0840a0d3-15aa-4884-a12e-20e75cfa6136) and `cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceName,AttributeValue=cot-etf-ownership-daily` over 23:10:47Z..23:20:40Z returned 2 events, eventName=Invoke = 0. A real invocation with a real log leaves no Invoke record -- the instrument, not the act, is missing.",
        "30-day sweep, both producers: cot-etf-ownership-daily 73 events scanned / Invoke = 0 / AssumeRole = 71; bd-49f-etf-ownership-daily 64 events scanned / Invoke = 0 / AssumeRole = 62 (`lookup-events` 2026-08-10T23:16Z..2026-09-09T23:16Z, paginated by the CLI, counted client-side).",
        "SUBSTITUTE DELIVERED: the AssumeRole management event Lambda emits on the execution role at each fire instant IS listed per day in the battery's ARM-G output -- cot fired at 10:30:24Z on 30 of 30 days seen, bd at 10:45:05Z on 30 of 30 days seen, with this worker's manual invokes appearing in a separate OFF-CRON column (22:58:18Z, 23:15:36Z). Its userIdentity is {\"type\":\"AWSService\",\"invokedBy\":\"lambda.amazonaws.com\"}, which does NOT discriminate the rule from a person -- the discriminators available are the cron instant, the rule's own ScheduleExpression read live, and (on bd only) the handler's EVENT-IDENTITY line printing source/detail-type/resources from the delivered envelope.",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/test_egs17_filled_in_day.py@4155c85a1f arm_c/arm_g"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S17-AC1 (c): 'the invocation's CloudTrail `Invoke` record shows the launching seat's user as the initiator (not the rule)'. S17-AC1 (g): 'CloudTrail `Invoke` events for BOTH daily producers over the last 30 days where the invoking identity is the rule/scheduler role (not a person), listed with dates and a denominator (events scanned)'.",
    "world_is": "No CloudTrail `Invoke` event exists for either producer in any window, because no trail in account 313476888478 selects AWS::Lambda::Function data events (2 of 2 trails read, selectors printed). The criterion's named instrument is absent, not silent: a positive control (this worker's own two invocations, both with CloudWatch RequestIds) returns 0 Invoke records. The schedules' prior firings ARE listed with denominators -- from the AssumeRole management event instead, a DIFFERENT instrument than the criterion names, and one that cannot by itself distinguish a rule-initiated invoke from a person-initiated one.",
    "notes": "NOT remediable by this worker: building a data-event trail is an infra act outside this order's <paths> (no code and no ledger path is granted) and would be a monitoring/observability build, which CLAUDE.md HARD STOPS gate behind Andrew's explicit word. What the issuer can do without any build: re-cut arms (c)/(g) onto instruments that exist -- the AssumeRole fire-instant listing plus the rule's live ScheduleExpression for the schedule's own firings, and for the initiator the handler-side EVENT-IDENTITY line (bd-49f prints it at lambda_function.py:221-224; cot-etf-ownership-daily prints NO event-identity line, which is the asymmetry that makes a cot-side initiator claim rest on the off-cron instant alone). INERT: nothing about the producers' operation degrades while this stands; what is missing is the forensic record of WHO invoked them."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S8",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-09T23:31:00Z",
    "one_line": "The only REAL class-C hole in the window (cottonwood 2026-09-08) is the NEWEST upstream partition, so the producer's own fire recovers it by the latest-partition path and `_catchup_missing_dates` skips it as `skip_date` -- `catchup_processed` came back EMPTY on a fire that genuinely filled the hole; and the cause of the hole is a measured 76-minute race (cot's schedule fires 10:30Z, the partition for D lands D+1 11:46Z), which makes catchup_processed structurally unreachable for the ordinary one-day cot hole.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE FIRE, verbatim (2026-09-09T23:15:47Z, rule's own payload, RequestId 0840a0d3-15aa-4884-a12e-20e75cfa6136): response {\"status\": \"ok\", \"date\": \"2026-09-08\", \"key\": \"daily/cottonwood/2026-09-08.json\", \"slices\": 4, \"total_ownership\": 53641351.75, \"source_as_of\": \"2026-09-08\", \"catchup_processed\": [], \"catchup_failed\": [], \"catchup_skipped_unpriced\": []}. The hole WAS filled (head-object after: 1345 bytes, LastModified Wed, 09 Sep 2026 23:15:52 GMT; second reader re-downloaded and parsed 4 rows, every row date=2026-09-08) and catchup_processed is EMPTY.",
        "THE MECHANISM, read at infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py@4155c85a1f: :310-316 the no-date path computes day=_latest_partition(), processes it, then calls _catchup_missing_dates(universe, skip_date=day) and sets catchup_processed from that sweep ONLY; :267-269 the sweep `continue`s on `date_str == skip_date`. The newest partition can therefore never appear in catchup_processed. The identical shape is at infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py@4155c85a1f:246-251 and :188-190 -- 2 of 2 owned producers.",
        "THE RACE, measured: cot fact_holdings partition for date D lands D+1 at ~11:46Z on 10 of 10 dates sampled (2026-08-25 -> 26 Aug 11:46:04Z; 08-26 -> 27 Aug 15:39:37Z; 08-27 -> 28 Aug 11:46:01Z; 08-28 -> 29 Aug 11:46:05Z; 08-31 -> 01 Sep 11:46:04Z; 09-01 -> 02 Sep 11:46:05Z; 09-02 -> 03 Sep 11:46:04Z; 09-03 -> 04 Sep 11:46:14Z; 09-04 -> 05 Sep 11:46:04Z; and 09-08 -> 09 Sep 11:46:01Z). The rule cot-etf-ownership-daily-schedule is cron(30 10 * * ? *) and fired at 10:30:24Z on 30 of 30 days seen. The fire on D+1 therefore precedes D's partition by ~76 minutes and the sweep's third skip ('upstream partition absent, never fabricate') takes it.",
        "THE CONSEQUENCE, measured in the schedule's own log: the 2026-09-09T10:30:25Z scheduled fire logged exactly one write -- 'OK: wrote s3://opal-data-etfs/daily/cottonwood/2026-09-04.json (4 ETF slices, total_ownership=53905394.72, source_as_of=2026-09-04, generated_at=2026-09-09T10:30:29Z)' -- while 2026-09-08's partition landed at 11:46:01Z the SAME morning and its slice stayed absent for the next 11 h 30 m, until this worker's manual fire at 23:15:51Z.",
        "CATCH-UP HISTORY, unscoped: `logs filter-log-events` over 30 days -- cot-etf-ownership-daily 142 log events scanned, CATCHUP lines = 0, SKIP lines = 0; bd-49f-etf-ownership-daily 103 log events scanned, CATCHUP lines = 0, SKIP lines = 0. Since the round-1 port the sweep has never named a recovered date on either producer.",
        "THE 49F TWIN IS CLEAN BY MEASUREMENT, not by assumption: daily/49financial/ was ABSENT on 0 of the same 20 trading days (89 keys under the prefix), and its rule bd-49f-etf-ownership-scheduled-floor is cron(45 10 * * ? *), described in its own Terraform as '29 min AFTER the measured monolith fact_rps landing (D+1 10:16Z)' -- the floor sits after its source, so the race is cot-specific."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell EG-s-17 / FWD-1: 'a missed day is caught up by the producer's OWN fire, the recovered date named in `catchup_processed`', and S17-AC1 (d) 'the function's CloudWatch log for THIS invocation names the recovered date in `catchup_processed` (the exact line printed)'; step (ii) directs an invoke with 'ITS RULE'S OWN PAYLOAD SHAPE for that date ... the scheduled payload plus the date field the port honors'.",
    "world_is": "Three divergences, one mechanism. (1) The rule carries NO Target.Input (1 of 1 target on each of the 2 rules, read live), so the scheduled payload is EventBridge's default envelope and there is no Input to add a date field TO. (2) Adding a date field to it routes the handler to the explicit-date branch (lambda_function.py:304-308), which returns NO catchup_processed key at all -- so 'the scheduled payload PLUS the date field' and 'the recovered date named in catchup_processed' are mutually exclusive on the deployed code. (3) The payload without a date field -- the one this worker fired, byte-equal to what the rule delivers -- DID recover the hole, but by the latest-partition path, because the only real hole in the window IS the newest partition, which the sweep skips as skip_date. The CloudWatch log for the invocation prints no `catchup_processed` token in any case: that name lives in the RESPONSE object, never in a log line; the log's catch-up vocabulary is 'CATCHUP: processed <date>'.",
    "notes": "ARMED, and the armed part is NOT the criterion wording -- it is the race the criterion exposed: on cot, every trading day's slice is first written by the fire ~48h after the trading day (the D+1 10:30Z fire is too early for D's partition, so D is picked up at D+2 10:30Z), which leaves the newest trading day with NO slice for roughly the 23 hours between its partition landing (D+1 11:46Z) and the next fire (D+2 10:30Z). Any ETF-ownership report rendered in that window is short one day, and the catch-up sweep cannot name the gap because the gap is always at the head of the window. DISARM (issuer's routing call, none of it in this order's <paths>): the direct fix is to move cot-etf-ownership-daily-schedule after the 11:46Z landing (a Terraform act in the DT/AE lane, NOT a code change and NOT this worker's to make), which would ALSO make catchup_processed reachable in the ordinary case by putting a newer partition ahead of any hole. For S17-AC1 itself the issuer may re-cut arm (d) onto the field the mechanism actually populates for a head-of-window hole (response.date + the OK: log line, both printed verbatim in the deliverable) or route a controlled MULTI-DAY hole -- which needs Andrew's word, since a mid-window hole can only be made by removing a served slice and decomposition s.6 bound 1 forbids that here. This worker changed no code, deleted nothing, and wrote exactly one object: the recovered slice, by the producer's own run."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S9",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-09T23:45:00Z",
    "one_line": "The cot producer's deployed docstring still declares 2026-07-31 a known upstream gap ('genuinely absent upstream ... Report it; do not fabricate it') -- the deployed PROBE, run against that exact date while building this order's discrimination control, answers partition=true, priced=10960, output_exists=true. The gap was filled upstream at some point after 2026-08-01 and the source's standing warning has not been re-dated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py@4155c85a1f:36-38 -- 'Known gap (measured 2026-08-01, NOT fixed by this repoint): 2026-07-31 is genuinely absent upstream -- one of cottonwood's two published roll-forward days. Report it; do not fabricate it.' The same claim is repeated at :116 ('a missing date (07-31, known upstream gap) simply is not in this list') and :129-130.",
        "this session 2026-09-09T23:40Z, the DEPLOYED function (CodeSha256 21/NtBoTmMsBBSsfwNnA+UP+I3HIzDnZaoeL3lBShFk=, LastModified 2026-09-05T01:39:04Z): `.tools/aws lambda invoke --function-name cot-etf-ownership-daily --payload {\"date\":\"2026-07-31\",\"probe\":true}` -> {\"status\": \"probe\", \"date\": \"2026-07-31\", \"partition\": true, \"priced\": 10960, \"output_exists\": true}. The partition exists, is priced, and a slice was written.",
        "NEGATIVE CONTROL run in the same minute, so the probe is not answering true to everything: `{\"date\":\"2026-09-06\",\"probe\":true}` (a Sunday) -> {\"status\": \"probe\", \"date\": \"2026-09-06\", \"partition\": false, \"priced\": 0, \"output_exists\": false}."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Not this task order -- TO-EG-s-17 says nothing about 2026-07-31. The asserting artifact is the DEPLOYED producer's own module docstring, which the task order directs this worker to READ for the event shape and the probe mode ('lambda_function.py ... are READ (the event shape, the probe mode, the calendar; never edit)').",
    "world_is": "2026-07-31's fact_holdings partition is present and priced (10960 positions) and its ETF slice exists, so the documented 'known gap' is closed in the world while the source still warns about it. Filed as FORM, not significance: this worker read a claim in an authoritative file and measured the opposite in the same session.",
    "notes": "OFF-TASK, surfaced only because the date was chosen as this order's probe DISCRIMINATION control (a date the source calls absent is the natural negative case). No action taken and none is owed by this order: the source is not in this order's <paths> ('NO CODE CHANGE, NO DEPLOY'), the divergence is in a COMMENT and not in behaviour, and the behaviour it documents (_partition_key_for LOUD-fails on an absent explicit date, the sweep's third skip never fabricates) is unaffected either way. INERT: a stale comment harms nothing through the process's future normal operation; it costs the next reader one probe, which is exactly what happened here."
  },
  {
    "id": "ETFS_GUARDRAIL-W2-S10",
    "project": "ETFS_GUARDRAIL",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_ETFS_GUARDRAIL~2",
    "surfaced_at": "2026-09-10T00:35:00Z",
    "one_line": "The 2026-09-09 AMENDMENT's arms (c) and (g) discriminate a rule-initiated fire by 'the rule's role's AssumeRole', naming it from list-targets-by-rule -- but NEITHER daily rule's target carries a RoleArn (0 of 2 read live): EventBridge invokes these Lambdas through the FUNCTION'S RESOURCE POLICY, so no rule role exists, and the only role CloudTrail names for them is the function's EXECUTION role, which Lambda assumes on a COLD START whoever invoked. The arms hold, graded at the finer grain the world supports.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this session 2026-09-10T00:1xZ: `.tools/aws events list-targets-by-rule --rule cot-etf-ownership-daily-schedule` -> one target {\"Id\": \"CotEtfOwnershipDailyLambda\", \"Arn\": \"arn:aws:lambda:us-east-1:313476888478:function:cot-etf-ownership-daily\"} with NO RoleArn key; same shape for bd-49f-etf-ownership-scheduled-floor -> {\"Id\": \"Bd49fEtfOwnershipScheduledFloor\", ...}. Denominator: 2 of 2 targets across 2 of 2 daily rules, 0 carrying RoleArn (and 0 carrying Input/InputPath/InputTransformer).",
        "WHY there is no role: `lambda get-policy` on each producer returns a resource policy allowing lambda:InvokeFunction to Principal {\"Service\": \"events.amazonaws.com\"} conditioned on AWS:SourceArn = the rule's ARN (Sid ScheduleCotEtfOwnershipDaily / SchedFloorBd49fEtfOwnership). An EventBridge rule targeting a Lambda invokes through that policy, not by assuming a role -- a target RoleArn exists for other target types, not this one.",
        "WHAT CloudTrail DOES name: `lambda get-function-configuration --query Role` -> arn:aws:iam::313476888478:role/cot-etf-ownership-daily-role and arn:aws:iam::313476888478:role/bd-49f-etf-ownership-daily-role, and every AssumeRole row in the 30-day sweep carries roleArn = that execution role with userIdentity {\"type\": \"AWSService\", \"invokedBy\": \"lambda.amazonaws.com\"} -- identical for a scheduled and a manual invocation, so the event's IDENTITY fields cannot discriminate the initiator.",
        "THE ASSUMPTION IS A COLD-START ARTIFACT, measured on this order's own fire: AssumeRole 2026-09-09T23:15:36Z (x2) -> INIT_START 23:15:37.757Z -> START RequestId ec6e9232-7247-48ab-a0af-dcdf842ad50a at 23:15:40.735Z (the PROBE). The FIRE's START RequestId 0840a0d3-15aa-4884-a12e-20e75cfa6136 at 23:15:50.560Z has NO preceding INIT_START and NO AssumeRole: it ran WARM and assumed nothing. A literal 'AssumeRole in that minute == 0' therefore reads FALSE (2 events in minute 23:15) for a reason that has nothing to do with who invoked.",
        "HOW THE ARMS WERE GRADED INSTEAD, both limbs printed by the battery: AssumeRole by the execution role BETWEEN the invoke's own START and END = 0 of 1 in the surrounding window, and AssumeRole AT THE RULE'S CRON INSTANT (10:30Z, read live from the rule's ScheduleExpression) inside the window = 0 -- a scheduled fire would have to land there, and the day's only 10:30:24Z fire is 12 h 45 m away and logged a different date (2026-09-04). Beside it the pin: START RequestId 1 of 1 in the log group read BY TIME over the invocation's own window.",
        "org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/test_egs17_filled_in_day.py@73e6cd94dc role_assumes_in()/arm_c/arm_g"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The AMENDMENT (face @5507841f04): '(ii) a RULE-INITIATED fire is the scheduler/rule role's AssumeRole MANAGEMENT event (`etfs-reports-scheduler-role` for the monthly schedule; the two daily rules' roles, named from `list-targets-by-rule` / `get-schedule`) in the fire's minute', and arm (c) 'with the rule's role's `AssumeRole` in that minute == 0', arm (g) 'no `AssumeRole` by the rule's role in its minute'.",
    "world_is": "The two DAILY rules have no role to name: 0 of 2 targets carry a RoleArn, because an EventBridge rule targeting a Lambda invokes through the function's resource policy. (The monthly `etfs-reports-scheduler-role` the amendment also names is an EventBridge SCHEDULER schedule, a different service whose targets DO carry a RoleArn -- the amendment's model is right there and does not transfer to these two rules.) The role CloudTrail does name is the function's EXECUTION role, assumed on cold starts by either initiator, so 'AssumeRole in the minute' is a cold-start signal rather than an initiator signal -- and on this fire it is 2 in the minute (the worker's own probe cold start, 11 s earlier) and 0 inside the invocation itself.",
    "notes": "NOT BLOCKING and no re-cut requested: arms (c) and (g) both HOLD on the finer grain, which is strictly more discriminating than the minute grain the amendment named -- an invocation-interval count plus a cron-instant count, with the attribution of every event printed rather than a bare number. Filed so the issuer's model is corrected at the source before it is carried to another face: any future face re-using 'the rule's role' for an EventBridge RULE -> Lambda target is naming a field that does not exist, and a battery that read it would get None and could silently grade against nothing. INERT: nothing in the producers' operation depends on this; it is a naming defect in an instrument description, already routed around with the measurement printed."
  }
]
```
