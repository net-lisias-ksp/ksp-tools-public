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

from datetime import date

import ksp.metadata.V0_22.Stock as Stock
import ksp.metadata.V0_22.MakingHistory as MH
import ksp.metadata.V0_22.Serenity as Serenity

ALL_MODULES = Stock.MODULES | MH.MODULES | Serenity.MODULES
ALL_PARTS = Stock.PARTS | MH.PARTS | Serenity.PARTS

RELEASE_DATE=date(2013, 10, 16)
UNITY_VERSION=4
CSHARP_VERSION=3.5
