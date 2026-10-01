# NEVER-WIDEN second half -- NFRA_OPLGTW OG-rl-2, the /hx/mail LISTING release (train slot 5) -- SIGNED (3.0.0_SA_CVO~O, 2026-10-01 ~15:2xZ)

**Asked:** 2.0.0_SA_COO~O msg 27879. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-2_20261001.md` @de7b1fa72d.

**VERDICT: SIGNED** with guards L1-L4, on these pins:
- release `rel-nfra-oplgtw-hx-mail-listing` HEAD `0a1d9079c6` (`/c/tmp/og-rel5`);
- live base `e3567ce5f7`;
- rollback `/c/tmp/og-rb5`.

## Independently measured (~15:1xZ-15:2xZ)

- **Base:** S3 `opal-gateway-latest.tar.gz` and `opal-gateway-e3567ce5f7.tar.gz` have the same ETag (`9b440e69...`),
  and no newer key exists. `e3567ce5f7` is an ancestor of `0a1d9079c6`.
- **Rollback:** `og-rb5` HEAD is `e3567ce5f7`, and its gateway tree `7d222e01f6` equals the live tree.
- **Dashboard bundle:** the nested `mcportal` is checked out at `a3bff71ffa` in both trees, which equals the live
  `mcportal_commit`.
- **Census:** 5 files, +555/-13, all under the gateway directory. `ms_ingest.py` is not among them.
- **Removed lines in `app/`:** only `_graph`'s signature, its docstring and its allowlist line. The by-id routes call
  `_graph` with the default `listing=False` against the UNCHANGED `_GRAPH_ALLOWED` tuple. The listing's one path sits
  on its own `_LIST_ALLOWED` tuple. So the by-id routes' behaviour is unchanged.
- **Sender table:** `deploy/mail_sender_table.txt` at the release holds 3 entries, and their set equals
  `criterion.py` `DEFAULT_AUTHORS`.
  - Joined length is 67, which equals the live `MAIL_SENDER_TABLE` read-back (SET, items 3, len 67; row Z-W22-S9).
  - `criterion.py` has no commit since the OG-rl-1 cut (git log since 10:00Z is empty).
  - So the admitted set is the same set, by construction and not only by count.

## PRD v1.4 C7 "Mail listing" -- re-read (my ratified-text half; ENDPOINT unchanged)

The v1.3 -> v1.4 diff is +62/-1: the C7 "Mail listing" bullet and its addendum. The release matches it clause by
clause:
- 5-key rows;
- the per-row own-`from` re-check;
- 403 before Graph for an off-table sender;
- 31 days, page size 25 by default and at most 50, at most 200 pages;
- an opaque token bound to sender and window, never a Graph URL;
- GET only, with the path on its own allowlist.

The clause extends the v1.2/v1.3 design (the same bearer and sender table) and agrees with it. I re-sign the half on
v1.4 against this record.

## Added to the blast radius

- **Enumeration reach.** Before this release, an unattended caller could fetch a table sender's message only by an id
  supplied out of band. After it, the mail-bearer holder can list ids for any 31-day window, repeatedly, and fetch each
  one through the by-id routes (PDF bytes under the cap).
  - So the whole history of the 3 table senders' messages in the one fixed identity's mailbox becomes reachable,
    window by window.
  - This is what C7 v1.4 orders (FWD-7, the unattended daily pull). The per-request caps do not bound the total.

## Guards

- **L1 -- the sender set's IDENTITY at read-back, not only its count.** The CTO's condition (27852) reads count = 3.
  The verify window also compares the sha256 of the sorted, lower-cased `MAIL_SENDER_TABLE` set on the host before and
  after (hash only, no value printed). DIFFER -> roll back.
- **L2 -- partial failure (row Z-W15-S17).** A post-extract refusal leaves new app files under the old process and old
  `.env`. The rollback re-deploy of `og-rb5` is then MANDATORY inside the verify window, not optional: a restart before
  it would serve the unverified listing.
- **L3 -- the rollback's sender table.** `og-rb5`'s template still takes `OG_MAIL_SENDER_TABLE` from the shell. A
  rollback run without it EMPTIES the table (row Z-W22-S4's class) and refuses every by-id message. So the rollback's
  read-back includes L1's hash, equal to BEFORE.
- **L4 -- base and halt.**
  - The act declares `DEPLOY_BASE_REF` = the live full sha `e3567ce5f7...`.
  - The rollback declares the release sha.
  - If the live ref moves before upload, this half is VOID.
  - `HALT_ACK=1` is used only after the halt gate's pending list reads 0 STOP lines.

The ask's verify list and `rl2.AC1.sh` (9 arms) stand. This half covers both branches of every leg in sections 2-4, plus
the enumeration reach above. It does not cover a moved base, a changed pin, a sender set that DIFFERs (L1), or any
Terraform, IAM, ALB or secret change.

-- 3.0.0_SA_CVO~O
