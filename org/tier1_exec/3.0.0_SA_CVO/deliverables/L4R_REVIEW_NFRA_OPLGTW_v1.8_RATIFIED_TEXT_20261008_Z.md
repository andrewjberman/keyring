# L4-R review, NFRA_OPLGTW PRD v1.8, ratified-text half (CONTRACTS, C7) -- REFUSE (3.0.0_SA_CVO~Z, 2026-10-08 ~16:0xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 31854 and 31857 (this seat signs while `3.0.0_SA_CVO~O` is dark; the half is a file,
because `prd-signoff` binds the ENDPOINT hash and v1.8 moves CONTRACTS only). **Bytes reviewed:**
`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @29b7392bc9, the v1.8 addendum; `git diff 36ae4e822d 29b7392bc9`
on that file, whole (+58 -1). **The question put:** does the text say plainly what is Andrew's word and what is this
fabric's design, and is the widening stated whole.

## Verdict: REFUSE, on one ground

**The domain table's stated source holds a domain Andrew did not name.**

- The text: the table's entries "are copied from `infra/logic/registry/scopes.json` (`tenant.email_domain`) and
  `infra/logic/registry/mail_parties.json` ... entry by entry", and "the firms are his ... adding a firm is his word".
- My read of the two files at CLOUD (@f5accebd7c): `scopes.json` carries FOUR tenant domains, for 49 Financial,
  Inflection, Cottonwood and **`demo`, whose domain is `demo.test`**. `mail_parties.json` carries Opal's own domain and
  an Alongside row with no domain.
- His words (item 6 of the 2026-10-07 ~18:3xZ record, which I read): "client emails only (cottonwood, inflection,
  49financial, alongside, and opalinvest of course for internal)". Five parties. `demo` is not one.
- So a release that copies the files entry by entry, as the text directs, admits a sixth domain. `demo.test` cannot
  receive mail, so nothing would be read through it today. The ground is that the text's source and the text's rule
  disagree, and the next row added to `scopes.json` for any reason would be admitted the same way.

**The cure, one sentence in the domain-table paragraph:** the table holds the domains of the five parties he named and
no other; a domain in those files belonging to any other row is not copied; the halves list each entry beside the
party it belongs to.

## On the two questions as put

- **His word and this fabric's design are told apart plainly.** The addendum says the admission and listing shape is
  this fabric's design, stated to him twice, and that the firms are his. It also says the CTO did not read the record;
  I did, and the addendum's account of his words is faithful: his mailbox, the five parties, his name in the body.
- **The widening is stated whole in extent:** "every message from every address at a listed firm can be listed and
  fetched by the bearer's one holder", against three exact addresses today.

## Two notes, neither a ground

- **His second condition is not applied by the gateway.** He set two tests: the sender's firm, and his name in the
  body. The gateway applies the first; "the body test is the caller's". The text says so, and it is a sound design
  (the gateway reads no body to decide a listing). The consequence should be in the never-widen halves in plain words:
  the gateway will serve the bearer messages that do NOT name him, and for Opal's own domain that is every internal
  message in his mailbox within the window.
- **Alongside has no domain on record,** so one of his five parties is not served by this release. The text covers the
  rule ("a firm with no domain recorded is not considered"); the release record should say it by name.

## What reads correctly

GET only; the same prefix and bearer; rows of five fields with no subject, body, recipient or attachment name; a whole,
case-insensitive domain compare with no subdomain or suffix match; an empty table refusing every domain request before
any Graph call; the audit carrying a hash of the domain and never an address; the negative arms; and the restart held
under row Z-S67.

-- 3.0.0_SA_CVO~Z
