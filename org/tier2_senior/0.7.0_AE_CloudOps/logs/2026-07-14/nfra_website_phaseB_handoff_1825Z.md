# NFRA_WEBSITE -- Phase B handoff: everything staged for go-live, keyed to the meeting being booked
**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE
**agent:** 0.7.0_AE_CloudOps~A · **window:** 2026-07-14 ~18:05Z -> ~18:25Z (delta since session_1730-1815Z log)

## Delta this window
- COO RAVC-4 VALIDATED Phase A (181142Z): independent second-observer exercise (https 200, trusted
  chain no -k, correct title) + ledger record confirmed. Loop closed, nothing owed.
- Patricia emailed Andrew 181015Z: "When do you want to plan to do the next step? We can book a time
  on the calendar." -> DRAFT reply created in Andrew's Outlook Drafts (NOT sent; Andrew sends):
  gives her https://new.opalinvest.com/ for the TWLC review, proposes TTL-change Wednesday +
  go-live window Thursday afternoon, re-states touch-only-the-A-records.
- Andrew-direct (this session): "great work write /log with handoff for next steps on this once we
  have the meeting set." This log IS that handoff.

## CURRENT STATE (zero-prior-context handoff surface)
- STAGING IS LIVE: https://new.opalinvest.com/ -- real Bricks site, LE cert CN=new.opalinvest.com
  (notAfter 2026-10-12), strict-verified on-box + external. Box i-0152e3fe2599fa630, EIP
  18.208.18.213, wp docroot /usr/local/lsws/wordpress. blog_public=0 (staging hygiene -- MUST be
  asserted back to 1 at go-live, TO-2 B7).
- Phase A deploy ledger CLOSED 7/7: org/critical_paths/change_management/
  20260714T1748Z_nfra-website-phaseA-staging_deploy_completion.md. Commits: cbd19923d (tls-cutover.sh
  IMDSv2 my_public_ip fix), 256837907 (records to parity). All pushed; S3 code prefix ETag-verified
  9/9 MATCH against repo HEAD.
- Governing records (all current as of 256837907): org/projects/NFRA_WEBSITE.json ·
  org/projects/REGISTRY.md row · org/tier2_senior/0.7.0_AE_CloudOps/task_orders/
  NFRA_WEBSITE.TO-2.opalinvest-cutover-staging-first.md · infra/website/RUNBOOK.md §4-5.
- GoDaddy human = PATRICIA (TWLC) at the keyboard; comms route VIA ANDREW only (MSTR-directed).
- admin_email gate: CLOSED 07-13 (andrew@opalinvest.com; new_admin_email shadow slot deleted).

## HANDOFF -- NEXT STEPS, KEYED TO THE MEETING (fires when Andrew confirms the calendar slot)
GATES FIRST: A6 sign-off (Andrew + TWLC review of the staging site) precedes everything below.
PHASE B fires ONLY on Andrew's explicit word. Owner of every AWS/SSM step: [0.7.0_AE_CloudOps~A].

  T-minus (before the go-live day):
  1. [Andrew+TWLC] A6 review of https://new.opalinvest.com/ -- pages/Bricks render, forms filled.
  2. [0.7.0_AE_CloudOps~A] W3 gate 2b prep (COO HARD-BLOCK, RUNBOOK 5.2b): prove the Contact-form
     notification END-TO-END to its REAL recipient. SES is still SANDBOX; info@opalinvest.com
     verification was INITIATED 07-10 and NEEDS A CLICK at the info@ inbox -- check
     get-identity-verification-attributes; if still pending, have Andrew click or re-send. A form
     that renders but cannot notify does NOT go live.
  3. [Patricia via Andrew, day before go-live] lower GoDaddy apex A + www TTL -> 600 (current
     ~86400; without this a rollback takes ~a day). Verify: dig +noall +answer opalinvest.com A.
  4. [0.7.0_AE_CloudOps~A] pre-flip captures for AC-4/AC-7: dig the FULL mail record set (MX, SPF
     TXT, selector1/2._domainkey, autodiscover, _dmarc) + capture Wix IPs (185.230.63.107/.171/.186
     = THE rollback target) into the new deploy ledger AT OPEN.

  GO-LIVE WINDOW (~30 min, Patricia live at GoDaddy; open deploy ledger FIRST -- NEVER#6):
  5. B1 re-key WP new. -> https://opalinvest.com (wp search-replace, dry-run count first, backup
     immediately before, assert ZERO residual new.opalinvest.com rows).
  6. B2a admin roster trim (Andrew-ruled at-go-live): KEEP opaladmin + patricia@; DEMOTE (not
     delete) mike/Lindsay unless Patricia asks -- confirm identities with Patricia first.
  7. B4 tls-cutover.sh issue (DNS-01; HTTP-01 CANNOT work -- apex still resolves to Wix) + show-txt
     from a SECOND SSM call; Patricia pastes the _acme-challenge TXT values (ADD-only).
  8. B5 tls-cutover.sh wire + verify -- strict, SAN-assert apex AND www. THE GO/NO-GO GATE.
  9. B6 [Patricia] FLIP apex A + www -> 18.208.18.213.
 10. B7 assert blog_public=1 (explicit -- a noindex launch is invisible for weeks).
 11. B8 tls-cutover.sh convert-renewal -- NOT OPTIONAL (a --manual cert never auto-renews; script
     refuses to run pre-flip, so it cannot fire early). Then certbot renew --dry-run must PASS (AC-2).
 12. AC-4 EMAIL UNHARMED: re-read the live zone, assert byte-identical mail records vs the step-4
     capture, AND exercise a real send to an @opalinvest.com mailbox.
 13. [3.0.0_SA_CVO] B9 live-verify the served site (render, forms+email, TLS, no mixed content).
 14. Close the ledger 100%; RAVC2 to COO+MSTR; records to parity (JSON/REGISTRY/TO-2).

  ROLLBACK at any point post-flip: point apex A back at the Wix IPs (fast at TTL 600). Wix stays up
  untouched throughout. AT GODADDY TOUCH ONLY apex A + www -- MX/SPF/_domainkey/autodiscover/_dmarc
  are LIVE M365 COMPANY EMAIL. SES sender graduation to @opalinvest.com stays OUT OF SCOPE (second
  SPF TXT = RFC-7208 permerror; separate window, MSTR first).

## Blockers
None self-owned. Open items are human gates by design: A6 review (Andrew+TWLC), the calendar slot
(Patricia<->Andrew, draft in his Drafts), Phase B on Andrew's word, info@ verification click (gate-2b
check is mine at T-minus).

## MCP traffic
2 significant this window: COO RAVC-4 VALIDATED received (181142Z, closed); no dispatches sent.

## Compiler Tools
None run this window -- coordination/scribe only (email draft + this handoff); no code, infra, or
search performed. Phase A's tool runs are logged in session_1730-1815Z and org/compiler-tools-log.md.
