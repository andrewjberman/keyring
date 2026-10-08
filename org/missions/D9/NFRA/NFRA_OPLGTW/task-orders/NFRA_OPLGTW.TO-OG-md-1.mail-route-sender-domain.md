# NFRA_OPLGTW task order -- `OG-md-1` -- the headless mail route admits and lists by sender DOMAIN (PRD v1.9, C7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-md-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~36</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the tests run offline with Graph faked.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is PRD v1.9's C7 addendum (org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @b736f07a28), ratified-text half signed @d77caa1548.
EGRESS CLASS, declared: NONE. No network request of any kind; no mailbox is read.
</preflight>

## 1. THE CELL -- `OG-md-1` (decomposition addendum R3-T.29)

The gateway's headless mail route, `infra/aws/ec2/opal-gateway/app/mail_route.py`, serves a message only when its own
sender ADDRESS is on `MAIL_SENDER_TABLE` (three addresses today), and lists one table sender at a time. Its own text
says "No thread reach, no domain match". PRD v1.9 changes that in two places and nowhere else. READ the addendum
first: the section `### v1.8 addendum` of `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`, as v1.9 amended
its domain-table paragraph. Where this order
and that text differ, the PRD wins and you report the difference.

Do:
1. **The domain table.** One new configured value, `MAIL_SENDER_DOMAIN_TABLE`, in `app/config.py` beside
   `MAIL_SENDER_TABLE`, read the same way. A `domain_table()` function beside `sender_table()`: lower-cased entries;
   empty or unset means NOTHING is admitted by domain.
2. **Admission.** `sender_allowed` admits a message when its OWN sender address is on the sender table (as today) OR
   its own sender's DOMAIN is on the domain table. The domain is the text after the LAST `@`, compared
   case-insensitively and WHOLE: no subdomain match, no suffix match. No thread is consulted. The message-by-id route
   and the two attachment routes apply the same rule, because they already call the same function: prove that, do
   not duplicate the rule.
3. **Listing.** `GET /hx/mail/messages` takes EXACTLY ONE of `sender` (as today) or `sender_domain` (ONE domain, which
   must be on the domain table, else 403 before any Graph call; a malformed value is 400). Both, or neither: 400.
   - With `sender_domain`, the Graph filter is the received window ONLY (and `hasAttachments` when asked). Do NOT put
     any filter on the sender address into the Graph query for a domain listing.
   - The gateway judges each row's own `from` against the REQUESTED domain. A row that fails is dropped and counted,
     never listed. The existing drop-and-continue loop and `MAX_PAGES` stay; a page may hold fewer rows than
     `page_size`, and an empty page with a `next_page_token` is legal.
   - Rows are v1.4's five fields EXACTLY. No subject, body, recipient, sender or attachment name is added.
   - The opaque page token binds the sender OR the domain, and the window. A token minted for one is refused 400 for
     the other, and for another domain.
4. **Audit.** The listing's audit record carries a HASH of the domain (as it carries a hash of the sender today), the
   rows listed and the rows dropped. Never the domain, an address or content.
5. **The deploy template.** The sender table reaches the host from the shipped `deploy/mail_sender_table.txt` through
   `deploy-to-ec2.sh` (lines 279-294 and the `.env` write near line 400). Add the domain table the SAME way: a shipped
   `deploy/mail_sender_domain_table.txt` and the same host-side read into `MAIL_SENDER_DOMAIN_TABLE`, with these
   differences: an EMPTY or missing domain file is LEGAL (the route then admits nothing by domain) and the deploy
   does not refuse on it; a character outside a domain list (letters, digits, `.`, `-`, `,`, space) refuses as the
   address check does. **Ship the file EMPTY** (comment lines only). The comment says, as PRD v1.9 does: the table holds
   the domains of the five parties Andrew named and no other row's; `infra/logic/registry/scopes.json`
   (`tenant.email_domain`) and `infra/logic/registry/mail_parties.json` are where a party's domain is LOOKED UP, never
   a list to copy whole; the demo tenant's domain is not admitted; the release's record lists each entry beside its
   party. Which domains go in is decided at the release, in the never-widen halves, not here.
   Change nothing else in `deploy-to-ec2.sh`: not the bun pre-check, not the pip line, not the restart.
