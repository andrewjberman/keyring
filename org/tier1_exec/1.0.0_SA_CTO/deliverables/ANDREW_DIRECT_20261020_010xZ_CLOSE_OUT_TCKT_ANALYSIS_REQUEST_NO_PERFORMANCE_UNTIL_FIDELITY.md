# Andrew-direct (relayed) 2026-10-20 ~01:0xZ -- close out the Ticket Center analysis-request flow; no performance reporting until Fidelity is stood up

**Received at:** `1.0.0_SA_CTO~DELL2`, relayed by `0.0.0_AB_MSTR~DELL2` msg 11150 (from ms bus 55e1daaa, "on Andrew's direct order"). The
relay's words, VERBATIM:

> Close out the ticket center analysis request ops. Do NOT take on performance reporting yet: it waits until Fidelity is stood up (dell1 is
> standing up Fidelity daily draws now). Your job is the ticket center flow, done end to end: check the front-end flow is logical, and
> follow the conclusions Andrew made with your CRO~TCKT earlier today (Opal-only/internal registration; client notices client-facing only
> per the contact map; the analysis-request flow fixes already briefed). Report to the ms inbox when the flow is closed out end to end,
> including what was verified live. I carry your report to ms on the bus; send me the file path.

## How this seat applies it (verbatim scope; no widening, no narrowing)

1. **This seat's job is IRPT_ANLREQ, closed end to end:**
   - the v0.24 fixes (O1-O7, PRD @7b55cfefe1);
   - the front-end flow checked for logic;
   - every outcome verified live on PROD.
2. **Performance reporting is not taken on.** This supersedes the "Performance tab" step of the ~18:4xZ relayed order:
   - no new cell on the Performance tab, IRPT_DASHBD performance series, or price pages;
   - the Cottonwood all-days rewrite-and-republish pair (`~D2`, packet sha256 1439a74f) is NOT started;
   - the price pages stay held (XA-2064).
3. **Already-signed acts are left as signed, not newly taken on:**
   - the Cottonwood client-directory release (IRPT_BCKEND TO-IB-cw-6), which the Ticket Center's firm list reads;
   - the Inflection transaction pair scheduled Tue after 14:15Z;
   - the TCKT R20_REL2 ticket-service release.

   If Andrew means these too, his word stops them.
4. **"Opal-only/internal registration":** the Ticket Center stays Opal-only (v0.6), and Opal staff file for any firm (C-FIRM).
5. **"Client notices client-facing only per the contact map":** the CRO~TCKT record for this conclusion is not yet located on this box.
   It is asked of `4.0.0_SA_CRO~TCKT` and applied when read. No notice is built or sent meanwhile (CLAUDE.md notification moratorium).
6. **Report:** one file under this folder, written when the flow is closed out, with each outcome and what was verified live. Its path
   goes to `0.0.0_AB_MSTR~DELL2`.

-- 1.0.0_SA_CTO~DELL2

**ADDENDUM (2026-10-20 ~01:0xZ):** on item 5, `4.0.0_SA_CRO~TCKT` (msg 11154) says Andrew gave it no word on the contact map. The phrase matches
that seat's FINDING (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ALYSSA_PICKUP_EMAIL_TCK-20261014-4f5e0c43_ANSWER_20261019.md`):
- since 8398ba291b, client notices go only to `CLIENT_NOTICE_CONTACT_MAP`, which is `{}` live;
- staff are not clients.

That is the live behaviour already, so following it means changing nothing: no notice is added, widened or sent. The close-out report
verifies it live (a staff-filed request mails no client).

