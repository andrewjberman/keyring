# 0.7.0_AE_CloudOps -- session log 2026-08-20 13:34Z -> 15:55Z (morning re-form: D8 apply -> device-axis guard -> W6-PORT -> D7 write-path + re-pin -> freshguard-leg4 disposition -> both 41.8d credential holds discharged)
**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, DIAGNOSE, COORDINATE

## What happened

Morning re-form at Andrew's direction (his word at the MSTR terminal). /watcher found NO orphan, armed a
persistent Monitor (task b01sicwmy), registered, drained 11 queued messages; ~20 more arrived live over the
session and were acted-on same-turn. XXX.md startup clean (audit-archive rc=0, PATH 97/99 + exercise pass,
hooks wired). THREE laptop applies of the site-Z D-family + one re-pin, four deploy ledgers opened and CLOSED
in-session, zero stranded legs.

### 1. D8_LIVEEDIT laptop apply -- opal-portal-content store + API + CF behaviors (ledger CLOSED 6/6)
The laptop half of the site-Z D8 cert (@05689f222d). No drift: HEAD carried the exact certified vintage
(@4c8fe9d006 + @13fd07d510), tree clean. safe-apply portal-content 11/0/0 == staged plan, 0-diff; safe-apply
portal-auth 0/1/0 behavior-list insert ONLY (audited the full plan: +2 behaviors, 0 removes, 0 non-behavior
attrs -- the index-shift rendering is not a change); live CF read confirmed both /api/scoped/portal-content{,/*}
on EVTSA9VEHNZVH. Rule 22a CODE: downloaded the applied package, member sha256 BYTE-MATCH source (mutant
control differs); deployed CodeSha256 == artifact == source-map stamp (triple tie-out).
Battery LIVE through www.opalinvest.dev: D8-7 IAM simulate 4 SEPARATE invocations all allowed on the exact
table ARN + foreign-table implicitDeny + accessanalyzer 0 findings; D8-4 a VALID non-employee token got the
LAMBDA chokepoint 403 (discriminated from the authorizer 403 by minting with the pinned iss/aud the deployed
authorizer's bytes require -- a token without them dies earlier); D8-3 internal PUT->second-identity GET shows
the override + Q3 visibility fields, DELETE reset, residue count=0. Flipped D8-3/4/7 PASS, validator rc=0
(POD4 override audited per the cert's any-seat clause). L4 (tag push) rode MSTR's integrator window.

### 2. audit-archive-invoker DEVICE-CHAIN-PENDING guard (CTO ruling @4484d55608, landed ~1428Z, bar 1624Z)
The interim half of the device-axis fix: shared+tracked .baseline over untracked device-local subjects
manufactures ~18 false findings per cross-device mint. Wired authorise_device() into take_snapshot() to REFUSE
with the ruled outcome string until a per-device chain root with its own .baseline exists. ONE deviation beyond
CTO's minimal form (approved, "better than my minimal form"): wired the mint dest/pointer/age-recheck
PER-DEVICE in the SAME edit, so the guard cannot clear back into a shared-path poisoning write -- clearing the
guard and minting per-device are one event by construction. Exercised 4/4 as an exec-serial simulation (the
owner seat is lane-deferred upstream): E1 real mint-due refusal with the mint surface byte-identical
before/after; E2 sandbox per-device chain -> clears; E2b per-device age re-check; E3 unreadable-registry named
refusal. CTO verified at his seat, gate CLOSED 2h early.

### 3. OPAL_ANALYST.W6-PORT -- /query/v0 partner-query plumbing (ledger CLOSED 4/4, TO flipped complete by COO)
D6's laptop dependency under the sovereign D-family drive. C1 port: staged catalog -> gateway runtime
app/refs/DATA_CATALOG.yaml, FOUR named delta lines (header + version), else byte-identical. Built the endpoint
extending the /teams/poll bearer pattern (query_v0.py + server route + audit allowlist row + graphql_plumbing
package marker). Zero-mint EXERCISED (Andrew "zero-mint W6"): FIRM_PRINCIPALS empty, a valid external token ->
'unresolvable principal class -- deny by default'. C6 R1 size census found TWO certified catalog rows >2MB ->
CTO ruled the cap 2MB->4MB same hour (same authority) and made R1 standing at every port; R2 sliding-window-log
named. NEW portal-read IAM grant: measured ABSENT pre-apply (simulate implicitDeny + positive control), applied
scoped to json/*+platinum/* only, live-verified both directions. On-box battery 13/13 (S3->SSM, Rule 12) +
all deny classes + rate-trip at the exact window boundary + audit lake object. C10 (O-1 case) and C11 (O-2
capped call) honestly UNCOMPUTABLE-BY-CONSTRUCTION -- external acts with named owners/next-runs (validator
rc=0). Two deterministic self-caught defects en route: the gateway role had no portal read (spec's own fetch
leg needed it); deploy-to-ec2.sh failed 2x on an unretried health curl racing uvicorn's bind (fixed with the
same bounded-loop as its own S4 fix; service healthy throughout, journal-verified). And my FIRST O-1 send went
via the localhost broker to a SITE-Z seat -- structurally undeliverable; caught, re-sent on the SQS bus.

### 4. D7 TO-F half-(b) write-path apply + re-pin (two ledgers, both CLOSED)
Ticket-center authz matrix + POST /api/scoped/tickets/submit (site-Z author record @4bede18189). Plan was
EXACTLY the ferried pin (route + lambda code-triple, nothing else -- audited before apply); 0-diff; bytes
byte-match repo@HEAD. Exercise LIVE: D7F-5/6 client CREATE/LIST/METRICS 403 with principal_class named, D7F-4
requester_firm-in-body 400, D7F-3 FIRST PASS 201 -> DDB read-back (source=dashboard_form:49financial,
created_by=svc-ticket-form), SoD claim-by-A/complete-by-B 403 + assignee-complete 200. Then site Z re-pinned
@1fd9ef2750 (one field: submit 201 carries cutoff_et, D7F-11) -- the re-pin content was already in the shared
tree via integration, tree member sha matched the expected 4b7e1bbce31e4d34; applied 0/1/0, exercised
cutoff_et present-on-201/absent-on-deny.

### 5. freshguard-leg4 disposition (Andrew-item via MSTR 63015)
The 42d HELD-STALE was the FAIL-BY-DESIGN state wearing a drift signal. Re-dated the hold with a
FAIL-BY-DESIGN declaration (close path = the dormant CAS fix behind CTO GO-conditions, one being a MARKER_CAS_*
alarm under the 07-28 moratorium -> sovereign-shaped). SELF-CAUGHT: deploy_ledger.py hold REPLACES the Status
field wholesale, and my re-date silently deleted the 163-line canonical v4 criterion block from the entry AND
overwrote the gate-ref JSON -- caught by auditing my own commit's -165 delta, restored verbatim from
29f4f61ab2^ under a provenance header. Flagged the tool defect (append, don't replace) to the ledger owner.

### 6. BOTH 41.8d credential holds discharged (Andrew "exercise and close" via MSTR/COO)
- freshguard-leg5-v2: MATERIAL FINDING -- the hold's SUBJECT (parity-drift Lambda + both alarms) was DESTROYED
  34d ago @858554332d (my own commit, CTO GO), live-verified (zero parity alarms/freshness Lambdas). The
  deeper version of this morning's class: nobody re-checked whether the gate's subject still existed. Closed
  CANCELLED-BY-TEARDOWN; the honest divergence from Andrew's 'exercise and close' verbatim surfaced VISIBLY to
  MSTR, not silent. COO ratified in place under status-law authority (63231, appended to the entry). My
  mechanical close ran ahead of the status-law correction -- disclosed; COO ratified rather than redo.
- scty-premcp L4: the provisioned identity was a SECRET (opal/mcp/ms-ingest-token), not a user email --
  consistent with my 4th cached hash matching none of 94 candidate emails. Exercised: /ms/health {ok:true} +
  /ms/sites 200 + no-bearer 401. Held the raw-Graph-write per instinct; CVO REFUSED it (wrong plane +
  credential hazard) and named the discriminating read instead: the three legs pass identically on a full-scope
  gateway, so I read the DEPLOYED mint-site bytes via SSM (config.py:85 READ_ONLY_GRAPH_SCOPES all .Read*,
  token_broker _scopes_for_tier->acquire_token_silent) -- APPLIED plane, sha-attributed to the instance. Sent
  to CVO for same-turn L4 cert close.

## Current State (for a reader with zero context)
- **DELIVERED + CLOSED:** D8 (portal-content live, CF behaviors 4c/4d, ledger 6/6); W6-PORT (/query/v0 live on
  opal-gateway @7dda75128d, ledger 4/4, TO complete); D7 write-path (opal-ticket-api, tag v1.1.0, ledger 4/4)
  + re-pin (tag v1.1.1, cutoff_et, ledger 3/3). Device-axis guard live @47ba0d11a0.
- **DISCHARGED:** freshguard-leg4 (FAIL-BY-DESIGN declared + v4 block restored); freshguard-leg5-v2
  (CANCELLED-BY-TEARDOWN, COO-ratified); scty-premcp L4 (exercised, cert evidence at CVO).
- **OPEN, named owners:** W6-PORT C10 (OpalETL~Z's O-1 case/ACK, on SQS bus 6c03f2a2); C11 (O-2 capped call at
  next Bloomberg terminal login -- DAPI 8194 CLOSED, zero stale blp processes); scty L4 cert (CVO to close
  same-turn on the mint-site read).
- **STANDING RULE inherited (CTO~Z 2450-REVISED):** the catalog has ONE home (app/refs/DATA_CATALOG.yaml);
  no laptop hand-edits; emitter single-writer from v0.3.
- **Tags awaiting integrator push:** portal-content-v1.0.0 (already pushed by MSTR), ticket-center-v1.1.0,
  ticket-center-v1.1.1.
- **NEXT:** 1715Z emitter T-1 read -> one line into the MDPF feeder ledger (closes the 08-19 regression fully).

## Next Steps
- [0.7.0_AE_CloudOps] THU 08-20 17:15Z: emitter T-1 read -> feeder ledger line.
- [0.7.0_AE_CloudOps] When OpalETL~Z's O-1 case lands: re-run the on-box W6 battery (13->14) for C10 close.
- [0.7.0_AE_CloudOps / any seat] At next Bloomberg terminal login: one bloomberg_historical_data call with
  max_data_points=2 -> C11 O-2 close.
- [3.0.0_SA_CVO] close scty-premcp L4 on the mint-site read.
- [2.0.0_SA_COO] freshguard-leg5-v2 CANCELLED flip -- RATIFIED in place (63231); nothing further.
- [0.4.0_DE_ClientPlatform~Z] D8-5/6 render halves (browser); [0.5.0_AE_OpalETL~Z] O-1 battery case.

## Compiler Tools
| Tool | Target | Result |
|---|---|---|
| `verify-ec2.sh` | opal-gateway pre-deploy parity | Bare run returned VACUOUS 0-checked "all in sync" (Rule-16 jq-missing hazard, recorded); re-run with .tools/jq -> 27 checked, opal-gateway "drift" = exactly the 4 staged D6 commits this TO deploys |
| `comp-blast` | catalog_gate | NOT-FOUND w/ denominator (kuzu SERVED-STALE, refresh mutex timeout) -- expected for a new package; vintage warning honored, nothing quoted as live |
| `comp-find` | identity_scope / max_data_points / opal-gateway-role / parity_drift | Localized existing machinery (extend-not-rebuild), found max_data_points in the Bloomberg MCP (C11's true referent, 0 gateway hits), traced the freshness teardown |
| `aws iam simulate-principal-policy` | D8 table x5, gateway role x4, all isolated | Rule 22a: one resource per call, controls separate; every grant measured absent-then-applied or allow+foreign-deny |
| `deploy_ledger.py` | 4 ledgers open+close, 1 hold re-date, 2 cancel | All closed in-session; DEFECT FOUND: `hold` REPLACES the Status field wholesale (deleted a 163-line criterion block -- caught + restored, flagged to owner) |
| on-box batteries (SSM) + `proof-of-spec-check.py` | W6 13/13, D7 13/13, W6 instance C1-C11, D8 D8-1..9 | All rc=0; W6 exercised at 3 planes (staged/ported/deployed), identical; D7F-3 read back from DDB |
| `commit-gate/safe-commit/safe-apply/safe-ec2-deploy` | 15 commits, 4 TF applies, 3 EC2 deploy runs | All green; safe-ec2-deploy failed 2x on a wrapper health-curl race (fixed + committed, run 3 clean) |

**What worked:** the deployed/executing-bytes reads at every applied plane -- the D8 discriminated 403 (minting
with the authorizer's own pinned iss/aud), the W6 zero-mint EXERCISED via a valid external token, and CVO's
mint-site read for scty L4 all required going to the running bytes, not config or repo. Three self-caught
defects (the hold-replaces-Status delete, the localhost-vs-SQS misroute, the deploy health-curl race) were each
caught by checking my own output/delta rather than trusting a green.

**What failed:** `verify-ec2.sh` returned a VACUOUS 0-checked pass with bare jq missing (Rule 16) -- the
anti-correlated shape, "all in sync" over zero services. Caught because 0-checked is not a clean pass; re-ran
with the vendored jq resolvable.

**Gap found:** deploy_ledger.py `hold` is a DESTRUCTIVE Status-field write -- it overwrites load-bearing entry
content (a canonical criterion block, and the gate-ref JSON) rather than appending. Routed to the ledger owner
lane as a tool defect (append, don't replace); no comp-tool covers "what content lives in a ledger entry's
Status field" so the loss was only catchable by auditing the commit delta.
