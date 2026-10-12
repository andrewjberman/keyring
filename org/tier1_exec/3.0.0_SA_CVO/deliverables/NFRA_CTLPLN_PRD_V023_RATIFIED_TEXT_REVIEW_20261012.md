# NFRA_CTLPLN PRD v0.23 -- ratified-text half (ENDPOINT + CONTRACTS) review

**Reviewer:** `3.0.0_SA_CVO~L` (laptop), on the L4-R delivery 1.0.0_SA_CTO msg 108409 (also msgs 108407 and 2.0.0_SA_COO~C 108408).
2026-10-12 ~02:2xZ.
**Verdict:** SIGNED.

## What was read

- PRD at 8424b373f2: `org/missions/D0/NFRA/NFRA_CTLPLN/prd/NFRA_CTLPLN_PRD.md` v0.23, unchanged at HEAD.
- Hashes from `.tools/prd_signoff_lib.py`:

| pin | ratified-text half_hash | endpoint_hash |
|---|---|---|
| 6c5cf02601 (v0.22, last signed) | `01ea6f807832...` | `b6c8d5290b25...` |
| 8424b373f2 (v0.23) | `ee788020478c5ae495c0d31144d798bc96f758eac961c9c487052908a55c24b7` | `774926cdc75c...` |

## Checks against the delivery's four criteria

1. **ENDPOINT verbatim against the ratified pins.** A line diff of the ratified sections, v0.22 to v0.23, shows 0 lines removed and
   24 added. The 24 lines are FWD-27 and FWD-28, at the next unused ids. FWD-1 to FWD-26 are byte-identical, and nothing is
   renumbered. The header's `endpoint_outcomes` lists FWD-1 to FWD-28.
2. **Operative constraints present.** FWD-27: OpenSSH as a service, port 22 admitted only from 100.64.0.0/10, password
   authentication off once a key is in place, RDP unchanged, password and off-tailnet logins refused, and the elevated
   enable is Andrew's one line. This matches LD-0644 (cluster remote-access setup) and the record
   `ANDREW_DIRECT_20261012_015xZ_SSH_OVER_TAILNET_EXECUTE_COO_C.md`. FWD-28: a 403 for a partner-firm token and a 200 for an
   internal one on the data proxy and the content api's GET. PUT and DELETE keep their firm fence, and a "came through API
   Gateway" check is excluded. This matches section 3 of `CTO_RULINGS_POST_OFFLINE_FIVE_CROSSBOX_CALLS_AND_TWO_SECURITY_CARRIES_20261012.md`
   (XB-e588; its "11 routes" comes from the cited worker read @723a94955a). Neither outcome builds an alert or monitor.
   Both are provable on demand by one act, so neither waits on anything.
3. **No annotation, history or seat name inside the section.** One seat name is present: FWD-27's SOURCE quotes Andrew
   verbatim, "... perhaps COO~C can handle it". It is his word, not an annotation, and the existing SOURCE lines already
   quote him naming a role ("MSTR"). The routing it carries is restated in the v0.23 addendum, outside the section. NOTE,
   not blocking: at the next ENDPOINT bump, cut the quote at "rdp" so that no lane name sits in the ratified text.
4. **CONTRACTS agrees with the counterpart.** CONTRACTS is unchanged at v0.23 (0 diff lines). C-RDP (FWD-14) and FWD-27 are
   consistent: RDP stays the fallback, and SSH is added beside it.

## Not checked

I did not run a live call against either portal function. The ENDPOINT states an outcome to be exercised, not a fact to
verify at L4.
