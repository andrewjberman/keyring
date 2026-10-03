# Leg H -- ONE seed-only capture on the host from Andrew's HAR session (Andrew-direct 2026-10-03 ~16:2xZ, 0.0.0_AB_MSTR
# msgs 104639/104640: "the premise is that if your long lived token has died out, here is another one").
#
# Sent verbatim to the resident host by host_read.py (Systems Manager, root). THIS IS A LIVE VENDOR READ with Andrew's
# session: /dashboard/ and the library's probe. It is NOT a sign-in: no login form is opened, no credential is read, no
# challenge is answered. In the resident's own context (user, environment minus PYTHON*, the secret-id pointers), it runs
# node ONCE:
#   1. take the provider lease exactly as the library does (fence_token + 1), or stop if it is held;
#   2. read the staged seed (version stage IMPORT_HAR of the session secret: ycsessionid + csrftoken only);
#   3. open a headless context with the library's contextOptions(), add the two cookies, load /dashboard/ (the browser
#      clears any WAF interstitial itself and mints its own aws-waf-token on the host);
#   4. lib.probeSession on that context: identity read + template probe. Not authenticated -> STOP, persist nothing;
#   5. the identity must be the enrolled user (1276035), else STOP;
#   6. lib.versionedBundle + lib.persistSession under the lease (the library's fenced write) -> a genuine EC2 capture;
#   7. release the lease. Bounded at 180 s.
# The printed receipt holds booleans, numbers, cookie NAMES and the verdict. No value, ever. ASCII only.
set -u
umask 077
TS=$(date -u +%Y%m%dT%H%M%SZ)
echo "leg H start $TS"
/usr/bin/python3.12 - "$TS" <<'PY'
import hashlib
import os
import pwd
import shutil
import signal
import subprocess
import sys
import tempfile

TS = sys.argv[1]
H = "/opt/investor-reporting-ycharts"
UNIT = "irpt-analysis-resident.service"


def sh(*argv):
    return subprocess.run(argv, capture_output=True, text=True).stdout.strip()


pid = int(sh("systemctl", "show", UNIT, "-p", "MainPID", "--value") or 0)
if pid <= 0:
    print("REFUSED: the resident unit has no main pid; nothing run")
    print("HAR_SEED_VERDICT=NOT_RUN:NO_RESIDENT")
    sys.exit(3)
env = {}
for item in open("/proc/%d/environ" % pid, "rb").read().split(b"\0"):
    if b"=" in item:
        key, value = item.split(b"=", 1)
        if not key.decode().upper().startswith("PYTHON"):
            env[key.decode()] = value.decode()
owner = pwd.getpwuid(os.stat("/proc/%d" % pid).st_uid)
print("resident pid %d user %s; library pin %s" % (
    pid, owner.pw_name, hashlib.sha256(open(H + "/ycharts_session.js", "rb").read()).hexdigest()[:16]))
