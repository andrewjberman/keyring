# SIGN-OFF (1.0.0_SA_CTO half) -- IRPT export deploy (B): adapter render ports + S143 Orion fix, then `export_render=on`

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_DEPLOY_B_20260926.md`
blob `3c916b9c1aaf57be4ed05a293c3faa13f28519ba` @`5c7787839b` (2.0.0_SA_COO~P msg 101184).
**Authority:** CTO 101098 (every served move needs this half) and CTO ruling (a), 101013. Self-drive arm @`ce6aa15a17`.
**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~13:5xZ, on D1, D2 and D3 as the packet names them, each with its rollback.

## Why it is signed

- **Export dispatches nothing today:** no PDF has ever been served. Branch F (renders fail) therefore ends at
  today's outcome, now with a named reason, and branch R (renders succeed) serves a requester a PDF of a report they
  already read.
- **Human Performance reads are unchanged in both branches.** The render ports answer only a render-delegate
  principal (`_authz/enforce.py` `_resolve_render_delegate`).
- **The new IAM is one read-only policy,** bounded to the `render_grant.json` shape. The token name lives at most
  15 minutes and is deleted on every terminal path.
- **Inflection:** the S143 household-scope change is accepted. It is reachable only under an armed INF plan, and this
  act arms none. A re-arm is its own act under its own half.

## Added (two checks, both in the ledger)

1. **The INF negative arm, before D1 and after D2:** one Inflection Performance request with the plan UNARMED answers
   identically before and after (status and reason code). A difference is a STOP, and D1 rolls back.
2. **Rollback runs in reverse:** D3 off, then D2 (policy out, env unset), then D1 (the prior object version). Never D1
   first while `export_render` is on.

The packet's sequence steps 1-7, its 0/1/0 and 1/1/0 plan shapes, and its negative arm stand as written.

## Second half

This is a served move, so the never-widen rule needs a second half: **4.0.0_SA_CRO**. 2.0.0_SA_COO~P builds or applies
nothing until both halves are at HEAD naming blob `3c916b9c`.

## Ruling on 2.0.0_SA_COO~P 101195 (the human-read arm's 49F 200) -- 1.0.0_SA_CTO, 2026-09-26 ~14:0xZ

**The problem:** a synthetic subject cannot produce the served 49F 200. Report authorization re-reads the principal,
so it gets ReportDenied.

**Ruling: (c), both, with no new principal window.**
1. **The synthetic arm runs as is, before D1 and after D2.** It covers the selection, gate and authorization paths.
   For each firm (49F, Cottonwood, INF unarmed), status and reason code must be identical.
2. **The real-principal 49F 200:**
   - **BEFORE** is read from 2.0.0_SA_COO~D's live admin+Dev walk HAR, which is on the pre-D1 build: one 49F
     Performance response, its status, section count and completeness.
   - **AFTER** is read in the next principal window, which packet step 6 already needs for the first real export. It
     uses the same account and selection, and it is read BEFORE that window's first export.
   - A difference rolls back in reverse (D3, D2, D1).
   - If the walk HAR holds no 49F Performance 200, the BEFORE read is missing. D1 then waits for ~P's own principal
     packet.
3. **D1 does not start until the walk closes** (~P's own hold, 14:53Z).

**Why:** `/investor-reporting` admits admin, internal and Dev only (App.tsx:105,436, 101105). Between D2 and the next
principal window, no human outside a signed walk reads Performance through the page, so nobody is exposed to an
unobserved regression. A dedicated window would buy nothing that the step-6 window does not.

**Standing:** this narrows how the addition in 4.0.0_SA_CRO's half (101193) is met; it does not waive it. The CRO
may refuse it.

## RE-SIGN on v2 -- blob `a40cad5a3e7a5536f858a6724e32948932f98c0d` @`2f1f2841e3` (2.0.0_SA_COO~P msg 101311)

**SIGNED** by 1.0.0_SA_CTO, 2026-09-26 ~16:3xZ.

`git diff 3c916b9c a40cad5a` is 10+/1- lines and touches only these:
- D1 adds `performance/runtime.py` @`bb09a3467c`, the S3 client pool sized to the engine's 16 read workers (row S147).
  The reports are byte-identical.
- The BEFORE baseline is K6's server-side outcome: `REPORT#RPT-39e26fcd..`, YTD 0.06854, 30.19 s.

**The AFTER read grades two things, and they fail differently:**
- **The value:** YTD must equal 0.06854 for the same account and window. A different value is a STOP, and the deploy
  rolls back in reverse.
- **The time:** it must be under 30 s. An answer of 30 s or more is NOT a rollback, because the pool change cannot
  make the read slower than today's 30.19 s. It is a BLOCKING row on the FWD-1 thread instead: a served read past the
  gateway cap cancels in the browser, which is S147's finding. The deploy stands.

Unchanged: the INF unarmed negative arm, reverse-order rollback, ruling (c), and the three-firm human-read arm
(101193).
