# ANDREW-DIRECT 2026-10-05 ~16:3xZ -- Security Analysis: no "no permission" screen; invisible in the sidebar for a non-Opal user

- **Channel:** the site-Z terminal of `2.0.0_SA_COO~D` (session 6c9ea2f7-a212-40bf-aefa-ce51b8750285), typed by Andrew. Three
  messages, ~16:35Z.
- **Context:** the round-42 list (CTO countersign @f5d6919117, item 4) asked for a read of the designed "no permission" state with a
  simulated non-Opal `firmId`. This seat found (msg 29701) that `ProtectedRoute.tsx:111-113` sends such a viewer to the firm's landing
  page before any role gate, so that state is never shown on `/security-analysis`.
- **Recorded by:** `2.0.0_SA_COO~D`. It is committed on branch `wk-DSGN_AMGTV1-r42-issue` during MSTR~Z's parity hold (msg 29688), and
  drains to CLOUD at PARITY CLOSED.

## Verbatim

1. "no there should not be a "no permission" screen."
2. "It should simply be invisible on sidebar and on access if you are not an Opal user."
3. "Dont worry about CTO~Z, I will speak to them directly on the subject now"

## What Andrew said at the CTO's terminal (relayed by `1.0.0_SA_CTO~Z`, msgs 29703 and 29704, ~16:4xZ, verbatim as relayed)

- "It should simply not be visible if you are not permitted. E.g., you dont see a sidebar element for Security Analysis if you are not
  an opal user. That is the easiest way to handle that."
- "I dont think we really need to go into the backend ops of how its not visible, because its just market data, not client data, so
  im not that concerned at this stage about making that URL completely blocked to non Opal users."

## What it sets (relayed at its own scope)

- **Round-42 item 4 is ONE read:** a non-Opal viewer sees no Security Analysis sidebar item. No "no permission" screen is built or
  graded.
- **No work on routes, redirects or the backend.** The existing route guard stays as it is. The CTO withdrew its ruling (a)
  (msg 29703).
- **Already true on DEV e6ab82ad, by static read.** The nav entry carries `requiresTier: 'internal'`, and the sidebar filter drops a
  path outside the firm's allowlist (`isPathAllowedForFirm`, App.tsx). Partner allowlists do not name `/security-analysis` (access40
  arms 1 and 3). The live read confirms it on the rendered sidebar.
