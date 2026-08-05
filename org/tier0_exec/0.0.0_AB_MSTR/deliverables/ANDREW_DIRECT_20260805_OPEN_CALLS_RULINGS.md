# ANDREW-DIRECT — /open-calls rulings, 2026-08-05 ~1550Z, base MSTR terminal

**Channel:** base MSTR terminal, in response to /open-calls (8 calls presented).
**VERBATIM:**

> "1.) Sitez should follow your rec (a). The rest of the recs are accepted, with two caveats:
> A.) I would have sitez set the bloomberg daily pull job at 7a ET. and B.) If its just a read
> token, why not just reuse the existing read token? That is easier, then we only need rotate
> one at a time."

## Dispositions (recorded, not adjudicated beyond the words)

1. **Site-Z CRLF fix = option (a):** audited one-shot `--no-verify` on the scoped EOL-only
   renormalization commit. NOT reset --hard.
2. **TAXSMA released to 0.2.0_DT** (rec accepted).
3. **Tag `security-ops-v0.2.0` delete APPROVED** (rec accepted; his word is the human
   confirmation the `git tag -d` gate required).
4. **Credentials caveat (B):** do NOT mint new read tokens where an existing read token can be
   reused — "then we only need rotate one at a time." The two held verify legs (freshguard
   leg-5 GitHub PAT; scty-premcp MS identity token) re-scope to REUSE-EXISTING-FIRST; owning
   seats evaluate which existing token fits and come back only if none exists.
5. **B6 capture uploader AUTHORIZED**, sequenced after CTO~B's corpus-delivery fix (rec
   accepted as framed).
6. **Bloomberg durable daily pull job: 7a ET** (caveat A — supersedes both the current 08:25 ET
   task time and my 03:37 ET recommendation). Sitez sets it.
7. **/govern standing re-arm row DISCHARGED** (rec accepted): the XXX.md Step 1b-F MSTR-row
   scoped re-arm (both seats) is struck; successors and MSTR~Z return to zero-crons-by-default.
8. **Phase-0 sitting:** no action needed; remains at his calendar.
