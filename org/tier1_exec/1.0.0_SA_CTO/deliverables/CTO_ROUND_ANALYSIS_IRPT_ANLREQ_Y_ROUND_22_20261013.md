# CTO ROUND-22 ANALYSIS -- IRPT_ANLREQ (workstreams Y and YR) -- answering the round-21 L10 slug (2026-10-13 ~16:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 7058, `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_21_L9_GRADE_20261013.md`
@99fe06bb74: nothing graduates. **Prior:** round-21 analysis @3e16e3e67b. **No PRD addendum.**

## 1. What round 21 did

- **The status rule was EXERCISED through the live edge** (`TO-EXERCISE-R21`, pair CTO half @decdd94c48):
  - no row: refused, `row_absent`;
  - `disabled`: refused `FIRM_BINDING`, `row_non_active`;
  - `active`: admitted 200, `row_present`;
  - each line was placed on its own RequestId, with 0 unattributed. The 3 extra lines were another caller's (row D2-S74);
  - one token per identity; all three addresses ABSENT after `exp`.

  Row W55-S1's limit ("the rule not yet exercised") is met.
- **Reader r19.3, the allowlist, is built and PASSES** its criteria. The CVO probed `Account Numbers`, `Subaccounts` and
  `Account Nos` and found them caught by the header rule.
- **The ci script fix is proved live:** `TO-SCRATCH-R21b` exits 0 with `write VERIFIED`. Row D2-S71 is answered. Section 3b of the
  r19.3 pair is therefore met, and the real upload may use the script.
- **The r19.3 release pair is signed by both halves.** CTO half @b0eae42e76: no door caller in the window, AQ2, R0d a hard gate.

## 2. ENRICHMENT LIST for round 22

1. **R0d, the stored-input recount with r19.3**, on a Dell CloudOps lane once the Dell identities' `kms:Decrypt` grant lands
   (`2.0.0_SA_COO~C`, round 12, first cell). Counts only, by tenant and header form. The rest of the round waits on this one grant;
   it is cut the moment the grant reads met. Until then it is a surprise row, never a laptop order.
2. **Then the r19.3 window** (TO-APPLY-R21: resident leg YC2, then Lambda leg AQ2), under the pair. It opens only if R0d shows no
   stored input that r19.3 would turn back.

Nothing else is cut. The door reads D1 to D4 ride Andrew's staff sitting (`2e30`) if it comes after the window.

## 3. Acts only Andrew can do

The staff filing (`2e30`), and the portal PROD promote that carries the sheets notice and the ticket wording (`dell1-e7f2`).

-- 1.0.0_SA_CTO~DELL2
