# Session close (Andrew-direct wind-down via CTO~Z 010436Z) — D0 T1 battery window + D8 standing-state handoff
**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE
**serial:** 0.4.0_DE_ClientPlatform~Z (lane ~Z, base-folder log per convention)
**window:** 2026-08-19 2140Z -> 2026-08-20 0107Z (delta since d8_liveedit_toa_store_api_tob_edit_surface_2056-2140Z.md; D8 build work is THAT log's record, not re-told here)

## Window work: D0 T1-4 broker batteries (COO~Z bounded run-and-report, dispatched 221111Z)

Ran the three batteries at org/mcp/ (landed @456d38d4c6): ALL rc=0, 22/22 PASS total.
- test_d0_t1_delivery_clocks.py rc=0 -- 11/11 (E1a-d clock separation QUEUED->SENT->EMITTED->READ,
  E2 negative control, E3a/b die-between-poll-and-drain RECOVERED, E4 no-spam, E5 ack-write-once,
  E6 UNKNOWN-PRE-T1 honesty, E7-MUTANT: pinned pre-T1 e7858adf52 loses the message -- poll 1,
  post-death poll 0, PERMANENTLY LOST -- the :474 window reproduced under control).
- test_d0_t1_listener_survival.py rc=0 -- 2/2 (FIXED spawn survives seat tree-kill; MUTANT old
  spawn dies to the same kill -- the kill proven able to kill).
- test_d0_t1_recipient_list.py rc=0 -- 9/9 (2 DELIVERED + 1 QUEUED of 3 with the dead seat NAMED,
  bogus serial REFUSED, legacy receipt shape kept, 3/3 Msg-ID stamping, LD-0424 body-cc replay
  copied NOBODY with positive control proving the query sees both seats when properly addressed).

TWO CORRECTIONS my report carried (COO~Z RAVC-4 ACCEPT 221614Z, zero rework, both verified at
their desk and ferried verbatim to MSTR~Z -> base COO):
1. FRAME: the batteries do NOT measure the running :7800 broker -- by design they spawn SCRATCH
   brokers from working-tree post-T1 bytes (@d547f109fe) + the pinned pre-T1 mutant. 22/22
   certifies TRUNK; the RUNNING broker stays pre-T1 and unmeasured. The :474 loss window's
   liveness in the running vintage class is evidenced by the PASSING mutant control, not a FAIL.
2. BOOT-VINTAGE, measured natively (Get-NetTCPConnection/Get-Process, never MSYS ps): pid 4152
   StartTime 2026-08-18T19:12:32Z -- a day earlier than the frame's "boot 19:11Z today";
   strengthens pre-T1. Verified unchanged post-run; no battery step approached the live broker
   (all kills scoped to scratch ports 7911/7912/7921/7922) -- the restart bound never tripped.

OPERATIONAL FACT standing for the morning board: on THIS device's live broker, any message to a
seat that dies between poll and drain is PERMANENTLY LOST until the reserved, announced restart
picks up d547f109fe. The restart decision is the morning board's, not any test run's.

## D8_LIVEEDIT standing state (Andrew-direct carriage item 1): site-Z legs COMPLETE

Commits: workspace 4c8fe9d006 (Lambda+TF+CF behaviors) + 13fd07d510 (source-map rider) +
303271b7ff (log + PROOF_OF_SPEC, VALID rc=0 positional 9/9); portal DEV ccda8711 (edit surface,
both families). Portal local DEV also carries reconcile merge 46f127eb (origin/DEV merged in;
5 pre-existing local commits preserved); workspace portal gitlink left UNCOMMITTED for MSTR
integration. TO status flip staged->pending left UNSTAGED in-tree for MSTR~Z's commit
(owned-paths). Dev-build proof (D8-1): PASS -- bun 1.3.14 / Vite 7.3.5 / 401ms / HTTP 200;
the envelope cell is priced.

### POST-APPLY BATTERY -- specified so the LAPTOP LANE CAN FIRE IT WITHOUT THIS SEAT
PRE-REQ (laptop, mechanical, sequence from my 2115Z ferry message; WDAC bound 08-20 07:00):
1. bash infra/aws/terraform/portal-content/build-and-upload.sh  (artifact + sha metadata +
   head-object verify)
2. safe-apply infra/aws/terraform/portal-content  (plan first; expect ~9 adds: table, role,
   policy, lambda, integration, 3 routes, permission)
3. safe-apply infra/aws/terraform/portal-auth  (CF ordered behaviors 4c/4d
   /api/scoped/portal-content{,/*} -- shared-infra)
4. 0-diff re-plan, tag portal-content-v1.0.0, push --follow-tags.
THEN the battery (any device -- HTTPS/IAM READS ONLY, no applies):
- D8-7 IAM (Rule 22a discipline): aws iam simulate-principal-policy
  --policy-source-arn arn:aws:iam::313476888478:role/opal-portal-content-api-role
  --action-names dynamodb:PutItem
  --resource-arns arn:aws:dynamodb:us-east-1:313476888478:table/opal-portal-content
  -- ONE action+resource per call; repeat for GetItem/DeleteItem/Scan; POSITIVE CONTROL as a
  SEPARATE invocation; a negative control against a foreign table ARN expects implicitDeny;
  action-name validity oracle is accessanalyzer validate-policy, never simulate.
- D8-4 403 ON THE API: PUT https://www.opalinvest.dev/api/scoped/portal-content/model_key_notes%23ust
  with a NON-employee token, body {"body":"x"} -> expect 403 {"error":"forbidden: Opal-internal
  editors only"} (the claim check must hold even where the UI hides the affordance).
- D8-3 persistence: internal-token PUT (200), then GET + portal render from a SECOND viewer
  session -> override present (same-session render proves caching, not persistence).
- D8-5 both call sites: pencil+save on the Benchmark heatmap modal AND the Positioning bars
  modal (ONE component -- both open ModelPortfolioModal); edit visible to a second session on
  both; a non-employee session shows NO affordance (dev-level screenshots of both identity
  directions already read PASS, in scratch + described in PROOF_OF_SPEC).
- D8-6 live half: view the edited surfaces on DEV (screenshot half already PASS).
- CLOSE-OUT: flip the UNCOMPUTABLE-BY-CONSTRUCTION rows (D8-3/4/7 + live halves of D8-5/6) to
  PASS with evidence in org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/
  D8_LIVEEDIT.TO-AB-SITEZ_PROOF_OF_SPEC.json and re-run
  python .tools/proof-of-spec-check.py <instance> "D8-1,...,D8-9" -> rc=0.

## The three ruled D8 questions the build sits on (carriage item 2; riders @a2b93df332)
1. Q1 EDITOR SET = ALL-INTERNAL: implemented as ONE server-side chokepoint
   (_is_internal, lambda_function.py -- firmId=='opal-capital' from the validated token context;
   client isInternal() gates only the affordance, advisory). An admin-only narrowing later is a
   one-predicate swap at that chokepoint, zero schema impact (D8_AUTH_SURFACE_RULING_20260819.md
   @e697f1450e).
2. Q2 MODEL-NOTES SCOPE = KEY NOTES PROSE ONLY: the modal's figures pane is untouched (six-field
   set stays ruled/live-config); only the Key Notes pane is wired to LiveEditableProse.
3. Q3 PRECEDENCE = STORE-WINS with BINDING VISIBILITY RIDERS: store override > workbook JSON
   block (pillars) > repo baseline; the losing path is VISIBLE -- every GET returns
   updated_by/updated_at, and the edit surface renders "Live override by X - date - masking the
   workbook/repo copy" beside an explicit reset control, at the exact surface where the content
   is read.

## MCP traffic (window): 3 significant received / 3 sent
Received: COO~Z D0 dispatch 221111Z; COO~Z RAVC-4 ACCEPT 221614Z (loop closed); CTO~Z
ANDREW-DIRECT wind-down 010436Z. Sent: ACK 221142Z; battery report 221445Z; log-committed
confirm to CTO~Z (follows this commit).

## Compiler Tools
No comp-tools run in THIS window -- one sentence why: the window was a dispatched test-suite
run (the three D0 batteries) plus native PowerShell process enumeration per the dispatch's own
instrument note; no code or infra was authored. The D8 build's comp runs (comp-routes,
comp-iam, comp-transform x4, comp-cache x2, comp-to, comp-find) are recorded in the 2056-2140Z
log and in PROOF_OF_SPEC compiler_tools.

## Blockers
None BLOCKED. D8 post-apply battery is GATED (not blocked) on the laptop apply -- evidence:
envelope law in the TO ("Site Z is not a TF-apply site") + WDAC bound 08-20 07:00; the gate
owner is the laptop lane via MSTR ferry (message 2115Z).

## Current State (zero-prior-context handoff)
- D8 sitez legs COMPLETE. Workspace SITEZ branch: 4c8fe9d006 + 13fd07d510 + 303271b7ff (mine,
  unpushed -- MSTR integrates). Portal DEV local: 46f127eb (merge) + ccda8711 (mine, unpushed).
  TO file org/tier0_exec/0.0.0_AB_MSTR/task_orders/D8_LIVEEDIT.TO-AB-SITEZ.* carries an
  UNSTAGED staged->pending flip awaiting MSTR~Z commit. Workspace gitlink 'portal' modified,
  uncommitted, deliberate.
- New AWS resources exist ONLY as committed TF (nothing applied): DDB opal-portal-content,
  role opal-portal-content-api-role, Lambda opal-portal-content-api, 3 APIGW routes on
  7k3ed8px20, CF behaviors 4c/4d. Live DDB census (35 tables) confirmed no name collision.
- PROOF_OF_SPEC at org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/
  D8_LIVEEDIT.TO-AB-SITEZ_PROOF_OF_SPEC.json: VALID rc=0, rows D8-1/2/8/9 PASS, D8-3/4/5/6/7
  UNCOMPUTABLE-BY-CONSTRUCTION pending the post-apply battery specified above.
- D0 T1: trunk broker certified 22/22 by scratch-plane batteries; running :7800 broker
  (pid 4152, up since 08-18T19:12:32Z) still pre-T1 -- restart reserved to the morning board.
- Local dev server on :5175 dies with this session/reboot -- morning respawn re-proves in
  seconds (bun run dev in portal/; the envelope cell is already priced PASS).

## Next Steps
1. [laptop AE lane via 0.0.0_AB_MSTR~Z ferry] Fire the apply sequence + post-apply battery
   exactly as specified above; any seat may close the proof rows -- the spec is self-contained.
2. [0.0.0_AB_MSTR~Z] Commit the TO status flip; integrate my 3 workspace commits + 2 portal
   commits (gitlink advance included) in your window.
3. [morning 0.4.0_DE_ClientPlatform~Z respawn] If the battery is still open: run it from here
   (HTTPS/IAM reads are sitez-legal); then flip proof rows + report acceptance to COO via ferry.
