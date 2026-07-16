# Session close 1935-2125Z (~A lane) -- NFRA_WEBSITE GO-LIVE: apex cutover COMPLETE, plus two live defects found by Andrew's questions (not by the plan)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

**Agent:** 0.7.0_AE_CloudOps~A | **Session:** 2026-07-16 19:35Z start (fresh lane session) | **Window:** start -> 21:25Z
**Authorization:** Andrew-direct, mid-startup, VERBATIM: *"You are going to be working on NFRA_WEBSITE. Today is the go live day. We have a call with Patricia in 25 minutes. I want you to assess status, refresh your memory on the recent logs and her and my correspondence on outlook, and make sure we are good to go here."* Recorded + broadcast same turn (COO/CTO/MSTR 19:43Z); CTO ACK 19:45Z ("nothing at my gate blocks the call").

## HEADLINE

**`https://opalinvest.com` IS LIVE ON AWS.** The Wix site is replaced; the apex + `www` serve the Bricks WordPress site from `i-0152e3fe2599fa630` @ `18.208.18.213` over a trusted LE cert that **auto-renews (proven, not assumed)**. Deploy ledger `20260716T1948Z_nfra-website-phaseB-cutover` CLOSED 10/10 @ `2afa00817`.

**The two most valuable outputs of this window were NOT on the plan** -- both were live user-visible defects surfaced by Andrew asking an ordinary question, and **both were initially concealed by an instrument of MINE that returned green.**

## 1. PHASE B APEX CUTOVER -- EXECUTED + VERIFIED (ledger 10/10)

Pre-call verification (19:35-19:45Z, all measured live, none assumed): staging 200 strict-TLS; apex A x3 + `www` CNAME **TTL=600 measured at ns47** (Patricia lowered them 07-15 21:28Z); apex still on Wix; deployed `tls-cutover.sh` S3 ETag == repo md5.

| Leg | Outcome |
|---|---|
| B1 issue (DNS-01) | cert `CN=opalinvest.com`, LE/YE2, notAfter **Oct 14 2026**, SAN = apex + www + new |
| B2 TXT adds | **Only TWO codes needed, not three** -- the `new.opalinvest.com` authz was still valid from the Phase-A HTTP-01 cert, so LE did not re-challenge it. Both verified exact-match at ns47 AND 8.8.8.8 before LE polled. |
| B3 backup | `2026-07-16_201955Z` -> s3://opal-website-backups/backups/db/ + /wp-content/ |
| B4 re-key | dry-run 938 -> live 938; residual `new.opalinvest.com` = **0**; siteurl+home re-read = `https://opalinvest.com` |
| B5 wire+verify | positive control 200 + box-pinned 200 + **SAN assert apex AND www** -> GO issued |
| B6 THE FLIP | Patricia deleted 2 of 3 Wix A rows + repointed the third -> apex A = `18.208.18.213`; confirmed ns47 + 8.8.8.8 |
| B7 blog_public=1 | re-read = 1 (site is NOT launched noindex) |
| B9 convert-renewal | webroot re-issue + **`certbot renew --dry-run` PASSES** -- the manual DNS-01 cert can now actually renew |
| B10 external verify | apex 200 / `ssl_verify_result=0` / ip=18.208.18.213 / real Bricks title; www 301 -> apex (TLS rc=0, followed -> 200); http 301 -> https |

**Fix shipped mid-flight @ `3a6cc9da9`:** `tls-cutover.sh issue` failed rc=1 on its first Phase-B run -- certbot saw the Phase-A staging cert as a **subset match** and raised its expand-or-not prompt, which under `--non-interactive` is a hard failure. Cured with `--cert-name "$DOMAIN"` (fresh pinned lineage; also leaves the staging cert wired as fallback until `wire` swaps it). Same pin applied to `convert-renewal`. S3 ETag `1f1bce0c` == repo.

**ROLLBACK (still live, ~10 min at 600s TTL):** point apex A back to `185.230.63.107/.171/.186`. Wix was never touched.

