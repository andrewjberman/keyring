# 0.7.0_AE_CloudOps~A -- NFRA_WEBSITE W1 close-out + a dead least-priv control + the ghost-sentinel RED

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, DEPLOY, IMPLEMENT
**serial:** 0.7.0_AE_CloudOps~A | **date:** 2026-07-09 | **window:** ~1830Z -> ~1945Z | second log of session

## Summary
NFRA-first drive session. Three things, in order (COO-sequenced): (1) dispositioned a NEVER#6 RED
deploy-ledger -- CLOSED with a FRESH live exercise, and ground the RED itself to a structural
close-mechanism bug (a resurrected sentinel = a ghost RED); (2) sent COO/Andrew the exact hand-steps
to mint the read-only MS identity token the layer2 ledger is HELD on; (3) drove NFRA_WEBSITE **W1 to
completion** -- verified all 6 acceptance criteria LIVE, found + fixed the one real gap (the WP DB user
held `ALL PRIVILEGES ON *.*`), proved DR end-to-end (backup + restore drill), fixed two smaller
defects. COO independently re-verified 4 ACs on live and **ACCEPTED W1**; TO-1 closing; W2 GO'd.

## The finding, stated correctly (COO-requested framing)
I did **not** "fix a DB permission." I found **a control that existed, ran, reported success, and
enforced nothing.** `bootstrap-stack.sh` had a least-priv "verify" block meant to guarantee the WP DB
user is scoped to its own database. Its detection regex was `ON \*\.\*.*(ALL|SUPER|GRANT OPTION)` --
it looked for the privilege token to the RIGHT of `ON *.*`. But `SHOW GRANTS` emits the token to the
LEFT (`GRANT ALL PRIVILEGES ON *.*`). So the regex never matched, the code fell to its `else`, and it
**affirmatively logged "least-priv confirmed"** while the live grant was `ALL PRIVILEGES ON *.*`
(global). The control's own success condition was **decoupled from the property it existed to
guarantee**. A code-read shows "least-priv enforcement: present." Only EXERCISING it -- reading the
live `SHOW GRANTS` and reproducing the regex against the exact grant string -- revealed the grant was
`*.*`. This is the purest instance of the session's through-line COO named: *an instrument reporting
confidently on something other than what it claims to measure* -- the tenth instantiation today,
alongside a worker latched in ALARM, parity alarms blind on a 401, an 18-day guard counting bytes not
rows, a deploy ledger whose prose disagreed with its gate, and fabric-check calling five held ledgers
"half-landed."

FIX (assert, never detect): new `db-least-priv.sh` -- deterministic + idempotent (unconditional
`REVOKE ALL` + db-scoped `GRANT`, converges from any state) then HARD-VERIFY (`die`, never `|| true`:
shipping an over-privileged public DB user must fail LOUD). `bootstrap-stack.sh` regex->assert;
`harden.sh` section 3.5 runs it; `dispatch.sh` gains the sync entry + a `dbpriv` step. Applied
S3->box (Rule 12). EXERCISED: POST grants = `USAGE ON *.*` (no global priv) + `ALL ON opal_wp.*`; WP
read (`option get siteurl`), write (`option add/get/delete`), DDL (`CREATE/DROP`) all OK under the
scoped grant; site 200 post-change. Commits `f05629cf5` (fix), ledger `nfra-website-db-least-priv`
CLOSED 4/4.

## The RED deploy-ledger -- also a wrong-instrument, at the tooling layer
COO's `deploy_ledger.py check --red` fired RED on `scty-premcp-p1-c1c2-ratelimit-size` (OPEN 58h/8h,
stranded L4), while the rendered ledger `.md` said CLOSED-all-4-legs-proven since 2026-07-07. Both
were "true": the checker reads the `.open_deploys/<slug>.json` SENTINEL, not the `.md`.

MECHANISM (source + git grounded, Rule 22 -- not inferred):
- `cmd_close` (`deploy_ledger.py:298`) does `_state_path(slug).unlink()` -- deletes the sentinel from
  DISK only.
- The sentinel is git-TRACKED. The original closing commit `6813fea08` staged ONLY the `.md`
  (`git show --stat` = 1 file). The deletion was never committed, so the OPEN sentinel survived in HEAD.
