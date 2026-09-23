/** Additional selection and public-CID negatives; original controls stay unchanged. */
import { afterAll, expect, test } from 'bun:test'
import { readFileSync, writeFileSync } from 'node:fs'
import { resolve } from 'node:path'
import { pathToFileURL } from 'node:url'
const root = process.env.IRPT_PORTAL_REVIEW_ROOT!
const own = process.env.IRPT_OUTER_EVIDENCE_ROOT!
const { parseIrEnvelope } = await import(pathToFileURL(resolve(root, 'src/pages/InvestorReporting/contracts/envelope.ts')).href)
const read = (name: string) => JSON.parse(readFileSync(resolve(own, name), 'utf8'))
const selection = read('SELECTION.json')
const outer = read('OUTER_PAIR_7915_OUTER.json')
const results: any[] = []
function control(name: string, run: () => void) {
  test(name, () => {
    try { run(); results.push({ name, outcome: 'PASS' }) }
    catch (e) { results.push({ name, outcome: 'FAIL', error: String(e) }); throw e }
  })
}
control('fresh actual selection success and refusal retain facts', () => {
  const good = parseIrEnvelope('selection-create', selection.success)
  expect(good.refused).toBe(false)
  const denied = parseIrEnvelope('selection-create', selection.refusal)
  expect(denied.refused).toBe(true)
  expect(denied.data).toBe(null)
  expect(denied.publicReasonCode).toBe('OBJECT_NOT_COVERED')
})
for (const [kind, pair] of Object.entries({ ...outer.cases, selection }) as any) {
  control(kind + ' public parser rejects injected server-only correlation', () => {
    const raw = structuredClone(pair.refusal)
    raw.status.internal_correlation_id = 'review-private-correlation'
    expect(() => parseIrEnvelope(raw.operation, raw)).toThrow()
  })
}
afterAll(() => writeFileSync(resolve(own, 'PUBLIC_PROJECTION_PORTAL.json'), JSON.stringify({
  backend_pin: selection.pin, portal_pin: JSON.parse(readFileSync(resolve(root, 'review-source-hashes.json'), 'utf8')).pin, results,
}, null, 2) + '\n'))
