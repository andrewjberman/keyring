"""GATE-2 RELEASE PROOF (3.0.0_SA_CVO~B) -- A3 exercised THROUGH THE DISPATCH.

Base CTO, 054842Z: "exercise A3 THROUGH THE DISPATCH, not just against the lib ... The arm
that killed it is the arm that clears it -- same fixture, same partition, resolver skipped."

WHY THIS EXISTS. My original gate-2 DELTA-0 (0/871) was measured RESOLVER-DIRECT: the harness
invoked the resolver, then compared. A resolver-direct harness ALWAYS holds a freshly-written
resolution, so it STRUCTURALLY CANNOT EXPRESS the state "artifact present + resolver skipped."
That is why it passed clean. The harness shared the defect's blind spot. This one does not:
it asks THE REAL DISPATCH what it would run, and only then reads.

WHAT IT ACTUALLY EXERCISES (stated precisely; nothing blurred):
  * REAL: orion-gold-dispatch.sh's own chain-assembly code path, driven under both switch
    states via `--help` (which exits before ANY script executes -- assembly is top-level at
    :343-356, arg-parsing is at :1147). No gold script runs. No S3 write. No nightly touched.
    CLAUDE.md forbids ad-hoc gold runs to validate work; this respects that.
  * REAL: lib/aor_resolution.load_resolution() -- the exact call every migrated consumer makes.
  * STUBBED: S3, holding the artifact-present-and-stale state the rollback actually creates.

THE COMPOSITION IS THE POINT. Neither half alone can see the defect:
  the dispatch half proves the resolver is NOT SCHEDULED under OFF;
  the consumer half proves load_resolution() RETURNS on the leftover artifact.
  Together: nothing writes the resolution, and the consumer reads yesterday's anyway -- silently.

VINTAGE (read this before quoting the harness): written against the PRE-R5 dispatch, where chain
entry was SWITCH-gated at :353. R5 has since DE-MULTIPLEXED that -- entry is now PRESENCE-gated
(:410-430) and the resolver is prepended to CHAIN_INCREMENTAL/CHAIN_GOLD_A too. The composition
this harness performs (ask the dispatch what it schedules -> then perform the consumer's REAL
read) is still exactly right; only the in-line commentary about :353 is of the older tree. The
KEY is verified separately by aor_r182_key_verify.py.

PASS/FAIL: this arm is RED while the chokepoint key is wrong, and GREEN when it is right.
It is the same arm in both cases. exit 1 = RED (fail-open reproduced). exit 0 = GREEN (closed).
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from io import BytesIO

import pandas as pd

REPO = r'C:\Users\AndrewBerman\Desktop\ajb_workspace'
DISPATCH = os.path.join(REPO, 'data', 'inf', 'scripts', 'gold', 'orion-gold-dispatch.sh')
# Pin Git Bash explicitly: a bare 'bash' resolves to WSL's bash on this host, which cannot
# execvpe the script at all -- and a broken interpreter would surface as an EMPTY chain read,
# i.e. "resolver absent", which is the verdict we are testing for. The instrument must not be
# able to manufacture its own finding.
BASH = next(p for p in (r'C:\Program Files\Git\bin\bash.exe',
                        r'C:\Program Files\Git\usr\bin\bash.exe') if os.path.exists(p))
LIB = os.path.join(REPO, 'data', 'inf', 'scripts', 'gold', 'lib')
sys.path.insert(0, LIB)

PIN = os.environ.get('INF_AOR_ASOF') or '2026-07-12'   # the live pin: latest accounts_v2 partition
os.environ['INF_AOR_ASOF'] = PIN

SERVICING = 'peter_lee'       # what a switch-OFF run MUST serve (DELTA-0)
FOLDED = 'noel_soderblom'     # what the artifact from the last ON run carries for a mover

from aor_resolution import RESOLUTION_KEY, load_resolution  # noqa: E402
from aor_resolution import code_digest as _code_digest  # noqa: E402


# ---- STEP 1: ask THE REAL DISPATCH what it would run -----------------------------------

def dispatch_chain(fold_active: str) -> list[str]:
    """Drive the real dispatch's chain assembly. `--help` exits before any script runs."""
    env = dict(os.environ, INF_AOR_FOLD_ACTIVE=fold_active)
    # the runner stages this; satisfy it so `set -e` does not abort before assembly
    os.makedirs('/tmp/orion_gold_scripts', exist_ok=True)
    open('/tmp/orion_gold_scripts/telemetry-sync.sh', 'a').close()
    p = subprocess.run([BASH, '-x', DISPATCH, '--help'], env=env,
                       capture_output=True, text=True)
    hits = re.findall(r"^\+ CHAIN_COMPUTE='?([^'\n]+)'?", p.stderr, re.M)
    if not hits:
        raise RuntimeError('INSTRUMENT BROKEN: never observed CHAIN_COMPUTE assignment. '
                           'Refusing to report a membership verdict off an empty read.')
    return hits[-1].split()


