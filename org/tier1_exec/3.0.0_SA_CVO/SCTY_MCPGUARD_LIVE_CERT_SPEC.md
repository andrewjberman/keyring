# SCTY_MCPGUARD — Live-Cert Spec (CVO pre-stage, fire-on-deploy-land)

**Author:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Status:** PRE-STAGED (COO-ACCEPTED 193955Z, + Case 4 added) — deploy is HELD (0.7.0~A lane + CTO scope-collision ruling). Cert fires the instant COO cues "0.7.0~A deployed + on-box-verified."
**Deploy roster (COO-confirmed 193955Z):** `MASTER_ADMIN_EMAILS=andrew@opalinvest.com` · `WRITE_CAPABLE_EMAILS=alyssa@opalinvest.com` · all-else READ_ONLY. **Instrument = `create_draft` for ALL FOUR cases — guard-cert only, NO real outward send (COO explicit: do not fire one).**
**Cert gates:** the SCTY deploy-ledger close. **Role:** verifier-not-fixer — any failure = immediate COO flag + rollback trigger, NOT fix-forward.

## Grounded artifact-under-cert
Guard mechanism read 1:1 from build-lane source (`org/tier2_senior/0.5.0_AE_OpalETL/deliverables/scty/{guard,tier,destructive_ops}.py`) + landing-diff `docs/briefs/scty-mcpguard-landing-diff-20260701.md` (8de441c6b). Wiring lands in `tools._run()` (DIFF 3): resolve tier ONCE → `guard.enforce` → audit-with-tier.
- **Mutating surface = 5 send-class tools** (`destructive_ops.DESTRUCTIVE_OPS`): `create_draft` (WRITE_REVERSIBLE), `send_email`, `reply_email`, `send_chat_message`, `send_channel_message` (all IRREVERSIBLE_SEND). Everything else = SAFE (guard bypass). Unknown tool → fail-closed destructive.
- **Tier resolution** (`tier.resolve_tier`): unverified provider → READ_ONLY for everyone (root-of-trust); else exact-match `MASTER_ADMIN_EMAILS` → MASTER_ADMIN, exact-match `WRITE_CAPABLE_EMAILS` → STANDARD_EMPLOYEE, else → READ_ONLY.

## Cert instrument = `create_draft` (the SAFEST mutating probe)
`create_draft` is mutating (routes through the guard) but WRITE_REVERSIBLE — a draft, never an irreversible send. So if a deny ever fails-OPEN during the test, worst case is a deletable draft in a mailbox, **not** a sent message. Use it for all four cases (COO-confirmed: guard-cert only, no real send). (Do NOT use `send_email`/`send_chat_message` as the deny-case probe — a fail-open there is an irreversible real send.)

## Preconditions to confirm on the running gateway BEFORE exercising (structural sharp-test)
| # | Precondition | How | Fail meaning |
|---|---|---|---|
| P1 | Guard code is actually deployed | on-box `app/{guard,tier,destructive_ops}.py` present; `tools._run` has the `guard.enforce` wiring; `config.py` has the 3 SCTY vars; EC2_MANIFEST `deployed_commit` == the SCTY artifact sha | not-deployed → nothing to cert (current state: box @ 28ecbd838, pre-SCTY) |
| P2 | `IDENTITY_PROVIDER=alb_oidc` (verified) on box | on-box `.env`/config | if unverified → andrew@ fails-closed to READ_ONLY → Case 3 CANNOT pass |
| P3 | full roster on-box: `MASTER_ADMIN_EMAILS` includes `andrew@opalinvest.com` (Case 3) AND `WRITE_CAPABLE_EMAILS` includes `alyssa@opalinvest.com` (Case 4) | on-box env | andrew@ = the MCP-path identity (confirmed live via whoami 2026-07-01); alyssa@ = the write-grantee; a missing WRITE_CAPABLE entry false-locks alyssa@ to READ_ONLY |

## The 4 cert cases

| # | Case | Identity presented | Call | BINDING pass signature (LIVE) | G6 audit corroboration (s3://opal-mcp-audit) |
|---|---|---|---|---|---|
| 1 | READ_ONLY tier → mutating **DENY** | a verified-but-unmatched email → READ_ONLY (or any caller under an unverified provider → forced READ_ONLY) | `create_draft` | tool result `{"error":"tier READ_ONLY may not call mutating tool 'create_draft'","guard_denied":true,"code":"read_only_denied"}`; **NO draft created** | `outcome=denied`, `detail=tier READ_ONLY may not call...`, `tier=read_only` |
| 2 | no-identity → mutating **DENY** | no verified identity claim | `create_draft` | `{"error":"no verified identity established",...,"guard_denied":true,"code":"identity_required"}` (token path) **OR** `{"error":"mutating tool 'create_draft' requires a verified identity; none established","guard_denied":true,"code":"identity_required"}` (enforce path); **NO draft** | `outcome=denied`, `code/detail=identity_required` |
| 3 | master-admin → mutating **PASS** | `andrew@opalinvest.com` via alb_oidc (verified) — my live MCP path | `create_draft` | tool result = a **real draft object** (id/webLink); **NO `guard_denied` key** → guard did not block | `outcome=ok`, `tier=master_admin` |
| 4 | **write-capable (non-master) → mutating PASS** | `alyssa@opalinvest.com` via alb_oidc (verified), exact-matches `WRITE_CAPABLE_EMAILS` → STANDARD_EMPLOYEE | `create_draft` | tool result = a **real draft object**; **NO `guard_denied` key** → write-grantee NOT false-locked | `outcome=ok`, **`tier=standard`** ← the discriminator |