## 2. >> B11 -- P1 LIVE MAIL DEFECT: EVERY CONTACT-FORM EMAIL WAS SILENTLY DYING <<

**Trigger:** Andrew asked *"if somebody sends an email on one of the contact forms on the page, what email does that go to?"* -- an orientation question, not a bug report.

**Answer to his question:** `andrew@opalinvest.com` (GF form 1 "Contact", 2 active notifications: `{admin_email}` + a literal). `wp-mail-smtp` `from_email_force=true` rewrites GF's `no-reply@opalinvest.com` From to `noreply@opalinvest.dev` -- which is exactly what the instance role's `ses:FromAddress` condition permits. **Rule 23 clean.**

**But it did not arrive.** `/var/log/opal-website-ses-sendmail.log` carried `aws: command not found` **x2 at 20:39:51Z (bytes=5075 x2 = BOTH notifications)** -- **Patricia's live go-live test submission** (GF entry 1, 20:39:51, ip 68.200.202.19, "Testing 123") **saved to the DB and its notifications were SILENTLY LOST.** Same failure 2026-07-12T19:00:53Z. The visitor still sees the form's success message.

**MECHANISM (source + measured, not inferred):** `ses-sendmail` called **bare `aws`**. lsphp's runtime PATH is **`/bin:/usr/bin`** (measured: `tr '\0' '\n' < /proc/<lsphp>/environ`); the CLI is at `/usr/local/bin/aws`. So the shim resolved `aws` ONLY from a root/login shell.

### >> THE INSTRUMENT THAT LIED (#1): MY FIRST TEST PASSED. <<

`wp --allow-root eval "wp_mail(...)"` returned `bool(true)` and logged `OK msgid=...` -- **because wp-cli runs as ROOT with `/usr/local/bin` on PATH.** That test **could not fail the way production fails**: it exercised a different PATH than the web server's. Had I stopped at the green, I would have reported "forms work" **on go-live day** while every real submission died. **What caught it was reading the log's own ERROR lines -- not the passing test.** (CLAUDE.md 22a: *care is not a control*; an instrument that cannot fail is not an instrument.)

**FIX @ `992ec0d31`:** absolute-path resolution (`/usr/local/bin/aws` + PATH-explicit fallback + loud fail-closed if absent). Authored in-repo (Rule 12, never on the VM); S3 ETag `632e3c74` == repo md5 == deployed md5.

**PROVEN IN THE FAILING CONTEXT (the only test that counts):** `su nobody` + `env -i PATH=/bin:/usr/bin` + lsphp -> the shim **reached SES** and returned a real SES API error on a deliberately-empty probe (`InvalidParameterValue: Missing final '@domain'`, 20:50:07Z) -- i.e. the CLI was FOUND and INVOKED where it previously was not. Then Patricia's real entry-1 notifications were **resent and DELIVERED**: `20:52:03Z OK bytes=5071 msgid=0100019f6cb362b7-...` + `20:52:05Z OK bytes=5075 msgid=0100019f6cb36902-...`.

## 3. >> BRICKS CSS MIXED-CONTENT: THE THUMBNAILS A DB SEARCH-REPLACE CANNOT REACH <<

**Trigger:** Andrew noticed the banner videos looked static vs the `new.` preview; then relayed Patricia: *"there should be a thumbnail there not just a gray box with a play icon."*

**Rendered in a real browser (Playwright) -- 2 console errors:**
```
Mixed Content: page loaded over HTTPS, but requested an insecure image
'http://18.208.18.213/wp-content/uploads/2026/06/video-poster-ceoconvo-1024x565.webp'
-> This request has been blocked
```

**THE HUNT (and why every DB check said the site was clean):**
- `wp search-replace '18.208.18.213' --all-tables --dry-run` -> **0**. Plain form -> 0. **Escaped-slash form (`http:\/\/`) -> 0.** The DB was genuinely clean.
- Raw IP in served HTML -> **0**. Same under a Chrome UA (ruled out an LSCache UA-variant). Same bytes, same cache stamp.
- **FOUND ON DISK:** `grep -rl` over `wp-content/` -> `uploads/bricks/css/post-2.min.css` + `post-90.min.css`.

