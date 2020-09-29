'''
Created on Sep 27, 2020

@author: lisias
'''

import ksp.metadata

if __name__ == '__main__':
	print ("{: ^12s}|{: ^16s}|{: ^12s}|{: ^12s}|{: ^16s}|{: ^10s}|{: ^8s}|{: ^12s}".format(
		'Version', 'ReleaseDt', '∑Modules', '∑AllParts', '∑AllDeprecated', '∑Stock', '∑MH', '∑Serenity'
		))
	print ("{:-^12s}+{:-^16s}+{:-^12s}+{:-^12s}+{:-^16s}+{:-^10s}+{:-^8s}+{:-^12s}".format(
		'', '', '', '', '', '', '', ''
		))

	for kspv in ksp.metadata.ALL_VERSIONS_SORTED:
		m = ksp.metadata.get(kspv)
		print("{: >12s}|{: ^16s}|{: >12d}|{: >12d}|{: >16d}|{: >10d}|{: >8d}|{: >12d}".format(
				kspv,
				str(m.RELEASE_DATE),
				len(m.ALL_MODULES),
				len(m.ALL_PARTS),
				len(m.ALL_DEPRECATED_PARTS),
				len(m.Stock.PARTS),
				len(m.MH.PARTS),
				len(m.Serenity.PARTS)
			))
