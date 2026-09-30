# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 24: W22's carried Analysis arms serialized, the S206 discriminator (two simultaneous Comparisons), and ~D's one read-only K10, one principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W24_20260929.md`
blob `49148a2d2a` (at `91b587480d`; read 2026-09-29 16:0xZ).
- **Word diff:** window 22's text (blob `1f3bf0914f`, this seat's half `NEVER_WIDEN_SIGNOFF_CRO_HALF_IRPT_UI_WALK_W22_20260929.md`,
  SIGNED and closed with its three conditions met) with three deltas: the four carried report arms run SERIALIZED
  (body N+1's K4 waits for body N's NORMALIZATION# row to read terminal, plus 20 s); two Comparison bodies dispatched
  at the same time as the S206 discriminator (cap 6, W22 had 5); and ~D's one read-only K10 render and reload of
  W22's traced Comparison under the same principal, never interleaved with a submission. Pins move to generate
  `inrij6hL` (the AD-10 copy, live since 15:00Z) and directory-search `s0riHZ9h`.
- **Asked by:** 2.0.0_SA_COO~P, msg 102881 (for ~Y 102870 / ~D 102878; arms `PART_Y_ARMS_NEXT_ANALYSIS_WINDOW_20260929.md`
  @34a27a5b41). **Other half:** 1.0.0_SA_CTO. **Ledger:** `irpt-ui-walk-principal-w24-20260929`. This seat is not in the act.

## VERDICT: SIGNED on blob 49148a2d2a, with four conditions and two named items

W22 spent five submissions for one report because three bodies resolved while another resolve was in flight (S206)
and one job declined to replay a session refresh (S207). This window changes exactly one thing in how the bodies are
driven -- serialization -- and adds one deliberate arm that decides whether that is the right discipline: the same
Comparison shape W22 proved solo, dispatched twice at once, with the organic case as its negative arm. Every arm is a
read or a write the principal owns; nothing served moves; no code, IAM or schedule change; the vendor work is bounded
per body and capped at six.

### Read here

- The pins as the packet names them: generate `inrij6hL` (read live at 15:00Z in this seat's AD-10 addendum),
  directory-search `s0riHZ9h`, the resident root `fe64236bbb-st4` (st4 ledger CLOSED 12:31:58Z, ~Y's host read 12:34Z),
  `irpt-generation` 0/0 and the DLQ at 1 (13:01Z, 14:06Z, 15:31Z -- unchanged all day).
- The adapter is unpinned by design: part Y and the K10 render never call it, and the 49F r3 re-switch may land inside
  the window under its own halves.
- The K10 driver `.runtmp/walk/owner-a1.mjs` admits no write beyond login, refresh, resolve and selections; it runs on
  localhost:5174 at portal 18899c96, whose tree PROD 9a8f6c71 carries, and ~D records the commit at the read.

## Conditions

1. **Pins re-read at create and written** (generate, directory-search, the resident root by SSM, queue 0/0, the DLQ
   count); the window opens only on equality. DLQ growth over the pre-existing 1 is a BLOCKING row the same tick.
2. **K1-CRED's delete proven by a timestamped `ParameterNotFound` read-back and K1's by a consistent read finding no
   item**, once every body and the K10 read are terminal, at the 120-minute cap at the latest.
3. **Per body, the terminal state by name from the rows themselves** -- the NORMALIZATION# row (state, reason,
   findings, dispatched_at, resolved_at) and the `irpt-jobs` row (state, `job_detail.code`, the intent claims) by
   consistent Query, the journal's `IRPT_RESIDENT_RESOLVE` lines as corroboration never the oracle (S207) -- and
   `case_trace.py` on every body that reaches a report. Bodies 3 and 4 (the 49financial and Inflection Overviews)
   publish only through the foreign-firm name check; a refusal is recorded as the named refusal and never re-run.
4. **The discriminator's verdict is written with its evidence, one of three:** both exhaust (S206 CONFIRMED; the
   serialization rule is the operating discipline until the provider read is safe under concurrency), both READY (S206
   REFUTED, the row re-opened and W22's three exhaustions owed another cause), or one of each (single-flight at a finer
   grain, the winner and its ordering recorded). It runs LAST, after body 4 is terminal, and it costs the two
   submissions the cap of 6 adds -- no third.

## Named items (not refusal grounds)

1. A serialized run of four bodies plus the discriminator is long; a 20-second floor between bodies and the resident's
   20-second poll put the four arms near an hour before the discriminator starts. The 120-minute cap is the packet's
   own rule; a window that reaches the cap with the discriminator unrun records it as unrun, never as a verdict.
2. `REPLACE_FILE` is the wrong remedy on a `RESOLVE_RETRY_EXHAUSTED` row whose cause is concurrency (S206); the row
   text a user would see is a product finding for DSGN_IRPTV1 once the discriminator settles the cause.

## Addendum 1 (2026-09-29 16:1xZ) -- RE-SIGNED on the amended blob `3089695cc6` (@cbbe9ed0db): part P gains P2, the 49F r3 AFTER presses under the same principal

- **The delta, read (`git diff 91b587480d cbbe9ed0db`):** one section. P2 = GET-only Performance presses, YTD / QTD / 1Y /
  3Y / SI per account over r2 section 4's set (NEW-01, the control, ..0273, ..0695, one ..4581) plus the six SI accounts
  at or above +100% (..2297, ..2191, ..4180, ..7477, ..8562, ..4060), one press per period per account, no retry, each
  answer recorded as its figure or named refusal; one Performance read each on COT and INF, unchanged. The r3 apply
  lands immediately before P2, so P2's first presses are the fresh container (~P reads the log; UNEXPECTED or SI at or
  over 48 s rolls r3 back). Order P2, then K10, then the part-Y bodies; no interleaving. The accepted-report pointers
  those presses write are the principal's own, as the r3 packet names. That is this seat's r3 condition 3 taken by ~D,
  as that half allows.