**MECHANISM (source-confirmed):** **Bricks compiles CSS to FILES on disk with absolute URLs baked in at generation time.** Those files were generated while the site was keyed to the raw IP. **A DB search-replace cannot touch files** -- so the re-key (correctly reporting residual 0) left them behind. `post-2.min.css` IS loaded by the homepage and contained:
```css
#brxe-qqxwjc {background-image: url("http://18.208.18.213/.../video-poster-ceoconvo-1024x565.webp")}
#brxe-fzwewn {background-image: url("http://18.208.18.213/.../video-poster-exist-1024x569.webp")}
```
These are the **Vimeo facade thumbnails** (the small videos are Vimeo embeds; the hero is a separate Bricks background video). Blocked as insecure -> background never paints -> **gray box + play icon, no thumbnail.** Exactly Patricia's report.

**FIX (zero material change -- same images, correct address):** backed up `uploads/bricks/css/` -> `/tmp/bricks-css-backup-20260716` (18 files), then invoked Bricks' OWN supported mechanism `Bricks\Assets_Files::regenerate_css_files()` (rebuilds from the clean DB), then LSCache purge all.

**VERIFIED IN A REAL BROWSER (not a config read):** console **0 errors / 0 warnings** (was 2/2); computed `background-image` on both elements now `https://opalinvest.com/...`; `insecure_refs_in_dom` = **0**; and the hero video measured **actually playing**: `paused:false, currentTime:17.66, loop:true, muted:true, readyState:4`.

### >> THE INSTRUMENT THAT LIED (#2): I NEARLY REPORTED A SITE-WIDE CSS OUTAGE. <<

Post-regeneration I ran a loop that reported **every Bricks CSS 404** -- I was one step from escalating "the live site lost its styling." **ANDREW CAUGHT IT: *"I think something in your query is wrong, it looks fine on my device."*** He was right. My grep captured paths as `uploads/bricks/css/...` and I pasted them onto the domain **without the `wp-content/` prefix** -- I was fetching URLs that never existed. The *same output* contained the disproof (`post-2.min.css -> HTTP 200` from a correctly-formed direct fetch) and I had not read it. **Two false instruments in one session, both mine, both green/red in the wrong direction; the human caught the second one.** The lesson is not "be careful" -- it is that a constructed URL is a hypothesis and needs a positive control (a URL known to exist) before its 404 is a finding.

## 4. ANDREW DESIGN CALLS THIS WINDOW (recorded; I surfaced, he ruled)

- **`dev.opalinvest.com` as a hidden admin URL -- PROPOSED BY ANDREW, CORRECTLY DROPPED.** Stated goal: *"a custom wp-admin address... not so obvious... too obvious for bad actors."* **I pushed back with two grounds: (a) a subdomain does not REMOVE `opalinvest.com/wp-admin` -- it adds a second door beside the obvious one; (b) EVERY CERT WE ISSUE IS PUBLISHED TO PUBLIC CERTIFICATE TRANSPARENCY LOGS (crt.sh) -- `new.opalinvest.com` is already listed there from today's cert, so a `dev` subdomain would be ADVERTISED to exactly the people it is meant to hide from.** The tool that actually does this is `wps-hide-login` (present in the original backup's plugin inventory, **NOT installed on the box**; only `wps-limit-login` is active). Andrew ruled: **"no we dont have to go that far, its fine for now at /wp-admin."** NOTHING INSTALLED, no change made.
- **Isolated staging copy at `dev.opalinvest.com` -- ASKED, THEN WITHDRAWN.** Andrew initially chose a real second WP (own DB/docroot/vhost/cert); I surveyed the box (25G free, WP 340M, one `wordpress` vhost, single `opal_wp` DB) and had authored nothing when he withdrew it: *"nevermind we just need the friendly admin approach."* **Nothing built, nothing to unwind.** Grounding that informed the fork: there is exactly ONE WordPress -- any hostname on that box lands on the SAME site (`new.opalinvest.com/wp-admin/` was measured 302 -> `opalinvest.com/wp-login.php`), so a `dev` alias would be the PRODUCTION admin under a different name, with zero isolation.

