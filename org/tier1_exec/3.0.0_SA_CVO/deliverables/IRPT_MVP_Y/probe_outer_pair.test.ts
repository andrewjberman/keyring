/** Exact regenerated outer Entry wires through the pinned consumer parser. */
import { afterAll, expect, test } from 'bun:test'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'
const root = process.env.IRPT_PORTAL_REVIEW_ROOT!
const own = process.env.IRPT_OUTER_EVIDENCE_ROOT!
if (!root || !own) throw new Error('Exact source and evidence roots required')
const { parseIrEnvelope } = await import(pathToFileURL(resolve(root, 'src/pages/InvestorReporting/contracts/envelope.ts')).href)
const read = (name: string) => JSON.parse(readFileSync(resolve(own, name), 'utf8'))
const outer = read('OUTER_PAIR_7915_OUTER.json'), dates = read('OUTER_PAIR_7915_DATES.json')
const backend = read('OUTER_PAIR_7915_REVIEW.json')
const results: any[] = []
function control(name: string, run: () => void) {
  test(name, () => {
    try { run(); results.push({ name, outcome: 'PASS' }) }
    catch (e) { results.push({ name, outcome: 'FAIL', error: String(e) }); throw e }
  })
}
for (const [kind, pair] of Object.entries(outer.cases) as any) {
  control(kind + ' actual success and refusal parse', () => {
    const success = parseIrEnvelope(pair.success.operation, pair.success)
    expect(success.refused).toBe(false); expect(success.data).not.toBe(null)
    const refusal = parseIrEnvelope(pair.refusal.operation, pair.refusal)
    expect(refusal.refused).toBe(true); expect(refusal.data).toBe(null)
    expect(refusal.publicReasonCode).toBe('CONTRACT_VERSION')
  })
}
for (const [kind, wire] of Object.entries(dates.cases) as any) {
  control(kind + ' actual date outer success preserves producer facts', () => {
    const parsed = parseIrEnvelope(wire.operation, wire)
    expect(parsed.refused).toBe(false)
    if (kind === 'single_date') expect(parsed.data.sourceDate.businessAsOf).toBe('2026-09-01')
    else if (kind === 'old_consumer') { expect(parsed.data.state).toBe('UNAVAILABLE'); expect(parsed.data.sourceDate.prospectDates).toBe(undefined) }
    else if (kind === 'not_ready') expect(parsed.data.state).toBe('LOADING')
    else expect(parsed.data.sourceDate.prospectDates.sections).toEqual(wire.data.source_dates.section_dates)
  })
}
for (const row of backend.negatives) {
  control(row.name + ' schema-invalid wire must be refused by strict parser', () => {
    expect(row.schema_rejects).toBe(true)
    expect(() => parseIrEnvelope(row.wire.operation, row.wire)).toThrow()
  })
}
afterAll(() => {
  const source = JSON.parse(readFileSync(resolve(root, 'review-source-hashes.json'), 'utf8'))
  writeFileSync(process.env.IRPT_PORTAL_REVIEW_OUTPUT!, JSON.stringify({ portal_pin: source.pin,
    backend_pin: backend.pin, source_sha256: source.hashes, controls: results,
    limitations: ['Regenerated actual Entry with offline storage; parser tests only, no browser/runtime',
      'Refusal parsing success does not resolve raw server-only correlation wire conflict'] }, null, 2) + '\n')
})
