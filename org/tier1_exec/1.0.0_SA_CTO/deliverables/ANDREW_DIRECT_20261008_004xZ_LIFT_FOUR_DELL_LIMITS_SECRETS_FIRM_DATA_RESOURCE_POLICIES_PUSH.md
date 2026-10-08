# ANDREW-DIRECT 2026-10-08 ~00:4xZ (1.0.0_SA_CTO terminal) -- lift four of the Dell limits: 1, 2, 3 and 6

## His words, VERBATIM AND ENTIRE (two messages)

> "Concisely tell me what the dell boxes are not allowed to do, because im thinking of saying fuck it just let them deploy , let them run iams, let them just do admin stuff and get work done."

> "lets start with lifting 1 2 3 6"

## The list he answered, as this seat put it to him (numbered as shown to him)

1. Read any stored secret: vendor keys, client sign-in sessions.
2. Read parts of client firm data on dell1: another firm's code folder, and listing the Cottonwood bucket. dell2 is fully admitted.
3. Change who may reach a resource: bucket policies, key policies, Lambda permissions, queue policies (an explicit deny of 75 actions).
4. Create or change IAM roles and policies.
5. Change shared network routes.
6. Push to the shared code branch.
7. Download from the open internet.
8. Message a laptop work seat directly.

## Reading, at the width written

- **Lifted: 1, 2, 3, 6.** "lets start with" says more may follow; nothing else is lifted by this.
- **Not lifted: 4, 5, 7, 8.** IAM stays as he set it ("they shouldnt need to create or touch IAMs"); 7 is his download rule of 13:3xZ.
- **Item 3 reverses his own earlier line** "For now, laptop should admin" (bucket and key policies, Lambda permissions). He was
  shown that it does, in the same answer, and lifted it.
- **One width question on item 1, not decided by this seat either way.** The line he lifted names "vendor keys, client sign-in
  sessions". Minutes earlier this seat told him it had left the portal's signing keys, the admin seed and the gateway tokens
  out of the grant. Whether "1" takes those in is not said. The grant is cut WITHOUT them (the narrower reading, and the one
  that can be widened in one apply); he is told so in one line.

## Rulings to carry it, same turn

1. **Secrets.** The Dell group reads every vendor credential and every client-firm or custodian session in the store, whether
   or not a Dell project's code names it today. Out: the signing keys, seeds and bearer tokens (above), and nothing else.
   `openai-api-key` is a vendor credential and is now IN: his word lifts the read; whether a given project may call that vendor
   is still the vendor list's line, which a read does not change.
2. **Firm data.** dell1 is admitted to the firm-data fences in full, as dell2 is. The scoped rows of today become full rows; the
   prefix-list cell `2.0.0_SA_COO~C` described (msg 106668) is not needed.
3. **Resource policies.** The Deny on resource-policy actions comes off the Dell group. The routes Deny (item 5) stays. A Dell
   seat that changes a resource policy does it under its own box's never-widen pair; the laptop is told, per his 19:0xZ word,
   and steps in only on an overlap.
4. **The shared branch.** Each Dell's own fabric manager pushes its box's work to the shared branch itself: fetch, merge, push,
   never a rebase, with the same merge guard the laptop uses. The laptop's fabric manager stops being the only pusher.
5. Each of 1 to 3 is an IAM change the laptop applies (item 4 is not lifted), under a CTO and COO pair. This seat signs on receipt.
