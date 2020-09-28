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
	"ModuleGroundCommsPart",
	"ModuleGroundExpControl",
	"ModuleGroundExperiment",
	"ModuleGroundSciencePart",
	"ModulePhysicMaterial",
	"ModuleResourceAutoShiftState",
	"ModuleRobotArmScanner",
	"ModuleRoboticController",
	"ModuleRoboticRotationServo",
	"ModuleRoboticServoHinge",
	"ModuleRoboticServoPiston",
	"ModuleRoboticServoRotor",
])

PARTS_BY_CATEGORY = {
	'*UNSORTED*': set([
		'kerbalEVA', 'kerbalEVAFuture', 'kerbalEVAVintage', 'kerbalEVAfemale', 'kerbalEVAfemaleFuture', 'kerbalEVAfemaleVintage'
	]),
	'Aero': set([
		'FanShroud_01', 'FanShroud_02', 'FanShroud_03', 'largeFanBlade', 'largeHeliBlade', 'largePropeller', 'mediumFanBlade', 'mediumHeliBlade', 'mediumPropeller', 'noseconeTiny'
		'noseconeVS', 'smallFanBlade', 'smallHeliBlade', 'smallPropeller'
	]),
	'Cargo': set([
		'DeployedCentralStation', 'DeployedGoExOb', 'DeployedIONExp', 'DeployedRTG', 'DeployedSatDish', 'DeployedSeismicSensor', 'DeployedSolarPanel', 'DeployedWeatherStn', 'cargoContainer', 'smallCargoContainer'
	]),
	'Robotics': set([
		'RotorEngine_02', 'RotorEngine_03', 'controller1000', 'hinge_01', 'hinge_01_s', 'hinge_03', 'hinge_03_s', 'hinge_04', 'piston_01', 'piston_02'
		'piston_03', 'piston_04', 'rotoServo_00', 'rotoServo_02', 'rotoServo_03', 'rotoServo_04', 'rotor_01', 'rotor_01s', 'rotor_02', 'rotor_02s'
		'rotor_03', 'rotor_03s'
	]),
	'Science': set([
		'RobotArmScanner_S1', 'RobotArmScanner_S2', 'RobotArmScanner_S3'
	]),
	'Structural': set([
		'lGripPad', 'lGripStrip', 'mGripPad', 'sGripPad', 'sGripStrip'
	]),
}

from itertools import chain
PARTS = set(chain.from_iterable(PARTS_BY_CATEGORY.values()))

