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
'''
Created on Sep 26, 2020

@author: lisias
'''

MODULES = set([
	"ModuleServiceModule",
])

PARTS_BY_CATEGORY = {
	'*UNSORTED*': set([
		'kerbalEVAVintage', 'kerbalEVAfemaleVintage'
	]),
	'Aero': set([
		'rocketNoseConeSize4'
	]),
	'Coupling': set([
		'Decoupler_1p5', 'Decoupler_4', 'EnginePlate1p5', 'EnginePlate2', 'EnginePlate3', 'EnginePlate4', 'InflatableAirlock', 'Separator_1p5', 'Separator_4', 'Size1p5_Strut_Decoupler'
	]),
	'Engine': set([
		'LiquidEngineKE-1', 'LiquidEngineLV-T91', 'LiquidEngineLV-TX87', 'LiquidEngineRE-I2', 'LiquidEngineRE-J10', 'LiquidEngineRK-7', 'LiquidEngineRV-1'
	]),
	'FuelTank': set([
		'Size1p5_Monoprop', 'Size1p5_Size0_Adapter_01', 'Size1p5_Size1_Adapter_01', 'Size1p5_Size1_Adapter_02', 'Size1p5_Size2_Adapter_01', 'Size1p5_Tank_01', 'Size1p5_Tank_02', 'Size1p5_Tank_03', 'Size1p5_Tank_04', 'Size1p5_Tank_05'
		'Size3_Size4_Adapter_01', 'Size4_EngineAdapter_01', 'Size4_Tank_01', 'Size4_Tank_02', 'Size4_Tank_03', 'Size4_Tank_04'
	]),
	'Ground': set([
		'roverWheelM1-F'
	]),
	'Payload': set([
		'ServiceModule18', 'ServiceModule25', 'Size1to0ServiceModule', 'fairingSize1p5', 'fairingSize4'
	]),
	'Pods': set([
		'MEMLander', 'Mk2Pod', 'kv1Pod', 'kv2Pod', 'kv3Pod'
	]),
	'Propulsion': set([
		'monopropMiniSphere'
	]),
	'Structural': set([
		'EquiTriangle0', 'EquiTriangle1', 'EquiTriangle1p5', 'EquiTriangle2', 'Panel0', 'Panel1', 'Panel1p5', 'Panel2', 'Triangle0', 'Triangle1'
		'Triangle1p5', 'Triangle2', 'Tube1', 'Tube1p5', 'Tube2', 'Tube3', 'Tube4'
	]),
	'Thermal': set([
		'HeatShield1p5'
	]),
}

from ksp.metadata import sum_all_parts
PARTS = sum_all_parts(PARTS_BY_CATEGORY)

