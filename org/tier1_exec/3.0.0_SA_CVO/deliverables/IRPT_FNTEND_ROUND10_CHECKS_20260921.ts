/** CVO round-10 read-only probes. Run from the workspace root with bun run <this file>.
 * No backend requests, files written, fixtures changed, or worker artifacts overwritten.
 */
import { readFileSync } from 'node:fs'
import { execFileSync } from 'node:child_process'
import { parseIrEnvelope } from '../../../../portal/src/pages/InvestorReporting/contracts/envelope'

const project = 'org/missions/D9/IRPT/IRPT_FNTEND'
const readJson = (path: string) => JSON.parse(readFileSync(path, 'utf8'))
const oldMap = readJson('portal/src/pages/InvestorReporting/fixtures/smoke/fe-s-16-print-narrative.json')
const newMap = readJson('portal/src/pages/InvestorReporting/__tests__/fe-s-63/fixtures/print-ready.json')
const route = '/api/scoped/investor-reporting/performance/'
function parse(label: string, body: unknown) {
  try {
    const parsed = parseIrEnvelope<any>('performance-report', body)
    console.log(label, JSON.stringify({ accepted: true, state: parsed.state, availability: parsed.data?.availability }))
    return true
  } catch (error: any) {
    console.log(label, JSON.stringify({ accepted: false, name: error.name, field: error.field, code: error.publicReasonCode, message: error.message }))
    return false
  }
}
console.log('ORIGINAL ROUTE KEYS', Object.keys(oldMap))
console.log('NEW ROUTE KEYS', Object.keys(newMap))
const oldAccepted = parse('ORIGINAL performance envelope', oldMap[route])
const newAccepted = parse('REPLACEMENT performance envelope', newMap[route])
const repairedOld = structuredClone(oldMap[route])
repairedOld.unprojected_grant = structuredClone(newMap[route].unprojected_grant)
const oneFieldAccepted = parse('CONTROL original plus ONLY unprojected_grant', repairedOld)
const brokenNew = structuredClone(newMap[route])
delete brokenNew.unprojected_grant
const mutantAccepted = parse('CONTROL replacement minus ONLY unprojected_grant', brokenNew)
if (oldAccepted || !newAccepted || !oneFieldAccepted || mutantAccepted) throw new Error('Envelope discriminator did not match the stated hypothesis')

const censusPath = `${project}/deliverables/0.9.0_WK_IRPT_FNTEND~1/component-census.json`
const round1 = JSON.parse(execFileSync('git', ['show', `9e0370009f:${censusPath}`], { encoding: 'utf8' }))
const prior = readJson(censusPath)
const current = readJson(`${project}/deliverables/0.9.0_WK_IRPT_FNTEND~14/component-census.json`)
for (const [label, baseline] of [['round1', round1], ['committed_prior', prior]] as const) {
  const before = new Set(baseline.components.map((row: any) => row.component))
  const after = new Set(current.components.map((row: any) => row.component))
  console.log('CENSUS', JSON.stringify({ baseline: label, baselineCount: before.size, current: after.size,
    added: [...after].filter(name => !before.has(name)), removed: [...before].filter(name => !after.has(name)) }))
}
console.log('CENSUS COUNTS', JSON.stringify({ components: current.components.length,
  reused: current.components.filter((row: any) => row.classification === 'REUSED').length,
  new: current.components.filter((row: any) => row.classification === 'NEW').length }))
console.log('CENSUS REASON CONTROL', JSON.stringify(current.components.filter((row: any) => ['UnnamedReasonCodeFlag', 'PageSheet'].includes(row.component))))

const grey = 0x59 / 255
const luminance = grey <= 0.04045 ? grey / 12.92 : ((grey + 0.055) / 1.055) ** 2.4
console.log('SOURCE-COLOUR CONTRAST #595959 on #FFFFFF', (1.05 / (luminance + 0.05)).toFixed(4), ':1; not a pixel or physical-print measurement')
