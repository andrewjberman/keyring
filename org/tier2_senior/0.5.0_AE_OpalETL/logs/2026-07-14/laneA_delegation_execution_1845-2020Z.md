# 0.5.0_AE_OpalETL~A — Andrew-direct scoping + execution delegation, window 1845-2020Z

**archetype:** MIXED (IMPLEMENT + DEPLOY + VALIDATE + SCRIBE)

## Window summary

Fresh ~A lane (spawn 18:45:51Z, GA-3 clean, no orphan; Monitor bkbvrwuvw). Deconflicted with the
live base session (pid 26332) at startup; executed ONE bounded base handoff mid-window (C4
pre-flight IAM verify: 6/6 tonight-keys allowed, pos+neg controls, NoSuchBucketPolicy closes the
simulate blind layer — RAVC-4 CLOSED by base 19:04Z, rides its 22:00Z verdict report).

**ANDREW-DIRECT x2 (both verbatim-recorded + broadcast same turn, COO/CTO/MSTR ACKs banked):**
(1) ~18:52Z scope TAXSMA + Opal Ticket System, deliverable = implementation brief;
(2) ~19:30Z EXECUTION DELEGATION — sovereign authority, register-if-unregistered, run to
completion, fabric-quiet. Record: ANDREW_DIRECT_20260714_taxsma_ticket_system_scoping.md (+ addendum).

1. **Brief DELIVERED** `docs/briefs/ANDREW_BRIEF_20260714_taxsma_and_ticket_system.md` (293c062fb):
   PFMG_TAXSMA reconciled (registered 06-26 — Andrew's "check first" confirmed), TCKT designed
   against the AJ transcript (timestamped reqs) + live portal seams at vintage.
2. **TCKT_CENTER REGISTERED** (1ebafbd14): new TCKT macro (Pod 3), JSON + REGISTRY row; the two
   exec-lane files (MACRO_CODES, later EC2_MANIFEST) rode the AUDITED override citing the
   delegation (BLOCK->OVERRIDE lines in org/git-author-override-audit.log).
3. **PFMG_TAXSMA S0 CLOSED** (df17cbeb0): S0.1 NOT-A-LOOKUP (3 accounts absent from ULN 226,608
   lots + ACC 6,897 accounts, number+name axes, timing control on 2 pre-partition accounts);
   S0.3 attachment-name-primary rule (live feed 5 days incl. the 07-10 FOUR-send day; ground
   truth from Yang's own Short Sale folder: one final `SSAVAIL2 YYYYMMDD.ASC` per TRADE day).
4. **TAXSMA step-1 SHIPPED:** m365-gateway `list_email_attachments` (SAFE) +
   `save_email_attachment_to_site` (write_files ACTIVATED, upload-session for the 10-15MB .ASC,
   conflictBehavior=fail) — guard-wired fail-closed, 5-AC suite (AC4 env-gated), deployed
   633941502 via safe-ec2-deploy (on-box md5, service active, /health 200 = import-proven);
   `/taxsma-step1` runner skill (b239c4d1d). EXERCISED-pending the next m365 MCP reconnect.
5. **TCKT P0 SHIPPED:** `opal-tickets` + `opal-ticket-api` + 6 pure-add routes on the shared
   portal API — plan 14/0/0, safe-apply, 0-diff, 22a battery 5/5 + isolated pos/neg controls
   (both axes), e2e lifecycle exercised GREEN incl. 409 claim-race (ledger
   20260714T1958Z...CLOSED, tag ticket-center-v1.0.0). Portal page on DEV 11a638fb
   (/ticket-center, Tools nav, typecheck clean; pointer 16c4ee8a1). CF twin behaviors
   CTO-APPROVED 20:08Z -> 0.7.0 lands them (the one shared-infra item, routed via CTO's own
   collision channel).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-grep/comp-glob | ~10 calls (TAXSMA registry, S0 deliverables, gateway locate, APIGW route precedent, MACRO_CODES) | PASS — the registry hit reshaped the whole task (project already existed) |
| comp-routes behaviors | data-refresh serving path | PASS — pinned the CF-behavior gap; CTO's approval note cites the same instrument |
| comp-iam gaps | after authoring the new role | pre-existing estate flags only; NOT cited as sufficient — live 22a battery run instead (comp-iam fails GREEN on new resources) |
| comp-transform schema-check TicketCenter | new component | WARN types-not-colocated (live in api/endpoints/tickets.ts — accepted pattern) |
| comp-pulse (via safe-commit x9) | risk reflex | advisory HOLDs read each time; none applied to the pure-add diffs |
| aws iam simulate-principal-policy | 2 batteries (C4 handoff: 6+2 calls; TCKT: 5+3 calls) | all one-ARN-per-call, isolated controls; negatives implicitDeny both axes |
| rail-checked raw calls | logged inline per call | each carries its why; comp-which-rail.log has the trail |

Gap found: none new. The comp-freshness HUD nudge fired on an account-MEMBERSHIP s3 ls (not a
freshness question) — correctly overridden with a rail-checked marker, noting for the rail's
intent-classifier backlog.

## MCP traffic

Sent: 2x Andrew-direct broadcasts (x3 recipients each), deconflict + ACK + RAVC-3 report to base,
CF-behavior surface to CTO. Received + acted: base handoff + RAVC-4 close, CTO ACK x2 + CF
approval, COO ACK x2. Zero dispatches INTO the fabric (delegation honored; CTO's 0.7.0 dispatch
was his own).

## Current State (zero-prior-context)

Branch CLOUD pushed through 16c4ee8a1 + tag ticket-center-v1.0.0; portal DEV @ 11a638fb.
LIVE + verified: opal-ticket-api stack (e2e-exercised), gateway attachment tools (import-proven),
/taxsma-step1 skill. PENDING external: CF behaviors (0.7.0 confirms direct), m365 MCP reconnect
(first /taxsma-step1 live run + S0.3 name byte-confirm), step-2 feed answer (Andrew/Yang ops
request), Andrew's UI-platform call (TAXSMA steps 3/5 + Alyssa runner), TCKT P1-P3 phases.
Base 0.5.0's 22:00Z pipeline untouched throughout.

## Next Steps

1. [self/any-session, next m365 reconnect] first /taxsma-step1 live run -> byte-confirm S0.3
   names -> append confirmation to the S0 close doc.
2. [0.7.0 -> self] CF behaviors land -> exercise /ticket-center end-to-end through the edge.
3. [Andrew] one-word items in the final report: step-5 in/out of initial TAXSMA build; UI
   platform call; the Schwab CRS ops request for the 3 accounts; Alyssa write_files entitlement.
4. [self] TCKT P1 (sweeps + claim links) once the cutoff time is confirmed from the agreement.
5. [self] TAXSMA steps 3/5: generic write-file gateway tool + /taxsma-run skill, on a fresh
   Tax Lot date.
