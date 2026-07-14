# Session 2026-07-14 ~17:30-18:15Z -- NFRA_WEBSITE Phase A executed: STAGING LIVE at https://new.opalinvest.com/
**archetype:** DEPLOY
**agent:** 0.7.0_AE_CloudOps~A

## Trigger
ANDREW-DIRECT (this session, ~17:3xZ, verbatim): "Check my emails from Patricia regarding setting up our
website for Opal, and check current status of NFRA_WEBSITE work. I want to proceed that project."
Recorded + broadcast same turn (COO 174132Z / CTO 174137Z / MSTR 174143Z; COO ACK 174415Z).

## What changed since the 07-13 record
- Andrew emailed Patricia (TWLC) 07-13 18:01 ET asking for the ONE unblocking record
  (A / new -> 18.208.18.213 / TTL 600). Patricia replied 07-14 14:27Z: "This has been completed."
  NOTE FOR THE RECORD: the GoDaddy human is PATRICIA/TWLC (she operates the sign-in), not only AJ Graff --
  the 07-13 "blocked on AJ" framing is superseded.
- VERIFIED LIVE (not self-report): new.opalinvest.com -> 18.208.18.213 on public DNS. A1 DONE.

## Phase A execution (TO-2; deploy ledger 20260714T1748Z_nfra-website-phaseA-staging, closed 7/7)
| Leg | What | Evidence |
|---|---|---|
| L1 | repo->S3 script parity | 5 scripts were STALE in S3 (predated the 127da60f3 domain purge!) -- synced, 9/9 ETag=md5 MATCH |
| L2 | A2 blog_public=0 | SSM ba1eaf33, re-read 0 |
| L3 | pre-re-key backup | SSM 8787060c, opal_wp_2026-07-14_175030Z.sql.gz (1.9MB) listed in S3 |
| L4 | A3 WP re-key off raw IP | SSM 68d30b2d dry-run 943 == 07-13 preflight; SSM 4f89830a live 943; residual-IP count 0; siteurl+home = https://new.opalinvest.com |
| L5 | A4 stage-issue HTTP-01 | SSM 6c093f10: LE cert CN=new.opalinvest.com, notAfter 2026-10-12 |
| L6 | A5 stage-wire | SSM 8829e56e: wired+reloaded; positive control 200; box-pinned strict 200; trusted chain |
| L7 | EXTERNAL exercise | off-box strict curl via public DNS: 200 from 18.208.18.213, real Bricks title. No -k anywhere. |

## Defect found + fixed en route
`tls-cutover.sh stage-issue` FAILED CLOSED on first run: the box enforces IMDSv2 (HttpTokens=required,
grounded on live describe-instances), so the script's bare IMDSv1 curl returned EMPTY and the
DNS-vs-self guard refused a CORRECT DNS state. The guard did its job (refused rather than proceeding
blind); the instrument under it was wrong. Fix: my_public_ip() token-first + IMDSv1 fallback, both call
sites -- commit cbd19923d, bash -n + safe-commit, S3 re-synced (ETag verified), re-run GREEN.

## Records driven to parity (the NFRA_WEBSITE stale-record lesson applied to itself)
- NFRA_WEBSITE.json phase+blocking: staging LIVE, at A6 gate; blocker text CLEARED.
- REGISTRY.md row: Phase A executed; ALSO fixed a second stale claim -- the row still said the
  admin_email W3 gate was OPEN; it was CLOSED 07-13 (andrew@opalinvest.com + new_admin_email shadow
  deleted, per TO-2 B2).
- TO-2 status field updated.

## Gates HELD (not advanced)
- A6 = Andrew + TWLC review https://new.opalinvest.com/ -- sign-off gate, THEIRS.
- PHASE B apex flip = public go-live: ONLY on Andrew's explicit word. Prereq: GoDaddy lowers apex A +
  www TTL -> 600 24-48h ahead. blog_public back to 1 is an explicit Phase B assert.
- SES sender graduation: untouched, separate gated window (second SPF TXT = RFC-7208 permerror).
- No outward-facing sends: I did NOT email Patricia/TWLC -- external comms route via Andrew.

## Blockers
None self-owned. Everything open is at a human gate by design (A6 review; Phase B on Andrew's word).

## Compiler Tools
| Tool | Result |
|---|---|
| comp-to NFRA_WEBSITE.TO-2... | session TO context set (race-free per-session file) |
| (raw aws, rail-checked) describe-instances MetadataOptions | grounded the IMDSv2 mechanism behind the stage-issue false-refusal -- live-primitive question no comp-tool models (TO-2 honest-gap note: no comp-tool covers DNS/on-box OLS/wp-cli/IMDS state; this lane rides raw aws/SSM with rail-checked markers) |
| ETag-vs-md5 parity sweep (website lane instrument) | caught 5 STALE scripts in S3 incl. the pre-purge tls-cutover.sh -- dispatching from S3 as-is would have run the OLD opalcapital-era script |
No comp-pipescript/comp-iam runs: no gold scripts touched, no IAM change (the fix was a read-path
lookup inside an on-box shell script).
