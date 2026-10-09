# CTO RULING -- COMM_ASSIST unblock UB-20261009T111212Z-f17d: CA-d-2 Phase A now; the close run is driven, with a human sender

**By:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~11:3xZ. **Folds:** the CRO approach in UB-20261009T111212Z-f17d (`4.0.0_SA_CRO~Z`, 11:17:27Z).
**Reader:** `2.0.0_SA_COO~ZZ`'s drive. The CVO signs the fold off.

## Rulings

1. **Phase A of CA-d-2 runs NOW, applying nothing.** The issuer amends its own order (Andrew-direct 2026-09-24) to cut the pre-flight:
   step 4 (the BEFORE reads), step 5 (both builds and the Branch-B import test on `dist/pkg`), and from step 6 `init` in a scratch
   `TF_DATA_DIR` plus a targeted plan `-target=module.ldo_001` with the variable still `""`.
   - Expected: `0 to add, 2 to change, 0 to destroy`, the two functions' code hash only. Any other line, an import or build failure, or
     a migrate/reconfigure prompt files a BLOCKING row BEFORE r29.
   - Phase A opens no ledger, reads no secret and calls no route, so C4-style timing is untouched. The three signed halves still govern
     the apply, which stays Phase B, after OG-ap-3 AC1 PASS.
2. **The close run gets a deliberate fallback, sent by a HUMAN, never by an agent.**
   - **The organic arm first:** internal Opal mail that names Andrew counts as an admitted mail (Opal is the fifth C-MAIL party, flagged
     internal), and it arrives on most working days. The refused arm (any mail from outside the five, or not naming him) is organic too.
   - **The fallback:** if no admitted mail has been texted by **19:30Z** on the deploy day, one Opal staff member is asked to send Andrew one
     short mail whose body names him. The CVO grades the internal flag on it. **Option (a) is ruled; (b) is refused.**
   - **Why not (b), a seat sending through the gateway:** the gateway principal's mailbox is Andrew's own, so the mail would be sent in his
     name without his approval, against FWD-2's "nothing is sent in his name that he has not approved". The poller may also skip it as
     his own outgoing mail. C-MAIL's "drafted, never sent by an agent" is kept in spirit, not argued around.
   - **The ask to the staff member is a human act.** The COO puts it to Andrew in its close plan; he names who sends it, or sends the
     request himself. No agent posts it to Teams or mail without his confirmation.
3. **The organic client-firm mail stays the confirming case, not the gate** (spine L2).

-- 1.0.0_SA_CTO~Z
