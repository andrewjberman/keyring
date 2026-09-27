# Never-widen sign-off packet -- WINDOW 18: the round-8 walk, K8 on the async export, and four identity reads

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete, and of the identity reads:**
`2.0.0_SA_COO~P`, 2026-09-27 ~20:2xZ. **Walker:** `2.0.0_SA_COO~D` only.
**Asked by:**
- `2.0.0_SA_COO~D` 102033 (the round-8 walk);
- the async-export packets' arms (dd91065c, 5f45ed04);
- `2.0.0_SA_COO~Y` 102032 / CTO 102028 (1) (the identity reads).

**Ledgers (opened before any write):** `irpt-ui-walk-principal-w18-20260927`. The window also closes the A1 legs of
`irpt-export-async-submit-20260927` and `irpt-export-reopen-rule-20260927`.

This packet is window 17's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W17_K8_EXPORT_20260927.md`, blob b185fd73, both halves,
and through it windows 16, 14, 12 and 10) with ONLY the deltas below. Window 9's read-only walk shape (blob 6dd81fbf)
is added as part A. Every unnamed section reads as window 17's, including:
- K7 and K8 (ONE 49F ****9978 YTD read, ONE export POST, the receipt GETs, ONE download if READY) and the route classes;
- every signing condition: the /download BODY out of the HAR, a local PDF only in gitignored tmp/, the %PDF audit on
  the SERVED object, no new *.pdf, *.png or *.har in git, the byte-proof at walk start and end.

## W18-1 -- three acts, one principal

- **A. The round-8 walk** (~D 102033): DSGN_IRPTV1 IV-e-54..66 on a LOCAL portal build of DEV `3b98939b` at
  localhost:5174, window 9's shape.
  - Reads only: GET, plus login, refresh, resolve and selections.
  - It covers E8's OVER WHAT expansion (UIR-17), the refusal state with a named refused account (UIR-18/19, read
    only) and "About this scope" (UIR-22), across 49F, INF and COT.
  - It is the artifact `3.0.0_SA_CVO` grades round 8 on.
- **B. K7/K8 on the async export**, after part A in the same session.
- **C. The four identity reads** on the resident host: operator P, not the walker. They run once, at any point while
  the window is open.

## W18-2 -- the pins, re-read at create

- irpt-export-render **`Ulim/gmf..`** with `IRPT_EXPORT_RENDER=on`, `IRPT_EXPORT_FUNCTION_TIMEOUT_S=120`, and
  event-invoke-config MaximumRetryAttempts **0**. Ledgers: async-submit D1 @d43edd47cd, binding CLOSED @ad0590b8f1.
- The SSM document irpt-export-render-run v5.
- adapter `bOefL9nx..` with no plan and `IRPT_EVIDENCE_BUCKET` set.
- irpt-status `bMMJ/bQ+5..`; irpt-directory-search `o1TXq5PH..`.
- The resident: running root `/opt/irpt-resident/fe64236bbb-lt`, queue 0/0.
- The page: local portal DEV **`3b98939b`** (~D 102033), with 0 tracked changes. ~D holds DEV there until this window
  closes.

If any differs, the window does not open.

## W18-3 -- when it opens and closes

- **Opens:** only after 4.0.0_SA_CRO reports its ui-walker DISARMED (102071, and its update: about 20:55Z), so no
  walker row or walker report lands inside the window. The user census and REPORT# census are taken AFTER that
  report.
- **Closes:** well clear of MSTR's freeze (102065, from about 03:00Z). The K1 cap is 120 min from create. K1-CRED is
  deleted when ~D reports logged in.

## W18-4 -- part B's arms (the async-submit packet dd91065c section 5, with CTO 102037 conditions 2-3)

1. ONE POST answers QUEUED with an `exr_` revision in **under 29 s, measured at the client from the HAR's POST
   duration**.
2. The pointer `firms/49financial/generations/<exr>/pending.json` goes BUILDING -> SUBMITTED with an EXP id, and its
   `binding` names this window's principal.
3. The receipt goes NOT_READY -> READY with a %PDF on the served object, or a named FAILED. The narrative slot shows
   either released prose or the client sentence, never internal validation text.
4. The render grant and the receipt name THIS window's principal. This is the reopen rule's arm 4.
5. The owner row is unchanged (arm 3). **One hop is proven by count:** exactly 2 irpt-export-render invocations for the
   ONE POST (the HTTP request and its marked event), read from the log group by request id.

**Censuses added** (before and after): `exr_` objects under both firm segments, and irpt-export-render invocations in
the window.

**On any arm failing:** P rolls irpt-export-render back per dd91065c section 3 in the same turn, before any other export.

## W18-5 -- part C, the identity reads (spec: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/P_COMPARISON_IDENTITY_READ_ACT_20260927.md` @5e97af4153)

- **Runner:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/comparison_identity_read_20260927.sh` (this
  commit). It is sent ONCE by SSM AWS-RunShellScript to i-0167fd745ad906a66 and runs as ec2-user.
- **The act:** EXACTLY four `GET /securities/securities_info?securities=P:{1728413,1728415,1728315,1728420}` on the
  resident's own published vendor session (`ResidentSession.acquire`, the `_opal` operation lease), with no body and
  no retry.
- **Stop rule:** a non-200, a login destination or a non-JSON answer stops the act. That read is recorded as refused,
  and the rest are not sent.
- **Write set:**
  - the vendor: 4 GETs, 0 writes;
  - the `_opal` lease row in irpt-jobs (acquire and release, as on every session use);
  - ONE evidence file, `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/COMPARISON_IDENTITY_READS_W18_20260927.json`,
    decoded from the command's stdout. It holds Opal's own model-portfolio rows, and no client data.
  - Nothing else: no S3, no queue, no job row, no report, no catalogue edit.
- **Proof:** the SSM command id and its output (4 statuses); the lease row's holder is empty after; queue 0/0 before
  and after; the evidence file's sha256. P sends ~Y the path.
- **Authority:** CTO 102028 (1) for these four reads with two halves, on Andrew's session egress (MSTR 101850 as scoped
  by CTO 101854). Andrew's permission word for the Comparison feature (CTO 102047) is separate, and this act does not
  depend on it.

## What the halves sign against

This file's committed blob; window 17's text (b185fd73) and window 9's (6dd81fbf) as amended here; the pins in
W18-2; the timing in W18-3; part B's arms with the same-turn rollback; and part C's runner at this commit, with its
write set and stop rule.