# ---- STEP 2: the artifact-present-and-stale state the ROLLBACK actually creates ---------

ETAG_NOW = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'   # the accounts_v2 partition as it stands RIGHT NOW


def _stale_folded_resolution() -> pd.DataFrame:
    """Written by LAST night's ON run: FOLDED keys, SAME pin, SAME source content (no new partition).

    CRITICAL: this artifact is FULLY SELF-DESCRIBING and every field the guard checks AGREES with
    this run EXCEPT fold_mode. as_of matches the pin; source_digest matches the partition's current
    ETag. That is the whole point -- it is NOT a crude stale artifact that any check would catch. It
    is precisely the artifact a prompt rollback leaves behind, and the ONLY thing that betrays it is
    the MODE it was built under. If we stamped it non-self-describing we would exercise the A2 branch
    and learn nothing about A3.
    """
    return pd.DataFrame({
        'account_id': [1, 2, 3],
        'advisor_key': [FOLDED, 'peter_lee', 'patrick_scanlan'],
        'rep_bucket': ['individual'] * 3,
        'servicing_advisor_key': [SERVICING] * 3,
        'advisor_of_record_raw': ['Noel', '', ''],
        'explicit_aor': [True, False, False],
        'is_mover': [True, False, False],
        'as_of': [PIN] * 3,
        'fold_mode': ['ACTIVE'] * 3,        # built under ON, last night  <-- THE ONLY MISMATCH
        'source_digest': [ETAG_NOW] * 3,    # from the SAME partition this run reads -- source is INNOCENT
        # round-8.2 R-B: the artifact must ALSO carry the CODE identity, and it must MATCH this run's
        # lib -- otherwise the guard raises on NOT-SELF-DESCRIBING and we exercise the A2 branch,
        # learning nothing about A3. The whole test is that EVERY field agrees except fold_mode.
        'code_digest': [_code_digest()] * 3,
    })


class StubS3:
    def __init__(self, frame):
        self.frame = frame

    def get_object(self, Bucket, Key):
        if self.frame is None or Key != RESOLUTION_KEY:
            raise FileNotFoundError('NoSuchKey')
        b = BytesIO()
        self.frame.to_parquet(b, index=False, engine='pyarrow')
        b.seek(0)
        return {'Body': BytesIO(b.read())}

    def head_object(self, Bucket, Key):
        return {'ETag': f'"{ETAG_NOW}"'}    # the source partition is UNCHANGED: only the MODE differs


print('=' * 100)
print('GATE-2 RELEASE PROOF -- A3 THROUGH THE DISPATCH   (rollback: artifact PRESENT + resolver SKIPPED)')
print('=' * 100)

# STEP 1 -- the dispatch's decision, under the ROLLBACK (switch flipped OFF)
off = dispatch_chain('0')
on = dispatch_chain('1')
resolver_scheduled = 'INF_A_0' in off
detector_scheduled = 'INF_D_11' in off

