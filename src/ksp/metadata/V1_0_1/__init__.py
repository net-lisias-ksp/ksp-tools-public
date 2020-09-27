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

from datetime import datetime

import ksp.metadata.V1_0_1.Stock as Stock
import ksp.metadata.V1_0_1.MakingHistory as MH
import ksp.metadata.V1_0_1.Serenity as Serenity

ALL_MODULES = Stock.MODULES | MH.MODULES | Serenity.MODULES

RELEASE_DATETIME=datetime(2015, 5, 1, 0, 0)
UNITY_VERSION=4
CSHARP_VERSION=3.5
