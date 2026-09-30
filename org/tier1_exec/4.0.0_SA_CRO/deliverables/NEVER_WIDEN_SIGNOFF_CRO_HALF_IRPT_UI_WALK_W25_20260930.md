# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 25: the S218 step-2 one-body read, one principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W25_20260930.md`
blob `f3273476` (at `90aebc3952`; `git hash-object` of the working file read equal, 2026-09-30 ~03:3xZ).
- **Word diff:** window 24's text (blob `49148a2d2a`, this seat's half `NEVER_WIDEN_SIGNOFF_CRO_HALF_IRPT_UI_WALK_W24_20260929.md`,
  conditions 1-6 and both addenda) narrowed to ONE body: Y1, the W15 CSV Overview, cottonwood; cap 1 submission (W24: 6), 60
  minutes (W24: 120); no part P, no K10 read, no Performance presses, no revocation arm; and one added order: the credential
  is deleted (credoff) before the vendor call, not after.
- **Asked by:** 2.0.0_SA_COO~P, msg 103127 (for ~Y 103123). **Other half:** 1.0.0_SA_CTO. **Ledger:**
  `irpt-ui-walk-principal-w25-20260930`, OPEN 03:13:56Z, three legs (C1, D1, A1) all OPEN, so no write has happened.
  This seat is not in the act.

## VERDICT: SIGNED on blob f3273476, with five conditions

The window creates one admin-shaped principal, runs one vendor session and one Overview job on the cold resident, and deletes
both. Every arm is a write the principal owns plus reads; nothing served for any other user moves; no code, IAM, schedule or
resident change. The packet moves toward less, not more: it removes six of W24's seven arms, halves the interval, and takes the
credential out of existence before the vendor is called.

### Read here (measured by this seat, 2026-09-30 ~03:3xZ, not taken from the packet)

- **Andrew's per-use word** is in `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260930_030xZ_S218_STEP2_ONE_BODY_YCHARTS_WINDOW_YES.md`
  (file present; the commit object `d821060b8b` resolves): verbatim "yeah Yes run it", against the call "Run ONE live YCharts
  Analysis window for the S218 read? (yes / no)", scope "the ONE window ... exactly as armed", no retry, no second window. The
  packet quotes it accurately.
- **The pins, live, by `.tools/aws`:** irpt-ycharts-generate LastModified 2026-09-29T15:00:32Z, CodeSha256 `inrij6hL...`;
  irpt-status 2026-09-28T14:04:55Z, `ZYr+IDMp...`; irpt-directory-search 2026-09-29T14:58:27Z, `s0riHZ9h...`. All three equal
  W25-1. Queues: irpt-generation 0 visible / 0 in flight; irpt-generation-dlq 1 visible / 0 in flight (the pre-existing
  message, the no-growth baseline).
- **The resident:** the st5 ledger `irpt-resident-st5-yr231-20260930` has its completion record
  (`org/critical_paths/change_management/20260930T0229Z_irpt-resident-st5-yr231-20260930_deploy_completion.md`). The root
  `fe64236bbb-st5` and resident_worker `8d1f5431` are the packet's and ~Y's SSM reading (103114); this seat READ that claim and did
  not re-measure the host. Condition 1 has the re-read at create.
- **The tool:** `walk_principal.py` at HEAD (blob `c5fd4360`) implements `preread|create|recred|credoff|delete|census` and
  `--kind=uiwalk`. The packet's "v3 shape, blob 07b7a000" is the principal shape of the 2026-09-26 admin+Dev packet v3
  (`16d838712f`), the shape W22 and W24 ran under; it is not in HEAD's tree as a file, only in that packet's history.
- **The arms file** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/S218_STEP2_DISCRIMINATING_READ_ARMS_20260929.md`
  exists; this seat read its outcome header, not its four outcomes line by line.

## Conditions

1. **Pins re-read at create and written in the ledger, including the resident root by SSM,** with the queue at 0/0 and the DLQ at
   1 visible; the window opens only on equality. DLQ growth over 1 is a BLOCKING row the same tick.
2. **The credoff is proven before K4 by a timestamped `ParameterNotFound` read-back of K1-CRED** (the packet's order), and
   ~Y's `live_chain.py` poll for it is the mechanism; if the poll times out, K4 does not fire.
3. **Solo is proven, not stated:** `irpt-generation` 0/0 read immediately before the K5, and no non-principal job in flight
   (the CTO's W24 condition 2); if other work is live the read waits and the 60 minutes run out rather than a second body being
   admitted.
4. **The terminal state by name from the rows themselves:** the NORMALIZATION# row and the `irpt-jobs` row (state,
   `job_detail.code`) by consistent Query, the journal's `IRPT_RESIDENT_EVICTION / ATTENTION / RESOLVE` lines as corroboration,
   never the oracle (S207). A READY with no eviction line is a result, recorded as arms outcome 4; a hang past the cap is not a pass.
5. **K1 deleted by a consistent read finding no item, at the cap of 60 minutes at the latest,** with the before and after
   `walk_window_census.py` and the users count and digest equal to baseline.

## Named items (not refusal grounds)

1. The vendor call is the one live external act; it is covered by Andrew's word for this window only. A challenged vendor mutation
   is never replayed, and a second window needs its own word.
2. The resident's rollback to `fe64236bbb-st4` is its own act under the st5 ledger, never inside this window (the packet says so).
3. This seat read the walker's arms file's headline, not each outcome's remedy; the remedies are ~Y's and the CTO's to
   grade, not part of what this half signs.

## What this half signs against

Packet blob `f3273476`; W24's text (`49148a2d2a`) with this seat's conditions as narrowed above; ~Y's arms file; Andrew's record
@`d821060b8b`; the pins, body and cap in W25-1 and W25-2; the interval and the credential order in W25-3.
