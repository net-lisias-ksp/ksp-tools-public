#    This file is part of KSP Tools
#    © 2020 LisiasT
#
#    KSP Tools is licensed as follows:
#
#        * GPL 2.0 : https://www.gnu.org/licenses/gpl-2.0.txt
#
#    KSP Tools is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#    You should have received a copy of the GNU General Public License 2.0
#    along with KSP Tools, if not see <https://www.gnu.org/licenses/>.
#

import ksp.metadata.V0_22
import ksp.metadata.V0_23_0
import ksp.metadata.V0_23_5
import ksp.metadata.V0_24_0
import ksp.metadata.V0_24_1
import ksp.metadata.V0_24_2
import ksp.metadata.V0_25
import ksp.metadata.V0_90
import ksp.metadata.V1_0_0
import ksp.metadata.V1_0_1
import ksp.metadata.V1_0_2
import ksp.metadata.V1_0_3
import ksp.metadata.V1_0_4
import ksp.metadata.V1_0_5
import ksp.metadata.V1_1_0
import ksp.metadata.V1_1_1
import ksp.metadata.V1_1_2
import ksp.metadata.V1_1_3
import ksp.metadata.V1_2_0
import ksp.metadata.V1_2_1
import ksp.metadata.V1_2_2
import ksp.metadata.V1_3_0
import ksp.metadata.V1_3_1
import ksp.metadata.V1_4_0
import ksp.metadata.V1_4_1
import ksp.metadata.V1_4_2
import ksp.metadata.V1_4_3
import ksp.metadata.V1_4_4
import ksp.metadata.V1_4_5
import ksp.metadata.V1_5_0
import ksp.metadata.V1_5_1
import ksp.metadata.V1_6_0
import ksp.metadata.V1_6_1
import ksp.metadata.V1_7_0
import ksp.metadata.V1_7_1
import ksp.metadata.V1_7_2
import ksp.metadata.V1_7_3
import ksp.metadata.V1_8_0
import ksp.metadata.V1_8_1
import ksp.metadata.V1_9_0
import ksp.metadata.V1_9_1
import ksp.metadata.V1_10_0
import ksp.metadata.V1_10_1

def get(key):
	if "1.10.1" == key: return ksp.metadata.V1_10_1
	if "1.10.0" == key: return ksp.metadata.V1_10_0
	if "1.9.1" == key: return ksp.metadata.V1_9_1
	if "1.9.0" == key: return ksp.metadata.V1_9_0
	if "1.8.1" == key: return ksp.metadata.V1_8_1
	if "1.8.0" == key: return ksp.metadata.V1_8_0
	if "1.7.3" == key: return ksp.metadata.V1_7_3
	if "1.7.2" == key: return ksp.metadata.V1_7_2
	if "1.7.1" == key: return ksp.metadata.V1_7_1
	if "1.7.0" == key: return ksp.metadata.V1_7_0
	if "1.6.1" == key: return ksp.metadata.V1_6_1
	if "1.6.0" == key: return ksp.metadata.V1_6_0
	if "1.5.1" == key: return ksp.metadata.V1_5_1
	if "1.5.0" == key: return ksp.metadata.V1_5_0
	if "1.4.5" == key: return ksp.metadata.V1_4_5
	if "1.4.4" == key: return ksp.metadata.V1_4_4
	if "1.4.3" == key: return ksp.metadata.V1_4_3
	if "1.4.2" == key: return ksp.metadata.V1_4_2
	if "1.4.1" == key: return ksp.metadata.V1_4_1
	if "1.4.0" == key: return ksp.metadata.V1_4_0
	if "1.3.1" == key: return ksp.metadata.V1_3_1
	if "1.3.0" == key: return ksp.metadata.V1_3_0
	if "1.2.2" == key: return ksp.metadata.V1_2_2
	if "1.2.1" == key: return ksp.metadata.V1_2_1
	if "1.2.0" == key: return ksp.metadata.V1_2_0
	if "1.1.3" == key: return ksp.metadata.V1_1_3
	if "1.1.2" == key: return ksp.metadata.V1_1_2
	if "1.1.1" == key: return ksp.metadata.V1_1_1
	if "1.1.0" == key: return ksp.metadata.V1_1_0
	if "1.0.5" == key: return ksp.metadata.V1_0_5
	if "1.0.4" == key: return ksp.metadata.V1_0_4
	if "1.0.3" == key: return ksp.metadata.V1_0_3
	if "1.0.2" == key: return ksp.metadata.V1_0_2
	if "1.0.1" == key: return ksp.metadata.V1_0_1
	if "1.0.0" == key: return ksp.metadata.V1_0_0
	if "0.90" == key: return ksp.metadata.V0_90
	if "0.25" == key: return ksp.metadata.V0_25
	if "0.24.2" == key: return ksp.metadata.V0_24_2
	if "0.24.1" == key: return ksp.metadata.V0_24_1
	if "0.24.0" == key: return ksp.metadata.V0_24_0
	if "0.23.5" == key: return ksp.metadata.V0_23_5
	if "0.23.0" == key: return ksp.metadata.V0_23_0
	if "0.22" == key: return ksp.metadata.V0_22

	raise ModuleNotFoundError(key)