print('\n[1] THE DISPATCH, asked directly (denominators, so an empty read cannot pass as a verdict):')
print(f'      switch ON  -> {len(on):>2} steps | INF_A_0 scheduled: {"INF_A_0" in on} | INF_D_11: {"INF_D_11" in on}')
print(f'      switch OFF -> {len(off):>2} steps | INF_A_0 scheduled: {resolver_scheduled} | INF_D_11: {detector_scheduled}')
if resolver_scheduled:
    print('      -> resolver IS scheduled under OFF: the F1 chain-gate is FIXED.')
else:
    print('      -> resolver NOT scheduled under OFF  ==> NOTHING WILL WRITE aor_resolution THIS RUN.')
    print('         (and INF_D_11, the detector that would notice, is dropped by the SAME conditional)')

# first consumer that will actually execute, in real chain order
CONSUMERS = ['INF_A_00', 'INF_A_01', 'INF_B_00', 'INF_C_01', 'INF_C_07',
             'INF_09', 'INF_D_00c', 'INF_D_00d', 'INF_D_00f', 'INF_D_02b']
first_consumer = next((s for s in off if s in CONSUMERS), None)
print(f'\n[2] FIRST AoR CONSUMER the OFF chain will execute: {first_consumer}')
print('      it calls load_resolution() UNCONDITIONALLY (census: 10/10 consumers carry ZERO')
print('      AOR_FOLD_ACTIVE references -- the switch reaches only dispatch:353).')

# STEP 2 -- that consumer's REAL read, against the state the rollback leaves behind
print(f'\n[3] {first_consumer} performs its REAL read against the leftover artifact')
print(f'      (last ON run wrote it: advisor_key={FOLDED}, as_of={PIN}; no new partition since)')
try:
    res = load_resolution(StubS3(_stale_folded_resolution()), 'opal-data-inf')
    got = 'RETURNED'
    served = str(res.loc[res['account_id'] == 1, 'advisor_key'].iloc[0])
except Exception as e:
    got, served = 'RAISED', '-'
    detail = str(e).split(' -- ')[1][:110] if ' -- ' in str(e) else str(e)[:110]

print(f'      -> load_resolution() {got}')

print('\n' + '=' * 100)
if not resolver_scheduled and got == 'RETURNED':
    print('VERDICT: RED -- FAIL-OPEN REPRODUCED THROUGH THE DISPATCH.')
    print('  The dispatch did NOT schedule the resolver, so nothing wrote a resolution this run.')
    print(f'  The consumer read the LEFTOVER one and got advisor_key={served!r}')
    print(f'  -- but the switch is OFF, which demands {SERVICING!r} (servicing / DELTA-0).')
    print('  THE ROLLBACK SILENTLY RE-SERVED THE FOLD IT WAS ROLLING BACK FROM,')
    print('  with its own drift detector disabled by the same conditional.')
    print('\n  This is the arm that must go GREEN before gate-2 clears. Same arm, same state.')
    sys.exit(1)
if resolver_scheduled and got == 'RETURNED':
    print('VERDICT: GREEN-BY-SCHEDULING -- the resolver runs under OFF, so it rewrites the')
    print('  resolution servicing-only and the leftover artifact is never read. F1 chain-gate closed.')
    print('  NOTE: this does NOT by itself prove the chokepoint key is right -- a --single/--from')
    print('  consumer rerun still bypasses the chain entirely. Keep the lib-level arms.')
    sys.exit(0)
if got == 'RAISED':
    print('VERDICT: GREEN-BY-CHOKEPOINT -- the resolver was NOT scheduled, but load_resolution()')
    print(f'  REFUSED the leftover artifact: {detail}')
    print('  Fail-CLOSED: the chain aborts, yesterday\'s gold stays served. Serve stale, not garbage.')
    sys.exit(0)
print('VERDICT: INDETERMINATE -- do not quote this run.')
sys.exit(2)
