'''
Created on Sep 27, 2020

@author: lisias
'''

import ksp.metadata

if __name__ == '__main__':
	print ("Version \t ReleaseDt \t ∑Modules \t ∑AllParts \t ∑Stock \t ∑MH \t ∑Serenity")

	def s(x):
		r = int(x.replace(".",""))
		r = r / 10 if x.startswith("0") and x.count(".") > 1 else r
		return r
	for kspv in sorted(ksp.metadata.ALL_VERSIONS, key=s):
		m = ksp.metadata.get(kspv)
		print('{:s} \t\t {:s} \t {:d} \t\t {:d} \t\t {:d} \t {:d} \t\t {:d}'.format(
				kspv,
				str(m.RELEASE_DATE),
				len(m.ALL_MODULES),
				len(m.ALL_PARTS),
				len(m.Stock.PARTS),
				len(m.MH.PARTS),
				len(m.Serenity.PARTS)
			))
