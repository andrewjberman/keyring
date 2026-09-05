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
  }
]
```