work = tempfile.mkdtemp(prefix="irpt-har-seed-")
os.chown(work, owner.pw_uid, owner.pw_gid)
script = os.path.join(work, "har_seed.js")
open(script, "w").write(r"""
'use strict';
const { execFileSync } = require('child_process');
const APP = process.argv[2];
const lib = require(APP + '/ycharts_session.js');
const C = lib.constants;
const REGION = process.env.AWS_REGION || 'us-east-1';
const ENROLLED = 1276035;
const owner = 'irpt-ycharts-har-seed/' + process.pid;
const aws = (args) => JSON.parse(execFileSync('aws', args.concat(['--region', REGION]),
  { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }) || '{}');
const key = JSON.stringify({ tenant: { S: C.LEASE_TENANT }, job: { S: C.LEASE_JOB } });
const say = (o) => process.stdout.write(JSON.stringify(o) + '\n');
(async () => {
  const now = Math.floor(Date.now() / 1000);
  let lease;
  try {
    const out = aws(['dynamodb', 'update-item', '--table-name', C.LEASE_TABLE, '--key', key,
      '--update-expression', 'SET lease_owner = :me, lease_expires_at = :exp ADD fence_token :one',
      '--condition-expression', 'attribute_not_exists(lease_owner) OR lease_expires_at < :now OR lease_owner = :me',
      '--expression-attribute-values', JSON.stringify({ ':me': { S: owner }, ':now': { N: String(now) },
        ':exp': { N: String(now + 600) }, ':one': { N: '1' } }),
      '--return-values', 'ALL_NEW', '--output', 'json']);
    lease = { ok: true, owner, fence: parseInt(out.Attributes.fence_token.N, 10) };
  } catch (e) {
    say({ lease: 'HELD' });
    process.stdout.write('HAR_SEED_VERDICT=NOT_RUN:LEASE_HELD\n');
    return;
  }
  say({ lease: 'TAKEN', fence: lease.fence });
  let browser = null;
  let verdict = 'FAILED:UNKNOWN';
  try {
    const seed = JSON.parse(execFileSync('aws', ['secretsmanager', 'get-secret-value', '--secret-id', C.SESSION_SECRET_ID,
      '--version-stage', 'IMPORT_HAR', '--query', 'SecretString', '--output', 'text', '--region', REGION],
      { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] })).seed_cookies;
    say({ seed_cookie_names: seed.map((c) => c.name) });
    const pw = require(require.resolve(process.env.YC_PW_PATH || 'playwright', { paths: [APP] }));
    browser = await pw.chromium.launch({ headless: true, args: ['--no-sandbox', '--disable-dev-shm-usage'] });
    const ctxOpts = lib.contextOptions();
    const ctx = await browser.newContext(ctxOpts);
    await ctx.addCookies(seed);
    const page = await ctx.newPage();
    const nav = await page.goto(C.BASE + C.IDENTITY_PATH, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(8000);
    say({ dashboard_status: nav ? nav.status() : null, landed_path: new URL(page.url()).pathname });
    const probe = await lib.probeSession({ page, context: ctx }, { owner });
    say({ probe: { authenticated: probe.authenticated, reason: probe.reason,
      http_status: probe.evidence ? probe.evidence.probe_http_status : null,
      state: probe.evidence ? probe.evidence.probe_state : null,
      identity_leg: probe.evidence ? probe.evidence.identity_leg : null } });
    if (!probe.authenticated) { verdict = 'NOT_AUTHENTICATED:' + probe.reason; return; }
    const ident = probe.identity && probe.identity.ok ? probe.identity.identity_full : null;
    if (!ident || ident.user_id !== ENROLLED) { verdict = 'IDENTITY_MISMATCH'; return; }
    const cookies = await ctx.cookies();
    const expiryOf = (n) => { const c = cookies.find((x) => x.name === n); return c ? c.expires : null; };
    say({ expires_epoch: { ycsessionid: expiryOf('ycsessionid'), csrftoken: expiryOf('csrftoken'),
      'aws-waf-token': expiryOf('aws-waf-token') }, now_epoch: Math.floor(Date.now() / 1000) });
    const bundle = lib.versionedBundle({ cookies, identity: ident, userAgent: ctxOpts.userAgent, fence: lease.fence,
      probe_evidence: { probe_url_path: probe.probe_url_path, http_status: probe.evidence.probe_http_status,
        state: probe.evidence.probe_state }, owner });
    const persisted = await lib.persistSession(bundle, lease, { owner });
    say({ persisted: { fence: persisted.fence, previous_fence: persisted.previous_fence,
      cookie_names: (persisted.evidence && persisted.evidence.cookie_names) || null,
      identity_cookie_present: persisted.evidence ? persisted.evidence.identity_cookie_present : null,
      waf_cookie_present: persisted.evidence ? persisted.evidence.waf_cookie_present : null } });
    verdict = 'PERSISTED';
  } catch (e) {
    verdict = 'FAILED:' + (e && e.name ? e.name : 'Error') + ':' + String((e && e.message) || e).split('\n')[0].slice(0, 120);
  } finally {
    if (browser) { try { await browser.close(); } catch (e) { /* closing */ } }
    try {
      aws(['dynamodb', 'update-item', '--table-name', C.LEASE_TABLE, '--key', key,
        '--update-expression', 'SET lease_expires_at = :zero', '--condition-expression', 'lease_owner = :me',
        '--expression-attribute-values', JSON.stringify({ ':me': { S: owner }, ':zero': { N: '0' } }), '--output', 'json']);
      say({ lease: 'RELEASED' });
    } catch (e) { say({ lease: 'RELEASE_FAILED' }); }
    process.stdout.write('HAR_SEED_VERDICT=' + verdict + '\n');
  }
})();
""")
os.chown(script, owner.pw_uid, owner.pw_gid)
cmd = "cd %s && set -a && . ./secret-ids.env && set +a && exec node %s %s" % (H, script, H)
child = subprocess.Popen(["/bin/bash", "-c", cmd], cwd=H, env=env, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, start_new_session=True, user=owner.pw_name, group=owner.pw_gid,
                         extra_groups=os.getgrouplist(owner.pw_name, owner.pw_gid))
try:
    out, err = child.communicate(timeout=180)
    rc = child.returncode
except subprocess.TimeoutExpired:
    os.killpg(child.pid, signal.SIGKILL)
    out, err = child.communicate()
    rc = "TIMEOUT_180S"
finally:
    shutil.rmtree(work, ignore_errors=True)
for line in out.decode("utf-8", "replace").splitlines():
    print(line[:300])
tail = [l for l in err.decode("utf-8", "replace").splitlines() if "[ycharts-session]" in l][-6:]
for line in tail:
    print("stderr: " + line[:200])
print("node rc %s; work dir removed: %s" % (rc, not os.path.exists(work)))
PY
echo "leg H end $(date -u +%Y-%m-%dT%H:%M:%SZ)"
