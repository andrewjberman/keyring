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

### The addition, as answered for 2.0.0_SA_COO~P msg 101194 (~14:1xZ)

The synthetic arm (`deploy_b_human_arm.py`) returns 49F `ReportDenied`, COT `DEPENDENCY_UNAVAILABLE` and INF
`DEPENDENCY_UNAVAILABLE`. Those are refusal paths only, so it cannot see the served 200 the addition exists to protect.
It is kept as the immediate before/after check on the selection, gate and authorization paths. The 200 is graded
without a new principal window:
- **Before:** the 49F Performance responses in 2.0.0_SA_COO~D's walk HAR under packet 07b7a000. They are real
  principal reads, taken before D1 (P holds the adapter until the walk ends). Record their status, reason, section
  count and completeness in the ledger as the baseline.
- **After:** one 49F Performance read in the next principal window, the one packet step 6 already names for the first
  render, compared against that baseline. A difference is a STOP, with rollback in reverse.
- **Exposure between D2 and that window:** only an admin + internal + Dev login can open the page
  (`ProtectedRoute.tsx:105-117`), so the only readers who could see a regressed 200 in that gap are Opal Dev admins.
  This half accepts that, and names it.

## Not measured by this seat

- The served CodeSha256s in the packet's table (`jbojclF39H..`, `ryEMGlRu..`). They are 2.0.0_SA_COO~P's 13:4xZ read.
- The test counts (189 / 160 / 87) and C-S219's 43/43. They are the packet's.
- The publish branch `55c42208a9` content. The served zip is graded by `flat_import_check` at step 4.

---

## v2 (~16:3xZ): SIGNED on blob a40cad5a

**Packet v2:** blob `a40cad5a3e7a5536f858a6724e32948932f98c0d` @`2f1f2841e3`. The blob is the same at HEAD and on
disk (2.0.0_SA_COO~P msg 101312). The CTO re-signed on the same blob (msg 101314).

**Diff v1 -> v2, read:** a v2 header block, and the D1 source line adding `runtime.py` @`bb09a3467c`. Nothing else
changed.
- **The pool line is accepted.**
  - `bb09a3467c` changes `performance/runtime.py` only (6 insertions, 1 deletion): `max_pool_connections` =
    `f49_engine.MAX_READ_WORKERS` (16) on the shared botocore `Config`.
  - Retries are unchanged (`total_max_attempts: 1`).
  - It changes how many connections are pooled, never what is read or computed. The packet's "reports are
    byte-identical old vs new" is 2.0.0_SA_COO~P's measurement, not re-run here.
  - The new module-level `import f49_engine` is inside the package that step 4's `flat_import_check` grades on the
    served zip.
- **The BEFORE baseline is now value-level,** which is stronger than this half's status/reason/section arm:
  - K6's server-side outcome is `REPORT#RPT-39e26fcd..`, 49F, YTD 0.06854, actual 2026-01-02..2026-09-24, computed and
    retained in 30.19 s. The browser's GET was cancelled at the gateway cap.
  - This meets the addition as answered for msg 101194: a real-principal 49F read before D1.
- **The AFTER branches, agreed with the CTO's clarification (msg 101314):**
  - a YTD other than 0.06854 for the same account and window is a STOP, with rollback in reverse;
  - 30 s or more is NOT a rollback, because the BEFORE state was already 30.19 s and the pool cannot make it slower.
    It is a BLOCKING row on FWD-1 (S147).

  Both branches are covered.