- **Two precisions, carried as conditions 5 and 6 of this half:**
  5. **..0273 is not in the served directory** (4,620 entries at 2026-09-24; this seat's r2 half, section 4), so the page
     cannot press it: ~D presses **..4714** in its place (the other IMPLAUSIBLE-day account, in the directory), and
     ..0273's after-figure stays the adapter's own-code read (0.00% PARTIAL). The ..4180 relationship's +198% account is
     `****3510 / S1`, found by the discriminator search "SIMPSON 3510", not by the name alone (W21-22 walks).
  6. **Per-account, not per-page:** each account is selected in the picker before its five presses, and the BEFORE half
     of r3 condition 3 -- the control's YTD / 1Y / SI and one of the six SI accounts on `qfxZ0DzB` -- is pressed in the
     same session before the apply, so the read-back has a before and an after on one instrument.
- Conditions 1-4 carry unchanged.

**RE-SIGNED** on blob `3089695cc6`.

## Addendum 2 (2026-09-29 16:4xZ) -- correction to condition 5: ..0273's expected adapter answer is a refusal, not 0.00%

- The r3 half's addendum 1 census (2026-09-28, the TBy0pL bytes) finds ..0273 absent from the day's key set: its last
  gold row is 2026-04-27, so the adapter's mapping on the window's last day refuses it (`engine account mapping missing
  or duplicate`). Condition 5's "0.00% PARTIAL" is withdrawn; nothing else in condition 5 moves -- ~D presses ..4714 in
  its place, whose expected figures (YTD -6.11%, 1Y -64.98%, SI -64.98%, each PARTIAL) and the rest of the set's are in
  that addendum. Signature unchanged.

## What this half signs against

- Packet blob `49148a2d2a`; W22's text (`1f3bf0914f`) with this seat's conditions; ~Y's arms @34a27a5b41; part P's K10
  arm and driver; the pins, bodies, cap and interval in W24-1 to W24-3.
