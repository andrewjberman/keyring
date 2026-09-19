# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtf-9 / IB-rtf-3's re-hand: the bounded test advisor principal on the deployed mint path (two keys, not one)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-19 ~09:4xZ. **The act signed:** the
creation, exercise and deletion IB-rtf-3 performs when RE-HANDED, exactly as
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtf-9.md` describes it, read at HEAD
after the drain of `wk-irpt_bckend-6-ae1` (tip 46b43b230d), **blob `a1f36b95b26c8fefd6ff0d47489f9884f87dd2c4`** (`git rev-parse
HEAD:<path>`, this turn). A packet whose bytes differ from that blob is NOT what this half signs; the re-handed order re-reads the blob
hash before any write. **This packet REPLACES the key list of IB-rte-1's packet (blob 3d9f57335b); my rte-2 half @a0f05dda0c covered that
key list and covers this act no longer -- a re-cut packet is a re-signature.** The CTO half is asked the same tick, by blob; the CTO
ruled (98209 s.2) that K1b is INSIDE Andrew's 17:3xZ approval @af794c77e3, the boundedness carried by the delete-at-round-close.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention. The writers of each named
property are counted (the packet's census, re-read here; N printed).

## The keys, as the packet names them

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K1 | ONE `opal-users-v2` PROFILE item: `PK=USER#usr_irptrte_<epoch>`, `SK=PROFILE`, a `.test`-TLD e-mail, `passwordHash` (random, never recorded), `name`, `role=user`, `firmId=49financial`, `status=active`, `createdAt`, `createdBy` -- 9 attributes, each cited to the deployed line that reads it; `userType`, MFA, phone, `mustChangePassword`, `advisorKey/advisorId` DELIBERATELY ABSENT (nothing on the mint path reads the last two; `Dev`/`admin` would widen); the `FIRM#/MEMBER#` item NOT written | one login exists for the interval; it appears in no firm-member listing; `updateLastLogin` and the throttle counter's delete are the only side writes, both on K1 or creating nothing (a FAILED login creates one TTL'd counter -- named in the ledger if it happens) | `DeleteItem {PK, SK}` VERIFIED by a consistent-read base-table `GetItem` returning no `Item` (never the eventually-consistent e-mail GSI); PITR retains the item in backups for the window -- named, not a defect |
| K1b | ONE `opal-partner-49financial` item: `{email = K1's e-mail, advisorKey = abby_horton}` -- 2 attributes, exactly what `lib/partner/index.ts:27-31` reads; `firmRole`, `advisorRole`, `advisorName` DELIBERATELY ABSENT (`admin` in either role field bypasses the edge check, the backend tier and the L1 scope) | the token minted on K1 carries `advisorKey = advisorId = abby_horton`: FIRM_ADVISOR on the IRPT scoped routes for EXACTLY `abby_horton`'s existing 49financial grants (33 accounts / 18 relationships at the packet's read; the CTO half s.2 guard re-reads the live map before any write), served as the disclosed partial; edge allow-list `[abby_horton]`; authorizer `allowedFirmIds = 49financial` only; advisor-intelligence routes L0 firm aggregates only (the pre-existing firm-membership exposure, the CTO's -- IN-RADIUS, not widened, narrowed or fixed). **This is the FIRST binding of `abby_horton` in the partner table (0 of 11 rows today) -- the CTO's notification card to Andrew (98209 s.3) carries that fact; it is not a gate** | `DeleteItem {email}` VERIFIED by a consistent-read `GetItem` returning no `Item`; DELETED FIRST (the binding goes before the login); `deletion_protection_enabled` guards the table, never an item; PITR named |
| K2 | the session: access token TTL 15 min (`jwt.ts:17`), refresh 7 days bound to K1's `PK + createdAt` and dying with the row | one advisor session for the interval; the token, the `Authorization` header, the password and any secret value are NEVER recorded -- only each access token's `exp` | none needed: after both deletes a new login, a refresh and `/auth/me` all fail; **an already-issued access token lives to its own `exp` with its claims baked in and the IRPT resolver re-checks the GRANT, not the partner row -- so the principal's interval closes at `max(K1 delete verified, K1b delete verified, last access-token exp)`, and the re-handed order proves the close by one refused (401) request after the last `exp`** |

**Writers of the named property (`opal-partner-49financial` rows), counted:** identity plane `W = 4 of 263` principals simulated
(256 roles + 7 users, 0 unsimulated, 0 UNKNOWN; resource policy NONE; positive control `Andrew_Berman` writes, negative control
`opalinvest-auth-lambda-role` GetItem-only does not): `Andrew_Berman` (the operator identity the seat holds), `Andrew_Berman_Console`,
`Opal_Terminal`, and **`opal-news-lambda-role`** -- a NEWS Lambda's role holding all four write actions on a partner identity table,
outside this act, an IAM finding for the IAM owner (also on `opal-users-v2`, the first packet). Code writers: `create_user_v2.py`
`_write_partner_table` via three operator wrappers -- NOT used by this act (it refuses a non-`@49financial.com` e-mail, writes an unread
`FIRM#/MEMBER#` item, and sends SES mail unless `--no-ses`; bound 2 forbids any send). Readers `5 of 23` production files direct (all
identity-claim sense: `lib/partner/index.ts`, `db.ts`, `auth.ts` at login/refresh/me, `partner_contracts.py` read-back); claim
enforcers `12 of 42`, `0` unclassified; 8 SNS-topic false matches verified line by line. **Re-derived here on a different
instrument, not taken:** the packet's own battery compared its three census lines against re-derived counts and read EQUAL 3 of 3 --
and read DIFFERS 3 of 3 on the pre-packet run (09:05Z, rc 1), so the comparison can fail; I did not repeat the IAM simulation (a
second run of the same instrument is repetition); the CTO half owes its own writer read.

## Both branches covered

- **The producer creates and exercises** (both halves at HEAD naming this blob; the CTO half s.2 guard reads `abby_horton` PRESENT in
  the live 49financial map): K1 then K1b immediately before the login, each read back by consistent `GetItem` and hashed with
  `passwordHash` excluded from the digest input; ONE login through the real portal route; the negative controls BEFORE any outcome arm
  (firm swapped to inflection/cottonwood refused `FIRM_BINDING` without echo `m of m`; a route outside `api/scoped/` refused; the
  terminated-client gap enforced) -- **a failed negative control is a STOP and a same-turn rollback**; then FWD-1 / FWD-2 / FWD-5 by
  real signed requests with artifact hashes, `k` and `count` recorded against the grant count at the event, vendor calls `0`; FWD-11
  recorded as not reachable by a FIRM_ADVISOR principal. **This half does NOT predict k; the arm measures it.**
- **The producer STOPS** (a half absent; the packet blob differs; `abby_horton` ABSENT from the live map; a negative control fails; a
  premise on the mint path does not hold): nothing is written, or whatever was written is deleted the same turn K1b-first with each
  delete verified by a failing read, and the K2 close proven after the last `exp`; row S86 stays ARMED until the re-cut lands.
- **The deletion at round close, in every branch, is VERIFIED, NEVER ASSERTED** (the CTO's condition (a), 98209): `2 of 2` failing
  consistent reads printed, then one refused request after the last access-token `exp`, the interval recorded as
  `[K1 create, max(deletes verified, last exp)]`, the ledger closed and committed before the grading reads. **A test principal whose
  deletion is unverified is a standing credential.**

## What this half does NOT sign

FWD-11's roster parameter (a separate act); any second principal; any ownership-map, directory, auth-handler, authorizer, edge or JWT-key
change; `opal-news-lambda-role`'s write access (the IAM owner's); the portal's tracked credential fixtures (row S87, the CTO's); the
no-book-login census (the CTO's, 98209 s.4); the served bytes of the edge validator and the API authorizer (cited at source, not
compared -- the packet says so); any act on the L0 firm-membership exposure.

**Push state:** LOCAL -- origin/CLOUD @3dbba3a27c (the AE seat's ls-remote read 09:28Z, cited); HEAD after the rtf-9 drain.
