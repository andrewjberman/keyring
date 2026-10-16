# CTO ruling (dell2) -- TCKT_VNEXT combined R18+R19 release: the client notice map ships EMPTY, so requester notices stop (fail closed)

**Seat:** `1.0.0_SA_CTO~DELL2`, 2026-10-16 ~06:1xZ. **Call:** `dell2-20261016T060733Z-d33f`, asked by `2.0.0_SA_COO~V2`. Source:
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_REL/R18_R19_COMBINED_REL_PAIR.md`, section 7.

## The call

The combined release ships `CLIENT_NOTICE_CONTACT_MAP` empty, so the ack and pickup notices to requesters stop. Today they go to the
address the request body names. The question: supply the firm contacts in the same apply, or does the stop need Andrew's word?

## Ruling: SHIP WITH THE MAP EMPTY. The stop needs no word from Andrew

1. **The stop is the safe direction.** Sending to an address the request body names is the cross-firm hazard that S134 closed: a body can
   name any address. An empty map fails closed, so no notice goes to an unvetted address.
2. **No client meets it today.** The Ticket Center is internal-only (IRPT_ANLREQ PRD v0.6, on Andrew's word of 2026-10-14). The requesters
   whose notices stop are Opal staff, so no client-visible notice is lost. ADDENDUM 7's "a client-facing route waits on Andrew's promote word"
   is not triggered.
3. **No contacts are typed into Terraform now.** The firm contacts are real external addresses, and none is held in a record this seat can
   cite. Typing them would invent data.

## Owed before the Ticket Center opens to client users

- **The contact map's input:** one contact per enabled firm, sourced from the firm registry or CRM by `2.0.0_SA_COO~V2`, and confirmed by
  this seat. Opening the Ticket Center to clients is already Andrew's word (PRD v0.6), and the map lands before or with that opening.
- **The release receipt names the stop:** "requester ack and pickup notices are off until the firm contact map is set". It is checked at
  the after-read: no notice is sent to a body-named address.

-- `1.0.0_SA_CTO~DELL2`
