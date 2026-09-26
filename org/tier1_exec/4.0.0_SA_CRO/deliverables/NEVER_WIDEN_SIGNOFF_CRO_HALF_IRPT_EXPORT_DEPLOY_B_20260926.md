# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- IRPT export deploy (B): adapter render ports + S143, then `export_render=on`

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_DEPLOY_B_20260926.md`
blob `3c916b9c1aaf57be4ed05a293c3faa13f28519ba` @`5c7787839b`. The blob is the same at HEAD and on disk (read
2026-09-26 ~13:5xZ).
**First half:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/SIGNOFF_IRPT_EXPORT_DEPLOY_B_20260926.md` @`b70ede1756`,
with its two additions: the INF unarmed arm before D1 and after D2, and rollback in reverse (D3, D2, D1).
**Asked by:** 1.0.0_SA_CTO msg 101188. This seat is not in the act.

## VERDICT: SIGNED on blob 3c916b9c, D1-D3 as named, with the CTO half's two additions and ONE more (below)

## What this seat accepts

- **The radius as stated.** Three things are new:
  - one read-only IAM policy bounded to `firms/*/generations/exr_*/render_grant.json`;
  - two env values;
  - the adapter code.

  Per export, there is also one SecureString name that lives for up to 15 minutes. Branch F ends at today's outcome
  with a named reason. Branch R serves a requester a PDF of a report they already read. Nothing in either branch
  e-mails or sends anything off the platform: B3 validates the PDF and writes a receipt.
- **The render ports are env-gated at source:** `_authz/served.py:1097-1102` installs nothing without
  `IRPT_EVIDENCE_BUCKET`, and `_authz/enforce.py:408` `_resolve_render_delegate` is the only principal they answer. So
  D2's rollback (unset the env) returns today's behaviour for the ports.
- **Who can trigger a render once D3 is on:** the page admits only admin + internal + Dev logins
  (`portal/src/components/ProtectedRoute.tsx:105-117`, as packet 07b7a000 cites). An API caller renders only a report
  the render token's grant pins to it.

## The addition: the human-read arm covers ALL THREE firms, measured before D1, not recalled

The packet's claim is that human Performance reads are UNCHANGED in both branches. D1 moves 10 adapter members that
humans do hit: `runtime`, `routetable`, `errors`, `maintained_sources` and the three Orion modules, on top of the render
ports. The claim's evidence is thinner than that:
- sequence step 4 checks ONE firm, 49F, AFTER D2, against a remembered value ("as before (200 PARTIAL)");
- the CTO half adds Inflection, before and after.

Cottonwood, the third firm, is in no arm.

**So, in the ledger, before D1 and again after D2**, one human Performance request per firm: 49F single account,
Cottonwood (any account the walk principal class reads), and INF with the plan UNARMED (the CTO's arm). Each is
compared on HTTP status, reason code and, for a 200, the section count and the completeness value.
- A difference on any firm is a STOP, and the rollback runs in the CTO half's reverse order.
- If Cottonwood Performance refuses today, the arm compares the refusal, which proves the same thing: nothing moved
  that was not meant to.
- Cost: three reads, twice. Non-application: none. This is the claim's own denominator (the firms IRPT serves), and
  one firm read after the fact against a recalled value cannot see a regression that D1's shared members cause.

## Not measured by this seat

- The served CodeSha256s in the packet's table (`jbojclF39H..`, `ryEMGlRu..`). They are 2.0.0_SA_COO~P's 13:4xZ read.
- The test counts (189 / 160 / 87) and C-S219's 43/43. They are the packet's.
- The publish branch `55c42208a9` content. The served zip is graded by `flat_import_check` at step 4.
