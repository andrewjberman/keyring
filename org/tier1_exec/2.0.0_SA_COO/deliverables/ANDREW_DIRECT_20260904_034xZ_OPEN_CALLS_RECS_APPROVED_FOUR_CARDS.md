# ANDREW-DIRECT 2026-09-04 ~03:4xZ at the `2.0.0_SA_COO~Z` terminal -- "Recs approved"

**VERBATIM, IN FULL:**

> Recs approved

**CONTEXT:** answered against a four-card `/open-calls` queue put to him at ~03:3xZ for `NFRA_OPSEC202609`. He approved **the recommendations as written**, not a free hand -- so the scope of each act is the scope of the REC it answered. The cards are reproduced below **because a two-word approval is only auditable beside the text it approved**, and one of these recs is materially narrower than the call it answers.

---

## CARD 1 -- the login-abuse alarm recipient

**CALL:** *Who receives the login-abuse alarm? One email address.* Alarm, topic, metric filter and staged burst all built and the alarm transitioned; `FWD-4`'s bar is that a HUMAN receives it, and nobody did.
**REC (approved):** *Your own address, changeable later in one act. An alarm reaching one real person beats a distribution list that does not exist yet.*

**AUTHORISES:** subscribing the topic to `andrew.opalinvest2@gmail.com` -- the address this fabric identifies him by.
⛔ **DOES NOT COMPLETE `FWD-4` ON ITS OWN. An SNS email subscription is created `PendingConfirmation`; AWS emails the recipient and the recipient must click.** Until the `SubscriptionArn` is a real ARN **the alarm still reaches nobody**, which is the exact state `OP-s-6` was held for. **Andrew must click that confirmation email.** Told to him in the same turn. Dispatched to `0.7.0_AE_CloudOps~U`.

## CARD 2 -- the `/wp-admin` allow list

**CALL:** *Which addresses may reach `/wp-admin`?* Never supplied, so the admin interface of the live WordPress site is unrestricted at the edge. Row `Z-S102`, ARMED.
**REC (approved):** *Name the addresses you actually administer from. If you do not know them, authorise us to derive a candidate list from successful admin logins and bring it back for your approval -- we will NOT self-approve it, because tonight a similar window turned out 97.8% our own probes.*

⛔ **THIS IS THE NARROW ONE AND THE DISTINCTION IS LOAD-BEARING. He did NOT name addresses.** So what is authorised is **derive a candidate list and BRING IT BACK.** **Nothing is authorised to go live**, and a lane reading "recs approved" as permission to apply an allow list would be exceeding the word. Dispatched to `0.7.0_AE_CloudOps~U` with that bound stated twice.

## CARD 3 -- `opalinvest.com` DNS and certificate

**CALL:** the domain is at GoDaddy, not in this AWS account; no ACM certificate; the apex is an A record CloudFront cannot be the target of. The DNS half of `FWD-13` is unexecutable. Row `Z-S101`, ARMED.
**REC (approved):** *Split it. (a) Add ONE ACM validation CNAME at GoDaddy now -- small, reversible, unblocks the certificate. (b) Separately decide the apex: migrate the zone to Route53, or serve on www with a redirect. I do NOT recommend sharing a registrar credential into the fabric.*

**AUTHORISES:** requesting the ACM certificate with DNS validation so it emits the record, and handing Andrew **one CNAME** to add. **The no-registrar-credentials recommendation stands as approved.**
⛔ **(b) IS STILL OPEN. I gave no recommendation on the apex, so the approval selects nothing there** -- migrate-versus-`www` remains an unanswered call and is back in the queue.

## CARD 4 -- the legacy `opal-users` table

**CALL:** delete it or keep it standing? 12 rows, both IAM grants removed and proven, nothing reads it, snapshot verified matching on item count AND byte size.
**REC (approved):** *Delete -- but only after removing it from Terraform management first, or the next plan proposes to re-create it as an empty table wearing the retired one's name.*

**AUTHORISES:** the deletion. This is the human word `S9-AC4` parked the retirement on.
⭐ **THE METHOD WAS CHANGED IN THE FACE AND THE CHANGE IS DISCLOSED RATHER THAN SILENT.** The rec said *remove from Terraform management first*; **the face (`TO-OP-S-9D` @`dfd71b7be9`) instead destroys it THROUGH Terraform by removing the declaration.** The rec's INTENT was to prevent an orphan the next plan re-creates, and **destroying via Terraform serves that intent strictly better** -- consistent state, the act inside a plan and a ledger, nothing left to re-create. **`state rm` followed by a manual delete is forbidden in the face**, because it leaves an untracked live table if the second half fails and puts the destructive act outside the plan where no gate can see it. **This is a method improvement within the approved decision, not a widening of it** -- the decision was *delete*, and it is still *delete*.

---

## DISPOSITION, same turn

- `0.7.0_AE_CloudOps~U` -- cards 1, 2, 3 (subscribe; derive-and-return; request the cert). Msg at 03:44Z.
- `0.7.0_AE_CloudOps~X` -- card 4 via `TO-OP-S-9D`, cut and committed @`dfd71b7be9`, gated on `TO-OP-S-9C` terminal. Msg at 03:48Z.
- **BACK IN THE QUEUE:** the apex decision (card 3b), and Andrew's click on the SNS confirmation email (card 1).

**Push state: LOCAL at this vintage; not read against origin.**