- A later restore-from-HEAD (the LD-0262 disarm window) resurrected the pre-close sentinel with
  `L4 proof=null`. `git diff HEAD` on it showed only the checker's own `last_red_at` stamp = a HEAD
  copy. That is the ghost.

DISPOSITION = (a) CLOSED with a FRESH live exercise (I did not trust the `.md`). RE-EXERCISED vs the
live gateway `https://mcp.opalinvest.dev` (Rule 22a):
- EX-A cold-window burst, 25x `GET /authorize` in 1s (single reused connection): reqs 1-20 -> HTTP 400
  (passed the limiter), req 21 -> HTTP 429, `Retry-After: 59`, body `{"error":"rate_limited",
  "scope":"ip"}`. `RL_IP_AUTH_LIMIT=20/60s` fail-closed fires exactly on the 21st.
- EX-B bucket isolation at saturation: `POST /mcp` -> 401 (not 429) -- `ip_auth` vs `ip_global` are
  separate buckets, so an `/authorize` brute-force cannot DoS the bearer-gated `/mcp`.
- EX-C size cap: `POST /mcp` 1.3MiB -> 413 `request_too_large`; sharp control = 12B same endpoint ->
  401. The 413 is `MAX_REQUEST_BYTES` firing, not a generic reject.
- EX-D 413 still deterministic while `ip_auth` saturated.
Committed the sentinel DELETION this time (`c0069c141`, `delete mode`) so it cannot ghost; also
committed the layer2 sentinel's uncommitted HELD conversion (HEAD still said `OPEN` -> a would-be third
false RED). SWEEP: 2 ghosts total this week -- mine + DS~B's `advi-breaks-to3-49f` (both md=CLOSED /
sentinel=OPEN); 4 sentinels tracked-inconsistently. OFFERED COO/CTO a restore-safe fix
(status-flip-not-unlink) -- NOT done unilaterally (it's a NEVER-law gate tool).

## W1 -- all 6 acceptance criteria, each EXERCISED (not config-read)
1. EC2 in Opal VPC, TF-managed, EC2_MANIFEST-registered, ledger closed: i-0152e3fe2599fa630 t3.small,
   vpc-0cc0c6a75e54605e3, instance-profile on; both W1 ledgers CLOSED.
2. WordPress on the EIP: 18.208.18.213 home/wp-login/wp-json all 200 (server: LiteSpeed).
3. Patricia WP-admin: exercised-login proven prior session; email sent 07-09; AWS-console creds held.
4. S3 bucket + IAM role + SG-no-22 + MariaDB-local + LEAST-PRIV: SG 80/443-only zero-22 (live);
   role = SSM-core + opal-website-backups ONLY (firm-sep); bucket versioned + SSE-AES256; MariaDB
   127.0.0.1:3306; DB user least-priv FIXED+EXERCISED; DLM snapshot policy-0c0c24e7981c5522c live
   State=ENABLED (daily/7d, targets opal-website-wp -- a real backup, not a disabled phantom).
5. Old host untouched + live: opalcapital.com apex still 72.167.58.121 (GoDaddy), serving 200 =
   rollback point; no DNS record changed (cutover is W3).
6. Signals grounded (req-5): Cloudflare NOT proxying the apex (resolves to the GoDaddy host, not a
   104.x/172.67.x edge IP -> W3 is a clean apex-A flip; Turnstile is CAPTCHA-only); OpenLiteSpeed is
   the web server (litespeed-cache carries over).

## DR PROVEN (req-4 completeness -- backup that actually restores)
Not "cron installed": ran `backup-to-s3.sh` live -> fresh DB dump `opal_wp_2026-07-09_193638Z.sql.gz`
(2.1MB) + wp-content synced to S3. RESTORE DRILL (non-destructive, scratch DB): restored that dump
into `opal_wp_restoretest` -> 70 tables / wp_options 592 rows / siteurl intact = MATCHES live opal_wp
exactly; dropped scratch; live untouched. mysqldump uses the root socket -> the opal_wp least-priv
change did NOT affect backups (confirmed by this fresh dump+restore).

SMELL (recorded, decision-relevant): the DB grew 22KB (07-08 base install) -> 2.1MB / 70 tables
(base WP is ~12) -- TWLC's dev appears to have STARTED migrating the Bricks site. Two implications:
the old-host-untouched leash matters more now (real content accumulating on AWS), and W3 timing should
wait for migration-done + CVO staging-verify. I own the PLATFORM; I did not touch their content/DNS.

## Two smaller defects (both fixed, c88de96f7)
- EC2_MANIFEST.json had a DUPLICATE `opal-website-wp` key (stale stub instance_id=null + the real
  entry). last-wins hid it, but a first-wins parser reads null. Removed the stub; validated no-dup.
- infra/website README inventory listed Patricia's OLD inline policy; it's been customer-managed
  `website-estate-admin` since 07-09. Updated the row + added the on-box least-priv note.

## Deployment Sequence + Verification (AE)
| Commit | What | Verify |
|---|---|---|
| `c0069c141` | RED ledger L4 close + sentinel deletion + layer2 HELD-sentinel commit | `check --red` exits 0; EX-A/B/C/D transcript |
| `f05629cf5` | least-priv fix (db-least-priv.sh + 3 script edits); --force (MSTR contention, `--only` scoped) | SSM PRE/POST grants; WP read/write/DDL exercise |
| `c88de96f7` | EC2_MANIFEST dedup + README refresh | JSON no-dup validate; live IAM attach re-read |
| `f52897bd9` | ledger nfra-website-db-least-priv CLOSED md | 4/4 legs, L4 exercised |
All pushed to CLOUD. safe-apply not used (no TF change this session -- on-box config via S3->box).

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| comp-grep/native | rail gated my infra `.sh`/`.tf`/manifest greps 3x | routed | 2 were legit shell/json line-reads -> `# rail-checked:` markers; 1 (EC2_MANIFEST) switched to native Grep |
| comp-iam | Patricia standalone IAM user + WP instance role | N/A | comp-iam models lambda service-role->boto3 only (no standalone-user view, confirmed) + Rule 22a mandates LIVE primitives for a fresh IAM change anyway -> rode `aws iam get-role-policy`/`list-attached-*` with markers |
| deploy_ledger.py | RED disposition + new ledger open/close | used | check --red, close-leg x8, close x2, open |

**What worked:** live `aws`/SSM exercises were the authoritative proofs throughout -- SHOW GRANTS +
WP read/write/DDL for least-priv; the 429/413 burst for the rate-limiter; the restore drill for DR.
**What failed:** nothing tool-side. **Gap:** no comp-tool models EC2-on-box state (DB grants, wp-config,
systemd, DLM policy state) or standalone IAM users, or the deploy-ledger sentinel corpus -- all rode
raw `aws`/SSM with `# rail-checked:` markers (logged). The deploy_ledger `cmd_close` deletion-based
close is a structural false-RED source (flagged to COO/CTO, fix offered not taken).

## MCP traffic
COO x6: RED-ledger order -> ACK; disposition (a)-CLOSED + the ghost mechanism; MS-token 3-step block
for Andrew (relayed verbatim, approved); W1-COMPLETE report -> COO independently re-verified 4 ACs +
ACCEPTED + GO W2; W1 DR-addendum (restore drill + migration-underway signal); RAVC-ack of W2 GO +
README-already-done correction.

## Blockers
None. W1 COMPLETE + ACCEPTED. W2 GO'd (TLS/SMTP/backups/hardening) -- starting now. layer2 ledger
correctly HELD on Andrew's MS-token sign-in (steps relayed; L4 exercise mine to run when the cache
exists). Structural deploy_ledger fix awaits COO/CTO GO (gate-tool, not touched unilaterally).

## Next Steps
- **[0.7.0_AE_CloudOps~A]** W2: ground SES state (opalinvest.dev verified? sandbox?) -> wp-mail-smtp
  on an opalinvest.dev sender (Rule 23); certbot/TLS-staging path (no apex DNS change -- W3);
  final-hardening pass; W2 runbook in infra/website/. Each live step gets its own deploy-ledger.
- **[Andrew]** sign in once at https://mcp.opalinvest.dev/login as a non-admin identity -> unblocks my
  layer2 L4 live-403 exercise. W3 (GoDaddy apex-A -> EIP) remains his DNS-gated call.
- **[2.0.0_SA_COO / CTO]** decision on the restore-safe deploy_ledger cmd_close fix (false-RED ghost
  class; bit twice this week).