## 5. >> RESIDUALS -- SURFACED, NOT CLOSED. NONE ARE BLOCKING. <<

- **THE HERO VIDEO IS NOT OURS AND IS NOT ON OUR INFRASTRUCTURE.** The homepage background video is served from **`https://ewd.nyc3.cdn.digitaloceanspaces.com/opalcapital/home-hero-broll.mp4`** -- **`ewd` = Exton Web Design** (Mike, `mike@extonwebdesign.com`), a **DigitalOcean Spaces CDN bucket we do not own, do not pay for, cannot monitor, and cannot restore.** Measured reachable today (HTTP 200/206, `video/mp4`). **Opal's homepage hero depends on a third party's object storage staying up and staying paid -- and that third party is the same outside developer who currently holds a FULL ADMIN account on the live site (below).** This is the *"the estate has instruments for what is DEPLOYED and zero for what is OURS"* class (Rule 23's lesson, different domain): no freshness alarm, no IAM, no bucket policy of ours touches it, and **no instrument we own would tell us if it vanished** -- the first detector would be a visitor seeing a blank hero. Note also the path segment is `opalcapital/` -- the domain we do NOT own. **CURE (small, own window): copy the asset into `wp-content/uploads/` (or an Opal-owned bucket) and re-point the Bricks background-video URL.** Not done -- it is a content change on a live site inside a go-live window, and Andrew closed the session. **Route with CTO.**
- **SES IS STILL IN SANDBOX** (`ProductionAccess: false`; 200 msg/24h; `MaxSendRate` 1/s). Admin notifications work **ONLY because `andrew@opalinvest.com` is a verified identity**. **Any notification to an UNVERIFIED recipient WILL be rejected** -- there is no submitter auto-reply on form 1 today, so the contact form is unaffected, but this is a live constraint on a **public** website and the next person who adds an auto-reply will ship a silent failure. Precedent already in the log: `2026-07-13T22:16:39Z MessageRejected ... mike@hirst.digital` -- the sandbox has already eaten a real send. **CURE: production-access request. Route with CTO.**
- **`mike@extonwebdesign.com` HOLDS FULL ADMIN** on the live public site (outside developer). Roster: `opaladmin`/andrew@opalinvest.com, `patricia@thewhitelabelcreative.com`, `Lindsay@thewhitelabelcreative.com`, `mike`/mike@extonwebdesign.com. **Same identity class as the `mike@hirst.digital` shadow slot deleted 07-13 (W3 B2 -- which had held a live confirmation link that would have silently reverted the admin_email fix).** Ledger leg B8 = **SURFACED-OPEN, deliberately NOT actioned**: deleting users is destructive and Andrew's word governs. **Awaiting Andrew.**
- **Weak credential on a live public `/wp-admin`.** `whitelabel7` was authored for a private raw-IP box; it is now the admin password on Opal's public website, at the standard path, **with no hide-login plugin active** (`wps-limit-login` IS active, so brute force does get locked out -- that is the real protection and it is present). **ALSO: the briefing Andrew holds is STALE -- the user_login is `patricia@thewhitelabelcreative.com`, NOT `patricia`** (changed when he fixed her email in the user table 07-14). A stale credential note reads as a broken login. Surfaced.
- **This defect class may not be homepage-only.** The Bricks CSS regeneration rebuilt **all** files (18 -> 16; two stale orphans for non-existent posts dropped), so other pages were likely swept -- but I only *verified* the homepage. Worth a click-through of the main pages.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-pulse / risk-reflex | auto in safe-commit x3 | PASS (CLEAN) | measured, denominator printed (1 file vs 1239 danger nodes); danger map STALE 61-62h on every run -- noted, not blocking |
| comp-surface-check | auto in safe-commit x3 | OK | 1 changed file, no critical surface (advisory-only per Rule 20 -- read, not assumed) |
| comp-which / comp-grep | not used this window | -- | **Gap, stated plainly:** this window was ~entirely LIVE-STATE work (AWS/SSM/DNS/box filesystem/browser render) where the graph has no model -- the rail's own principle. The two repo searches I did run (`grep -n` over RUNBOOK, `grep` over tls-cutover.sh) were narrow reads of files already in hand; a comp-grep would have been the better reflex and I did not reach for it. Raw `aws` inspections carried `# rail-checked:` markers where required (instance-state, S3 single-artifact parity). |

**What worked:** the ledger's open-at-start/close-with-evidence discipline caught nothing (nothing half-landed) but made the B11 write-up trivial; `tls-cutover.sh`'s fail-closed design refused correctly at every gate and its **SAN assert** is what made the flip safe; the Playwright render is the ONLY instrument that found the mixed-content block -- **no config read, DB query, or curl of the HTML could have** (all three returned clean).
**What failed:** BOTH of my own ad-hoc verification instruments (root-context wp_mail test -> false GREEN; malformed-URL CSS sweep -> false RED). Neither was a comp tool; both were hand-rolled one-liners. **That is the pattern worth banking: the tools with controls behaved; the tools I improvised under time pressure on a live call are the ones that lied.**
**Gap found:** no comp tool renders a page and reads its console -- the class of defect that is invisible to source, DB, and HTTP-response inspection (mixed content, blocked resources, JS-injected media). `/frontend-dev` exists for portal but nothing covers the WordPress estate. **Tool candidate for CTO.**

## Deployment Sequence + Verification (AE)

- **Repo -> S3 -> box, every time (Rule 12); ETag-vs-md5 verified on every upload, never a `--quiet` rc=0:**
  - `tls-cutover.sh` @ `3a6cc9da9` -> S3 ETag `1f1bce0cf192d6c43caa96bcca9eed40` == repo md5.
  - `ses-sendmail.sh` @ `992ec0d31` -> S3 ETag `632e3c7465883cd238f49bb8a599c09f` == repo md5 == **on-box deployed md5** (all three pinned).
- **No Terraform, no Lambda, no `update-function-code` this window.** All box work via SSM RunShellScript (pull-from-S3-then-run). Zero code authored on the VM.
- **Pasted verification (actual output, abbreviated):**
  - `subject=CN = opalinvest.com / issuer=C = US, O = Let's Encrypt, CN = YE2 / notAfter=Oct 14 19:18:33 2026 GMT`
  - `covers opalinvest.com: yes` / `covers www.opalinvest.com: yes` / `OK: the apex flip is SAFE to make.`
  - `Congratulations, all simulated renewals succeeded: /etc/letsencrypt/live/opalinvest.com/fullchain.pem (success)`
  - `https://opalinvest.com -> HTTP 200 | TLS verify rc=0 | ip=18.208.18.213`
  - Playwright: `Total messages: 0 (Errors: 0, Warnings: 0)`; `hero_video {paused:false, currentTime:17.66}`

## MCP traffic

6 significant: Andrew-direct verbatim record broadcast x3 (COO/CTO/MSTR 19:43-19:50Z); **CTO ACK 19:45Z** -- gate clear, offered live arch word mid-call, ledger discipline noted; my ACK-of-ACK 19:45Z. No GOs issued, no RAVC left open.

## Blockers

**None.** Nothing half-landed; the deploy ledger is CLOSED 10/10 with evidence; no stranded leg; tree clean; rollback path live and documented. B8 (admin roster) is **SURFACED-OPEN awaiting Andrew's word** -- an owner decision, not a blocker.

## Current State (zero-context handoff)

- **`https://opalinvest.com` is LIVE on AWS** -- box `i-0152e3fe2599fa630` (t3.small, EIP `18.208.18.213`), OpenLiteSpeed + lsphp82 + local MariaDB (`opal_wp`), docroot `/usr/local/lsws/wordpress`. Apex A = single row -> `18.208.18.213`; `www` CNAME -> apex; TTL 600.
- **Cert:** `/etc/letsencrypt/live/opalinvest.com/` -- CN=opalinvest.com, SAN apex+www+new, notAfter **2026-10-14**, renewal **converted to webroot/HTTP-01 and dry-run PROVEN**. (A second lineage `new.opalinvest.com` also exists and also renews clean.)
- **Mail:** WP -> `php.ini sendmail_path` -> `/usr/local/bin/ses-sendmail` (md5 `632e3c74`) -> `aws ses send-raw-email` via instance role (no stored secret). From forced to `noreply@opalinvest.dev` by wp-mail-smtp; SES `ses:FromAddress` condition enforces it. **Log to watch: `/var/log/opal-website-ses-sendmail.log` -- an `ERROR` line there IS a lost email.**
- **Backups:** `s3://opal-website-backups/backups/{db,wp-content}/<date>/`; nightly cron `opal-website-backup`; pre-flip set = `2026-07-16_201955Z`. Bricks CSS pre-regen backup: `/tmp/bricks-css-backup-20260716` (**ephemeral -- /tmp, will not survive a reboot; the DB is the real source and it is clean**).
- **Code (all repo-authored):** `infra/aws/ec2/website/{tls-cutover,ses-sendmail,backup-to-s3,bootstrap-stack,harden,create-wp-admin,db-least-priv,tls-prep,dispatch}.sh` -> `s3://opal-website-backups/code/website/`. Procedure/gates/rollback: `infra/website/RUNBOOK.md` §4.
- **Ledger:** `org/critical_paths/change_management/20260716T1948Z_nfra-website-phaseB-cutover_deploy_completion.md` @ `2afa00817` (10 legs + B11 narrative + residuals).
- **Third-party surface (NOT ours):** homepage hero video @ `ewd.nyc3.cdn.digitaloceanspaces.com/opalcapital/home-hero-broll.mp4` (Exton Web Design's DO Spaces). Small videos = Vimeo embeds w/ our own `.webp` facade thumbnails (now serving correctly over HTTPS).
- **Pre-existing ~A queue, unchanged and event-gated:** DC1 orion-crawl + DC2 eclipse-crawl TOs; `OPAL_STNDRD.Z1`; `NFRA_COMPLEARN.AMD-P3a`; 22:00Z ETF AC3 cloud-guard verdict (a FAIL re-enables the laptop leg); 03:05Z 2026-07-17 bd49f maiden fire -> `[0.4.0_DS_ClientPlatform~B]`.

## Next Steps

- **[Andrew, RESERVED]** (a) `mike@extonwebdesign.com` full-admin disposition (ledger B8); (b) `whitelabel7` rotation + relay the CORRECT username `patricia@thewhitelabelcreative.com`; (c) whether to pull the hero video onto Opal-owned storage.
- **[1.0.0_SA_CTO]** route two residuals: **SES production-access request** (sandbox is a live constraint on a public site -- 200/day, verified-recipients-only) and the **hero-video third-party-CDN dependency** (an Opal-owned asset with no instrument pointed at it today).
- **[0.7.0_AE_CloudOps~A]** on Andrew's word: hero-video re-host (copy asset -> re-point Bricks background-video URL -> regenerate CSS -> verify render). Also worth one pass: click-through of main pages to confirm the CSS regeneration swept every stale generated file (homepage VERIFIED; others INFERRED from the all-files regen -- **that distinction is the finding, not a formality**).
- **[any agent]** two banked lessons: (1) **a test that runs as root cannot verify a path the web server takes** -- exercise the failing context or you are measuring yourself; (2) **a constructed URL is a hypothesis** -- run a positive control (a URL known to exist) before a 404 becomes a finding. Andrew caught #2 from his phone before I escalated it.
