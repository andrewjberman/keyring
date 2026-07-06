export const meta = {
  name: 'gold-runner-code-review',
  description: 'Exhaustive per-script code-review of a gold runner (any pipeline): one reviewer per gold script hunting type issues / incremental-vs-full breaks / unguarded reads / merge-dtype mismatches / silent served-number corruption, each material finding adversarially verified. Reusable across INF / 49F / COT.',
  phases: [
    { title: 'Review', detail: 'one reviewer per gold script' },
    { title: 'Verify', detail: 'adversarially verify each critical/high finding' },
  ],
}

// args (JSON, passed by the /gold-runner-code-review skill):
//   {
//     pipeline:   'inf' | '49f' | 'cot' | <name>,       // label only
//     dispatcher: 'data/.../orion-gold-dispatch.sh',    // the chain runner script (for the reviewer to grep)
//     full_chain: 'CHAIN_FULL',                         // env/var name of the daily full chain (optional)
//     incr_chain: 'CHAIN_INCREMENTAL',                  // env/var name of the incremental chain (optional)
//     scripts:    ['data/.../GOLD_A_00.foo.py', ...],   // the gold scripts to review, in chain order
//     context:    '...extra pipeline-specific notes...' // optional free text appended to CONTEXT
//   }
const A = (typeof args === 'string') ? JSON.parse(args) : (args || {})
const PIPELINE = A.pipeline || 'pipeline'
const DISPATCHER = A.dispatcher || '(the gold dispatcher script)'
const FULL_CHAIN = A.full_chain || 'the full/daily chain'
const INCR_CHAIN = A.incr_chain || 'the incremental chain'
const SCRIPTS = Array.isArray(A.scripts) ? A.scripts : (A.scripts ? JSON.parse(A.scripts) : [])
if (!SCRIPTS.length) throw new Error('gold-runner-code-review: args.scripts is empty -- pass the list of gold scripts to review.')

const REVIEW_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    script: { type: 'string' },
    verdict: { type: 'string', enum: ['clean', 'issues-found'] },
    runs_in_incremental: { type: 'boolean' },
    findings: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          category: { type: 'string', enum: ['type-issue','incremental-full-break','unguarded-read','empty-null-handling','merge-dedup','numeric-sign-units','schema-column','other'] },
          severity: { type: 'string', enum: ['critical','high','medium','low'] },
          mode: { type: 'string', enum: ['incremental','full','both'] },
          location: { type: 'string' },
          mechanism: { type: 'string' },
          failure_scenario: { type: 'string' },
          fix: { type: 'string' },
        },
        required: ['category','severity','mode','location','mechanism','failure_scenario'],
      },
    },
  },
  required: ['script','verdict','findings'],
}

const VERIFY_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    is_real: { type: 'boolean' },
    confidence: { type: 'string', enum: ['confirmed','plausible','refuted'] },
    corrected_severity: { type: 'string', enum: ['critical','high','medium','low'] },
    reasoning: { type: 'string' },
  },
  required: ['is_real','confidence','reasoning'],
}

function basename(p) { return p.split('/').pop() }

const CONTEXT = [
  `CONTEXT (${PIPELINE} gold runner, dispatched by ${DISPATCHER}):`,
  `- ${FULL_CHAIN} runs daily (mode=full): dimension scripts -> canonical -> client/account -> served platinum.`,
  `- ${INCR_CHAIN} (if present) runs API pulls + silver builds + the served/D-chain ONLY; it SKIPS the earlier gold scripts ("assumes their gold outputs exist in S3"). So in incremental mode the served chain reads FRESH silver + potentially-STALE upstream gold dims.`,
  `- The chain runner bounds ONLY the API-pull steps with a timeout+tolerate; ALL gold/silver compute steps run with NO timeout and HARD-FAIL the chain on any non-zero exit (sys.exit / uncaught exception).`,
  '- EXEMPLAR DEFECT CLASS we hunt: (1) a column written as the WRONG/UNSTABLE dtype across code paths or runs (bool->str, datetime->str, to_numeric(errors=coerce)->float/NaN where int/bool expected, a dtype pinned on the populated path but not the empty path). (2) an unguarded S3 read (get_object/read_parquet/read_csv/read_json) on an absent/SKIP/first-run input -> NoSuchKey/FileNotFoundError -> sys.exit(1) -> whole chain ABORTS. (3) a merge whose join-key DTYPE MISMATCHES (str vs Int64) -> pandas ValueError (crash) OR a silent 0-row join. (4) empty-DataFrame / all-NaN -> .max()/.min()/.iloc[0]/unguarded groupby -> crash or wrong default; missing-column KeyError. (5) percent-vs-decimal / sign / units magnitude bug. (6) inner-join or groupby(dropna=True) against a NA/stale/missing key -> silent row DROP -> under-counted served number.',
  A.context ? ('- PIPELINE NOTES: ' + A.context) : '',
].filter(Boolean).join('\n')