**Case 4 catches TWO opposite bugs (per COO):** a `guard_denied` return → alyssa@ was lumped into READ_ONLY = **false-lockout** of the write-grantee (RED). The `create_draft` PASS alone is identical to Case 3, so the **audit `tier` field is the discriminator**: it MUST read `standard` — `master_admin` there = **over-grant** (write-capable escalated to master), `read_only` = under-grant/lockout. Case 4 is not fully certified until the audit record shows `tier=standard`. (At this landing scope, STANDARD_EMPLOYEE passes G2 with no G1 recipient-cap / G3 confirm — those layer on next; a `create_draft` PASS with `tier=standard` is the correct result here.)

**Deny HTTP status:** capture as-observed. For an MCP tool call the `guard_denied` dict returns as the tool RESULT (likely HTTP 200 JSON-RPC with error in body); a REST mutating route may surface 403. The binding signature is the JSON `code`+`guard_denied:true`, not the HTTP status — record both.

## Identity-presentation mechanics (the operational crux)
- **Case 3** I fire directly through the ALB — my existing `m365` MCP path already resolves `andrew@opalinvest.com` (verified live via whoami). No forging needed.
- **Cases 1, 2 & 4** I cannot forge a non-master identity / no-identity / a specific write-grantee (`alyssa@`) through the ALB OIDC session. Two sanctioned routes:
  - **(a) primary** — on-box exercise against the local app listener (0.7.0~A owns the box + runs on-box-verify): a header-provider request with a verified-but-unmatched `X-User-Email` → READ_ONLY deny (Case 1); a request with no identity → identity_required deny (Case 2); a request presenting `alyssa@opalinvest.com` under a **verified provider** → STANDARD_EMPLOYEE PASS (Case 4). **Case-4 note:** alyssa@ only resolves to STANDARD_EMPLOYEE under a signature-verified provider — a plain unverified header-provider forces READ_ONLY for everyone (root-of-trust), which would make Case 4 read as a false-lockout artifact. So Case 4's on-box exercise must run under a verified-provider path (or the real ALB with an alyssa@ OIDC session), not the DEV header provider.
  - **(b) alt** — dedicated OIDC test accounts through the ALB: a non-allowlisted read-only account (Case 1), an identity-stripped request (Case 2), an `alyssa@` session (Case 4).
  - Recommend **(a)** with the verified-provider caveat for Case 4; I independently confirm via (i) witnessing the re-exercise and (ii) the audit-lake records (esp. Case 4's `tier=standard`).

## Positive-path scope note (Case 3)
`create_draft` proves the guard PASSES master-admin on a mutating tool with **zero external side-effect** — this certifies the guard's contract ("do not block master-admin"). The actual Graph *send* is unchanged by SCTY. If a FULL end-to-end "andrew@ CAN still send" (an actual irreversible `send_email`/`send_chat_message`) is wanted, that is an outward side-effect → I fire a controlled self-directed send to Andrew ONLY on explicit Andrew/COO confirm. **Recommendation: Case-3 = `create_draft` for the guard-cert.**

## Rollback triggers (flag COO immediately; do not fix-forward)
- Case 1 or 2 returns a non-deny (draft created / `ok`) → guard **fails-OPEN** → RED, rollback.
- Case 3 returns `guard_denied` (master-admin blocked) → guard **fails-closed-too-hard** (master-admin path broken) → flag.
- Case 4 returns `guard_denied` → write-grantee **false-locked** into READ_ONLY (RED); or Case 4 audit shows `tier=master_admin` → write-capable **over-granted** to master (RED). Either = a tier-resolution bug.
- Any precondition P1–P3 fails → cert cannot proceed; report + hold ledger open.

## Independent corroboration (CVO grounding discipline)
After exercise, read `s3://opal-mcp-audit` for the four records (denied/read_only, denied/identity_required, ok/master_admin, **ok/standard**) — grounds LIVE behavior against the SERVED audit artifact, never a self-report. Case 4's `tier=standard` in the audit is the load-bearing discriminator between correct-grant, over-grant, and lockout.