6. **Tests.** `infra/aws/ec2/opal-gateway/tests/test_mail_route_domain.py`, offline, the seven tests the header of
   `md1.AC1.sh` lists, named EXACTLY `test_ogmd1_ac01` to `test_ogmd1_ac07`. Use made-up domains under `.example`
   or `.test` and made-up addresses; never a real firm's domain or a real person's address. Reuse the fakes of
   `tests/test_mail_listing.py`.
7. **Do not weaken v1.4.** Delete or rename no existing test in `tests/test_mail_route.py` or
   `tests/test_mail_listing.py`. If an existing test pinned behaviour that v1.8 changes (for example "a request
   without `sender` is 400"), update ONLY the assertion v1.8 makes false, and name each such line in your report.
8. Update the module docstring's rules and the `sender_allowed` docstring so the file says what it now does.
9. Run, each in its own process, and state totals: `tests/test_mail_route.py`, `tests/test_mail_listing.py`,
   `tests/test_mail_route_domain.py`, `tests/test_principal_cutover.py`, `tests/test_data_entitlement_guard.py`,
   `tests/test_deploy_base_guard.py`, `tests/test_schwab_host_inputs.py`. If a test that counts `.env` keys or host
   inputs fails because of the new key, do NOT edit it: report its name and what it counts. That count is a release
   floor and the issuer moves it with the release.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~36/`.

## 2. BOUNDS

- No release, no deploy, no host act, no AWS call, no mailbox read. This cell is BUILT and HELD on your branch.
- GET only: add no write, send or reply verb, no new route path, no new bearer.
- Never write a real firm's mail domain, a real address, a tid, oid, credential or token into any file.
- Fetch nothing from the internet: no `pip install`, `bun`, `npm`, `curl`, `wget`.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/mail_route.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/deploy/mail_sender_domain_table.txt
infra/aws/ec2/opal-gateway/tests/test_mail_route_domain.py
infra/aws/ec2/opal-gateway/tests/test_mail_route.py
infra/aws/ec2/opal-gateway/tests/test_mail_listing.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~36/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W36-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-md-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r31/checks/md1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 7 of 7; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-md-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r31/checks/md1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)test_mail_route\.py: pytest rc=0 passed (\d+) failed/error 0; test functions at the cut \d+, now \d+, removed or renamed 0.*test_mail_listing\.py: pytest rc=0 passed (\d+) failed/error 0; test functions at the cut \d+, now \d+, removed or renamed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a listed domain is listed and fetched; every negative arm of PRD v1.9 refuses; the audit hashes the domain.
- `AC2`: the two v1.4 mail test files pass whole and lost no test.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-md-1.mail-route-sender-domain.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the diff of `mail_route.py`, `config.py` and `deploy-to-ec2.sh`; the proof that
   the by-id and attachment routes take the new rule through the one function; each existing assertion you changed,
   with its line; every test file run with its totals; any test that counts `.env` keys or host inputs and now
   fails; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 31 (R3-T.29), cut on PRD v1.9 @b736f07a28 (`1.0.0_SA_CTO~Z` msgs 31849, 31850), after the ratified-text half was
  signed by `3.0.0_SA_CVO~Z` @d77caa1548 (CTO ruling msg 31856). It is the laptop's cross-fabric request (CLAUDE.md
  rule 32), relayed by `0.0.0_AB_MSTR~Z` msgs 31616 and 31620.
- The mailbox is Andrew's own: the issuer's digest compare on live r28 (msg 31840).
- A WIDENING of a served read. The release that ships it carries CTO, COO and CVO halves that NAME the domain table's
  entries, and the file ships empty from this cell so no domain is admitted by the build alone.
- The release also changes the `.env` shape by one key, so the floor checks that count keys (51 today) move with it,
  and the restart falls under the form's rule on row Z-S67.
- Pre-cut: see the issuance commit.

<status>complete</status>
<round>31</round>
<slot>~36</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