const reviewPrompt = (script) => [
  CONTEXT, '',
  'TASK: exhaustively review ONE gold script for SUBTLE HOLES, TYPE ISSUES, INCREMENTAL-vs-FULL BREAKS, and anything that could FAIL THE GOLD RUN (crash/abort) or SILENTLY CORRUPT a served number.', '',
  'Target: ' + script, '',
  'Steps:',
  '1. Read the FULL target script. Also Read any local lib helper it imports that governs dtype or S3-read behavior (dtype-coercion helpers, silver-lib readers, cache readers, taxonomy/status maps) when a dtype or an S3 read flows through it.',
  '2. Determine whether this script runs in the INCREMENTAL chain: Grep ' + DISPATCHER + " for this script's step-ID in the incremental-chain string. Set runs_in_incremental accordingly (upstream dims are typically NOT in incremental).",
  '3. Hunt for the CLASS, concretely + skeptically (a REAL defect has a specific line + a concrete triggering input): TYPE ISSUES (dtype varies between code paths/runs; a merge-key or downstream-consumed column not deterministically typed); INCREMENTAL/FULL BREAKS (reads a gold dim incremental skips; a max-date/partition assumption); UNGUARDED READS (a read that can NoSuchKey/FileNotFound on an absent/first-run input -> aborts the no-timeout hard-fail chain); EMPTY/NULL (empty-DF or all-NaN on .max/.min/.iloc/.sum/groupby; missing-column KeyError); MERGE/DEDUP (inner-join silent drops; merge-key DTYPE MISMATCH; groupby(dropna) dropping NA-keyed rows; duplicate-key double-count); NUMERIC (percent-vs-decimal, sign, units, rounding).',
  '4. For each REAL defect: category, severity (critical=crashes the chain OR serves a materially-wrong number; high=likely real; medium/low), mode (incremental|full|both), location (file:line or function), mechanism, a CONCRETE failure_scenario (specific input/state -> the crash or the wrong output), and a fix.',
  '5. If after a careful read you find nothing real, return verdict "clean" with findings []. DO NOT invent findings to fill the list -- a clean verdict on a genuinely-simple script is a valid, valuable result. Precision over volume.',
  '',
  'Return the structured object; script = "' + script + '".',
].join('\n')

const verifyPrompt = (script, f) => [
  CONTEXT, '',
  'A reviewer flagged a potential defect in ' + script + '. ADVERSARIALLY verify it -- try to REFUTE it. Re-read the exact code at the cited location and trace the data/dtype/control flow.', '',
  'FLAGGED: [' + f.severity + '/' + f.category + '/' + f.mode + '] ' + f.location,
  'Mechanism: ' + f.mechanism,
  'Failure scenario: ' + f.failure_scenario, '',
  'Is this a REAL defect that can actually fire (a concrete input reaches the cited line and produces the crash/wrong-output), or is it refuted (guarded upstream, dtype actually pinned, path unreachable, mode assumption wrong)? DEFAULT to refuted if you cannot construct a concrete triggering path. Give confidence (confirmed=you traced a concrete trigger; plausible=likely but not fully confirmable; refuted) + corrected_severity + reasoning citing the code.',
].join('\n')

// PIPELINE by default (no barrier): each script's material findings verify as soon as its review lands.
const results = await pipeline(
  SCRIPTS,
  (script) => agent(reviewPrompt(script), { label: 'review:' + basename(script), phase: 'Review', schema: REVIEW_SCHEMA }),
  (review, script) => {
    if (!review) return { script, verdict: 'error', findings: [] }
    const all = review.findings || []
    const material = all.filter(f => f.severity === 'critical' || f.severity === 'high')
    if (!material.length) return { script: review.script || script, verdict: review.verdict, runs_in_incremental: review.runs_in_incremental, findings: all }
    return parallel(material.map(f => () =>
      agent(verifyPrompt(review.script || script, f), { label: 'verify:' + basename(script), phase: 'Verify', schema: VERIFY_SCHEMA })
        .then(v => ({ ...f, verify: v }))
    )).then(verified => {
      const nonMaterial = all.filter(f => !(f.severity === 'critical' || f.severity === 'high'))
      return { script: review.script || script, verdict: review.verdict, runs_in_incremental: review.runs_in_incremental, findings: [...verified, ...nonMaterial] }
    })
  }
)

const clean = results.filter(Boolean)
const confirmed = []
for (const r of clean) {
  for (const f of (r.findings || [])) {
    if (f.verify && f.verify.is_real && f.verify.confidence !== 'refuted') confirmed.push({ script: r.script, severity: f.verify.corrected_severity || f.severity, ...f })
  }
}
log(`Reviewed ${clean.length}/${SCRIPTS.length} ${PIPELINE} gold scripts; ${confirmed.length} confirmed/plausible material defects (post adversarial-verify)`)
return { pipeline: PIPELINE, reviewed: clean.length, total: SCRIPTS.length, confirmed_defects: confirmed, all: clean }
