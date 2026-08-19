# ANDREW-DIRECT 2026-08-19 ~19:4xZ — external intake email is opalsupport@, never opalbloomberg@

**Channel:** Andrew at the MSTR~Z console, said against the D7 TO-A one-liner's
membership-add proposal. **VERBATIM:**

> "We need to either change this email or create a new email to opalsupport@opalinvest.com.
> Can't be broadcasting 'opalbloomberg' externally"

**Effect:** whatever address joins the partner DLs / fronts the D7 intake (and anything the
Analyst sends externally) must present as `opalsupport@opalinvest.com` (or equivalent) —
`opalbloomberg@opalinvest.com` never appears externally. Reshapes D7 TO-B's intake-identity
input at laptop AE.

**Mechanism recommendation carried with the relay (not a ruling):** an ALIAS/proxy address
`opalsupport@opalinvest.com` on the EXISTING Opal Bloomberg mailbox — delivery stays in the
already-consented delegated-/me mailbox (TO-A's zero-new-consent property preserved),
outbound configured send-as opalsupport. A SEPARATE mailbox breaks the /me consent path and
forces the admin-consent round-trip TO-A priced. CAUTION: BG's identity pins (Teams monitor
+ gateway identity checks) pin `opalbloomberg@` — keep UPN/sign-in unchanged, alias only,
re-verify pins after the change.

**Whose act:** tenant admin (M365/Exchange admin center) = Andrew/IT hand — no seat holds
Directory-write (App-2 is delegated-only, 17 scopes). Put to Andrew as one-liner item 4.

**Broadcast (same turn):** laptop MSTR (f97c55bb — TO-B author's input), D7 seat
0.5.0_AE_OpalETL~Z (Q2 option-set amendment, TAC-1 unaffected).
