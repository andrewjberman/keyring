# AMGT_RESAPP task order -- `AMGT-rk-122` -- ONE `ordered_cache_behavior` for `/api/scoped/amgt/*` on distribution `EVTSA9VEHNZVH`, so the Security Analysis page's 16 mounted routes stop falling through to the SPA origin; SERVED INFRA, under a pair, and THE APPLY IS ROUTED (this seat's lane is REFUSED, measured)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-122</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~122</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence and runs no producer. It
  adds ONE CloudFront cache behavior.
comp-iam: DECLARED-NOT-APPLICABLE for a GRANT CHANGE -- no role, policy or trust is edited. The behavior ATTACHES the
  EXISTING `auth-validator-edge:20` viewer-request association that every sibling scoped family already carries; it
  mints nothing. AWS reads in AC0/AC3 run under the seat's existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~122`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`infra/aws/terraform/portal-auth/cloudfront-distribution.tf`, `.tools/safe-apply.sh` and `.tools/deploy_ledger.py`
exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~122;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-122` (round 30, row `AMGT_RESAPP-Z-S226`, ARMED)

**The ruling of record, verbatim** (`1.0.0_SA_CTO~Z` msg 24353, 2026-09-22T19:10:50Z):

> ADD rk-122 TO ROUND 30 -- the defect blanking the page (row Z-S226, ARMED):
> - There is NO CDN behavior for /api/scoped/amgt/*, so all 10 page requests fall to the SPA origin and return 200
>   text/html. Measured by me live on opalinvest.dev, with /api/scoped/advisor-intelligence/* and /api/general/*
>   returning 401 JSON as positive controls.
> - The cell adds the behavior at the API origin and MUST carry the same auth-validator edge attachment the working
>   families use, or it trades a blank page for a 401.
> - It is a SERVED infra act: CTO/COO pair, a deploy-ledger entry opened before the apply, and `safe-apply`, never a
>   bare terraform apply.
> - READ THE MODULE'S OWNED-PATHS LANE BEFORE THE APPLY. If the lane refuses your seat, route the apply to the AE/DT
>   seat through 0.0.0_AB_MSTR~Z rather than overriding.
> - Verify with BA_US_Equity first (7 of 7 prefixes populated), then 992_HK_Equity.

**THE MEASURED STATE at SITEZ HEAD (the issuer's own reads, 2026-09-22 ~19:2xZ). RE-READ every line at your branch
HEAD before editing:**

- **The resource:** `aws_cloudfront_distribution.portal`, declared at
  `infra/aws/terraform/portal-auth/cloudfront-distribution.tf:103`. Distribution id `EVTSA9VEHNZVH`, aliases
  `opalinvest.dev` and `www.opalinvest.dev`, Status `Deployed`.
- **The declared list:** `path_pattern` appears **28 times** in that file (comp-read enumerate, 28 of 28 whole-value).
  The live `CacheBehaviors.Quantity` is **28**, and **0** of the 28 contain `amgt`. Declared and live AGREE, so the
  file is the source of truth for this act.
- **THE TEMPLATE IS BEHAVIOR 15, `:898-933`, `/api/scoped/investor-reporting/*`** -- the SAME class of fix, landed
  2026-09-11. Its own comment records that before it existed the prefix returned `200 text/html`, 1068 bytes of
  index.html. Copy it EXACTLY and change ONLY the path pattern and the comment:
  - `target_origin_id = "APIGateway-portal"`;
  - `viewer_protocol_policy = "redirect-to-https"`;
  - `allowed_methods = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]` (the page has 3 POST routes);
  - `cached_methods = ["GET", "HEAD"]`; `compress = true`;
  - `cache_policy_id = data.aws_cloudfront_cache_policy.caching_disabled.id` (live id `4135ea2d-...`,
    Managed-CachingDisabled -- these are per-viewer scoped answers and must NEVER be cached at the edge);
  - `origin_request_policy_id = data.aws_cloudfront_origin_request_policy.all_viewer_except_host.id` (live `b689b0a8-...`);
  - ONE `lambda_function_association`, `event_type = "viewer-request"`, `lambda_arn = local.auth_validator_edge_arn`,
    `include_body = false`. **Live, both `/api/scoped/partners/*` and `/api/scoped/investor-reporting/*` carry exactly
    `auth-validator-edge:20` and nothing else.** That is the attachment the CTO's ruling names.
- **APPEND AT THE END OF THE ORDERED LIST.** `ordered_cache_behavior` is a LIST and its order IS CloudFront's
  precedence. Inserting in the middle shifts every later block and the plan would show changes this cell must not
  touch. Appending shifts nothing, and `/api/scoped/amgt/*` is disjoint from all 28 existing patterns (there is no
  `/api/*` or `/api/scoped/*` catch-all above it -- verify that yourself from the enumerate before you edit).
- **The API side is already complete:** the portal API `7k3ed8px20` (= the `APIGateway-portal` origin domain
  `7k3ed8px20.execute-api.us-east-1.amazonaws.com`) carries **16 amgt routes of 101 total**, and
  `infra/aws/terraform/harvest/scoped-amgt-api.tf:353,364` mounts them on `local.portal_api_id`, which
  `infra/aws/terraform/harvest/main.tf:100` sets to `"7k3ed8px20"`. **Only the edge route is missing.**
- **The defect, reproduced by the issuer** (live GET, no auth header):

  | path | status | content-type | bytes |
  |---|---|---|---|
  | `/api/scoped/amgt/lists` | 200 | text/html | 1000 |
  | `/api/scoped/amgt/freshness` | 200 | text/html | 1000 |
  | `/api/scoped/amgt/security/BA_US_Equity/thesis` | 200 | text/html | 1000 |
  | `/api/scoped/amgt/security/992_HK_Equity/thesis` | 200 | text/html | 1000 |
  | `/api/scoped/advisor-intelligence/summary` (CONTROL) | 401 | application/json | 51 |
  | `/api/general/health` (CONTROL) | 401 | application/json | 51 |
  | `/api/scoped/investor-reporting/x` (CONTROL) | 401 | application/json | 51 |
  | `/api/scoped/partners/x` (CONTROL) | 401 | application/json | 51 |

- **THE LANE, MEASURED BY THE ISSUER BY EXERCISING THE GATE ITSELF** (`.tools/git-hooks/owned-paths-check.sh`,
  `OWNED_PATHS_MODE=block`, staged = the one `.tf`), four serials, both directions:

  | serial | verdict |
  |---|---|
  | `0.7.0_AE_CloudOps` | **PERMIT** (the positive control -- the lane is real and the harness discriminates) |
  | `2.0.0_SA_COO~Z` | REFUSE -- `not in permitted_agents` |
  | `0.2.0_DT_PortfolioAnalytics` | REFUSE -- `not in permitted_agents` |
  | `0.9.0_WK_AMGT_RESAPP~122` | REFUSE -- `WORKER: no NON-TERMINAL task order at HEAD ... names this path` |

  `infra/aws/**` resolves to lane `CLOUD_OPS_OR_ETL` (`.owned-paths.yaml:1906`), whose members are the AE set
  (`0.5.0_AE_OpalETL`, `0.6.x_AE_PartnerETL`, `0.7.0_AE_CloudOps[~A~B~C]`, `0.8.0_AE_CloudComp`, `4.0.0_SA_CRO~SWEEP`).
  **So CASE B of the CTO's ruling applies: the lane refuses this seat, and the commit of the `.tf` AND the apply are
  ROUTED to an AE seat through `0.0.0_AB_MSTR~Z`. This order does NOT name the `.tf` in its `<paths>`, deliberately**
  -- see the record face for why that is a decision and not an omission.

**RULED, what you build:**

1. **In your worktree only**, append the one `ordered_cache_behavior` block to
   `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`, immediately after behavior 15 and before the
   `# --- Custom Error Responses ---` comment. Copy behavior 15 field-for-field; change ONLY `path_pattern` to
   `"/api/scoped/amgt/*"` and the leading comment (which names this cell, row Z-S226, and the append-at-end reason).
   **You will NOT commit this file** (AC2). Editing is not committing; the lane gate is commit-time.
2. Write the exact hunk to your deliverables dir as `rk122_amgt_behavior.patch` (`git diff` output for that one file),
   which is the artifact the routed AE seat applies. THIS is your deliverable.
3. Run the plan and prove its SHAPE (AC1).
4. Write `rk122_handoff.md` in your deliverables dir: the patch path, the exact commit command an AE seat runs, the
   exact `safe-apply` command, the ledger slug, and the post-apply verification commands (AC3's script), so the routed
   seat needs nothing from you but the file.

**What this cell does NOT change:** every other behavior, origin, cache policy, WAF rule, Lambda@Edge function or
version; the API Gateway routes (already mounted); the adapter; the portal bundle; any S3 object. **It does not touch
`Z-S227`** (0 of 5 tabs carry an isError branch) -- that is a separate defect with its own remedy and rides a later
frontend cell.

## 2. WHERE THIS CAME FROM

**ROUND 30**, decomposition s.38 (cut by `2.0.0_SA_COO~Z`), on the CTO's ruling msg 24353, itself on Andrew's report
at ~18:2xZ (record `@1fd5d2ba3f`): *"I just visual smoked the Security Analysis portal page, nothing loads."* Row
`AMGT_RESAPP-Z-S226` is the finding; `2.0.0_SA_COO~Z`'s direct Lambda invokes (msg 24327) proved the handler healthy,
which is what separated the edge route from everything behind it.

## 3. SURFACES -- what you may read and write

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-122.amgt-edge-behavior.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` is
  DELIBERATELY ABSENT: you EDIT it in your worktree to produce the patch and the plan, and you NEVER commit it. Reads
  need no grant. Scratch is `<your worktree>/.scratch/r122/` only, never committed.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~122 <0.9.0_WK_AMGT_RESAPP~122@opal.agent>" -F <msgfile> -- <paths>`
  with the message file written by the Write tool. Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

- **YOU DO NOT APPLY, AND YOU DO NOT COMMIT THE `.tf`.** Both are routed to an AE seat via `0.0.0_AB_MSTR~Z`. If you
  believe you can commit it, STOP with a BLOCKING row instead -- a lane that admits you would mean the order granted
  it, which this order deliberately does not.
- **NEVER a bare `terraform apply`.** The routed act uses
  `HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply -target=aws_cloudfront_distribution.portal`.
  A fresh worktree needs `terraform -chdir=infra/aws/terraform/portal-auth init -input=false` before any plan (row
  W94-S1). The init writes only the local `.terraform/` directory.
- **THE PLAN BOUND, widened EXACTLY as the precedent's CTO ruling widened it, and no further.** The predecessor act
  (IRPT IB-s-15, ledger `20260911T0855Z_irpt-bckend-s15-cloudfront`) was REFUSED BY ITS OWN GATE because the
  portal-auth plan carries resources that cell did not own. Its successful resume
  (`20260911T0940Z_irpt-bckend-s15-cloudfront-2`) ran under: **"ONE change plus the classified WAF read-normalisation
  no-op"**. So:
  - **CONFORMS (Branch A):** `Plan: 0 to add, 2 to change, 0 to destroy` naming ONLY
    `aws_cloudfront_distribution.portal` (exactly ONE `+ ordered_cache_behavior`, 0 removed, 0 modified) and
    `aws_wafv2_web_acl.opal_cloudfront_protection` (3 managed-rule blocks removed and 3 re-added, the SAME rule-name
    set on both sides, and a field-by-field diff of all 6 visible fields per block showing ZERO differing fields --
    the only hidden attribute is `version`, `''` vs `null`). **You must PRINT that field-by-field diff; asserting the
    no-op without it is not evidence.**
  - `Plan: 0 to add, 1 to change, 0 to destroy` naming only the distribution CONFORMS a fortiori.
  - **ANY other resource, or any second changed attribute on the distribution, is Branch B: STOP, no apply, a BLOCKING
    row.** In particular `aws_cloudfront_function.spa_fallback` appeared in the predecessor's refused plan as a CRLF
    checkout artifact. **The issuer measured it clean today** (`spa-fallback-function.js`: disk 0 CRLF / 26 LF, HEAD
    blob identical, `disk == HEAD` True), so it should be ABSENT from your plan -- if it appears, that is Branch B and
    a row, never a normalisation you perform.
- **Deploy ledger:** the ROUTED seat opens it BEFORE the apply --
  `python .tools/deploy_ledger.py open --slug amgt-rk122-edge-behavior --title "<title>" --author "<the AE serial>"`
  (the tool takes `--slug --title --author` and `--leg` or `--lambda`; there is NO `--legs`) -- and closes it on the
  AC3 read. Your handoff names the slug and every leg.
- **Rollback, per key, NEVER a delete:** remove the one behavior block in a NEW commit and run the SAME targeted
  apply; the live `CacheBehaviors.Quantity` returns to its AC0 value and the amgt pattern count returns to 0. **The
  distribution is NEVER deleted or disabled.** State in your handoff that a CloudFront update propagates globally
  (the predecessor's apply took 47s to return and the distribution then read `Deployed`), and that a WARM EDGE may
  serve the prior answer briefly, so a single post-apply read that still shows HTML is re-read once before it is
  called a failure -- and that a rollback carries the same propagation window.
- **THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
  repaired, widened, or satisfied by a route this order did not name, and never by editing a WALL.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W122-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`;
  append by textual splice inside the one fenced JSON array; never edit an existing row; `disarm_owner` is
  `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; each runs under timeout 600)

**Script files.** Write each block to the named file under `<your worktree>/.scratch/r122/`, byte-for-byte.

`.scratch/r122/ac0.py`:
```
import boto3, json, os, subprocess, urllib.request, urllib.error
cf = boto3.client("cloudfront", region_name="us-east-1")
cfg = cf.get_distribution_config(Id="EVTSA9VEHNZVH")
obs = cfg["DistributionConfig"]["CacheBehaviors"]
pats = [b["PathPattern"] for b in obs.get("Items", [])]
print("live_behaviors", obs["Quantity"], "amgt", sum(1 for p in pats if "amgt" in p))
print("patterns", json.dumps(pats))
src = open("infra/aws/terraform/portal-auth/cloudfront-distribution.tf", "rb").read().decode("utf-8")
print("declared_path_pattern", src.count("path_pattern"))
for who in ("0.7.0_AE_CloudOps", "2.0.0_SA_COO~Z", "0.9.0_WK_AMGT_RESAPP~122"):
    env = dict(os.environ)
    env["GIT_AUTHOR_NAME"] = who
    env["OWNED_PATHS_MODE"] = "block"
    env["OWNED_PATHS_STAGED_FILES"] = "infra/aws/terraform/portal-auth/cloudfront-distribution.tf"
    env["OWNED_PATHS_AUDIT_LOG"] = ".scratch/r122/lane.log"
    r = subprocess.run(["bash", ".tools/git-hooks/owned-paths-check.sh"], capture_output=True, text=True, env=env)
    print("lane", who, "PERMIT" if r.returncode == 0 else "REFUSE")
for p in ("/api/scoped/amgt/lists", "/api/scoped/amgt/security/BA_US_Equity/thesis",
          "/api/scoped/amgt/security/992_HK_Equity/thesis", "/api/scoped/advisor-intelligence/summary",
          "/api/general/health"):
    req = urllib.request.Request("https://opalinvest.dev" + p, headers={"User-Agent": "opal-rk122"})
    try:
        r2 = urllib.request.urlopen(req, timeout=30)
        code, ct, n = r2.status, r2.headers.get("Content-Type"), len(r2.read())
    except urllib.error.HTTPError as e:
        code, ct, n = e.code, e.headers.get("Content-Type"), len(e.read())
    print("pre", p, code, ct, n)
```

`.scratch/r122/plan_read.py <planfile>`:
```
import sys
lines = open(sys.argv[1], encoding="utf-8", errors="replace").read().splitlines()
print("plan_line", [l.strip() for l in lines if l.strip().startswith("Plan:") or "No changes." in l])
print("resources", [l.strip() for l in lines if l.strip().startswith("# ") and "will be" in l])
print("added_behaviors", sum(1 for l in lines if l.strip().startswith("+ ordered_cache_behavior")))
print("removed_behaviors", sum(1 for l in lines if l.strip().startswith("- ordered_cache_behavior")))
print("amgt_pattern_lines", [l.strip() for l in lines if "amgt" in l])
print("spa_fallback_present", any("aws_cloudfront_function.spa_fallback" in l for l in lines))
```

`.scratch/r122/ac3.py` (the ROUTED seat runs this AFTER the apply; you run it read-only to prove it works):
```
import boto3, urllib.request, urllib.error
cf = boto3.client("cloudfront", region_name="us-east-1")
obs = cf.get_distribution_config(Id="EVTSA9VEHNZVH")["DistributionConfig"]["CacheBehaviors"]
pats = [b["PathPattern"] for b in obs.get("Items", [])]
print("live_behaviors", obs["Quantity"], "amgt", sum(1 for p in pats if "amgt" in p), "last", pats[-1] if pats else None)
for b in obs.get("Items", []):
    if "amgt" in b["PathPattern"]:
        la = [(x["EventType"], x["LambdaFunctionARN"].split(":")[-2] + ":" + x["LambdaFunctionARN"].split(":")[-1])
              for x in b.get("LambdaFunctionAssociations", {}).get("Items", [])]
        print("amgt_behavior", b["PathPattern"], b["TargetOriginId"], b.get("CachePolicyId"), la)
for p in ("/api/scoped/amgt/security/BA_US_Equity/thesis", "/api/scoped/amgt/security/992_HK_Equity/thesis",
          "/api/scoped/amgt/lists", "/api/scoped/amgt/freshness",
          "/api/scoped/advisor-intelligence/summary", "/api/general/health"):
    req = urllib.request.Request("https://opalinvest.dev" + p, headers={"User-Agent": "opal-rk122"})
    try:
        r = urllib.request.urlopen(req, timeout=30)
        code, ct, body = r.status, r.headers.get("Content-Type"), r.read()
    except urllib.error.HTTPError as e:
        code, ct, body = e.code, e.headers.get("Content-Type"), e.read()
    print("post", p, code, ct, len(body), "json", "json" in (ct or ""), "html", body[:15].lstrip()[:9].lower() == b"<!doctype")
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-122"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r122/ac0.py</invocation><expect>BEFORE any edit: "live_behaviors 28 amgt 0" and "declared_path_pattern 28" (declared equals live, so the file is the source of truth; a drifted pair is a STOP and a row, never an edit); the patterns list contains NO /api/* or /api/scoped/* catch-all; the lane lines read PERMIT for 0.7.0_AE_CloudOps and REFUSE for both 2.0.0_SA_COO~Z and 0.9.0_WK_AMGT_RESAPP~122 -- the positive control proves the harness discriminates, and the two refusals are why the apply is ROUTED; and five "pre" lines with the 3 amgt paths at 200 text/html 1000 and the 2 controls at 401 application/json 51. Record every value: these are the baselines AC3 is graded against</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-122"><invocation>cd "$(git rev-parse --show-toplevel)" && terraform -chdir=infra/aws/terraform/portal-auth init -input=false -no-color > .scratch/r122/init.txt 2>&1; terraform -chdir=infra/aws/terraform/portal-auth plan -no-color -input=false -target=aws_cloudfront_distribution.portal > .scratch/r122/plan.txt 2>&1; python .scratch/r122/plan_read.py .scratch/r122/plan.txt</invocation><expect>AFTER the worktree edit (NOT committed): "added_behaviors 1" and "removed_behaviors 0"; "amgt_pattern_lines" is exactly one line carrying path_pattern = "/api/scoped/amgt/*"; "spa_fallback_present False"; and plan_line CONFORMS to section 4's bound -- either "Plan: 0 to add, 1 to change, 0 to destroy" naming only aws_cloudfront_distribution.portal, or "0 to add, 2 to change, 0 to destroy" naming ONLY that plus aws_wafv2_web_acl.opal_cloudfront_protection, in which case you ALSO print the WAF's field-by-field diff (rule names both sides, and all 6 visible fields per managed-rule block) and it must show ZERO differing fields. ANY other resource, or a second changed attribute on the distribution, is Branch B: STOP, no apply, a BLOCKING row quoting the extra lines</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-122"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff -- infra/aws/terraform/portal-auth/cloudfront-distribution.tf > org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_amgt_behavior.patch && git diff --numstat -- infra/aws/terraform/portal-auth/cloudfront-distribution.tf && git status --short -- infra/aws/terraform/portal-auth/ && python -c "b=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_amgt_behavior.patch','rb').read(); print('patch_bytes',len(b),'crlf',b.count(bytes([13,10])),'non_ascii',sum(1 for c in b.decode('utf-8') if ord(c)>127))"</invocation><expect>the numstat reads insertions with 0 DELETIONS on that one file (the append shifts nothing); git status --short shows the .tf as MODIFIED and UNSTAGED, and the patch file is written under your deliverables dir with crlf 0 and non_ascii 0. The .tf is NOT committed by you and appears in no commit of yours -- that is the routing, not an omission</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-122"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r122/ac3.py</invocation><expect>RUN TWICE. (a) BEFORE the routed apply, as a PRE control, it must reproduce AC0: "live_behaviors 28 amgt 0" and the amgt paths still text/html -- this proves the script reads the live plane and is not a stub. (b) AFTER the routed apply it is the acceptance: "live_behaviors 29 amgt 1" with the amgt pattern LAST; one "amgt_behavior" line reading /api/scoped/amgt/* APIGateway-portal with the caching-disabled policy id and exactly [('viewer-request', 'auth-validator-edge:20')]; BA_US_Equity FIRST then 992_HK_Equity each "json True html False" (a 401 application/json is a PASS here -- it proves the validator is attached; a 200 text/html is a FAIL); and the two controls UNMOVED at 401 application/json. If (b) cannot run because the routed apply has not happened, AC3 is REFUSED with its (a) half recorded and a row -- never a self-apply</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-122"><invocation>cd "$(git rev-parse --show-toplevel)" && ls -1 org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/ && python -c "t=open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/rk122_handoff.md',encoding='utf-8').read();print('handoff_bytes',len(t));print('names_safe_apply','safe-apply.sh' in t);print('names_ledger_slug','amgt-rk122-edge-behavior' in t);print('names_rollback','rollback' in t.lower());print('names_ae_lane','CLOUD_OPS_OR_ETL' in t)"</invocation><expect>the deliverables dir carries rk122_amgt_behavior.patch and rk122_handoff.md, and the handoff names the safe-apply command, the ledger slug amgt-rk122-edge-behavior, the rollback and the AE lane -- all four True. The routed seat needs nothing from you but these two files</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~122/AMGT_RESAPP.TO-AMGT-rk-122.amgt-edge-behavior.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4` (rc 0 is the verdict); flip the order's status
(on the record face) to `complete` only if every criterion PASSES -- which, on the routed shape, it cannot until the AE
seat has applied. Report once, naming: AC0's behavior count and the three lane verdicts, AC1's plan line and which
branch it took, the patch's numstat, and AC3's (a) half.

**MUTATION DISCIPLINE:** snapshot the `.tf`'s WORKING-TREE BYTES to `.scratch/r122/` before editing. Never
`git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices, flagged to the CTO at issuance:**

1. **THE `.tf` IS DELIBERATELY ABSENT FROM `<paths>`, AND THAT IS A DECISION THE CTO SHOULD RULE ON.** The worker
   grant (`.owned-paths.yaml` `worker_grant`, ADHC_OWNPTH.005, Andrew-direct 2026-09-04) admits a `0.9.0_WK_*` serial
   to **exactly the paths its own non-terminal order names at HEAD, with NO lane consulted** --
   `.tools/owned-paths-validate.py:209-235` applies no lane filter and `check_agent:330` calls it as an ADDITIVE fifth
   clause after the lane refuses. **So naming the `.tf` here would have admitted the worker to an AE-lane served infra
   file, silently, by this seat's own cut.** Measured today: the worker is REFUSED precisely because no order names
   it. Writing the order the other way would have converted an AE-lane act into a COO-issued worker act without the AE
   lane ever being consulted. The CTO's ruling says to route rather than override when the lane refuses this seat, and
   the measured lane refuses `2.0.0_SA_COO~Z` AND `0.2.0_DT_PortfolioAnalytics`, so **AE is the only routing target**.
   If the CTO would rather have the worker carry it end-to-end, that is a one-line `<paths>` amendment plus an explicit
   ruling that the self-grant is intended -- **this seat will not take that silently.**
2. **The apply's bound is WIDENED to the precedent's exact widening and no further.** The predecessor cell was refused
   by its own gate on a 3-resource plan; the resume ran under "ONE change plus the classified WAF read-normalisation
   no-op" and landed. The WAF artefact is DURABLE -- the predecessor's post-apply plan still read "1 to change" naming
   only the WAF, and the CTO recorded its owner as `0.7.0_AE_CloudOps`. Writing this cell to the naive "exactly one
   change" bound would reproduce a known refusal.
3. **The CRLF half is already closed:** `spa-fallback-function.js` reads 0 CRLF / 26 LF on disk and byte-identical to
   its HEAD blob, so `spa_fallback` should be absent from the plan. AC1 asserts that rather than assuming it.
4. **`allowed_methods` includes the write verbs** because the page's 16 mounted routes include 3 POSTs
   (`/refresh`, `/watchlist/star`, `/watchlist/unstar`). Behavior 15 carries the same set.
5. **NOT IN THIS CELL:** `Z-S227` (0 of 5 tabs carry an `isError` branch, so an errored read and an absent object
   render identically -- which is WHY this outage was silent) and `Z-S229` (the price axis is 12 days stale). Each has
   its own remedy and owner.

**ISSUER CLOSE-OUT, `2.0.0_SA_COO~Z`, 2026-09-22 (added at the round-30 drain-end, AFTER the act landed).**
This order is flipped `pending` -> `superseded`, NOT `complete`, and the distinction is the record:

- **Its own worker could never complete it, BY THIS SEAT'S DESIGN** -- s.6 above says so in terms ("which, on
  the routed shape, it cannot until the AE seat has applied"). AC0/AC1/AC2 PASSED here (three lane verdicts, the
  plan line, the patch numstat); AC3/AC4 are the apply and the live re-read, and they were carried by
  `AMGT_RESAPP.TO-AMGT-rk-123` at `0.7.0_AE_CloudOps` under the CTO's cutting practice (msg 24396: an order's
  `<paths>` may name only paths the ISSUING seat's lane admits, and the carrying order is cut in the SAME turn).
- **rk-123 is `complete` and the act is verified on THREE instruments** -- the AE seat's own AC0-AC5, the CTO's
  independent live GETs at 21:11:02Z, and this seat's read; all `/api/scoped/amgt/*` paths now return 401
  `application/json`, byte-identical to both control families, with the AE seat's mutant
  (`/api/scoped/amgtXYZZY/lists` still 200 `text/html`) settling causation.
- **This worker's deliverables were CONSUMED, not discarded:** the patch and plan rk-123 applied are this cell's,
  and row `Z-W122-S1` (the `spa_fallback` substring defect) was independently corroborated by the AE seat on a
  different instrument.
- ⚠ **The flip is an ISSUER act on the record face, not a grade.** No criterion is being marked PASS here that
  was not proven where it ran; `superseded` says the ORDER was overtaken, and the L9 reads rk-123's instance for
  the act's acceptance. Left `pending`, this order would have held the round open forever against a cell that
  had already served.

<status>superseded</status>
<round>30</round>
<slot>~122</slot>
<fabric>site-z</fabric>
